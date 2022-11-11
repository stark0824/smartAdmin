# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/07
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - 数据库基类
# +----------------------------------------------------------------------
from sqlalchemy import Column, Integer, String, SMALLINT
from flask_sqlalchemy import SQLAlchemy
from app.libs.memory import show_memory_info

db = SQLAlchemy()

show_memory_info('loader models')


class Base(db.Model):
    # 忽略基类的主键
    __abstract__ = True
    status = Column(SMALLINT(), default=0)

    def set_attr(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
