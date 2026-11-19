---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity_eq_distTranslate, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity_chargeDensity, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity_currentDensity, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_eq_distTranslate, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_scalarPotential, Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_vectorPotential
statement: formalized
proof: formalized
---

# Electrostatics of a stationary point particle in 3d

The module `Physlib.Electromagnetism.PointParticle.ThreeDimension`, [Physlib/Electromagnetism/PointParticle/ThreeDimension.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean): 13 declarations, 2 with a docstring.

## i. Overview

> In this module we give the electromagnetic properties of a point particle
> sitting at the origin in 3d space.

## ii. Key results

> - `threeDimPointParticle` : The electromagnetic potential of a point particle
>   stationary at a point in 3d space.
> - `threeDimPointParticle_isExterma` : The electric field of a point
>   particle stationary at a point of 3d space satisfies Maxwell's equations

## iv. References

> * None.

## A. The current density

> The current density of a point particle in 3d space is given by:
>
> $$J(r) = (c q \delta(r - r₀), 0, 0, 0) $$
>
> where $c$ is the speed light, $q$ is the charge of the particle and $r₀$ is the position of the
> particle in 3d space.

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L71).

> The current density of a point particle stationary at a point `r₀`
> of 3d space.

```lean
noncomputable def threeDimPointParticleCurrentDensity (c : SpeedOfLight) (q : ℝ) (r₀ : Space 3) :
    TempDistLorentzCurrentDensity 3
```

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity_eq_distTranslate`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L75).

```lean
lemma threeDimPointParticleCurrentDensity_eq_distTranslate (c : SpeedOfLight) (q : ℝ)
    (r₀ : Space 3) :
    threeDimPointParticleCurrentDensity c q r₀ = ((tempDistTimeSlice c).symm <|
    constantTime <|
    distTranslate (basis.repr r₀) <|
    ((c * q) • diracDelta' ℝ 0 (Lorentz.Vector.basis (Sum.inl 0))))
```

### A.1. The charge density

> The charge density of a point particle in 3d space is given by:
>
> $$ρ(r) = q \delta(r - r₀) $$
>
> where $q$ is the charge of the particle and $r₀$ is the position of the particle in 3d space.

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity_chargeDensity`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L98).

```lean
lemma threeDimPointParticleCurrentDensity_chargeDensity (c : SpeedOfLight) (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticleCurrentDensity c q r₀).chargeDensity c =
    constantTime (q • diracDelta ℝ r₀)
```

### A.2. The 3-current density

> The 3-current density of a point particle in 3d space is given by:
>
> $$\vec J(r) = 0.$$
>
> In other words, there is no current flow for a point particle at rest.

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticleCurrentDensity_currentDensity`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L122).

```lean
lemma threeDimPointParticleCurrentDensity_currentDensity (c : SpeedOfLight) (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticleCurrentDensity c q r₀).currentDensity c = 0
```

## B. The Potentials

### B.1. The electromagnetic potential

> The 4-potential of a point particle in 3d space is given by:
>
> $$A(r) = \frac{q μ₀ c}{4 π |r - r₀|} (1, 0, 0, 0) $$
>
> where $μ₀$ is the permeability of free space, $c$ is the speed of light,
> $q$ is the charge of the particle and $r₀$ is the position of the particle in 3d space.

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L150).

> The electromagnetic potential of a point particle stationary at `r₀`
> of 3d space.

```lean
noncomputable def threeDimPointParticle (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    TempDistElectromagneticPotential 3
```

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_eq_distTranslate`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L156).

```lean
lemma threeDimPointParticle_eq_distTranslate (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    threeDimPointParticle 𝓕 q r₀ = ((tempDistTimeSlice 𝓕.c).symm <|
    constantTime <|
    distTranslate (basis.repr r₀) <|
    distOfFunction (fun x => (((q * 𝓕.μ₀ * 𝓕.c)/ (4 * π))* ‖x‖⁻¹) •
      Lorentz.Vector.basis (Sum.inl 0))
      (((IsDistBounded.inv (by norm_num)).const_mul_fun _).smul_const _))
```

### B.2. The scalar potential

> The first component of the 4-potential is the scalar potential, once
> one has taken account of factors of the speed of light. It is given by:
>
> $$V(r) = \frac{q}{4 π \epsilon_0 |r - r_0|}.$$

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_scalarPotential`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L179).

```lean
lemma threeDimPointParticle_scalarPotential (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticle 𝓕 q r₀).scalarPotential 𝓕.c =
    Space.constantTime (distOfFunction (fun x => (q/ (4 * π * 𝓕.ε₀))• ‖x - r₀‖⁻¹)
      (((IsDistBounded.inv_shift _).const_mul_fun _)))
```

### B.3. The vector potential is zero

> The spatial components of the 4-potential give the vector potential, which is zero
> for a stationary point particle.
>
> $$\vec A(r) = 0.$$

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_vectorPotential`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L210).

