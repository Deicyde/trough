---
declaration: theorem
origin: cited
lean: AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction
statement: formalized
proof: formalized
---

# Hölder estimate along a curve

if `γ` is absolutely continuous on `[a, b]` and `1 ≤ p`,
then `edist (γ s) (γ u) ^ p ≤ edist s u ^ (p - 1) * curveAction p γ s u` for all `s, u ∈ [a, b]`.
In particular a curve of finite `p`-action with `1 < p` is `(1 - 1 / p)`-Hölder continuous.

```lean
AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {p : ℝ} {γ : ℝ → X} {a b : ℝ} (hγ : AbsolutelyContinuousOnInterval γ a b)
  (hp : 1 ≤ p) {s u : ℝ} (hs : s ∈ Set.uIcc a b) (hu : u ∈ Set.uIcc a b) :
  edist (γ s) (γ u) ^ p ≤ edist s u ^ (p - 1) * TauCeti.curveAction p γ s u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fundamental theorem for absolutely continuous curves, integrability](fundamental-theorem-for-absolutely-continuous-cu.md)
- [Hölder's inequality for the integral of a product](holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/CurveAction/Basic.html#AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction).

## Sources

- [Tau Ceti documentation: `AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/CurveAction/Basic.html#AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction)
- [Source of `AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction` in TauCeti/MeasureTheory/Function/CurveAction/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/CurveAction/Basic.lean#L214)
