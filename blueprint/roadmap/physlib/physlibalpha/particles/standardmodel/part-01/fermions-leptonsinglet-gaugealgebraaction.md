---
declaration: module
origin: cited
lean: StandardModel.LeptonSinglet.gaugeAlgebraAction, StandardModel.LeptonSinglet.gaugeAlgebraAction_apply, StandardModel.LeptonSinglet.matterField_repAlgebra_gaugeAlgebraEquiv, StandardModel.LeptonSinglet.gaugeAlgebraAction_comm_repLorentzGroup
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the charged-lepton singlet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonSinglet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean): 4 declarations, 4 with a docstring.

> The explicit `(1, 1)_{-6}` action of the gauge algebra on the charged-lepton singlet, and its
> agreement with the matter field.

## i. Overview

> The charged-lepton singlet carries the `(1, 1)_{-6}` representation of the gauge group,
> so the infinitesimal action of the gauge algebra is scalar, multiplication by
> `i` times `-6` times the `u(1)` value of the algebra element. This file defines that
> action and identifies it with the action of the gauge algebra of the matter field of
> the charged-lepton singlet, through the isomorphism of the gauge algebra with the Lie algebra
> of the global gauge group.

## ii. Key results

> - `gaugeAlgebraAction` : the infinitesimal `(1, 1)_{-6}` action of the gauge algebra.
> - `matterField_repAlgebra_gaugeAlgebraEquiv` : the action of the gauge algebra of the
>   matter field is `gaugeAlgebraAction`.
> - `gaugeAlgebraAction_comm_repLorentzGroup` : the gauge action commutes with the Lorentz
>   action.

## iv. References

> * None.

## A. The infinitesimal action of the gauge algebra

> The `(1, 1)_{-6}` representation acts through the `u(1)` factor alone, so its
> derivative is scalar multiplication by `i (-6)` times the `u(1)` value.

**`StandardModel.LeptonSinglet.gaugeAlgebraAction`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L66).

> The infinitesimal action of the gauge algebra on the charged-lepton singlet, the derivative
> of the `(1, 1)_{-6}` action of the gauge group. It is scalar multiplication by `i` times `-6`
> times the `u(1)` value, real-linear in the algebra slot and complex-linear in the value
> slot.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] LeptonSinglet →ₗ[ℂ] LeptonSinglet
```

**`StandardModel.LeptonSinglet.gaugeAlgebraAction_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L86).

> The gauge-algebra action on the charged-lepton singlet is scalar multiplication
> by `i` times `-6` times the `u(1)` value.

```lean
lemma gaugeAlgebraAction_apply (c : GaugeAlgebra) :
    gaugeAlgebraAction c
      = (Complex.I * (-(6 : ℂ) * c.toU1Value))
        • (LinearMap.id : LeptonSinglet →ₗ[ℂ] LeptonSinglet)
```

## B. The action of the matter field

**`StandardModel.LeptonSinglet.matterField_repAlgebra_gaugeAlgebraEquiv`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L99).

> The action of the gauge algebra of the matter field of the charged-lepton singlet,
> evaluated on the image of a gauge algebra element, is `gaugeAlgebraAction`.

```lean
lemma matterField_repAlgebra_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    matterField.repAlgebra (gaugeAlgebraEquiv c) = gaugeAlgebraAction c
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.LeptonSinglet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L121).

> The infinitesimal gauge action on the charged-lepton singlet is a scalar, so it
> commutes with the Lorentz action.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : LeptonSinglet) :
    LeptonSinglet.gaugeAlgebraAction c (LeptonSinglet.repLorentzGroup Λ v) =
      LeptonSinglet.repLorentzGroup Λ (LeptonSinglet.gaugeAlgebraAction c v)
```

## Depends on

- [The charged-lepton singlet as a matter field](fermions-leptonsinglet-matterfield.md)
- [The gauge algebra as the Lie algebra of the global gauge group](../part-02/gaugegroup-liealgebra.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean)
