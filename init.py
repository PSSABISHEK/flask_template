from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login_action", methods=['POST'])
def login_action():
    # form body
    print(request.form)
    
    # url_for takes in a function name and returns the route
    # e.g. url_for('home') --> '/home'
    # redirect takes in a route and redirects to the route
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return redirect('https://acetechworld.com/')

if __name__ == "__main__":
    app.run()

