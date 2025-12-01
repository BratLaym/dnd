from aiogram.fsm.state import State, StatesGroup


class StartSimple(StatesGroup):
    simple = State()
