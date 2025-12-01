from tortoise import fields

from .base import CharacterData, TimestampedModel, UuidModel


class Character(TimestampedModel, CharacterData, UuidModel):
    user = fields.ForeignKeyField("models.User")
    campaign = fields.ForeignKeyField("models.Campaign")

    class Meta:
        unique_together = ("user", "campaign")
