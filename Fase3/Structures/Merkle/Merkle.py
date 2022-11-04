# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _Merkle
else:
    import _Merkle

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Merkle.delete_SwigPyIterator

    def value(self):
        return _Merkle.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Merkle.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Merkle.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Merkle.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Merkle.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Merkle.SwigPyIterator_copy(self)

    def next(self):
        return _Merkle.SwigPyIterator_next(self)

    def __next__(self):
        return _Merkle.SwigPyIterator___next__(self)

    def previous(self):
        return _Merkle.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Merkle.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Merkle.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Merkle.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Merkle.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Merkle.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Merkle.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Merkle.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _Merkle:
_Merkle.SwigPyIterator_swigregister(SwigPyIterator)

SHARED_PTR_DISOWN = _Merkle.SHARED_PTR_DISOWN
class DataNode(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    value = property(_Merkle.DataNode_value_get, _Merkle.DataNode_value_set)

    def __init__(self, value):
        _Merkle.DataNode_swiginit(self, _Merkle.new_DataNode(value))
    __swig_destroy__ = _Merkle.delete_DataNode

# Register DataNode in _Merkle:
_Merkle.DataNode_swigregister(DataNode)

class HashNode(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    hash = property(_Merkle.HashNode_hash_get, _Merkle.HashNode_hash_set)
    value = property(_Merkle.HashNode_value_get, _Merkle.HashNode_value_set)
    left = property(_Merkle.HashNode_left_get, _Merkle.HashNode_left_set)
    right = property(_Merkle.HashNode_right_get, _Merkle.HashNode_right_set)

    def __init__(self, hash):
        _Merkle.HashNode_swiginit(self, _Merkle.new_HashNode(hash))
    __swig_destroy__ = _Merkle.delete_HashNode

# Register HashNode in _Merkle:
_Merkle.HashNode_swigregister(HashNode)

class Merkle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    tophash = property(_Merkle.Merkle_tophash_get, _Merkle.Merkle_tophash_set)
    index = property(_Merkle.Merkle_index_get, _Merkle.Merkle_index_set)
    datablock = property(_Merkle.Merkle_datablock_get, _Merkle.Merkle_datablock_set)
    sha = property(_Merkle.Merkle_sha_get, _Merkle.Merkle_sha_set)

    def __init__(self):
        _Merkle.Merkle_swiginit(self, _Merkle.new_Merkle())

    def add(self, value):
        return _Merkle.Merkle_add(self, value)

    def createTree(self, exp):
        return _Merkle.Merkle_createTree(self, exp)

    def _createTree(self, temp, exp):
        return _Merkle.Merkle__createTree(self, temp, exp)

    def genhash(self, temp, exp):
        return _Merkle.Merkle_genhash(self, temp, exp)

    def preorder(self, temp):
        return _Merkle.Merkle_preorder(self, temp)

    def auth(self):
        return _Merkle.Merkle_auth(self)

    def ramas_dot(self, nodo):
        return _Merkle.Merkle_ramas_dot(self, nodo)

    def dotget(self):
        return _Merkle.Merkle_dotget(self)

    def eliminar(self):
        return _Merkle.Merkle_eliminar(self)
    __swig_destroy__ = _Merkle.delete_Merkle

# Register Merkle in _Merkle:
_Merkle.Merkle_swigregister(Merkle)



