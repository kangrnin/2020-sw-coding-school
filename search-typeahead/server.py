from flask import Flask, render_template
from flask_restful import Resource, Api
from prefix import get_suggestion

app = Flask(__name__)

api = Api(app)

class Info(Resource):
   def get(self):
      return '1'

class Health(Resource):
   def get(self):
      return '2'

class Suggestion(Resource):
   def get(self, prefix):
      return get_suggestion(prefix)

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
api.add_resource(Suggestion, '/search/<string:prefix>')
api.add_resource(Reload, '/admin/index/reload')
api.add_resource(Index, '/admin/index/<string:prefix>')

@app.route('/')
def mainpage():
   return render_template('index.html')

host_addr = "127.0.0.1"
port_num = "8080"

if __name__ == "__main__":
   app.run(debug=True, host=host_addr, port=port_num)