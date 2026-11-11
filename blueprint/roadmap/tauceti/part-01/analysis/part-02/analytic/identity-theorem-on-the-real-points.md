---
declaration: theorem
origin: cited
lean: AnalyticAt.eventually_eq_zero_of_eventually_real
statement: formalized
proof: formalized
---

# Identity theorem on the real points

A complex analytic function of finitely many
variables that vanishes at the real points near a real point vanishes near that point.

```lean
AnalyticAt.eventually_eq_zero_of_eventually_real.{u_1, u_3} {ι : Type u_1} [Fintype ι]
  {E : Type u_3} [NormedAddCommGroup E] [NormedSpace ℂ E] {F : (ι → ℂ) → E} {a : ι → ℝ}
  (hF : AnalyticAt ℂ F fun i => ↑(a i)) (h : ∀ᶠ (x : ι → ℝ) in nhds a, (F fun i => ↑(x i)) = 0) :
  ∀ᶠ (z : ι → ℂ) in nhds fun i => ↑(a i), F z = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticAt.eventually_eq_zero_of_eventually_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Basic.html#AnalyticAt.eventually_eq_zero_of_eventually_real).

## Sources

- [Tau Ceti documentation: `AnalyticAt.eventually_eq_zero_of_eventually_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Basic.html#AnalyticAt.eventually_eq_zero_of_eventually_real)
- [Source of `AnalyticAt.eventually_eq_zero_of_eventually_real` in TauCeti/Analysis/Analytic/Complexification/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Analytic/Complexification/Basic.lean#L318)
