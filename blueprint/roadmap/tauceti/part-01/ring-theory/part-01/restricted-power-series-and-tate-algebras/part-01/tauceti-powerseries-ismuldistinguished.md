---
declaration: structure
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished
statement: formalized
---

# TauCeti.PowerSeries.IsMulDistinguished

`g` is **multiplicatively distinguished of degree `s`** at the radius `c` when it is
distinguished of degree `s` at `c` and its coefficient in degree `s` is a multiplicative unit.

The first condition says that the Gauss norm of `g` at `c` is attained in degree `s` and that
every later weighted coefficient norm is strictly smaller; earlier coefficients may tie. The
second makes left multiplication by `g` lose no norm, without any multiplicativity assumption on
the norm of the coefficient ring.

```lean
TauCeti.PowerSeries.IsMulDistinguished.{u_1} {R : Type u_1} [SeminormedRing R] (c : ℝ) (s : ℕ)
  (g : PowerSeries R) : Prop
```

## Depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MulDistinguished.html#TauCeti.PowerSeries.IsMulDistinguished).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/MulDistinguished.html#TauCeti.PowerSeries.IsMulDistinguished)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished` in TauCeti/RingTheory/PowerSeries/MulDistinguished.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/MulDistinguished.lean#L99)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
