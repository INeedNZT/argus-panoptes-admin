from .dashboard.dashboard import dashboard_bp
from .login.login import login_bp
from .live.live import live_bp
import os
from flask import redirect


def home():
    return redirect('/dashboard')

def init_bp(app):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    app.static_folder = os.path.join(base_dir, 'static')
    app.template_folder = os.path.join(base_dir, 'templates')
    app.register_blueprint(dashboard_bp,url_prefix="/dashboard")
    app.register_blueprint(login_bp,url_prefix="/login")
    app.register_blueprint(live_bp,url_prefix="/live")
    app.add_url_rule('/', 'redirect_home', home)
