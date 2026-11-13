---
declaration: module
origin: cited
lean: KleinGordon.continuous_wavePropagator, KleinGordon.fourier_wavePropagator, KleinGordon.sineEvolution_zero_mass_three, KleinGordon.solution_zero_mass_three, KleinGordon.wavePropagator_radial
statement: formalized
proof: formalized
---

# Kirchhoff's formula for the massless retarded solution in three dimensions

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.ClosedForm.MasslessSpace`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean): 5 declarations, 5 with a docstring.

> The massless sine evolution in three space dimensions is Kirchhoff's spherical mean.

## i. Overview

> The Fourier multiplier of the sphere mean is `sin (2π |ξ| t) / (2π |ξ|)`. This is the multiplier
> of the massless sine evolution. Fourier inversion identifies the two operators on Schwartz
> functions. The Duhamel integral of the sphere means is the retarded solution. This is the kernel
> `δ(t - r) / (4π r)`.
>
> The sphere integrals and their Fourier transform are taken from the worktree
> `causal-green-operators` (`FieldTheory/Wave/Kirchhoff` and `FieldTheory/Wave/Proofs/Fourier`).

## ii. Key results

> - `fourier_wavePropagator` : the transform of the Kirchhoff propagator.
> - `sineEvolution_zero_mass_three` : the massless sine evolution is the Kirchhoff propagator.
> - `solution_zero_mass_three` : the massless retarded solution is the Duhamel integral of the
>   spherical means.

## iv. References

> None.

## A. The sine evolution

> - `continuous_wavePropagator` : the Kirchhoff propagator of a Schwartz function is continuous.
> - `fourier_wavePropagator` : the transform of the Kirchhoff propagator.
> - `sineEvolution_zero_mass_three` : the massless sine evolution is the Kirchhoff propagator.

## B. The retarded solution

> - `solution_zero_mass_three` : the massless retarded solution is the Duhamel integral of the
>   spherical means.

**`KleinGordon.continuous_wavePropagator`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean#L65).

> The wave propagator of a Schwartz function is continuous.

```lean
lemma continuous_wavePropagator (g : 𝓢(Space 3, ℂ)) (t : ℝ) :
    Continuous (wavePropagator 1 t g)
```

**`KleinGordon.fourier_wavePropagator`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean#L80).

> **Kirchhoff's formula in Fourier space.** The Fourier transform of the wave propagator is
> the multiplier of the massless sine evolution times the transform of the data.

```lean
lemma fourier_wavePropagator (g : 𝓢(Space 3, ℂ)) (t : ℝ) {ξ : Space 3} (hξ : ξ ≠ 0) :
    𝓕 (wavePropagator 1 t g) ξ = multiplier t 0 ξ * 𝓕 g ξ
```

**`KleinGordon.sineEvolution_zero_mass_three`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean#L102).

> **The massless sine evolution is Kirchhoff's propagator.** In three space dimensions the
> massless sine evolution of a Schwartz function is the spherical mean `t M_t g`.

```lean
lemma sineEvolution_zero_mass_three (t : ℝ) (g : 𝓢(Space 3, ℂ)) (x : Space 3) :
    sineEvolution ℂ t 0 g x = wavePropagator 1 t g x
```

**`KleinGordon.solution_zero_mass_three`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean#L131).

> **Kirchhoff's formula for the retarded solution.** The massless retarded solution in three
> space dimensions is the Duhamel integral of the spherical means of the source over the earlier
> times. This is the retarded Green function `δ(t - r) / (4π r)`.

```lean
lemma solution_zero_mass_three (ψ : TestFunction (⊤ : Opens (ℝ × Space 3)) ℂ ⊤) (t : ℝ)
    (x : Space 3) :
    solution ℂ ψ 0 t x = ∫ s in Set.Iic t, wavePropagator 1 (t - s) (slice ℂ ψ s) x
```

**`KleinGordon.wavePropagator_radial`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean#L139).

> The Kirchhoff propagator at the origin of a radial function is the radius times its value.

```lean
lemma wavePropagator_radial {Φ : ℝ → ℂ} {g : Space 3 → ℂ} (hg : ∀ x, g x = Φ ‖x‖) {τ : ℝ}
    (hτ : 0 ≤ τ) : wavePropagator 1 τ g 0 = τ * Φ τ
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)
- [Waves propagating along spheres](../../waveequation/kirchhoff-setting.md)

## Proof depends on

- [Properties of the wave propagator](../../waveequation/kirchhoff-propagator.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/ClosedForm/MasslessSpace.lean)
