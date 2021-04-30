# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _bilinearform
else:
    import _bilinearform

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _bilinearform.SWIG_PyInstanceMethod_New
_swig_new_static_method = _bilinearform.SWIG_PyStaticMethod_New

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

import mfem._ser.globals
import mfem._ser.mem_manager
import mfem._ser.array
import mfem._ser.fespace
import mfem._ser.vector
import mfem._ser.coefficient
import mfem._ser.matrix
import mfem._ser.operators
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.bilininteg
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.handle
import mfem._ser.restriction
AssemblyLevel_LEGACYFULL = _bilinearform.AssemblyLevel_LEGACYFULL

AssemblyLevel_FULL = _bilinearform.AssemblyLevel_FULL

AssemblyLevel_ELEMENT = _bilinearform.AssemblyLevel_ELEMENT

AssemblyLevel_PARTIAL = _bilinearform.AssemblyLevel_PARTIAL

AssemblyLevel_NONE = _bilinearform.AssemblyLevel_NONE

class BilinearForm(mfem._ser.matrix.Matrix):
    r"""Proxy of C++ mfem::BilinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(BilinearForm self) -> BilinearForm
        __init__(BilinearForm self, FiniteElementSpace f) -> BilinearForm
        __init__(BilinearForm self, FiniteElementSpace f, BilinearForm bf, int ps=0) -> BilinearForm
        """
        if self.__class__ == BilinearForm:
            _self = None
        else:
            _self = self
        _bilinearform.BilinearForm_swiginit(self, _bilinearform.new_BilinearForm(_self, *args))

    def Size(self):
        r"""Size(BilinearForm self) -> int"""
        return _bilinearform.BilinearForm_Size(self)
    Size = _swig_new_instance_method(_bilinearform.BilinearForm_Size)

    def SetAssemblyLevel(self, assembly_level):
        r"""SetAssemblyLevel(BilinearForm self, mfem::AssemblyLevel assembly_level)"""
        return _bilinearform.BilinearForm_SetAssemblyLevel(self, assembly_level)
    SetAssemblyLevel = _swig_new_instance_method(_bilinearform.BilinearForm_SetAssemblyLevel)

    def GetAssemblyLevel(self):
        r"""GetAssemblyLevel(BilinearForm self) -> mfem::AssemblyLevel"""
        return _bilinearform.BilinearForm_GetAssemblyLevel(self)
    GetAssemblyLevel = _swig_new_instance_method(_bilinearform.BilinearForm_GetAssemblyLevel)

    def EnableStaticCondensation(self):
        r"""EnableStaticCondensation(BilinearForm self)"""
        return _bilinearform.BilinearForm_EnableStaticCondensation(self)
    EnableStaticCondensation = _swig_new_instance_method(_bilinearform.BilinearForm_EnableStaticCondensation)

    def StaticCondensationIsEnabled(self):
        r"""StaticCondensationIsEnabled(BilinearForm self) -> bool"""
        return _bilinearform.BilinearForm_StaticCondensationIsEnabled(self)
    StaticCondensationIsEnabled = _swig_new_instance_method(_bilinearform.BilinearForm_StaticCondensationIsEnabled)

    def SCFESpace(self):
        r"""SCFESpace(BilinearForm self) -> FiniteElementSpace"""
        return _bilinearform.BilinearForm_SCFESpace(self)
    SCFESpace = _swig_new_instance_method(_bilinearform.BilinearForm_SCFESpace)

    def EnableHybridization(self, constr_space, constr_integ, ess_tdof_list):
        r"""EnableHybridization(BilinearForm self, FiniteElementSpace constr_space, BilinearFormIntegrator constr_integ, intArray ess_tdof_list)"""
        val = _bilinearform.BilinearForm_EnableHybridization(self, constr_space, constr_integ, ess_tdof_list)

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(constr_integ)
        constr_integ.thisown = 0


        return val


    def UsePrecomputedSparsity(self, ps=1):
        r"""UsePrecomputedSparsity(BilinearForm self, int ps=1)"""
        return _bilinearform.BilinearForm_UsePrecomputedSparsity(self, ps)
    UsePrecomputedSparsity = _swig_new_instance_method(_bilinearform.BilinearForm_UsePrecomputedSparsity)

    def UseSparsity(self, *args):
        r"""
        UseSparsity(BilinearForm self, int * I, int * J, bool isSorted)
        UseSparsity(BilinearForm self, SparseMatrix A)
        """
        return _bilinearform.BilinearForm_UseSparsity(self, *args)
    UseSparsity = _swig_new_instance_method(_bilinearform.BilinearForm_UseSparsity)

    def AllocateMatrix(self):
        r"""AllocateMatrix(BilinearForm self)"""
        return _bilinearform.BilinearForm_AllocateMatrix(self)
    AllocateMatrix = _swig_new_instance_method(_bilinearform.BilinearForm_AllocateMatrix)

    def GetDBFI(self):
        r"""GetDBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetDBFI(self)
    GetDBFI = _swig_new_instance_method(_bilinearform.BilinearForm_GetDBFI)

    def GetBBFI(self):
        r"""GetBBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetBBFI(self)
    GetBBFI = _swig_new_instance_method(_bilinearform.BilinearForm_GetBBFI)

    def GetBBFI_Marker(self):
        r"""GetBBFI_Marker(BilinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _bilinearform.BilinearForm_GetBBFI_Marker(self)
    GetBBFI_Marker = _swig_new_instance_method(_bilinearform.BilinearForm_GetBBFI_Marker)

    def GetFBFI(self):
        r"""GetFBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetFBFI(self)
    GetFBFI = _swig_new_instance_method(_bilinearform.BilinearForm_GetFBFI)

    def GetBFBFI(self):
        r"""GetBFBFI(BilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.BilinearForm_GetBFBFI(self)
    GetBFBFI = _swig_new_instance_method(_bilinearform.BilinearForm_GetBFBFI)

    def GetBFBFI_Marker(self):
        r"""GetBFBFI_Marker(BilinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _bilinearform.BilinearForm_GetBFBFI_Marker(self)
    GetBFBFI_Marker = _swig_new_instance_method(_bilinearform.BilinearForm_GetBFBFI_Marker)

    def __call__(self, i, j):
        r"""__call__(BilinearForm self, int i, int j) -> double const &"""
        return _bilinearform.BilinearForm___call__(self, i, j)
    __call__ = _swig_new_instance_method(_bilinearform.BilinearForm___call__)

    def Elem(self, *args):
        r"""
        Elem(BilinearForm self, int i, int j) -> double
        Elem(BilinearForm self, int i, int j) -> double const &
        """
        return _bilinearform.BilinearForm_Elem(self, *args)
    Elem = _swig_new_instance_method(_bilinearform.BilinearForm_Elem)

    def Mult(self, x, y):
        r"""Mult(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_Mult(self, x, y)
    Mult = _swig_new_instance_method(_bilinearform.BilinearForm_Mult)

    def FullMult(self, x, y):
        r"""FullMult(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_FullMult(self, x, y)
    FullMult = _swig_new_instance_method(_bilinearform.BilinearForm_FullMult)

    def AddMult(self, x, y, a=1.0):
        r"""AddMult(BilinearForm self, Vector x, Vector y, double const a=1.0)"""
        return _bilinearform.BilinearForm_AddMult(self, x, y, a)
    AddMult = _swig_new_instance_method(_bilinearform.BilinearForm_AddMult)

    def FullAddMult(self, x, y):
        r"""FullAddMult(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_FullAddMult(self, x, y)
    FullAddMult = _swig_new_instance_method(_bilinearform.BilinearForm_FullAddMult)

    def AddMultTranspose(self, x, y, a=1.0):
        r"""AddMultTranspose(BilinearForm self, Vector x, Vector y, double const a=1.0)"""
        return _bilinearform.BilinearForm_AddMultTranspose(self, x, y, a)
    AddMultTranspose = _swig_new_instance_method(_bilinearform.BilinearForm_AddMultTranspose)

    def FullAddMultTranspose(self, x, y):
        r"""FullAddMultTranspose(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_FullAddMultTranspose(self, x, y)
    FullAddMultTranspose = _swig_new_instance_method(_bilinearform.BilinearForm_FullAddMultTranspose)

    def MultTranspose(self, x, y):
        r"""MultTranspose(BilinearForm self, Vector x, Vector y)"""
        return _bilinearform.BilinearForm_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_bilinearform.BilinearForm_MultTranspose)

    def InnerProduct(self, x, y):
        r"""InnerProduct(BilinearForm self, Vector x, Vector y) -> double"""
        return _bilinearform.BilinearForm_InnerProduct(self, x, y)
    InnerProduct = _swig_new_instance_method(_bilinearform.BilinearForm_InnerProduct)

    def Inverse(self):
        r"""Inverse(BilinearForm self) -> MatrixInverse"""
        return _bilinearform.BilinearForm_Inverse(self)
    Inverse = _swig_new_instance_method(_bilinearform.BilinearForm_Inverse)

    def Finalize(self, skip_zeros=1):
        r"""Finalize(BilinearForm self, int skip_zeros=1)"""
        return _bilinearform.BilinearForm_Finalize(self, skip_zeros)
    Finalize = _swig_new_instance_method(_bilinearform.BilinearForm_Finalize)

    def SpMat(self, *args):
        r"""
        SpMat(BilinearForm self) -> SparseMatrix
        SpMat(BilinearForm self) -> SparseMatrix
        """
        val = _bilinearform.BilinearForm_SpMat(self, *args)

        if not hasattr(self, "_spmat"): self._spmat = []
        self._spmat.append(val)
        val.thisown=0 


        return val


    def LoseMat(self):
        r"""LoseMat(BilinearForm self) -> SparseMatrix"""
        return _bilinearform.BilinearForm_LoseMat(self)
    LoseMat = _swig_new_instance_method(_bilinearform.BilinearForm_LoseMat)

    def SpMatElim(self, *args):
        r"""
        SpMatElim(BilinearForm self) -> SparseMatrix
        SpMatElim(BilinearForm self) -> SparseMatrix
        """
        return _bilinearform.BilinearForm_SpMatElim(self, *args)
    SpMatElim = _swig_new_instance_method(_bilinearform.BilinearForm_SpMatElim)

    def AddDomainIntegrator(self, bfi):
        r"""AddDomainIntegrator(BilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddDomainIntegrator(self, bfi)


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(BilinearForm self, BilinearFormIntegrator bfi)
        AddBoundaryIntegrator(BilinearForm self, BilinearFormIntegrator bfi, intArray bdr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        bfi = args[0]	     
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddBoundaryIntegrator(self, *args)


    def AddInteriorFaceIntegrator(self, bfi):
        r"""AddInteriorFaceIntegrator(BilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddInteriorFaceIntegrator(self, bfi)


    def AddBdrFaceIntegrator(self, *args):
        r"""
        AddBdrFaceIntegrator(BilinearForm self, BilinearFormIntegrator bfi)
        AddBdrFaceIntegrator(BilinearForm self, BilinearFormIntegrator bfi, intArray bdr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        bfi = args[0]
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.BilinearForm_AddBdrFaceIntegrator(self, *args)


    def Assemble(self, skip_zeros=1):
        r"""Assemble(BilinearForm self, int skip_zeros=1)"""
        return _bilinearform.BilinearForm_Assemble(self, skip_zeros)
    Assemble = _swig_new_instance_method(_bilinearform.BilinearForm_Assemble)

    def AssembleDiagonal(self, diag):
        r"""AssembleDiagonal(BilinearForm self, Vector diag)"""
        return _bilinearform.BilinearForm_AssembleDiagonal(self, diag)
    AssembleDiagonal = _swig_new_instance_method(_bilinearform.BilinearForm_AssembleDiagonal)

    def GetProlongation(self):
        r"""GetProlongation(BilinearForm self) -> Operator"""
        return _bilinearform.BilinearForm_GetProlongation(self)
    GetProlongation = _swig_new_instance_method(_bilinearform.BilinearForm_GetProlongation)

    def GetRestriction(self):
        r"""GetRestriction(BilinearForm self) -> Operator"""
        return _bilinearform.BilinearForm_GetRestriction(self)
    GetRestriction = _swig_new_instance_method(_bilinearform.BilinearForm_GetRestriction)

    def GetOutputProlongation(self):
        r"""GetOutputProlongation(BilinearForm self) -> Operator"""
        return _bilinearform.BilinearForm_GetOutputProlongation(self)
    GetOutputProlongation = _swig_new_instance_method(_bilinearform.BilinearForm_GetOutputProlongation)

    def GetOutputRestriction(self):
        r"""GetOutputRestriction(BilinearForm self) -> Operator"""
        return _bilinearform.BilinearForm_GetOutputRestriction(self)
    GetOutputRestriction = _swig_new_instance_method(_bilinearform.BilinearForm_GetOutputRestriction)

    def RecoverFEMSolution(self, X, b, x):
        r"""RecoverFEMSolution(BilinearForm self, Vector X, Vector b, Vector x)"""
        return _bilinearform.BilinearForm_RecoverFEMSolution(self, X, b, x)
    RecoverFEMSolution = _swig_new_instance_method(_bilinearform.BilinearForm_RecoverFEMSolution)

    def ComputeElementMatrices(self):
        r"""ComputeElementMatrices(BilinearForm self)"""
        return _bilinearform.BilinearForm_ComputeElementMatrices(self)
    ComputeElementMatrices = _swig_new_instance_method(_bilinearform.BilinearForm_ComputeElementMatrices)

    def FreeElementMatrices(self):
        r"""FreeElementMatrices(BilinearForm self)"""
        return _bilinearform.BilinearForm_FreeElementMatrices(self)
    FreeElementMatrices = _swig_new_instance_method(_bilinearform.BilinearForm_FreeElementMatrices)

    def ComputeElementMatrix(self, i, elmat):
        r"""ComputeElementMatrix(BilinearForm self, int i, DenseMatrix elmat)"""
        return _bilinearform.BilinearForm_ComputeElementMatrix(self, i, elmat)
    ComputeElementMatrix = _swig_new_instance_method(_bilinearform.BilinearForm_ComputeElementMatrix)

    def ComputeBdrElementMatrix(self, i, elmat):
        r"""ComputeBdrElementMatrix(BilinearForm self, int i, DenseMatrix elmat)"""
        return _bilinearform.BilinearForm_ComputeBdrElementMatrix(self, i, elmat)
    ComputeBdrElementMatrix = _swig_new_instance_method(_bilinearform.BilinearForm_ComputeBdrElementMatrix)

    def AssembleElementMatrix(self, *args):
        r"""
        AssembleElementMatrix(BilinearForm self, int i, DenseMatrix elmat, int skip_zeros=1)
        AssembleElementMatrix(BilinearForm self, int i, DenseMatrix elmat, intArray vdofs, int skip_zeros=1)
        """
        return _bilinearform.BilinearForm_AssembleElementMatrix(self, *args)
    AssembleElementMatrix = _swig_new_instance_method(_bilinearform.BilinearForm_AssembleElementMatrix)

    def AssembleBdrElementMatrix(self, *args):
        r"""
        AssembleBdrElementMatrix(BilinearForm self, int i, DenseMatrix elmat, int skip_zeros=1)
        AssembleBdrElementMatrix(BilinearForm self, int i, DenseMatrix elmat, intArray vdofs, int skip_zeros=1)
        """
        return _bilinearform.BilinearForm_AssembleBdrElementMatrix(self, *args)
    AssembleBdrElementMatrix = _swig_new_instance_method(_bilinearform.BilinearForm_AssembleBdrElementMatrix)

    def EliminateEssentialBC(self, *args):
        r"""
        EliminateEssentialBC(BilinearForm self, intArray bdr_attr_is_ess, Vector sol, Vector rhs, mfem::Operator::DiagonalPolicy dpolicy=DIAG_ONE)
        EliminateEssentialBC(BilinearForm self, intArray bdr_attr_is_ess, mfem::Operator::DiagonalPolicy dpolicy=DIAG_ONE)
        """
        return _bilinearform.BilinearForm_EliminateEssentialBC(self, *args)
    EliminateEssentialBC = _swig_new_instance_method(_bilinearform.BilinearForm_EliminateEssentialBC)

    def EliminateEssentialBCDiag(self, bdr_attr_is_ess, value):
        r"""EliminateEssentialBCDiag(BilinearForm self, intArray bdr_attr_is_ess, double value)"""
        return _bilinearform.BilinearForm_EliminateEssentialBCDiag(self, bdr_attr_is_ess, value)
    EliminateEssentialBCDiag = _swig_new_instance_method(_bilinearform.BilinearForm_EliminateEssentialBCDiag)

    def EliminateVDofs(self, *args):
        r"""
        EliminateVDofs(BilinearForm self, intArray vdofs, Vector sol, Vector rhs, mfem::Operator::DiagonalPolicy dpolicy=DIAG_ONE)
        EliminateVDofs(BilinearForm self, intArray vdofs, mfem::Operator::DiagonalPolicy dpolicy=DIAG_ONE)
        """
        return _bilinearform.BilinearForm_EliminateVDofs(self, *args)
    EliminateVDofs = _swig_new_instance_method(_bilinearform.BilinearForm_EliminateVDofs)

    def EliminateEssentialBCFromDofs(self, *args):
        r"""
        EliminateEssentialBCFromDofs(BilinearForm self, intArray ess_dofs, Vector sol, Vector rhs, mfem::Operator::DiagonalPolicy dpolicy=DIAG_ONE)
        EliminateEssentialBCFromDofs(BilinearForm self, intArray ess_dofs, mfem::Operator::DiagonalPolicy dpolicy=DIAG_ONE)
        """
        return _bilinearform.BilinearForm_EliminateEssentialBCFromDofs(self, *args)
    EliminateEssentialBCFromDofs = _swig_new_instance_method(_bilinearform.BilinearForm_EliminateEssentialBCFromDofs)

    def EliminateEssentialBCFromDofsDiag(self, ess_dofs, value):
        r"""EliminateEssentialBCFromDofsDiag(BilinearForm self, intArray ess_dofs, double value)"""
        return _bilinearform.BilinearForm_EliminateEssentialBCFromDofsDiag(self, ess_dofs, value)
    EliminateEssentialBCFromDofsDiag = _swig_new_instance_method(_bilinearform.BilinearForm_EliminateEssentialBCFromDofsDiag)

    def EliminateVDofsInRHS(self, vdofs, x, b):
        r"""EliminateVDofsInRHS(BilinearForm self, intArray vdofs, Vector x, Vector b)"""
        return _bilinearform.BilinearForm_EliminateVDofsInRHS(self, vdofs, x, b)
    EliminateVDofsInRHS = _swig_new_instance_method(_bilinearform.BilinearForm_EliminateVDofsInRHS)

    def FullInnerProduct(self, x, y):
        r"""FullInnerProduct(BilinearForm self, Vector x, Vector y) -> double"""
        return _bilinearform.BilinearForm_FullInnerProduct(self, x, y)
    FullInnerProduct = _swig_new_instance_method(_bilinearform.BilinearForm_FullInnerProduct)

    def Update(self, nfes=None):
        r"""Update(BilinearForm self, FiniteElementSpace nfes=None)"""
        return _bilinearform.BilinearForm_Update(self, nfes)
    Update = _swig_new_instance_method(_bilinearform.BilinearForm_Update)

    def GetFES(self):
        r"""GetFES(BilinearForm self) -> FiniteElementSpace"""

        import warnings
        warnings.warn("mfem::BilinearForm::GetFES() is deprecated",
                      DeprecationWarning,)


        return _bilinearform.BilinearForm_GetFES(self)


    def FESpace(self, *args):
        r"""
        FESpace(BilinearForm self) -> FiniteElementSpace
        FESpace(BilinearForm self) -> FiniteElementSpace
        """
        return _bilinearform.BilinearForm_FESpace(self, *args)
    FESpace = _swig_new_instance_method(_bilinearform.BilinearForm_FESpace)

    def SetDiagonalPolicy(self, policy):
        r"""SetDiagonalPolicy(BilinearForm self, mfem::Operator::DiagonalPolicy policy)"""
        return _bilinearform.BilinearForm_SetDiagonalPolicy(self, policy)
    SetDiagonalPolicy = _swig_new_instance_method(_bilinearform.BilinearForm_SetDiagonalPolicy)

    def UseExternalIntegrators(self):
        r"""UseExternalIntegrators(BilinearForm self)"""
        return _bilinearform.BilinearForm_UseExternalIntegrators(self)
    UseExternalIntegrators = _swig_new_instance_method(_bilinearform.BilinearForm_UseExternalIntegrators)
    __swig_destroy__ = _bilinearform.delete_BilinearForm

    def FormLinearSystem(self, *args):
        r"""
        FormLinearSystem(BilinearForm self, intArray ess_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B, int copy_interior=0)
        FormLinearSystem(BilinearForm self, intArray ess_tdof_list, Vector x, Vector b, SparseMatrix A, Vector X, Vector B, int copy_interior=0)
        """
        return _bilinearform.BilinearForm_FormLinearSystem(self, *args)
    FormLinearSystem = _swig_new_instance_method(_bilinearform.BilinearForm_FormLinearSystem)

    def FormSystemMatrix(self, *args):
        r"""
        FormSystemMatrix(BilinearForm self, intArray ess_tdof_list, OperatorHandle A)
        FormSystemMatrix(BilinearForm self, intArray ess_tdof_list, SparseMatrix A)
        """
        return _bilinearform.BilinearForm_FormSystemMatrix(self, *args)
    FormSystemMatrix = _swig_new_instance_method(_bilinearform.BilinearForm_FormSystemMatrix)
    def __disown__(self):
        self.this.disown()
        _bilinearform.disown_BilinearForm(self)
        return weakref.proxy(self)

# Register BilinearForm in _bilinearform:
_bilinearform.BilinearForm_swigregister(BilinearForm)

class MixedBilinearForm(mfem._ser.matrix.Matrix):
    r"""Proxy of C++ mfem::MixedBilinearForm class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(MixedBilinearForm self, FiniteElementSpace tr_fes, FiniteElementSpace te_fes) -> MixedBilinearForm
        __init__(MixedBilinearForm self, FiniteElementSpace tr_fes, FiniteElementSpace te_fes, MixedBilinearForm mbf) -> MixedBilinearForm
        """
        _bilinearform.MixedBilinearForm_swiginit(self, _bilinearform.new_MixedBilinearForm(*args))

    def Elem(self, *args):
        r"""
        Elem(MixedBilinearForm self, int i, int j) -> double
        Elem(MixedBilinearForm self, int i, int j) -> double const &
        """
        return _bilinearform.MixedBilinearForm_Elem(self, *args)
    Elem = _swig_new_instance_method(_bilinearform.MixedBilinearForm_Elem)

    def Mult(self, x, y):
        r"""Mult(MixedBilinearForm self, Vector x, Vector y)"""
        return _bilinearform.MixedBilinearForm_Mult(self, x, y)
    Mult = _swig_new_instance_method(_bilinearform.MixedBilinearForm_Mult)

    def AddMult(self, x, y, a=1.0):
        r"""AddMult(MixedBilinearForm self, Vector x, Vector y, double const a=1.0)"""
        return _bilinearform.MixedBilinearForm_AddMult(self, x, y, a)
    AddMult = _swig_new_instance_method(_bilinearform.MixedBilinearForm_AddMult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(MixedBilinearForm self, Vector x, Vector y)"""
        return _bilinearform.MixedBilinearForm_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_bilinearform.MixedBilinearForm_MultTranspose)

    def AddMultTranspose(self, x, y, a=1.0):
        r"""AddMultTranspose(MixedBilinearForm self, Vector x, Vector y, double const a=1.0)"""
        return _bilinearform.MixedBilinearForm_AddMultTranspose(self, x, y, a)
    AddMultTranspose = _swig_new_instance_method(_bilinearform.MixedBilinearForm_AddMultTranspose)

    def Inverse(self):
        r"""Inverse(MixedBilinearForm self) -> MatrixInverse"""
        return _bilinearform.MixedBilinearForm_Inverse(self)
    Inverse = _swig_new_instance_method(_bilinearform.MixedBilinearForm_Inverse)

    def Finalize(self, skip_zeros=1):
        r"""Finalize(MixedBilinearForm self, int skip_zeros=1)"""
        return _bilinearform.MixedBilinearForm_Finalize(self, skip_zeros)
    Finalize = _swig_new_instance_method(_bilinearform.MixedBilinearForm_Finalize)

    def GetBlocks(self, blocks):
        r"""GetBlocks(MixedBilinearForm self, mfem::Array2D< mfem::SparseMatrix * > & blocks)"""
        return _bilinearform.MixedBilinearForm_GetBlocks(self, blocks)
    GetBlocks = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetBlocks)

    def SpMat(self, *args):
        r"""
        SpMat(MixedBilinearForm self) -> SparseMatrix
        SpMat(MixedBilinearForm self) -> SparseMatrix
        """
        val = _bilinearform.MixedBilinearForm_SpMat(self, *args)

        if not hasattr(self, "_spmat"): self._spmat = []
        self._spmat.append(val)
        val.thisown=0 


        return val


    def LoseMat(self):
        r"""LoseMat(MixedBilinearForm self) -> SparseMatrix"""
        return _bilinearform.MixedBilinearForm_LoseMat(self)
    LoseMat = _swig_new_instance_method(_bilinearform.MixedBilinearForm_LoseMat)

    def AddDomainIntegrator(self, bfi):
        r"""AddDomainIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddDomainIntegrator(self, bfi)


    def AddBoundaryIntegrator(self, *args):
        r"""
        AddBoundaryIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)
        AddBoundaryIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi, intArray bdr_marker)
        """

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddBoundaryIntegrator(self, *args)


    def AddTraceFaceIntegrator(self, bfi):
        r"""AddTraceFaceIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(bfi)
        bfi.thisown=0 


        return _bilinearform.MixedBilinearForm_AddTraceFaceIntegrator(self, bfi)


    def AddBdrTraceFaceIntegrator(self, *args):
        r"""
        AddBdrTraceFaceIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi)
        AddBdrTraceFaceIntegrator(MixedBilinearForm self, BilinearFormIntegrator bfi, intArray bdr_marker)
        """
        return _bilinearform.MixedBilinearForm_AddBdrTraceFaceIntegrator(self, *args)
    AddBdrTraceFaceIntegrator = _swig_new_instance_method(_bilinearform.MixedBilinearForm_AddBdrTraceFaceIntegrator)

    def GetDBFI(self):
        r"""GetDBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetDBFI(self)
    GetDBFI = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetDBFI)

    def GetBBFI(self):
        r"""GetBBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetBBFI(self)
    GetBBFI = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetBBFI)

    def GetBBFI_Marker(self):
        r"""GetBBFI_Marker(MixedBilinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _bilinearform.MixedBilinearForm_GetBBFI_Marker(self)
    GetBBFI_Marker = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetBBFI_Marker)

    def GetTFBFI(self):
        r"""GetTFBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetTFBFI(self)
    GetTFBFI = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetTFBFI)

    def GetBTFBFI(self):
        r"""GetBTFBFI(MixedBilinearForm self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.MixedBilinearForm_GetBTFBFI(self)
    GetBTFBFI = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetBTFBFI)

    def GetBTFBFI_Marker(self):
        r"""GetBTFBFI_Marker(MixedBilinearForm self) -> mfem::Array< mfem::Array< int > * > *"""
        return _bilinearform.MixedBilinearForm_GetBTFBFI_Marker(self)
    GetBTFBFI_Marker = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetBTFBFI_Marker)

    def SetAssemblyLevel(self, assembly_level):
        r"""SetAssemblyLevel(MixedBilinearForm self, mfem::AssemblyLevel assembly_level)"""
        return _bilinearform.MixedBilinearForm_SetAssemblyLevel(self, assembly_level)
    SetAssemblyLevel = _swig_new_instance_method(_bilinearform.MixedBilinearForm_SetAssemblyLevel)

    def Assemble(self, skip_zeros=1):
        r"""Assemble(MixedBilinearForm self, int skip_zeros=1)"""
        return _bilinearform.MixedBilinearForm_Assemble(self, skip_zeros)
    Assemble = _swig_new_instance_method(_bilinearform.MixedBilinearForm_Assemble)

    def AssembleDiagonal_ADAt(self, D, diag):
        r"""AssembleDiagonal_ADAt(MixedBilinearForm self, Vector D, Vector diag)"""
        return _bilinearform.MixedBilinearForm_AssembleDiagonal_ADAt(self, D, diag)
    AssembleDiagonal_ADAt = _swig_new_instance_method(_bilinearform.MixedBilinearForm_AssembleDiagonal_ADAt)

    def GetProlongation(self):
        r"""GetProlongation(MixedBilinearForm self) -> Operator"""
        return _bilinearform.MixedBilinearForm_GetProlongation(self)
    GetProlongation = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetProlongation)

    def GetRestriction(self):
        r"""GetRestriction(MixedBilinearForm self) -> Operator"""
        return _bilinearform.MixedBilinearForm_GetRestriction(self)
    GetRestriction = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetRestriction)

    def GetOutputProlongation(self):
        r"""GetOutputProlongation(MixedBilinearForm self) -> Operator"""
        return _bilinearform.MixedBilinearForm_GetOutputProlongation(self)
    GetOutputProlongation = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetOutputProlongation)

    def GetOutputRestriction(self):
        r"""GetOutputRestriction(MixedBilinearForm self) -> Operator"""
        return _bilinearform.MixedBilinearForm_GetOutputRestriction(self)
    GetOutputRestriction = _swig_new_instance_method(_bilinearform.MixedBilinearForm_GetOutputRestriction)

    def ConformingAssemble(self):
        r"""ConformingAssemble(MixedBilinearForm self)"""
        return _bilinearform.MixedBilinearForm_ConformingAssemble(self)
    ConformingAssemble = _swig_new_instance_method(_bilinearform.MixedBilinearForm_ConformingAssemble)

    def ComputeElementMatrix(self, i, elmat):
        r"""ComputeElementMatrix(MixedBilinearForm self, int i, DenseMatrix elmat)"""
        return _bilinearform.MixedBilinearForm_ComputeElementMatrix(self, i, elmat)
    ComputeElementMatrix = _swig_new_instance_method(_bilinearform.MixedBilinearForm_ComputeElementMatrix)

    def ComputeBdrElementMatrix(self, i, elmat):
        r"""ComputeBdrElementMatrix(MixedBilinearForm self, int i, DenseMatrix elmat)"""
        return _bilinearform.MixedBilinearForm_ComputeBdrElementMatrix(self, i, elmat)
    ComputeBdrElementMatrix = _swig_new_instance_method(_bilinearform.MixedBilinearForm_ComputeBdrElementMatrix)

    def AssembleElementMatrix(self, *args):
        r"""
        AssembleElementMatrix(MixedBilinearForm self, int i, DenseMatrix elmat, int skip_zeros=1)
        AssembleElementMatrix(MixedBilinearForm self, int i, DenseMatrix elmat, intArray trial_vdofs, intArray test_vdofs, int skip_zeros=1)
        """
        return _bilinearform.MixedBilinearForm_AssembleElementMatrix(self, *args)
    AssembleElementMatrix = _swig_new_instance_method(_bilinearform.MixedBilinearForm_AssembleElementMatrix)

    def AssembleBdrElementMatrix(self, *args):
        r"""
        AssembleBdrElementMatrix(MixedBilinearForm self, int i, DenseMatrix elmat, int skip_zeros=1)
        AssembleBdrElementMatrix(MixedBilinearForm self, int i, DenseMatrix elmat, intArray trial_vdofs, intArray test_vdofs, int skip_zeros=1)
        """
        return _bilinearform.MixedBilinearForm_AssembleBdrElementMatrix(self, *args)
    AssembleBdrElementMatrix = _swig_new_instance_method(_bilinearform.MixedBilinearForm_AssembleBdrElementMatrix)

    def EliminateTrialDofs(self, bdr_attr_is_ess, sol, rhs):
        r"""EliminateTrialDofs(MixedBilinearForm self, intArray bdr_attr_is_ess, Vector sol, Vector rhs)"""
        return _bilinearform.MixedBilinearForm_EliminateTrialDofs(self, bdr_attr_is_ess, sol, rhs)
    EliminateTrialDofs = _swig_new_instance_method(_bilinearform.MixedBilinearForm_EliminateTrialDofs)

    def EliminateEssentialBCFromTrialDofs(self, marked_vdofs, sol, rhs):
        r"""EliminateEssentialBCFromTrialDofs(MixedBilinearForm self, intArray marked_vdofs, Vector sol, Vector rhs)"""
        return _bilinearform.MixedBilinearForm_EliminateEssentialBCFromTrialDofs(self, marked_vdofs, sol, rhs)
    EliminateEssentialBCFromTrialDofs = _swig_new_instance_method(_bilinearform.MixedBilinearForm_EliminateEssentialBCFromTrialDofs)

    def EliminateTestDofs(self, bdr_attr_is_ess):
        r"""EliminateTestDofs(MixedBilinearForm self, intArray bdr_attr_is_ess)"""
        return _bilinearform.MixedBilinearForm_EliminateTestDofs(self, bdr_attr_is_ess)
    EliminateTestDofs = _swig_new_instance_method(_bilinearform.MixedBilinearForm_EliminateTestDofs)

    def FormRectangularSystemMatrix(self, trial_tdof_list, test_tdof_list, A):
        r"""FormRectangularSystemMatrix(MixedBilinearForm self, intArray trial_tdof_list, intArray test_tdof_list, OperatorHandle A)"""
        return _bilinearform.MixedBilinearForm_FormRectangularSystemMatrix(self, trial_tdof_list, test_tdof_list, A)
    FormRectangularSystemMatrix = _swig_new_instance_method(_bilinearform.MixedBilinearForm_FormRectangularSystemMatrix)

    def FormRectangularLinearSystem(self, trial_tdof_list, test_tdof_list, x, b, A, X, B):
        r"""FormRectangularLinearSystem(MixedBilinearForm self, intArray trial_tdof_list, intArray test_tdof_list, Vector x, Vector b, OperatorHandle A, Vector X, Vector B)"""
        return _bilinearform.MixedBilinearForm_FormRectangularLinearSystem(self, trial_tdof_list, test_tdof_list, x, b, A, X, B)
    FormRectangularLinearSystem = _swig_new_instance_method(_bilinearform.MixedBilinearForm_FormRectangularLinearSystem)

    def Update(self):
        r"""Update(MixedBilinearForm self)"""
        return _bilinearform.MixedBilinearForm_Update(self)
    Update = _swig_new_instance_method(_bilinearform.MixedBilinearForm_Update)

    def TrialFESpace(self, *args):
        r"""
        TrialFESpace(MixedBilinearForm self) -> FiniteElementSpace
        TrialFESpace(MixedBilinearForm self) -> FiniteElementSpace
        """
        return _bilinearform.MixedBilinearForm_TrialFESpace(self, *args)
    TrialFESpace = _swig_new_instance_method(_bilinearform.MixedBilinearForm_TrialFESpace)

    def TestFESpace(self, *args):
        r"""
        TestFESpace(MixedBilinearForm self) -> FiniteElementSpace
        TestFESpace(MixedBilinearForm self) -> FiniteElementSpace
        """
        return _bilinearform.MixedBilinearForm_TestFESpace(self, *args)
    TestFESpace = _swig_new_instance_method(_bilinearform.MixedBilinearForm_TestFESpace)
    __swig_destroy__ = _bilinearform.delete_MixedBilinearForm

# Register MixedBilinearForm in _bilinearform:
_bilinearform.MixedBilinearForm_swigregister(MixedBilinearForm)

class DiscreteLinearOperator(MixedBilinearForm):
    r"""Proxy of C++ mfem::DiscreteLinearOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, domain_fes, range_fes):
        r"""__init__(DiscreteLinearOperator self, FiniteElementSpace domain_fes, FiniteElementSpace range_fes) -> DiscreteLinearOperator"""
        _bilinearform.DiscreteLinearOperator_swiginit(self, _bilinearform.new_DiscreteLinearOperator(domain_fes, range_fes))

    def AddDomainInterpolator(self, di):
        r"""AddDomainInterpolator(DiscreteLinearOperator self, DiscreteInterpolator di)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(di)
        di.thisown=0 


        return _bilinearform.DiscreteLinearOperator_AddDomainInterpolator(self, di)


    def AddTraceFaceInterpolator(self, di):
        r"""AddTraceFaceInterpolator(DiscreteLinearOperator self, DiscreteInterpolator di)"""

        if not hasattr(self, "_integrators"): self._integrators = []
        self._integrators.append(di)
        di.thisown=0 


        return _bilinearform.DiscreteLinearOperator_AddTraceFaceInterpolator(self, di)


    def GetDI(self):
        r"""GetDI(DiscreteLinearOperator self) -> mfem::Array< mfem::BilinearFormIntegrator * > *"""
        return _bilinearform.DiscreteLinearOperator_GetDI(self)
    GetDI = _swig_new_instance_method(_bilinearform.DiscreteLinearOperator_GetDI)

    def Assemble(self, skip_zeros=1):
        r"""Assemble(DiscreteLinearOperator self, int skip_zeros=1)"""
        return _bilinearform.DiscreteLinearOperator_Assemble(self, skip_zeros)
    Assemble = _swig_new_instance_method(_bilinearform.DiscreteLinearOperator_Assemble)
    __swig_destroy__ = _bilinearform.delete_DiscreteLinearOperator

# Register DiscreteLinearOperator in _bilinearform:
_bilinearform.DiscreteLinearOperator_swigregister(DiscreteLinearOperator)



