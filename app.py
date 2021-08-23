from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from helper_function import salt
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://beca0a61b96da0:2ee13097@us-cdbr-east-04.cleardb.com/heroku_130f9e0233f5e49'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        _username = request.form['username']
        _email = request.form['email']
        _password = request.form['password']

        salted = salt(_password)
        hashed = bcrypt.generate_password_hash(salted)

        try:
            new_user = User(username=_username,
                            email = _email,
                            password = hashed)
            db.session.add(new_user)
            db.session.commit()
        except:
            print(f'error happened')
            return redirect('/')

        return redirect('/')

    return render_template('Signup.html')

if __name__ ==  '__main__':
    app.run(debug=True)
