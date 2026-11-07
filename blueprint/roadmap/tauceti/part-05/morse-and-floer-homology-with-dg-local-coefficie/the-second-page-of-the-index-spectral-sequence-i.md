---
declaration: def
origin: cited
lean: TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso
statement: formalized
---

# The second page of the index spectral sequence is the cohomology of the classical complex

(BDHO, Definition 3.38 and Ch. 3 §4.2): the object at `(a, b)` of the page `3` of the index
spectral sequence (the classical `E₂` page, in Mathlib's numbering of pages) is the homology in
degree `b + 1` of the classical complex in coefficient degree `a + 2 * b + 1`. It is the
homology of the first page at `(a, b)`, identified with the homology of the classical complex by
`indexSecondPageShortComplexIso` (see `indexSpectralSequenceSecondPageXIso_eq`).

```lean
TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso.{uR, uA, uM, uP} {R : Type uR}
  {A : Type uA} {M : Type uM} [CommRing R] [Ring A] [Algebra R A] [AddCommGroup M]
  [_root_.Module R M] {P : Type uP} {ind : P → ℤ} [Fintype P] [_root_.Module Aᵐᵒᵖ M]
  [IsScalarTower R Aᵐᵒᵖ M] {ℳ : ℤ → Submodule R M} [DirectSum.Decomposition ℳ] {dM : M →ₗ[R] M}
  {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {d : A →ₗ[R] A} {h : TauCeti.IsDGAlgebra 𝒜 d}
  [SetLike.GradedSMul ((TauCeti.InternalGrading.ofDecomposition 𝒜).opposite.piece ℤ) ℳ]
  (m : TauCeti.TwistingCocycle 𝒜 d P ind) (hM : TauCeti.IsDGRightModule h ℳ dM) [DecidableEq P]
  (a b : ℤ) :
  ((TauCeti.TwistingCocycle.indexSpectralSequence dM m hM).page 3
          TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso._proof_2).X
      (a, b) ≅
    HomologicalComplex.homology (m.indexClassicalComplex hM (a + 2 * b + 1)) (b + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Twisted/SpectralSequence/E2.html#TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso).

## Sources

- [Tau Ceti documentation: `TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DG/Twisted/SpectralSequence/E2.html#TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso)
- [Source of `TauCeti.TwistingCocycle.indexSpectralSequenceSecondPageXIso` in TauCeti/Algebra/Homology/DG/Twisted/SpectralSequence/E2.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/DG/Twisted/SpectralSequence/E2.lean#L355)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
