from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from config import Config
from datetime import datetime
import re

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
    db.create_all()
    logs = SSHLog.query.order_by(desc(SSHLog.accessed_at)).all()
    return render_template('idx.html', logs=logs)


def insert_log_to_db(log_file_path: str) -> bool:
    with open(log_file_path, 'r') as f:
        log_text = f.readlines()
        for row in log_text:
            if 'Failed' in row and 'invalid user' in row:
                row = row.rstrip('\n').rstrip('\r\n')

                # Extract username
                match_obj = re.search(
                    r'user.*from',
                    row
                )
                username = match_obj.group(0)[5:-5]

                # Extract from_ip
                match_obj = re.search(
                    r'from.*port',
                    row
                )
                from_ip = match_obj.group(0)[5:-5]

                # Extract accessed_at
                accessed_at = row[0:15]
                accessed_at = datetime.strptime(
                    accessed_at,
                    '%b %d %H:%M:%S'
                )

                # Insert log
                log = SSHLog(
                    from_ip=from_ip,
                    username=username,
                    accessed_at=accessed_at
                )
                db.session.add(log)
                db.session.commit()

        f.close()

    return True


if __name__ == '__main__':
    app.run()
