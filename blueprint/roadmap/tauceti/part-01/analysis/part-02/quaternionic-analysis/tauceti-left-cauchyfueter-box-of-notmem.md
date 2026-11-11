---
declaration: theorem
origin: cited
lean: TauCeti.left_cauchyFueter_box_of_notMem
statement: formalized
proof: formalized
---

# TauCeti.left_cauchyFueter_box_of_notMem

The left Cauchy–Fueter box boundary sum vanishes when the pole is outside the
closed box. The coefficients retain the order `G * eᵢ * f`.

```lean
TauCeti.left_cauchyFueter_box_of_notMem {a b : Fin 4 → ℝ} (hab : a ≤ b)
  {f : Quaternion ℝ → Quaternion ℝ} {q₀ : Quaternion ℝ}
  (hq₀ : q₀ ∉ ⇑TauCeti.Quaternion.dq '' Set.Icc a b)
  (hc : ContinuousOn f (⇑TauCeti.Quaternion.dq '' Set.Icc a b))
  (hf :
    TauCeti.LeftFueterOn f (⇑TauCeti.Quaternion.dq '' Set.univ.pi fun i => Set.Ioo (a i) (b i))) :
  (TauCeti.boxBoundarySum a b fun i x =>
      TauCeti.cauchyFueterKernel (TauCeti.Quaternion.dq x) q₀ *
          TauCeti.Quaternion.dq (Pi.single i 1) *
        f (TauCeti.Quaternion.dq x)) =
    0
```

## Depends on

- [TauCeti.LeftFueterAt](tauceti-leftfueterat.md)

## Proof depends on

- [TauCeti.cauchy_box](tauceti-cauchy-box.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.left_cauchyFueter_box_of_notMem`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cauchy/Exterior.html#TauCeti.left_cauchyFueter_box_of_notMem).

## Sources

- [Tau Ceti documentation: `TauCeti.left_cauchyFueter_box_of_notMem`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cauchy/Exterior.html#TauCeti.left_cauchyFueter_box_of_notMem)
- [Source of `TauCeti.left_cauchyFueter_box_of_notMem` in TauCeti/Analysis/Quaternion/Cauchy/Exterior.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/Cauchy/Exterior.lean#L42)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)
