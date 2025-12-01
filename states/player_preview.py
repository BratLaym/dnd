from aiogram.fsm.state import State, StatesGroup


class PlayerPreview(StatesGroup):
    preview = State()
