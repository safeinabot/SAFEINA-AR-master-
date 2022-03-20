from userbot import CMD_HELP, safeina
from userbot.utils import admin_cmd
#𝑺𝑨𝑭𝑬𝑰𝑵𝑨 𖠢

@safeina.on(admin_cmd(pattern="خاص ?(.*)"))
async def pmto(event):
    r = event.pattern_match.group(1)
    p = r.split(" ")
    chat_id = p[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in p[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("**- تم ارسال الرسالة بنجاح ✓**")
    except BaseException:
        await event.edit("**- يبدو انه هنالك شي خطأ**")


"""   خاص بسورس سفينه ممنوع اخذ الملف بدون ذكر رابط القناة  ! """

CMD_HELP.update({"ارسال خاص": ".خاص <المعرف><الرسالة>\nالامر يرسل رسالة لشخص معين بدون الحاجه ان تدخل للدردشه اله فقط اكتب الامر مع معرف الحساب مع الرسالة وجربه بنفسك"})
