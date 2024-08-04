# flask_app/__init__.py
from flask import Flask
import os
import gspread
app=Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a strong random secret key
from flask_app import routes