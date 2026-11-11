---
declaration: def
origin: cited
lean: TauCeti.MvPowerSeries.restrictedAnalyticSubst
statement: formalized
---

# Analytic substitution

For series `gᵢ ∈ R{Y/s}` with `‖gᵢ‖ ≤ rᵢ`, the `R`-algebra
homomorphism `R{X/r} → R{Y/s}` sending `f = ∑ₜ fₜ Xᵗ` to the convergent sum `∑ₜ fₜ gᵗ`. The `gᵢ`
may have nonzero constant terms.

```lean
TauCeti.MvPowerSeries.restrictedAnalyticSubst.{u_1, u_2} {k : ℕ} {τ : Type u_1} {R : Type u_2}
  [NormedCommRing R] [IsUltrametricDist R] [CompleteSpace R] {r : Fin k → ℝ} {s : τ → ℝ}
  [∀ (j : τ), Fact (0 < s j)] (g : Fin k → ↥(MvPowerSeries.IsRestricted.subring s))
  (hg : ∀ (i : Fin k), ‖g i‖ ≤ r i) :
  ↥(MvPowerSeries.IsRestricted.subring r) →ₐ[R] ↥(MvPowerSeries.IsRestricted.subring s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.restrictedAnalyticSubst`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/AnalyticSubst.html#TauCeti.MvPowerSeries.restrictedAnalyticSubst).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.restrictedAnalyticSubst`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/AnalyticSubst.html#TauCeti.MvPowerSeries.restrictedAnalyticSubst)
- [Source of `TauCeti.MvPowerSeries.restrictedAnalyticSubst` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/AnalyticSubst.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/AnalyticSubst.lean#L83)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
