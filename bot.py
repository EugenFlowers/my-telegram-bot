import os
from telegram.ext import Application, CommandHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    print("❌ Добавьте BOT_TOKEN в Bothost.ru")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Открыть NetAngels", url="https://t.me/netangels_app_bot/netangels")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "💎 Тарифы NetAngels:\n"
        "• Базовый — 490₽/мес\n"
        "• Стандарт — 990₽/мес\n"
        "• Премиум — 1990₽/мес\n\n"
        "Выберите тариф в приложении 👇",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()




