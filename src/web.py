
from flask import Flask, render_template, url_for

from . import _monitor, _config


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html.j2', monitor=_monitor, config=_config,
                           stylesheet=url_for('static', filename='style.css'),
                           script=url_for('static', filename='packages.js'))
