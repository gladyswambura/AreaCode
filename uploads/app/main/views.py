from flask import render_template
from app import app

# Views
@app.route('/')
def uploads():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('uploads.html')