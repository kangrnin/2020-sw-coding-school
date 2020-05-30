from flask import Flask, render_template
import json
import click
from .indexer import Indexer
from .typeahead import Typeahead
from .path import abs_path
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object('search-typeahead.config.DevelopmentConfig')