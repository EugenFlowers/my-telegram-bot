import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    print("❌ Добавьте BOT_TOKEN в Bothost.ru")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data="btn1"),
            InlineKeyboardButton("Кнопка 2", callback_data="btn2")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('✅ Бот работает! Выберите кнопку:', reply_markup=reply_markup)[web:10][web:6]

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "btn1":
        await query.edit_message_text(text="Вы нажали Кнопка 1!")[web:10]
    elif query.data == "btn2":
        await query.edit_message_text(text="Вы нажали Кнопка 2!")[web:10]

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_callback))
app.run_polling()


