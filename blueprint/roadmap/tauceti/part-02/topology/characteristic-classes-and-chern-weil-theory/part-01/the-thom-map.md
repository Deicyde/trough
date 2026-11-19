---
declaration: def
origin: cited
lean: TauCeti.thomMap
statement: formalized
---

# The Thom map

**The Thom map** `a ↦ π^*a ⌣ u` of a relative class `u ∈ Hⁿ(E, E₀; K)`, from `Hᵖ(B; M)` to
`Hᵐ(E, E₀; M)`, `p + n = m`, as a `K`-bilinear map of `u` and `a`. The chain coefficients are `K`,
and the pairing of values is the right unitor `M ⊗ K ≅ M`. For a Thom class `u` of a real vector
bundle of rank `n` it is the Thom isomorphism.

```lean
TauCeti.thomMap.{w, u_1} {B : Type w} [TopologicalSpace B] (F : Type u_1) [TopologicalSpace F]
  (E : B → Type w) [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → Zero (E b)]
  [(b : B) → TopologicalSpace (E b)] [FiberBundle F E] {K : Type w} [CommRing K] (M : ModuleCat K)
  (n p m : ℕ) (h : p + n = m) :
  ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) n) →ₗ[K]
    ↑(TopCat.singularCohomology (↧K) K M (↧B) p) →ₗ[K]
      ↑((TauCeti.thomPair F E).singularCohomology (↧K) K M m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.thomMap`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Isomorphism.html#TauCeti.thomMap).

## Sources

- [Tau Ceti documentation: `TauCeti.thomMap`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/Isomorphism.html#TauCeti.thomMap)
- [Source of `TauCeti.thomMap` in TauCeti/Topology/VectorBundle/Thom/Isomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Thom/Isomorphism.lean#L89)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
