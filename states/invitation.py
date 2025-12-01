from aiogram.fsm.state import State, StatesGroup


class InvitationAccept(StatesGroup):
    invitation = State()
