from flask import render_template
from . import main



# Views
@main.route('/')
def index():
    title = 'Area Code | Live Freely'
    return render_template('index.html', title=title)

