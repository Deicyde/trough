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
- [Source of `TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean#L151)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
