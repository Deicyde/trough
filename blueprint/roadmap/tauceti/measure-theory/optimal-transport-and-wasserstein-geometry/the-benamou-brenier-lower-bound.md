---
declaration: theorem
origin: cited
lean: TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le
statement: formalized
proof: formalized
---

# The Benamou–Brenier lower bound

Let `t ↦ νₜ` be a curve of finite measures, narrowly
continuous on `[a, b]` with `a ≤ b`, solving the continuity equation with velocity `v` on
`(a, b)`, whose initial law `ν_a` is a probability measure (by conservation of mass, so is `ν_b`).
Then for `1 ≤ p < ∞` the `p`-Wasserstein distance between the endpoint laws is controlled by the
`p`-action of `v`: `W_p (ν_a, ν_b) ^ p ≤ (b - a) ^ (p - 1) * ∫_a^b ∫ ‖vₜ‖ ^ p dνₜ dt`.

On `[0, 1]` the factor is `1`, and this is the inequality `W_p (ν₀, ν₁) ^ p ≤ ∫₀¹ ∫ ‖vₜ‖ ^ p dνₜ dt`
of the Benamou–Brenier formula.

```lean
TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [FiniteDimensional ℝ E] [BorelSpace E]
  {ν : ℝ → MeasureTheory.FiniteMeasure E} {v : ℝ → E → E} {a b : ℝ}
  (h : TauCeti.IsContinuityEquation (fun t => ↑(ν t)) v a b) (hν : ContinuousOn ν (Set.Icc a b))
  (hab : a ≤ b) [MeasureTheory.IsProbabilityMeasure ↑(ν a)] {p : ENNReal} (hp : 1 ≤ p)
  (hp_top : p ≠ ⊤) :
  TauCeti.wassersteinEDist p ↑(ν a) ↑(ν b) ^ p.toReal ≤
    ENNReal.ofReal ((b - a) ^ (p.toReal - 1)) *
      ∫⁻ (t : ℝ) in Set.Ioo a b, ∫⁻ (x : E), ‖v t x‖ₑ ^ p.toReal ∂↑(ν t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](../../analysis/part-02/sobolev/part-01/the-fundamental-theorem-of-calculus-for-a-contin.md)
- [The Hopf–Lax subsolution inequality](../../analysis/part-02/pde/part-01/the-hopf-lax-subsolution-inequality.md)
- [The theorem of Rockafellar and Rüschendorf](../optimal-transport/part-02/the-theorem-of-rockafellar-and-ruschendorf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le)
- [Source of `TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le` in TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.lean#L175)
