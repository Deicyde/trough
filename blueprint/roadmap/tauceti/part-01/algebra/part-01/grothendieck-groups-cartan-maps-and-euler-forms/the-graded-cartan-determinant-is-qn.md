---
declaration: theorem
origin: cited
lean: TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution
statement: formalized
proof: formalized
---

# The graded Cartan determinant is `±qⁿ`

If every finite graded module has a finite
graded-projective resolution, the graded Cartan matrix in a projective basis and a module basis
indexed by the same finite type has determinant `qⁿ` or `-qⁿ` for some `n : ℤ`. This is the
graded counterpart of `TauCeti.cartanMatrix_det_eq_one_or_neg_one`; neither the sign nor the
exponent is asserted.

```lean
TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution.{uk, uA, u_1}
  {k : Type uk} [CommRing k] {A : Type uA} [Ring A] [Algebra k A] (𝒜 : ℤ → Submodule k A)
  [DirectSum.Decomposition 𝒜]
  (h :
    TauCeti.gradedFiniteModules 𝒜 ≤
      (TauCeti.gradedModuleCanonicalExactStructure 𝒜).admitsFiniteResolution
        (TauCeti.gradedFiniteProjectiveModules 𝒜))
  {I : Type u_1} [Fintype I] [DecidableEq I]
  (bP :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)))
  (bM :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteModulesExactStructure 𝒜))) :
  ∃ n,
    (TauCeti.gradedCartanMatrix 𝒜 bP bM).det = LaurentPolynomial.T n ∨
      (TauCeti.gradedCartanMatrix 𝒜 bP bM).det = -LaurentPolynomial.T n
```

## Depends on

- [The graded Cartan matrix in a projective basis `bP` and a module basis `bM`](the-graded-cartan-matrix-in-a-projective-basis-b.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The graded resolution theorem](../../../category-theory/grothendieck-group/the-graded-resolution-theorem.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [The resolution theorem for finite projective resolutions](../../../category-theory/grothendieck-group/the-resolution-theorem-for-finite-projective-res.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.html#TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.html#TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution)
- [Source of `TauCeti.exists_gradedCartanMatrix_det_eq_T_or_neg_T_of_le_admitsFiniteResolution` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.lean#L321)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
