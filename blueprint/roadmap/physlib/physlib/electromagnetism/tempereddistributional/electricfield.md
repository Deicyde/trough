---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.electricField, Electromagnetism.TempDistElectromagneticPotential.electricField_eq_fieldStrength
statement: formalized
proof: formalized
---

# The Electric Field (TemperedDistributional/ElectricField)

The module `Physlib.Electromagnetism.TemperedDistributional.ElectricField`, [Physlib/Electromagnetism/TemperedDistributional/ElectricField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ElectricField.lean): 2 declarations, 1 with a docstring.

## i. Overview

> The electric field is defined in terms of the electromagnetic potential `A` as
> `E = - ∇ φ - ∂ₜ \vec A`.
>
> In this module we define the electric field, and prove lemmas about it.

## ii. Key results

> - `DistElectromagneticPotential.electricField` : The electric field for
>   electromagnetic potentials which are distributions.

## iv. References

> * None.

## A. Electric field for distributions

**`Electromagnetism.TempDistElectromagneticPotential.electricField`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ElectricField.lean#L58).

> The electric field of an electromagnetic potential which is a distribution.

```lean
noncomputable def electricField {d} (c : SpeedOfLight) :
    TempDistElectromagneticPotential d →ₗ[ℝ]
    (Time × Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)
```

**`Electromagnetism.TempDistElectromagneticPotential.electricField_eq_fieldStrength`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ElectricField.lean#L76).

```lean
lemma electricField_eq_fieldStrength {d} {c : SpeedOfLight}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(Time × Space d, ℝ))
    (i : Fin d) : A.electricField c ε i = - c * (Vector.basis.tensorProduct Vector.basis).repr
      (distTimeSlice c (A.fieldStrength) ε) (Sum.inl 0, Sum.inr i)
```

## Depends on

- [The Field Strength Tensor (TemperedDistributional/FieldStrength)](fieldstrength.md)
- [The Scalar Potential (TemperedDistributional/ScalarPotential)](scalarpotential.md)
- [The vector Potential (TemperedDistributional/VectorPotential)](vectorpotential.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/ElectricField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/ElectricField.lean)
