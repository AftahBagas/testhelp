from time import sleep
from userbot.cmdhelp import CmdHelp
from userbot.events import alphabot


@alphabot(outgoing=True, pattern='^.sadboi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama aku suka kamu`")
    sleep(2)
    await typew.edit("`Kedua ternyata kamu udah ada yg punya:(`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah aku sakit hati`")
# Create by myself @localheart


@alphabot(outgoing=True, pattern='^.oii(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Eh Pada Ngapain Tu**")


@alphabot(outgoing=True, pattern='^.gabung(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Boleh Gabung Gak?**")


# Create by myself @localheart

CmdHelp ('animasi5').add_command( 'sadboi', None, 'Sadboi Sedang Curhat Wkwk.' 
    ).add_command( 'oii', None, 'Cek Aja Sendiri.' 
    ).add_command( 'gabung', None, 'Animasi Pengen Ikut Nimbrung.' 
    ).add()
