---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix, Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_eq_vectorPotential, Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_basis_repr_eq_vector_potential, Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_distSpaceDeriv_basis_repr_eq_vector_potential, Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_basis_repr_eq_fieldStrength, Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_one_dim_eq_zero
statement: formalized
proof: formalized
---

# The Magnetic Field

The module `Physlib.Electromagnetism.TemperedDistributional.MagneticField`, [Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean): 6 declarations, 1 with a docstring.

## i. Overview

> In general dimensions we define the magnetic field matrix from the spatial components of the
> field strength matrix. This is an antisymmetric matrix. We define it
> in this module for distributions.

## ii. Key results

> - `TempDistElectromagneticPotential.magneticFieldMatrix` : The magnetic field matrix from the
>   electromagnetic potential in general spatial dimensions.

## iv. References

> * None.

## A. Magnetic field matrix for distributions

**`Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean#L60).

> The magnetic field matrix of an electromagnetic potential which is a distribution.

```lean
noncomputable def magneticFieldMatrix {d} (c : SpeedOfLight) :
    TempDistElectromagneticPotential d →ₗ[ℝ]
    (Time × Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d) ⊗[ℝ] EuclideanSpace ℝ (Fin d))
```

### A.1. Magnetic field matrix in terms of vector potentials

**`Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_eq_vectorPotential`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean#L80).

```lean
lemma magneticFieldMatrix_eq_vectorPotential {c : SpeedOfLight}
    (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(Time × Space d, ℝ)) :
    A.magneticFieldMatrix c ε = ∑ i, ∑ j,
    (Space.distSpaceDeriv j (A.vectorPotential c) ε i -
      Space.distSpaceDeriv i (A.vectorPotential c) ε j) •
    EuclideanSpace.basisFun (Fin d) ℝ i ⊗ₜ[ℝ] EuclideanSpace.basisFun (Fin d) ℝ j
```

**`Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_basis_repr_eq_vector_potential`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean#L97).

```lean
lemma magneticFieldMatrix_basis_repr_eq_vector_potential {c : SpeedOfLight}
    (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(Time × Space d, ℝ)) (i j : Fin d) :
    ((PiLp.basisFun 2 ℝ (Fin d)).tensorProduct (PiLp.basisFun 2 ℝ (Fin d))).repr
        (A.magneticFieldMatrix c ε) (i, j) =
      Space.distSpaceDeriv j (A.vectorPotential c) ε i -
      Space.distSpaceDeriv i (A.vectorPotential c) ε j
```

**`Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_distSpaceDeriv_basis_repr_eq_vector_potential`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean#L106).

```lean
lemma magneticFieldMatrix_distSpaceDeriv_basis_repr_eq_vector_potential {c : SpeedOfLight}
    (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(Time × Space d, ℝ)) (i j k : Fin d) :
    ((PiLp.basisFun 2 ℝ (Fin d)).tensorProduct (PiLp.basisFun 2 ℝ (Fin d))).repr
    (Space.distSpaceDeriv k (A.magneticFieldMatrix c) ε) (i, j) =
    Space.distSpaceDeriv k (Space.distSpaceDeriv j (A.vectorPotential c)) ε i -
    Space.distSpaceDeriv k (Space.distSpaceDeriv i (A.vectorPotential c)) ε j
```

### A.2. The magnetic field matrix in terms of the field strength

**`Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_basis_repr_eq_fieldStrength`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean#L122).

```lean
lemma magneticFieldMatrix_basis_repr_eq_fieldStrength {c : SpeedOfLight}
    (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(Time × Space d, ℝ)) (i j : Fin d) :
    ((PiLp.basisFun 2 ℝ (Fin d)).tensorProduct (PiLp.basisFun 2 ℝ (Fin d))).repr
        (A.magneticFieldMatrix c ε) (i, j) =
      (Lorentz.Vector.basis.tensorProduct Lorentz.Vector.basis).repr
        (distTimeSlice c A.fieldStrength ε) (Sum.inr i, Sum.inr j)
```

### A.3. Magnetic field matrix in 1d

**`Electromagnetism.TempDistElectromagneticPotential.magneticFieldMatrix_one_dim_eq_zero`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean#L147).

```lean
lemma magneticFieldMatrix_one_dim_eq_zero {c : SpeedOfLight}
    (A : TempDistElectromagneticPotential 1) :
    A.magneticFieldMatrix c = 0
```

## Depends on

- [The Field Strength Tensor](fieldstrength.md)
- [The vector Potential](vectorpotential.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/MagneticField.lean)
