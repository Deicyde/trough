---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential.continuityEquation, Space.distTimeDeriv_distSpaceDiv, Space.exists_schwartz_eq_comp_ray, Space.integral_Ioi_fderiv_ray, Space.integral_Ioi_fderiv_ray_basis, Space.timeIntegralSchwartz_fderiv_space, Space.exists_integral_time_ne_zero, Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction
statement: formalized
proof: formalized
---

# Junctions of thin wires

The module `PhyslibAlpha.Electromagnetism.TemperedDistributional.WireJunction`, [PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean): 10 declarations, 9 with a docstring, 1 listed as significant.

## i. Overview

> Let `A` be a distributional electromagnetic potential and `J` a distributional Lorentz current
> density such that Maxwell's equations hold, `IsExtrema 𝓕 A J`. Taking the divergence of
> Ampère's law and using Gauss's law gives the continuity equation `∂ₜ ρ + ∇ ⬝ J = 0` as an
> equation of distributions.
>
> Distributions allow currents to be carried by thin wires. A junction is modelled by finitely
> many straight, semi-infinite wires leaving the origin in the directions `u k`, carrying steady
> currents `I k`. The divergence of such a current density is `(∑ k, I k) δ₀`: the wires end at
> the origin, where the currents must come from somewhere. If no charge accumulates, the
> continuity equation forces `∑ k, I k = 0`.
>
> This is motivated by Kirchhoff's current law, of which it is a special case: a single node with
> steady currents, rather than the branch currents at every node of a lumped-element circuit.

## ii. Key results

> - `Electromagnetism.TempDistElectromagneticPotential.continuityEquation` : the continuity equation
>   for distributions.
> - `Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction` : the current density of a
>   junction of thin wires.
> - `Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction.distSpaceDiv_currentDensity` : the
>   divergence of the current density of a junction.
> - `Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction.sum_currents_eq_zero` : the
>   currents leaving a junction of thin wires sum to zero.

## iv. References

> * None.

## A. Analysis on `Space`

### A.1. Time derivatives and the divergence of distributions

**`Space.distTimeDeriv_distSpaceDiv`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L73).

> The divergence and the time derivative of distributions commute.

```lean
lemma distTimeDeriv_distSpaceDiv {d} (f : (Time × Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) :
    distTimeDeriv (distSpaceDiv f) = distSpaceDiv (distTimeDeriv f)
```

### A.2. Schwartz functions along a ray

> The ray from the origin in the direction `w` is parametrized by `s ↦ s • w`.

**`Space.exists_schwartz_eq_comp_ray`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L90).

> The restriction of a Schwartz function to a line through the origin is a Schwartz
> function.

```lean
lemma exists_schwartz_eq_comp_ray {d} (χ : 𝓢(Space d, ℝ)) {w : Space d} (hw : w ≠ 0) :
    ∃ g : 𝓢(ℝ, ℝ), ∀ s : ℝ, g s = χ (s • w)
```

**`Space.integral_Ioi_fderiv_ray`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L100).

> The fundamental theorem of calculus along the ray in direction `w`.

```lean
lemma integral_Ioi_fderiv_ray {d} (ψ : 𝓢(Space d, ℝ)) {w : Space d} (hw : w ≠ 0) :
    ∫ s in Ioi (0 : ℝ), fderiv ℝ ψ (s • w) w = - ψ 0
```

**`Space.integral_Ioi_fderiv_ray_basis`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L115).

```lean
lemma integral_Ioi_fderiv_ray_basis {d} (ψ : 𝓢(Space d, ℝ)) {u : EuclideanSpace ℝ (Fin d)}
    (hu : u ≠ 0) :
    ∑ i, (∫ s in Ioi (0 : ℝ), fderiv ℝ ψ (s • basis.repr.symm u) (basis i)) * u i = - ψ 0
```

### A.3. Integrating test functions over time

**`Space.timeIntegralSchwartz_fderiv_space`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L139).

> Integrating over time commutes with differentiating in space.

