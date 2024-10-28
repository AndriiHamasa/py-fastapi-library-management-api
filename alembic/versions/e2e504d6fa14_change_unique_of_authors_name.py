"""change unique of authors name

Revision ID: e2e504d6fa14
Revises: e00855069317
Create Date: 2024-10-28 17:33:36.062044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2e504d6fa14'
down_revision: Union[str, None] = 'e00855069317'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'author', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'author', type_='unique')
    # ### end Alembic commands ###
