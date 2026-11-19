---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity_eq_distTranslate, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity_currentDensity, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity_chargeDensity, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_eq_distTranslate, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_vectorPotential, Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_scalarPotential
statement: formalized
proof: formalized
---

# The electrostatics of a stationary point particle in 1d

The module `Physlib.Electromagnetism.PointParticle.OneDimension`, [Physlib/Electromagnetism/PointParticle/OneDimension.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean): 13 declarations, 2 with a docstring.

## i. Overview

> In this module we give the electromagnetic properties of a point particle
> sitting at the origin in 1d space.

## ii. Key results

> - `oneDimPointParticle` : The electromagnetic potential of a point particle
>   stationary at the origin of 1d space.
> - `oneDimPointParticle_isExterma` : The electric field of a point
>   particle stationary at the origin of 1d space satisfies Maxwell's equations

## iv. References

> * None.

## A. The current density

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L62).

> The current density of a point particle stationary at the origin
> of 1d space.

```lean
noncomputable def oneDimPointParticleCurrentDensity (c : SpeedOfLight) (q : ℝ) (r₀ : Space 1) :
    TempDistLorentzCurrentDensity 1
```

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity_eq_distTranslate`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L66).

```lean
lemma oneDimPointParticleCurrentDensity_eq_distTranslate (c : SpeedOfLight) (q : ℝ) (r₀ : Space 1) :
    oneDimPointParticleCurrentDensity c q r₀ = ((tempDistTimeSlice c).symm <|
    constantTime <|
    distTranslate (basis.repr r₀) <|
    ((c * q) • diracDelta' ℝ 0 (Lorentz.Vector.basis (Sum.inl 0))))
```

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity_currentDensity`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L77).

```lean
lemma oneDimPointParticleCurrentDensity_currentDensity (c : SpeedOfLight) (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticleCurrentDensity c q r₀).currentDensity c = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticleCurrentDensity_chargeDensity`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L84).

```lean
lemma oneDimPointParticleCurrentDensity_chargeDensity (c : SpeedOfLight) (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticleCurrentDensity c q r₀).chargeDensity c =
    constantTime (q • diracDelta ℝ r₀)
```

## B. The Potentials

### B.1. The electromagnetic potential

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L110).

> The electromagnetic potential of a point particle stationary at `r₀`
> of 1d space.

```lean
noncomputable def oneDimPointParticle (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    TempDistElectromagneticPotential 1
```

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_eq_distTranslate`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L116).

```lean
lemma oneDimPointParticle_eq_distTranslate (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    oneDimPointParticle 𝓕 q r₀ = ((tempDistTimeSlice 𝓕.c).symm <|
    constantTime <|
    distTranslate (basis.repr r₀) <|
    distOfFunction (fun x => ((- (q * 𝓕.μ₀ * 𝓕.c)/ 2) * ‖x‖) • Lorentz.Vector.basis (Sum.inl 0))
      (by fun_prop))
```

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_vectorPotential`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L134).

```lean
lemma oneDimPointParticle_vectorPotential (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticle 𝓕 q r₀).vectorPotential 𝓕.c = 0
```

### B.3. The scalar potential

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_scalarPotential`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L146).

```lean
lemma oneDimPointParticle_scalarPotential (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticle 𝓕 q r₀).scalarPotential 𝓕.c =
    Space.constantTime (distOfFunction (fun x =>
      - ((q * 𝓕.μ₀ * 𝓕.c ^ 2)/(2)) • ‖x-r₀‖) (by fun_prop))
```

## C. The electric field

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_electricField`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L169).

```lean
lemma oneDimPointParticle_electricField (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticle 𝓕 q r₀).electricField 𝓕.c =
    ((q * 𝓕.μ₀ * 𝓕.c ^ 2) / 2) • constantTime (distOfFunction (fun x : Space 1 =>
      ‖x - r₀‖ ^ (- 1 : ℤ) • basis.repr (x - r₀))
      ((IsDistBounded.zpow_smul_repr_self (- 1 : ℤ) (by omega)).comp_sub_right r₀))
```

### C.1. The time derivative of the electric field

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_electricField_timeDeriv`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L195).

```lean
lemma oneDimPointParticle_electricField_timeDeriv (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    Space.distTimeDeriv ((oneDimPointParticle 𝓕 q r₀).electricField 𝓕.c) = 0
```

## D. The magnetic field

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_magneticFieldMatrix`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L206).

```lean
lemma oneDimPointParticle_magneticFieldMatrix (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticle 𝓕 q r₀).magneticFieldMatrix 𝓕.c = 0
```

## E. Maxwell's equations

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_div_electricField`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L216).

```lean
lemma oneDimPointParticle_div_electricField {𝓕} (q : ℝ) (r₀ : Space 1) :
    distSpaceDiv ((oneDimPointParticle 𝓕 q r₀).electricField 𝓕.c) =
    (𝓕.μ₀ * 𝓕.c ^ 2) • constantTime (q • diracDelta ℝ r₀)
```

**`Electromagnetism.TempDistElectromagneticPotential.oneDimPointParticle_isExterma`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean#L245).

```lean
lemma oneDimPointParticle_isExterma (𝓕 : FreeSpace) (q : ℝ) (r₀ : Space 1) :
    (oneDimPointParticle 𝓕 q r₀).IsExtrema 𝓕 (oneDimPointParticleCurrentDensity 𝓕.c q r₀)
```

## Depends on

- [Extrema of the Lagrangian density (TemperedDistributional/Dynamics/IsExtrema)](../tempereddistributional/dynamics-isextrema.md)
- [Translations on space](../../spaceandtime/space/part-01/translations.md)

## Proof depends on

- [The norm on space](../../spaceandtime/space/part-02/norm-basic.md)

## Sources

- [Physlib/Electromagnetism/PointParticle/OneDimension.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/Electromagnetism/PointParticle/OneDimension.lean)
