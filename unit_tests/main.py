
import unittest

from . import test_shape


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_shape) )

runner = unittest.TextTestRunner(verbosity = 1)
result = runner.run(suite)