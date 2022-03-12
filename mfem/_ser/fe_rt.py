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
    from . import _fe_rt
else:
    import _fe_rt

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _fe_rt.SWIG_PyInstanceMethod_New
_swig_new_static_method = _fe_rt.SWIG_PyStaticMethod_New

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


import weakref

import mfem._ser.fe_base
import mfem._ser.intrules
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.geom
import mfem._ser.densemat
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.element
import mfem._ser.globals
import mfem._ser.table
import mfem._ser.hash
class RT_QuadrilateralElement(mfem._ser.fe_base.VectorTensorFiniteElement):
    r"""Proxy of C++ mfem::RT_QuadrilateralElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(RT_QuadrilateralElement self, int const p, int const cb_type=GaussLobatto, int const ob_type=GaussLegendre) -> RT_QuadrilateralElement"""
        _fe_rt.RT_QuadrilateralElement_swiginit(self, _fe_rt.new_RT_QuadrilateralElement(*args, **kwargs))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_QuadrilateralElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_QuadrilateralElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_QuadrilateralElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_QuadrilateralElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_QuadrilateralElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_CalcDivShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_QuadrilateralElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_QuadrilateralElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_QuadrilateralElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_QuadrilateralElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_QuadrilateralElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_QuadrilateralElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_GetTransferMatrix)

    def ProjectFromNodes(self, vc, Trans, dofs):
        r"""ProjectFromNodes(RT_QuadrilateralElement self, Vector vc, mfem::ElementTransformation & Trans, Vector dofs)"""
        return _fe_rt.RT_QuadrilateralElement_ProjectFromNodes(self, vc, Trans, dofs)
    ProjectFromNodes = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_ProjectFromNodes)

    def ProjectMatrixCoefficient(self, mc, T, dofs):
        r"""ProjectMatrixCoefficient(RT_QuadrilateralElement self, mfem::MatrixCoefficient & mc, mfem::ElementTransformation & T, Vector dofs)"""
        return _fe_rt.RT_QuadrilateralElement_ProjectMatrixCoefficient(self, mc, T, dofs)
    ProjectMatrixCoefficient = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_ProjectMatrixCoefficient)

    def Project(self, *args):
        r"""
        Project(RT_QuadrilateralElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_QuadrilateralElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_QuadrilateralElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        Project(RT_QuadrilateralElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_QuadrilateralElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_QuadrilateralElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_Project)

    def ProjectGrad(self, fe, Trans, grad):
        r"""ProjectGrad(RT_QuadrilateralElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix grad)"""
        return _fe_rt.RT_QuadrilateralElement_ProjectGrad(self, fe, Trans, grad)
    ProjectGrad = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_ProjectGrad)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_QuadrilateralElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_QuadrilateralElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_QuadrilateralElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_QuadrilateralElement

# Register RT_QuadrilateralElement in _fe_rt:
_fe_rt.RT_QuadrilateralElement_swigregister(RT_QuadrilateralElement)

class RT_HexahedronElement(mfem._ser.fe_base.VectorTensorFiniteElement):
    r"""Proxy of C++ mfem::RT_HexahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(RT_HexahedronElement self, int const p, int const cb_type=GaussLobatto, int const ob_type=GaussLegendre) -> RT_HexahedronElement"""
        _fe_rt.RT_HexahedronElement_swiginit(self, _fe_rt.new_RT_HexahedronElement(*args, **kwargs))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_HexahedronElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_HexahedronElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_HexahedronElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_HexahedronElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_HexahedronElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_CalcDivShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_HexahedronElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_HexahedronElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_HexahedronElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_HexahedronElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_HexahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_HexahedronElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_GetTransferMatrix)

    def ProjectFromNodes(self, vc, Trans, dofs):
        r"""ProjectFromNodes(RT_HexahedronElement self, Vector vc, mfem::ElementTransformation & Trans, Vector dofs)"""
        return _fe_rt.RT_HexahedronElement_ProjectFromNodes(self, vc, Trans, dofs)
    ProjectFromNodes = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_ProjectFromNodes)

    def ProjectMatrixCoefficient(self, mc, T, dofs):
        r"""ProjectMatrixCoefficient(RT_HexahedronElement self, mfem::MatrixCoefficient & mc, mfem::ElementTransformation & T, Vector dofs)"""
        return _fe_rt.RT_HexahedronElement_ProjectMatrixCoefficient(self, mc, T, dofs)
    ProjectMatrixCoefficient = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_ProjectMatrixCoefficient)

    def Project(self, *args):
        r"""
        Project(RT_HexahedronElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_HexahedronElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_HexahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        Project(RT_HexahedronElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_HexahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_HexahedronElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_Project)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_HexahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_HexahedronElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_HexahedronElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_HexahedronElement

# Register RT_HexahedronElement in _fe_rt:
_fe_rt.RT_HexahedronElement_swigregister(RT_HexahedronElement)

class RT_TriangleElement(mfem._ser.fe_base.VectorFiniteElement):
    r"""Proxy of C++ mfem::RT_TriangleElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(RT_TriangleElement self, int const p) -> RT_TriangleElement"""
        _fe_rt.RT_TriangleElement_swiginit(self, _fe_rt.new_RT_TriangleElement(p))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_TriangleElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_TriangleElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_TriangleElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_TriangleElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_TriangleElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_TriangleElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_TriangleElement_CalcDivShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_TriangleElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_TriangleElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_TriangleElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_TriangleElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_TriangleElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_TriangleElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_TriangleElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_TriangleElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_TriangleElement_GetTransferMatrix)

    def ProjectFromNodes(self, vc, Trans, dofs):
        r"""ProjectFromNodes(RT_TriangleElement self, Vector vc, mfem::ElementTransformation & Trans, Vector dofs)"""
        return _fe_rt.RT_TriangleElement_ProjectFromNodes(self, vc, Trans, dofs)
    ProjectFromNodes = _swig_new_instance_method(_fe_rt.RT_TriangleElement_ProjectFromNodes)

    def ProjectMatrixCoefficient(self, mc, T, dofs):
        r"""ProjectMatrixCoefficient(RT_TriangleElement self, mfem::MatrixCoefficient & mc, mfem::ElementTransformation & T, Vector dofs)"""
        return _fe_rt.RT_TriangleElement_ProjectMatrixCoefficient(self, mc, T, dofs)
    ProjectMatrixCoefficient = _swig_new_instance_method(_fe_rt.RT_TriangleElement_ProjectMatrixCoefficient)

    def Project(self, *args):
        r"""
        Project(RT_TriangleElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_TriangleElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_TriangleElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        Project(RT_TriangleElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_TriangleElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_TriangleElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_TriangleElement_Project)

    def ProjectGrad(self, fe, Trans, grad):
        r"""ProjectGrad(RT_TriangleElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix grad)"""
        return _fe_rt.RT_TriangleElement_ProjectGrad(self, fe, Trans, grad)
    ProjectGrad = _swig_new_instance_method(_fe_rt.RT_TriangleElement_ProjectGrad)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_TriangleElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_TriangleElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_TriangleElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_TriangleElement

# Register RT_TriangleElement in _fe_rt:
_fe_rt.RT_TriangleElement_swigregister(RT_TriangleElement)

class RT_TetrahedronElement(mfem._ser.fe_base.VectorFiniteElement):
    r"""Proxy of C++ mfem::RT_TetrahedronElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(RT_TetrahedronElement self, int const p) -> RT_TetrahedronElement"""
        _fe_rt.RT_TetrahedronElement_swiginit(self, _fe_rt.new_RT_TetrahedronElement(p))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_TetrahedronElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_TetrahedronElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_TetrahedronElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_TetrahedronElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_TetrahedronElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_CalcDivShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_TetrahedronElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_TetrahedronElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_TetrahedronElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_TetrahedronElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_TetrahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_TetrahedronElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_GetTransferMatrix)

    def ProjectFromNodes(self, vc, Trans, dofs):
        r"""ProjectFromNodes(RT_TetrahedronElement self, Vector vc, mfem::ElementTransformation & Trans, Vector dofs)"""
        return _fe_rt.RT_TetrahedronElement_ProjectFromNodes(self, vc, Trans, dofs)
    ProjectFromNodes = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_ProjectFromNodes)

    def ProjectMatrixCoefficient(self, mc, T, dofs):
        r"""ProjectMatrixCoefficient(RT_TetrahedronElement self, mfem::MatrixCoefficient & mc, mfem::ElementTransformation & T, Vector dofs)"""
        return _fe_rt.RT_TetrahedronElement_ProjectMatrixCoefficient(self, mc, T, dofs)
    ProjectMatrixCoefficient = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_ProjectMatrixCoefficient)

    def Project(self, *args):
        r"""
        Project(RT_TetrahedronElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_TetrahedronElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_TetrahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        Project(RT_TetrahedronElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_TetrahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_TetrahedronElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_Project)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_TetrahedronElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_TetrahedronElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_TetrahedronElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_TetrahedronElement

# Register RT_TetrahedronElement in _fe_rt:
_fe_rt.RT_TetrahedronElement_swigregister(RT_TetrahedronElement)

class RT_WedgeElement(mfem._ser.fe_base.VectorFiniteElement):
    r"""Proxy of C++ mfem::RT_WedgeElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(RT_WedgeElement self, int const p) -> RT_WedgeElement"""
        _fe_rt.RT_WedgeElement_swiginit(self, _fe_rt.new_RT_WedgeElement(p))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_WedgeElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_WedgeElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_WedgeElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_WedgeElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_WedgeElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_WedgeElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_WedgeElement_CalcDivShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_WedgeElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_WedgeElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_WedgeElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_WedgeElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_WedgeElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_WedgeElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_WedgeElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_WedgeElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_WedgeElement_GetTransferMatrix)

    def ProjectMatrixCoefficient(self, mc, T, dofs):
        r"""ProjectMatrixCoefficient(RT_WedgeElement self, mfem::MatrixCoefficient & mc, mfem::ElementTransformation & T, Vector dofs)"""
        return _fe_rt.RT_WedgeElement_ProjectMatrixCoefficient(self, mc, T, dofs)
    ProjectMatrixCoefficient = _swig_new_instance_method(_fe_rt.RT_WedgeElement_ProjectMatrixCoefficient)

    def Project(self, *args):
        r"""
        Project(RT_WedgeElement self, mfem::Coefficient & coeff, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_WedgeElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_WedgeElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        Project(RT_WedgeElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_WedgeElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_WedgeElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_WedgeElement_Project)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_WedgeElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_WedgeElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_WedgeElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_WedgeElement

# Register RT_WedgeElement in _fe_rt:
_fe_rt.RT_WedgeElement_swigregister(RT_WedgeElement)

class RT_R1D_SegmentElement(mfem._ser.fe_base.VectorFiniteElement):
    r"""Proxy of C++ mfem::RT_R1D_SegmentElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(RT_R1D_SegmentElement self, int const p, int const cb_type=GaussLobatto, int const ob_type=GaussLegendre) -> RT_R1D_SegmentElement"""
        _fe_rt.RT_R1D_SegmentElement_swiginit(self, _fe_rt.new_RT_R1D_SegmentElement(*args, **kwargs))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_R1D_SegmentElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_R1D_SegmentElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_R1D_SegmentElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_R1D_SegmentElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_R1D_SegmentElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_R1D_SegmentElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_R1D_SegmentElement_CalcDivShape)

    def Project(self, *args):
        r"""
        Project(RT_R1D_SegmentElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_R1D_SegmentElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_R1D_SegmentElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_R1D_SegmentElement_Project)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_R1D_SegmentElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_R1D_SegmentElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_R1D_SegmentElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_R1D_SegmentElement

