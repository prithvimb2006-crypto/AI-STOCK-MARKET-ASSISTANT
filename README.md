# AI Stock Market Assistant 🚀

An AI-powered stock analysis assistant built using Python and OpenAI.

This project fetches real-time stock market data, calculates technical indicators like Moving Average and RSI, and uses an LLM to generate intelligent stock insights.

---

## 🔥 Features

- Fetches live stock data using yFinance
- Calculates 50-day Moving Average
- Computes 14-day RSI (Relative Strength Index)
- Uses OpenAI API for natural-language analysis
- Secure API key handling using environment variables

---

## 🧠 How It Works

1. User enters a stock symbol (e.g., AAPL)
2. Python fetches real market data
3. Technical indicators are calculated using Pandas
4. Data is sent to OpenAI model
5. Model returns a human-readable stock analysis

This architecture ensures:
- Accurate mathematical calculations (handled by Python)
- Smart interpretation (handled by LLM)

---

## 🛠 Tech Stack

- Python
- OpenAI API
- Pandas
- yFinance
- dotenv
- Git & GitHub

---

## 🔐 Security

API keys are stored securely using a `.env` file and are not pushed to GitHub.

---

## 🚀 How To Run

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

   pip install -r requirements.txt

4. Create a `.env` file and add your OpenAI API key:

   OPENAI_API_KEY=your_key_here

5. Run:

   python main.py

---

## 📌 Future Improvements

- Add MACD indicator
- Add Bollinger Bands
- Build Streamlit web UI
- Add portfolio analysis
- Deploy as web app

---

## 👨‍💻 Author

Prithvi Halder
