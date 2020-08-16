"""empty message

Revision ID: bf1438d002b8
Revises: 
Create Date: 2020-06-08 01:10:31.906618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf1438d002b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('date_of_joining', sa.Date(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('Zone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zone', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('History_of_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['Company.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('expire_date', sa.Date(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['Company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Pharamcy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=False),
    sa.Column('support', sa.String(length=200), nullable=True),
    sa.Column('date_of_joining', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['zone_id'], ['Zone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Doctor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=True),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('speciality', sa.String(length=200), nullable=False),
    sa.Column('d_class', sa.String(length=2), nullable=True),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('support', sa.String(length=200), nullable=False),
    sa.Column('loyality', sa.String(length=200), nullable=False),
    sa.Column('date_of_joining', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.ForeignKeyConstraint(['zone_id'], ['Zone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Acceptance_of_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('acceptance', sa.Boolean(), nullable=False),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['Doctor.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['Item.id'], ),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Availabilty_of_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['Doctor.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['Item.id'], ),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('History_of_marketing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['Doctor.id'], ),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('History_of_user_activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=False),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['Doctor.id'], ),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['zone_id'], ['Zone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=False),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.Column('date_of_order', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['Doctor.id'], ),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.ForeignKeyConstraint(['zone_id'], ['Zone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('History_of_doctor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('visit_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['doctor_id'], ['Doctor.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['Order.id'], ),
    sa.ForeignKeyConstraint(['visit_id'], ['History_of_user_activity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('History_of_pharmacy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pharmacy_id', sa.Integer(), nullable=False),
    sa.Column('visit_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['Order.id'], ),
    sa.ForeignKeyConstraint(['pharmacy_id'], ['Pharamcy.id'], ),
    sa.ForeignKeyConstraint(['visit_id'], ['History_of_user_activity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['Item.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['Order.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_order')
    op.drop_table('History_of_pharmacy')
    op.drop_table('History_of_doctor')
    op.drop_table('Order')
    op.drop_table('History_of_user_activity')
    op.drop_table('History_of_marketing')
    op.drop_table('Availabilty_of_item')
    op.drop_table('Acceptance_of_item')
    op.drop_table('Doctor')
    op.drop_table('Pharamcy')
    op.drop_table('Item')
    op.drop_table('History_of_company')
    op.drop_table('Zone')
    op.drop_table('User')
    op.drop_table('Company')
    # ### end Alembic commands ###
