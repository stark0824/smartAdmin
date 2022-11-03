# +----------------------------------------------------------------------
# | Author:Stark
# +----------------------------------------------------------------------
# | Date:2022/11/03
# +----------------------------------------------------------------------
# | Desc: 智慧后台 v0.1 - 框架路由装载器
# +----------------------------------------------------------------------
class BaseRoutes:
    def __init__(self, name):
        self.name = name
        self.loader = []

    def route(self, rule, **options):
        def decorator(f):
            self.loader.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=''):
        # 依次注册蓝图
        for f, rule, options in self.loader:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)