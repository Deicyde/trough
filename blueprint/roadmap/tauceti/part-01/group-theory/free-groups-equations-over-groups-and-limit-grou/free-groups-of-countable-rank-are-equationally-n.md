---
declaration: theorem
origin: cited
lean: TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis
statement: formalized
proof: formalized
---

# Free groups of countable rank are equationally Noetherian

A group with a countable
free basis is equationally Noetherian over any coefficients; for free groups of finite rank this
is Guba's theorem.

```lean
TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis.{u_1, u_2, u_6} {G : Type u_1}
  {H : Type u_2} [Group G] [Group H] {κ : Type u_6} [Countable κ] (ι : G →* H)
  (b : FreeGroupBasis κ H) : TauCeti.GroupAlgGeom.IsEquationallyNoetherian ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Linear.html#TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Linear.html#TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis)
- [Source of `TauCeti.GroupAlgGeom.isEquationallyNoetherian_of_freeGroupBasis` in TauCeti/GroupTheory/GroupAlgGeom/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAlgGeom/Linear.lean#L221)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
