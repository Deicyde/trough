---
declaration: def
origin: cited
lean: TauCeti.MvPowerSeries.IsRestrictedFamily
statement: formalized
---

# TauCeti.MvPowerSeries.IsRestrictedFamily

A family of coefficients `a : (σ →₀ ℕ) → E` in a seminormed group is restricted at the
polyradius `c` if `‖a t‖ * ∏ i ∈ t.support, c i ^ t i → 0` along the cofinite filter. These are
the coefficient families of restricted power series with coefficients in `E`.

```lean
TauCeti.MvPowerSeries.IsRestrictedFamily.{u_1, u_3} {σ : Type u_1} {E : Type u_3}
  [SeminormedAddCommGroup E] (c : σ → ℝ) (a : (σ →₀ ℕ) → E) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.IsRestrictedFamily`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Basic.html#TauCeti.MvPowerSeries.IsRestrictedFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.IsRestrictedFamily`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Basic.html#TauCeti.MvPowerSeries.IsRestrictedFamily)
- [Source of `TauCeti.MvPowerSeries.IsRestrictedFamily` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Basic.lean#L80)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
