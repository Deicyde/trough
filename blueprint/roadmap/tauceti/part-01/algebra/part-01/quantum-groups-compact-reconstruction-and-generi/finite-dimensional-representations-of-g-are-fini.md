---
declaration: def
origin: cited
lean: TauCeti.FiniteHopfModuleCat.equivalenceFDRep
statement: formalized
---

# Finite-dimensional representations of `G` are finite-dimensional `k[G]`-modules

The
functor is `ofFDRep k G` and the inverse is `toFDRep k G`.

```lean
TauCeti.FiniteHopfModuleCat.equivalenceFDRep.{u, v} (k : Type u) [Field k] (G : Type v) [Monoid G] :
  FDRep k G ≌ TauCeti.FiniteHopfModuleCat k (MonoidAlgebra k G)
```

## Depends on

- [TauCeti.FiniteHopfModuleCat](tauceti-finitehopfmodulecat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteHopfModuleCat.equivalenceFDRep`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/FDRep.html#TauCeti.FiniteHopfModuleCat.equivalenceFDRep).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteHopfModuleCat.equivalenceFDRep`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FiniteHopfModuleCat/FDRep.html#TauCeti.FiniteHopfModuleCat.equivalenceFDRep)
- [Source of `TauCeti.FiniteHopfModuleCat.equivalenceFDRep` in TauCeti/Algebra/Category/FiniteHopfModuleCat/FDRep.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/FiniteHopfModuleCat/FDRep.lean#L228)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuantumGroups/STATUS.md)
