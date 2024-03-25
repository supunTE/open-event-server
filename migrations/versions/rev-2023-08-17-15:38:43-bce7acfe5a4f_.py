"""empty message

Revision ID: bce7acfe5a4f
Revises: 1af4cc4f7cd5
Create Date: 2023-08-17 15:38:43.387065

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bce7acfe5a4f'
down_revision = '1af4cc4f7cd5'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('virtual_check_in',
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket_holder_id', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('microlocation_id', sa.Integer(), nullable=True),
    sa.Column('check_in_type', sa.String(), nullable=False),
    sa.Column('check_in_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('check_out_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['microlocation_id'], ['microlocations.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('virtual_check_in')
    # ### end Alembic commands ###