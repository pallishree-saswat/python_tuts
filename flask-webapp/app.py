
from flask import Flask
from db import db



app = Flask(__name__)

app.config.from_object('config.Config')
db.init_app(app)


from routes.index import *


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
