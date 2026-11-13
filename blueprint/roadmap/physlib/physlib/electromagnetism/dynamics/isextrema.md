---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.IsExtrema, Electromagnetism.ElectromagneticPotential.isExtrema_iff_gradLagrangian, Electromagnetism.ElectromagneticPotential.isExtrema_iff_toFieldStrength_eval, Electromagnetism.ElectromagneticPotential.isExtrema_iff_tensors, Electromagnetism.ElectromagneticPotential.isExtrema_lorentzGroup_apply_iff, Electromagnetism.ElectromagneticPotential.isExtrema_iff_gauss_ampere_magneticFieldMatrix, Electromagnetism.ElectromagneticPotential.time_deriv_electricField_of_isExtrema, Electromagnetism.ElectromagneticPotential.time_deriv_time_deriv_magneticFieldMatrix_of_isExtrema
statement: formalized
proof: formalized
---

# Extrema of the Lagrangian density

The module `Physlib.Electromagnetism.Dynamics.IsExtrema`, [Physlib/Electromagnetism/Dynamics/IsExtrema.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean): 9 declarations, 1 with a docstring.

## i. Overview

> In this module we define what it means for an electromagnetic potential
> to be an extremum of the Lagrangian density in presence of a Lorentz current density.
>
> This is equivalent to the electromagnetic potential satisfying
> Maxwell's equations with sources, i.e. Gauss's law and Ampère's law.

## ii. Key results

> - `IsExtrema` : The condition on an electromagnetic potential to be an extrema of the lagrangian.
> - `isExtrema_iff_gauss_ampere_magneticFieldMatrix` : The electromagnetic potential is an extrema
>   of the lagrangian if and only if Gauss's law and Ampère's law hold
>   (in terms of the magnetic field matrix).
> - `time_deriv_time_deriv_magneticFieldMatrix_of_isExtrema` : A wave-like equation for the
>   magnetic field matrix from the extrema condition.
> - `time_deriv_time_deriv_electricField_of_isExtrema` : A wave-like equation for the
>   electric field from the extrema condition.

## iv. References

> * None.

## A. The condition for an extrema of the Lagrangian density

**`Electromagnetism.ElectromagneticPotential.IsExtrema`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L75).

> The condition on an electromagnetic potential to be an extrema of the lagrangian.

```lean
def IsExtrema {d} (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) : Prop
```

**`Electromagnetism.ElectromagneticPotential.isExtrema_iff_gradLagrangian`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L79).

```lean
lemma isExtrema_iff_gradLagrangian {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) :
    IsExtrema 𝓕 A J ↔ A.gradLagrangian 𝓕 J = 0
```

### A.1. Extrema condition in terms of the field strength tensor

**`Electromagnetism.ElectromagneticPotential.isExtrema_iff_toFieldStrength_eval`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L89).

```lean
lemma isExtrema_iff_toFieldStrength_eval {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d) (hJ : ContDiff ℝ ∞ J) :
    IsExtrema 𝓕 A J ↔
    ∀ x, ∀ ν, ∑ μ, ∂_ μ (fun x => toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ) x =
      𝓕.μ₀ * J x ν
```

### A.2. Extrema condition in terms of tensors

> The electromagnetic potential is an exterma of the lagrangian if and only if
>
> $$\frac{1}{\mu_0} \partial_\mu F^{\mu \nu} - J^{\nu} = 0.$$

**`Electromagnetism.ElectromagneticPotential.isExtrema_iff_tensors`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L131).

```lean
lemma isExtrema_iff_tensors {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d) (hJ : ContDiff ℝ ∞ J) :
    IsExtrema 𝓕 A J ↔ ∀ x,
    {((1/ 𝓕.μ₀ : ℝ) • tensorDeriv A.toFieldStrength x | κ κ ν') + - (J x | ν')}ᵀ = 0
```

### A.3. Equivariance of the extrema condition

> If `A` is an extrema of the lagrangian with current density `J`, then the Lorentz transformation
> `Λ • A (Λ⁻¹ • x)` is an extrema of the lagrangian with current density `Λ • J (Λ⁻¹ • x)`.
>
> Combined with `time_deriv_time_deriv_electricField_of_isExtrema`, this shows that
> the speed with which an electromagnetic wave propagates is invariant under Lorentz transformations.

**`Electromagnetism.ElectromagneticPotential.isExtrema_lorentzGroup_apply_iff`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L177).

```lean
lemma isExtrema_lorentzGroup_apply_iff {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d) (hJ : ContDiff ℝ ∞ J)
    (Λ : LorentzGroup d) :
    IsExtrema 𝓕 (Λ • A) (fun x => Λ • J (Λ⁻¹ • x)) ↔
    IsExtrema 𝓕 A J
```

## B. Gauss's law and Ampère's law and the extrema condition

**`Electromagnetism.ElectromagneticPotential.isExtrema_iff_gauss_ampere_magneticFieldMatrix`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L230).

