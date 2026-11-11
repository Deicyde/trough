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
- [Source of `TauCeti.MarkovEquiv.homfly_eq` in TauCeti/KnotTheory/Homfly/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Homfly/Existence.lean#L320)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricTopology/STATUS.md)
