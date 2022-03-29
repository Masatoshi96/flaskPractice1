from multiprocessing.spawn import import_main_path
from flask import Flask
app = Flask(__name__)
import flaskr.main

from flaskr import db
db.create_books_table()