---
declaration: theorem
origin: cited
lean: TauCeti.isMinOn_sublevel_iff
statement: formalized
proof: formalized
---

# TauCeti.isMinOn_sublevel_iff

A minimum on a sublevel is a minimum on the whole set, provided its value is
below the sublevel threshold.

```lean
TauCeti.isMinOn_sublevel_iff.{u_1, u_2} {X : Type u_1} {β : Type u_2} [LinearOrder β] {f : X → β}
  {S : Set X} {u : X} {b : β} (hu : f u ≤ b) : IsMinOn f {x | x ∈ S ∧ f x ≤ b} u ↔ IsMinOn f S u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isMinOn_sublevel_iff`](https://taucetiproject.org/docs/TauCeti/Order/Filter/Extr.html#TauCeti.isMinOn_sublevel_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.isMinOn_sublevel_iff`](https://taucetiproject.org/docs/TauCeti/Order/Filter/Extr.html#TauCeti.isMinOn_sublevel_iff)
- [Source of `TauCeti.isMinOn_sublevel_iff` in TauCeti/Order/Filter/Extr.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Order/Filter/Extr.lean#L25)
- [Tau Ceti roadmap status: Variational methods and constrained spectral theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VariationalMethods/STATUS.md)
