from tortoise import fields

from .base import CharacterData, TimestampedModel, UuidModel


class Character(CharacterData, TimestampedModel, UuidModel):
    user = fields.ForeignKeyField("models.User")
    campaign = fields.ForeignKeyField("models.Campaign")
    data = fields.JSONField(null=True)

    class Meta:
        unique_together = ("user", "campaign")
