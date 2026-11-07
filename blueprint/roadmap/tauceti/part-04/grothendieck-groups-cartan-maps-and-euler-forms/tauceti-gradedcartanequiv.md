---
declaration: def
origin: cited
lean: TauCeti.gradedCartanEquiv
statement: formalized
---

# TauCeti.gradedCartanEquiv

If every finite graded module admits a finite graded-projective resolution, the graded Cartan
map is an isomorphism of `ℤ[q,q⁻¹]`-modules.

```lean
TauCeti.gradedCartanEquiv.{uk, uA} {k : Type uk} [CommRing k] {A : Type uA} [Ring A] [Algebra k A]
  (𝒜 : ℤ → Submodule k A) [DirectSum.Decomposition 𝒜]
  (h :
    TauCeti.gradedFiniteModules 𝒜 ≤
      (TauCeti.gradedModuleCanonicalExactStructure 𝒜).admitsFiniteResolution
        (TauCeti.gradedFiniteProjectiveModules 𝒜)) :
  TauCeti.LaurentK0 (TauCeti.gradedFiniteProjectiveModulesExactStructure 𝒜) ≃ₗ[LaurentPolynomial ℤ]
    TauCeti.LaurentK0 (TauCeti.gradedFiniteModulesExactStructure 𝒜)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.html#TauCeti.gradedCartanEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.html#TauCeti.gradedCartanEquiv)
- [Source of `TauCeti.gradedCartanEquiv` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/Resolution.lean#L273)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
