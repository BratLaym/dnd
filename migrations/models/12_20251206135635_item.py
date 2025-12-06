from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "items" (
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "id" UUID NOT NULL PRIMARY KEY,
    "title" VARCHAR(255) NOT NULL,
    "quantity" INT NOT NULL DEFAULT 1,
    "description" TEXT NOT NULL,
    "weight" DOUBLE PRECISION,
    "value" DECIMAL(10,2),
    "rarity" VARCHAR(50),
    "attunement_required" BOOL NOT NULL DEFAULT False,
    "tags" VARCHAR[],
    "is_equipped" BOOL NOT NULL DEFAULT False,
    "equipped_slot" VARCHAR(50),
    "is_cursed" BOOL NOT NULL DEFAULT False,
    "charges" INT,
    "current_durability" INT,
    "max_durability" INT,
    "magic_bonus" INT NOT NULL DEFAULT 0,
    "magical_properties" JSONB,
    "attuned_character_id" UUID REFERENCES "character" ("id") ON DELETE SET NULL,
    "campaign_id" UUID NOT NULL REFERENCES "campaign" ("id") ON DELETE CASCADE,
    "holder_character_id" UUID REFERENCES "character" ("id") ON DELETE SET NULL,
    "holder_user_id" BIGINT REFERENCES "user" ("id") ON DELETE SET NULL
);
CREATE INDEX IF NOT EXISTS "idx_items_title_a80898" ON "items" ("title");
CREATE INDEX IF NOT EXISTS "idx_items_rarity_3f1de0" ON "items" ("rarity");
CREATE INDEX IF NOT EXISTS "idx_items_campaig_d923e5" ON "items" ("campaign_id", "holder_character_id");
CREATE INDEX IF NOT EXISTS "idx_items_campaig_c59ef5" ON "items" ("campaign_id", "holder_user_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "items";"""


MODELS_STATE = (
    "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"
)
