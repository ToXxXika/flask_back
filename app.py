from flask import Flask, request, redirect, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from faker import Faker
from flask_cors import CORS, cross_origin
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

app = Flask(__name__)
CORS(app)
fake = Faker()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.username


def generate_fake_data():
    for i in range(100):
        user = Users(username=fake.name(), password=fake.password())
        db.session.add(user)
        db.session.commit()


@app.route('/')
def database_definition():
    db.create_all()
    return 'Database created'


@app.route('/generate')
@cross_origin()
def mock_data_route():
    generate_fake_data()
    return 'Mock data created!'


@app.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    try:
        signup_data = request.get_json()
        username = signup_data['username']
        password = signup_data['password']
        print(username)
        print(password)
        user = Users(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 200, 'message': 'User created successfully'})
    except SQLAlchemyError:
        return jsonify({'status': 500, 'message': 'Internal server error'})


@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 400, 'message': 'No file part'})
    file = request.files['file']
    image = mpimg.imread(file)
    plt.imshow(image)
    plt.show()


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    try:
        login_data = request.get_json()
        username = login_data['username']
        password = login_data['password']
        print(username)
        print(password)
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return jsonify({'status': 401, 'message': 'User not found'})
        if user.password == password:
            return jsonify({'status': 200, 'message': 'Login successful'})
        else:
            return jsonify({'status': 401, 'message': 'Invalid password'})
    except SQLAlchemyError:
        return jsonify({'status': 500, 'message': 'Internal server error'})


if __name__ == '__main__':
    app.run()
