from os import mkdir
from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods =['GET','POST']) 
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('user')
        password = request.form.get('password')
        if (user == 'admin' and password == 'admin'):
            return render_template('index.html')
        else:
            return redirect('/login'), 403



if __name__ == "__main__":
    app.run(host="localhost", port=5000)
