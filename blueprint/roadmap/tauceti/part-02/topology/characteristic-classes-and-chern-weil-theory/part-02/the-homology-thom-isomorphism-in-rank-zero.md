---
declaration: theorem
origin: cited
lean: TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero
statement: formalized
proof: formalized
---

# The homology Thom isomorphism in rank zero

For a bundle of rank zero and a Thom class `u`
with coefficients in a field `K`, the homology Thom map `x ↦ π_*(x ⌢ u)` is a bijection
`Hₘ(E, E₀; K) ≅ Hₘ(B; K)` in every degree.

```lean
TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero.{w, u_1} {B : Type w}
  [TopologicalSpace B] {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type w}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → Zero (E b)]
  [(b : B) → TopologicalSpace (E b)] [FiberBundle F E] {K : Type w} [Field K]
  (hF : Module.finrank ℝ F = 0)
  {u : ↑((TauCeti.thomPair F E).singularCohomology (↧K) K (↧K) (Module.finrank ℝ F))}
  (hu : TauCeti.IsThomClass F E u) {p m : ℕ} (h : Module.finrank ℝ F + p = m) :
  Function.Bijective
    ⇑(ModuleCat.Hom.hom ((TauCeti.homologyThomMap F E (↧K) (Module.finrank ℝ F) p m h) u))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative universal coefficient theorem over a field](../../../../part-01/algebraic-topology/cohomology/the-relative-universal-coefficient-theorem-over.md)
- [The Thom isomorphism in rank zero](the-thom-isomorphism-in-rank-zero.md)
- [The Thom map](../part-01/the-thom-map.md)
- [The universal coefficient theorem over a field](../../../../part-01/algebraic-topology/cohomology/the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/RankZero.html#TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Thom/RankZero.html#TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero)
- [Source of `TauCeti.IsThomClass.bijective_homologyThomMap_of_finrank_eq_zero` in TauCeti/Topology/VectorBundle/Thom/RankZero.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Thom/RankZero.lean#L178)
