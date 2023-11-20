"""empty message

Revision ID: 90b34dd62870
Revises: e1ead70a6c71
Create Date: 2023-11-20 23:54:32.170561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b34dd62870'
down_revision = 'e1ead70a6c71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('org', 'is_deleted',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'updated_by',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'updated_by',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('org', 'is_deleted',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
