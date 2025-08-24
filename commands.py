from telegram import Update
from telegram.ext import ContextTypes


from telegram.ext import ContextTypes
from telegram import Update

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('images/start_image_with_healsy_food.jpg', 'rb') as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=(
                "👋 Hi! I’m *CaloriesBot* — your personal helper for calculating daily calorie needs.\n\n"
                "🍎 To get started, simply type */calories*.\n\n"
                "📋 Here’s how it works:\n"
                "1️⃣ Enter your *weight* (in kg)\n"
                "2️⃣ Provide your *body fat percentage* "
                "(I’ll show you a reference picture so it’s easier)\n"
                "3️⃣ Type your *height* (in cm)\n"
                "4️⃣ Choose your *gender* and *activity level*\n\n"
                "📊 Then I’ll calculate how many calories you need every day 💪"
            ),
            parse_mode="Markdown"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("just type a /calories")

