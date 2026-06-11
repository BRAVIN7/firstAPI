"""add foreign key to posts table

Revision ID: c2ccdcc3ebb8
Revises: 18bb9608e8fd
Create Date: 2026-06-11 08:53:45.663109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2ccdcc3ebb8'
down_revision: Union[str, Sequence[str], None] = '18bb9608e8fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # 1. Add column as nullable first to allow existing rows
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=True))
    
    # 2. Backfill existing rows with a default value (replace 1 with a valid user_id)
    # If you have no data, this step is safe but optional.
    op.execute("UPDATE posts SET owner_id = 1 WHERE owner_id IS NULL")
    
    # 3. Alter column to be non-nullable
    op.alter_column('posts', 'owner_id', nullable=False)
    
    # 4. Create the foreign key (Ensure name matches downgrade)
    op.create_foreign_key(
        'posts_users_fk', 
        source_table="posts", 
        referent_table="users",
        local_cols=['owner_id'], 
        remote_cols=['id'], 
        ondelete="CASCADE"
    )

def downgrade():
    # Fix: Name must match upgrade ('posts_users_fk', not 'post_users_fk')
    op.drop_constraint('posts_users_fk', table_name="posts", type_="foreignkey")
    op.drop_column('posts', 'owner_id')   
