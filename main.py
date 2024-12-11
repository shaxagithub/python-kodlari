from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Salom! Men sodda suhbat botiman. Menga xabar yozing va javob beraman.")

# Xabarlarni qayta ishlovchi funksiya
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    if user_message.lower() in ["salom", "assalom alaykum"]:
        reply = "Va alaykum assalom! Qalaysiz?"
    elif user_message.lower() == "qalesan":
        reply = "Yaxshi, rahmat! Siz-chi?"
    else:
        reply = "Ajoyib xabar! 😊"
    
    await update.message.reply_text(reply)

# Botning asosiy funksiyasi
if __name__ == "__main__":
    # Tokenni o'rnating (Telegramdan olingan bot token)
    BOT_TOKEN = "7874746934:AAFrxEQLF44VNCHIrwgWSGIlA1e-QP46qzY"

    # Bot ilovasini yarating
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlerlarni qo'shing
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni ishga tushiring
    print("Bot ishlamoqda...")
    app.run_polling()
