from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`GUA SAYANG SAMA LO`")
    sleep(2)
    await typew.edit("`DAN SEBALIKNYA`")
    sleep(1)
    await typew.edit("`MUMPUNG KITA SAMA' SAYANG DAN CINTA KNP KITA G PACARAN? NANTI KITA NGENTOT YA MWAHH SAYANG KAMU`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.azel(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIABLO HIPOKRIT☑️**")
    await typew.edit("**DIABLO HIPOKRIT✅**")
    sleep(1)
    await typew.edit("**Cleo kemloc☑️**")
    await typew.edit("**Cleo kemloc✅**")
    sleep(2)
    await typew.edit("**Bink kontol☑️**")
    await typew.edit("**Bink kontol✅**")
    sleep(2)
    await typew.edit("**ayunda bgst☑️**")
    await typew.edit("**ayunda bgst✅**")
    sleep(2)
    await typew.edit("**tata bacot☑️**")
    await typew.edit("**tata bacot✅**")
    sleep(2)
    await typew.edit("**moon cipan☑️**")
    await typew.edit("**moon cipan✅**")
    sleep(2)
    await typew.edit("**piraa angen☑️**")
    await typew.edit("**piraa angen✅**")
    sleep(2)
    await typew.edit("**daki vcs☑️**")
    await typew.edit("**daki vcs✅**")
    sleep(3)
    await typew.edit("**CUMA AZEL YG GANTENG !**")

# Create by myself @localheart

CMD_HELP.update({
    "azel-ubot":
    "`.zelbut`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: coba aja & salam."
})
