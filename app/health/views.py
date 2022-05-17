from flask import render_template
from . import health

@health.route('/')
def healthhome():
    return render_template('health/healthhome.html')