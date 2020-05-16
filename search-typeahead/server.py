import config
from flask import Flask, render_template
from flask_restful import Resource, Api
from typeahead import get_typeahead

app = Flask(__name__)

api = Api(app)

class Info(Resource):
   def get(self):
      return '1'

class Health(Resource):
   def get(self):
      return '2'

class Typeahead(Resource):
   def get(self, prefix):
      return get_typeahead(prefix)

class Reload(Resource):
   def post(self):
      return '4'

class Index(Resource):
   def post(self, prefix):
      return prefix

   def delete(self, prefix):
      return prefix

api.add_resource(Info, '/info')
api.add_resource(Health, '/healthcheck')
api.add_resource(Typeahead, '/search/<string:prefix>')
api.add_resource(Reload, '/admin/index/reload')
api.add_resource(Index, '/admin/index/<string:prefix>')

@app.route('/')
def mainpage():
   return render_template('index.html')

if __name__ == "__main__":
   app.run(debug=True, host=config.host_addr, port=config.port_num)