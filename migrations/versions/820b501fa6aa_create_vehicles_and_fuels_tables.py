"""create vehicles and fuels tables

Revision ID: 820b501fa6aa
Revises: d1240d2e4a8d
Create Date: 2025-03-07 08:35:09.807045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '820b501fa6aa'
down_revision: Union[str, None] = 'd1240d2e4a8d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fuels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model', sa.String(length=20), nullable=False),
    sa.Column('brand', sa.String(length=20), nullable=False),
    sa.Column('plate', sa.String(length=10), nullable=False),
    sa.Column('year', sa.String(length=10), nullable=False),
    sa.Column('color', sa.String(length=20), nullable=False),
    sa.Column('id_fuel', sa.Integer(), nullable=False),
    sa.Column('renavam', sa.CHAR(length=11), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_fuel'], ['fuels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    op.drop_table('fuels')
    # ### end Alembic commands ###
