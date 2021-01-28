from flask import Flask, render_template
from api.api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)