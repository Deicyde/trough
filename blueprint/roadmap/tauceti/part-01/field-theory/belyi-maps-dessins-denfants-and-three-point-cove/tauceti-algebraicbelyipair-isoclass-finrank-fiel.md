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
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.finrank_fieldOfModuli_eq_trueOrbitSize` in TauCeti/FieldTheory/FunctionField/Belyi/FiniteDescent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/Belyi/FiniteDescent.lean#L231)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BelyiMaps/STATUS.md)
