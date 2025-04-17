from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = '7812284701:AAHSrWNoMj20w7XnyETCuBkgsLS4Q4iEeLc'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello {update.effective_user.first_name}! I'm your bot 🤖")


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    
    app.add_handler(CommandHandler('start', start))

    print("Bot is running...")
    app.run_polling()
