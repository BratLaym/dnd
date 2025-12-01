import logging

from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Button, Cancel
from aiogram_dialog.widgets.text import Const, Format

from db.models import Invitation, Participation
from states.academy_campaigns import AcademyCampaignPreview
from states.invitation import InvitationAccept

logger = logging.getLogger(__name__)
router = Router()


async def invitation_getter(dialog_manager: DialogManager, **kwargs):
    invitation = await Invitation.get_or_none(id=dialog_manager.start_data["invitation_id"]).prefetch_related(
        "campaign"
    )
    return {
        "campaign_title": invitation.campaign.title,
        "role": invitation.role.name,
    }


async def on_accept(c: CallbackQuery, b: Button, m: DialogManager):
    invitation = await Invitation.get_or_none(id=m.start_data["invitation_id"]).prefetch_related("campaign")
    participation = await Participation.create(
        user=m.middleware_data["user"], campaign=invitation.campaign, role=invitation.role
    )
    await c.answer(f"Приглашение в кампанию {invitation.campaign.title} принято!")
    await m.done()
    if invitation.campaign.verified:
        await m.start(
            AcademyCampaignPreview.preview,
            data={"campaign_id": invitation.campaign.id, "participation_id": participation.id},
        )
    else:
        # TODO @pxc1984: когда доделаем другие игры следует сюда добавить логику активации игры для них
        #   https://github.com/cu-tabletop/dnd/issues/10
        ...


router.include_router(
    Dialog(
        Window(
            Format("Вас пригласили в кампанию <b>{campaign_title}</b> на роль <b>{role}</b>"),
            Button(Const("Присоединиться"), id="accept", on_click=on_accept),
            Cancel(Const("Отказаться")),
            getter=invitation_getter,
            state=InvitationAccept.invitation,
        )
    )
)
