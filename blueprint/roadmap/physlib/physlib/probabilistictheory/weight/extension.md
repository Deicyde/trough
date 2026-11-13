---
declaration: module
origin: cited
lean: PosCone.coe_nnreal_smul, PosCone.map_sub_eq_map_sub, PosCone.exists_sub, PosCone.extendFun, PosCone.extendFun_eq, PosCone.extend, PosCone.extend_apply, PosCone.extend_coe
statement: formalized
proof: formalized
---

# Extending finite weights

The module `Physlib.ProbabilisticTheory.Weight.Extension`, [Physlib/ProbabilisticTheory/Weight/Extension.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean): 12 declarations, 6 with a docstring.

## i. Overview

> An `ℝ≥0`-linear map on the positive cone extends uniquely to an `ℝ`-linear map on the whole space
> as soon as every element is a difference `P - Q` of positive elements: send `P - Q` to
> `f P - f Q`. In an order-unit space every element is such a difference, so a finite weight extends
> to a positive linear functional.

## ii. Key results

> - `PosCone.extend` : the `ℝ`-linear extension of an `ℝ≥0`-linear map on the positive cone.
> - `Weight.IsFinite.toLinearMap` : the `ℝ`-linear map extending a finite weight to all of `E`.

## iv. References

## A. Extension from the positive cone

**`PosCone.coe_nnreal_smul`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L51).

```lean
lemma coe_nnreal_smul (t : ℝ≥0) (P : PosCone E) : ((t • P : PosCone E) : E) = (t : ℝ) • (P : E)
```

**`PosCone.map_sub_eq_map_sub`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L55).

> `P - Q ↦ f P - f Q` does not depend on how an element is written as a difference.

```lean
lemma map_sub_eq_map_sub {P Q P' Q' : PosCone E} (h : (P : E) - Q = P' - Q') :
    f P - f Q = f P' - f Q'
```

**`PosCone.exists_sub`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L62).

> In an order unit space, every element is a difference of positive elements.

```lean
lemma exists_sub (A : E) : ∃ P Q : PosCone E, (P : E) - Q = A
```

**`PosCone.extendFun`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L67).

> The value of the extension, computed from a chosen decomposition `A = P - Q`.

```lean
noncomputable def extendFun (A : E) : ℝ
```

**`PosCone.extendFun_eq`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L70).

```lean
lemma extendFun_eq {A : E} {P Q : PosCone E} (h : (P : E) - Q = A) :
    extendFun f A = f P - f Q
```

**`PosCone.extend`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L75).

> The `ℝ`-linear extension of an `ℝ≥0`-linear map on an order unit space's positive cone.

```lean
noncomputable def extend : E →ₗ[ℝ] ℝ
```

**`PosCone.extend_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L97).

```lean
lemma extend_apply {P Q : PosCone E} : extend f ((P : E) - Q) = f P - f Q
```

**`PosCone.extend_coe`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L101).

```lean
lemma extend_coe (P : PosCone E) : extend f (P : E) = f P
```

## B. Extending finite weights

**`Weight.IsFinite.toReal`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L119).

> A finite weight, read as a real-valued `ℝ≥0`-linear map on the positive cone.

```lean
noncomputable def IsFinite.toReal (hw : w.IsFinite) : PosCone E →ₗ[ℝ≥0] ℝ
```

**`Weight.IsFinite.toReal_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L125).

```lean
lemma IsFinite.toReal_apply (hw : w.IsFinite) (A : PosCone E) : hw.toReal A = (w A).toReal
```

**`Weight.IsFinite.toLinearMap`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L134).

> The `ℝ`-linear map extending a finite weight.

```lean
noncomputable def IsFinite.toLinearMap (hw : w.IsFinite) : E →ₗ[ℝ] ℝ
```

**`Weight.IsFinite.toLinearMap_coe`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean#L138).

```lean
lemma IsFinite.toLinearMap_coe (hw : w.IsFinite) (A : PosCone E) :
    hw.toLinearMap (A : E) = (w A).toReal
```

## Depends on

- [Weights](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Weight/Extension.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Weight/Extension.lean)
