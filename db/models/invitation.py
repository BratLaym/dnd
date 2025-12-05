# db/models/invitation.py
import uuid

from tortoise import fields
from tortoise.fields import OnDelete

from db.models.base import TimestampedModel, UuidModel
from services.role import Role


class Invitation(TimestampedModel, UuidModel):
    user = fields.ForeignKeyField("models.User", related_name="invites_received", null=True)
    campaign = fields.ForeignKeyField("models.Campaign")
    role = fields.IntEnumField(Role, description="На какую роль мы приглашаем пользователя")
    start_data = fields.UUIDField(index=True)
    used = fields.BooleanField(default=False)
    created_by = fields.ForeignKeyField(
        "models.User", related_name="invites_created", null=True, on_delete=OnDelete.SET_NULL
    )

    async def save(self, *args, **kwargs):
        if not self.start_data:
            self.start_data = uuid.uuid4()
        await super().save(*args, **kwargs)

    @classmethod
    async def create(cls, **kwargs):  # noqa: ANN206
        if "start_data" not in kwargs:
            kwargs["start_data"] = uuid.uuid4()
        return await super().create(**kwargs)
