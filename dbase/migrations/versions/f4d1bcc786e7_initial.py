"""Initial

Revision ID: f4d1bcc786e7
Revises: 
Create Date: 2024-03-10 15:13:19.043544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4d1bcc786e7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('publisher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('nick', sa.String(length=6), nullable=True),
    sa.Column('pub_status', sa.Integer(), nullable=True),
    sa.Column('reference', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('motto', sa.String(length=128), nullable=True),
    sa.Column('ilink', sa.String(length=16), nullable=True),
    sa.Column('olink', sa.String(length=128), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('date_pub', sa.DateTime(), nullable=True),
    sa.Column('publisher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('i_name', sa.Integer(), nullable=True),
    sa.Column('p_width', sa.Integer(), nullable=False),
    sa.Column('p_height', sa.Integer(), nullable=False),
    sa.Column('articles_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['articles_id'], ['articles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.drop_table('articles')
    op.drop_table('publisher')
    # ### end Alembic commands ###