---
declaration: structure
origin: cited
lean: TauCeti.IsAlgebraicBelyiPair
statement: formalized
---

# TauCeti.IsAlgebraicBelyiPair

An **algebraic Belyi pair** over a field `k` of characteristic zero: a function field `F / k`
with exact constant field `k`, finite over the rational function field `k(t)` through the given
`Algebra (RatFunc k) F` structure, in which every place lying over a place of `k(t)` other than
`t = 0`, `t = 1` and `t = ∞` has ramification index `1`.

The branch locus is only required to be contained in the three marked places. The base field is
pinned to characteristic zero, where `F / k(t)` is automatically separable; in characteristic `p`
the power map `t ↦ t ^ p` is inseparable and `4t(1 - t)` is constant in characteristic `2`.

```lean
TauCeti.IsAlgebraicBelyiPair.{u_1, u_2} (k : Type u_1) (F : Type u_2) [Field k] [CharZero k]
  [Field F] [Algebra k F] [Algebra (RatFunc k) F] [IsScalarTower k (RatFunc k) F]
  [FiniteDimensional (RatFunc k) F] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAlgebraicBelyiPair`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Basic.html#TauCeti.IsAlgebraicBelyiPair).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAlgebraicBelyiPair`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Belyi/Basic.html#TauCeti.IsAlgebraicBelyiPair)
- [Source of `TauCeti.IsAlgebraicBelyiPair` in TauCeti/FieldTheory/FunctionField/Belyi/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Belyi/Basic.lean#L176)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
