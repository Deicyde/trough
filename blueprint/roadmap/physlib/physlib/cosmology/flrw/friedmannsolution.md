---
declaration: module
origin: cited
lean: Cosmology.FLRW.friedmannSolution_iff_addCosmologicalConstant, Cosmology.FLRW.FriedmannSolution.deriv_deriv_scaleFactor_pos_iff, Cosmology.FLRW.FriedmannSolution.deriv_deriv_scaleFactor_pos_iff_lambda, Cosmology.FLRW.FriedmannSolution.decelerationParameter_eq_sum, Cosmology.FLRW.FriedmannSolution.decelerationParameter_lambdaCDM, Cosmology.FLRW.FriedmannSolution.deriv_scaleFactor_ne_zero, Cosmology.FLRW.FriedmannSolution.deriv_scaleFactor_pos, Cosmology.FLRW.FriedmannSolution.deriv_deriv_scaleFactor_nonpos
statement: formalized
proof: formalized
---

# Solutions of the Friedmann equations: dynamical criteria

The module `Physlib.Cosmology.FLRW.FriedmannSolution`, [Physlib/Cosmology/FLRW/FriedmannSolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean): 10 declarations, 10 with a docstring.

## i. Overview

> Qualitative consequences of the Friedmann equations for an FLRW model `U : FLRW` filled with a
> cosmic fluid `F : CosmicFluid` that solves them, `U.FriedmannSolution F Λ G c`. The proposition
> `FLRW.FriedmannSolution` itself is defined in `Physlib.Cosmology.FLRW.Basic`, together with the
> tangent-line bound for a decelerating FLRW model, which does not use the Friedmann equations; the
> continuity equation (`Physlib.Cosmology.FLRW.MatterContent`) and the density parameters, which
> are used here, are stated about it. The energy conditions of the cosmic fluid are in
> `Physlib.Cosmology.FLRW.EnergyConditions`. On the interval `U.I` of the model: a solution with
> cosmological constant `Λ` is a solution without it for the fluid with `Λ` folded in; the
> expansion accelerates if and only if the fluid, with the cosmological constant folded in as a
> `w = -1` component, violates the strong energy condition; the deceleration parameter is
> `q = ½ Σ_x Ω_x (1 + 3 w_x)` for a finite family of barotropic fluids, and
> `q = ½ (Ω_m + 2 Ω_r - 2 Ω_Λ)` for ΛCDM; with a spatial geometry of non-positive curvature,
> positive density and `0 ≤ Λ`, the derivative `∂ₜ a` of the scale factor does not vanish, so that
> a model expanding at one time of `U.I` expands at all times of `U.I`. Finally, with `0 ≤ ρ`,
> `0 ≤ p` and `Λ = 0` the scale factor decelerates on `U.I`, so that a model expanding at
> `t₀ ∈ U.I` cannot be defined at any time earlier than `t₀ - 1 / H(t₀)`: its interval of time is
> bounded below, the Big Bang being at most `1 / H(t₀)` in the past. The de Sitter model of
> `Physlib.Cosmology.FLRW.DeSitter`, with `0 < Λ`, is defined at all times.

## ii. Key results

> - `FLRW.friedmannSolution_iff_addCosmologicalConstant`: a solution with `Λ` is a solution
>   without `Λ` for the fluid `F.addCosmologicalConstant Λ G c`.
> - `FLRW.FriedmannSolution.deriv_deriv_scaleFactor_pos_iff`: `0 < ∂ₜ ∂ₜ a ↔ ρ + 3 p / c² < 0`
>   (`Λ = 0`); `FLRW.FriedmannSolution.deriv_deriv_scaleFactor_pos_iff_lambda`: the same for the
>   total fluid with `Λ` folded in.
> - `FLRW.FriedmannSolution.decelerationParameter_eq_sum`: `q = ½ Σ_i Ω_i (1 + 3 w_i)`;
>   `FLRW.FriedmannSolution.decelerationParameter_lambdaCDM`: `q = ½ (Ω_m + 2 Ω_r - 2 Ω_Λ)`.
> - `FLRW.FriedmannSolution.deriv_scaleFactor_ne_zero`,
>   `FLRW.FriedmannSolution.deriv_scaleFactor_pos`: eternal expansion for a non-positive curvature.
> - `FLRW.FriedmannSolution.deriv_deriv_scaleFactor_nonpos`,
>   `FLRW.FriedmannSolution.lt_of_mem_I`, `FLRW.FriedmannSolution.bddBelow_I`: the Big-Bang bound.

## iv. References

