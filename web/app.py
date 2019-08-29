from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()


@app.route('/')
def index():
    return render_template('idx.html')


if __name__ == '__main__':
    app.run()
