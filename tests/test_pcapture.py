import unittest

import pcapture

class TestPCapture(unittest.TestCase):

    def test_has_version(self):
        self.assertTrue(pcapture.__version__)
