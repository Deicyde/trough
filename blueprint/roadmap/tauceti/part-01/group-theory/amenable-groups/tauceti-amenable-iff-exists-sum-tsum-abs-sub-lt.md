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
- [Source of `TauCeti.amenable_iff_exists_sum_tsum_abs_sub_lt` in TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Amenable/DiscreteFoelner.lean#L148)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
