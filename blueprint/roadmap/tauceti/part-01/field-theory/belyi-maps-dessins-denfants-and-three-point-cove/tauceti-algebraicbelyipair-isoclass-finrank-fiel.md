---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize
statement: formalized
proof: formalized
---

# TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize

Over a Galois extension `k` of `ℚ`, such as `AlgebraicClosure ℚ`, the degree of the field of
moduli of a class over `ℚ` is its true orbit size.

```lean
TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize.{u} {k : Type u}
  [Field k] [CharZero k] [IsGalois ℚ k] (c : TauCeti.AlgebraicBelyiPair.IsoClass k) :
  Module.finrank ℚ ↥c.fieldOfModuli = c.trueOrbitSize
```

## Depends on

- [The Galois action on isomorphism classes](the-galois-action-on-isomorphism-classes.md)
- [TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli](tauceti-algebraicbelyipair-isoclass-fieldofmodul.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/FiniteDescent.html#TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/FiniteDescent.html#TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize)
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize` in TauCeti/FieldTheory/FunctionField/Belyi/FiniteDescent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Belyi/FiniteDescent.lean#L231)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
