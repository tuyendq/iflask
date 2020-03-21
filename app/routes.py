from app import app

@app.route("/")
@app.route("/index")
def index():
    print("Return HTML page.")
    user = {'username': 'Tuyen'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''