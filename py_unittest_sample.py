# -*- coding: utf-8 -*-
import os, sys, unittest

class Sample():
	"""Target class for test"""
	# target method for test
	def return_hoge(self):
		return 'hoge'

	# target method for test
	def return_poyo(self):
		return 'poyo'

class SampleTest(unittest.TestCase):
	"""Test class for Sample class"""
	CLS_VAL = 'none'

	# called once when initializing class (python2.7 and higher)
	@classmethod
	def setUpClass(cls):
		if sys.flags.debug: print('> setUpClass method is called.')
		cls.CLS_VAL = '> setUpClass : initialized!'
		if sys.flags.debug: print(cls.CLS_VAL)

	# called once when releasing class (python2.7 and higher)
	@classmethod
	def tearDownClass(cls):
		if sys.flags.debug: print('> tearDownClass method is called.')
		cls.CLS_VAL = '> tearDownClass : released!'
		if sys.flags.debug: print(cls.CLS_VAL)

	# called everytime when calling each test methods
	def setUp(self):
		if sys.flags.debug: print(os.linesep + '> setUp method is called.')
		self.smpl = Sample()

	# called everytime when after calling each test method
	def tearDown(self):
		if sys.flags.debug: print(os.linesep + '> tearDown method is called.')

	def test_hoge(self):
		expected = 'hoge'
		actual = self.smpl.return_hoge()
		self.assertEqual(expected, actual)

	def test_poyo(self):
		expected = 'poyo'
		actual = self.smpl.return_hoge() # typo here!
		self.assertEqual(expected, actual)

if __name__ == '__main__':
	# run unittest. execution order will be setUpClass -> (setUp, test_method, tearDown) -> tearDownClass
	unittest.main()