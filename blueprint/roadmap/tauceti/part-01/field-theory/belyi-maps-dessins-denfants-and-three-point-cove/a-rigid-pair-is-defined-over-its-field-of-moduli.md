---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli
statement: formalized
proof: formalized
---

# A rigid pair is defined over its field of moduli

Over a finite extension `k` of `ℚ`, an
algebraic Belyi pair with no nontrivial automorphisms is defined over its field of moduli.

```lean
TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli.{u} {k : Type u} [Field k]
  [CharZero k] {X : TauCeti.AlgebraicBelyiPair k} [Subsingleton Gal(↑X/RatFunc k)]
  [FiniteDimensional ℚ k] :
  TauCeti.AlgebraicBelyiPair.IsoClass.IsDefinedOver
    (↥(TauCeti.AlgebraicBelyiPair.IsoClass.mk X).fieldOfModuli)
    (TauCeti.AlgebraicBelyiPair.IsoClass.mk X)
```

## Depends on

- [TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli](tauceti-algebraicbelyipair-isoclass-fieldofmodul.md)

## Proof depends on

- [Artin's theorem](../galois/artins-theorem.md)
- [The Galois action on isomorphism classes](the-galois-action-on-isomorphism-classes.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Rigidity.html#TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Rigidity.html#TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli)
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.isDefinedOver_fieldOfModuli` in TauCeti/FieldTheory/FunctionField/Belyi/Rigidity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Belyi/Rigidity.lean#L137)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
