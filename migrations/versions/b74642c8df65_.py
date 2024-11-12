"""empty message

Revision ID: b74642c8df65
Revises: a710b3626381
Create Date: 2024-11-11 21:41:30.633161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b74642c8df65'
down_revision = 'a710b3626381'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature_model_ratings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('feature_model_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['feature_model_id'], ['feature_model.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature_model_ratings')
    # ### end Alembic commands ###
