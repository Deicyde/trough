---
declaration: module
origin: cited
lean: StandardModel.GaugeGroupI.gaugeCartan, StandardModel.GaugeGroupI.gaugeCartan_toU1, StandardModel.GaugeGroupI.gaugeCartan_toSU2_coe, StandardModel.GaugeGroupI.gaugeCartan_smul_eq
statement: formalized
proof: formalized
---

# The gauge torus acting on Higgs vectors

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.GaugeTorus`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean): 4 declarations, 2 with a docstring.

> The SU(2) Cartan element diag(a, ā), which with the electromagnetic U(1) realises the gauge torus.

## i. Overview

> The maximal torus of the gauge group acting on a Higgs doublet is the group of diagonal phase
> rotations `diag(a, b)` of the two components. We realise it using
>
> * the `SU(2)` Cartan element `diag(a, ā)` (constructed here as `gaugeCartan`), and
> * the electromagnetic `U(1)` `electromagnetismU1`, whose action is `diag(μ, 1)`.
>
> Together these realise an arbitrary diagonal phase `diag(a, b)`, which is the symmetry underlying
> the charge-balancing ("Condition A") of the effective potential on the orbit representatives.

## ii. Key results

> - `StandardModel.GaugeGroupI.gaugeCartan` : the Cartan `SU(2)` gauge element `diag(a, ā)`.
> - `StandardModel.GaugeGroupI.gaugeCartan_smul_eq` : it acts on a Higgs vector as `diag(a, ā)`.

## iv. References

> * None.

## A. The Cartan gauge element

**`StandardModel.GaugeGroupI.gaugeCartan`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean#L56).

> The Cartan `SU(2)` gauge element `diag(a, ā)`, for `a` a phase.

```lean
noncomputable def gaugeCartan (a : unitary ℂ) : GaugeGroupI
```

**`StandardModel.GaugeGroupI.gaugeCartan_toU1`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean#L72).

```lean
lemma gaugeCartan_toU1 (a : unitary ℂ) : (gaugeCartan a).toU1 = 1
```

**`StandardModel.GaugeGroupI.gaugeCartan_toSU2_coe`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean#L75).

```lean
lemma gaugeCartan_toSU2_coe (a : unitary ℂ) :
    ((gaugeCartan a).toSU2 : Matrix (Fin 2) (Fin 2) ℂ) = !![(a : ℂ), 0; 0, (star a : ℂ)]
```

**`StandardModel.GaugeGroupI.gaugeCartan_smul_eq`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean#L79).

> The Cartan element acts as the diagonal matrix `diag(a, ā)`.

```lean
lemma gaugeCartan_smul_eq (a : unitary ℂ) (φ : HiggsVec) :
    HiggsVec.repGaugeGroupI (gaugeCartan a) φ =
      WithLp.toLp 2 (!![(a : ℂ), 0; 0, (star a : ℂ)] *ᵥ φ.ofLp)
```

## Depends on

- [The Higgs field](../../../physlib/particles/standardmodel/higgsboson/basic.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/GaugeTorus.lean)
