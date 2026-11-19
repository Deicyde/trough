---
declaration: instance
origin: cited
lean: TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece
statement: formalized
---

# TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece

The signed symmetric algebra is internally graded by input degree.

```lean
TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece.{u, v} {R : Type u} [CommRing R] {V : Type v}
  [AddCommGroup V] [_root_.Module R V] (G : TauCeti.InternalGrading R V ℤ) :
  GradedAlgebra (TauCeti.signedSymPiece G)
```

## Depends on

- [TauCeti.SignedSym](tauceti-signedsym.md)

## Proof depends on

- [TauCeti.instGradedAlgebraIntTensorAlgebraTensorAlgebraPiece](tauceti-instgradedalgebrainttensoralgebratensora.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.html#TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece).

## Sources

- [Tau Ceti documentation: `TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.html#TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece)
- [Source of `TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean#L153)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
