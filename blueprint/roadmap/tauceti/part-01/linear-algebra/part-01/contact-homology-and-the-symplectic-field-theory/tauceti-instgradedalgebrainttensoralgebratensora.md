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
- [Source of `TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece` in TauCeti/LinearAlgebra/TensorAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/TensorAlgebra/Grading.lean#L139)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
