---
declaration: theorem
origin: cited
lean: TauCeti.relativePropertyT_inl_of_injective_of_not_amenable, TauCeti.relativePropertyT_inl_of_injective_of_not_hasFoelnerSets, TauCeti.relativePropertyT_inl_of_not_amenable
statement: formalized
proof: formalized
---

# Burger's theorem

if a topological group `G` embeds injectively into `SL(2, ℤ)` and is not
amenable, then the normal subgroup `ℤ²` inside `ℤ² ⋊ G` has relative property (T) in every
Hilbert-space universe `u`.

```lean
TauCeti.relativePropertyT_inl_of_injective_of_not_amenable.{u, v} {G : Type v} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] {ι : G →* Matrix.SpecialLinearGroup (Fin 2) ℤ}
  (hι : Function.Injective ⇑ι) (hG : ¬TauCeti.Amenable G) :
  SemidirectProduct.inl.range.RelativePropertyT
```

## Depends on

- [Subgroup.RelativePropertyT](../../approximation-deformation-and-rigidity-of-finite/subgroup-relativepropertyt.md)
- [TauCeti.Amenable](../../amenable-groups/tauceti-amenable.md)

## Proof depends on

- [ContRepresentation.HasAlmostInvariantVectors](../../approximation-deformation-and-rigidity-of-finite/contrepresentation-hasalmostinvariantvectors.md)
- [Furstenberg's concentration lemma on the projective line](../../../geometry/part-02/manifold/part-02/furstenbergs-concentration-lemma-on-the-projecti.md)
- [TauCeti.Amenable.of_commGroup](../../amenable-groups/tauceti-amenable-of-commgroup.md)
- [TauCeti.Mean.instCompactSpace](../../amenable-groups/tauceti-mean-instcompactspace.md)
- [Uniqueness of the projection-valued measure of a representation](../../../analysis/part-02/operator-theory/uniqueness-of-the-projection-valued-measure-of-a.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.relativePropertyT_inl_of_injective_of_not_amenable`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/SpecialLinear.html#TauCeti.relativePropertyT_inl_of_injective_of_not_amenable).

## Other forms

**Burger's theorem (Følner form).** Formalized in Tau Ceti as [`TauCeti.relativePropertyT_inl_of_injective_of_not_hasFoelnerSets`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/SpecialLinear.html#TauCeti.relativePropertyT_inl_of_injective_of_not_hasFoelnerSets).

```lean
TauCeti.relativePropertyT_inl_of_injective_of_not_hasFoelnerSets.{u, v} {G : Type v} [Group G]
  {ι : G →* Matrix.SpecialLinearGroup (Fin 2) ℤ} (hι : Function.Injective ⇑ι)
  (hG : ¬TauCeti.HasFoelnerSets G) : SemidirectProduct.inl.range.RelativePropertyT
```

**Burger's theorem for subgroups `G ≤ SL(2, ℤ)`.** Formalized in Tau Ceti as [`TauCeti.relativePropertyT_inl_of_not_amenable`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/SpecialLinear.html#TauCeti.relativePropertyT_inl_of_not_amenable).

```lean
TauCeti.relativePropertyT_inl_of_not_amenable.{u}
  (G : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)) (hG : ¬TauCeti.Amenable ↥G) :
  SemidirectProduct.inl.range.RelativePropertyT
```

## Sources

- [Tau Ceti documentation: `TauCeti.relativePropertyT_inl_of_injective_of_not_amenable`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/SpecialLinear.html#TauCeti.relativePropertyT_inl_of_injective_of_not_amenable)
- [Source of `TauCeti.relativePropertyT_inl_of_injective_of_not_amenable` in TauCeti/GroupTheory/PropertyT/SpecialLinear.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/PropertyT/SpecialLinear.lean#L703)
