from flask import Flask, render_template
from datetime import timedelta
from api.api import api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'starfruit'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.permanent_session_lifetime = timedelta(365)

db = SQLAlchemy(app)

class Alunos(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Gabaritos(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)


app.register_blueprint(api, url_prefix='/api')

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/alunos')
def alunos():
    return render_template('alunos.html')
@app.route('/gabaritos')
def gabaritos():
    return render_template('gabaritos.html')
if __name__ == '__main__':
    app.run(debug=True)