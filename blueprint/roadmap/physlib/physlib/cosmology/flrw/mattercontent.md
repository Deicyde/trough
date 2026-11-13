---
declaration: module
origin: cited
lean: Cosmology.FLRW.FriedmannEquation.ContinuityEquation, Cosmology.FLRW.FriedmannEquation.deriv_firstOrderFriedmann, Cosmology.FLRW.FriedmannEquation.continuityEquation_of_friedmann, Cosmology.FLRW.FriedmannEquation.secondOrderFriedmann_of_continuityEquation, Cosmology.FLRW.FriedmannSolution.continuityEquation, Cosmology.FLRW.FriedmannEquation.barotropicPressure, Cosmology.FLRW.FriedmannEquation.deriv_of_continuityEquation_barotropic, Cosmology.FLRW.FriedmannEquation.density_scaling
statement: formalized
proof: formalized
---

# Matter content of FLRW cosmology

The module `Physlib.Cosmology.FLRW.MatterContent`, [Physlib/Cosmology/FLRW/MatterContent.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean): 15 declarations, 15 with a docstring.

## i. Overview

> …
>
> Time derivatives of curves `Time → ℝ` are computed through the bridge
> `Time.hasDerivAt_mk_of_differentiableAt` to Mathlib's `HasDerivAt` on `ℝ`.

## ii. Key results

> - `ContinuityEquation`: the continuity equation at an instant `t`.
> - `deriv_firstOrderFriedmann`: the time derivative of the first-order Friedmann equation,
>   `2 H (a''/a - H²) = (8 π G / 3) ρ' + 2 k c² H / a²`.
> - `continuityEquation_of_friedmann`: the continuity equation follows from the two Friedmann
>   equations.
> - `secondOrderFriedmann_of_continuityEquation`: the second-order Friedmann equation follows
>   from the first-order equation and the continuity equation when `∂ₜ a ≠ 0`.
> - `FLRW.FriedmannSolution.continuityEquation`: the continuity equation holds on the interval of
>   an FLRW model whose cosmic fluid solves the Friedmann equations.
> - `barotropicPressure`: `p = w ρ c²`; `density_scaling`: under the barotropic continuity
>   equation at all times, `ρ t = ρ t₀ (a t / a t₀)^(-3(1+w))`; `continuityEquation_of_scaling`:
>   the converse; `density_scaling_dust`, `density_scaling_radiation`,
>   `density_scaling_vacuum`: `ρ ∝ a⁻³`, `ρ ∝ a⁻⁴`, `ρ` constant.
> - `firstOrderFriedmann_iff_lambdaFluid`, `secondOrderFriedmann_iff_lambdaFluid`: the Friedmann
>   equations with `Λ` are the Friedmann equations without `Λ` for the fluid `ρ + ρ_Λ`, `p + p_Λ`,
>   where `ρ_Λ = Λ c² / (8 π G)` and `p_Λ = - ρ_Λ c²` (`cosmologicalConstantDensity` and
>   `cosmologicalConstantPressure`, defined in `Physlib.Cosmology.FLRW.Basic`);
>   `cosmologicalConstantPressure_eq_barotropic`: `p_Λ` is the `w = -1` barotropic pressure.

## A. The continuity equation

### A.1. The definition

**`Cosmology.FLRW.FriedmannEquation.ContinuityEquation`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L97).

> The continuity equation of the cosmic fluid at the instant `t`:
> `∂ₜ ρ + 3 H (ρ + p / c²) = 0`, with `H = hubbleConstant a`.

```lean
def ContinuityEquation (a ρ p : Time → ℝ) (c : SpeedOfLight) (t : Time) : Prop
```

### A.2. The derivative of the first-order Friedmann equation

**`Cosmology.FLRW.FriedmannEquation.deriv_firstOrderFriedmann`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L108).

> Differentiating the first-order Friedmann equation, assumed at all times near `t`, at `t`:
> `2 H (a''/a - H²) = (8 π G / 3) ρ' + 2 k c² H / a²`.

```lean
lemma deriv_firstOrderFriedmann {a ρ : Time → ℝ} {k Λ G : ℝ} {c : SpeedOfLight} {t : Time}
    (ha : a t ≠ 0) (hd1 : DifferentiableAt ℝ a t) (hd2 : DifferentiableAt ℝ (∂ₜ a) t)
    (hdρ : DifferentiableAt ℝ ρ t) (hF1 : ∀ᶠ s in 𝓝 t, FirstOrderFriedmann a ρ k Λ G c s) :
    2 * (∂ₜ a t / a t) * (∂ₜ (∂ₜ a) t / a t - (∂ₜ a t / a t) ^ 2)
      = 8 * π * G / 3 * ∂ₜ ρ t + 2 * k * (c : ℝ) ^ 2 * (∂ₜ a t / a t) / (a t) ^ 2
```

### A.3. Continuity from the Friedmann equations

**`Cosmology.FLRW.FriedmannEquation.continuityEquation_of_friedmann`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L138).

