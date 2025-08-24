from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update


async def asc_gender(update: Update, context):
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton("👨 Male", callback_data="male"),
            InlineKeyboardButton("👩 Female", callback_data="female"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Choose your gender:", reply_markup=reply_markup)

async def asc_activity_level(update: Update, context):
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton('🛋 Low activity', callback_data='low'),
            InlineKeyboardButton('🚶‍♂️ Light activity', callback_data='light'),
            InlineKeyboardButton('🏃‍♂️ Moderate activity', callback_data='moderate'),
            InlineKeyboardButton('🏋️‍♀️ High activity', callback_data='high'),
            InlineKeyboardButton('🏃‍♂️🔥 Very high activity', callback_data='very high')
        ]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text("""🛋 Low activity – mostly sitting, little movement (~0–1 workouts/week)
🚶‍♂️ Light activity – light walking, occasional exercise (~1–3 workouts/week)
🏃‍♂️ Moderate activity – regular exercise or physical job (~3–5 workouts/week)
🏋️‍♀️ High activity – intense daily workouts (~6–7 workouts/week)
🏃‍♂️🔥 Very high activity – professional athlete or extreme training (~2 workouts/day)""",
                                    reply_markup=reply_markup)


async def asc_goal(update: Update, context):
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton("⚖️ Maintain", callback_data="maintain"),
            InlineKeyboardButton("➕ Gain", callback_data="gain"),
            InlineKeyboardButton("➖ Lose", callback_data="lose"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        "🎯 Choose your final goal:",
        reply_markup=reply_markup
    )


