from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تهيئة البوت
api_id = 27477919
api_hash = "b25cce1727f6d33d41d9e00e3ed62583"
bot_token = "6740821383:AAEYFkVfDlK_OHfTxeweHm4GDHvkcovOY34"

app = Client("my_bot", api_id=api_id, api_hash=api_hash,  bot_token=bot_token)


# التعامل مع الرسائل الواردة
@app.on_message(filters.command("start"))
def start_command(client, message):
    # إنشاء زرين انلاين
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("زر أول", callback_data="button1"),
            InlineKeyboardButton("زر ثاني", callback_data="button2")
        ]]
    )
    message.reply_text(
        "مرحباً بك في البوت!",
        reply_markup=keyboard
    )


# التعامل مع الاستجابة من الأزرار الانلاين
@app.on_callback_query()
def button_click(client, callback_query):
    if callback_query.data == "button1":
        callback_query.answer("أنت اخترت الزر الأول")
    elif callback_query.data == "button2":
        callback_query.answer("أنت اخترت الزر الثاني")