> The continuity equation follows from the first-order Friedmann equation, assumed at all
> times near `t`, and the second-order Friedmann equation at `t`; `a` must be twice
> differentiable and `ρ` differentiable at `t`.

```lean
lemma continuityEquation_of_friedmann {a ρ p : Time → ℝ} {k Λ G : ℝ} {c : SpeedOfLight}
    {t : Time} (hG : G ≠ 0) (ha : a t ≠ 0) (hd1 : DifferentiableAt ℝ a t)
    (hd2 : DifferentiableAt ℝ (∂ₜ a) t)
    (hdρ : DifferentiableAt ℝ ρ t) (hF1 : ∀ᶠ s in 𝓝 t, FirstOrderFriedmann a ρ k Λ G c s)
    (hF2 : SecondOrderFriedmann a ρ p Λ G c t) :
    ContinuityEquation a ρ p c t
```

### A.4. The second-order Friedmann equation from continuity

**`Cosmology.FLRW.FriedmannEquation.secondOrderFriedmann_of_continuityEquation`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L163).

> The second-order Friedmann equation at `t` follows from the first-order Friedmann
> equation, assumed at all times near `t`, and the continuity equation at `t`, provided
> `∂ₜ a t ≠ 0`. Together with `continuityEquation_of_friedmann`, the three equations are not
> independent.

```lean
lemma secondOrderFriedmann_of_continuityEquation {a ρ p : Time → ℝ} {k Λ G : ℝ}
    {c : SpeedOfLight} {t : Time} (ha : a t ≠ 0) (ha' : ∂ₜ a t ≠ 0) (hd1 : DifferentiableAt ℝ a t)
    (hd2 : DifferentiableAt ℝ (∂ₜ a) t) (hdρ : DifferentiableAt ℝ ρ t)
    (hF1 : ∀ᶠ s in 𝓝 t, FirstOrderFriedmann a ρ k Λ G c s)
    (hC : ContinuityEquation a ρ p c t) :
    SecondOrderFriedmann a ρ p Λ G c t
```

### A.5. The continuity equation of a solution of the Friedmann equations

**`Cosmology.FLRW.FriedmannSolution.continuityEquation`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L190).

> If the FLRW model `U` filled with the cosmic fluid `F` solves the Friedmann equations, the
> continuity equation holds at every time of the interval `U.I` at which the energy density is
> differentiable: it is obtained from the two Friedmann equations through
> `continuityEquation_of_friedmann`.

```lean
lemma _root_.Cosmology.FLRW.FriedmannSolution.continuityEquation {U : FLRW} {F : CosmicFluid}
    {Λ G : ℝ} {c : SpeedOfLight} (h : U.FriedmannSolution F Λ G c) (hG : G ≠ 0) {t : Time}
    (ht : t ∈ U.I) (hdρ : DifferentiableAt ℝ F.ρ t) :
    ContinuityEquation U.a F.ρ F.p c t
```

## B. The barotropic equation of state and the density scaling law

### B.1. The equation of state

**`Cosmology.FLRW.FriedmannEquation.barotropicPressure`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L211).

> The barotropic pressure `p = w ρ c²` with constant equation-of-state parameter `w`.

```lean
noncomputable def barotropicPressure (w : ℝ) (ρ : Time → ℝ) (c : SpeedOfLight) : Time → ℝ
```

**`Cosmology.FLRW.FriedmannEquation.deriv_of_continuityEquation_barotropic`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L215).

> Under the barotropic continuity equation, `∂ₜ ρ = -3 (1 + w) H ρ`.

```lean
lemma deriv_of_continuityEquation_barotropic {a ρ : Time → ℝ} {w : ℝ} {c : SpeedOfLight}
    {t : Time} (hC : ContinuityEquation a ρ (barotropicPressure w ρ c) c t) :
    ∂ₜ ρ t = -3 * (1 + w) * hubbleConstant a t * ρ t
```

### B.2. The density scaling law

**`Cosmology.FLRW.FriedmannEquation.density_scaling`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L234).

> The density scaling law: under the barotropic continuity equation at all times, with `a`
> and `ρ` differentiable and `a > 0`, `ρ t = ρ t₀ (a t / a t₀)^(-3(1+w))`. The proof shows that
> `ρ a^(3(1+w))` has zero derivative along the time chart.

```lean
lemma density_scaling {a ρ : Time → ℝ} {w : ℝ} {c : SpeedOfLight} (hd1 : Differentiable ℝ a)
    (hdρ : Differentiable ℝ ρ) (hapos : ∀ s, 0 < a s)
    (hC : ∀ s, ContinuityEquation a ρ (barotropicPressure w ρ c) c s) (t t₀ : Time) :
    ρ t = ρ t₀ * (a t / a t₀) ^ (-(3 * (1 + w)))
```

**`Cosmology.FLRW.FriedmannEquation.continuityEquation_of_scaling`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L263).

