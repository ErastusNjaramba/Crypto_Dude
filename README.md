# Crypto_Dude Chatbot
Overview
Crypto Dude is a rule-based chatbot built in Python that provides cryptocurrency investment advice based on profitability (e.g., price trends, market cap) and sustainability (e.g., energy efficiency, project viability). It’s designed for beginners to learn about AI-driven decision-making, conversational logic, and basic data analysis. The chatbot uses a predefined dataset and simple if-else logic to respond to user queries like “Which crypto is trending?” or “What’s the most sustainable coin?”
Features

Friendly Personality: Engages users with a fun, approachable tone (e.g., “Let’s find you a crypto gem! 🚀”).
Profitability Analysis: Recommends coins with rising price trends and high/medium market caps.
Sustainability Focus: Prioritizes eco-friendly coins with low energy use and high sustainability scores.
Ethics Disclaimer: Warns users about the risks of cryptocurrency investing.
Extensible: Supports optional integration with CoinGecko API and NLTK for advanced functionality.

Prerequisites

Python: Version 3.6 or higher.
IDE: Visual Studio Code (recommended) or any Python-compatible editor.
Optional Libraries (for stretch goals):
pycoingecko for real-time crypto data.
nltk for natural language processing.



Installation

Set Up Python Environment:

Ensure Python is installed. Verify with:python --version


If not installed, download from python.org.


Clone or Download the Code:

Save the cryptobuddy.py file (provided below) to your project directory.


Optional Dependencies (for stretch goals):

Install pycoingecko for API integration:pip install pycoingecko


Install nltk for natural language processing:pip install nltk

Then, in Python, download NLTK data:import nltk
nltk.download('punkt')





Usage

Run the Chatbot:

Open your terminal or IDE and navigate to the project directory.
Run the script:python cryptobuddy.py




Interact with CryptoDude:

The chatbot will greet you and display a disclaimer:  👋 Hey there! I'm CryptoBuddy, your guide to crypto investing! 🚀
Ask me about trending cryptos, sustainable coins, or long-term picks!
Type 'exit' to quit. ⚠️ Disclaimer: Crypto is risky—do your own research!


Ask questions like:
“Which crypto is trending up?”
“What’s the most sustainable coin?”
“Which crypto should I buy for long-term growth?”


Type exit to quit.


Sample Interaction:
What do you want to know? Which crypto is trending up?
📈 Hot picks for profitability: Bitcoin, Cardano! These coins are trending up with solid market caps!

What do you want to know? What’s the most sustainable coin?
🌱 Cardano is the most sustainable with a score of 8.0/10 and low energy use!

What do you want to know? exit
👋 Thanks for chatting with CryptoDude! Stay savvy! 😎



Code Structure

File: cryptobuddy.py
Dataset: A dictionary (crypto_db) with predefined data for Bitcoin, Ethereum, and Cardano, including:
price_trend: “rising”, “stable”, or “falling”.
market_cap: “high”, “medium”, or “low”.
energy_use: “high”, “medium”, or “low”.
sustainability_score: A score out of 10.


Logic:
Uses if-else statements to match user queries (e.g., “trend”, “sustainable”) to dataset attributes.
Rules:
Profitability: Recommends coins with price_trend = "rising" and market_cap in (“high”, “medium”).
Sustainability: Recommends the coin with the highest sustainability_score, prioritizing scores > 7/10.
Long-term Growth: Combines rising trends and high sustainability scores (> 7/10).




Main Function: crypto_buddy() runs a loop to handle user input and generate responses.

Extending the Project
Stretch Goal 1: Real-Time Data with CoinGecko API

Replace the static dataset with live data using the pycoingecko library.
Example: Fetch Bitcoin’s price and market cap:from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
data = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=True)
print(f"Bitcoin Price: ${data['bitcoin']['usd']}")


Update the dataset dynamically and adjust logic to handle real-time trends.

Stretch Goal 2: Natural Language Processing with NLTK

Use NLTK to parse user queries more flexibly.
Example: Tokenize input to detect synonyms (e.g., “eco-friendly” for “sustainable”):import nltk
from nltk.tokenize import word_tokenize
def parse_query(query):
    tokens = word_tokenize(query.lower())
    return "sustainable" in tokens or "eco-friendly" in tokens


Install NLTK and download required data (see Installation).

Stretch Goal 3: Visualizations

Add a chart to display sustainability scores or price trends using matplotlib:pip install matplotlib

import matplotlib.pyplot as plt
coins = list(crypto_db.keys())
scores = [crypto_db[coin]["sustainability



