---
declaration: def
origin: cited
lean: TauCeti.SignedSym.gradedLift
statement: formalized
---

# TauCeti.SignedSym.gradedLift

The graded universal extension of a degree-preserving generator assignment satisfying
the Koszul relations. Its underlying algebra map is `SignedSym.lift`.

```lean
TauCeti.SignedSym.gradedLift.{u, v, w} {R : Type u} [CommRing R] {V : Type v} [AddCommGroup V]
  [_root_.Module R V] (G : TauCeti.InternalGrading R V ℤ) {A : Type w} [Ring A] [Algebra R A]
  (𝒜 : ℤ → Submodule R A) [GradedAlgebra 𝒜] (f : V →ₗ[R] A)
  (hr :
    ∀ (p q : ℤ) (x y : V),
      x ∈ G.piece p → y ∈ G.piece q → f x * f y = ↑(p * q).negOnePow • (f y * f x))
  (hf : TauCeti.LinearMap.IsHomogeneous f G.piece 𝒜 0) : TauCeti.signedSymPiece G →ₐᵍ[R] 𝒜
```

## Depends on

- [TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece](tauceti-instgradedalgebraintsignedsymsignedsympi.md)
- [TauCeti.SignedSym](tauceti-signedsym.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SignedSym.gradedLift`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.html#TauCeti.SignedSym.gradedLift).

## Sources

- [Tau Ceti documentation: `TauCeti.SignedSym.gradedLift`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.html#TauCeti.SignedSym.gradedLift)
- [Source of `TauCeti.SignedSym.gradedLift` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean#L237)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
