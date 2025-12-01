import json
import logging

from aiogram import Router
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Cancel, Url
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from db.models import User
from services.character_data import character_preview_getter
from states.player_preview import PlayerPreview

logger = logging.getLogger(__name__)
router = Router()


async def preview_getter(dialog_manager: DialogManager, **kwargs):
    user = await User.get(id=dialog_manager.start_data["user_id"])
    data = json.loads(user.data["data"])

    return {
        "profile_link": f"tg://user?id={user.id}",
        **character_preview_getter(user, data),
    }


router.include_router(
    Dialog(
        Window(
            DynamicMedia("avatar", when="avatar"),
            Format("{character_data_preview}", when="character_data_preview"),
            Url(Const("Перейти в профиль"), Format("{profile_link}")),
            Cancel(Const("Назад")),
            getter=preview_getter,
            state=PlayerPreview.preview,
        )
    )
)
