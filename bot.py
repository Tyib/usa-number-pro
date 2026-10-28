import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    ["🇺🇸 Get USA Number"],
    ["⚡ Temporary Number", "📅 Monthly Number"],
    ["📩 My SMS", "📱 My Numbers"],
    ["💰 My Balance", "🆘 Support"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇺🇸 Welcome to USA Number Pro!\n\n"
        "Choose an option below.\n"
        "Real numbers will be available after provider setup.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text
    responses = {
        "🇺🇸 Get USA Number": "Choose Temporary or Monthly Number.",
        "⚡ Temporary Number": "Temporary rentals will be available after provider setup.",
        "📅 Monthly Number": "Monthly rentals will be available after provider setup.",
        "📩 My SMS": "You have no active rentals yet.",
        "📱 My Numbers": "You have no active numbers yet.",
        "💰 My Balance": "Balance: 0.00",
        "🆘 Support": "Please contact the bot administrator for support.",
    }
    await update.message.reply_text(
        responses.get(choice, "Please select an option from the menu.")
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing from .env")

    app = (
        Application.builder()
        .token(TOKEN)
        .proxy(PROXY)
        .get_updates_proxy(PROXY)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu)
    )

    print("USA Number Pro is running through Tor!")
    app.run_polling()

if __name__ == "__main__":
    main()
