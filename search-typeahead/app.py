from . import app
from flask import Flask, render_template
import json
import sys
import click
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
   print(app.config)
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

@app.route('/admin/index/reload', methods=['POST'])
def reload():
   try:
      typeahead.apply_changes()
      indexer.make_prefix(typeahead.index)
      app.logger.info('applied index changes')
      return {"result" : "success"}
   except:
      app.logger.error(sys.exc_info())
      return {"result" : "failure"}
   

@app.route('/admin/index/<prefix>', methods=['POST'])
def update_index(prefix):
   try:
      indexer.update_index(prefix)
      app.logger.info('updated word "'+prefix+'" to the first element of index')
      return {"result" : "success"}
   except:
      app.logger.error(sys.exc_info())
      return {"result" : "failure"}

@app.route('/admin/index/<prefix>', methods=['DELETE'])
def delete_index(prefix):
   try:
      indexer.delete_index(prefix)
      app.logger.info('deleted word "'+prefix+'" from index')
      return {"result" : "success"}
   except:
      app.logger.error(sys.exc_info())
      return {"result" : "failure"}

@app.cli.command('make-prefix')
def make_prefix():
   indexer.make_wordcount()
   indexer.make_prefix()
   app.logger.info('prefix build complete')

if __name__ == "__main__":
   app.run(debug=True, host=app.config['HOST_ADDR'], port=app.config['PORT_NUM'])