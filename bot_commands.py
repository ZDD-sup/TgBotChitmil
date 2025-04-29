from aiogram.types import BotCommand

def get_default_commands() -> list[BotCommand]:
    return [
        BotCommand(command="start", description="Начать работу с ботом"),
        BotCommand(command="help", description="Справка"),
        BotCommand(command="chitmil", description="Начать опрос Chitmil"),
        BotCommand(command="my_chitmils", description="Посмотреть свои записи"),
    ]
