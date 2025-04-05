import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["5/5", "4/5"], ["3/5", "Qiyin bo‘ldi"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Assalomu alaykum, Umidjon Baxtiyorivich!\nBugungi kuningiz qanday o‘tdi?", reply_markup=reply_markup)

# Javoblar
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_response = update.message.text
    await update.message.reply_text(f"Javob qabul qilindi: {user_response}\nRahmat! Ertaga yana eslataman.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))
    print("[JARVIS] Bot ishga tushdi.")
    app.run_polling()
