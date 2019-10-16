from flask import Flask, render_template, redirect, url_for, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')
