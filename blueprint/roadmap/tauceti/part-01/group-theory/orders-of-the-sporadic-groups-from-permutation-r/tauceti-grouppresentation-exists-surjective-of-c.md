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
- [Source of `TauCeti.GroupPresentation.exists_surjective_of_closure_range_eq` in TauCeti/GroupTheory/Presentation/GroupPresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Presentation/GroupPresentation.lean#L244)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SporadicOrders/STATUS.md)
