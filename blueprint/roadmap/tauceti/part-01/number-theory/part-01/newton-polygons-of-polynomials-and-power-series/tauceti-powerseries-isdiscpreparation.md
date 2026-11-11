---
declaration: structure
origin: cited
lean: TauCeti.PowerSeries.IsDiscPreparation
statement: formalized
---

# TauCeti.PowerSeries.IsDiscPreparation

`f = P * U` is the **normalised preparation** of `f` on the closed disc of radius `r`: `f` is
distinguished of degree `d` at `r`, `P` is a polynomial of degree `d` with constant coefficient `1`,
and `U` is a series restricted at `r` with constant coefficient `1` and `‖U - 1‖_r < 1`.

Over a complete nonarchimedean field, a series with constant coefficient `1` which is restricted at
`r > 0` has exactly one such factorization in its distinguished degree
(`TauCeti.PowerSeries.IsDistinguished.existsUnique_isDiscPreparation`). The polynomial `P` carries
the zeros of `f` in the closed disc of radius `r`
(`TauCeti.PowerSeries.IsDiscPreparation.evalAt_eq_zero_iff`).

```lean
TauCeti.PowerSeries.IsDiscPreparation.{u_1} {K : Type u_1} [NormedField K] (r : ℝ) (d : ℕ)
  (f : PowerSeries K) (P : Polynomial K) (U : PowerSeries K) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDiscPreparation`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DiscPreparation.html#TauCeti.PowerSeries.IsDiscPreparation).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDiscPreparation`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DiscPreparation.html#TauCeti.PowerSeries.IsDiscPreparation)
- [Source of `TauCeti.PowerSeries.IsDiscPreparation` in TauCeti/RingTheory/PowerSeries/Weierstrass/DiscPreparation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/DiscPreparation.lean#L92)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NewtonPolygons/STATUS.md)
