from flask import Response

from main import app


# this file is only for local development
# static files are located outside the Flask environment in a static folder for Firebase
@app.get('/style.css')
def style_css():
    f = open('../../static/style.css', 'r')
    return Response(f.read(), mimetype='text/css')
