from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "The default, 'root' route"
@app.route("/hello/<name>")
def hello(name=None):
    user = {'name': name}
    return render_template('hello.html',user=user)
@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world :("

@app.route("/private")
def private():
    # test user login fail
    # redirect to login URL
    return redirect(url_for('login'))
@app.route('/upload/', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/upload.png')
        return "File Uploaded"
    else:
        page='''
        <html>
        <body>
        <form action="" method="post" name="form" enctype="multipart/form-data">
            <input type="file" name="datafile"/>
            <input type="submit" name="submit" id="submit"/>
        </form>
        </body>
        </html>
        '''
        return page,200
@app.route('/login')
def login():
    return "Now we would get username and password"

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested.", 404

@app.route('/display/<file>')
def static_example_img(file):
    imgLoc = 'uploads/' + file

    start = '<img src="'
    url = url_for('static', filename=imgLoc)
    end = '">'
    return start+url+end, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

