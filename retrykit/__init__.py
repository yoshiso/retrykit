__author__ = 'Sho Yoshida'
__version__ = '0.0.1'
__license__ = 'MIT'

import time


class retry:

    def __init__(self, exc=Exception, tries=3, backoff=2):
        self.tries = tries
        self.backoff = backoff
        self.exc = exc
        self.errors = None

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
