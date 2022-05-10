#█▀▀ █▀▀▄ █▀▀▄ █░░█
#█▀▀ █░░█ █░░█ █▄▄█
#▀▀▀ ▀░░▀ ▀▀▀░ ▄▄▄█
#█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ 
#█░▀░█ █░░█ █░░█ ▀▀█ 
#▀░░░▀ ▀▀▀▀ ▀▀▀░ ▀▀▀
#
# Copyright 2022 t.me/endy_mods
# Licensed under the Apache License, Version 2.0

# meta developer: @dan_endy
# scope: hikka_only

import random
import requests
from telethon.tl.types import Message
import os
from asyncio import sleep

from .. import loader, utils

calling_lnk = "https://siasky.net/_Agdc1lPT-jsI2vmXkuKrw0_TLno77Bsahctqwt0LDx3CA"
yes_lnk = "https://siasky.net/_AnH1OER62yt1inz8mocSHAC1pdZt4O96aAllHSVkjGs4A"
hohoho_lnk = "https://siasky.net/_AGOB4aho7rRsvx-0OyC_nmLHMrAn-nqbBdFq9KIgkZ8Fw"
no_lnk = "https://siasky.net/_Am69SVaX-zhebA5Kwvuljp-UgKWk4dFuetyITvlEUEvQg"
ugh_lnk = "https://siasky.net/_AmrXP9sRqrs6RvVaZnsWI8UecP4UjcduljlrqP5fWJLzg4"

ben_answers = ["yes", "hohoho", "no", "ugh"]

@loader.tds
class TalkingBenMod(loader.Module):
    """Ben in video messages!\n🌘Hikka only"""
    strings = {"name": "TalkingBen", "wait": "⚙️Starting\n💿 Checking files, first start wil be long", "calling": "📞Calling Ben on this issue...", "downloaded": "✅All Downloads Completed!"}
    strings_ru = {"wait": "⚙️Запуск\n💿 Проверка файлов, первый запуск может быть дольше чем обычно", "calling": "📞Звонок Бену по данному вопросу...", "downloaded": "✅Все загрузки завершены!"}

    @loader.unrestricted
    async def bencmd(self, message):
        """Press your question to the grate prophet"""
        await utils.answer(message, self.strings("wait"))
        await sleep(1)
        if not os.path.isfile("assets/call.mp4"):
            r = requests.get(calling_lnk)
            with open('assets/call.mp4', 'wb') as f:
                f.write(r.content)
        if not os.path.isfile("assets/yes.mp4"):
            r = requests.get(yes_lnk)
            with open('assets/yes.mp4', 'wb') as f:
                f.write(r.content)
        if not os.path.isfile("assets/hohoho.mp4"): 
            r = requests.get(hohoho_lnk)
            with open('assets/hohoho.mp4', 'wb') as f:
                f.write(r.content)
        if not os.path.isfile("assets/no.mp4"):
            r = requests.get(no_lnk)
            with open('assets/no.mp4', 'wb') as f:
                f.write(r.content)
        if not os.path.isfile("assets/ugh.mp4"):
            r = requests.get(ugh_lnk)
            with open('assets/ugh.mp4', 'wb') as f:
                f.write(r.content)
            await utils.answer(message, self.strings("downloaded"))
            await sleep(1)
        args = utils.get_args_raw(message)
        ben = random.choice(ben_answers)
        msg = await message.client.send_file(message.to_id, "assets/call.mp4", video_note=True)
        reply = await utils.answer(message, self.strings("calling"))
        await sleep(3)
        await message.client.send_file(message.to_id, "assets/"+ben+".mp4", video_note=True, reply_to=reply)
        await message.client.delete_messages(message.to_id, msg)
        
        if "?" not in args:
            args = utils.get_args_raw(message)+"?"
        await utils.answer(message, "🔮 "+args)
