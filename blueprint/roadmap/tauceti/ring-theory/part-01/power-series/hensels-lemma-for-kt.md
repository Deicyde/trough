---
declaration: theorem
origin: cited
lean: PowerSeries.henselianLocalRing
statement: formalized
proof: formalized
---

# Hensel's lemma for `K⟦t⟧`

Over a field `K`, the power series ring `K⟦t⟧` is a Henselian
local ring. If `a₀` is a root modulo `t` of a monic polynomial `f` with `f' (a₀)` a unit, its
constant coefficient `c` is a simple root of the reduction of `f`, which therefore factors as
`(X - c) * h` with `X - c` coprime to `h`; lifting this factorization
(`Polynomial.Monic.exists_monic_mul_eq_of_isCoprime`) gives a linear factor `X - a` of `f` with
`a ≡ a₀ mod t`.

```lean
PowerSeries.henselianLocalRing.{u_1} {K : Type u_1} [Field K] : HenselianLocalRing (PowerSeries K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Hensel.html#PowerSeries.henselianLocalRing).

## Sources

- [Tau Ceti documentation: `PowerSeries.henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Hensel.html#PowerSeries.henselianLocalRing)
- [Source of `PowerSeries.henselianLocalRing` in TauCeti/RingTheory/PowerSeries/Hensel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Hensel.lean#L304)
