---
declaration: theorem
origin: cited
lean: TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible
statement: formalized
proof: formalized
---

# The graded Cartan map is an isomorphism when the simples are Euler-admissible

Over a
finite-dimensional nonnegatively graded algebra with semisimple degree-zero part, if every pair of
members of an exhaustive family of graded simples is graded Euler-admissible, then the graded
Cartan map `K₀^gr(proj A) ⟶ G₀^gr(mod A)` is bijective.

```lean
TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible.{w, uk, uA, uI} {k : Type uk} [Field k]
  {A : Type uA} [Ring A] [Algebra k A] [Module.Finite k A] {𝒜 : ℤ → Submodule k A} [GradedAlgebra 𝒜]
  [IsSemisimpleRing ↥(𝒜 0)] [CategoryTheory.HasExt (TauCeti.GradedModuleCat 𝒜)]
  (hneg : ∀ p < 0, 𝒜 p = ⊥) {I : Type uI} [Finite I]
  {S : I → (TauCeti.gradedFiniteModules 𝒜).FullSubcategory}
  (hS : TauCeti.IsExhaustiveGradedSimpleFamily S)
  (h :
    ∀ (i j : I),
      TauCeti.IsGradedEulerAdmissible k (TauCeti.GradedModuleCat.shift 𝒜) (S i).obj (S j).obj) :
  Function.Bijective ⇑(TauCeti.gradedCartanMap 𝒜)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)
- [TauCeti.gradedCartanEquiv](tauceti-gradedcartanequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/EulerAdmissible.html#TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/EulerAdmissible.html#TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible)
- [Source of `TauCeti.gradedCartanMap_bijective_of_isGradedEulerAdmissible` in TauCeti/Algebra/Category/GradedModuleCat/CartanMap/EulerAdmissible.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/GradedModuleCat/CartanMap/EulerAdmissible.lean#L100)
