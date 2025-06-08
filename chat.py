# CryptoBuddy Chatbot
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def crypto_buddy():
    print("👋 Hey there! I'm CryptoBuddy, your guide to crypto investing! 🚀")
    print("Ask me about trending cryptos, sustainable coins, or long-term picks!")
    print("Type 'exit' to quit. ⚠️ Disclaimer: Crypto is risky—do your own research!")

    while True:
        user_query = input("\nWhat do you want to know? ").lower()

        if user_query == "exit":
            print("👋 Thanks for chatting with CryptoBuddy! Stay savvy! 😎")
            break

        # Query handling for trending cryptocurrencies
        if "trend" in user_query or "trending" in user_query or "profitable" in user_query:
            trending_coins = [
                coin for coin, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]
            ]
            if trending_coins:
                print(f"📈 Hot picks for profitability: {', '.join(trending_coins)}! These coins are trending up with solid market caps!")
            else:
                print("🤔 No trending coins match your criteria right now.")

        # Query handling for sustainable cryptocurrencies
        elif "sustainable" in user_query or "eco-friendly" in user_query:
            sustainable_coin = max(
                crypto_db, key=lambda x: crypto_db[x]["sustainability_score"]
            )
            if crypto_db[sustainable_coin]["sustainability_score"] > 7/10:
                print(f"🌱 {sustainable_coin} is the most sustainable with a score of {crypto_db[sustainable_coin]['sustainability_score']*10}/10 and low energy use!")
            else:
                print(f"🌿 {sustainable_coin} is the best for sustainability, but its score is only {crypto_db[sustainable_coin]['sustainability_score']*10}/10.")

        # Query handling for long-term growth
        elif "long-term" in user_query or "growth" in user_query:
            long_term_coins = [
                coin for coin, data in crypto_db.items()
                if data["price_trend"] == "rising" and data["sustainability_score"] > 7/10
            ]
            if long_term_coins:
                print(f"🚀 For long-term growth, I recommend: {', '.join(long_term_coins)}! They’re trending up and eco-friendly!")
            else:
                print("🤔 No coins match both rising trends and high sustainability right now.")

        # Fallback for unrecognized queries
        else:
            print("🤔 Hmm, I didn’t catch that. Try asking about 'trending', 'sustainable', or 'long-term' cryptos!")

# Run the chatbot
crypto_buddy()