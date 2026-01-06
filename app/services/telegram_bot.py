import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# These should be in your .env file
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """The Legal Sentinel Intro triggered by /start"""
    intro_text = (
        "⚖️ **Welcome to LawSync Sentinel**\n\n"
        "I am your automated judicial monitor. I currently track portals in "
        "**Lagos, Abuja (FCT), and Oyo** to ensure you never miss a status change.\n\n"
        "🛡️ **How I help:**\n"
        "• **Real-time Monitoring:** I scan courts every morning at 6:00 AM.\n"
        "• **AI Extraction:** I turn messy court data into structured case summaries.\n"
        "• **Compliance:** I generate your **Section 84 Certificates** automatically.\n\n"
        "🚀 *Please enter a Suit Number (e.g., LD/1234/CIV/2024) to begin your first sync.*"
    )
    
    await update.message.reply_text(intro_text, parse_mode='Markdown')

def run_bot():
    """Starts the Telegram Bot listener"""
    application = Application.builder().token(TOKEN).build()
    
    # Register the /start command
    application.add_handler(CommandHandler("start", start))
    
    print("SENTINEL BOT IS LIVE...")
    application.run_polling()

if __name__ == "__main__":
    run_bot()