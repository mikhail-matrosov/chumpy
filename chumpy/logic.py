"""
Author(s): Matthew Loper

See LICENCE.txt for licensing and contact information.
"""

from .ch import Ch
import numpy as np

__author__ = 'Matthew Loper'
__all__ = []  # added to incrementally below


class LogicFunc(Ch):
    dterms = 'a'  # we keep this here so that changes to children of "a" will trigger cache changes
    terms = 'args', 'kwargs', 'funcname'

    def compute_r(self):
        arr = self.a
        fn = getattr(np, self.funcname)
        return fn(arr, *self.args, **self.kwargs)

    def compute_dr_wrt(self, wrt):
        pass


def all(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='all')


def any(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='any')


def isfinite(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='isfinite')


def isinf(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='isinf')


def isnan(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='isnan')


def isneginf(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='isneginf')


def isposinf(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='isposinf')


def logical_not(a, *args, **kwargs):
    return LogicFunc(a=a, args=args, kwargs=kwargs, funcname='logical_not')


if __name__ == '__main__':
    print all(np.array([1, 2, 3]))
    print isinf(np.array([0, 2, 3]))
