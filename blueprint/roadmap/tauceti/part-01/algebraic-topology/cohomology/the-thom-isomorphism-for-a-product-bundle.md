---
declaration: theorem
origin: cited
lean: TauCeti.bijective_pullbackCup_prodThomPair
statement: formalized
proof: formalized
---

# The Thom isomorphism for a product bundle

Let `F` be a real normed space of finite
dimension `r ≥ 2`, and let `u ∈ Hʳ(B × F, B × (F ∖ {0}); K)` restrict on the fibre pair
`(F, F ∖ {0})` over every point of `B` to a generator of the `K`-module `Hʳ(F, F ∖ {0}; K)`.
Then for every `K`-module `M` and every degree `p`, the Thom map
`Hᵖ(B; M) ⟶ Hᵖ⁺ʳ(B × F, B × (F ∖ {0}); M)`, `a ↦ π^*a ⌣ u`, is bijective.

```lean
TauCeti.bijective_pullbackCup_prodThomPair.{w} {K : Type w} [CommRing K] (M : ModuleCat K)
  {B : Type w} [TopologicalSpace B] {F : Type w} [NormedAddCommGroup F] [NormedSpace ℝ F]
  (hF : 2 ≤ Module.finrank ℝ F)
  (u : ↑((TauCeti.prodThomPair B F).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F)))
  (hu :
    ∀ (b : B),
      K ∙
          (CategoryTheory.ConcreteCategory.hom
              (TopPair.singularCohomologyMap (TauCeti.prodThomPairFiberMap F b)
                (Module.finrank ℝ F)))
            u =
        ⊤)
  {p m : ℕ} (h : p + Module.finrank ℝ F = m) :
  Function.Bijective
    ⇑((TopPair.pullbackCup M (TauCeti.prodThomPair B F) (TauCeti.prodThomPairProj B F)
          (Module.finrank ℝ F) p m h)
        u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Eilenberg–Zilber theorem for singular chains](../singular/the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [The relative universal coefficient theorem over a field](the-relative-universal-coefficient-theorem-over.md)
- [The universal coefficient theorem over a field](the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bijective_pullbackCup_prodThomPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/ProdThomPair/Isomorphism.html#TauCeti.bijective_pullbackCup_prodThomPair).

## Sources

- [Tau Ceti documentation: `TauCeti.bijective_pullbackCup_prodThomPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/ProdThomPair/Isomorphism.html#TauCeti.bijective_pullbackCup_prodThomPair)
- [Source of `TauCeti.bijective_pullbackCup_prodThomPair` in TauCeti/AlgebraicTopology/Cohomology/ProdThomPair/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/ProdThomPair/Isomorphism.lean#L181)
