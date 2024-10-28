from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "The default, 'root' route"
@app.route("/hello/")
def hello():
    return "Hello Napier!!! :3"
@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world :("

@app.route("/private")
def private():
    # test user login fail
    # redirect to login URL
    return redirect(url_for('login'))
@app.route('/login')
def login():
    return "Now we would get username and password"

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

