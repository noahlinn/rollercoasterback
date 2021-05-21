"""create_users

Revision ID: 3ebf364fa6d0
Revises: 
Create Date: 2021-05-21 13:42:40.678782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ebf364fa6d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('location', sa.String, nullable=False),
        sa.Column('about_me', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('users')