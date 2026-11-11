---
declaration: instance
origin: cited
lean: TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece
statement: formalized
---

# TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece

The tensor algebra is a `ℤ`-graded algebra for the input-degree grading.

```lean
TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece.{uR, uM} {R : Type uR} {M : Type uM}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] (G : TauCeti.InternalGrading R M ℤ) :
  GradedAlgebra (TauCeti.tensorAlgebraPiece G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/TensorAlgebra/Grading.html#TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece).

## Sources

- [Tau Ceti documentation: `TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/TensorAlgebra/Grading.html#TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece)
- [Source of `TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece` in TauCeti/LinearAlgebra/TensorAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/TensorAlgebra/Grading.lean#L139)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
