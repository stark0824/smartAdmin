# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/03
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - login控制器入口
# +----------------------------------------------------------------------
from flask import request, session, jsonify

from app.libs.BaseRoutes import BaseRoutes
from app.validators.form.login import LoginForm
from app.models.admin.tp_manager import tp_manager
from app.libs.memory import show_memory_info

api = BaseRoutes('login')


@api.route('/login/loginHandle', methods=['POST'])
def loginHandle():
    form = LoginForm(request.form)
    if form.validate():
        # 验证通过的逻辑
        r = tp_manager.get_manager_by_name(form.username.data)
        if r:
            msg = '操作成功'
            session['manager_id'] = r.id
            print(tp_manager.STATUS_NORMAL)
            show_memory_info(loginHandle)
        else:
            msg = '账号和密码错误'

        return jsonify({"code": 200, "data": [], "msg": msg})
    else:
        # 错误暂时忽略...
        return form.errors
