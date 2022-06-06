
#█▀▀ █▀▀▄ █▀▀▄ █░░█
#█▀▀ █░░█ █░░█ █▄▄█
#▀▀▀ ▀░░▀ ▀▀▀░ ▄▄▄█
#█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ 
#█░▀░█ █░░█ █░░█ ▀▀█ 
#▀░░░▀ ▀▀▀▀ ▀▀▀░ ▀▀▀
#
# Copyright 2022 t.me/endy_mods
# Licensed under the Apache License, Version 2.0

# meta developer: </code>@endy_mods

import random

from .. import loader, utils

yon =["Yes", "No", "[повесил трубку]"]
@loader.tds
class TalkingBenMod(loader.Module):
    """За основу взят модуль рандомайзера @D4n13l3k00\n\nГоворящий Бен пророк, гадалка, называйте как хотите"""
    strings = {"name": "TalkingBen"}
    prefix = "<b>[TalkingBen]</b>\n\n"

    @loader.owner
    async def bencmd(self, m):
        "<Текст который требуется ответить>\n(можно и ничего не писать, тогда ответит либо Yes, либо No, либо [повесил трубку])"
        args = utils.get_args_raw(m)
        if not args:
            await m.edit(self.prefix+random.choice(yon))
            return
        lst = [i.strip() for i in args.split(",") if i]
        await m.edit(self.prefix+args)