# Register RT_R1D_SegmentElement in _fe_rt:
_fe_rt.RT_R1D_SegmentElement_swigregister(RT_R1D_SegmentElement)

class RT_R2D_SegmentElement(mfem._ser.fe_base.VectorFiniteElement):
    r"""Proxy of C++ mfem::RT_R2D_SegmentElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(RT_R2D_SegmentElement self, int const p, int const ob_type=GaussLegendre) -> RT_R2D_SegmentElement"""
        _fe_rt.RT_R2D_SegmentElement_swiginit(self, _fe_rt.new_RT_R2D_SegmentElement(*args, **kwargs))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_R2D_SegmentElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_R2D_SegmentElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_R2D_SegmentElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_R2D_SegmentElement_CalcVShape)

    def CalcDivShape(self, ip, div_shape):
        r"""CalcDivShape(RT_R2D_SegmentElement self, IntegrationPoint ip, Vector div_shape)"""
        return _fe_rt.RT_R2D_SegmentElement_CalcDivShape(self, ip, div_shape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_R2D_SegmentElement_CalcDivShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_R2D_SegmentElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_R2D_SegmentElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_R2D_SegmentElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_R2D_SegmentElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_R2D_SegmentElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_R2D_SegmentElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_R2D_SegmentElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_R2D_SegmentElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_R2D_SegmentElement_GetTransferMatrix)
    __swig_destroy__ = _fe_rt.delete_RT_R2D_SegmentElement

