from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from handlers.text_command import START_COMMAND, HELP_COMMAND

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(text=START_COMMAND)
    await message.delete()

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(text=HELP_COMMAND)