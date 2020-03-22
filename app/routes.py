from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    print("Return HTML page using template.")
    user = {'username': 'Practice Habits'}
    return render_template('index.html', title='Home', user=user)