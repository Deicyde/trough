---
declaration: def
origin: cited
lean: TauCeti.profiniteFrattini
statement: formalized
---

# TauCeti.profiniteFrattini

The **Frattini subgroup** `Φ(G)` of a topological group: the intersection of its maximal open
subgroups. For a profinite group this is the Frattini subgroup of Ribes–Zalesskii; with the
discrete topology it is Mathlib's `frattini` (`TauCeti.profiniteFrattini_eq_frattini`).

```lean
TauCeti.profiniteFrattini.{u} (G : Type u) [Group G] [TopologicalSpace G] : Subgroup G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.profiniteFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Frattini.html#TauCeti.profiniteFrattini).

## Sources

- [Tau Ceti documentation: `TauCeti.profiniteFrattini`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Frattini.html#TauCeti.profiniteFrattini)
- [Source of `TauCeti.profiniteFrattini` in TauCeti/Topology/Algebra/Group/Profinite/Frattini.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Frattini.lean#L84)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
