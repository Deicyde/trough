---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq
statement: formalized
proof: formalized
---

# Burnside's surjectivity criterion

A continuous homomorphism from a compact group
to a profinite pro-`p` group is surjective exactly when its composites with all index-`p`
quotient maps are surjective.

```lean
TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq.{u_1, u_2} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {G : Type u_1} [Group G] {H : Type u_2} [Group H] [TopologicalSpace H]
  [IsTopologicalGroup H] [CompactSpace H] [TotallyDisconnectedSpace H] [TopologicalSpace G]
  [CompactSpace G] (hH : TauCeti.IsProP p H) (f : G →* H) (hf : Continuous ⇑f) :
  Function.Surjective ⇑f ↔
    ∀ (U : OpenNormalSubgroup H),
      (↑U.toOpenSubgroup).index = p →
        Function.Surjective ⇑((QuotientGroup.mk' ↑U.toOpenSubgroup).comp f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Surjective.html#TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Surjective.html#TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq)
- [Source of `TauCeti.IsProP.surjective_iff_surjective_quotient_index_eq` in TauCeti/Topology/Algebra/Group/Profinite/ProP/Surjective.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/ProP/Surjective.lean#L86)
