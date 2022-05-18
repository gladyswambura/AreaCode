from flask import render_template, request
from . import main
from flask_login import login_required


# Views
@main.route('/')
def index():
 
    title = 'Area Code | Live Freely'
    return render_template('index.html', title=title)

