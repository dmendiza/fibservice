# -*- coding: utf-8 -*-
"""
    fibservice
    ----------
    Simple web service using Flask.
"""
from flask import Flask, jsonify
from werkzeug.routing import BaseConverter


app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


def fibonacci(size):
    """Returns a Fibonacci series list of requested size."""
    fib = [0, 1]
    if size < 3:
        return fib[0: size]
    for index in range(2, size):
        fib.append(fib[index - 2] + fib[index - 1])
    return fib


@app.route('/fibonacci/<int:size>')
def get_fibonacci(size):
    if size > 1500:
        response = jsonify(error='Fibonacci sequence size must be less than 1,500.')
        response.status_code = 400
        return response
    return jsonify(fibonacci=fibonacci(size))


@app.route('/fibonacci/<regex("-\d+"):size>')
def get_negative_error(size):
    response = jsonify(error='Fibonacci sequence size must be zero or a positive integer.')
    response.status_code = 400
    return response


if __name__ == '__main__':
    app.run()
