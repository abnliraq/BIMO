import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="followme ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    str = event.pattern_match.group(1)
    await event.edit(str)
