---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.IsExtrema, Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_gradLagrangian, Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_components, Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_space_time, Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_vectorPotential, Electromagnetism.TempDistElectromagneticPotential.isExterma_iff_tensor, Electromagnetism.TempDistElectromagneticPotential.isExterma_equivariant
statement: formalized
proof: formalized
---

# Extrema of the Lagrangian density (TemperedDistributional/Dynamics/IsExtrema)

The module `Physlib.Electromagnetism.TemperedDistributional.Dynamics.IsExtrema`, [Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean): 7 declarations, 1 with a docstring.

## i. Overview

> In this module we define what it means for an electromagnetic potential
> to be an extremum of the Lagrangian density in presence of a Lorentz current density.
>
> This is equivalent to the electromagnetic potential satisfying
> Maxwell's equations with sources, i.e. Gauss's law and Ampère's law.

## ii. Key results

> - `IsExtrema` : The condition on an electromagnetic potential to be an extrema of the lagrangian.

## iv. References

> * None.

## A. Is Extrema condition in the distributional case

> The above results looked at the extrema condition for electromagnetic potentials that are
> functions. We now look at the case where the electromagnetic potential is a distribution.

**`Electromagnetism.TempDistElectromagneticPotential.IsExtrema`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L57).

> The proposition on an electromagnetic potential, corresponding to the statement that
> it is an extrema of the lagrangian.

```lean
def IsExtrema {d} (𝓕 : FreeSpace)
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) : Prop
```

**`Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_gradLagrangian`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L61).

```lean
lemma isExtrema_iff_gradLagrangian {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) :
    IsExtrema 𝓕 A J ↔ A.gradLagrangian 𝓕 J = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_components`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L66).

```lean
lemma isExtrema_iff_components {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) :
    IsExtrema 𝓕 A J ↔ (∀ ε, A.gradLagrangian 𝓕 J ε (Sum.inl 0) = 0)
    ∧ (∀ ε i, A.gradLagrangian 𝓕 J ε (Sum.inr i) = 0)
```

### A.1. IsExtrema and Gauss's law and Ampère's law

> We show that `A` is an extrema of the lagrangian if and only if Gauss's law and Ampère's law hold.
> In other words,
>
> $$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$
>
> and
>
> $$\mu_0 \varepsilon_0 \frac{\partial \mathbf{E}_i}{\partial t} -
>   \sum_j \partial_j \mathbf{B}_{j i} + \mu_0 \mathbf{J}_i = 0.$$
>
> Here $\mathbf{B}$ is the magnetic field matrix.

**`Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_space_time`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L93).

```lean
lemma isExtrema_iff_space_time {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) :
    IsExtrema 𝓕 A J ↔
      (∀ ε, distSpaceDiv (A.electricField 𝓕.c) ε = (1/𝓕.ε₀) * (J.chargeDensity 𝓕.c) ε) ∧
      (∀ ε i, 𝓕.μ₀ * 𝓕.ε₀ * (Space.distTimeDeriv (A.electricField 𝓕.c)) ε i -
      ∑ j, ((PiLp.basisFun 2 ℝ (Fin d)).tensorProduct (PiLp.basisFun 2 ℝ (Fin d))).repr
        ((Space.distSpaceDeriv j (A.magneticFieldMatrix 𝓕.c)) ε) (j, i) +
      𝓕.μ₀ * J.currentDensity 𝓕.c ε i = 0)
```

### A.2. IsExtrema in terms of Vector Potentials

> We show that `A` is an extrema of the lagrangian if and only if Gauss's law and Ampère's law hold.
> In other words,
>
> $$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$
>
> and
>
> $$\mu_0 \varepsilon_0 \frac{\partial \mathbf{E}_i}{\partial t} -
>   \sum_j -(\partial_j \partial_j \vec A_i - \partial_j \partial_i \vec A_j) +
>   \mu_0 \mathbf{J}_i = 0.$$

**`Electromagnetism.TempDistElectromagneticPotential.isExtrema_iff_vectorPotential`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L150).

```lean
lemma isExtrema_iff_vectorPotential {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) :
    IsExtrema 𝓕 A J ↔
      (∀ ε, distSpaceDiv (A.electricField 𝓕.c) ε = (1/𝓕.ε₀) * (J.chargeDensity 𝓕.c) ε) ∧
      (∀ ε i, 𝓕.μ₀ * 𝓕.ε₀ * distTimeDeriv (A.electricField 𝓕.c) ε i -
      (∑ x, -(distSpaceDeriv x (distSpaceDeriv x (A.vectorPotential 𝓕.c)) ε i
        - distSpaceDeriv x (distSpaceDeriv i (A.vectorPotential 𝓕.c)) ε x)) +
      𝓕.μ₀ * J.currentDensity 𝓕.c ε i = 0)
```

### A.3. The extrema condition in terms of tensors

> We show that `A` is an extrema of the lagrangian if and only if the equation
>
> $$\frac{1}{\mu_0} \partial_\kappa F^{\kappa \nu'} - J^{\nu'} = 0,$$
>
> holds.

**`Electromagnetism.TempDistElectromagneticPotential.isExterma_iff_tensor`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L183).

```lean
lemma isExterma_iff_tensor {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) :
    IsExtrema 𝓕 A J ↔ ∀ ε,
    {((1/ 𝓕.μ₀ : ℝ) • distTensorDeriv A.fieldStrength ε | κ κ ν') + - (J ε | ν')}ᵀ = 0
```

### A.4. The invariance of the extrema condition under Lorentz transformations

> We show that the Extrema condition is invariant under Lorentz transformations.
> This implies that if an electromagnetic potential is an extrema in one inertial frame,
> it is also an extrema in any other inertial frame.
> In otherwords that the Maxwell's equations are Lorentz invariant.
> A natural consequence of this is that the speed of light is the same in all inertial frames.

**`Electromagnetism.TempDistElectromagneticPotential.isExterma_equivariant`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean#L222).

```lean
lemma isExterma_equivariant {𝓕 : FreeSpace}
    (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) (Λ : LorentzGroup d) :
    IsExtrema 𝓕 (Λ • A) (Λ • J) ↔ IsExtrema 𝓕 A J
```

## Depends on

- [The Lagrangian in electromagnetism (TemperedDistributional/Dynamics/Lagrangian)](dynamics-lagrangian.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Dynamics/IsExtrema.lean)
