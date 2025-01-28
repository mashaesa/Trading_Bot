# Trading Bot Project

## Introduction

This project represents my journey in developing an automated trading bot designed to interact with cryptocurrency exchanges through APIs. The bot aims to streamline processes by leveraging Python and the WOOX API to fetch market data, analyse trends, and execute trades automatically. The ultimate goal is to build a scalable, and efficient system capable of supporting algorithmic trading strategies across various markets.

## Initial Ideas

![Blueprint for Trading Bot](https://raw.githubusercontent.com/mashaesa/-Trading_Bot/main/Untitled-2025-01-26-1337.png)

The bot operates based on the following components:

### Features
1. **Automated Data Retrieval**: The bot fetches trade history and candlestick data for tokens listed on WOOX, enabling dynamic and real-time decision-making.
2. **Indicators**:
   - Stochastic RSI
   - Slow Stochastic (two variations)
   - Supertrend Indicator
   - Exponential Moving Averages (EMA)
   - Moving Averages (MA)
3. **Entry and Exit Logic**:
   - The bot evaluates conditions across multiple timeframes (1-hour, 15-minute, and 5-minute) to ensure robust entries.
   - Trades are exited when a 2.5% profit or loss is achieved.
4. **Risk Management**:
   - The max capital per trade is capped at $1000.
   - Stoploss levels are strictly enforced.
5. **Notifications**: (in progress)
   - Email alerts are sent upon executing a trade.
6. **Logging and Analytics**: 
   - Detailed logs are saved for performance review.
   - Graphs and reports summarise daily profit/loss and strategy performance.

---

## Technical Deep Dive

This document provides a deep dive into the data science concepts, programming tools, and overall architecture of the trading bot.

### Strategy Details

1. **Trading Style:**
   - Day trading with a focus on cryptocurrencies.

2. **Indicators & Technical Analysis:**
   - **Candlestick Patterns:** Used as part of trade confirmation.
   - **Stochastic RSI:** Multiple settings for fine-tuned analysis:
     - K: 3, D: 3, RSI Length: 5, Stochastic Length: 5.
     - K: 3, D: 3, RSI Length: 8, Stochastic Length: 8.
   - **Slow Stochastics:**
     - SmoothK: 14, SmoothD: 3.
     - SmoothK: 8, SmoothD: 3.
   - **Supertrend Indicator:**
     - ATR Period: 11, Source: HL2, ATR Multiplier: 2, Timeframe: Chart.
   - **Moving Averages:**
     - Exponential Moving Averages (EMAs): 11, 26, 100, 200, 300, 400.
     - Standard Moving Averages (MAs): 25, 39, 50, 200.

3. **Entry & Exit Criteria:**
   - **Entry Trigger:**
     - Hourly chart: All Stochastic RSI and Slow Stochastics align at 20.
     - 15-minute and 5-minute charts: Same alignment.
     - Confirmation: A green candle closes on the 5-minute chart after alignment.
   - **Exit Trigger:**
     - Trade achieves a 2.5% profit or incurs a 2.5% loss.

4. **Risk Management:**
   - Maximum capital per trade: $1,000.
   - Risk-to-reward ratio: 2.5% stop-loss and profit target.

5. **Timeframe and Trading Hours:**
   - Timeframes: 1-hour, 15-minute, and 5-minute charts.
   - Trading frequency: One trade per day.

---

### 1. Stochastic RSI
The **Stochastic RSI** combines the relative strength index (RSI) and stochastic oscillator to identify overbought and oversold conditions:
- **Purpose**: Detect momentum shifts in price action.
- **Implementation**:
  - Calculate RSI over a defined period.
  - Identify the highest and lowest RSI values within a rolling window.
  - Compute the stochastic oscillator of the RSI values.

### 2. Slow Stochastic
The **Slow Stochastic** smooths the regular stochastic oscillator:
- **Purpose**: Mitigate noise and provide clearer trend signals.
- **Implementation**:
  - Smooth `%K` (raw stochastic) with a simple moving average.
  - Smooth `%D` (signal line) over a shorter period.

### 3. Supertrend Indicator
The **Supertrend Indicator** highlights market trends based on average true range (ATR):
- **Purpose**: Identify potential trend reversals.
- **Implementation**:
  - Compute ATR for price volatility.
  - Create upper and lower bands based on ATR and price movement.

### 4. Moving Averages (MA & EMA)
- **Moving Averages (MA)** smooth historical prices over a defined window to reduce noise.
- **Exponential Moving Averages (EMA)** assign greater weight to recent prices to react faster to price changes.

---

## Programming Tools and Libraries

### 1. Python
The core language for this project due to its:
- Robust libraries for data manipulation (e.g., Pandas).
- Ease of integrating APIs.
- Extensive community support for algorithmic trading.

### 2. Libraries Used
#### a. **Pandas**
- **Purpose**: Data manipulation and analysis.
- **Use Cases**:
  - Cleaning and structuring API response data.
  - Calculating technical indicators.

#### b. **Matplotlib**
- **Purpose**: Data visualisation.
- **Use Cases**:
  - Plotting profit/loss summaries.
  - Visualising trade history and market trends.

#### c. **HMAC & hashlib**
- **Purpose**: Securely sign API requests.
- **Use Cases**:
  - Generate cryptographic signatures for authenticating WOOX API calls.

#### d. **Dotenv**
- **Purpose**: Manage sensitive credentials.
- **Use Cases**:
  - Load API keys and email credentials from a `.env` file.

#### e. **Requests**
- **Purpose**: HTTP requests to interact with APIs.
- **Use Cases**:
  - Fetch market data.
  - Execute trades.

---

## Design

### Workflow
1. **Data Retrieval**:
   - Fetch historical trade data and candlestick patterns using the WOOX API.
   - Ensure data consistency through retries and error handling.

2. **Indicator Calculation**:
   - Apply Stochastic RSI, Slow Stochastic, Supertrend, and MAs to the data.
   - Align indicators across multiple timeframes for robust trade decisions.

3. **Trade Execution**:
   - Evaluate entry and exit criteria.
   - Execute trades via API with a predefined risk cap.

4. **Notifications**:
   - Send trade execution details via email for transparency.

5. **Logging and Analytics**:
   - Log trade details for performance evaluation.
   - Generate visual reports for profit/loss analysis.

---

## Milestones

1. **Secure API Integration**:
   - HMAC-SHA256 signatures ensure secure and authenticated API calls.
2. **Error Handling**:
   - Managed API failures with retries and graceful exits.
3. **Multi-Token Data Retrieval**:
   - Scaled data collection for 30+ tokens simultaneously.

---

### Automation

1. **Exchange Integration:**
   - Platform: WOOX exchange.
   - Order type: Market orders.

2. **Backtesting and Alerts:**
   - Historical data: Past one year with 1-hour, 15-minute, 5-minute, and 30-minute intervals.

3. **Hosting & Deployment:** (in progress)
   - Platform: Azure, with Docker for containerisation.
   - Deployment region: US-East or Europe for optimal latency.

4. **Logging & Analytics:**
   - Logs: CSV format.
   - Analytics: Daily profit/loss summaries and performance reports visualised with Matplotlib and Plotly.

### The Plan

1. **Trading Logic:**
   - Encode trade entry conditions (stochastic RSI and slow stochastic alignment).
   - Include additional filters such as candlestick confirmations.

2. **Exchange API Integration:**
   - Authenticate using WOOX API credentials.
   - Target USDT trading pairs with a 10% increase in the last 24 hours.

3. **Backtesting Module:**
   - Fetch and analyse historical data to calculate win/loss ratios.

4. **Notifications:**
   - Send email alerts summarising trades and profit/loss updates.

5. **Deployment:**
   - Host on Azure with Docker for streamlined deployment.

6. **Logging & Analytics:**
   - Generate daily logs and analytics reports for strategy evaluation.

7. **Machine Learning:**
   - Build predictive models for trend and volatility analysis.
   - Generate datasets from historical trades for training and testing.

## Current Progress

### Functionality Implemented:

1. **Environment Configuration:**
   - Utilised the `dotenv` library to securely manage API keys and secrets in a `.env` file, ensuring sensitive information is not exposed in the codebase.

2. **Timestamp Generation:**
   - Created a function to generate a 13-digit Unix timestamp (in milliseconds) for API request signing and synchronisation with the exchange server.

3. **HMAC-SHA256 Signature Creation:**
   - Developed a function to generate secure signatures using the API secret, ensuring integrity and authenticity of API requests.

4. **Fetching Trade History:**
   - Implemented an API call to fetch historical trade data from the exchange for a specified time range.
   - Integrated query parameter construction, signature generation, and HTTP headers setup to comply with the exchange’s API requirements.

5. **Debugging and Error Handling:**
   - Added print statements to debug the request flow (e.g., query strings, headers, and signature details).
   - Included exception handling to manage HTTP request errors gracefully.

### Code Use in Bot Development

#### Purpose of the Code:
The script demonstrates the process of securely fetching trade history from a cryptocurrency exchange using its API. It includes:
1. **Environment Configuration:** Securely loading API keys from a `.env` file.
2. **API Authentication:** Generating HMAC-SHA256 signatures for secure requests.
3. **Data Retrieval:** Fetching trade history for a specific symbol over a specified time range.

#### Key Components:
- **`get_timestamp`:** Generates a Unix timestamp in milliseconds to synchronise with the API.
- **`create_signature`:** Generates a cryptographic signature for API requests using the secret key and payload.
- **`fetch_trade_history`:** Sends a GET request to fetch trade history, building the query string, headers, and signature dynamically.

### Sample Output

#### Request Debugging:
```plaintext
Request URL: https://api.woox.io/v1/client/trades
Headers: {
  'x-api-key': '...',
  'x-api-signature': '...',
  'x-api-timestamp': '...',
  'Content-Type': 'application/json'
}
Query String: end_t=1737065089590&page=1&size=25&start_t=1729289089590&symbol=PERP_POWR_USDT
```

#### Response:
```plaintext
Response Status Code: 200
Response Content: {
  "success": true,
  "meta": {"total": 25, "records_per_page": 100, "current_page": 1},
  "rows": [
    {"id": 1391018966, "symbol": "PERP_POWR_USDT", "side": "SELL", ...},
    {"id": 1391018965, "symbol": "PERP_POWR_USDT", "side": "SELL", ...},
    ...
  ]
}
```

#### Output (Sample Rows):
| Trade ID     | Symbol          | Side | Executed Price | Quantity | Fee   | Fee Asset |
|--------------|-----------------|------|----------------|----------|-------|-----------|
| 1391018966  | PERP_POWR_USDT  | SELL | 0.3405         | 710      | 0.120 | USDT      |
| 1391018965  | PERP_POWR_USDT  | SELL | 0.3406         | 856      | 0.145 | USDT      |
| 1391018964  | PERP_POWR_USDT  | SELL | 0.3406         | 3506     | 0.597 | USDT      |

1. **Request Debugging:** Debugging information ensures the request is constructed correctly and helps trace issues.
2. **Response Content:** The JSON response includes metadata (e.g., total records and pagination) and trade data such as executed price, quantity, and fees.
3. **Parsed Data:** The parsed table highlights key fields, making it easier to visualise the trade history.

### Fetching Data for Multiple Tokens

Building upon the initial functionality, the project has been extended to:
1. Retrieve historical trade data for multiple cryptocurrency tokens dynamically.
2. Save the trade data for each token in a separate `.csv` file.
3. Combine all retrieved data into a single `.csv` file for comprehensive analysis.

This implementation demonstrates scalability and prepares the system for broader market analysis and strategy development.

#### Features of the Code:
- **Dynamic Token Handling:** Automatically fetches data for a list of predefined tokens.
- **Pagination:** Retrieves complete historical data by iterating through multiple pages of API responses.
- **Export to CSV:** Exports both individual token data and aggregated data for easy analysis.

#### Preview:
```python
import time
import pandas as pd
import os
import requests
import hashlib
import hmac
import logging
import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import asyncio
import aiohttp

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WOOX_API_KEY")
API_SECRET = os.getenv("WOOX_API_SECRET")
DB_CONNECTION = os.getenv("DB_CONNECTION")

# Set logging
logging.basicConfig(level=logging.INFO, filename="trading_bot.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

plt.style.use("dark_background")

# Database connection setup
def connect_to_db():
    """
    Establish connection to PostgreSQL database.
    """
    return psycopg2.connect(DB_CONNECTION)

# Asynch fetch for candle data
async def fetch_candles_async(symbol, interval, limit=500):
    """
    Asynchronously fetch historical candle data from WOOX API.
    """
    base_url = "https://api.woox.io/v1/market/candles"
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

    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, headers=headers, params=query_params) as response:
            if response.status == 200:
                data = await response.json()
                if "rows" in data and data["rows"]:
                    df = pd.DataFrame(data["rows"], columns=["timestamp", "open", "high", "low", "close", "volume"])
                    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
                    return df
                else:
                    logging.warning(f"No data returned for {symbol} with interval {interval}.")
                    return None
            else:
                logging.error(f"Failed to fetch candles for {symbol} with interval {interval}. HTTP Status: {response.status}")
                return None


# Save data to PostgreSQL
def save_to_database(data, table_name):
    """
    Save DataFrame to PostgreSQL.
    """
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            timestamp TIMESTAMP,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume FLOAT
        )""")

        execute_values(cursor, f"INSERT INTO {table_name} (timestamp, open, high, low, close, volume) VALUES %s",
                       data.values.tolist())
        conn.commit()
        logging.info(f"Data saved to table {table_name}.")
    except Exception as e:
        logging.error(f"Failed to save data to database: {e}")
    finally:
        cursor.close()
        conn.close()


# Stoch RSI calculation :)
def stochastic_rsi(data, k_period=3, d_period=3, rsi_length=14, stochastic_length=14, column="close"):
    """
    Calculate the Stochastic RSI indicator.
    """
    delta = data[column].diff()
    gain = delta.where(delta > 0, 0).rolling(window=rsi_length).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=rsi_length).mean()
    rs = gain / loss
    data["rsi"] = 100 - (100 / (1 + rs))

    rsi_min = data["rsi"].rolling(window=stochastic_length).min()
    rsi_max = data["rsi"].rolling(window=stochastic_length).max()
    data["stoch_rsi"] = (data["rsi"] - rsi_min) / (rsi_max - rsi_min)
    data["k"] = data["stoch_rsi"].rolling(window=k_period).mean()
    data["d"] = data["k"].rolling(window=d_period).mean()

    return data


# Backtesting 
def backtest_strategy(data, entry_threshold=20, exit_threshold=80):
    """
    Simple backtesting logic using Stochastic RSI.
    """
    data = stochastic_rsi(data)
    balance = 1000  # Starting balance (USDT)
    position = 0    # Position size

    for i in range(1, len(data)):
        if data["k"].iloc[i] < entry_threshold and position == 0:
            # Enter position
            position = balance / data["close"].iloc[i]
            balance = 0
            logging.info(f"Entered position at {data['close'].iloc[i]} on {data['timestamp'].iloc[i]}.")

        elif data["k"].iloc[i] > exit_threshold and position > 0:
            # Exit position
            balance = position * data["close"].iloc[i]
            position = 0
            logging.info(f"Exited position at {data['close'].iloc[i]} on {data['timestamp'].iloc[i]}.")

    return balance


# Plot daily token volume
def plot_today_token_volume(data):
    """
    Plot today's token volume by hour.
    """
    today = pd.Timestamp("now").normalize()
    data_today = data[data["timestamp"].dt.date == today.date()]

    if data_today.empty:
        logging.warning("No data available for today's date.")
        return

    data_today["hour"] = data_today["timestamp"].dt.hour
    hourly_volume = data_today.groupby("hour")["volume"].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(hourly_volume.index, hourly_volume.values, marker="o", linestyle="-", color="magenta")
    plt.title("Today's Token Volume by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Total Token Volume")
    plt.grid()
    plt.savefig("todays_token_volume.png")
    plt.show()
    logging.info("Today's token volume graph saved as todays_token_volume.png.")


# Bot logic
async def run_bot():
    symbols = ["PERP_LDO_USDT", "PERP_ATOM_USDT"]  
    interval = "1h"
    all_results = []

    for symbol in symbols:
        candles = await fetch_candles_async(symbol, interval)
        if candles is not None:
            save_to_database(candles, symbol.replace("PERP_", ""))
            final_balance = backtest_strategy(candles)
            logging.info(f"Final balance after backtesting {symbol}: ${final_balance:.2f}")
            all_results.append((symbol, final_balance))
            plot_today_token_volume(candles)
    for symbol, balance in all_results:
        print(f"Symbol: {symbol}, Final Balance: ${balance:.2f}")


if __name__ == "__main__":
    asyncio.run(run_bot())
```

### Significance:
This step enables the trading bot to:
1. Analyse trends across multiple tokens, broadening its analytical scope.
2. Use the exported data for advanced strategy development.
3. Prepare for scalability by handling large datasets and multiple markets efficiently.

### Next Up:
1. Analyse the exported data for trends and correlations.
2. Incorporate technical indicators to evaluate market conditions.
3. Optimise the data-fetching process for better performance and reliability.

## Tools and Libraries Used

### Current Libraries:
1. **`time`:** For handling timestamps and scheduling tasks.
2. **`hmac` and `hashlib`:** To generate cryptographic signatures for secure API interactions.
3. **`requests`:** For making HTTP requests to the exchange API.
4. **`dotenv`:** For managing sensitive credentials in environment variables.
5. **`os`:** To retrieve environment variables securely.
6. **`pandas`:** For data manipulation and exporting to CSV files.

### Planned Libraries and Tools:
1. **TA-Lib (Technical Analysis Library):** For implementing advanced technical indicators (e.g., RSI, MACD) to enhance trading strategies.
2. **NumPy:** To perform numerical computations for custom indicators and strategy optimisation.
3. **Matplotlib/Plotly:** For visualising market trends, trade performance, and backtest results.
4. **Trading APIs:** Integration with other exchanges (e.g., Binance, Alpaca) to broaden market access.
5. **Websockets:** For real-time data streaming and event-driven decision-making.
6. **SQL or MongoDB:** To store and manage historical trade data and bot logs.
7. **Docker:** To containerise the bot for consistent deployment and scalability.
8. **Cloud Platforms (e.g., AWS, Azure):** To host the bot, ensuring high availability and efficient performance.

## Next Steps

**Enhance API Functionality:**
   - Add support for fetching live market data and placing trades.
   - Implement features to handle multiple currency pairs dynamically.

**Optimise Performance:**
   - Reduce latency in API calls and improve error handling.

**Documentation and Testing:**
   - Document the API workflow and write unit tests to ensure code reliability.

**Advanced Backtesting**:
   - Use historical data to simulate and refine trading strategies.
   - Evaluate win/loss ratios and strategy performance metrics.

**Real-Time Trading**:
   - Transition from historical analysis to live trading using WebSocket integrations.

**Machine Learning**:
   - Introduce trend prediction and volatility analysis models.
   - Explore reinforcement learning for adaptive strategies.

**Scalable Deployment**:
   - Deploy on Azure with Docker for reliability and low latency.

**Database Integration**:
   - Implement PostgreSQL to store trade history, backtesting results, and performance logs.
   - Use Neo4j to map relationships between indicators and trade outcomes.

---

## Conclusion

This project is an ongoing exploration of algorithmic trading. It combines my passion for technology and financial markets, leveraging Python and industry-standard tools to create a professional-grade trading bot. The repository will be regularly updated as I progress in implementing new features and optimising the bot for real-world usage.


