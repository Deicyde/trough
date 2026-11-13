---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.freeCurrentPotential, Electromagnetism.ElectromagneticPotential.freeCurrentPotential_add_const, Electromagnetism.ElectromagneticPotential.freeCurrentPotential_hasVarGradientAt, Electromagnetism.ElectromagneticPotential.freeCurrentPotential_eq_sum_scalarPotential_vectorPotential, Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential, Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential_eq_sum_basis, Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential_eq_chargeDensity_currentDensity, Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential_eq_tensor
statement: formalized
proof: formalized
---

# The Lagrangian in electromagnetism

The module `Physlib.Electromagnetism.Dynamics.Lagrangian`, [Physlib/Electromagnetism/Dynamics/Lagrangian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean): 18 declarations, 5 with a docstring.

## i. Overview

> In this module we define the Lagrangian density for the electromagnetic field in
> presence of a current density. We prove properties of this lagrangian density,
> and find it's variational gradient.
>
> The lagrangian density is given by
> `L = -1/(4 μ₀) F_{μν} F^{μν} - A_μ J^μ`
>
> …

## ii. Key results

> - `freeCurrentPotential` : The potential energy from the interaction of the electromagnetic
>   potential with a free Lorentz current density.
> - `gradFreeCurrentPotential` : The variational gradient of the free current potential.
> - `lagrangian` : The lagrangian density for the electromagnetic field in presence of a
>   Lorentz current density.
> - `gradLagrangian` : The variational gradient of the lagrangian density.
> - `gradLagrangian_eq_electricField_magneticField` : The variational gradient of the lagrangian
>   density expressed in Gauss's and Ampère laws.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]
> * https://ph.qmul.ac.uk/sites/default/files/EMT10new.pdf. [ref: qmul\_emt10\_notes]

## A. Free current potential

**`Electromagnetism.ElectromagneticPotential.freeCurrentPotential`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L88).

> The potential energy from the interaction of the electromagnetic potential
> with the free current `J`.

```lean
noncomputable def freeCurrentPotential (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d)
    (x : SpaceTime d) : ℝ
```

### A.1. Shifts in the free current potential under shifts in the potential

**`Electromagnetism.ElectromagneticPotential.freeCurrentPotential_add_const`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L98).

```lean
lemma freeCurrentPotential_add_const (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) (c : Lorentz.Vector d) (x : SpaceTime d) :
    freeCurrentPotential ⟨fun x => A x + c⟩ J x = freeCurrentPotential A J x + ⟪c, J x⟫ₘ
```

### A.2. The free current potential has a variational gradient

**`Electromagnetism.ElectromagneticPotential.freeCurrentPotential_hasVarGradientAt`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L109).

```lean
lemma freeCurrentPotential_hasVarGradientAt (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) :
    HasVarGradientAt (fun A => freeCurrentPotential ⟨A⟩ J)
    (((∑ μ, fun x => (η μ μ * J x μ) • Lorentz.Vector.basis μ))) A
```

### A.3. The free current potential in terms of the scalar and vector potentials

**`Electromagnetism.ElectromagneticPotential.freeCurrentPotential_eq_sum_scalarPotential_vectorPotential`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L137).

```lean
lemma freeCurrentPotential_eq_sum_scalarPotential_vectorPotential
    (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) (x : SpaceTime d) :
    A.freeCurrentPotential J x =
    A.scalarPotential 𝓕.c (x.time 𝓕.c) x.space * J.chargeDensity 𝓕.c (x.time 𝓕.c) x.space
    - ∑ i, A.vectorPotential 𝓕.c (x.time 𝓕.c) x.space i *
        J.currentDensity 𝓕.c (x.time 𝓕.c) x.space i
```

### A.4. The variational gradient of the free current potential

