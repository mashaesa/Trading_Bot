# Trading Bot Project

## Introduction

This project represents my journey in developing an automated trading bot designed to interact with cryptocurrency exchanges through APIs. The bot aims to streamline processes by leveraging Python and the WOOX API to fetch market data, analyse trends, and execute trades automatically. The ultimate goal is to build a robust, scalable, and efficient system capable of supporting algorithmic trading strategies across various markets.

The bot operates based on the following key components:

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
   - The maximum capital per trade is capped at $1000.
   - Stop-loss levels are strictly enforced.
5. **Notifications**:
   - Email alerts are sent upon executing a trade.
6. **Logging and Analytics**:
   - Detailed logs are saved for performance review.
   - Graphs and reports summarise daily profit/loss and strategy performance.

## Technical Deep Dive

To understand the in-depth technical implementation, the tools and libraries used, and the data science concepts behind the bot, visit:

👉 [Technical Overview](technical_overview/README.md)

---

## Future Plans

I plan to evolve this bot in the following ways:

1. **Backtesting and Optimisation**:
   - Integrate a robust backtesting framework to test the strategy on historical data.
   - Fine-tune the parameters of indicators to optimise performance.

2. **Machine Learning**:
   - Introduce predictive models using TensorFlow to analyse trends and improve decision-making.
   - Explore reinforcement learning for dynamic strategy adaptation.

3. **Hosting**:
   - Deploy the bot on Azure using Docker for scalability and reliability.
   - Optimise deployment to reduce latency by selecting servers close to the WOOX exchange.

4. **Database Integration**:
   - Implement PostgreSQL to store trade history, backtesting results, and performance logs.
   - Use Neo4j to map relationships between indicators and trade outcomes.

5. **TradingView Integration**:
   - Set up TradingView alerts and webhook integration to enhance signal accuracy.

6. **Multi-Token Support**:
   - Expand the bot’s capabilities to analyse and trade multiple tokens simultaneously.

---

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
## Strategy and Implementation Plan

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

### Automation Preferences

1. **Exchange Integration:**
   - Platform: WOOX exchange.
   - Order type: Market orders.

2. **Backtesting and Alerts:**
   - Historical data: Past one year with 1-hour, 15-minute, 5-minute, and 30-minute intervals.

3. **Hosting & Deployment:**
   - Platform: Azure, with Docker for containerisation.
   - Deployment region: US-East or Europe for optimal latency.

4. **Logging & Analytics:**
   - Logs: CSV format.
   - Analytics: Daily profit/loss summaries and performance reports visualised with Matplotlib and Plotly.

### Technical Enhancements

1. **Machine Learning Integration:**
   - Use cases: Price trend prediction and volatility analysis.
   - Libraries: TensorFlow, PyTorch, or Scikit-learn (as appropriate).

2. **Database Setup:**
   - Database: PostgreSQL for scalability.
   - Tables: Trade history, backtesting results, and performance logs.

3. **Additional Tools:**
   - Integration with TradingView alerts and Neo4j for relationship mapping.

### Implementation Plan

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

This section outlines the systematic approach to developing a highly functional trading bot, incorporating advanced analytics and automation for market behaviour learning and optimisation.

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

The current code is foundational for:
- **Data Retrieval:** The `fetch_trade_history` function provides access to historical trading data, which is essential for backtesting strategies and understanding market behaviour.
- **Authentication Workflow:** The implementation of secure API authentication sets the groundwork for other bot functionalities, such as placing orders or monitoring account balances.
- **Scalable Design:** Modular functions make it easy to expand and integrate additional features like real-time data fetching, order placement, and portfolio management.

## Code Demonstration and Output

### Code Overview

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

#### Parsed Output (Sample Rows):
| Trade ID     | Symbol          | Side | Executed Price | Quantity | Fee   | Fee Asset |
|--------------|-----------------|------|----------------|----------|-------|-----------|
| 1391018966  | PERP_POWR_USDT  | SELL | 0.3405         | 710      | 0.120 | USDT      |
| 1391018965  | PERP_POWR_USDT  | SELL | 0.3406         | 856      | 0.145 | USDT      |
| 1391018964  | PERP_POWR_USDT  | SELL | 0.3406         | 3506     | 0.597 | USDT      |

### Explanation:
1. **Request Debugging:** Debugging information ensures the request is constructed correctly and helps trace issues.
2. **Response Content:** The JSON response includes metadata (e.g., total records and pagination) and trade data such as executed price, quantity, and fees.
3. **Parsed Data:** The parsed table highlights key fields, making it easier to visualise the trade history.

