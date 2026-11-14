---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity, Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_chargeDesnity, Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_currentDensity_fst, Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_currentDensity_snd, Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_currentDensity_thrd, Electromagnetism.TempDistElectromagneticPotential.infiniteWire, Electromagnetism.TempDistElectromagneticPotential.infiniteWire_scalarPotential, Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential
statement: formalized
proof: formalized
---

# The magnetic field around a infinite wire

The module `Physlib.Electromagnetism.Current.InfiniteWire`, [Physlib/Electromagnetism/Current/InfiniteWire.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean): 15 declarations, 2 with a docstring.

## i. Overview

> In this module we verify the electromagnetic properties of an infinite wire
> carrying a steady current along the x-axis.

## ii. Key results

> - `wireCurrentDensity` : The current density associated with an infinite wire
>   carrying a current `I` along the `x`-axis.
> - `infiniteWire` : The electromagnetic potential associated with an infinite wire
>   carrying a current `I` along the `x`-axis.
> - `infiniteWire_isExterma` : The electromagnetic potential of an infinite wire
>   carrying a current `I` along the `x`-axis satisfies Maxwell's equations.

## iv. References

> * None.

## A. The current density

> The 4-current density of an infinite wire carrying a current `I` along the `x`-axis is given by
>
> $$J(t, x, y, z) = (0, I δ((y, z)), 0, 0).$$

**`Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L64).

> The current density associated with an infinite wire carrying a current `I`
> along the `x`-axis.

```lean
noncomputable def wireCurrentDensity (c : SpeedOfLight) :
    ℝ →ₗ[ℝ] TempDistLorentzCurrentDensity 3
```

**`Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_chargeDesnity`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L74).

```lean
lemma wireCurrentDensity_chargeDesnity (c : SpeedOfLight) (I : ℝ) :
    (wireCurrentDensity c I).chargeDensity c = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_currentDensity_fst`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L80).

```lean
lemma wireCurrentDensity_currentDensity_fst (c : SpeedOfLight) (I : ℝ)
    (η : 𝓢(Time × Space 3, ℝ)) :
    (wireCurrentDensity c I).currentDensity c η 0 =
    (constantTime <|
    constantSliceDist 0 <|
    I • diracDelta ℝ 0) η
```

**`Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_currentDensity_snd`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L90).

```lean
lemma wireCurrentDensity_currentDensity_snd (c : SpeedOfLight) (I : ℝ)
    (ε : 𝓢(Time × Space 3, ℝ)) :
    (wireCurrentDensity c I).currentDensity c ε 1 = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.wireCurrentDensity_currentDensity_thrd`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L97).

```lean
lemma wireCurrentDensity_currentDensity_thrd (c : SpeedOfLight) (I : ℝ)
    (ε : 𝓢(Time × Space 3, ℝ)) :
    (wireCurrentDensity c I).currentDensity c ε 2 = 0
```

## B. The electromagnetic potential

> The electromagnetic potential of an infinite wire carrying a current `I` along the `x`-axis is
> given by
>
> $$A(t, x, y, z) = \left(0, -\frac{μ_0 I}{2\pi} \log (\sqrt{y^2 + z^2}), 0, 0\right).$$

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L114).

> The electromagnetic potential of an infinite wire along the x-axis carrying a current `I`.

```lean
noncomputable def infiniteWire (𝓕 : FreeSpace) (I : ℝ) :
    TempDistElectromagneticPotential 3
```

### B.1. The scalar potential

> THe scalar potential of an infinite wire carrying a current `I` along the `x`-axis is zero:
>
> $$V(t, x, y, z) = 0.$$

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_scalarPotential`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L134).

```lean
lemma infiniteWire_scalarPotential (𝓕 : FreeSpace) (I : ℝ) :
    (infiniteWire 𝓕 I).scalarPotential 𝓕.c = 0
```

### B.2. The vector potential

