__author__ = 'Sho Yoshida'
__version__ = '0.0.2'
__license__ = 'MIT'

import time
from functools import wraps


class retry:

    def __init__(self, exc=Exception, tries=3, backoff=2):
        self.tries = tries
        self.backoff = backoff
        self.exc = exc
        self.errors = None

    def __call__(self, func):

        @wraps(func)
        def _wrap(*args, **kwargs):
            for ctx in self.trial():
                with ctx:
                    return func(*args, **kwargs)

        return _wrap

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.errors = (exc_type, exc_value, traceback)
        return True

    def trial(self):

        for i in range(self.tries):

            yield self

            if self.errors is None:
                break

            if not isinstance(self.errors[1], self.exc):
                raise self.errors[1]

            if i < self.tries - 1:
                time.sleep(i**self.backoff)

        if self.errors:
            raise self.errors[1]
