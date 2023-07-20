"""add last few columns to posts table

Revision ID: 639b1ebf0084
Revises: 4d0aa253f836
Create Date: 2023-07-16 18:24:00.269270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '639b1ebf0084'
down_revision = '4d0aa253f836'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(),nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text
        ('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
