from app import app

@app.route("/")
@app.route("/index")
def index():
    print("Handling request from home page.")
    return "Hello Azure! First Python webapp with Flask."