from aiogram.fsm.state import State, StatesGroup


class StartJoin(StatesGroup):
    invitation = State()