# Register RT_R2D_SegmentElement in _fe_rt:
_fe_rt.RT_R2D_SegmentElement_swigregister(RT_R2D_SegmentElement)

class RT_R2D_FiniteElement(mfem._ser.fe_base.VectorFiniteElement):
    r"""Proxy of C++ mfem::RT_R2D_FiniteElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_R2D_FiniteElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_R2D_FiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        CalcVShape(RT_R2D_FiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        """
        return _fe_rt.RT_R2D_FiniteElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_R2D_FiniteElement_CalcVShape)

    def GetLocalInterpolation(self, Trans, I):
        r"""GetLocalInterpolation(RT_R2D_FiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_R2D_FiniteElement_GetLocalInterpolation(self, Trans, I)
    GetLocalInterpolation = _swig_new_instance_method(_fe_rt.RT_R2D_FiniteElement_GetLocalInterpolation)

    def GetLocalRestriction(self, Trans, R):
        r"""GetLocalRestriction(RT_R2D_FiniteElement self, mfem::ElementTransformation & Trans, DenseMatrix R)"""
        return _fe_rt.RT_R2D_FiniteElement_GetLocalRestriction(self, Trans, R)
    GetLocalRestriction = _swig_new_instance_method(_fe_rt.RT_R2D_FiniteElement_GetLocalRestriction)

    def GetTransferMatrix(self, fe, Trans, I):
        r"""GetTransferMatrix(RT_R2D_FiniteElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)"""
        return _fe_rt.RT_R2D_FiniteElement_GetTransferMatrix(self, fe, Trans, I)
    GetTransferMatrix = _swig_new_instance_method(_fe_rt.RT_R2D_FiniteElement_GetTransferMatrix)

    def Project(self, *args):
        r"""
        Project(RT_R2D_FiniteElement self, mfem::VectorCoefficient & vc, mfem::ElementTransformation & Trans, Vector dofs)
        Project(RT_R2D_FiniteElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix I)
        """
        return _fe_rt.RT_R2D_FiniteElement_Project(self, *args)
    Project = _swig_new_instance_method(_fe_rt.RT_R2D_FiniteElement_Project)

    def ProjectCurl(self, fe, Trans, curl):
        r"""ProjectCurl(RT_R2D_FiniteElement self, FiniteElement fe, mfem::ElementTransformation & Trans, DenseMatrix curl)"""
        return _fe_rt.RT_R2D_FiniteElement_ProjectCurl(self, fe, Trans, curl)
    ProjectCurl = _swig_new_instance_method(_fe_rt.RT_R2D_FiniteElement_ProjectCurl)
    __swig_destroy__ = _fe_rt.delete_RT_R2D_FiniteElement

# Register RT_R2D_FiniteElement in _fe_rt:
_fe_rt.RT_R2D_FiniteElement_swigregister(RT_R2D_FiniteElement)

class RT_R2D_TriangleElement(RT_R2D_FiniteElement):
    r"""Proxy of C++ mfem::RT_R2D_TriangleElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, p):
        r"""__init__(RT_R2D_TriangleElement self, int const p) -> RT_R2D_TriangleElement"""
        _fe_rt.RT_R2D_TriangleElement_swiginit(self, _fe_rt.new_RT_R2D_TriangleElement(p))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_R2D_TriangleElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_R2D_TriangleElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        CalcVShape(RT_R2D_TriangleElement self, IntegrationPoint ip, DenseMatrix shape)
        """
        return _fe_rt.RT_R2D_TriangleElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_R2D_TriangleElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_R2D_TriangleElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_R2D_TriangleElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_R2D_TriangleElement_CalcDivShape)
    __swig_destroy__ = _fe_rt.delete_RT_R2D_TriangleElement

# Register RT_R2D_TriangleElement in _fe_rt:
_fe_rt.RT_R2D_TriangleElement_swigregister(RT_R2D_TriangleElement)

class RT_R2D_QuadrilateralElement(RT_R2D_FiniteElement):
    r"""Proxy of C++ mfem::RT_R2D_QuadrilateralElement class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args, **kwargs):
        r"""__init__(RT_R2D_QuadrilateralElement self, int const p, int const cb_type=GaussLobatto, int const ob_type=GaussLegendre) -> RT_R2D_QuadrilateralElement"""
        _fe_rt.RT_R2D_QuadrilateralElement_swiginit(self, _fe_rt.new_RT_R2D_QuadrilateralElement(*args, **kwargs))

    def CalcVShape(self, *args):
        r"""
        CalcVShape(RT_R2D_QuadrilateralElement self, IntegrationPoint ip, DenseMatrix shape)
        CalcVShape(RT_R2D_QuadrilateralElement self, mfem::ElementTransformation & Trans, DenseMatrix shape)
        CalcVShape(RT_R2D_QuadrilateralElement self, IntegrationPoint ip, DenseMatrix shape)
        """
        return _fe_rt.RT_R2D_QuadrilateralElement_CalcVShape(self, *args)
    CalcVShape = _swig_new_instance_method(_fe_rt.RT_R2D_QuadrilateralElement_CalcVShape)

    def CalcDivShape(self, ip, divshape):
        r"""CalcDivShape(RT_R2D_QuadrilateralElement self, IntegrationPoint ip, Vector divshape)"""
        return _fe_rt.RT_R2D_QuadrilateralElement_CalcDivShape(self, ip, divshape)
    CalcDivShape = _swig_new_instance_method(_fe_rt.RT_R2D_QuadrilateralElement_CalcDivShape)
    __swig_destroy__ = _fe_rt.delete_RT_R2D_QuadrilateralElement

# Register RT_R2D_QuadrilateralElement in _fe_rt:
_fe_rt.RT_R2D_QuadrilateralElement_swigregister(RT_R2D_QuadrilateralElement)



