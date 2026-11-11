---
declaration: structure
origin: cited
lean: TauCeti.PositiveDegreeMap
statement: formalized
---

# TauCeti.PositiveDegreeMap

An additive map of positive degree data, together with a monotone cutoff modulus.
The modulus is part of the data, so two maps with different moduli need not be equal.

```lean
TauCeti.PositiveDegreeMap.{u_1, u_2} {N : Type u_1} {M : Type u_2} [AddCommMonoid N]
  [AddCommMonoid M] (d : TauCeti.PositiveDegrees N) (e : TauCeti.PositiveDegrees M) :
  Type (max u_1 u_2)
```

## Depends on

- [TauCeti.PositiveDegrees](tauceti-positivedegrees.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PositiveDegreeMap`](https://taucetiproject.org/docs/TauCeti/Algebra/PositiveDegrees/Map.html#TauCeti.PositiveDegreeMap).

## Sources

- [Tau Ceti documentation: `TauCeti.PositiveDegreeMap`](https://taucetiproject.org/docs/TauCeti/Algebra/PositiveDegrees/Map.html#TauCeti.PositiveDegreeMap)
- [Source of `TauCeti.PositiveDegreeMap` in TauCeti/Algebra/PositiveDegrees/Map.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/PositiveDegrees/Map.lean#L39)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