> * None.

## A. The cosmological constant folded into the cosmic fluid

**`Cosmology.FLRW.friedmannSolution_iff_addCosmologicalConstant`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L78).

> An FLRW model filled with the cosmic fluid `F` solves the Friedmann equations with the
> cosmological constant `Λ` if and only if it solves them without cosmological constant for the
> fluid `F` with `Λ` folded in.

```lean
lemma _root_.Cosmology.FLRW.friedmannSolution_iff_addCosmologicalConstant {U : FLRW}
    {F : CosmicFluid} {Λ G : ℝ} {c : SpeedOfLight} (hG : G ≠ 0) :
    U.FriedmannSolution F Λ G c ↔ U.FriedmannSolution (F.addCosmologicalConstant Λ G c) 0 G c
```

## B. Accelerated expansion and the strong energy condition

**`Cosmology.FLRW.FriedmannSolution.deriv_deriv_scaleFactor_pos_iff`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L98).

> On the interval of a solution without cosmological constant, the second derivative
> `∂ₜ ∂ₜ a` of the scale factor is positive (the expansion accelerates) if and only if
> `ρ + 3 p / c² < 0`, that is, if and only if the strong energy condition of the cosmic fluid
> fails through its second inequality.

```lean
lemma deriv_deriv_scaleFactor_pos_iff (h : U.FriedmannSolution F 0 G c) (hG : 0 < G) {t : Time}
    (ht : t ∈ U.I) : 0 < ∂ₜ (∂ₜ U.a) t ↔ F.ρ t + 3 * F.p t / (c : ℝ) ^ 2 < 0
```

**`Cosmology.FLRW.FriedmannSolution.deriv_deriv_scaleFactor_pos_iff_lambda`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L118).

> With cosmological constant `Λ`, on the interval of a solution, `∂ₜ ∂ₜ a` is positive if and
> only if the total fluid, `Λ` folded in as the `w = -1` component, violates
> `0 ≤ ρ + 3 p / c²`.

```lean
lemma deriv_deriv_scaleFactor_pos_iff_lambda (h : U.FriedmannSolution F Λ G c) (hG : 0 < G)
    {t : Time} (ht : t ∈ U.I) :
    0 < ∂ₜ (∂ₜ U.a) t ↔ (F.ρ t + cosmologicalConstantDensity Λ G c)
      + 3 * (F.p t + cosmologicalConstantPressure Λ G c) / (c : ℝ) ^ 2 < 0
```

## C. The deceleration parameter in terms of the density parameters

**`Cosmology.FLRW.FriedmannSolution.decelerationParameter_eq_sum`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L135).

> For a solution of the Friedmann equations without cosmological constant whose cosmic fluid is
> a sum of barotropic components of pressure `w_i ρ_i c²`, the deceleration parameter is
> `q = ½ Σ_i Ω_i (1 + 3 w_i)` at the times of the interval of the model at which `H ≠ 0`, for
> `G ≠ 0`.

```lean
lemma decelerationParameter_eq_sum {n : ℕ} {Fi : Fin n → CosmicFluid} {w : Fin n → ℝ}
    (h : U.FriedmannSolution F 0 G c) (hG : G ≠ 0) (hρ : ∀ s, F.ρ s = ∑ i, (Fi i).ρ s)
    (hp : ∀ s, F.p s = ∑ i, (Fi i).p s) (hw : ∀ i, (Fi i).p = barotropicPressure (w i) (Fi i).ρ c)
    {t : Time} (ht : t ∈ U.I) (hH : hubbleConstant U.a t ≠ 0) :
    decelerationParameter U.a t
      = 1 / 2 * ∑ i, U.densityParameter (Fi i) G t * (1 + 3 * w i)
```

**`Cosmology.FLRW.FriedmannSolution.decelerationParameter_lambdaCDM`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L173).

> For a solution of the Friedmann equations whose cosmic fluid is the sum of matter (zero
> pressure) and radiation (pressure `ρ_r c² / 3`), the deceleration parameter is
> `q = ½ (Ω_m + 2 Ω_r - 2 Ω_Λ)` at the times of the interval of the model (the ΛCDM case).

```lean
lemma decelerationParameter_lambdaCDM {Fm Fr : CosmicFluid} (h : U.FriedmannSolution F Λ G c)
    (hρ : ∀ s, F.ρ s = Fm.ρ s + Fr.ρ s) (hp : ∀ s, F.p s = Fm.p s + Fr.p s)
    (hm : Fm.p = barotropicPressure 0 Fm.ρ c) (hr : Fr.p = barotropicPressure (1 / 3) Fr.ρ c)
    {t : Time} (ht : t ∈ U.I) :
    decelerationParameter U.a t = 1 / 2 * (U.densityParameter Fm G t
      + 2 * U.densityParameter Fr G t - 2 * U.lambdaDensityParameter Λ c t)
```

