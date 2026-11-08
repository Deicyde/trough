---
declaration: theorem
origin: cited
lean: TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain
statement: formalized
proof: formalized
---

# The sharp Poincaré inequality on an interval

For every `u ∈ H¹₀(a, b)`,

`(π / (b - a))² ∫_a^b u² ≤ ∫_a^b |u'|²`,

and `(π / (b - a))²` is the largest constant for which this holds: it is the first Dirichlet
eigenvalue (`TauCeti.PDE.firstDirichletEigenvalue_laplacian_intervalDomain`).

```lean
TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain {a b : ℝ} (hab : a < b) :
  IsGreatest
    {C |
      ∀ (u : ↥(TauCeti.W1p0 MeasureTheory.volume (TauCeti.PDE.intervalDomain a b) 2)),
        C * ‖TauCeti.W1p.value ↑u‖ ^ 2 ≤ TauCeti.PDE.energyFormH1 (fun x => 1) 0 0 ↑u ↑u}
    ((Real.pi / (b - a)) ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set, the form that Rellich--Kondrachov for `W^{1,p}_0(Ω)` consumes](../../../../measure-theory/function/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [Green's first identity against `H¹₀(Ω)`](../part-01/greens-first-identity-against-h10.md)
- [Gårding's inequality on `H¹(Ω)`](../part-01/gardings-inequality-on-h1.md)
- [Hölder's inequality for Young's exponents](../../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The Poincaré inequality on a ball](../../sobolev/part-01/the-poincare-inequality-on-a-ball.md)
- [The Rayleigh lower bound](../../inner-product-space/part-02/the-rayleigh-lower-bound.md)
- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Interval.html#TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Spectrum/Interval.html#TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain)
- [Source of `TauCeti.PDE.isGreatest_mul_norm_value_sq_le_energyFormH1_intervalDomain` in TauCeti/Analysis/PDE/Spectrum/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Spectrum/Interval.lean#L368)
