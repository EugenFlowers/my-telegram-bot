import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загрузка .env (локально)
load_dotenv()

# Токен из переменных окружения (Bothost или .env)
TOKEN = os.getenv('BOT_TOKEN')

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Добавьте в Bothost.ru > Переменные окружения")

logger.info(f"✅ Токен OK, длина: {len(TOKEN)}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик /start"""
    await update.message.reply_text('Привет! Бот работает на Bothost.ru ✅')

def main() -> None:
    """Запуск бота"""
    application = Application.builder().token(TOKEN).build()
    
    # Добавляем хендлер
    application.add_handler(CommandHandler("start", start))
    
    # Запуск
    logger.info("🚀 Бот запущен!")
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
