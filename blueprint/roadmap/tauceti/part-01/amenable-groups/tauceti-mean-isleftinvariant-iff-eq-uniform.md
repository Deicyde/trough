---
declaration: theorem
origin: cited
lean: TauCeti.Mean.isLeftInvariant_iff_eq_uniform
statement: formalized
proof: formalized
---

# TauCeti.Mean.isLeftInvariant\_iff\_eq\_uniform

On a finite group, the uniform mean is the unique left-invariant mean.

```lean
TauCeti.Mean.isLeftInvariant_iff_eq_uniform.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [Finite G] {m : TauCeti.Mean G} :
  m.IsLeftInvariant ↔ m = TauCeti.Mean.uniform G
```

## Depends on

- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Mean.isLeftInvariant_iff_eq_uniform`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Finite.html#TauCeti.Mean.isLeftInvariant_iff_eq_uniform).

## Sources

- [Tau Ceti documentation: `TauCeti.Mean.isLeftInvariant_iff_eq_uniform`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Finite.html#TauCeti.Mean.isLeftInvariant_iff_eq_uniform)
- [Source of `TauCeti.Mean.isLeftInvariant_iff_eq_uniform` in TauCeti/GroupTheory/Amenable/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Finite.lean#L141)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)
