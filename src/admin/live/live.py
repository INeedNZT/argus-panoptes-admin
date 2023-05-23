from flask import Blueprint, render_template

live_bp = Blueprint('live',__name__, template_folder='templates', static_folder='static')

@live_bp.route('/')
def view():
    return render_template('live.html')
