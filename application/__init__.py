from flask import Flask
from .container_cell import bp as container_bp
from .auth import bp as auth_bp
from .examine import bp as examine_bp
from .samplefrom import bp as samplefrom_bp
from .collection import bp as collection_bp
from .analyse import bp as analyse_bp
from flask_cors import CORS
from .config import config 
def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)  # 解决跨域问题，注册CORS, "/*" 允许访问所有api
    app.register_blueprint(container_bp)
    app.register_blueprint(examine_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(samplefrom_bp)
    app.register_blueprint(collection_bp)
    app.register_blueprint(analyse_bp)
    app.config.from_object(config["dev"])
    app.config['JSON_SORT_KEYS'] = False
    return app

