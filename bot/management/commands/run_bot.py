import asyncio

# from aiogram import Bot, types
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
#
# from django.conf import settings
from django.core.management import BaseCommand

from .commands import commands



async def main():
    print("Starting bot...")
    from bot.handlers import dp
    from bot.handlers import bot
    await bot.set_my_commands(commands=commands)
    await dp.start_polling(bot)


class Command(BaseCommand):
    def handle(self, *args, **options):
        asyncio.run(main())
