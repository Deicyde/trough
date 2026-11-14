---
declaration: module
origin: cited
lean: Cosmology.FLRW.FriedmannEquation.deSitterScaleFactor, Cosmology.FLRW.FriedmannEquation.deriv_deSitterScaleFactor, Cosmology.FLRW.FriedmannEquation.deriv_deriv_deSitterScaleFactor, Cosmology.FLRW.FriedmannEquation.sq_deSitterRate, Cosmology.FLRW.FriedmannEquation.deSitterScaleFactor_firstOrderFriedmann, Cosmology.FLRW.FriedmannEquation.deSitterScaleFactor_secondOrderFriedmann, Cosmology.FLRW.FriedmannEquation.hubbleConstant_deSitterScaleFactor, Cosmology.FLRW.FriedmannEquation.decelerationParameter_deSitterScaleFactor
statement: formalized
proof: formalized
---

# The de Sitter solution of the Friedmann equations

The module `Physlib.Cosmology.FLRW.DeSitter`, [Physlib/Cosmology/FLRW/DeSitter.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean): 11 declarations, 9 with a docstring.

## i. Overview

> The de Sitter solution of the Friedmann equations (`FirstOrderFriedmann` and
> `SecondOrderFriedmann` of `Physlib.Cosmology.FLRW.Basic`): the scale factor
> `a(t) = a₀ exp(σ √(Λ/3) c t)`, `σ = ±1`, solves both equations with `ρ = 0`, `p = 0`, flat
> spatial slices and `Λ > 0`; its Hubble parameter is constant and its deceleration parameter is
> `q = -1`. As an FLRW model filled with the empty cosmic fluid, `FLRW.deSitter`, it is defined at
> all times: its interval of time is not bounded below, whereas a solution with `0 ≤ ρ`, `0 ≤ p`
> and `Λ = 0` that expands at one time has a Big Bang
> (`Physlib.Cosmology.FLRW.FriedmannSolution`).

## ii. Key results

> - `deSitterScaleFactor`: `a(t) = a₀ exp(σ √(Λ/3) c t)` with `σ = ±1`.
> - `deSitterScaleFactor_firstOrderFriedmann`, `deSitterScaleFactor_secondOrderFriedmann`:
>   it solves both Friedmann equations with `ρ = 0`, `p = 0`, `k = 0` and `Λ > 0`.
> - `hubbleConstant_deSitterScaleFactor`: its Hubble parameter is the constant `σ √(Λ/3) c`
>   (for any `σ`, `Λ`, `c`).
> - `decelerationParameter_deSitterScaleFactor`: its deceleration parameter is `q = -1`.
> - `FLRW.deSitter`, `FLRW.friedmannSolution_deSitter`: the de Sitter model, defined at all
>   times, filled with the empty cosmic fluid solves the Friedmann equations.
> - `FLRW.not_bddBelow_deSitter_I`: the interval of the de Sitter model is not bounded below.

## iv. References

> * None.

## A. The scale factor and its derivatives

**`Cosmology.FLRW.FriedmannEquation.deSitterScaleFactor`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L64).

> The de Sitter scale factor `a(t) = a₀ exp(σ √(Λ/3) c t)`, for `σ = ±1`
> (the expanding branch is `σ = 1`).

```lean
noncomputable def deSitterScaleFactor (a₀ σ Λ : ℝ) (c : SpeedOfLight) : Time → ℝ
```

**`Cosmology.FLRW.FriedmannEquation.deriv_deSitterScaleFactor`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L67).

```lean
lemma deriv_deSitterScaleFactor (a₀ σ Λ : ℝ) (c : SpeedOfLight) :
    ∂ₜ (deSitterScaleFactor a₀ σ Λ c) =
      fun t => a₀ * (σ * √(Λ / 3) * (c : ℝ)) * Real.exp (σ * √(Λ / 3) * (c : ℝ) * t.val)
```

**`Cosmology.FLRW.FriedmannEquation.deriv_deriv_deSitterScaleFactor`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L79).

```lean
lemma deriv_deriv_deSitterScaleFactor (a₀ σ Λ : ℝ) (c : SpeedOfLight) :
    ∂ₜ (∂ₜ (deSitterScaleFactor a₀ σ Λ c)) =
      fun t => a₀ * (σ * √(Λ / 3) * (c : ℝ)) * (σ * √(Λ / 3) * (c : ℝ)) *
        Real.exp (σ * √(Λ / 3) * (c : ℝ) * t.val)
```

**`Cosmology.FLRW.FriedmannEquation.sq_deSitterRate`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L98).

> `σ² (√(Λ/3))² c² = Λ c² / 3` for `σ = ±1` and `0 ≤ Λ`.

