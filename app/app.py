# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/03
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - 入口文件
# +----------------------------------------------------------------------
from flask import Flask


def create_app():
    app = Flask(__name__)
    # 导入config中的配置文件
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    # 注册并导入蓝图
    register_blue(app)
    return app


def register_blue(app):
    from app.api import create_blueprint_api
    app.register_blueprint(create_blueprint_api(), url_prefix='/api')
