import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="followme ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = ""
    help_string = """@nazi_kun
    
