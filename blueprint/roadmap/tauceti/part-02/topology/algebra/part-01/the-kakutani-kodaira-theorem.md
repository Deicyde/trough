---
declaration: theorem
origin: cited
lean: TauCeti.exists_compact_normal_subgroup_quotient_metrizable, TauCeti.exists_compact_normal_addSubgroup_quotient_metrizable
statement: formalized
proof: formalized
---

# The Kakutani–Kodaira theorem

In a σ-compact weakly locally compact topological group `G`,
for any countable family `U` of neighbourhoods of `1`, there exists a closed compact normal
subgroup `K` contained in `⋂ i, U i` whose quotient `G ⧸ K` is metrizable and second countable.

```lean
TauCeti.exists_compact_normal_subgroup_quotient_metrizable.{u_1, u_2} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [WeaklyLocallyCompactSpace G] [SigmaCompactSpace G]
  {ι : Type u_2} [Countable ι] (U : ι → Set G) (hU : ∀ (i : ι), U i ∈ nhds 1) :
  ∃ K,
    ∃ (x : K.Normal),
      IsCompact ↑K ∧
        IsClosed ↑K ∧
          ↑K ⊆ ⋂ i, U i ∧
            (nhds 1).IsCountablyGenerated ∧
              TopologicalSpace.MetrizableSpace (G ⧸ K) ∧ SecondCountableTopology (G ⧸ K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Birkhoff–Kakutani theorem](birkhoff-kakutani-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_compact_normal_subgroup_quotient_metrizable`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/KakutaniKodaira.html#TauCeti.exists_compact_normal_subgroup_quotient_metrizable).

## Other forms

**The Kakutani–Kodaira theorem (additive form).** Formalized in Tau Ceti as [`TauCeti.exists_compact_normal_addSubgroup_quotient_metrizable`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/KakutaniKodaira.html#TauCeti.exists_compact_normal_addSubgroup_quotient_metrizable).

```lean
TauCeti.exists_compact_normal_addSubgroup_quotient_metrizable.{u_1, u_2} {G : Type u_1} [AddGroup G]
  [TopologicalSpace G] [IsTopologicalAddGroup G] [WeaklyLocallyCompactSpace G] [SigmaCompactSpace G]
  {ι : Type u_2} [Countable ι] (U : ι → Set G) (hU : ∀ (i : ι), U i ∈ nhds 0) :
  ∃ K,
    ∃ (x : K.Normal),
      IsCompact ↑K ∧
        IsClosed ↑K ∧
          ↑K ⊆ ⋂ i, U i ∧
            (nhds 0).IsCountablyGenerated ∧
              TopologicalSpace.MetrizableSpace (G ⧸ K) ∧ SecondCountableTopology (G ⧸ K)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_compact_normal_subgroup_quotient_metrizable`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/KakutaniKodaira.html#TauCeti.exists_compact_normal_subgroup_quotient_metrizable)
- [Source of `TauCeti.exists_compact_normal_subgroup_quotient_metrizable` in TauCeti/Topology/Algebra/Group/KakutaniKodaira.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/KakutaniKodaira.lean#L171)
