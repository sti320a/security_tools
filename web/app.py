from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


class SSHLog(db.Model):
    # TODO: move to models dir
    id = db.Column(db.Integer, primary_key=True)
    from_ip = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64))
    accessed_at = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'SSHLOG <{self.id}>'


@app.route('/')
def index():
    return render_template('idx.html')


@app.route('/test')
def test():
    # TEST
    db.create_all()
    log = SSHLog(from_ip='127.0.0.1', username='root')
    db.session.add(log)
    db.session.commit()
    logs = SSHLog.query.all()
    return render_template('idx.html', logs=logs)


def insert_log_to_db(log_file_path: str) -> bool:
    with open(log_file_path, 'r') as f:
        log_text = f.read()
        print(log_text)
        f.close()

    return False


if __name__ == '__main__':
    app.run()
