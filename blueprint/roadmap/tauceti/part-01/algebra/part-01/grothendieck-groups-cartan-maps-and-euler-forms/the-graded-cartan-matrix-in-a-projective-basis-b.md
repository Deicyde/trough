---
declaration: def
origin: cited
lean: TauCeti.gradedCartanMatrix
statement: formalized
---

# The graded Cartan matrix in a projective basis `bP` and a module basis `bM`

the matrix
of the Laurent-linear graded Cartan map.  Rows are indexed by `bM` and columns by `bP`.

```lean
TauCeti.gradedCartanMatrix.{uk, uA, uI, uJ} {k : Type uk} [CommRing k] {A : Type uA} [Ring A]
  [Algebra k A] (𝒜 : ℤ → Submodule k A) {I : Type uI} {J : Type uJ} [Fintype I] [Finite J]
  (bP :
    Module.Basis I (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜)))
  (bM :
    Module.Basis J (LaurentPolynomial ℤ)
      (TauCeti.LaurentK0 (TauCeti.gradedFiniteModulesExactStructure 𝒜))) :
  Matrix J I (LaurentPolynomial ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.html#TauCeti.gradedCartanMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.html#TauCeti.gradedCartanMatrix)
- [Source of `TauCeti.gradedCartanMatrix` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.lean#L65)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
