from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Merhaba!, Benim Adım {bn}  🎵

Grubunuzun sesli sohbetinde müzik çalabilirim [POYRAZ](https://t.me/Poyraz2103) tarafından geliştirildi.

Beni grubunuza ekleyin ve özgürce müzik çalın!**
        """,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑Sahibim👑", url="https://t.me/Poyraz2103")
                  ],[
                    InlineKeyboardButton(
                        "🎵Assistanım🎵", url="https://t.me/GoodVibeesMusic"
                    ),
                    InlineKeyboardButton(
                        "🔊 Kanalım", url="https://t.me/Fmsarkilar"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekleyin ➕", url="https://t.me/GoodVibeesBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Çevrimiçi Grup Müzik Çalar ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Kanalım", url="https://t.me/Fmsarkilar")
                ]
            ]
        )
   )


