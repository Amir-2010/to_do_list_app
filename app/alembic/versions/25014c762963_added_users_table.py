"""added users table

Revision ID: 25014c762963
Revises: c9b10d2afa14
Create Date: 2026-08-12 19:57:27.955904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '25014c762963'
down_revision: Union[str, Sequence[str], None] = 'c9b10d2afa14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("tasks", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_tasks_user_id_users",
            "users",
            ["user_id"],
            ["id"],
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("tasks", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_tasks_user_id_users",
            type_="foreignkey",
        )