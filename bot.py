
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = [
        [InlineKeyboardButton("📺 Watch on YouTube", url="https://www.youtube.com/@alogicadoprecoob")]
    ]
    reply_markup = InlineKeyboardMarkup(button)
    await update.message.reply_text("Welcome! Click the button below to watch 👇", reply_markup=reply_markup)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
