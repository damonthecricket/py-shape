
import unittest

from . import test_shapes


loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests( loader.loadTestsFromModule(test_shapes) )

runner = unittest.TextTestRunner(verbosity = 3)
result = runner.run(suite)