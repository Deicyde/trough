---
declaration: theorem
origin: cited
lean: TauCeti.measure_exists_lt_norm_sub_le
statement: formalized
proof: formalized
---

# Entrywise Chebyshev union bound

For any measure `μ`, if every squared entrywise deviation
of a matrix-valued function `S` from a fixed matrix `A` is integrable with integral at most `v`,
then the measure of the event where some entry deviates by more than `η > 0` is at most
`ENNReal.ofReal (card m * card n * v / η²)`.

```lean
TauCeti.measure_exists_lt_norm_sub_le.{u_1, u_2, u_3, u_4} {Ω : Type u_1} {m : Type u_2}
  {n : Type u_3} {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [Fintype m] [Fintype n]
  {E : Type u_4} {S : Ω → Matrix m n E} {A : Matrix m n E} {v η : ℝ} [Norm E] [Sub E]
  (hint : ∀ (k : m) (l : n), MeasureTheory.Integrable (fun ω => ‖S ω k l - A k l‖ ^ 2) μ)
  (hmoment : ∀ (k : m) (l : n), ∫ (ω : Ω), ‖S ω k l - A k l‖ ^ 2 ∂μ ≤ v) (hη : 0 < η) :
  μ {ω | ∃ k l, η < ‖S ω k l - A k l‖} ≤
    ENNReal.ofReal (↑(Fintype.card m) * ↑(Fintype.card n) * v / η ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The uncentered Chebyshev inequality](the-uncentered-chebyshev-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_exists_lt_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/MatrixConcentration.html#TauCeti.measure_exists_lt_norm_sub_le).

## Sources

- [Tau Ceti documentation: `TauCeti.measure_exists_lt_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/MatrixConcentration.html#TauCeti.measure_exists_lt_norm_sub_le)
- [Source of `TauCeti.measure_exists_lt_norm_sub_le` in TauCeti/Probability/Moments/MatrixConcentration.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Moments/MatrixConcentration.lean#L82)
