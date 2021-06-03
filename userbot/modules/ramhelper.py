""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/bibitunggulnexus)"
        "\n[Repo](https://github.com/azel-kochoyy/AZEL-UBOT)"
        "\n[Channel](https://t.me/badguyshitt)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/azel-kochoyy/AZEL-UBOT/AZEL-UBOT/varshelper.txt)")


CMD_HELP.update({
    "Zelhelp":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk AZEL-UBOT.\
\n`.lordvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
