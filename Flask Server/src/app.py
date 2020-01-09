import os

from flask import Flask, request, render_template

from src.common.database import Database
from src.models.user import User

app = Flask(__name__)

@app.before_first_request
def initial_database():
    Database.initialize()


@app.route('/', methods=['GET'])
def uploader():
    return render_template('upload.html')


@app.route("/", methods=['POST'])
def save():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        image = request.files['image'].read()
        user = User(
            username,
            password,
            image)
        user.save()
    # return
    return "Image Uploaded ML Processing"

if __name__ == "__main__":
    app.run(debug=True)
