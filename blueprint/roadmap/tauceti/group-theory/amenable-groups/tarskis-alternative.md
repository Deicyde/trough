---
declaration: theorem
origin: cited
lean: TauCeti.amenable_iff_not_paradoxical_univ, TauCeti.hasFoelnerSets_iff_not_paradoxical_univ
statement: formalized
proof: formalized
---

# Tarski's alternative

a discrete group is amenable exactly when it is not paradoxical for
its left regular action.

```lean
TauCeti.amenable_iff_not_paradoxical_univ.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] : TauCeti.Amenable G ↔ ¬TauCeti.Paradoxical G Set.univ
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [Equidecompositions as partitions](equidecompositions-as-partitions.md)
- [Hall's theorem for expanding sets](../../combinatorics/other-results/halls-theorem-for-expanding-sets.md)
- [Reiter implies Følner](reiter-implies-flner.md)
- [Schröder–Bernstein theorem for equidecompositions](schroder-bernstein-theorem-for-equidecomposition.md)
- [TauCeti.Amenable.of_hasFoelnerSets](tauceti-amenable-of-hasfoelnersets.md)
- [TauCeti.hasFoelnerSets_iff](tauceti-hasfoelnersets-iff.md)
- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.amenable_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.amenable_iff_not_paradoxical_univ).

## Other forms

**Tarski's alternative, topology-free form.** Formalized in Tau Ceti as [`TauCeti.hasFoelnerSets_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.hasFoelnerSets_iff_not_paradoxical_univ).

```lean
TauCeti.hasFoelnerSets_iff_not_paradoxical_univ.{u_1} {G : Type u_1} [Group G] :
  TauCeti.HasFoelnerSets G ↔ ¬TauCeti.Paradoxical G Set.univ
```

## Sources

- [Tau Ceti documentation: `TauCeti.amenable_iff_not_paradoxical_univ`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Tarski.html#TauCeti.amenable_iff_not_paradoxical_univ)
- [Source of `TauCeti.amenable_iff_not_paradoxical_univ` in TauCeti/GroupTheory/Amenable/Tarski.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Tarski.lean#L96)
