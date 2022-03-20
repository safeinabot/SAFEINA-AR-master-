from telethon import events
from telethon.utils import pack_bot_file_id


@tgbot.on(events.NewMessage(pattern="^الايدي"))
async def _(event):
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await tgbot.send_message(
                event.chat_id,
                "⌯︙ايـدي الـدردشة: `{}`\n⌯︙ايدي المستخدم: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id), bot_api_file_id
                ),
            )
        else:
            await tgbot.send_message(
                event.chat_id,
                "⌯︙ايـدي الـدردشة: `{}`\n⌯︙ايدي المستخدم: `{}`".format(
                    str(event.chat_id), str(r_msg.from_id)
                ),
            )
    else:
        await tgbot.send_message(
            event.chat_id, "⌯︙ايـدي الـدردشة: `{}`".format(str(event.chat_id))
        )

# 𝑺𝑨𝑭𝑬𝑰𝑵𝑨 𖠢
#@S_F_M_L
