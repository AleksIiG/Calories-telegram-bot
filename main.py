from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

import commands
from calories import handle_weight_input, handle_fat_input, handle_height_input, calories_counter, handle_gender_input, \
    handle_activity_input, handle_goal_input
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


BOT_USERNAME = 'CaloriesBot'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    if context.user_data.get('expecting') == 'weight':
        await handle_weight_input(update, context, text)


    elif context.user_data.get('expecting') == 'fat':
        await handle_fat_input(update, context, text)

    elif context.user_data.get('expecting') == 'height':
        await handle_height_input(update, context, text)


    else:
        await update.message.reply_text("Please type /calories to start the calculation.")



async def calories_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Input your weight in kg:')
    context.user_data['expecting'] = 'weight'



if __name__ == '__main__':
    print('BOt starting...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', commands.start_command))
    app.add_handler(CommandHandler('help', commands.help_command))
    app.add_handler(CommandHandler('calories', calories_command))
    app.add_handler(CallbackQueryHandler(handle_gender_input, pattern="^(male|female)$"))
    app.add_handler(CallbackQueryHandler(handle_activity_input, pattern="^(low|light|moderate|high|very high)$"))
    app.add_handler(CallbackQueryHandler(handle_goal_input, pattern="^(maintain|gain|lose)$"))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print('Polling...')
    app.run_polling(3)


"""
    1.Clean a handle_message ---DONe---
    2.Make a gender choice with cool buttons
    3.Make a activity choice also with COOL buttons
    4.Make everything look prettier
"""