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
- [Source of `TauCeti.MvPowerSeries.restrictedAnalyticSubst` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/AnalyticSubst.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/AnalyticSubst.lean#L83)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
