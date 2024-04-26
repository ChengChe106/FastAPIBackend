"""first migrations

Revision ID: 32a009e7014e
Revises: 8207a18ea793
Create Date: 2024-04-22 09:32:05.551893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '32a009e7014e'
down_revision: Union[str, None] = '8207a18ea793'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
