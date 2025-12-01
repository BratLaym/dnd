from aiogram.fsm.state import State, StatesGroup


class AcademyRating(StatesGroup):
    rating = State()