```lean
lemma isExtrema_iff_gauss_ampere_magneticFieldMatrix {d} {𝓕 : FreeSpace}
    {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) :
    IsExtrema 𝓕 A J ↔ ∀ t, ∀ x, (∇ ⬝ (A.electricField 𝓕.c t)) x = J.chargeDensity 𝓕.c t x / 𝓕.ε₀
    ∧ ∀ i, 𝓕.μ₀ * 𝓕.ε₀ * ∂ₜ (fun t => A.electricField 𝓕.c t x) t i =
    ∑ j, ∂[j] (A.magneticFieldMatrix 𝓕.c t · (j, i)) x - 𝓕.μ₀ * J.currentDensity 𝓕.c t x i
```

## C. Time derivatives from the extrema condition

**`Electromagnetism.ElectromagneticPotential.time_deriv_electricField_of_isExtrema`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L281).

```lean
lemma time_deriv_electricField_of_isExtrema {A : ElectromagneticPotential d}
    {𝓕 : FreeSpace}
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d) (hJ : ContDiff ℝ ∞ J)
    (h : IsExtrema 𝓕 A J) (t : Time) (x : Space d) (i : Fin d) :
    ∂ₜ (A.electricField 𝓕.c · x) t i =
      1 / (𝓕.μ₀ * 𝓕.ε₀) * ∑ j, ∂[j] (A.magneticFieldMatrix 𝓕.c t · (j, i)) x -
      (1/ 𝓕.ε₀) * J.currentDensity 𝓕.c t x i
```

## D. Second time derivatives from the extrema condition

### D.1. Second time derivatives of the magnetic field from the extrema condition

> We show that the magnetic field matrix $B_{ij}$ satisfies the following wave-like equation
>
> $$\frac{\partial^2 B_{ij}}{\partial t^2} = c^2 \sum_k \frac{\partial^2 B_{ij}}{\partial x_k^2} +
>   \frac{1}{\epsilon_0} \left(\frac{\partial J_i}{\partial x_j} -
>   \frac{\partial J_j}{\partial x_i} \right).$$
>
> When the free current density is zero, this reduces to the wave equation.

**`Electromagnetism.ElectromagneticPotential.time_deriv_time_deriv_magneticFieldMatrix_of_isExtrema`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L311).

```lean
lemma time_deriv_time_deriv_magneticFieldMatrix_of_isExtrema {A : ElectromagneticPotential d}
    {𝓕 : FreeSpace}
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) (h : IsExtrema 𝓕 A J)
    (t : Time) (x : Space d) (i j : Fin d) :
    ∂ₜ (∂ₜ (A.magneticFieldMatrix 𝓕.c · x (i, j))) t =
    𝓕.c ^ 2 * ∑ k, ∂[k] (∂[k] (A.magneticFieldMatrix 𝓕.c t · (i, j))) x +
    𝓕.ε₀⁻¹ * (∂[j] (J.currentDensity 𝓕.c t · i) x - ∂[i] (J.currentDensity 𝓕.c t · j) x)
```

### D.2. Second time derivatives of the electric field from the extrema condition

> We show that the electric field $E_i$ satisfies the following wave-like equation:
>
> $$\frac{\partial^2 E_{i}}{\partial t^2} = c^2 \sum_k \frac{\partial^2 E_{i}}{\partial x_k^2} -
>   \frac{c ^ 2}{\epsilon_0} \frac{\partial \rho}{\partial x_i} -
>   c ^ 2 μ_0 \frac{\partial J_i}{\partial t}.$$
>
> When the free current density and charge density are zero, this reduces to the wave equation.

**`Electromagnetism.ElectromagneticPotential.time_deriv_time_deriv_electricField_of_isExtrema`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean#L377).

```lean
lemma time_deriv_time_deriv_electricField_of_isExtrema {A : ElectromagneticPotential d}
    {𝓕 : FreeSpace}
    (hA : ContDiff ℝ ∞ A) (J : LorentzCurrentDensity d)
    (hJ : ContDiff ℝ ∞ J) (h : IsExtrema 𝓕 A J)
    (t : Time) (x : Space d) (i : Fin d) :
    ∂ₜ (∂ₜ (A.electricField 𝓕.c · x i)) t =
      𝓕.c ^ 2 * ∑ j, (∂[j] (∂[j] (A.electricField 𝓕.c t · i)) x) -
      𝓕.c ^ 2 / 𝓕.ε₀ * ∂[i] (J.chargeDensity 𝓕.c t ·) x -
      𝓕.c ^ 2 * 𝓕.μ₀ * ∂ₜ (J.currentDensity 𝓕.c · x i) t
```

## Depends on

- [The Lagrangian in electromagnetism](lagrangian.md)

## Sources

- [Physlib/Electromagnetism/Dynamics/IsExtrema.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/IsExtrema.lean)
