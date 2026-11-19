---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt
statement: formalized
proof: formalized
---

# TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt

A discrete group is amenable exactly when it satisfies **Reiter's condition**: for every
finite `K` and `ε > 0` there is a finitely supported probability density `p` with
`∑_{g ∈ K} ∑_x |p (g⁻¹ x) - p x| < ε`.

```lean
TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] :
  TauCeti.Amenable G ↔
    ∀ (K : Finset G) (ε : ℝ),
      0 < ε →
        ∃ p,
          0 ≤ p ∧
            Function.HasFiniteSupport p ∧
              ∑' (x : G), p x = 1 ∧ ∑ g ∈ K, ∑' (x : G), |p (g⁻¹ * x) - p x| < ε
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.Mean.instCompactSpace](tauceti-mean-instcompactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DiscreteFoelner.html#TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DiscreteFoelner.html#TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt)
- [Source of `TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt` in TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean#L148)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AmenableGroups/STATUS.md)
