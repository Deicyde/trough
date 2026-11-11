---
declaration: theorem
origin: cited
lean: TauCeti.Place.isTotallyRamified_of_isEisensteinAt
statement: formalized
proof: formalized
---

# The Eisenstein criterion (Stichtenoth, Proposition 3.1.15)

if `F' = F(y)` and the
minimal polynomial of `y` over `F` is Eisenstein at the place of `F / k` below `P'`, then `P'`
is totally ramified over `F`. Together with
`TauCeti.Place.setOf_restrict_eq_eq_singleton_of_isTotallyRamified` this says that the place
below `P'` is totally ramified in `F' / F`: it has exactly one extension, of ramification index
`[F' : F]` and relative degree `1`.

```lean
TauCeti.Place.isTotallyRamified_of_isEisensteinAt.{u, u', v, v'} (k : Type u) {k' : Type u'}
  (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  {P' : TauCeti.Place k' F'} [FiniteDimensional F F'] {y : F'} (htop : F⟮y⟯ = ⊤)
  (hφ : (TauCeti.Place.restrict k F P').IsEisensteinAt (minpoly F y)) :
  TauCeti.Place.IsTotallyRamified F P'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.isTotallyRamified_of_isEisensteinAt`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Eisenstein.html#TauCeti.Place.isTotallyRamified_of_isEisensteinAt).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.isTotallyRamified_of_isEisensteinAt`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Eisenstein.html#TauCeti.Place.isTotallyRamified_of_isEisensteinAt)
- [Source of `TauCeti.Place.isTotallyRamified_of_isEisensteinAt` in TauCeti/FieldTheory/FunctionField/Place/Extension/Eisenstein.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Place/Extension/Eisenstein.lean#L413)
