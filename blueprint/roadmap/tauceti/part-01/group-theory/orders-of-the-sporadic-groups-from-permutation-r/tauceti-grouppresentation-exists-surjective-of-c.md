---
declaration: theorem
origin: cited
lean: TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq
statement: formalized
proof: formalized
---

# TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq

A satisfying assignment whose values generate a subgroup `H` gives a surjective homomorphism
from the presented group onto `H`.

```lean
TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq.{u_1}
  (P : TauCeti.GroupPresentation) {G : Type u_1} [Group G] {H : Subgroup G}
  (f : { f // ∀ t ∈ P.transcribed, (FreeGroup.lift f) t.toFreeGroup = 1 })
  (h : Subgroup.closure (Set.range ↑f) = H) : ∃ g, Function.Surjective ⇑g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/GroupPresentation.html#TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/GroupPresentation.html#TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq)
- [Source of `TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq` in TauCeti/GroupTheory/Presentation/GroupPresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Presentation/GroupPresentation.lean#L245)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SporadicOrders/STATUS.md)