### Significant Milestone: Fetching Data for Multiple Tokens

#### Description:
Building upon the initial functionality, the project has been extended to:
1. Retrieve historical trade data for multiple cryptocurrency tokens dynamically.
2. Save the trade data for each token in a separate `.csv` file.
3. Combine all retrieved data into a single `.csv` file for comprehensive analysis.

This implementation demonstrates scalability and prepares the system for broader market analysis and strategy development.

#### Key Features of the Code:
- **Dynamic Token Handling:** Automatically fetches data for a list of predefined tokens.
- **Pagination:** Retrieves complete historical data by iterating through multiple pages of API responses.
- **Export to CSV:** Exports both individual token data and aggregated data for easy analysis.

#### Code Preview:
```python
import time
import pandas as pd
import os
import requests
import hashlib
import hmac
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WOOX_API_KEY")
API_SECRET = os.getenv("WOOX_API_SECRET")

# List of tokens
tokens = [
    "LDO", "POPCAT", "JTO", "CHZ", "TAO", "ATOM", "NEAR", "SUNDOG", "MEW",
    "1000BONK", "BOME", "ID", "MOODENG", "BSV", "UXLINK", "SUIU", "LQTY",
    "GOAT", "GMT", "WU", "MERL", "ZRX", "RSR", "ORDER", "BIGTIME", "CKB",
    "ONDO", "WIF", "VET", "CRV"
]
symbols = [f"PERP_{token}_USDT" for token in tokens]

# Fetch data for all tokens
all_data = []
start_time = str(int((time.time() - 180 * 24 * 60 * 60) * 1000))  # 180 days ago
end_time = str(int(time.time() * 1000))  # Current timestamp

def fetch_trade_history(symbol, start_time, end_time, page=1, size=100):
    base_url = "https://api.woox.io/v1/client/trades"
    query_params = {
        "symbol": symbol,
        "start_t": start_time,
        "end_t": end_time,
        "page": page,
        "size": size
    }
    query_string = "&".join(f"{key}={value}" for key, value in sorted(query_params.items()))
    timestamp = str(int(time.time() * 1000))
    content_to_sign = f"{query_string}|{timestamp}"
    signature = hmac.new(
        API_SECRET.encode('utf-8'),
        content_to_sign.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    headers = {
        "x-api-key": API_KEY,
        "x-api-signature": signature,
        "x-api-timestamp": timestamp,
        "Content-Type": "application/json"
    }
    response = requests.get(base_url, headers=headers, params=query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
        return None

for symbol in symbols:
    print(f"Fetching data for {symbol}...")
    current_page = 1
    token_data = []
    while True:
        result = fetch_trade_history(symbol, start_time, end_time, page=current_page, size=100)
        if result and result.get("rows"):
            token_data.extend(result["rows"])
            current_page += 1
            if len(result["rows"]) < 100:  # No more pages
                break
        else:
            break
    if token_data:
        all_data.extend(token_data)
        # Save token-specific data
        df_token = pd.DataFrame(token_data)
        df_token.to_csv(f"{symbol}_trade_history.csv", index=False)
        print(f"Saved data for {symbol} to {symbol}_trade_history.csv.")

# Save all combined data
if all_data:
    df_all = pd.DataFrame(all_data)
    df_all.to_csv("all_trade_history.csv", index=False)
    print("Saved all token data to all_trade_history.csv.")
else:
    print("No data retrieved for any tokens.")
```

### Significance:
This step enables the trading bot to:
1. Analyse trends across multiple tokens, broadening its analytical scope.
2. Use the exported data for advanced strategy development.
3. Prepare for scalability by handling large datasets and multiple markets efficiently.

### Next Steps:
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

1. **Enhance API Functionality:**
   - Add support for fetching live market data and placing trades.
   - Implement features to handle multiple currency pairs dynamically.

2. **Integrate Strategy Logic:**
   - Begin incorporating simple trading strategies for backtesting using the fetched data.

3. **Optimise Performance:**
   - Reduce latency in API calls and improve error handling.

4. **Documentation and Testing:**
   - Document the API workflow and write unit tests to ensure code reliability.

5. **Real-Time Trading:**
   - Develop event-driven mechanisms for real-time market analysis and trade execution.

## Conclusion

This project is an ongoing exploration of algorithmic trading. It combines my passion for technology and financial markets, leveraging Python and industry-standard tools to create a professional-grade trading bot. The repository will be regularly updated as I progress in implementing new features and optimising the bot for real-world usage.


