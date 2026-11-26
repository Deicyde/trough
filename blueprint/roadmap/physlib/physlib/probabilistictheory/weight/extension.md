---
declaration: module
origin: cited
lean: Weight.IsFinite.toReal, Weight.IsFinite.toReal_apply, Weight.IsFinite.toLinearMap, Weight.IsFinite.toLinearMap_coe
statement: formalized
proof: formalized
---

# Extending finite weights (Physlib)

The module `Physlib.ProbabilisticTheory.Weight.Extension`, [Physlib/ProbabilisticTheory/Weight/Extension.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/Extension.lean): 4 declarations, 2 with a docstring.

> Finite weights extend to real-linear functionals on all observables.

## i. Overview

> Take the real value of a finite weight on positive observables, then use the common linear
> extension from the positive cone.

## ii. Key results

> - `Weight.IsFinite.toLinearMap` : extend a finite weight to all observables.

## iv. References

## A. Extending finite weights

**`Weight.IsFinite.toReal`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/Extension.lean#L45).

> A finite weight, read as a real-valued `ℝ≥0`-linear map on the positive cone.

```lean
noncomputable def IsFinite.toReal (hw : w.IsFinite) : PosCone P →ₗ[ℝ≥0] ℝ
```

**`Weight.IsFinite.toReal_apply`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/Extension.lean#L51).

```lean
lemma IsFinite.toReal_apply (hw : w.IsFinite) (A : PosCone P) : hw.toReal A = (w A).toReal
```

**`Weight.IsFinite.toLinearMap`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/Extension.lean#L54).

> The `ℝ`-linear map extending a finite weight.

```lean
noncomputable def IsFinite.toLinearMap (hw : w.IsFinite) : P.Observables →ₗ[ℝ] ℝ
```

**`Weight.IsFinite.toLinearMap_coe`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/Extension.lean#L58).

```lean
lemma IsFinite.toLinearMap_coe (hw : w.IsFinite) (A : PosCone P) :
    hw.toLinearMap (A : P.Observables) = (w A).toReal
```

## Depends on

- [Linear extension from positive observables](../orderunit/coneextension.md)
- [Weights (Physlib)](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Weight/Extension.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/Extension.lean)
