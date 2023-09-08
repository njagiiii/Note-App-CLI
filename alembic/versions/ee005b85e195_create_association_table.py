"""Create association table

Revision ID: ee005b85e195
Revises: 710da7459aea
Create Date: 2023-09-08 09:44:18.040833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee005b85e195'
down_revision: Union[str, None] = '710da7459aea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
        'new_association',
        sa.Column('note_id', sa.Integer(), sa.ForeignKey('notes.id'), nullable=True),
        sa.Column('tag_id', sa.Integer(), sa.ForeignKey('tags.id'), nullable=True),
    )


def downgrade() -> None:
    op.drop_table('new_association')