```lean
lemma threeDimPointParticle_vectorPotential (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticle 𝓕 q r₀).vectorPotential 𝓕.c = 0
```

## C. The electric field

> The electric field of a point particle in 3d space is given by:
>
> $$\vec E(r) = \frac{q}{4 π \epsilon_0} \frac{\vec r - \vec r₀}{|\vec r - \vec r₀|^3}.$$

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_electricField`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L225).

```lean
lemma threeDimPointParticle_electricField (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticle 𝓕 q r₀).electricField 𝓕.c =
    (q/ (4 * π * 𝓕.ε₀)) • constantTime (distOfFunction (fun x : Space 3 =>
      ‖x - r₀‖ ^ (- 3 : ℤ) • basis.repr (x - r₀))
      ((IsDistBounded.zpow_smul_repr_self (- 3 : ℤ) (by omega)).comp_sub_right r₀))
```

### C.1. the time derivative of the electric field

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_electricField_timeDeriv`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L249).

```lean
lemma threeDimPointParticle_electricField_timeDeriv (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    Space.distTimeDeriv ((threeDimPointParticle 𝓕 q r₀).electricField 𝓕.c) = 0
```

## D. The magnetic field

> Given that the vector potential is zero, the magnetic field is also zero.

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_magneticFieldMatrix`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L263).

```lean
lemma threeDimPointParticle_magneticFieldMatrix (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticle 𝓕 q r₀).magneticFieldMatrix 𝓕.c = 0
```

## E. Maxwell's equations

> The divergence of the electric field of a point particle in 3d space is given by:
>
> $$∇ · \vec E(r) = \frac{1}{\epsilon_0} q \delta(r - r₀).$$
>
> From this, it follows that the electromagnetic potential of a point particle in 3d space
> satisfies Maxwell's equations for a point particle at rest.

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_div_electricField`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L280).

```lean
lemma threeDimPointParticle_div_electricField {𝓕} (q : ℝ) (r₀ : Space 3) :
    distSpaceDiv ((threeDimPointParticle 𝓕 q r₀).electricField 𝓕.c) =
    (1/𝓕.ε₀) • constantTime (q • diracDelta ℝ r₀)
```

**`Electromagnetism.TempDistElectromagneticPotential.threeDimPointParticle_isExterma`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean#L303).

```lean
lemma threeDimPointParticle_isExterma (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 3) :
    (threeDimPointParticle 𝓕 q r₀).IsExtrema 𝓕 (threeDimPointParticleCurrentDensity 𝓕.c q r₀)
```

## Depends on

- [Extrema of the Lagrangian density (TemperedDistributional/Dynamics/IsExtrema)](../tempereddistributional/dynamics-isextrema.md)
- [Translations on space](../../spaceandtime/space/part-01/translations.md)

## Proof depends on

- [The norm on space](../../spaceandtime/space/part-02/norm-basic.md)

## Sources

- [Physlib/Electromagnetism/PointParticle/ThreeDimension.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/ThreeDimension.lean)
