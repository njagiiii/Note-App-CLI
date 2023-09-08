"""Create user table

Revision ID: 5b31302a659f
Revises: a60000616e6f
Create Date: 2023-09-08 09:38:49.950467

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b31302a659f'
down_revision: Union[str, None] = 'a60000616e6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )

def downgrade() -> None:
    op.drop_table('users')