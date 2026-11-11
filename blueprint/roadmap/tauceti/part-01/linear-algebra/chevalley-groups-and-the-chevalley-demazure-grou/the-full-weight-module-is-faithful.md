---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.instIsFaithfulScModule
statement: formalized
proof: formalized
---

# The full-weight module is faithful

only the zero element of the pinned Lie algebra acts
by zero on `V_sc(t)`.

```lean
TauCeti.DynkinType.instIsFaithfulScModule (t : TauCeti.DynkinType) (ht : t.Valid) :
  LieModule.IsFaithful ℚ (↥(t.lieAlgebra ht)) (t.scModule ht)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.instIsFaithfulScModule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule.html#TauCeti.DynkinType.instIsFaithfulScModule).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.instIsFaithfulScModule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule.html#TauCeti.DynkinType.instIsFaithfulScModule)
- [Source of `TauCeti.DynkinType.instIsFaithfulScModule` in TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/RootSystem/SimplyConnectedRootDatum/LieAlgebra/SimplyConnectedModule.lean#L130)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