**`Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L157).

> The variational gradient of the free current potential.

```lean
noncomputable def gradFreeCurrentPotential {d} (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) : SpaceTime d → Lorentz.Vector d
```

**`Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential_eq_sum_basis`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L161).

```lean
lemma gradFreeCurrentPotential_eq_sum_basis {d} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) :
    A.gradFreeCurrentPotential J = (∑ μ, fun x => (η μ μ * J x μ) • Lorentz.Vector.basis μ)
```

**`Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential_eq_chargeDensity_currentDensity`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L167).

```lean
lemma gradFreeCurrentPotential_eq_chargeDensity_currentDensity {d}
    (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) (x : SpaceTime d) :
    A.gradFreeCurrentPotential J x =
      (𝓕.c * J.chargeDensity 𝓕.c (x.time 𝓕.c) x.space) • Lorentz.Vector.basis (Sum.inl 0) +
      (∑ i, - J.currentDensity 𝓕.c (x.time 𝓕.c) x.space i • Lorentz.Vector.basis (Sum.inr i))
```

**`Electromagnetism.ElectromagneticPotential.gradFreeCurrentPotential_eq_tensor`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L181).

```lean
lemma gradFreeCurrentPotential_eq_tensor {d} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) (x : SpaceTime d) (ν : Fin 1 ⊕ Fin d) :
    A.gradFreeCurrentPotential J x ν = η ν ν * ((Tensorial.toTensor (M := Lorentz.Vector d)).symm
    (permT id (IsReindexing.auto) {J x | ν'}ᵀ)) ν
```

## B. The Lagrangian density

> The lagrangian density for the electromagnetic field in presence of a current density `J` is
> `L = -1/(4 μ₀) F_{μν} F^{μν} - A_μ J^μ`

**`Electromagnetism.ElectromagneticPotential.lagrangian`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L205).

> The lagrangian density associated with a electromagnetic potential and a Lorentz
> current density.

```lean
noncomputable def lagrangian (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) (x : SpaceTime d) : ℝ
```

### B.1. Shifts in the lagrangian under shifts in the potential

**`Electromagnetism.ElectromagneticPotential.lagrangian_add_const`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L215).

```lean
lemma lagrangian_add_const {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) (c : Lorentz.Vector d) (x : SpaceTime d) :
    lagrangian 𝓕 ⟨fun x => A x + c⟩ J x = lagrangian 𝓕 A J x - ⟪c, J x⟫ₘ
```

### B.2. Lagrangian in terms of electric and magnetic fields

**`Electromagnetism.ElectromagneticPotential.lagrangian_eq_electric_magnetic`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L228).

> The Lagrangian is equal to `1/2 * (ε₀ E^2 - 1/μ₀ B^2) - φρ + A · j`

```lean
lemma lagrangian_eq_electric_magnetic {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (hA : ContDiff ℝ 2 A)
    (J : LorentzCurrentDensity d) (x : SpaceTime d) :
    A.lagrangian 𝓕 J x = 1 / 2 * (𝓕.ε₀ * ‖A.electricField 𝓕.c (x.time 𝓕.c) x.space‖ ^ 2 -
    (1 / (2 * 𝓕.μ₀)) * ∑ i, ∑ j, ‖A.magneticFieldMatrix 𝓕.c (x.time 𝓕.c) x.space (i, j)‖ ^ 2)
    - A.scalarPotential 𝓕.c (x.time 𝓕.c) x.space * J.chargeDensity 𝓕.c (x.time 𝓕.c) x.space
    + ∑ i, A.vectorPotential 𝓕.c (x.time 𝓕.c) x.space i *
        J.currentDensity 𝓕.c (x.time 𝓕.c) x.space i
```

## C. The variational gradient of the lagrangian density

### C.1. The lagrangian density has a variational gradient

**`Electromagnetism.ElectromagneticPotential.lagrangian_hasVarGradientAt_eq_add_gradKineticTerm`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L252).

```lean
lemma lagrangian_hasVarGradientAt_eq_add_gradKineticTerm {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) :
    HasVarGradientAt (fun A => lagrangian 𝓕 ⟨A⟩ J)
    (A.gradKineticTerm 𝓕 - A.gradFreeCurrentPotential J) A
```

### C.2. The definition of, `gradLagrangian`, the variational gradient of the lagrangian density

**`Electromagnetism.ElectromagneticPotential.gradLagrangian`**, a def, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L273).

> The variational gradient of the lagrangian of electromagnetic field.

```lean
noncomputable def gradLagrangian {d} (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) : SpaceTime d → Lorentz.Vector d
```

### C.3. The variational gradient in terms of the gradient of the kinetic term

**`Electromagnetism.ElectromagneticPotential.gradLagrangian_eq_kineticTerm_sub`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L283).

```lean
lemma gradLagrangian_eq_kineticTerm_sub {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) :
    A.gradLagrangian 𝓕 J = A.gradKineticTerm 𝓕 - A.gradFreeCurrentPotential J
```

### C.4. The lagrangian density has the variational gradient equal to `gradLagrangian`

**`Electromagnetism.ElectromagneticPotential.lagrangian_hasVarGradientAt_gradLagrangian`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L294).

```lean
lemma lagrangian_hasVarGradientAt_gradLagrangian {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d) (hJ : ContDiff ℝ ∞ J) :
    HasVarGradientAt (fun A => lagrangian 𝓕 ⟨A⟩ J) (A.gradLagrangian 𝓕 J) A
```

### C.5. The variational gradient in terms of the field strength tensor

**`Electromagnetism.ElectromagneticPotential.gradLagrangian_eq_sum_toFieldStrength_eval`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L307).

```lean
lemma gradLagrangian_eq_sum_toFieldStrength_eval {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d) (hJ : ContDiff ℝ ∞ J) :
    A.gradLagrangian 𝓕 J = fun x => ∑ ν,
      (η ν ν • (1 / 𝓕.μ₀ * ∑ μ, ∂_ μ (fun x => toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ) x
      - J x ν) • Lorentz.Vector.basis ν)
```

### C.6. The lagrangian gradient recovering Gauss's and Ampère laws

**`Electromagnetism.ElectromagneticPotential.gradLagrangian_eq_electricField_magneticField`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L329).

```lean
lemma gradLagrangian_eq_electricField_magneticField {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) (x : SpaceTime d) :
    A.gradLagrangian 𝓕 J x = (1 / (𝓕.μ₀ * 𝓕.c.val) *
        Space.div (electricField 𝓕.c A ((time 𝓕.c) x)) (space x) +
        - 𝓕.c * J.chargeDensity 𝓕.c (x.time 𝓕.c) x.space) •
      Lorentz.Vector.basis (Sum.inl 0) +
    ∑ i, (𝓕.μ₀⁻¹ * (𝓕.ε₀ * 𝓕.μ₀ * ∂ₜ (electricField 𝓕.c A · x.space) ((time 𝓕.c) x) i -
      ∑ j, ∂[j] (magneticFieldMatrix 𝓕.c A (x.time 𝓕.c) · (j, i)) x.space) +
      J.currentDensity 𝓕.c (x.time 𝓕.c) x.space i) •
        Lorentz.Vector.basis (Sum.inr i)
```

### C.7. The lagrangian gradient in tensor notation

**`Electromagnetism.ElectromagneticPotential.gradLagrangian_eq_tensor`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean#L357).

```lean
lemma gradLagrangian_eq_tensor {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) (x : SpaceTime d) (ν : Fin 1 ⊕ Fin d) :
    A.gradLagrangian 𝓕 J x ν =
    η ν ν * ((Tensorial.toTensor (M := Lorentz.Vector d)).symm
    (permT id (IsReindexing.auto) {((1/ 𝓕.μ₀ : ℝ) • tensorDeriv A.toFieldStrength x | κ κ ν') +
    - (J x | ν')}ᵀ)) ν
```

## Depends on

- [The Lorentz Current Density](currentdensity.md)
- [The kinetic term](kineticterm.md)

## Sources

- [Physlib/Electromagnetism/Dynamics/Lagrangian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Lagrangian.lean)
