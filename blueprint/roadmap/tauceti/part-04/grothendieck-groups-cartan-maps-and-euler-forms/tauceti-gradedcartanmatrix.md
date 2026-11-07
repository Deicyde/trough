---
declaration: def
origin: cited
lean: TauCeti.gradedCartanMatrix
statement: formalized
---

# TauCeti.gradedCartanMatrix

**The graded Cartan matrix** in a projective basis `bP` and a module basis `bM`: the matrix
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

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.html#TauCeti.gradedCartanMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.html#TauCeti.gradedCartanMatrix)
- [Source of `TauCeti.gradedCartanMatrix` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Matrix.lean#L61)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
