# šŗšØš­š¬š°šµšØ š ¢
import asyncio

from userbot import jmthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import ALIVE_NAME

plugin_category = "fun"


@safeina.ar_cmd(
    pattern="ŲŖŁŁŁŲ±$",
    command=("ŲŖŁŁŁŲ±", plugin_category),
    info={
        "header": "Fun hack animation.",
        "description": "Reply to user to show hack animation",
        "note": "This is just for fun. Not real hacking.",
        "usage": "{tr}hack",
    },
)
async def _(event):
    "Fun hack animation."
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd ==  5193718748:
            await edit_or_reply(
                event, "**āÆļøŲ¹ŁŲ°Ų±Ų§ ŁŲ§ Ų§Ų³ŲŖŁŲ·ŁŲ¹ Ų§Ų®ŁŲŖŲ±Ų§Ł ŁŁŲ·ŁŲ±Ł Ų§Ų¹ŁŲŖŲ°Ų± Ų§Ł Ų³ŁŁŁŁŁ ŲØŲŖŁŁŁŁŲ±Ł**"
            )
        else:
            event = await edit_or_reply(event, "ŁŲŖŁŁ Ų§ŁŲ§Ų®ŲŖŁŲ±Ų§Ł ..")
            animation_chars = [
                "āÆļøŲŖŁŁ Ų§ŁŲ±ŲØŁŲ· ŲØŲ³ŁŁŲ±ŁŲ±Ų§ŲŖ Ų§ŁŁŲŖŁŁŁŲ± Ų§ŁŲ®ŁŲ§ŲµŲ©",
                "ŲŖŁŁ ŲŖŲ­ŁŲÆŁŲÆ Ų§ŁŲ¶Ų­ŁŁŲ©",
                "**ŲŖŁŁŁŁŲ±**... 0%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 4%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 8%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 20%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 36%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 52%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 84%\nāāāāāāāāāāāāāāāāāāāāāāāāā ",
                "**ŲŖŁŁŁŁŲ±**... 100%\nāāāāāāāāāāāāāāāāāāāāāāāā ",
                f"āÆļø** ŲŖŁŁ Ų§Ų®ŁŲŖŲ±Ų§Ł Ų§ŁŲ¶ŁŲ­ŁŲ©**..\n\nŁŁŁ ŲØŲ§ŁŁŲÆŁŲ¹ Ų§ŁŁ {ALIVE_NAME} ŁŲ¹ŁŲÆŁ ŁŲ“ŁŲ± ŁŲ¹ŁŁŁŲ§ŲŖŁ ŁŲµŁŁŲ±Ł",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(
            event,
            "āÆļøŁŁ ŁŲŖŁŁ Ų§ŁŲŖŲ¹ŁŲ±Ł Ų¹ŁŁ Ų§ŁŁŲ³ŲŖŁŲ®ŲÆŁ",
            parse_mode=_format.parse_pre,
        )