> The vector potential of an infinite wire carrying a current `I` along the `x`-axis is given by
>
> $$\vec A(t, x, y, z) = \left(-\frac{μ_0 I}{2\pi} \log (\sqrt{y^2 + z^2}), 0, 0\right).$$
>
> The time derivative $\partial_t \vec A$ is zero, as expected for a steady current,
> and the spatial derivative $\partial_x \vec A$ is also zero, as expected for
> a system with translational symmetry along the x-axis.

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L153).

```lean
lemma infiniteWire_vectorPotential (𝓕 : FreeSpace) (I : ℝ) :
    (infiniteWire 𝓕 I).vectorPotential 𝓕.c =
    (constantTime <|
    constantSliceDist 0
    ((- I * 𝓕.μ₀ / (2 * Real.pi)) • distOfFunction (fun (x : Space 2) =>
      Real.log ‖x‖ • EuclideanSpace.single 0 (1 : ℝ))
    (by apply (IsDistBounded.log_norm (by norm_num)).smul_const)))
```

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential_fst`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L165).

```lean
lemma infiniteWire_vectorPotential_fst (𝓕 : FreeSpace) (I : ℝ)(η : 𝓢(Time × Space 3, ℝ)) :
    (infiniteWire 𝓕 I).vectorPotential 𝓕.c η 0 =
    (constantTime <|
    constantSliceDist 0 <|
    (- I * 𝓕.μ₀ / (2 * Real.pi)) • distOfFunction (fun (x : Space 2) => Real.log ‖x‖)
    (IsDistBounded.log_norm)) η
```

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential_snd`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L175).

```lean
lemma infiniteWire_vectorPotential_snd (𝓕 : FreeSpace) (I : ℝ) :
    (infiniteWire 𝓕 I).vectorPotential 𝓕.c η 1 = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential_thrd`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L181).

```lean
lemma infiniteWire_vectorPotential_thrd (𝓕 : FreeSpace) (I : ℝ) :
    (infiniteWire 𝓕 I).vectorPotential 𝓕.c η 2 = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential_distTimeDeriv`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L187).

```lean
lemma infiniteWire_vectorPotential_distTimeDeriv (𝓕 : FreeSpace) (I : ℝ) :
    distTimeDeriv ((infiniteWire 𝓕 I).vectorPotential 𝓕.c) = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_vectorPotential_distSpaceDeriv_0`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L194).

```lean
lemma infiniteWire_vectorPotential_distSpaceDeriv_0 (𝓕 : FreeSpace) (I : ℝ) :
    distSpaceDeriv 0 ((infiniteWire 𝓕 I).vectorPotential 𝓕.c) = 0
```

## C. The electric field

> The electric field of an infinite wire carrying a current `I` along the `x`-axis is zero:
>
> $$\vec E(t, x, y, z) = 0.$$

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_electricField`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L210).

```lean
lemma infiniteWire_electricField (𝓕 : FreeSpace) (I : ℝ) :
    (infiniteWire 𝓕 I).electricField 𝓕.c = 0
```

## D. Maxwell's equations

**`Electromagnetism.TempDistElectromagneticPotential.infiniteWire_isExterma`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean#L222).

```lean
lemma infiniteWire_isExterma {𝓕 : FreeSpace} {I : ℝ} :
    IsExtrema 𝓕 (infiniteWire 𝓕 I) (wireCurrentDensity 𝓕.c I)
```

## Depends on

- [Extrema of the Lagrangian density (TemperedDistributional/Dynamics/IsExtrema)](../tempereddistributional/dynamics-isextrema.md)
- [Constant slice distributions](../../spaceandtime/space/part-01/constantslicedist.md)

## Proof depends on

- [The norm on space](../../spaceandtime/space/part-02/norm-basic.md)

## Sources

- [Physlib/Electromagnetism/Current/InfiniteWire.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Current/InfiniteWire.lean)
