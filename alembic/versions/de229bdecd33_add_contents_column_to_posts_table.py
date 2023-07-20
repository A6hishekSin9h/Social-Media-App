"""add contents column to posts table

Revision ID: de229bdecd33
Revises: f3ce16761107
Create Date: 2023-07-16 13:15:52.526395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de229bdecd33'
down_revision = 'f3ce16761107'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
