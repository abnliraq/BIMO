import asyncio
import json
import math
import os
import time
from datetime import datetime
from telethon import events
from uniborg.util import admin_cmd, progress, humanbytes


@borg.on(admin_cmd(pattern="ping ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    asyncio.gather("Pong!")
    end = datetime.now()
    ms = (end - start)milli.seconds / 1000
    asyncio.gather("`Pong speed⚡️` !\n{}ms".format(ms))
