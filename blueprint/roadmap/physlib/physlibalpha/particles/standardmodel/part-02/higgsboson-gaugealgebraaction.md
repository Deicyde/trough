---
declaration: module
origin: cited
lean: StandardModel.HiggsVec.weakEnd, StandardModel.HiggsVec.weakEnd_apply, StandardModel.HiggsVec.weakEnd_add, StandardModel.HiggsVec.weakEnd_smul, StandardModel.HiggsVec.actionMatrix, StandardModel.HiggsVec.gaugeAlgebraAction, StandardModel.HiggsVec.valEnd_eq_weakEnd, StandardModel.HiggsVec.derivMat_gaugeRep_gaugeAlgebraEquiv
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the Higgs doublet

The module `PhyslibAlpha.Particles.StandardModel.HiggsBoson.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean): 9 declarations, 9 with a docstring.

> The explicit `(1, 2)_{3}` action of the gauge algebra on the Higgs doublet, and its agreement
> with the matter field.

## i. Overview

> The infinitesimal `(1, 2)_{3}` action of the gauge algebra on the Higgs doublet is written out
> here in the form used by physicists. The weak part of the algebra element acts on the weak index
> and the hypercharge part scales, both through the physicists' factor of `i`, matching the group
> action `u ^ 3 • U₂` infinitesimally. Section B checks that this is the action of the Lie algebra
> on the matter field `HiggsVec.matterField`, which is defined abstractly as the derivative of the
> group action, transported along the Lie algebra isomorphism `gaugeAlgebraEquiv`.

## ii. Key results

> - `StandardModel.HiggsVec.weakEnd` : the endomorphism of the Higgs doublet defined by a
>   `2 × 2` matrix on the weak index.
> - `StandardModel.HiggsVec.gaugeAlgebraAction` : the infinitesimal `(1, 2)_{3}` action of the
>   gauge algebra.
> - `StandardModel.HiggsVec.matterField_repAlgebra_gaugeAlgebraEquiv` : the action of the Lie
>   algebra on the matter field of the Higgs, at the image of `c` under `gaugeAlgebraEquiv`, is
>   `gaugeAlgebraAction c`.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.HiggsVec.weakEnd`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L64).

> The endomorphism of the Higgs doublet defined by a `2 × 2` complex matrix acting on
> the weak index.

```lean
noncomputable def weakEnd (A : Matrix (Fin 2) (Fin 2) ℂ) :
    HiggsVec →ₗ[ℂ] HiggsVec
```

**`StandardModel.HiggsVec.weakEnd_apply`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L69).

> The weak endomorphism applies the matrix to the doublet.

```lean
lemma weakEnd_apply (A : Matrix (Fin 2) (Fin 2) ℂ) (v : HiggsVec) :
    weakEnd A v = Matrix.toLpLinAlgEquiv 2 A v
```

**`StandardModel.HiggsVec.weakEnd_add`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L73).

> The weak endomorphism is additive in the matrix.

```lean
lemma weakEnd_add (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (A + B) = weakEnd A + weakEnd B
```

**`StandardModel.HiggsVec.weakEnd_smul`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L78).

> The weak endomorphism is complex-linear in the matrix.

```lean
lemma weakEnd_smul (z : ℂ) (A : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (z • A) = z • weakEnd A
```

**`StandardModel.HiggsVec.actionMatrix`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L84).

> The matrix of the infinitesimal `(1, 2)_{3}` action of a gauge algebra element on
> the weak index, `i` times the weak part shifted by `i` times `3` the hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.HiggsVec.gaugeAlgebraAction`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L90).

> The infinitesimal action of the gauge algebra on the Higgs doublet, the derivative of the
> `(1, 2)_{3}` action of the gauge group. It is real-linear in the algebra slot and
> complex-linear in the value slot.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] HiggsVec →ₗ[ℂ] HiggsVec
```

## B. The action of the gauge algebra of the matter field

**`StandardModel.HiggsVec.valEnd_eq_weakEnd`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L123).

> The endomorphism of the Higgs doublet induced by a matrix on the internal index, through
> the identification `tensorEquiv`, is the weak endomorphism.

```lean
lemma valEnd_eq_weakEnd (A : Matrix (Fin 2) (Fin 2) ℂ) :
    MatrixRep.valEnd tensorEquiv A = weakEnd A
```

**`StandardModel.HiggsVec.derivMat_gaugeRep_gaugeAlgebraEquiv`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L137).

> The matrix of the action of the gauge algebra on the gauge representation of the Higgs,
> at the image of `c` under `gaugeAlgebraEquiv`, is `actionMatrix c`.

```lean
lemma derivMat_gaugeRep_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    derivMat gaugeRep (gaugeAlgebraEquiv c) = actionMatrix c
```

**`StandardModel.HiggsVec.matterField_repAlgebra_gaugeAlgebraEquiv`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L147).

> The action of the gauge algebra of the matter field of the Higgs, at the image of
> `c` under `gaugeAlgebraEquiv`, is `gaugeAlgebraAction c`.

```lean
lemma matterField_repAlgebra_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    matterField.repAlgebra (gaugeAlgebraEquiv c) = gaugeAlgebraAction c
```

## Depends on

- [The gauge algebra as the Lie algebra of the global gauge group](gaugegroup-liealgebra.md)
- [The Higgs field as a matter field](higgsboson-matterfield.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean)
