---
declaration: module
origin: cited
lean: Cosmology.FLRW.criticalDensity, Cosmology.FLRW.densityParameter, Cosmology.FLRW.curvatureDensityParameter, Cosmology.FLRW.lambdaDensityParameter, Cosmology.FLRW.lambdaDensityParameter_eq_densityParameter, Cosmology.FLRW.densityParameter_addCosmologicalConstant, Cosmology.FLRW.FriedmannSolution.densityParameter_add_lambda_add_curvature, Cosmology.FLRW.FriedmannSolution.densityParameter_add_curvature
statement: formalized
proof: formalized
---

# Density parameters and the closure relation

The module `Physlib.Cosmology.FLRW.DensityParameters`, [Physlib/Cosmology/FLRW/DensityParameters.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean): 8 declarations, 8 with a docstring.

## i. Overview

> The first-order Friedmann equation of `Physlib.Cosmology.FLRW.Basic`,
> `H² = (8 π G / 3) ρ - k c² / a² + Λ c² / 3`, can be read as a budget for the expansion rate `H`.
>
> The critical density `ρ_cr = 3 H² / (8 π G)` is the density for which this equation holds with
> `k = 0` and `Λ = 0`. When `Λ = 0`, a universe denser than `ρ_cr` is spatially closed (`k > 0`), a
> less dense one is open (`k < 0`), and one at exactly `ρ_cr` is flat.
>
> Measuring each term in units of `ρ_cr` gives the density parameter `Ω = ρ / ρ_cr` of a fluid, the
> density parameter `Ω_Λ = Λ c² / (3 H²)` of the cosmological constant and the curvature density
> parameter `Ω_K = - k c² / (H² a²)`. Dividing the Friedmann equation by `H²` gives the closure
> relation `Ω + Ω_Λ + Ω_K = 1`.
>
> These quantities are defined for an FLRW model. For a solution of the Friedmann equations, the
> closure relation holds at every time of the interval of the model at which `H ≠ 0`.
>
> The reduced Hubble function of the standard cosmological model is in
> `Physlib.Cosmology.FLRW.ReducedHubble`, and the age of the universe in
> `Physlib.Cosmology.FLRW.Age`.

## ii. Key results

> - `FLRW.criticalDensity`, `FLRW.densityParameter`, `FLRW.curvatureDensityParameter`,
>   `FLRW.lambdaDensityParameter`: the critical density and the density parameters of an FLRW
>   model.
> - `FLRW.lambdaDensityParameter_eq_densityParameter`,
>   `FLRW.densityParameter_addCosmologicalConstant`: `Ω_Λ` is the density parameter of the
>   cosmological constant as a fluid.
> - `FLRW.FriedmannSolution.densityParameter_add_lambda_add_curvature`,
>   `FLRW.FriedmannSolution.densityParameter_add_curvature`: the closure relations
>   `Ω + Ω_Λ + Ω_K = 1` and, for `Λ = 0`, `Ω + Ω_K = 1`.

## A. The critical density and the density parameters

> With the convention `x / 0 = 0`, these quantities vanish when `H = 0` or `G = 0`. They have their
> physical meaning at the times at which `H ≠ 0`.

**`Cosmology.FLRW.criticalDensity`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L73).

> The critical density `ρ_cr = 3 H² / (8 π G)` of an FLRW model at time `t`, where `H` is the
> Hubble parameter of its scale factor. It is the density of a spatially flat universe without
> cosmological constant expanding at the rate `H`.

```lean
noncomputable def criticalDensity (G : ℝ) (t : Time) : ℝ
```

**`Cosmology.FLRW.densityParameter`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L77).

> The density parameter `Ω = ρ / ρ_cr` of a cosmic fluid in an FLRW model.

```lean
noncomputable def densityParameter (F : CosmicFluid) (G : ℝ) (t : Time) : ℝ
```

**`Cosmology.FLRW.curvatureDensityParameter`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L83).

> The curvature density parameter `Ω_K = - k c² / (H² a²)` of an FLRW model, where `k` is the
> curvature parameter of its spatial geometry. When `H` and `a` are nonzero, it is positive for a
> saddle geometry, negative for a spherical one and zero for the flat one.

```lean
noncomputable def curvatureDensityParameter (c : SpeedOfLight) (t : Time) : ℝ
```

**`Cosmology.FLRW.lambdaDensityParameter`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L88).

> The density parameter `Ω_Λ = Λ c² / (3 H²)` of the cosmological constant in an FLRW
> model.

```lean
noncomputable def lambdaDensityParameter (Λ : ℝ) (c : SpeedOfLight) (t : Time) : ℝ
```

**`Cosmology.FLRW.lambdaDensityParameter_eq_densityParameter`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L93).

> For `G ≠ 0`, `Ω_Λ` is the density parameter of the empty fluid with the cosmological constant
> folded in.

```lean
lemma lambdaDensityParameter_eq_densityParameter {Λ G : ℝ} {c : SpeedOfLight} (hG : G ≠ 0)
    (t : Time) :
    U.lambdaDensityParameter Λ c t
      = U.densityParameter (CosmicFluid.empty.addCosmologicalConstant Λ G c) G t
```

**`Cosmology.FLRW.densityParameter_addCosmologicalConstant`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L104).

> For `G ≠ 0`, folding the cosmological constant into a cosmic fluid adds `Ω_Λ` to its
> density parameter.

```lean
lemma densityParameter_addCosmologicalConstant (F : CosmicFluid) {Λ G : ℝ} {c : SpeedOfLight}
    (hG : G ≠ 0) (t : Time) :
    U.densityParameter (F.addCosmologicalConstant Λ G c) G t
      = U.densityParameter F G t + U.lambdaDensityParameter Λ c t
```

## B. The closure relation

**`Cosmology.FLRW.FriedmannSolution.densityParameter_add_lambda_add_curvature`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L124).

> The closure relation `Ω + Ω_Λ + Ω_K = 1` for a solution of the Friedmann equations, at the
> times of the interval of the model at which `H ≠ 0`.

```lean
lemma densityParameter_add_lambda_add_curvature (h : U.FriedmannSolution F Λ G c) {t : Time}
    (ht : t ∈ U.I) (hH : hubbleConstant U.a t ≠ 0) :
    U.densityParameter F G t + U.lambdaDensityParameter Λ c t
      + U.curvatureDensityParameter c t = 1
```

**`Cosmology.FLRW.FriedmannSolution.densityParameter_add_curvature`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean#L145).

> The closure relation `Ω + Ω_K = 1` for a solution of the Friedmann equations without
> cosmological constant, at the times of the interval of the model at which `H ≠ 0`.

```lean
lemma densityParameter_add_curvature (h : U.FriedmannSolution F 0 G c) {t : Time} (ht : t ∈ U.I)
    (hH : hubbleConstant U.a t ≠ 0) :
    U.densityParameter F G t + U.curvatureDensityParameter c t = 1
```

## Depends on

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)

## Sources

- [Physlib/Cosmology/FLRW/DensityParameters.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DensityParameters.lean)
