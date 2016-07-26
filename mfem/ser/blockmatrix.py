# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_blockmatrix', [dirname(__file__)])
        except ImportError:
            import _blockmatrix
            return _blockmatrix
        if fp is not None:
            try:
                _mod = imp.load_module('_blockmatrix', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _blockmatrix = swig_import_helper()
    del swig_import_helper
else:
    import _blockmatrix
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except Exception:
    weakref_proxy = lambda x: x


import array
import vector
import matrix
import operators
import sparsemat
import densemat
class BlockMatrix(matrix.AbstractSparseMatrix):
    __swig_setmethods__ = {}
    for _s in [matrix.AbstractSparseMatrix]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlockMatrix, name, value)
    __swig_getmethods__ = {}
    for _s in [matrix.AbstractSparseMatrix]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, BlockMatrix, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _blockmatrix.new_BlockMatrix(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def SetBlock(self, i, j, mat):
        return _blockmatrix.BlockMatrix_SetBlock(self, i, j, mat)

    def NumRowBlocks(self):
        return _blockmatrix.BlockMatrix_NumRowBlocks(self)

    def NumColBlocks(self):
        return _blockmatrix.BlockMatrix_NumColBlocks(self)

    def GetBlock(self, *args):
        return _blockmatrix.BlockMatrix_GetBlock(self, *args)

    def IsZeroBlock(self, i, j):
        return _blockmatrix.BlockMatrix_IsZeroBlock(self, i, j)

    def RowOffsets(self, *args):
        return _blockmatrix.BlockMatrix_RowOffsets(self, *args)

    def ColOffsets(self, *args):
        return _blockmatrix.BlockMatrix_ColOffsets(self, *args)

    def RowSize(self, i):
        return _blockmatrix.BlockMatrix_RowSize(self, i)

    def EliminateRowCol(self, ess_bc_dofs, sol, rhs):
        return _blockmatrix.BlockMatrix_EliminateRowCol(self, ess_bc_dofs, sol, rhs)

    def CreateMonolithic(self):
        return _blockmatrix.BlockMatrix_CreateMonolithic(self)

    def PrintMatlab(self, *args):
        return _blockmatrix.BlockMatrix_PrintMatlab(self, *args)

    def Elem(self, *args):
        return _blockmatrix.BlockMatrix_Elem(self, *args)

    def Inverse(self):
        return _blockmatrix.BlockMatrix_Inverse(self)

    def NumNonZeroElems(self):
        return _blockmatrix.BlockMatrix_NumNonZeroElems(self)

    def GetRow(self, row, cols, srow):
        return _blockmatrix.BlockMatrix_GetRow(self, row, cols, srow)

    def EliminateZeroRows(self):
        return _blockmatrix.BlockMatrix_EliminateZeroRows(self)

    def Mult(self, x, y):
        return _blockmatrix.BlockMatrix_Mult(self, x, y)

    def AddMult(self, x, y, val=1.):
        return _blockmatrix.BlockMatrix_AddMult(self, x, y, val)

    def MultTranspose(self, x, y):
        return _blockmatrix.BlockMatrix_MultTranspose(self, x, y)

    def AddMultTranspose(self, x, y, val=1.):
        return _blockmatrix.BlockMatrix_AddMultTranspose(self, x, y, val)
    __swig_destroy__ = _blockmatrix.delete_BlockMatrix
    __del__ = lambda self: None
    __swig_setmethods__["owns_blocks"] = _blockmatrix.BlockMatrix_owns_blocks_set
    __swig_getmethods__["owns_blocks"] = _blockmatrix.BlockMatrix_owns_blocks_get
    if _newclass:
        owns_blocks = _swig_property(_blockmatrix.BlockMatrix_owns_blocks_get, _blockmatrix.BlockMatrix_owns_blocks_set)
BlockMatrix_swigregister = _blockmatrix.BlockMatrix_swigregister
BlockMatrix_swigregister(BlockMatrix)


def Transpose(*args):
    return _blockmatrix.Transpose(*args)
Transpose = _blockmatrix.Transpose

def Mult(*args):
    return _blockmatrix.Mult(*args)
Mult = _blockmatrix.Mult
# This file is compatible with both classic and new-style classes.


