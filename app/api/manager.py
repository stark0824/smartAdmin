# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/03
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - login控制器入口
# +----------------------------------------------------------------------
from flask import session

from app.libs.BaseRoutes import BaseRoutes

from app.models.admin.tp_manager import tp_manager
api = BaseRoutes('manager')


@api.route('/manager/getInfo', methods=['POST'])
def getInfo():
    r = tp_manager.get_manager_info(session['manager_id'])
    print(r.__dict__)
    return "getInfo"
