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

   PATH_SOURCE_TEXT = 'data/pro/text.txt'
   PATH_WORD_COUNT = 'data/pro/wordcount.bin'
   PATH_PREFIX_INDEX = 'data/pro/prefix.bin'
   PATH_PREFIX_UPDATE = 'data/pro/prefix.bin'
   PATH_PREFIX_DELETE = 'data/pro/prefix.bin'

class DevelopmentConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   TESTING = True
   PORT_NUM = '3000'

   PATH_SOURCE_TEXT = 'data/dev/text.txt'
   PATH_WORD_COUNT = 'data/dev/wordcount.bin'
   PATH_PREFIX_INDEX = 'data/dev/prefix.bin'
   PATH_PREFIX_UPDATE = 'data/dev/prefix_update.bin'
   PATH_PREFIX_DELETE = 'data/dev/prefix_delete.bin'
