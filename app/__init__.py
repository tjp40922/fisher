from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    # 导入配置文件
    app.config.from_object('app.settings')
    app.config.from_object('app.secure')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
