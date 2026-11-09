---
declaration: abbrev
origin: cited
lean: TauCeti.UniversalEnvelopingAlgebra.reesAlgebra
statement: formalized
---

# TauCeti.UniversalEnvelopingAlgebra.reesAlgebra

The PBW Rees algebra: the coefficient of `tⁿ` belongs to PBW filtration degree `n`.

```lean
TauCeti.UniversalEnvelopingAlgebra.reesAlgebra.{u, v} (R : Type u) (L : Type v) [CommRing R]
  [LieRing L] [LieAlgebra R L] : Subalgebra R (Polynomial (UniversalEnvelopingAlgebra R L))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalEnvelopingAlgebra.reesAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/Basic.html#TauCeti.UniversalEnvelopingAlgebra.reesAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalEnvelopingAlgebra.reesAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/Basic.html#TauCeti.UniversalEnvelopingAlgebra.reesAlgebra)
- [Source of `TauCeti.UniversalEnvelopingAlgebra.reesAlgebra` in TauCeti/Algebra/Lie/UniversalEnveloping/Rees/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/UniversalEnveloping/Rees/Basic.lean#L52)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
