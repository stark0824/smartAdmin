# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/07
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - user 用户 models
# +----------------------------------------------------------------------

from sqlalchemy import Column, Index

from sqlalchemy.dialects.mysql import VARCHAR, TEXT, BIGINT, INTEGER, SMALLINT, TINYINT, DECIMAL, FLOAT, \
    DOUBLE, DATETIME, TIMESTAMP, DECIMAL

from app.models.base import Base, db


class wm_user_user(Base):
    STATUS_NORMAL = 1
    __tablename__ = 'wm_user_user9'

    user_id = Column(TINYINT, primary_key=True, autoincrement=True)
    user_name = Column(VARCHAR(length=50), nullable=False, index=True, comment="账号")
    _password = Column('user_psw', VARCHAR(length=50), nullable=False, comment="密码")
    user_status = Column(TINYINT(display_width=1), nullable=False, server_default="1",
                         comment="1为正常,0为审核中")
    user_display = Column(TINYINT(display_width=4), nullable=False, server_default="1",
                          comment="0为永久封禁，1为正常，2为定时封禁 3 注销用户")
    user_nickname = Column(VARCHAR(length=50), index=True, nullable=False, comment="昵称")
    user_email = Column(VARCHAR(length=50), index=True, nullable=False, comment="邮箱")
    user_qq = Column(VARCHAR(length=15), nullable=False, comment="用户QQ号")
    user_tel = Column(VARCHAR(length=18), index=True, nullable=False, comment="用户的手机号")
    user_sex = Column(TINYINT(display_width=1), nullable=False, server_default="1", comment="性别")

    user_birthday = Column(DATETIME, nullable=False, default='1991-10-24', comment="用户的出生年月日")
    user_head = Column(VARCHAR(length=200), nullable=False, comment="头像")
    user_sign = Column(VARCHAR(length=255), nullable=False, comment="签名")
    user_ticket_act = Column(INTEGER(display_width=11), server_default="0", comment="凤凰蛋")
    user_gold2 = Column(DECIMAL(precision=12, scale=3), server_default="0", comment="金币2")
    user_gold2_frozen = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="冻结玉佩数")
    user_ticket_rec = Column(INTEGER(display_width=11), server_default="0", comment="海星")
    user_ischarge = Column(TINYINT(display_width=1), nullable=False, server_default="0", comment="是否首冲过了")
    user_exp = Column(INTEGER(display_width=11), server_default="0", comment="经验")
    user_browse = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="空间浏览量")
    user_logintime = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="上次登录时间")
    user_regtime = Column(INTEGER(display_width=11), index=True, server_default="0", nullable=False, comment="注册时间")
    user_regip = Column(VARCHAR(length=15), nullable=False, server_default='0.0.0.0', comment="注册IP")
    user_displaytime = Column(INTEGER(display_width=11), server_default="0", nullable=False,
                              comment="如果是时间段，那么就是封禁的时间段")
    user_nickname_before = Column(TEXT, comment="曾用名")
    user_auth = Column(SMALLINT, nullable=False, server_default="0")
    delete_time = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="逻辑删除时间")
    refresh_token = Column(VARCHAR(length=50), nullable=False, server_default='',
                           comment="存储refresh token和过期时间 用于redis崩溃恢复系统登陆 用|分割")
    nation_code = Column(INTEGER(display_width=11), server_default="86", nullable=False, comment="国家电话代号")
    credit = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="积分")
    close_time = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="注销时间")
    finance_id = Column(INTEGER(display_width=11), server_default="0", nullable=False, comment="财务表Id")
    user_underage_status = Column(SMALLINT, nullable=False, server_default="0", comment="未成年保护 0关闭 1开启")
    attr_limit = Column(VARCHAR(length=20), nullable=False, comment="属性限制，英文逗号分隔，1、昵称；2、头像；3、签名")

    # 添加配置设置编码
    __table_args__ = {
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }

    @classmethod
    def get_user_list(cls):
        r = cls.query.filter(cls.status == cls.STATUS_NORMAL).limit(30).all()
        return r
    
