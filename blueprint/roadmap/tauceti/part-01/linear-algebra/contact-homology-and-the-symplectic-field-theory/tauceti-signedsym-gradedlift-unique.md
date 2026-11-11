---
declaration: theorem
origin: cited
lean: TauCeti.SignedSym.gradedLift_unique
statement: formalized
proof: formalized
---

# TauCeti.SignedSym.gradedLift_unique

The degree-preserving extension is unique among graded algebra maps.

```lean
TauCeti.SignedSym.gradedLift_unique.{u, v, w} {R : Type u} [CommRing R] {V : Type v}
  [AddCommGroup V] [_root_.Module R V] (G : TauCeti.InternalGrading R V ℤ) {A : Type w} [Ring A]
  [Algebra R A] (𝒜 : ℤ → Submodule R A) [GradedAlgebra 𝒜] (f : V →ₗ[R] A)
  (hr :
    ∀ (p q : ℤ) (x y : V),
      x ∈ G.piece ℤ p → y ∈ G.piece ℤ q → f x * f y = ↑(p * q).negOnePow • (f y * f x))
  (hf : TauCeti.LinearMap.IsHomogeneous f (G.piece ℤ) 𝒜 0) (φ : TauCeti.signedSymPiece G →ₐᵍ[R] 𝒜)
  (hφ : ∀ (x : V), φ ((TauCeti.SignedSym.generator G) x) = f x) :
  φ = TauCeti.SignedSym.gradedLift G 𝒜 f hr hf
```

## Depends on

- [TauCeti.instGradedAlgebraIntSignedSymSignedSymPiece](tauceti-instgradedalgebraintsignedsymsignedsympi.md)
- [TauCeti.SignedSym](tauceti-signedsym.md)
- [TauCeti.SignedSym.gradedLift](tauceti-signedsym-gradedlift.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SignedSym.gradedLift_unique`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.html#TauCeti.SignedSym.gradedLift_unique).

## Sources

- [Tau Ceti documentation: `TauCeti.SignedSym.gradedLift_unique`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.html#TauCeti.SignedSym.gradedLift_unique)
- [Source of `TauCeti.SignedSym.gradedLift_unique` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean#L234)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
