import telebot

# Your bot token (keep this secret in production)
BOT_TOKEN = "7582321947:AAF6YHg_WN-6lVolrJ97EnssQoXOr-bRarg"

bot = telebot.TeleBot(BOT_TOKEN)

# Start and help command handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Probo Predictor Bot!\n\nSend me a prediction or ask a question!")

# Echo text handler
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"🤖 You said: {message.text}")

# Run the bot
print("🤖 Bot is live and polling for messages...")
bot.polling()