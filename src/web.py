
from flask import Flask, render_template

from . import _monitor, _config


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', monitor=_monitor, config=_config)
