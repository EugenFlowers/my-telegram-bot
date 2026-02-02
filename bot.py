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
        [InlineKeyboardButton("VDS", callback_data="vds")],
        [InlineKeyboardButton("Хостинг", callback_data="hosting")],
        [InlineKeyboardButton("Домены", callback_data="domains")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "💎 Выберите услугу NetAngels:",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "back":
        # Возврат на стартовый экран
        keyboard = [
            [InlineKeyboardButton("VDS", callback_data="vds")],
            [InlineKeyboardButton("Хостинг", callback_data="hosting")],
            [InlineKeyboardButton("Домены", callback_data="domains")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "💎 Выберите услугу NetAngels:",
            reply_markup=reply_markup
        )
        return

    # Клавиатура для услуг: NetAngels + Назад
    netangels_keyboard = [
        [InlineKeyboardButton("Открыть NetAngels", url="https://t.me/netangels_app_bot/netangels")],
        [InlineKeyboardButton("◀️ Назад", callback_data="back")]
    ]

    if query.data == "vds":
        text = (
            "☁️ VDS от NetAngels\n\n"
            "• Надёжные VPS на NVMe-дисках\n"
            "• От 221₽/мес (Старт-1: 1 ядро, 0.5 ГБ RAM, 10 ГБ)\n"
            "• Защита от DDoS, бэкапы\n"
            "• KVM-виртуализация, Linux/Windows\n\n"
            "Подробнее в приложении:"
        )
    elif query.data == "hosting":
        text = (
            "🌐 Хостинг от NetAngels\n\n"
            "• Неограниченные сайты и БД\n"
            "• От 150₽/мес (Базовый)\n"
            "• SSL бесплатно, изоляция сайтов\n"
            "• Nginx+Apache, PHP/Python/NodeJS\n\n"
            "Подробнее в приложении:"
        )
    elif query.data == "domains":
        text = (
            "📛 Домены от NetAngels\n\n"
            "• .RU от 450₽/год\n"
            "• Быстрая регистрация\n"
            "• DNS-хостинг, делегирование\n"
            "• Поддержка всех зон (.com, .ru, .su)\n\n"
            "Подробнее в приложении:"
        )

    reply_markup = InlineKeyboardMarkup(netangels_keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_callback))
app.run_polling()

