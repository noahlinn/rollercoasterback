"""create_bucket_list_coasters

Revision ID: 7eeaaf8ed033
Revises: c572935a0ec3
Create Date: 2021-05-25 13:25:23.720952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eeaaf8ed033'
down_revision = 'c572935a0ec3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'bucket_list_coasters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('coaster_id', sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table('bucket_list_coasters')
