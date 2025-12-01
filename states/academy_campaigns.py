from aiogram.fsm.state import StatesGroup, State


class AcademyCampaigns(StatesGroup):
    campaigns = State()


class AcademyCampaignPreview(StatesGroup):
    preview = State()
