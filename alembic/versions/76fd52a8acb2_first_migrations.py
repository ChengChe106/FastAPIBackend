"""first migrations

Revision ID: 76fd52a8acb2
Revises: f63b04f695c2
Create Date: 2024-04-22 09:33:33.342418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76fd52a8acb2'
down_revision: Union[str, None] = 'f63b04f695c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
