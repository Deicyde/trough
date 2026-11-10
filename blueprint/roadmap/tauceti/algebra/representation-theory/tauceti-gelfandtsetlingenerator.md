---
declaration: def
origin: cited
lean: TauCeti.gelfandTsetlinGenerator
statement: formalized
---

# TauCeti.gelfandTsetlinGenerator

The **Gelfand-Tsetlin generator** of degree `r` at level `k ≤ n`: the image in `U(gl (Fin n))`
of the Gelfand invariant `Cᵣ` of the upper-left corner `gl (Fin k)`.

```lean
TauCeti.gelfandTsetlinGenerator.{u_1} (K : Type u_1) [CommRing K] {n k : ℕ} (hk : k ≤ n) (r : ℕ) :
  UniversalEnvelopingAlgebra K (Matrix (Fin n) (Fin n) K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.gelfandTsetlinGenerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/GeneralLinear/GelfandInvariant/Basic.html#TauCeti.gelfandTsetlinGenerator).

## Sources

- [Tau Ceti documentation: `TauCeti.gelfandTsetlinGenerator`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/GeneralLinear/GelfandInvariant/Basic.html#TauCeti.gelfandTsetlinGenerator)
- [Source of `TauCeti.gelfandTsetlinGenerator` in TauCeti/Algebra/Lie/GeneralLinear/GelfandInvariant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/GeneralLinear/GelfandInvariant/Basic.lean#L216)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
