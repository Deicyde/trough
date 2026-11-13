---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential, Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_eq_sum_basis, Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_sum_inl_0, Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_sum_inr_i, Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_eq_tensor, Electromagnetism.TempDistElectromagneticPotential.gradLagrangian, Electromagnetism.TempDistElectromagneticPotential.gradLagrangian_sum_inl_0, Electromagnetism.TempDistElectromagneticPotential.gradLagrangian_sum_inr_i
statement: formalized
proof: formalized
---

# The Lagrangian in electromagnetism (TemperedDistributional/Dynamics/Lagrangian)

The module `Physlib.Electromagnetism.TemperedDistributional.Dynamics.Lagrangian`, [Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean): 9 declarations, 2 with a docstring.

## i. Overview

> In this module we define the Lagrangian density for the electromagnetic field in
> presence of a current density. We prove properties of this lagrangian density,
> and find it's variational gradient.
>
> The lagrangian density is given by
> `L = -1/(4 μ₀) F_{μν} F^{μν} - A_μ J^μ`
>
> In this implementation we set `μ₀ = 1`. …

## ii. Key results

> - `gradFreeCurrentPotential` : The variational gradient of the free current potential.
> - `gradLagrangian` : The variational gradient of the lagrangian density.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]
> * https://ph.qmul.ac.uk/sites/default/files/EMT10new.pdf. [ref: qmul\_emt10\_notes]

## A. The gradient of the lagrangian density for distributions

### A.1. The gradient of the free current potential

> We define this through the lemma `gradFreeCurrentPotential_eq_sum_basis`

**`Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L75).

> The variational gradient of the free current potential for distributional potentials.

```lean
noncomputable def gradFreeCurrentPotential {d} :
    TempDistLorentzCurrentDensity d →ₗ[ℝ] ((SpaceTime d) →d[ℝ] Lorentz.Vector d)
```

**`Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_eq_sum_basis`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L98).

```lean
lemma gradFreeCurrentPotential_eq_sum_basis {d}
    (J : TempDistLorentzCurrentDensity d) (ε : 𝓢(SpaceTime d, ℝ)) :
    (gradFreeCurrentPotential J) ε =
    (∑ μ, (η μ μ • (J ε μ) • Lorentz.Vector.basis μ))
```

**`Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_sum_inl_0`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L103).

```lean
lemma gradFreeCurrentPotential_sum_inl_0 (𝓕 : FreeSpace) {d}
    (J : TempDistLorentzCurrentDensity d) (ε : 𝓢(SpaceTime d, ℝ)) :
    (gradFreeCurrentPotential J) ε (Sum.inl 0) =
    𝓕.c * (distTimeSlice 𝓕.c).symm (J.chargeDensity 𝓕.c) ε
```

**`Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_sum_inr_i`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L117).

```lean
lemma gradFreeCurrentPotential_sum_inr_i (𝓕 : FreeSpace) {d}
    (J : TempDistLorentzCurrentDensity d) (ε : 𝓢(SpaceTime d, ℝ)) (i : Fin d) :
    (gradFreeCurrentPotential J) ε (Sum.inr i) =
    - (distTimeSlice 𝓕.c).symm (J.currentDensity 𝓕.c) ε i
```

#### A.1.1. Free current potential as a tensor

**`Electromagnetism.TempDistElectromagneticPotential.gradFreeCurrentPotential_eq_tensor`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L135).

```lean
lemma gradFreeCurrentPotential_eq_tensor {d}
    (J : TempDistLorentzCurrentDensity d) (ε : 𝓢(SpaceTime d, ℝ))
    (ν : Fin 1 ⊕ Fin d) :
    gradFreeCurrentPotential J ε ν = η ν ν * ((Tensorial.toTensor (M := Lorentz.Vector d)).symm
    (permT id (IsReindexing.auto) {J ε | ν'}ᵀ)) ν
```

### A.2. The gradient of the lagrangian density

> Defined through `gradLagrangian_eq_kineticTerm_sub`.

**`Electromagnetism.TempDistElectromagneticPotential.gradLagrangian`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L158).

> The variational gradient of lagrangian for an electromagnetic potential which is
> a distribution.

```lean
noncomputable def gradLagrangian {d} (𝓕 : FreeSpace) (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) : ((SpaceTime d) →d[ℝ] Lorentz.Vector d)
```

**`Electromagnetism.TempDistElectromagneticPotential.gradLagrangian_sum_inl_0`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L162).

```lean
lemma gradLagrangian_sum_inl_0 {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (J : TempDistLorentzCurrentDensity d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    A.gradLagrangian 𝓕 J ε (Sum.inl 0) =
    (1/(𝓕.μ₀ * 𝓕.c) * (distTimeSlice 𝓕.c).symm (Space.distSpaceDiv (A.electricField 𝓕.c)) ε)
    - 𝓕.c * (distTimeSlice 𝓕.c).symm (J.chargeDensity 𝓕.c) ε
```

**`Electromagnetism.TempDistElectromagneticPotential.gradLagrangian_sum_inr_i`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L170).

```lean
lemma gradLagrangian_sum_inr_i {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (J : TempDistLorentzCurrentDensity d)
    (ε : 𝓢(SpaceTime d, ℝ)) (i : Fin d) :
    A.gradLagrangian 𝓕 J ε (Sum.inr i) =
    𝓕.μ₀⁻¹ * (1 / 𝓕.c ^ 2 *
      (distTimeSlice 𝓕.c).symm (Space.distTimeDeriv (A.electricField 𝓕.c)) ε i -
      ∑ j, ((PiLp.basisFun 2 ℝ (Fin d)).tensorProduct (PiLp.basisFun 2 ℝ (Fin d))).repr
        ((distTimeSlice 𝓕.c).symm (Space.distSpaceDeriv j (A.magneticFieldMatrix 𝓕.c)) ε) (j, i)) +
    (distTimeSlice 𝓕.c).symm (J.currentDensity 𝓕.c) ε i
```

#### A.2.1. The lagrangian gradient as a tensor

**`Electromagnetism.TempDistElectromagneticPotential.gradLagrangian_eq_tensor`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean#L188).

```lean
lemma gradLagrangian_eq_tensor {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d) (J : TempDistLorentzCurrentDensity d)
    (ε : 𝓢(SpaceTime d, ℝ)) (ν : Fin 1 ⊕ Fin d) :
    A.gradLagrangian 𝓕 J ε ν =
    η ν ν * ((Tensorial.toTensor (M := Lorentz.Vector d)).symm
    (permT id (IsReindexing.auto) {((1/ 𝓕.μ₀ : ℝ) • (distTensorDeriv A.fieldStrength ε) | κ κ ν') +
    - (J ε | ν')}ᵀ)) ν
```

## Depends on

- [The Lorentz Current Density (TemperedDistributional/Dynamics/CurrentDensity)](dynamics-currentdensity.md)
- [The kinetic term (TemperedDistributional/Dynamics/KineticTerm)](dynamics-kineticterm.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/Lagrangian.lean)
