from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/home")   #for the same server we can have multiple routes
def index():
    return "<H1>Welcome to home page</H1>"


@app.route("/about")
def about():
    return "<H1>Welcome to about page</H1>"

if __name__ == "__main__":
    app.run(debug = True)    