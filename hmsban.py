from pyrogram import Client, filters
import random
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

api_id = "27477919"
api_hash = "b25cce1727f6d33d41d9e00e3ed62583"
bot_token = "6634084600:AAELYN64BKtF62w6rWyBprgQfa9wACFtaVo"

bot = Client("programer senzir", api_id, api_hash, bot_token=bot_token)

@bot.on_message(filters.command("senzir"))
def send_random_text(_, message):
    random_texts = ["Card Number: 5204039030895628\nFull Name: Miranda Sweeney\nCVV: 661\nPin: 5868\n", "كيف حالك؟", "أتمنى لك يومًا سعيدًا!", "ماذا أفعل لمساعدتك؟", "كسمك"]

    random_text = random.choice(random_texts)

    message.reply_text(random_text)
    
@bot.on_message(filters.command("start"))
def start(client, message):
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝙎 .࿆𝙉 .࿆𝙍 </>", url="https://t.me/programer_senzir")],
        [InlineKeyboardButton("𝗖𝗛:", url="https://t.me/def_Zoka")]
    ])
    message.reply_text(
        "اهلا بك عزيزي 🤗\n\n"
        "انا بوت اقوم بارسال فيزات خاصيًا لهيركو لانشاء فيزا قم بارسال امر /senzir ♡",
        reply_markup=reply_markup
    )


print("برمجة وتطوير @programer_senzir 🇸🇾")
bot.run()
