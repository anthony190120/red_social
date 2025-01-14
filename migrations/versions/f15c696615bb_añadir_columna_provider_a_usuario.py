"""Añadir columna provider a usuario

Revision ID: f15c696615bb
Revises: b86930486e7d
Create Date: 2024-12-12 04:35:14.721044

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f15c696615bb'
down_revision = 'b86930486e7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('provider', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('foto_perfil', sa.String(length=500), nullable=True))
        batch_op.add_column(sa.Column('banner_imagen', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('descripcion', sa.String(length=255), nullable=True))
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=60),
               type_=sa.String(length=64),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=64),
               type_=mysql.VARCHAR(length=60),
               existing_nullable=False)
        batch_op.drop_column('descripcion')
        batch_op.drop_column('banner_imagen')
        batch_op.drop_column('foto_perfil')
        batch_op.drop_column('provider')

    # ### end Alembic commands ###
