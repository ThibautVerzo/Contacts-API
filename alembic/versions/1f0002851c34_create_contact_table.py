"""Create Contact table

Revision ID: 1f0002851c34
Revises: 
Create Date: 2022-02-08 00:53:50.776390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f0002851c34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('contact',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    )


def downgrade():
    op.drop_table('contact')
