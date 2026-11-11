---
declaration: theorem
origin: cited
lean: TauCeti.integral_inner_sub_integral_le
statement: formalized
proof: formalized
---

# The quadratic Fenchel–Young inequality in mean

Let `X` and `Y` be square-integrable
random vectors, where the law of `X` has covariance matrix `A * T * A` for a positive-semidefinite
matrix `A`. Then the correlation of the centred variable `X - 𝔼 X` with `Y` is at most
`(𝔼 ⟪A Y, Y⟫ + tr (A * T)) / 2`.

```lean
TauCeti.integral_inner_sub_integral_le.{u_1, u_2} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {Ω : Type u_2} [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure P] {X Y : Ω → EuclideanSpace ℝ ι}
  (hX : MeasureTheory.MemLp X 2 P) (hY : MeasureTheory.MemLp Y 2 P) {A T : Matrix ι ι ℝ}
  (hA : A.PosSemidef) (hcov : TauCeti.covMatrix (MeasureTheory.Measure.map X P) = A * T * A) :
  ∫ (ω : Ω), inner ℝ (X ω - ∫ (ω' : Ω), X ω' ∂P) (Y ω) ∂P ≤
    (∫ (ω : Ω), inner ℝ ((Matrix.toEuclideanLin A) (Y ω)) (Y ω) ∂P + (A * T).trace) / 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_inner_sub_integral_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/FenchelYoung.html#TauCeti.integral_inner_sub_integral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_inner_sub_integral_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/FenchelYoung.html#TauCeti.integral_inner_sub_integral_le)
- [Source of `TauCeti.integral_inner_sub_integral_le` in TauCeti/Probability/Moments/FenchelYoung.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Moments/FenchelYoung.lean#L80)
