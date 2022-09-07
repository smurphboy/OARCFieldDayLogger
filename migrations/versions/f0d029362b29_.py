"""empty message

Revision ID: f0d029362b29
Revises: 40c4e0ef289f
Create Date: 2022-09-07 17:45:45.074553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0d029362b29'
down_revision = '40c4e0ef289f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('QSO', schema=None) as batch_op:
        batch_op.drop_column('antenna')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('QSO', schema=None) as batch_op:
        batch_op.add_column(sa.Column('antenna', sa.VARCHAR(length=50), nullable=True))

    # ### end Alembic commands ###