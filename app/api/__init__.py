# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/03
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - api 构造方法中添加api
# +----------------------------------------------------------------------
from flask import Blueprint
from app.api import login, manager, user


def create_blueprint_api():
    route_api = Blueprint('route_api', __name__)
    login.api.register(route_api)
    manager.api.register(route_api)
    user.api.register(route_api)
    return route_api
