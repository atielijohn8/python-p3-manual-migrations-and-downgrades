"""Renaming students to scholars

Revision ID: 0cba2063a0fc
Revises: 791279dd0760
Create Date: 2025-08-29 13:39:17.928779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cba2063a0fc'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
   op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