> Conversely, `ρ = ρ₀ (a / a₀)^(-3(1+w))` satisfies the barotropic continuity equation at
> all times, for `a` differentiable and positive.

```lean
lemma continuityEquation_of_scaling {a : Time → ℝ} {w : ℝ} {c : SpeedOfLight} {ρ₀ a₀ : ℝ}
    (ha₀ : a₀ ≠ 0) (hd1 : Differentiable ℝ a) (hapos : ∀ s, 0 < a s) (t : Time) :
    ContinuityEquation a (fun s => ρ₀ * (a s / a₀) ^ (-(3 * (1 + w))))
      (barotropicPressure w (fun s => ρ₀ * (a s / a₀) ^ (-(3 * (1 + w)))) c) c t
```

### B.3. Dust, radiation and vacuum energy

**`Cosmology.FLRW.FriedmannEquation.density_scaling_dust`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L288).

> Dust, `w = 0`: `ρ ∝ a⁻³`.

```lean
lemma density_scaling_dust {a ρ : Time → ℝ} {c : SpeedOfLight} (hd1 : Differentiable ℝ a)
    (hdρ : Differentiable ℝ ρ) (hapos : ∀ s, 0 < a s)
    (hC : ∀ s, ContinuityEquation a ρ (barotropicPressure 0 ρ c) c s) (t t₀ : Time) :
    ρ t = ρ t₀ * (a t₀ / a t) ^ 3
```

**`Cosmology.FLRW.FriedmannEquation.density_scaling_radiation`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L298).

> Radiation, `w = 1/3`: `ρ ∝ a⁻⁴`.

```lean
lemma density_scaling_radiation {a ρ : Time → ℝ} {c : SpeedOfLight} (hd1 : Differentiable ℝ a)
    (hdρ : Differentiable ℝ ρ) (hapos : ∀ s, 0 < a s)
    (hC : ∀ s, ContinuityEquation a ρ (barotropicPressure (1 / 3) ρ c) c s) (t t₀ : Time) :
    ρ t = ρ t₀ * (a t₀ / a t) ^ 4
```

**`Cosmology.FLRW.FriedmannEquation.density_scaling_vacuum`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L308).

> Vacuum energy, `w = -1`: `ρ` is constant.

```lean
lemma density_scaling_vacuum {a ρ : Time → ℝ} {c : SpeedOfLight} (hd1 : Differentiable ℝ a)
    (hdρ : Differentiable ℝ ρ) (hapos : ∀ s, 0 < a s)
    (hC : ∀ s, ContinuityEquation a ρ (barotropicPressure (-1) ρ c) c s) (t t₀ : Time) :
    ρ t = ρ t₀
```

## C. The cosmological constant as a fluid

> The density `cosmologicalConstantDensity` and the pressure `cosmologicalConstantPressure` of the
> cosmological constant, and the cosmic fluid `CosmicFluid.addCosmologicalConstant` with the
> cosmological constant folded in, are defined in `Physlib.Cosmology.FLRW.Basic`.

**`Cosmology.FLRW.FriedmannEquation.firstOrderFriedmann_iff_lambdaFluid`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L327).

> The first-order Friedmann equation with `Λ` is the first-order Friedmann equation without
> `Λ` for the density `ρ + ρ_Λ`.

```lean
lemma firstOrderFriedmann_iff_lambdaFluid {a ρ : Time → ℝ} {k Λ G : ℝ} {c : SpeedOfLight}
    {t : Time} (hG : G ≠ 0) :
    FirstOrderFriedmann a ρ k Λ G c t ↔
      FirstOrderFriedmann a (fun s => ρ s + cosmologicalConstantDensity Λ G c) k 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.secondOrderFriedmann_iff_lambdaFluid`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L342).

> The second-order Friedmann equation with `Λ` is the second-order Friedmann equation
> without `Λ` for the density `ρ + ρ_Λ` and the pressure `p + p_Λ`.

```lean
lemma secondOrderFriedmann_iff_lambdaFluid {a ρ p : Time → ℝ} {Λ G : ℝ} {c : SpeedOfLight}
    {t : Time} (hG : G ≠ 0) :
    SecondOrderFriedmann a ρ p Λ G c t ↔
      SecondOrderFriedmann a (fun s => ρ s + cosmologicalConstantDensity Λ G c)
        (fun s => p s + cosmologicalConstantPressure Λ G c) 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.cosmologicalConstantPressure_eq_barotropic`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean#L359).

> `p_Λ` is the barotropic pressure of `ρ_Λ` with `w = -1`.

```lean
lemma cosmologicalConstantPressure_eq_barotropic (Λ G : ℝ) (c : SpeedOfLight) (t : Time) :
    cosmologicalConstantPressure Λ G c
      = barotropicPressure (-1) (fun _ => cosmologicalConstantDensity Λ G c) c t
```

…

## Depends on

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)

## Sources

- [Physlib/Cosmology/FLRW/MatterContent.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/MatterContent.lean)
