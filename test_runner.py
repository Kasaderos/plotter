import unittest
import plotter_tests

pTestSuite = unittest.TestSuite()
pTestSuite.addTest(unittest.makeSuite(plotter_tests.TestPlotter))
print("count of tests: " + str(pTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(pTestSuite)
