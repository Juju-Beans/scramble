"""empty message

Revision ID: 2e2cb6b7476c
Revises: d650c4904f30
Create Date: 2021-11-16 16:23:47.167346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2cb6b7476c'
down_revision = 'd650c4904f30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'runs', ['player_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'runs', type_='unique')
    # ### end Alembic commands ###
