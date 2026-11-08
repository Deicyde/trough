---
declaration: theorem
origin: cited
lean: TopCat.isIso_reducedMayerVietorisδ
statement: formalized
proof: formalized
---

# The reduced Mayer–Vietoris connecting morphism is an isomorphism when both open sets are acyclic in the adjacent degrees

if the reduced homology of `U` and of `V` vanishes in degrees
`k` and `k + 1`, then `Hₖ₊₁(X) ⟶ H_redₖ(U ∩ V)` is an isomorphism.

```lean
TopCat.isIso_reducedMayerVietorisδ.{w, v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Limits.HasCoproducts C] [CategoryTheory.Abelian C] (R : C) {X : TopCat}
  {U V : Set ↑X} (hU : IsOpen U) (hV : IsOpen V) (hUV : U ∪ V = Set.univ) {k : ℕ}
  (hU₁ : CategoryTheory.Limits.IsZero ((TauCeti.reducedSingularHomologyFunctor R (k + 1)).obj ↧↑U))
  (hV₁ : CategoryTheory.Limits.IsZero ((TauCeti.reducedSingularHomologyFunctor R (k + 1)).obj ↧↑V))
  (hU₀ : CategoryTheory.Limits.IsZero ((TauCeti.reducedSingularHomologyFunctor R k).obj ↧↑U))
  (hV₀ : CategoryTheory.Limits.IsZero ((TauCeti.reducedSingularHomologyFunctor R k).obj ↧↑V)) :
  CategoryTheory.IsIso (TopCat.reducedMayerVietorisδ R hU hV hUV k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.isIso_reducedMayerVietorisδ`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/MayerVietoris/Reduced.html#TopCat.isIso_reducedMayerVietoris%CE%B4).

## Sources

- [Tau Ceti documentation: `TopCat.isIso_reducedMayerVietorisδ`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/MayerVietoris/Reduced.html#TopCat.isIso_reducedMayerVietoris%CE%B4)
- [Source of `TopCat.isIso_reducedMayerVietorisδ` in TauCeti/AlgebraicTopology/Singular/MayerVietoris/Reduced.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/MayerVietoris/Reduced.lean#L147)
