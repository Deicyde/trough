---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm, Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_eq_sum_sum, Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_eq_fieldStrength, Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_sum_inl_eq, Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_sum_inr_eq, Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_eq_distTensorDeriv
statement: formalized
proof: formalized
---

# The kinetic term

The module `Physlib.Electromagnetism.TemperedDistributional.Dynamics.KineticTerm`, [Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean): 6 declarations, 1 with a docstring.

## i. Overview

> The kinetic term of the electromagnetic field is `- 1/(4 μ₀) F_μν F^μν`.
> We define this, show it is invariant under Lorentz transformations,
> and show properties of its variational gradient.
>
> In particular the variational gradient `gradKineticTerm` of the kinetic term
> is directly related to Gauss's law and the Ampere law.
>
> …

## ii. Key results

> - `TempDistElectromagneticPotential.gradKineticTerm` is the variational gradient of the kinetic term
>   for distributional electromagnetic potentials.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]

## A. The gradient of the kinetic term for distributions

> For distributions we define the gradient of the kinetic term directly
> using `ElectromagneticPotential.gradKineticTerm_eq_sum_sum` as the defining formula.

**`Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean#L64).

> The gradient of the kinetic term for an Electromagnetic potential which
> is a distribution.

```lean
noncomputable def gradKineticTerm {d} (𝓕 : FreeSpace) :
    TempDistElectromagneticPotential d →ₗ[ℝ] (SpaceTime d) →d[ℝ] Lorentz.Vector d
```

**`Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_eq_sum_sum`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean#L95).

```lean
lemma gradKineticTerm_eq_sum_sum {d} {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) :
    A.gradKineticTerm 𝓕 ε = ∑ ν, ∑ μ,
        (1 / (𝓕.μ₀) * (η μ μ * η ν ν * distDeriv μ (distDeriv μ A) ε ν -
        distDeriv μ (distDeriv ν A) ε μ)) • Lorentz.Vector.basis ν
```

**`Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_eq_fieldStrength`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean#L101).

```lean
lemma gradKineticTerm_eq_fieldStrength {d} {𝓕 : FreeSpace} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    A.gradKineticTerm 𝓕 ε = ∑ ν, (1/𝓕.μ₀ * η ν ν) •
    (∑ μ, ((Vector.basis.tensorProduct Vector.basis).repr
      (distDeriv μ (A.fieldStrength) ε) (μ, ν))) • Lorentz.Vector.basis ν
```

**`Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_sum_inl_eq`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean#L122).

```lean
lemma gradKineticTerm_sum_inl_eq {d} {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) :
    A.gradKineticTerm 𝓕 ε (Sum.inl 0) =
    (1/(𝓕.μ₀ * 𝓕.c) * (distTimeSlice 𝓕.c).symm (Space.distSpaceDiv (A.electricField 𝓕.c)) ε)
```

**`Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_sum_inr_eq`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean#L143).

```lean
lemma gradKineticTerm_sum_inr_eq {d} {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) (i : Fin d) :
    A.gradKineticTerm 𝓕 ε (Sum.inr i) =
    (𝓕.μ₀⁻¹ * (1 / 𝓕.c ^ 2 * (distTimeSlice 𝓕.c).symm
      (Space.distTimeDeriv (A.electricField 𝓕.c)) ε i -
      ∑ j, ((PiLp.basisFun 2 ℝ (Fin d)).tensorProduct (PiLp.basisFun 2 ℝ (Fin d))).repr
        ((distTimeSlice 𝓕.c).symm (Space.distSpaceDeriv j
          (A.magneticFieldMatrix 𝓕.c)) ε) (j, i)))
```

### A.1. The gradient of the kinetic term as a tensor

**`Electromagnetism.TempDistElectromagneticPotential.gradKineticTerm_eq_distTensorDeriv`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean#L177).

```lean
lemma gradKineticTerm_eq_distTensorDeriv {d} {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (ε : 𝓢(SpaceTime d, ℝ)) (ν : Fin 1 ⊕ Fin d) :
    A.gradKineticTerm 𝓕 ε ν = η ν ν * ((Tensorial.toTensor (M := Lorentz.Vector d)).symm
    (permT id (IsReindexing.auto) {(1/ 𝓕.μ₀ : ℝ) •
    distTensorDeriv A.fieldStrength ε | κ κ ν'}ᵀ)) ν
```

## Depends on

- [Free space](../dynamics/basic.md)
- [The Electric Field](electricfield.md)
- [The Magnetic Field](magneticfield.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/KineticTerm.lean)
