from tortoise.exceptions import ValidationError


class ItemHeldByBothError(ValidationError):
    MESSAGE = "Item cannot be held by both a character and a user simultaneously."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class NoHolderError(ValidationError):
    MESSAGE = "Item must have either a character or user holder."

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)


class CursedTransferError(ValidationError):
    MESSAGE = "Cannot transfer cursed item without force=True"

    def __init__(self) -> None:
        super().__init__(self.MESSAGE)
