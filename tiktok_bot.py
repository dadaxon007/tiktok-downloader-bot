import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔑 Tokeningizni bu yerga yozing
TOKEN = "7485352783:AAFQFlfbTXVorIItGl-FxW8qQ6ykfHs06SQ"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salom! Menga TikTok link yuboring, men videoni yuklab beraman 🎥")

async def download_tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    await update.message.reply_text("🔄 Video yuklanmoqda, biroz kuting...")

    try:
        api_url = "https://www.tikwm.com/api/"
        response = requests.post(api_url, data={"url": url})
        data = response.json()

        if data.get("data") and data["data"].get("play"):
            video_url = data["data"]["play"]
            await update.message.reply_video(video_url)
        else:
            await update.message.reply_text("❌ Xatolik yuz berdi. Iltimos, haqiqiy TikTok link yuboring.")
    except Exception as e:
        logging.error(e)
        await update.message.reply_text("⚠️ Video yuklashda muammo yuz berdi. Keyinroq urinib ko‘ring.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_tiktok))
    print("🤖 Bot ishga tushdi...")
    app.run_polling()
