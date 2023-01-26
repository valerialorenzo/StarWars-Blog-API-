"""empty message

Revision ID: 58d7814ef5cf
Revises: f2ce1ecb1cbc
Create Date: 2023-01-26 15:17:33.620915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58d7814ef5cf'
down_revision = 'f2ce1ecb1cbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('personajes_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('vehiculos_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'vehiculos', ['vehiculos_id'], ['id'])
        batch_op.create_foreign_key(None, 'personajes', ['personajes_id'], ['id'])
        batch_op.create_foreign_key(None, 'personajes', ['usuario_id'], ['id'])
        batch_op.drop_column('agregar')
        batch_op.drop_column('eliminar')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('eliminar', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('agregar', sa.VARCHAR(length=250), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('vehiculos_id')
        batch_op.drop_column('personajes_id')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###