## D. Eternal expansion

**`Cosmology.FLRW.FriedmannSolution.deriv_scaleFactor_ne_zero`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L205).

> For a spatial geometry of non-positive curvature parameter, `0 ≤ Λ` and a positive density
> at a time `t` of the interval, the first-order Friedmann equation forces `0 < H²` at `t`:
> the derivative `∂ₜ a` of the scale factor does not vanish at `t`.

```lean
lemma deriv_scaleFactor_ne_zero (h : U.FriedmannSolution F Λ G c)
    (hk : U.geometry.curvature ≤ 0) (hΛ : 0 ≤ Λ) (hG : 0 < G) {t : Time} (ht : t ∈ U.I)
    (hρ : 0 < F.ρ t) : ∂ₜ U.a t ≠ 0
```

**`Cosmology.FLRW.FriedmannSolution.deriv_scaleFactor_pos`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L226).

> If moreover the density is positive on the interval and the model expands at one time `t₀`
> of `U.I`, it expands at all times of `U.I`: with a non-positive curvature parameter, `0 ≤ Λ`
> and a positive density, an expanding model expands forever.

```lean
lemma deriv_scaleFactor_pos (h : U.FriedmannSolution F Λ G c) (hk : U.geometry.curvature ≤ 0)
    (hΛ : 0 ≤ Λ) (hG : 0 < G) (hρ : ∀ s ∈ U.I, 0 < F.ρ s) {t₀ : Time} (ht₀ : t₀ ∈ U.I)
    (h0 : 0 < ∂ₜ U.a t₀) {t : Time} (ht : t ∈ U.I) : 0 < ∂ₜ U.a t
```

## E. The Big-Bang bound for a solution of the Friedmann equations

**`Cosmology.FLRW.FriedmannSolution.deriv_deriv_scaleFactor_nonpos`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L252).

> With `0 ≤ ρ`, `0 ≤ p` and `Λ = 0` at a time `t` of the interval, the second-order Friedmann
> equation gives `∂ₜ ∂ₜ a ≤ 0` at `t`: the expansion decelerates.

```lean
lemma deriv_deriv_scaleFactor_nonpos (h : U.FriedmannSolution F 0 G c) (hG : 0 < G) {t : Time}
    (ht : t ∈ U.I) (hρ : 0 ≤ F.ρ t) (hp : 0 ≤ F.p t) : ∂ₜ (∂ₜ U.a) t ≤ 0
```

**`Cosmology.FLRW.FriedmannSolution.lt_of_mem_I`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L269).

> The Big-Bang bound for a solution of the Friedmann equations with `0 ≤ ρ`, `0 ≤ p` and
> `Λ = 0` on its interval: if the model expands at `t₀ ∈ U.I`, every time of `U.I` is later than
> `t₀ - 1 / H(t₀)`, the Big Bang being at most `1 / H(t₀)` in the past.

```lean
lemma lt_of_mem_I (h : U.FriedmannSolution F 0 G c) (hG : 0 < G) (hρ : ∀ s ∈ U.I, 0 ≤ F.ρ s)
    (hp : ∀ s ∈ U.I, 0 ≤ F.p s) {t₀ : Time} (ht₀ : t₀ ∈ U.I) (h0 : 0 < ∂ₜ U.a t₀) {t : Time}
    (ht : t ∈ U.I) :
    t₀.val - 1 / hubbleConstant U.a t₀ < t.val
```

**`Cosmology.FLRW.FriedmannSolution.bddBelow_I`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean#L280).

> Under the same assumptions, the interval of the model is bounded below.

```lean
lemma bddBelow_I (h : U.FriedmannSolution F 0 G c) (hG : 0 < G) (hρ : ∀ s ∈ U.I, 0 ≤ F.ρ s)
    (hp : ∀ s ∈ U.I, 0 ≤ F.p s) {t₀ : Time} (ht₀ : t₀ ∈ U.I) (h0 : 0 < ∂ₜ U.a t₀) :
    BddBelow U.I
```

## Depends on

- [Density parameters and the closure relation](densityparameters.md)
- [Matter content of FLRW cosmology](mattercontent.md)

## Sources

- [Physlib/Cosmology/FLRW/FriedmannSolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/FriedmannSolution.lean)
