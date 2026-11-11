---
declaration: theorem
origin: cited
lean: TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow
statement: formalized
proof: formalized
---

# The dyadic John–Nirenberg inequality for any additive Haar measure

the superlevel
set at `2ⁿ⁺¹ N M` has measure at most `2⁻ᴺ` times the cube measure.

```lean
TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow.{u_1, u_2} {ι : Type u_1} [Fintype ι]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] {f : (ι → ℝ) → E} {q₀ : ℤ × (ι → ℤ)}
  {M : NNReal} [CompleteSpace E] {μ : MeasureTheory.Measure (ι → ℝ)} [μ.IsAddHaarMeasure]
  (hf : MeasureTheory.IntegrableOn f (TauCeti.dyadicCube q₀.1 q₀.2) μ)
  (hM :
    ∀ (q : ℤ × (ι → ℤ)),
      TauCeti.dyadicCube q.1 q.2 ⊆ TauCeti.dyadicCube q₀.1 q₀.2 →
        ⨍⁻ (x : ι → ℝ) in TauCeti.dyadicCube q.1 q.2,
            ‖f x - ⨍ (y : ι → ℝ) in TauCeti.dyadicCube q.1 q.2, f y ∂μ‖ₑ ∂μ ≤
          ↑M)
  (N : ℕ) :
  μ
      {x |
        x ∈ TauCeti.dyadicCube q₀.1 q₀.2 ∧
          2 ^ (Fintype.card ι + 1) * ↑N * ↑M <
            ‖f x - ⨍ (y : ι → ℝ) in TauCeti.dyadicCube q₀.1 q₀.2, f y ∂μ‖ₑ} ≤
    2⁻¹ ^ N * μ (TauCeti.dyadicCube q₀.1 q₀.2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lebesgue's differentiation theorem along dyadic cubes](../../measure/lebesgues-differentiation-theorem-along-dyadic-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/JohnNirenberg.html#TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow)
- [Source of `TauCeti.measure_lt_enorm_sub_setAverage_le_inv_two_pow` in TauCeti/MeasureTheory/Integral/JohnNirenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/JohnNirenberg.lean#L439)
