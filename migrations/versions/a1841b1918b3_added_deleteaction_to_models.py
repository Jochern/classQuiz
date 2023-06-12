"""Added DeleteAction to models

Revision ID: a1841b1918b3
Revises: 89c4b5d547aa
Create Date: 2023-06-09 13:13:00.865587

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = "a1841b1918b3"
down_revision = "89c4b5d547aa"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("fk_api_keys_users_id_user", "api_keys", type_="foreignkey")
    op.create_foreign_key("fk_api_keys_users_id_user", "api_keys", "users", ["user"], ["id"], ondelete="CASCADE")
    op.drop_constraint("fk_fido_credentials_users_id_user", "fido_credentials", type_="foreignkey")
    op.create_foreign_key(
        "fk_fido_credentials_users_id_user", "fido_credentials", "users", ["user"], ["id"], ondelete="CASCADE"
    )
    op.drop_constraint("fk_game_results_quiz_id_quiz", "game_results", type_="foreignkey")
    op.drop_constraint("fk_game_results_users_id_user", "game_results", type_="foreignkey")
    op.create_foreign_key(
        "fk_game_results_users_id_user", "game_results", "users", ["user"], ["id"], ondelete="CASCADE"
    )
    op.create_foreign_key("fk_game_results_quiz_id_quiz", "game_results", "quiz", ["quiz"], ["id"], ondelete="CASCADE")
    op.drop_constraint("fk_quiz_users_id_user_id", "quiz", type_="foreignkey")
    op.create_foreign_key("fk_quiz_users_id_user_id", "quiz", "users", ["user_id"], ["id"], ondelete="CASCADE")
    op.drop_constraint("fk_quiztivitys_users_id_user", "quiztivitys", type_="foreignkey")
    op.create_foreign_key("fk_quiztivitys_users_id_user", "quiztivitys", "users", ["user"], ["id"], ondelete="CASCADE")
    op.drop_constraint("fk_quiztivityshares_quiztivitys_id_quiztivity", "quiztivityshares", type_="foreignkey")
    op.drop_constraint("fk_quiztivityshares_users_id_user", "quiztivityshares", type_="foreignkey")
    op.create_foreign_key(
        "fk_quiztivityshares_quiztivitys_id_quiztivity",
        "quiztivityshares",
        "quiztivitys",
        ["quiztivity"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "fk_quiztivityshares_users_id_user", "quiztivityshares", "users", ["user"], ["id"], ondelete="CASCADE"
    )
    op.drop_constraint("fk_storage_items_users_id_user", "storage_items", type_="foreignkey")
    op.create_foreign_key(
        "fk_storage_items_users_id_user", "storage_items", "users", ["user"], ["id"], ondelete="SET NULL"
    )
    op.drop_constraint("fk_user_sessions_users_id_user", "user_sessions", type_="foreignkey")
    op.create_foreign_key(
        "fk_user_sessions_users_id_user", "user_sessions", "users", ["user"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("fk_user_sessions_users_id_user", "user_sessions", type_="foreignkey")
    op.create_foreign_key("fk_user_sessions_users_id_user", "user_sessions", "users", ["user"], ["id"])
    op.drop_constraint("fk_storage_items_users_id_user", "storage_items", type_="foreignkey")
    op.create_foreign_key("fk_storage_items_users_id_user", "storage_items", "users", ["user"], ["id"])
    op.drop_constraint("fk_quiztivityshares_users_id_user", "quiztivityshares", type_="foreignkey")
    op.drop_constraint("fk_quiztivityshares_quiztivitys_id_quiztivity", "quiztivityshares", type_="foreignkey")
    op.create_foreign_key("fk_quiztivityshares_users_id_user", "quiztivityshares", "users", ["user"], ["id"])
    op.create_foreign_key(
        "fk_quiztivityshares_quiztivitys_id_quiztivity", "quiztivityshares", "quiztivitys", ["quiztivity"], ["id"]
    )
    op.drop_constraint("fk_quiztivitys_users_id_user", "quiztivitys", type_="foreignkey")
    op.create_foreign_key("fk_quiztivitys_users_id_user", "quiztivitys", "users", ["user"], ["id"])
    op.drop_constraint("fk_quiz_users_id_user_id", "quiz", type_="foreignkey")
    op.create_foreign_key("fk_quiz_users_id_user_id", "quiz", "users", ["user_id"], ["id"])
    op.drop_constraint("fk_game_results_quiz_id_quiz", "game_results", type_="foreignkey")
    op.drop_constraint("fk_game_results_users_id_user", "game_results", type_="foreignkey")
    op.create_foreign_key("fk_game_results_users_id_user", "game_results", "users", ["user"], ["id"])
    op.create_foreign_key("fk_game_results_quiz_id_quiz", "game_results", "quiz", ["quiz"], ["id"])
    op.drop_constraint("fk_fido_credentials_users_id_user", "fido_credentials", type_="foreignkey")
    op.create_foreign_key("fk_fido_credentials_users_id_user", "fido_credentials", "users", ["user"], ["id"])
    op.drop_constraint("fk_api_keys_users_id_user", "api_keys", type_="foreignkey")
    op.create_foreign_key("fk_api_keys_users_id_user", "api_keys", "users", ["user"], ["id"])
    # ### end Alembic commands ###