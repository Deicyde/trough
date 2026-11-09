---
declaration: theorem
origin: cited
lean: AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one, BoundedVariationOn.jordanSign_naturalParameterization_eq_one_or_neg_one, AbsolutelyContinuousOnInterval.windingNumber_eq_jordanSign_of_mem_filledHull_sdiff, BoundedVariationOn.windingNumber_naturalParameterization_eq_jordanSign
statement: formalized
proof: formalized
---

# Jordan index theorem (orientation sign dichotomy)

for a simple closed absolutely
continuous curve on `[a, b]` (`a < b`), `jordanSign γ a b` is either `1` or `-1`, and equals the
winding number at every point of `filledHull (γ '' uIcc a b) \ (γ '' uIcc a b)`.

```lean
AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one {γ : ℝ → ℂ} {a b : ℝ} (hab : a < b)
  (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b)) :
  TauCeti.Contour.jordanSign γ a b = 1 ∨ TauCeti.Contour.jordanSign γ a b = -1
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Fundamental theorem for absolutely continuous curves, integrability](../../../measure-theory/function/fundamental-theorem-for-absolutely-continuous-cu.md)
- [The Jordan curve theorem](../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/the-jordan-curve-theorem.md)
- [The Jordan separation theorem](../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-01/the-jordan-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.html#AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one).

## Other forms

**Jordan index theorem for rectifiable simple closed curves (orientation sign dichotomy).** Formalized in Tau Ceti as [`BoundedVariationOn.jordanSign_naturalParameterization_eq_one_or_neg_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.html#BoundedVariationOn.jordanSign_naturalParameterization_eq_one_or_neg_one).

```lean
BoundedVariationOn.jordanSign_naturalParameterization_eq_one_or_neg_one {γ : ℝ → ℂ} {a b : ℝ}
  (hab : a < b) (hγ : BoundedVariationOn γ (Set.Icc a b)) (hcont : ContinuousOn γ (Set.Icc a b))
  (hclosed : γ a = γ b) (hinj : Set.InjOn γ (Set.Ico a b)) :
  TauCeti.Contour.jordanSign (naturalParameterization γ (Set.Icc a b) a) 0
        (eVariationOn γ (Set.Icc a b)).toReal =
      1 ∨
    TauCeti.Contour.jordanSign (naturalParameterization γ (Set.Icc a b) a) 0
        (eVariationOn γ (Set.Icc a b)).toReal =
      -1
```

**The Jordan index theorem for simple closed absolutely continuous curves.** Formalized in Tau Ceti as [`AbsolutelyContinuousOnInterval.windingNumber_eq_jordanSign_of_mem_filledHull_sdiff`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.html#AbsolutelyContinuousOnInterval.windingNumber_eq_jordanSign_of_mem_filledHull_sdiff).

```lean
AbsolutelyContinuousOnInterval.windingNumber_eq_jordanSign_of_mem_filledHull_sdiff {γ : ℝ → ℂ}
  {a b : ℝ} {z : ℂ} (hab : a < b) (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b))
  (hz : z ∈ TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b) :
  TauCeti.Contour.windingNumber γ a b z = ↑(TauCeti.Contour.jordanSign γ a b)
```

**The Jordan index theorem for the arclength parametrization of a rectifiable simple closed curve.** Formalized in Tau Ceti as [`BoundedVariationOn.windingNumber_naturalParameterization_eq_jordanSign`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.html#BoundedVariationOn.windingNumber_naturalParameterization_eq_jordanSign).

```lean
BoundedVariationOn.windingNumber_naturalParameterization_eq_jordanSign {γ : ℝ → ℂ} {a b : ℝ} {z : ℂ}
  (hab : a < b) (hγ : BoundedVariationOn γ (Set.Icc a b)) (hcont : ContinuousOn γ (Set.Icc a b))
  (hclosed : γ a = γ b) (hinj : Set.InjOn γ (Set.Ico a b))
  (hz : z ∈ TauCeti.filledHull (γ '' Set.Icc a b) \ γ '' Set.Icc a b) :
  TauCeti.Contour.windingNumber (naturalParameterization γ (Set.Icc a b) a) 0
      (eVariationOn γ (Set.Icc a b)).toReal z =
    ↑(TauCeti.Contour.jordanSign (naturalParameterization γ (Set.Icc a b) a) 0
        (eVariationOn γ (Set.Icc a b)).toReal)
```

## Sources

- [Tau Ceti documentation: `AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.html#AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one)
- [Source of `AbsolutelyContinuousOnInterval.jordanSign_eq_one_or_neg_one` in TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Winding/AbsolutelyContinuous/Jordan.lean#L380)
