"""adding foreign key constraints

Revision ID: b9a37038d89a
Revises: ada61062c991
Create Date: 2018-12-21 13:26:13.560245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a37038d89a'
down_revision = 'ada61062c991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignment') as batch_op:
        batch_op.create_foreign_key("fk_course_id",'course', ['course_id'], ['id'])
        batch_op.create_foreign_key("fk_admin_id", 'admin', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignment') as batch_op:
        batch_op.drop_constraint("fk_course_id", type_='foreignkey')
        batch_op.drop_constraint("fk_admin_id", type_='foreignkey')

    # ### end Alembic commands ###
