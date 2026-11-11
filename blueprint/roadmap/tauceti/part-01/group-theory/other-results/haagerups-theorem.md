---
declaration: theorem
origin: cited
lean: TauCeti.hasHaagerupProperty_freeGroup
statement: formalized
proof: formalized
---

# Haagerup's theorem

The free group on a countable set of generators has the Haagerup
property.

```lean
TauCeti.hasHaagerupProperty_freeGroup.{u_1} (ι : Type u_1) [Countable ι] :
  TauCeti.HasHaagerupProperty (FreeGroup ι)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Haagerup's cocycle identity](../free-group/haagerups-cocycle-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasHaagerupProperty_freeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/HaagerupProperty/FreeGroup.html#TauCeti.hasHaagerupProperty_freeGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.hasHaagerupProperty_freeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/HaagerupProperty/FreeGroup.html#TauCeti.hasHaagerupProperty_freeGroup)
- [Source of `TauCeti.hasHaagerupProperty_freeGroup` in TauCeti/GroupTheory/HaagerupProperty/FreeGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/HaagerupProperty/FreeGroup.lean#L46)
