from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
# from test_model import Person
import os
from mysql_model import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PORT'] = os.getenv('PORT')
db = SQLAlchemy(app)

@app.route('/try_html')
def try_html():
    return render_template('try_html.html')

@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
