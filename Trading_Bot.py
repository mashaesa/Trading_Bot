import time
import pandas as pd
import os
import requests
import hashlib
import hmac
import logging
from dotenv import load_dotenv

# load all the API keys from env file
load_dotenv()
API_KEY = os.getenv("WOOX_API_KEY")
API_SECRET = os.getenv("WOOX_API_SECRET")

# Set up logging
logging.basicConfig(level=logging.INFO, filename="trading_bot.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Retry function for fetching candles
def fetch_candles(symbol, interval, limit=500, retries=3, delay=5):
    """
    Fetch historical candle data from WOOX API with retries
    """
    url = "https://api.woox.io/v1/market/candles"
    timestamp = str(int(time.time() * 1000))

    query_params = {
        "symbol": symbol,
        "timeframe": interval,
        "limit": limit
    }
    query_string = "&".join(f"{key}={value}" for key, value in query_params.items())
    signature_payload = f"{query_string}|{timestamp}".encode("utf-8")
    signature = hmac.new(API_SECRET.encode("utf-8"), signature_payload, hashlib.sha256).hexdigest()

    headers = {
        "x-api-key": API_KEY,
        "x-api-signature": signature,
        "x-api-timestamp": timestamp,
        "Content-Type": "application/json",
    }

    for attempt in range(retries):
        response = requests.get(url, headers=headers, params=query_params)
        if response.status_code == 200:
            data = response.json()
            if "rows" in data and data["rows"]:
                df = pd.DataFrame(data["rows"], columns=["timestamp", "open", "high", "low", "close", "volume"])
                df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
                return df
            else:
                logging.warning(f"No data returned for {symbol} with interval {interval}.")
                return None
        else:
            logging.error(f"Failed to fetch candles for {symbol} with interval {interval}, attempt {attempt + 1}.")
            logging.error(f"Status Code: {response.status_code}, Response: {response.content}")
            time.sleep(delay)

    logging.error(f"Failed to fetch candles for {symbol} after {retries} attempts.")
    return None


# Stoch RSI Calculation
def stochastic_rsi(data, k_period=3, d_period=3, rsi_length=14, stochastic_length=14, column="close"):
    """
    Calculate the Stochastic RSI indicator.
    """
    if data is None:
        logging.warning("No data provided to stochastic_rsi.")
        return None

    delta = data[column].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=rsi_length).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_length).mean()
    rs = gain / loss
    data["rsi"] = 100 - (100 / (1 + rs))

    rsi_min = data["rsi"].rolling(window=stochastic_length).min()
    rsi_max = data["rsi"].rolling(window=stochastic_length).max()
    data["stoch_rsi"] = (data["rsi"] - rsi_min) / (rsi_max - rsi_min)
    data["k"] = data["stoch_rsi"].rolling(window=k_period).mean()
    data["d"] = data["k"].rolling(window=d_period).mean()

    return data


# Define the trading logic
def check_entry_conditions(candles_1h, candles_15m, candles_5m):
    """
    Check if conditions for entering a trade met
    """
    try:
        if candles_1h["k"].iloc[-1] < 20 and candles_15m["k"].iloc[-1] < 20 and candles_5m["k"].iloc[-1] < 20:
            return True
    except Exception as e:
        logging.error(f"Error checking entry conditions: {e}")
    return False


def execute_trade(symbol, side, amount):
    """
    Simulate executing a trade (to be replaced with actual trading logic).
    """
    logging.info(f"Executing trade: {side} {amount} {symbol}")
    print(f"Trade executed: {side} {amount} {symbol}")


# Main Bots Logic
def run_bot():
    symbol = "PERP_LDO_USDT"  # Replace with desired symbol
    candles_1h = fetch_candles(symbol, "1h")
    candles_15m = fetch_candles(symbol, "15m")
    candles_5m = fetch_candles(symbol, "5m")

    if candles_1h is None or candles_15m is None or candles_5m is None:
        logging.warning(f"Skipping trading for {symbol} due to missing data.")
        return

    # indicators
    candles_1h = stochastic_rsi(candles_1h, k_period=3, d_period=3, rsi_length=14, stochastic_length=14)
    candles_15m = stochastic_rsi(candles_15m, k_period=3, d_period=3, rsi_length=14, stochastic_length=14)
    candles_5m = stochastic_rsi(candles_5m, k_period=3, d_period=3, rsi_length=14, stochastic_length=14)

    # Check and execute the trade!!! :D
    if check_entry_conditions(candles_1h, candles_15m, candles_5m):
        execute_trade(symbol, "BUY", 1000)  # Example trade
    else:
        logging.info(f"No entry conditions met for {symbol}.")


# Run the bot
if __name__ == "__main__":
    run_bot()
