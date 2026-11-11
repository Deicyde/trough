---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq
statement: formalized
proof: formalized
---

# Young's inequality for integral kernels

Let `1 ≤ p ≤ q` and let `r` be the exponent with
`1/p + 1/r = 1 + 1/q`. If the `r`-th powers of the kernel `k` have row integrals
`∫⁻ y, k x y ^ r ∂ν` at most `A` for almost every `x` and column integrals `∫⁻ x, k x y ^ r ∂μ`
at most `B` for almost every `y`, then the integral operator with kernel `k` satisfies
`∫⁻ x, (∫⁻ y, k x y * g y ∂ν) ^ q ∂μ ≤ A ^ (q (1 - 1/p)) * B * (∫⁻ y, g y ^ p ∂ν) ^ (q / p)`.

The kernel need only be a.e. measurable: the proof applies the measurable case to a measurable
modification of `k`, which agrees with `k` on almost every row and on almost every column.
For `p = q` this is Schur's test, `TauCeti.lintegral_rpow_lintegral_mul_le`.

```lean
TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  [MeasurableSpace α] [MeasurableSpace β] {μ : MeasureTheory.Measure α}
  {ν : MeasureTheory.Measure β} [MeasureTheory.SFinite μ] [MeasureTheory.SFinite ν]
  {k : α → β → ENNReal} (hk : AEMeasurable (Function.uncurry k) (μ.prod ν)) {g : β → ENNReal}
  (hg : AEMeasurable g ν) {p q r : ℝ} (hp : 1 ≤ p) (hpq : p ≤ q) (hr : p⁻¹ + r⁻¹ = 1 + q⁻¹)
  {A B : ENNReal} (hA : ∀ᵐ (x : α) ∂μ, ∫⁻ (y : β), k x y ^ r ∂ν ≤ A)
  (hB : ∀ᵐ (y : β) ∂ν, ∫⁻ (x : α), k x y ^ r ∂μ ≤ B) :
  ∫⁻ (x : α), (∫⁻ (y : β), k x y * g y ∂ν) ^ q ∂μ ≤
    A ^ (q * (1 - p⁻¹)) * B * (∫⁻ (y : β), g y ^ p ∂ν) ^ (q / p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for Young's exponents](../part-01/holders-inequality-for-youngs-exponents.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SchurTest.html#TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/SchurTest.html#TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq)
- [Source of `TauCeti.lintegral_rpow_lintegral_mul_le_of_inv_add_inv_eq` in TauCeti/MeasureTheory/Integral/SchurTest.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/SchurTest.lean#L131)
