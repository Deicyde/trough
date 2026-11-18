---
declaration: module
origin: cited
lean: Space.normRegularizedPow, Space.normRegularizedPow_eq, Space.norm_sq_add_unit_sq_pos, Space.normRegularizedPow_pos, Space.normRegularizedPow_hasTemperateGrowth, Space.normRegularizedPow_measurable
statement: formalized
proof: formalized
---

# Regularized powers of the norm on space

The module `Physlib.SpaceAndTime.Space.Norm.Regularized`, [Physlib/SpaceAndTime/Space/Norm/Regularized.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean): 6 declarations, 4 with a docstring.

## i. Overview

> This file contains basic API for regularized powers of the norm on `Space d`, namely
> `x ↦ (‖x‖ ^ 2 + ε ^ 2) ^ (s / 2)`.

## ii. Key results

> - `normRegularizedPow` : The regularized norm power `x ↦ (‖x‖ ^ 2 + ε ^ 2) ^ (s / 2)`.
> - `normRegularizedPow_pos` : Positivity for nonzero regularization parameter.
> - `normRegularizedPow_hasTemperateGrowth` : Temperate growth of regularized norm powers.
> - `normRegularizedPow_measurable` : Measurability of regularized norm powers.

## iv. References

> * None.

## A. Regularized powers of the norm

**`Space.normRegularizedPow`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean#L49).

> Power of regularized norm, `(‖x‖² + ε²)^(s/2)`.

```lean
def normRegularizedPow (d : ℕ) (ε s : ℝ) : Space d → ℝ
```

**`Space.normRegularizedPow_eq`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean#L52).

```lean
lemma normRegularizedPow_eq (d : ℕ) (ε s : ℝ) :
    normRegularizedPow d ε s = fun x ↦ (‖x‖ ^ 2 + ε ^ 2) ^ (s / 2)
```

**`Space.norm_sq_add_unit_sq_pos`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean#L56).

> For a nonzero regularization parameter, `‖x‖² + ε²` is positive.

```lean
lemma norm_sq_add_unit_sq_pos {d : ℕ} (ε : ℝˣ) (x : Space d) : 0 < ‖x‖ ^ 2 + ε ^ 2
```

**`Space.normRegularizedPow_pos`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean#L60).

> The regularized norm power is positive for nonzero regularization parameter.

```lean
lemma normRegularizedPow_pos (d : ℕ) (ε : ℝˣ) (s : ℝ) (x : Space d) :
    0 < normRegularizedPow d ε s x
```

**`Space.normRegularizedPow_hasTemperateGrowth`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean#L65).

> The regularized norm power has temperate growth.

```lean
lemma normRegularizedPow_hasTemperateGrowth (d : ℕ) (ε : ℝˣ) (s : ℝ) :
    HasTemperateGrowth (normRegularizedPow d ε s)
```

**`Space.normRegularizedPow_measurable`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean#L79).

```lean
lemma normRegularizedPow_measurable (d : ℕ) (ε s : ℝ) :
    Measurable (normRegularizedPow d ε s)
```

## Depends on

- [The structure of a module on Space](../part-01/module.md)

## Sources

- [Physlib/SpaceAndTime/Space/Norm/Regularized.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Regularized.lean)
