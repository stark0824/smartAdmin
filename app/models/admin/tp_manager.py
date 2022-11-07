# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/07
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - manager 管理员 models
# +----------------------------------------------------------------------
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base


class tp_manager(Base):
    __tablename__ = 'tp_manager'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, comment="登录名")
    _password = Column('password', String(64), nullable=False, comment="密码")
    nickname = Column(String(30), nullable=False, comment="昵称")
    headimg = Column(String(255), default="/admin/images/default_head.png", comment="头像")
    job = Column(String(20), default="/admin/images/default_head.png", comment="工作职位")
    mobile = Column(String(20), default=None, comment="手机号码")
    email = Column(String(50), default=None, comment="邮箱地址")
    role_id = Column(String(255), default=None, comment="角色id字符串以逗号分隔")
    department_ids = Column(String(255), default=None, comment="部门ID")
    wrong_times = Column(SmallInteger(), default=None, comment="错误次数")
    locking_time = Column(Integer(), default=0, nullable=False, comment="锁定时间")
    this_log_time = Column(Integer(), default=0, nullable=False, comment="最新登陆时间")
    last_log_time = Column(Integer(), default=0, nullable=False, comment="最后登陆时间")
    down_time = Column(Integer(), default=0, nullable=False, comment="账号停用时间")
    log_times = Column(Integer(), default=1, nullable=False, comment="登陆次数")
    status = Column(SmallInteger(), default=1, nullable=False, comment="状态")
    is_administrator = Column(SmallInteger(), default=0, nullable=False, comment="是否为超级管理员")
    delete = Column(Integer(), default=0, nullable=False, comment="删除时间")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        # 处理加密的方法
        # self._password = generate_password_hash(raw)
        pass

