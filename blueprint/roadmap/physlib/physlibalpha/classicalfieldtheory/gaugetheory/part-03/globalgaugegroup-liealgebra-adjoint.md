---
declaration: module
origin: cited
lean: GlobalGaugeGroup.adjoint, GlobalGaugeGroup.adjoint_val, GlobalGaugeGroup.oneParameterSubgroup_adjoint
statement: formalized
proof: formalized
---

# The adjoint action of a global gauge group on its Lie algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.Adjoint`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean): 3 declarations, 2 with a docstring.

> The action `X ↦ g X g⁻¹` of a global gauge group on its Lie algebra.

## i. Overview

> A global gauge group `G` acts on its Lie algebra `𝔤` by conjugation, `X ↦ g X g⁻¹`. This is
> the adjoint action, the way an infinitesimal gauge transformation changes under a global
> one, and it is how the gauge fields transform under `G`. It maps the one-parameter subgroup
> of `X` to the conjugate by `g` of that subgroup, since `exp (t g X g⁻¹) = g exp (t X) g⁻¹`.

## ii. Key results

> - `GlobalGaugeGroup.adjoint` : the adjoint action of the group on its Lie algebra.
> - `GlobalGaugeGroup.oneParameterSubgroup_adjoint` : the one-parameter subgroup of `g X g⁻¹`
>   is the conjugate of that of `X`.

## iv. References

> * B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

## A. The adjoint action

**`GlobalGaugeGroup.adjoint`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean#L53).

> The adjoint action `X ↦ g X g⁻¹` of an element `g` of the group on its Lie algebra.

```lean
def adjoint (g : G.group) (X : G.lieAlgebra) : G.lieAlgebra
```

**`GlobalGaugeGroup.adjoint_val`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean#L60).

```lean
lemma adjoint_val (g : G.group) (X : G.lieAlgebra) :
    (G.adjoint g X : Matrix κ κ ℂ) = (g.1 : Matrix κ κ ℂ) * X * (↑g.1⁻¹ : Matrix κ κ ℂ)
```

## B. The adjoint action on one-parameter subgroups

**`GlobalGaugeGroup.oneParameterSubgroup_adjoint`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean#L70).

> The one-parameter subgroup of `g X g⁻¹` is the conjugate by `g` of that of `X`.

```lean
lemma oneParameterSubgroup_adjoint (g : G.group) (X : G.lieAlgebra) (t : ℝ) :
    G.oneParameterSubgroup (G.adjoint g X) t = g * G.oneParameterSubgroup X t * g⁻¹
```

## Depends on

- [One-parameter subgroups of a global gauge group](globalgaugegroup-liealgebra-oneparameter.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Adjoint.lean)
