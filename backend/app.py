from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
from models import db, User, Category, Expense, Budget

load_dotenv()

app = Flask(__name__)
CORS(app)

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{quote_plus(db_password)}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return jsonify({"message": "Spendlytics backend is running"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
