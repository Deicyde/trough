---
declaration: def
origin: cited
lean: TauCeti.FiniteHopfModuleCat
statement: formalized
---

# TauCeti.FiniteHopfModuleCat

Left modules over `H` whose restriction to `k` is finite-dimensional, with carriers in the
universe of `k`. Only the algebra structure is needed for the underlying category.

```lean
TauCeti.FiniteHopfModuleCat.{u, v} (k : Type u) [Field k] (H : Type v) [Ring H] [Algebra k H] :
  Type (max (u + 1) v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteHopfModuleCat`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/Basic.html#TauCeti.FiniteHopfModuleCat).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteHopfModuleCat`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/Basic.html#TauCeti.FiniteHopfModuleCat)
- [Source of `TauCeti.FiniteHopfModuleCat` in TauCeti/Algebra/Category/FiniteHopfModuleCat/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/FiniteHopfModuleCat/Basic.lean#L53)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
