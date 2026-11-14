---
declaration: module
origin: cited
lean: PoincareGroup.contDiff_smul, PoincareGroup.contDiff_act, PoincareGroup.actSmooth, PoincareGroup.actSmooth_coe, PoincareGroup.tsupport_actSmooth, PoincareGroup.actSmooth_one, PoincareGroup.actSmooth_mul, PoincareGroup.hasCompactSupport_act
statement: formalized
proof: formalized
---

# The Poincaré action on smooth fields

The module `PhyslibAlpha.Relativity.Poincare.Fields`, [PhyslibAlpha/Relativity/Poincare/Fields.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean): 11 declarations, 11 with a docstring.

> The Poincaré group acts on smooth fields and on compactly supported smooth fields.

## i. Overview

> The action `(g • u) x = u (g⁻¹ x)` sends smooth functions to smooth functions. It is linear and
> it sends the support to the image of the support. So it preserves compact support. The file
> restricts the action to the submodule of smooth fields and to the submodule of test fields.

## ii. Key results

> - `PoincareGroup.actSmooth` : the action as a linear map on smooth fields.
> - `PoincareGroup.actTest` : the action as a linear map on test fields.
> - `PoincareGroup.tsupport_actSmooth` : the support of a transformed field.

## iv. References

> None.

## A. Smooth fields

> - `PoincareGroup.actSmooth` : the action as a linear map on smooth fields.

## B. Test fields

> - `PoincareGroup.actTest` : the action as a linear map on test fields.

**`PoincareGroup.contDiff_smul`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L61).

> The action on points is smooth.

```lean
lemma contDiff_smul (g : PoincareGroup d) : ContDiff ℝ ∞ fun x : SpaceTime d => g • x
```

**`PoincareGroup.contDiff_act`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L66).

> The action preserves smooth functions.

```lean
lemma contDiff_act (g : PoincareGroup d) {u : SpaceTime d → V} (hu : ContDiff ℝ ∞ u) :
    ContDiff ℝ ∞ (act g u)
```

**`PoincareGroup.actSmooth`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L71).

> The action as a linear map on smooth fields.

```lean
def actSmooth (g : PoincareGroup d) : smoothFields d V →ₗ[ℝ] smoothFields d V
```

**`PoincareGroup.actSmooth_coe`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L78).

> The value of a transformed smooth field.

```lean
lemma actSmooth_coe (g : PoincareGroup d) (u : smoothFields d V) :
    (actSmooth g u : SpaceTime d → V) = act g u.1
```

**`PoincareGroup.tsupport_actSmooth`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L82).

> The support of a transformed smooth field is the image of the support.

```lean
lemma tsupport_actSmooth (g : PoincareGroup d) (u : smoothFields d V) :
    tsupport (actSmooth g u : SpaceTime d → V) = g • tsupport (u : SpaceTime d → V)
```

**`PoincareGroup.actSmooth_one`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L87).

> The identity acts trivially on smooth fields.

```lean
lemma actSmooth_one (u : smoothFields d V) : actSmooth (1 : PoincareGroup d) u = u
```

**`PoincareGroup.actSmooth_mul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L91).

> The action on smooth fields is a left action.

```lean
lemma actSmooth_mul (g h : PoincareGroup d) (u : smoothFields d V) :
    actSmooth (g * h) u = actSmooth g (actSmooth h u)
```

**`PoincareGroup.hasCompactSupport_act`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L101).

> The action preserves compact support.

```lean
lemma hasCompactSupport_act (g : PoincareGroup d) {u : SpaceTime d → V}
    (hu : HasCompactSupport u) : HasCompactSupport (act g u)
```

**`PoincareGroup.actSmooth_mem_testField`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L108).

> The action preserves test fields.

```lean
lemma actSmooth_mem_testField (g : PoincareGroup d) {u : smoothFields d V}
    (hu : u ∈ compactFields (smoothFields d V)) :
    actSmooth g u ∈ compactFields (smoothFields d V)
```

**`PoincareGroup.actTest`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L114).

> The action as a linear map on test fields.

```lean
def actTest (g : PoincareGroup d) : TestField d V →ₗ[ℝ] TestField d V
```

**`PoincareGroup.actTest_coe`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean#L119).

> The value of a transformed test field.

```lean
lemma actTest_coe (g : PoincareGroup d) (f : TestField d V) :
    ((actTest g f : TestField d V) : smoothFields d V) = actSmooth g f
```

## Depends on

- [The Poincaré group](basic.md)
- [Smooth fields and distributions on spacetime](../../spaceandtime/spacetime/fields.md)

## Sources

- [PhyslibAlpha/Relativity/Poincare/Fields.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Fields.lean)
