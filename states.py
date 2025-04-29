from aiogram.fsm.state import State, StatesGroup

class ChitmilStates(StatesGroup):
    what_allow = State()
    day_name = State()
    period = State()
    increase = State()