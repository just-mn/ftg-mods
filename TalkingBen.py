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

import random
import requests
from telethon.tl.types import Message
import os
from asyncio import sleep

from .. import loader, utils

calling_lnk = "https://x0.at/CosT.mp4"
yes_lnk = "https://x0.at/3-of.mp4"
hohoho_lnk = "https://x0.at/snEh.mp4"
no_lnk = "https://x0.at/kCVU.mp4"
ugh_lnk = "https://x0.at/WKR0.mp4"

ben_answers = ["yes", "hohoho", "no", "ugh"]

@loader.tds
class TalkingBenMod(loader.Module):
    """Ben in video messages!\nGeekTG only😎"""
    strings = {"name": "TalkingBen", "wait": "⚙️Starting\n💿 Checking files, first start wil be long", "calling": "📞Calling Ben on this issue...", "downloaded": "✅All Downloads Completed!"}
    strings_ru = {"wait": "⚙️Запуск\n💿 Проверка файлов, первый запуск может быть дольше чем обычно", "calling": "📞Звонок Бену по данному вопросу...", "downloaded": "✅Все загрузки завершены!"}

    @loader.unrestricted
    async def bencmd(self, message):
        """Press your question to the grate prophet"""
        await utils.answer(message, self.strings("wait"))
        if not os.path.exists("assets"):
            os.mkdir("assets")
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
        await message.client.send_file(message.to_id, "assets/"+ben+".mp4", video_note=True)
        await message.client.delete_messages(message.to_id, msg)
        
        if "?" not in args:
            args = utils.get_args_raw(message)+"?"
        await utils.answer(message, "🔮 "+args)