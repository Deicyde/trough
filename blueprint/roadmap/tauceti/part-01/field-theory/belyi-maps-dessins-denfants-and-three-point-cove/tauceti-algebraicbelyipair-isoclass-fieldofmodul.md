---
declaration: def
origin: cited
lean: TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli
statement: formalized
---

# TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli

The **field of moduli** of an isomorphism class `c` of algebraic Belyi pairs over `k`: the
subfield of `k` fixed by every automorphism of `k` that fixes `c`. At `k = ℂ` it is Köck's
relative moduli field `M(X, t)` of a representative `(X, t)`; at `k = AlgebraicClosure ℚ` it is
the field of moduli of the Belyi map.

```lean
TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli.{u} {k : Type u} [Field k] [CharZero k]
  (c : TauCeti.AlgebraicBelyiPair.IsoClass k) : IntermediateField ℚ k
```

## Depends on

- [The Galois action on isomorphism classes](the-galois-action-on-isomorphism-classes.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/FieldOfModuli.html#TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/FieldOfModuli.html#TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli)
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli` in TauCeti/FieldTheory/FunctionField/Belyi/FieldOfModuli.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/Belyi/FieldOfModuli.lean#L89)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BelyiMaps/STATUS.md)
