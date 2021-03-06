"""followers

Revision ID: 925208bc7af8
Revises: 27026ec449d4
Create Date: 2019-01-02 15:04:40.541278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '925208bc7af8'
down_revision = '27026ec449d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
