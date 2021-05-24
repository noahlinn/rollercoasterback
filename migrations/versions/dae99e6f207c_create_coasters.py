"""create_coasters

Revision ID: dae99e6f207c
Revises: 3ebf364fa6d0
Create Date: 2021-05-23 17:58:24.243830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dae99e6f207c'
down_revision = '3ebf364fa6d0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'roller_coasters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('park_located_at', sa.String, nullable=False),
        sa.Column('location', sa.String, nullable=False),
        sa.Column('year_built', sa.Integer),
        sa.Column('type_of', sa.String, nullable=False),
        sa.Column('top_speed_in_mph', sa.Integer, nullable=False),
        sa.Column('length_in_feet', sa.Integer, nullable=False),
        sa.Column('height_in_feet', sa.Integer, nullable=False),
        sa.Column('number_of_inversions', sa.Integer, nullable=False),
        sa.Column('manufacturer', sa.String),
        sa.Column("image", sa.String),
        sa.Column('video', sa.String),
        sa.Column('user_id', sa.Integer)
    )

def downgrade():
    op.drop_table('roller_coasters')
