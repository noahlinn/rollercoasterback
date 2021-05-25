"""create_ridden_coasters

Revision ID: c572935a0ec3
Revises: dae99e6f207c
Create Date: 2021-05-25 10:53:24.672686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c572935a0ec3'
down_revision = 'dae99e6f207c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ridden_coasters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('coaster_id', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('ridden_coasters')
