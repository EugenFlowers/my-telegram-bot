import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

async def start(update, context):
    await update.message.reply_text('Привет! Бот работает.')

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler('start', start))
app.run_polling()
