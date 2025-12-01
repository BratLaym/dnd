from aiogram.fsm.state import State, StatesGroup


class AcademyCampaigns(StatesGroup):
    campaigns = State()


class AcademyCampaignPreview(StatesGroup):
    preview = State()