```lean
lemma sq_deSitterRate {σ Λ : ℝ} {c : SpeedOfLight} (hΛ : 0 ≤ Λ) (hσ : σ = 1 ∨ σ = -1) :
    (σ * √(Λ / 3) * (c : ℝ)) ^ 2 = Λ * (c : ℝ) ^ 2 / 3
```

## B. The Friedmann equations

**`Cosmology.FLRW.FriedmannEquation.deSitterScaleFactor_firstOrderFriedmann`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L111).

> The de Sitter scale factor solves the first-order Friedmann equation with `ρ = 0`,
> `k = 0` and `Λ > 0`.

```lean
lemma deSitterScaleFactor_firstOrderFriedmann {a₀ σ Λ G : ℝ} {c : SpeedOfLight} (hΛ : 0 < Λ)
    (ha₀ : a₀ ≠ 0) (hσ : σ = 1 ∨ σ = -1) (t : Time) :
    FirstOrderFriedmann (deSitterScaleFactor a₀ σ Λ c) (fun _ => 0) 0 Λ G c t
```

**`Cosmology.FLRW.FriedmannEquation.deSitterScaleFactor_secondOrderFriedmann`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L125).

> The de Sitter scale factor solves the second-order Friedmann equation with `ρ = 0`,
> `p = 0` and `Λ > 0`.

```lean
lemma deSitterScaleFactor_secondOrderFriedmann {a₀ σ Λ G : ℝ} {c : SpeedOfLight} (hΛ : 0 < Λ)
    (ha₀ : a₀ ≠ 0) (hσ : σ = 1 ∨ σ = -1) (t : Time) :
    SecondOrderFriedmann (deSitterScaleFactor a₀ σ Λ c) (fun _ => 0) (fun _ => 0) Λ G c t
```

## C. The Hubble and deceleration parameters

**`Cosmology.FLRW.FriedmannEquation.hubbleConstant_deSitterScaleFactor`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L145).

> The Hubble parameter of the de Sitter solution is the constant `σ √(Λ/3) c`.

```lean
lemma hubbleConstant_deSitterScaleFactor {a₀ σ Λ : ℝ} {c : SpeedOfLight} (ha₀ : a₀ ≠ 0)
    (t : Time) :
    hubbleConstant (deSitterScaleFactor a₀ σ Λ c) t = σ * √(Λ / 3) * (c : ℝ)
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter_deSitterScaleFactor`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L155).

> The deceleration parameter of the de Sitter solution is `q = -1`.

```lean
lemma decelerationParameter_deSitterScaleFactor {a₀ σ Λ : ℝ} {c : SpeedOfLight} (hΛ : 0 < Λ)
    (ha₀ : a₀ ≠ 0) (hσ : σ = 1 ∨ σ = -1) (t : Time) :
    decelerationParameter (deSitterScaleFactor a₀ σ Λ c) t = -1
```

## D. The de Sitter model

**`Cosmology.FLRW.deSitter`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L181).

> The de Sitter model, defined at all times: the FLRW model with the scale factor
> `deSitterScaleFactor a₀ σ Λ c`, `a₀ > 0`, and the flat spatial geometry.

```lean
noncomputable def _root_.Cosmology.FLRW.deSitter (a₀ σ Λ : ℝ) (c : SpeedOfLight) (ha₀ : 0 < a₀) :
    FLRW
```

**`Cosmology.FLRW.friedmannSolution_deSitter`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L198).

> The de Sitter model filled with the empty cosmic fluid solves the Friedmann equations with
> cosmological constant `Λ > 0`, for `σ = ±1`.

```lean
lemma _root_.Cosmology.FLRW.friedmannSolution_deSitter {a₀ σ Λ : ℝ} (G : ℝ) (c : SpeedOfLight)
    (hΛ : 0 < Λ) (ha₀ : 0 < a₀) (hσ : σ = 1 ∨ σ = -1) :
    (FLRW.deSitter a₀ σ Λ c ha₀).FriedmannSolution CosmicFluid.empty Λ G c
```

## E. The de Sitter model is defined at all times

**`Cosmology.FLRW.not_bddBelow_deSitter_I`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean#L213).

> The de Sitter model, which solves the Friedmann equations with `0 < Λ`
> (`FLRW.friedmannSolution_deSitter`), is defined at all times: its interval is not bounded
> below.

```lean
lemma _root_.Cosmology.FLRW.not_bddBelow_deSitter_I (a₀ σ Λ : ℝ) (c : SpeedOfLight)
    (ha₀ : 0 < a₀) :
    ¬ BddBelow (FLRW.deSitter a₀ σ Λ c ha₀).I
```

## Depends on

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)

## Sources

- [Physlib/Cosmology/FLRW/DeSitter.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/DeSitter.lean)
