from flask import Blueprint

# 在 __init__ 中创建一个统一的蓝图管理对象，各个路由模块需要注册，就在各自的模块中导入这个对象，把路由注册进去就行
web = Blueprint('web', __name__)

# 各个模块导入蓝图对象后，为啥要在这边再导入，各个模块？
# 是因为各个模块没有被调用或者导入不会执行
# 所以在__init__中导入一次
from app.web import book
from app.web import users
