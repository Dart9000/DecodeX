from flask import Flask,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

STATIC_DIR = os.path.abspath('static')

#Doc
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
app = Flask(__name__, static_folder=STATIC_DIR)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__' :
        app.run(debug=True)
