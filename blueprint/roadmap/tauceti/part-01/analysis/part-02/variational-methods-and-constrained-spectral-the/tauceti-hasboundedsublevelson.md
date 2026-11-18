---
declaration: def
origin: cited
lean: TauCeti.HasBoundedSublevelsOn
statement: formalized
---

# TauCeti.HasBoundedSublevelsOn

Every sublevel of `E` relative to `S` is bounded. No lower bound on `E` is required.

```lean
TauCeti.HasBoundedSublevelsOn.{u_1, u_2} {X : Type u_1} {β : Type u_2} [Bornology X] [LE β]
  (E : X → β) (S : Set X) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasBoundedSublevelsOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/BoundedSublevels.html#TauCeti.HasBoundedSublevelsOn).

## Sources

- [Tau Ceti documentation: `TauCeti.HasBoundedSublevelsOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/BoundedSublevels.html#TauCeti.HasBoundedSublevelsOn)
- [Source of `TauCeti.HasBoundedSublevelsOn` in TauCeti/Analysis/Variational/BoundedSublevels.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Variational/BoundedSublevels.lean#L27)
- [Tau Ceti roadmap status: Variational methods and constrained spectral theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VariationalMethods/STATUS.md)
