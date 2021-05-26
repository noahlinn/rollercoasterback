"""add_profile_pic_to_user

Revision ID: 3be9ac0834dc
Revises: 7eeaaf8ed033
Create Date: 2021-05-26 13:54:49.351140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3be9ac0834dc'
down_revision = '7eeaaf8ed033'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users',
        sa.Column('profile_pic', sa.String)
    )


def downgrade():
    op.remove_column('users', 'profile_pic')
