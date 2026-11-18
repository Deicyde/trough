---
declaration: module
origin: cited
lean: Cosmology.FLRW.FriedmannEquation.reducedHubble, Cosmology.FLRW.FriedmannEquation.equalityScaleFactorRadiationMatter, Cosmology.FLRW.FriedmannEquation.equalityScaleFactorMatterLambda, Cosmology.FLRW.FriedmannEquation.equalityScaleFactorRadiationMatter_spec, Cosmology.FLRW.FriedmannEquation.equalityScaleFactorMatterLambda_spec, Cosmology.FLRW.FriedmannSolution.sq_hubbleConstant_eq_mul_densityParameters, Cosmology.FLRW.FriedmannSolution.sq_hubbleConstant_eq_reducedHubble, Cosmology.FLRW.FriedmannSolution.hubbleConstant_eq_reducedHubble
statement: formalized
proof: formalized
---

# The reduced Hubble function of the standard cosmological model

The module `Physlib.Cosmology.FLRW.ReducedHubble`, [Physlib/Cosmology/FLRW/ReducedHubble.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean): 8 declarations, 8 with a docstring.

## i. Overview

> The reduced Hubble function of the standard cosmological model is
> `E(x) = √(Ω_Λ + Ω_m x⁻³ + Ω_r x⁻⁴ + Ω_K x⁻²)`, with the density parameters of
> `Physlib.Cosmology.FLRW.DensityParameters` taken at a reference time `t₀`. For an FLRW model
> filled with matter (`ρ ∝ a⁻³`) and radiation (`ρ ∝ a⁻⁴`) that solves the Friedmann equations, the
> Hubble parameter is `H = H₀ E(a / a₀)` with `H₀ = H(t₀) > 0` and `H ≥ 0`. The scaling laws of the
> densities between `t₀` and `t` are hypotheses, not derived here.
>
> The equality scale factors are the values of `x = a / a₀` at which two terms of `E²` are equal:
> radiation and matter at `a_eq = Ω_r / Ω_m`, matter and cosmological constant at
> `a_Λ = (Ω_m / Ω_Λ)^(1/3)`.

## ii. Key results

> - `reducedHubble`: the reduced Hubble function of the standard model.
> - `FLRW.FriedmannSolution.sq_hubbleConstant_eq_mul_densityParameters`: the normalised Friedmann
>   equation `H² = H₀² (Ω_Λ + Ω_m x⁻³ + Ω_r x⁻⁴ + Ω_K x⁻²)` with `x = a / a₀`.
> - `FLRW.FriedmannSolution.sq_hubbleConstant_eq_reducedHubble`,
>   `FLRW.FriedmannSolution.hubbleConstant_eq_reducedHubble`: `H² = H₀² E(a / a₀)²` and
>   `H = H₀ E(a / a₀)`.
> - `equalityScaleFactorRadiationMatter`, `equalityScaleFactorMatterLambda` and the equalities
>   they realise.

## iv. References

> * None.

## A. The reduced Hubble function

**`Cosmology.FLRW.FriedmannEquation.reducedHubble`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L66).

> The reduced Hubble function `E(x) = √(Ω_Λ + Ω_m x⁻³ + Ω_r x⁻⁴ + Ω_K x⁻²)` of the standard
> cosmological model: the Hubble parameter in units of its value `H₀` at the reference time,
> as a function of the scale factor `x = a / a₀` in units of its reference value. The four
> terms are the shares of the cosmological constant, matter, radiation and curvature at the
> reference time, each diluted by its own power of `x`.

```lean
noncomputable def reducedHubble (ΩΛ Ωm Ωr ΩK x : ℝ) : ℝ
```

## B. The equality scale factors

**`Cosmology.FLRW.FriedmannEquation.equalityScaleFactorRadiationMatter`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L77).

> The radiation-matter equality scale factor `a_eq = Ω_r / Ω_m`: the value of `x = a / a₀`
> at which the matter and radiation terms of `E²` are equal; radiation dominates before it.

```lean
noncomputable def equalityScaleFactorRadiationMatter (Ωr Ωm : ℝ) : ℝ
```

**`Cosmology.FLRW.FriedmannEquation.equalityScaleFactorMatterLambda`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L82).

> The matter-Λ equality scale factor `a_Λ = (Ω_m / Ω_Λ)^(1/3)`: the value of `x = a / a₀`
> at which the matter term of `E²` equals `Ω_Λ`; the cosmological constant dominates after
> it.

```lean
noncomputable def equalityScaleFactorMatterLambda (Ωm ΩΛ : ℝ) : ℝ
```

**`Cosmology.FLRW.FriedmannEquation.equalityScaleFactorRadiationMatter_spec`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L85).

> At `a_eq`, the matter and radiation terms of `E²` are equal.

```lean
lemma equalityScaleFactorRadiationMatter_spec {Ωr Ωm : ℝ} (hr : 0 < Ωr) (hm : 0 < Ωm) :
    Ωm * equalityScaleFactorRadiationMatter Ωr Ωm ^ (-3 : ℝ)
      = Ωr * equalityScaleFactorRadiationMatter Ωr Ωm ^ (-4 : ℝ)
```

