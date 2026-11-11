---
declaration: theorem
origin: cited
lean: TauCeti.sq_setAverage_norm_le_setAverage_norm_sq, ConvexOn.map_average_le_of_monotoneOn_Ici, TauCeti.rpow_laverage_le_laverage_rpow
statement: formalized
proof: formalized
---

# Jensen's inequality for the square of a mean

On a set `s` of finite nonzero measure, the
square of the mean of `‖g‖` is at most the mean of `‖g‖²`.

```lean
TauCeti.sq_setAverage_norm_le_setAverage_norm_sq.{u_1, u_2} {X : Type u_1} {F : Type u_2}
  [MeasurableSpace X] {μ : MeasureTheory.Measure X} [NormedAddCommGroup F] {g : X → F} {s : Set X}
  (hs0 : μ s ≠ 0) (hs : μ s ≠ ⊤) (hg : MeasureTheory.IntegrableOn g s μ)
  (hg2 : MeasureTheory.IntegrableOn (fun x => ‖g x‖ ^ 2) s μ) :
  (⨍ (x : X) in s, ‖g x‖ ∂μ) ^ 2 ≤ ⨍ (x : X) in s, ‖g x‖ ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../function/part-01/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_setAverage_norm_le_setAverage_norm_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.sq_setAverage_norm_le_setAverage_norm_sq).

## Other forms

**Jensen's inequality for a monotone function convex on a half-line.** Formalized in Tau Ceti as [`ConvexOn.map_average_le_of_monotoneOn_Ici`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#ConvexOn.map_average_le_of_monotoneOn_Ici).

```lean
ConvexOn.map_average_le_of_monotoneOn_Ici.{u_1} {α : Type u_1} [MeasurableSpace α]
  {μ : MeasureTheory.Measure α} [MeasureTheory.IsFiniteMeasure μ] [NeZero μ] {a : ℝ} {g : α → ℝ}
  {Φ : ℝ → ℝ} (hΦ : ConvexOn ℝ (Set.Ici a) Φ) (hΦm : MonotoneOn Φ (Set.Ici a))
  (hg : ∀ᵐ (x : α) ∂μ, a ≤ g x) (hgi : MeasureTheory.Integrable g μ)
  (hΦi : MeasureTheory.Integrable (fun x => Φ (g x)) μ) :
  Φ (⨍ (x : α), g x ∂μ) ≤ ⨍ (x : α), Φ (g x) ∂μ
```

**Jensen's inequality for the average of a nonnegative function.** Formalized in Tau Ceti as [`TauCeti.rpow_laverage_le_laverage_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.rpow_laverage_le_laverage_rpow).

```lean
TauCeti.rpow_laverage_le_laverage_rpow.{u_1} {X : Type u_1} [MeasurableSpace X]
  {μ : MeasureTheory.Measure X} {u : X → ENNReal} {r : ℝ} (hr : 1 ≤ r) :
  (⨍⁻ (x : X), u x ∂μ) ^ r ≤ ⨍⁻ (x : X), u x ^ r ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.sq_setAverage_norm_le_setAverage_norm_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.sq_setAverage_norm_le_setAverage_norm_sq)
- [Source of `TauCeti.sq_setAverage_norm_le_setAverage_norm_sq` in TauCeti/MeasureTheory/Integral/Average.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Average.lean#L435)