```lean
lemma timeIntegralSchwartz_fderiv_space {d} (η : 𝓢(Time × Space d, ℝ)) (i : Fin d)
    (x : Space d) :
    timeIntegralSchwartz (SchwartzMap.evalCLM ℝ (Time × Space d) ℝ (0, basis i)
      (fderivCLM ℝ (Time × Space d) ℝ η)) x = fderiv ℝ (timeIntegralSchwartz η) x (basis i)
```

**`Space.exists_integral_time_ne_zero`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L149).

> Some test function has a non-zero time integral at the origin.

```lean
lemma exists_integral_time_ne_zero {d} :
    ∃ η : 𝓢(Time × Space d, ℝ), ∫ t, η (t, 0) ≠ 0
```

## B. The continuity equation

**`Electromagnetism.TempDistElectromagneticPotential.continuityEquation`**, a theorem, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L176). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The continuity equation for distributions: Maxwell's equations imply local conservation of
> charge.

```lean
theorem continuityEquation {d} {𝓕 : FreeSpace} (A : TempDistElectromagneticPotential d)
    (J : TempDistLorentzCurrentDensity d) (h : IsExtrema 𝓕 A J) (ε : 𝓢(Time × Space d, ℝ)) :
    distTimeDeriv (J.chargeDensity 𝓕.c) ε + distSpaceDiv (J.currentDensity 𝓕.c) ε = 0
```

## C. Junctions of thin wires

### C.1. The current density of a junction

> The `k`-th wire is the ray `s ↦ s • u k`, `s > 0`. A current `I k` along it has current density
> `I k` times the unit tangent times the arc-length measure on the ray; in the parameter `s` this is
> `I k • u k` times the Lebesgue measure, whatever the length of `u k`. The currents are steady, so
> the pairing with a test function `η` only sees its time integral.

**`Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L232).

> The current density of `J` is that of steady currents `I k` flowing away from the origin
> along thin, straight, semi-infinite wires in the directions `u k`.

```lean
def IsWireJunction {d} (c : SpeedOfLight) (J : TempDistLorentzCurrentDensity d) {ι : Type}
    [Fintype ι] (u : ι → EuclideanSpace ℝ (Fin d)) (I : ι → ℝ) : Prop
```

**`Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction.distSpaceDiv_currentDensity`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L239).

> The wires of a junction meet at the origin, where they act as a source of strength the
> total current leaving along them.

```lean
lemma IsWireJunction.distSpaceDiv_currentDensity {d} {c : SpeedOfLight}
    {J : TempDistLorentzCurrentDensity d} {ι : Type} [Fintype ι] {u : ι → EuclideanSpace ℝ (Fin d)}
    {I : ι → ℝ} (hJ : J.IsWireJunction c u I) (hu : ∀ k, u k ≠ 0) (η : 𝓢(Time × Space d, ℝ)) :
    distSpaceDiv (J.currentDensity c) η = (∑ k, I k) * ∫ t, η (t, 0)
```

### C.2. The currents at a junction sum to zero

**`Electromagnetism.TempDistLorentzCurrentDensity.IsWireJunction.sum_currents_eq_zero`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean#L263).

> If Maxwell's equations hold and no charge accumulates, the steady currents leaving a junction
> of thin wires sum to zero. This is motivated by Kirchhoff's current law, of which it is the
> special case of a single node.

```lean
lemma IsWireJunction.sum_currents_eq_zero {d} {𝓕 : FreeSpace} {J : TempDistLorentzCurrentDensity d}
    {ι : Type} [Fintype ι] {u : ι → EuclideanSpace ℝ (Fin d)} {I : ι → ℝ}
    (hJ : J.IsWireJunction 𝓕.c u I) (hu : ∀ k, u k ≠ 0) (A : TempDistElectromagneticPotential d)
    (h : TempDistElectromagneticPotential.IsExtrema 𝓕 A J)
    (hρ : distTimeDeriv (J.chargeDensity 𝓕.c) = 0) :
    ∑ k, I k = 0
```

## Depends on

- [Extrema of the Lagrangian density (TemperedDistributional/Dynamics/IsExtrema)](../../../physlib/electromagnetism/tempereddistributional/dynamics-isextrema.md)

## Sources

- [PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Electromagnetism/TemperedDistributional/WireJunction.lean)
