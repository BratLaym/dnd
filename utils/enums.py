import enum


class Role(enum.IntEnum):
    PLAYER = 0
    MASTER = 1
    OWNER = 2


class Mode(enum.StrEnum):
    ACADEMY = "Академия"
    OTHER_CAMPAIGNS = "Классический"
