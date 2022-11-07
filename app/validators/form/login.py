# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/07
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - login 表单数据验证层
# +----------------------------------------------------------------------
from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError

# 引入models
from app.models.user import User


class LoginForm(Form):
    username = StringField('username', [validators.data_required()])
    password = PasswordField('password', [validators.DataRequired()])

    def validators_username(self, field):
        pass
