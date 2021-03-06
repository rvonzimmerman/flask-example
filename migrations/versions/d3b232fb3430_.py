"""empty message

Revision ID: d3b232fb3430
Revises: b1a81022c365
Create Date: 2017-12-27 13:01:45.419544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3b232fb3430'
down_revision = 'b1a81022c365'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'description')
    # ### end Alembic commands ###
