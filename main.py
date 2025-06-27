import telebot
import random
import datetime

# Replace this with your real token
API_KEY = "7582321947:AAF6YHg_WN-6lVolrJ97EnssQoXOr-bRarg"

bot = telebot.TeleBot(API_KEY)

# ==== Prediction logic ====
def predict_crypto(symbol):
    trend = random.choice(["bullish", "bearish", "sideways"])
    change = round(random.uniform(0.5, 5), 2)
    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")

    if trend == "bullish":
        text = f"📈 *{symbol} is looking bullish!* 🔥\nExpected rise: +{change}%"
    elif trend == "bearish":
        text = f"📉 *{symbol} might dip soon!* ❄️\nExpected drop: -{change}%"
    else:
        text = f"⏸ *{symbol} is likely to move sideways.*\nExpected change: ±{change}%"

    return f"🕒 *{time}*\n\n{text}\n\n_Note: This is a prediction for the next 24 hours._"

# ==== Commands ====
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to *Probo Predictor Bot*!\n\nAvailable commands:\n/btc - Predict Bitcoin\n/usdt - Predict Tether (USDT)\n/ask <your question> - General advice or fun response\n/help - Show this menu again", parse_mode="Markdown")

@bot.message_handler(commands=['btc'])
def btc_prediction(message):
    response = predict_crypto("Bitcoin (BTC)")
    bot.send_message(message.chat.id, response, parse_mode="Markdown")

@bot.message_handler(commands=['usdt'])
def usdt_prediction(message):
    response = predict_crypto("Tether (USDT)")
    bot.send_message(message.chat.id, response, parse_mode="Markdown")

@bot.message_handler(commands=['ask'])
def ask_google_like(message):
    query = message.text.replace("/ask", "").strip()
    if not query:
        bot.reply_to(message, "❓ Please ask something like:\n/ask Will BTC go up today?")
    else:
        answers = [
            f"I think '{query}' needs a bit more data, but I’d say maybe!",
            f"Interesting question: '{query}' 🤔\nLet me guess... yes!",
            f"'{query}'? Hmm... Looks like a strong *yes*!",
            f"'{query}' – Too early to tell. Stay tuned!"
        ]
        bot.reply_to(message, random.choice(answers), parse_mode="Markdown")

# ==== Fallback for random messages ====
@bot.message_handler(func=lambda message: True)
def default_reply(message):
    bot.reply_to(message, "Use /btc or /usdt to get crypto predictions.\nTry /help to see all commands.")

# ==== Start polling ====
print("Bot is running...")
bot.infinity_polling()