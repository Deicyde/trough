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
      x ∈ G.piece p → y ∈ G.piece q → f x * f y = ↑(p * q).negOnePow • (f y * f x))
  (hf : TauCeti.LinearMap.IsHomogeneous f G.piece 𝒜 0) (φ : TauCeti.signedSymPiece G →ₐᵍ[R] 𝒜)
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
- [Source of `TauCeti.SignedSym.gradedLift_unique` in TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/SignedSymmetricAlgebra/Grading.lean#L266)
- [Tau Ceti roadmap status: Contact homology and the symplectic field theory formalism](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticFieldTheory/STATUS.md)
