from . import app
from flask import Flask, render_template
import json
import sys
import click
from os import path
from .indexer import Indexer
from .typeahead import Typeahead
from .path import abs_path

indexer = Indexer(app.config)
typeahead = Typeahead(app.config)

@app.route('/', methods=['GET'])
def mainpage():
   return render_template('index.html')

@app.route('/info', methods=['GET'])
def get_info():
   info = dict()
   info['VERSION'] = app.config['VERSION']
   info['FLASK_ENV'] = app.config['FLASK_ENV']
   info['DEBUG'] = app.config['DEBUG']
   info['PUNCTUATION_CHARS'] = app.config['PUNCTUATION_CHARS']
   info['PREFIX_LENGTH'] = app.config['PREFIX_LENGTH']
   info['PQ_SIZE'] = app.config['PQ_SIZE']
   return info

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
   return {"result" : "success"}

@app.route('/search/<prefix>', methods=['GET'])
def suggestion(prefix):
   if app.config['DEBUG']:
      app.logger.info(typeahead.get_typeahead(prefix))
   return typeahead.get_typeahead(prefix)

@app.route('/admin/index/<word>', methods=['POST'])
def update_index(word):
   try:
      typeahead.update_index(word)
      app.logger.info('updated word "'+word+'" to the first element of index')
      return {"result" : "success"}
   except:
      app.logger.error(sys.exc_info())
      return {"result" : "failure"}

@app.route('/admin/index/<word>', methods=['DELETE'])
def delete_index(word):
   try:
      typeahead.delete_index(word)
      app.logger.info('deleted word "'+word+'" from index')
      return {"result" : "success"}
   except:
      app.logger.error(sys.exc_info())
      return {"result" : "failure"}

@app.route('/admin/index/reload', methods=['POST'])
def reload():
   result = typeahead.apply_changes()
   
   if result == True:
      app.logger.info('applied index changes')
      return {"result" : "success"}
   else:
      app.logger.info('nothing to change')
      return {"result" : "failure", "info" : "nothing to change"}
      
   #except:
   #   app.logger.error(sys.exc_info())
   #   return {"result" : "failure"}

@app.cli.command('build-prefix')
def build_prefix():
   indexer.make_prefix()
   app.logger.info('prefix build complete')

if __name__ == "__main__":
   app.run(debug=True, host=app.config['HOST_ADDR'], port=app.config['PORT_NUM'])