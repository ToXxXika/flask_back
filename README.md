# Flask_Backend

This project is a part of Backend for an AI model Handling in the database
## Authors
ToXxXika : [GITHUB](https://github.com/ToXxXika) to contact me 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install flask flask_sqlalchemy mysqlclient faker flask-cors
```

## Usage

```python
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


```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

