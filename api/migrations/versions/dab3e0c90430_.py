"""empty message

Revision ID: dab3e0c90430
Revises: 0f541a3193b2
Create Date: 2018-06-11 19:42:39.294640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dab3e0c90430'
down_revision = '0f541a3193b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('ftl', sa.Boolean(), nullable=True))
    op.drop_column('User', 'one_time_login')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('one_time_login', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('User', 'ftl')
    # ### end Alembic commands ###
