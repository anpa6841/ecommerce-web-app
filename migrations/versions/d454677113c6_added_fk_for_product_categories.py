"""Added Fk for product categories

Revision ID: d454677113c6
Revises: 955021727835
Create Date: 2023-05-27 14:48:34.700649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd454677113c6'
down_revision = '955021727835'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_product_categories_id', 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product_categories_id', type_='foreignkey')

    # ### end Alembic commands ###
