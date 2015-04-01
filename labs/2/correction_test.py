#!/usr/bin/python2
import unittest
import os
import sys
import correction
import time
from StringIO import StringIO

class CorrectionTests(unittest.TestCase):
    def setUp(self):
        self.corr = correction.Correction()
        self.out = StringIO()
        sys.stdout = self.out

    def test_regular_direction(self):
        self.corr.report(1)
        time.sleep(3)
        self.corr.term()
        output = self.out.getvalue().strip()
        self.assertEqual(output, "Disturbance: 1, correcting by: -1", "incorrect output")

    def test_reverse_direction(self):
        self.corr.report(-1)
        time.sleep(3)
        self.corr.term()
        output = self.out.getvalue().strip()
        self.assertEqual(output, "Disturbance: -1, correcting by: 1", "incorrect output")

    def tearDown(self):
        self.corr.term()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CorrectionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)