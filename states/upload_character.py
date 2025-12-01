from aiogram.fsm.state import State, StatesGroup


class UploadCharacter(StatesGroup):
    upload = State()
