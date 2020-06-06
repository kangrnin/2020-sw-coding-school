class BaseConfig(object):
   VERSION = '1.4'

   HOST_ADDR = '127.0.0.1'
   PORT_NUM = '8080'

   PUNCTUATION_CHARS = '=_;:!?.,--—*[]{}()#$%`&"“”\'‘’'
   PREFIX_LENGTH = 5
   PQ_SIZE = 8

class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   DEBUG = False
   TESTING = False

   PATH_SOURCE = 'data/pro/text.txt'
   PATH_INDEX = 'data/pro/VERSION/index.bin'
   PATH_UPDATE = 'data/pro/VERSION/update.bin'
   PATH_DELETE = 'data/pro/VERSION/delete.bin'

class DevelopmentConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   TESTING = True
   PORT_NUM = '3000'

   PATH_SOURCE = 'data/dev/text.txt'
   PATH_INDEX = 'data/dev/VERSION/index.bin'
   PATH_UPDATE = 'data/dev/VERSION/update.bin'
   PATH_DELETE = 'data/dev/VERSION/delete.bin'
