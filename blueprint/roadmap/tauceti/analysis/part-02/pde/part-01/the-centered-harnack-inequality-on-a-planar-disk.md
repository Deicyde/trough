---
declaration: theorem
origin: cited
lean: InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere, InnerProductSpace.HarmonicOnNhd.harnack_inequality_center
statement: formalized
proof: formalized
---

# The centered Harnack inequality on a planar disk

If `f` is harmonic on the open disk of radius `R` about `c`, continuous on its closure and
nonnegative on its boundary circle, then every `w` in the open disk satisfies

`(R - ‖w - c‖) / (R + ‖w - c‖) * f c ≤ f w
  ≤ (R + ‖w - c‖) / (R - ‖w - c‖) * f c`.

```lean
InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere {f : ℂ → ℝ}
  {c w : ℂ} {R : ℝ} (hf : InnerProductSpace.HarmonicContOnCl f (Metric.ball c R))
  (hnonneg : ∀ z ∈ Metric.sphere c R, 0 ≤ f z) (hw : w ∈ Metric.ball c R) :
  (R - ‖w - c‖) / (R + ‖w - c‖) * f c ≤ f w ∧ f w ≤ (R + ‖w - c‖) / (R - ‖w - c‖) * f c
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Planar.html#InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere).

## Other forms

**The centered Harnack inequality on an open planar disk.** Formalized in Tau Ceti as [`InnerProductSpace.HarmonicOnNhd.harnack_inequality_center`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Planar.html#InnerProductSpace.HarmonicOnNhd.harnack_inequality_center).

```lean
InnerProductSpace.HarmonicOnNhd.harnack_inequality_center {f : ℂ → ℝ} {c w : ℂ} {R : ℝ}
  (hf : InnerProductSpace.HarmonicOnNhd f (Metric.ball c R))
  (hnonneg : ∀ z ∈ Metric.ball c R, 0 ≤ f z) (hw : w ∈ Metric.ball c R) :
  (R - ‖w - c‖) / (R + ‖w - c‖) * f c ≤ f w ∧ f w ≤ (R + ‖w - c‖) / (R - ‖w - c‖) * f c
```

## Sources

- [Tau Ceti documentation: `InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Planar.html#InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere)
- [Source of `InnerProductSpace.HarmonicContOnCl.harnack_inequality_center_of_nonneg_on_sphere` in TauCeti/Analysis/PDE/Harnack/Planar.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Harnack/Planar.lean#L59)
