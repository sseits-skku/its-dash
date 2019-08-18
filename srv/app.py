from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import CONFIG

app = Flask(__name__)
app.config.update(**CONFIG)
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
