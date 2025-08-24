from telegram import Update

from buttons import asc_gender, asc_activity_level, asc_goal


async def handle_weight_input(update: Update, context, text: str):
    try:
        weight = float(text)
        if weight <= 30 or weight >= 400:
            await update.message.reply_text('Your weight must be greater than 30k and less that 400kg')
            return
        context.user_data['weight'] = weight
        context.user_data['expecting'] = 'fat'

        with open('images/fat percent image.jpg', 'rb') as f:
            await update.message.reply_photo(photo=f, caption="Focus on photo and choose your fat percent")
        await update.message.reply_text('Input your fat percent:')

        return

    except ValueError:
        await update.message.reply_text('Please input your weight in kg:')


async def handle_fat_input(update: Update, context, text: str):
    try:
        fat = float(text)
        if fat <= 5 or fat >= 70:
            await update.message.reply_text('Your fat percent must be greater than 5 and less than 70')
            return

        context.user_data['fat'] = fat
        context.user_data['expecting'] = 'height'
        await update.message.reply_text('Input your height in cm:')
        return


    except ValueError:
        await update.message.reply_text("Please input your fat percent as a number:")


async def handle_height_input(update: Update, context, text: str):
    try:
        height = float(text)
        if height <= 50 or height >= 250:
            await update.message.reply_text('Your height must be greater than 50cm and less than 250cm')
            return
        context.user_data['height'] = height
        await asc_gender(update, context)
        context.user_data['expecting'] = 'gender'
        return

    except ValueError:
        await update.message.reply_text('Please input your height in cm:')


async def handle_gender_input(update: Update, context):
    query = update.callback_query
    await query.answer()

    gender = query.data
    context.user_data['gender'] = gender
    context.user_data['expecting'] = 'activity'

    await query.edit_message_text(f'Gender selected: {gender.capitalize()} ✅')
    await query.message.reply_text("Almost done! 💪 Choose your daily activity level. This helps me "
                                    "calculate your calories more accurately:")

    await asc_activity_level(update, context)

async def handle_activity_input(update: Update, context):
    query = update.callback_query
    await query.answer()

    activity_level = 0
    activity = query.data
    match activity:
        case 'low':
            activity_level = 1.2
        case 'light':
            activity_level = 1.375
        case 'moderate':
            activity_level = 1.55
        case 'high':
            activity_level = 1.725
        case 'very high':
            activity_level = 1.9
    context.user_data['activity'] = activity_level

    context.user_data['expecting'] = None
    await asc_goal(update, context)


async def handle_goal_input(update: Update, context):
    query = update.callback_query
    await query.answer()

    goal = query.data
    context.user_data['goal'] = goal
    context.user_data['expecting'] = None


    await query.edit_message_text(f'Goal selected: {goal.capitalize()} ✅')
    await calories_counter(update, context)






async def calories_counter(update: Update, context):
    query = update.callback_query

    weight = context.user_data['weight']
    fat = context.user_data['fat']
    height = context.user_data['height']
    gender = context.user_data['gender']
    activity = context.user_data['activity']
    goal = context.user_data.get('goal', 'maintain')

    # 1) Обчислюємо LBM і BMR (Katch–McArdle)
    lbm = weight * (1 - fat / 100)
    bmr = 370 + (21.6 * lbm)

    # 2) Добова норма з активністю
    calories = bmr * activity

    # 3) Корекція по цілі
    if goal == "gain":
        calories += 300
    elif goal == "lose":
        calories -= 300

    # 4) Макроси
    if goal == "gain":
        protein_g = weight * 2.0
        fat_g = weight * 1.0
    elif goal == "lose":
        protein_g = weight * 2.2
        fat_g = weight * 0.8
    else:  # maintain
        protein_g = weight * 1.8
        fat_g = weight * 0.9

    # 5) Переводимо калорії
    protein_cal = protein_g * 4
    fat_cal = fat_g * 9
    carbs_cal = calories - (protein_cal + fat_cal)
    carbs_g = carbs_cal / 4

    await query.message.reply_text(
        f"📊 Your stats:\n"
        f"⚖️ Weight: {weight} kg\n"
        f"💡 Fat: {fat}%\n"
        f"📏 Height: {height} cm\n"
        f"🚻 Gender: {gender.capitalize()}\n"
        f"🔥 Activity factor: {activity}\n"
        f"🎯 Goal: {goal.capitalize()}\n\n"
        f"➡️ Daily calories: *{round(calories)} kcal*\n\n"
        f"🍗 Protein: *{round(protein_g)} g*\n"
        f"🥑 Fat: *{round(fat_g)} g*\n"
        f"🍚 Carbs: *{round(carbs_g)} g*",
        parse_mode="Markdown"
    )
