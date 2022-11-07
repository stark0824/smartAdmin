# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/03
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - login控制器入口
# +----------------------------------------------------------------------
from flask import request

from app.libs.BaseRoutes import BaseRoutes
from app.validators.form.login import LoginForm
from app.models.admin.tp_manager import tp_manager

api = BaseRoutes('login')


@api.route('/login/loginHandle', methods=['POST'])
def loginHandle():
    form = LoginForm(request.form)
    if form.validate():
        # 验证通过的逻辑
        r = tp_manager.query.filter(tp_manager.username == form.username.data).one()
        print(r)
        return "200"

    else:
        return form.errors
