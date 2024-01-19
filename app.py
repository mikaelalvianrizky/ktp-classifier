import os

from flask import Flask
from src.api.routes.ktp import ktpApp

# from src.api.utils import database
# from flask_migrate import Migrate

app = Flask(__name__)

# db_username= os.getenv('DB_USERNAME', 'root')
# db_password = os.getenv('DB_PASSWORD', 'password')
# db_database = os.getenv('DB_DATABASE', 'database')
# db_host = os.getenv('DB_HOST', 'localhost')
# db_port = os.getenv('DB_PORT', '3306')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+db_username+':'+db_password+'@'+db_host+':'+db_port+'/'+db_database+'?charset=utf8mb4'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 #maksimal 100 MB

# migrate = Migrate(app, database)
# # setup all our dependencies
# database.init_app(app)
# migrate.init_app(app, database)

# register blueprint
app.register_blueprint(ktpApp)

# database.db.create_all(app=app)

@app.route('/')
def hello():
	return "Hello, world!"

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80, debug=True)