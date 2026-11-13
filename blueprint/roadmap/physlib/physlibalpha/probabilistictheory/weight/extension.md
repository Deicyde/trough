---
declaration: module
origin: cited
lean: ProbabilisticTheory.Weight.IsFinite.rawValue, ProbabilisticTheory.Weight.IsFinite.rawValue_of_le, ProbabilisticTheory.Weight.IsFinite.rawValue_indep, ProbabilisticTheory.Weight.IsFinite.toFun, ProbabilisticTheory.Weight.IsFinite.toFun_eq, ProbabilisticTheory.Weight.IsFinite.toFun_of_nonneg, ProbabilisticTheory.Weight.IsFinite.toFun_zero, ProbabilisticTheory.Weight.IsFinite.toFun_add
statement: formalized
proof: formalized
---

# Extending finite weights

The module `PhyslibAlpha.ProbabilisticTheory.Weight.Extension`, [PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean): 16 declarations, 15 with a docstring.

> A finite weight extends uniquely to a positive linear functional on the order unit space.

## i. Overview

> A finite weight on the positive cone of an order-unit space extends uniquely to a positive linear
> functional on the whole space. Since `1` is an order unit, any `A : E` becomes nonnegative after
> adding enough copies of `1`, so we set `toFun A := w (r • 1 + A) - r * w 1` for such an `r`, and
> check the result does not depend on the `r` chosen.

## ii. Key results

> - `Weight.IsFinite.toLinearMap` : the `ℝ`-linear map extending a finite weight to all of `E`.

## iv. References

> * None.

## A. The raw shifted value

**`ProbabilisticTheory.Weight.IsFinite.rawValue`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L59).

> `A` shifted into the cone by `r` copies of the order unit, minus the corresponding multiple
> of the weight of the order unit.

```lean
noncomputable def rawValue (w : Weight E) (A : E) (r : ℝ) (h : 0 ≤ r • (1 : E) + A) : ℝ
```

**`ProbabilisticTheory.Weight.IsFinite.rawValue_of_le`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L63).

> Shifting by a larger `s` gives the same value as shifting by `r`.

```lean
lemma rawValue_of_le (hw : w.IsFinite) (A : E) {r s : ℝ} (hr : 0 ≤ r • (1 : E) + A)
    (hs : 0 ≤ s • (1 : E) + A) (hrs : r ≤ s) : rawValue w A s hs = rawValue w A r hr
```

**`ProbabilisticTheory.Weight.IsFinite.rawValue_indep`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L78).

> The shifted value of a finite weight does not depend on the chosen shift.

```lean
lemma rawValue_indep (hw : w.IsFinite) (A : E) {r s : ℝ} (hr : 0 ≤ r • (1 : E) + A)
    (hs : 0 ≤ s • (1 : E) + A) : rawValue w A r hr = rawValue w A s hs
```

## B. The linear extension

**`ProbabilisticTheory.Weight.IsFinite.toFun`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L90).

> The linear extension of a finite weight from the positive cone to all of `E`.

```lean
noncomputable def toFun (w : Weight E) (A : E) : ℝ
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_eq`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L95).

> The extension can be computed with any shift `r` making `r • 1 + A` nonnegative.

```lean
lemma toFun_eq (hw : w.IsFinite) (A : E) {r : ℝ} (h : 0 ≤ r • (1 : E) + A) :
    toFun w A = rawValue w A r h
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_of_nonneg`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L100).

```lean
lemma toFun_of_nonneg (hw : w.IsFinite) (A : PosCone E) : toFun w (A : E) = (w A).toReal
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_zero`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L107).

> The extension of a finite weight sends `0` to `0`.

```lean
lemma toFun_zero (hw : w.IsFinite) : toFun w (0 : E) = 0
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_add`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L111).

> The extension of a finite weight is additive.

```lean
lemma toFun_add (hw : w.IsFinite) (A B : E) : toFun w (A + B) = toFun w A + toFun w B
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_neg`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L127).

> The extension of a finite weight is odd.

```lean
lemma toFun_neg (hw : w.IsFinite) (A : E) : toFun w (-A) = -toFun w A
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_real_nonneg_smul`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L133).

> Nonnegative real homogeneity of the finite-weight extension.

```lean
lemma toFun_real_nonneg_smul (hw : w.IsFinite) {t : ℝ} (ht : 0 ≤ t) (A : E) :
    toFun w (t • A) = t * toFun w A
```

**`ProbabilisticTheory.Weight.IsFinite.toFun_smul`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L150).

> Full real homogeneity of the finite-weight extension.

```lean
lemma toFun_smul (hw : w.IsFinite) (t : ℝ) (A : E) : toFun w (t • A) = t * toFun w A
```

**`ProbabilisticTheory.Weight.IsFinite.toLinearMap`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L157).

> The `ℝ`-linear map extending a finite weight.

```lean
noncomputable def toLinearMap (hw : w.IsFinite) : E →ₗ[ℝ] ℝ
```

**`ProbabilisticTheory.Weight.IsFinite.toLinearMap_apply`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L164).

> The linear extension agrees with `toFun` by construction.

```lean
lemma toLinearMap_apply (hw : w.IsFinite) (A : E) : toLinearMap hw A = toFun w A
```

**`ProbabilisticTheory.Weight.IsFinite.toPositiveLinearMap`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L167).

> The positive linear extension of a finite weight.

```lean
noncomputable def toPositiveLinearMap (hw : w.IsFinite) : E →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.Weight.IsFinite.toPositiveLinearMap_apply`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L174).

> The positive extension agrees with the underlying finite-weight extension.

```lean
lemma toPositiveLinearMap_apply (hw : w.IsFinite) (A : E) :
    hw.toPositiveLinearMap A = toFun w A
```

**`ProbabilisticTheory.Weight.IsFinite.toPositiveLinearMap_apply_of_nonneg`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean#L178).

> On positive elements, the positive extension is the real value of the weight.

```lean
lemma toPositiveLinearMap_apply_of_nonneg (hw : w.IsFinite) (A : PosCone E) :
    hw.toPositiveLinearMap (A : E) = (w A).toReal
```

## Depends on

- [Weights](basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Weight/Extension.lean)
