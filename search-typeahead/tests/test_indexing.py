import unittest
from ..src.indexer import make_wordcount
from ..src.indexer import make_prefix

class TestIndexing(unittest.case.TestCase):
    def test_indexing(self):
        make_wordcount()
        make_prefix()
        
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()