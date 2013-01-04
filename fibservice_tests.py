# -*- coding: utf-8 -*-
"""
    fibservice tests
    ----------------
"""
import unittest
import fibservice
from flask import json


class FibonacciServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fibservice.app.test_client()

    def test_fibonacci_of_zero_length(self):
        rv = self.app.get('/fibonacci/0')
        assert 'fibonacci' in rv.data
        data = json.loads(rv.data)
        fib = data['fibonacci']
        assert not len(fib)

    def test_fibonacci_response(self):
        """Check length and correct values"""
        rv = self.app.get('/fibonacci/5')
        assert 'fibonacci' in rv.data
        data = json.loads(rv.data)
        fib = data['fibonacci']
        assert len(fib) == 5
        assert 0 == fib[0]
        assert 1 == fib[1]
        assert 3 == fib[-1]

    def test_negative_length_error(self):
        rv = self.app.get('/fibonacci/-5')
        assert 400 == rv.status_code
        assert 'error' in rv.data

    def test_fibonacci_size_limit(self):
        rv = self.app.get('/fibonacci/1501')
        assert 400 == rv.status_code
        assert 'error' in rv.data
    
    def test_bad_length(self):
        rv = self.app.get('/fibonacci/foo')
        assert 404 == rv.status_code


if __name__ == '__main__':
	unittest.main()
