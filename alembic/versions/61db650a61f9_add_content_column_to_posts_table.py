"""add content column to posts table

Revision ID: 61db650a61f9
Revises: 4922f05bafc4
Create Date: 2026-06-11 08:21:49.356644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61db650a61f9'
down_revision: Union[str, Sequence[str], None] = '4922f05bafc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