**`Cosmology.FLRW.FriedmannEquation.equalityScaleFactorMatterLambda_spec`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L97).

> At `a_Λ`, the matter term of `E²` equals `Ω_Λ`.

```lean
lemma equalityScaleFactorMatterLambda_spec {Ωm ΩΛ : ℝ} (hm : 0 < Ωm) (hL : 0 < ΩΛ) :
    Ωm * equalityScaleFactorMatterLambda Ωm ΩΛ ^ (-3 : ℝ) = ΩΛ
```

## C. The Hubble parameter of a solution of the Friedmann equations

**`Cosmology.FLRW.FriedmannSolution.sq_hubbleConstant_eq_mul_densityParameters`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L123).

> For a solution of the Friedmann equations whose density is that of matter plus that of
> radiation, take two times `t` and `t₀` of the interval of the model with `H(t₀) ≠ 0` at which
> `ρ_m(t) = ρ_m(t₀) (a(t₀) / a(t))³` and `ρ_r(t) = ρ_r(t₀) (a(t₀) / a(t))⁴`. Then
> `H² = H₀² (Ω_Λ + Ω_m x⁻³ + Ω_r x⁻⁴ + Ω_K x⁻²)` with `x = a(t) / a(t₀)` and the density
> parameters taken at `t₀`.

```lean
lemma sq_hubbleConstant_eq_mul_densityParameters (h : U.FriedmannSolution F Λ G c)
    (hρ : ∀ s, F.ρ s = Fm.ρ s + Fr.ρ s) {t t₀ : Time} (ht : t ∈ U.I) (ht₀ : t₀ ∈ U.I)
    (hH₀ : hubbleConstant U.a t₀ ≠ 0)
    (hm : Fm.ρ t = Fm.ρ t₀ * (U.a t₀ / U.a t) ^ 3) (hr : Fr.ρ t = Fr.ρ t₀ * (U.a t₀ / U.a t) ^ 4) :
    hubbleConstant U.a t ^ 2 = hubbleConstant U.a t₀ ^ 2
      * (U.lambdaDensityParameter Λ c t₀ + U.densityParameter Fm G t₀ * (U.a t / U.a t₀) ^ (-3 : ℝ)
        + U.densityParameter Fr G t₀ * (U.a t / U.a t₀) ^ (-4 : ℝ)
        + U.curvatureDensityParameter c t₀ * (U.a t / U.a t₀) ^ (-2 : ℝ))
```

**`Cosmology.FLRW.FriedmannSolution.sq_hubbleConstant_eq_reducedHubble`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L153).

> `H² = H₀² E(a / a₀)²`, under the hypotheses of
> `sq_hubbleConstant_eq_mul_densityParameters`.

```lean
lemma sq_hubbleConstant_eq_reducedHubble (h : U.FriedmannSolution F Λ G c)
    (hρ : ∀ s, F.ρ s = Fm.ρ s + Fr.ρ s) {t t₀ : Time} (ht : t ∈ U.I) (ht₀ : t₀ ∈ U.I)
    (hH₀ : hubbleConstant U.a t₀ ≠ 0)
    (hm : Fm.ρ t = Fm.ρ t₀ * (U.a t₀ / U.a t) ^ 3) (hr : Fr.ρ t = Fr.ρ t₀ * (U.a t₀ / U.a t) ^ 4) :
    hubbleConstant U.a t ^ 2 = hubbleConstant U.a t₀ ^ 2
      * reducedHubble (U.lambdaDensityParameter Λ c t₀) (U.densityParameter Fm G t₀)
        (U.densityParameter Fr G t₀) (U.curvatureDensityParameter c t₀) (U.a t / U.a t₀) ^ 2
```

**`Cosmology.FLRW.FriedmannSolution.hubbleConstant_eq_reducedHubble`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean#L175).

> `H = H₀ E(a / a₀)` for `0 < H₀` and `0 ≤ H`, under the hypotheses of
> `sq_hubbleConstant_eq_reducedHubble`.

```lean
lemma hubbleConstant_eq_reducedHubble (h : U.FriedmannSolution F Λ G c)
    (hρ : ∀ s, F.ρ s = Fm.ρ s + Fr.ρ s) {t t₀ : Time} (ht : t ∈ U.I) (ht₀ : t₀ ∈ U.I)
    (hH₀ : 0 < hubbleConstant U.a t₀) (hH : 0 ≤ hubbleConstant U.a t)
    (hm : Fm.ρ t = Fm.ρ t₀ * (U.a t₀ / U.a t) ^ 3) (hr : Fr.ρ t = Fr.ρ t₀ * (U.a t₀ / U.a t) ^ 4) :
    hubbleConstant U.a t = hubbleConstant U.a t₀
      * reducedHubble (U.lambdaDensityParameter Λ c t₀) (U.densityParameter Fm G t₀)
        (U.densityParameter Fr G t₀) (U.curvatureDensityParameter c t₀) (U.a t / U.a t₀)
```

## Depends on

- [Density parameters and the closure relation](densityparameters.md)

## Sources

- [Physlib/Cosmology/FLRW/ReducedHubble.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/ReducedHubble.lean)
