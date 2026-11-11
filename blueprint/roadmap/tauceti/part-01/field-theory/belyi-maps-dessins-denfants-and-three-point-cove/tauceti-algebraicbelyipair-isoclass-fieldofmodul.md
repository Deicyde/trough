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
- [Source of `TauCeti.AlgebraicBelyiPair.IsoClass.fieldOfModuli` in TauCeti/FieldTheory/FunctionField/Belyi/FieldOfModuli.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Belyi/FieldOfModuli.lean#L89)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BelyiMaps/STATUS.md)
