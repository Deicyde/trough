---
declaration: theorem
origin: cited
lean: TauCeti.MarkovEquiv.homfly_eq
statement: formalized
proof: formalized
---

# The HOMFLY polynomial is a link invariant on braid closures

Markov-equivalent braids
have the same HOMFLY polynomial.

```lean
TauCeti.MarkovEquiv.homfly_eq.{u_1} (K : Type u_1) [Field K] {β γ : TauCeti.MarkovBraid}
  (h : TauCeti.MarkovEquiv β γ) : TauCeti.MarkovBraid.homfly K β = TauCeti.MarkovBraid.homfly K γ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MarkovEquiv.homfly_eq`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Homfly/Existence.html#TauCeti.MarkovEquiv.homfly_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.MarkovEquiv.homfly_eq`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Homfly/Existence.html#TauCeti.MarkovEquiv.homfly_eq)
- [Source of `TauCeti.MarkovEquiv.homfly_eq` in TauCeti/KnotTheory/Homfly/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Homfly/Existence.lean#L320)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
