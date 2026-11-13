---
declaration: module
origin: cited
lean: Cosmology.FLRW.FriedmannEquation.deriv_powerLaw, Cosmology.FLRW.FriedmannEquation.deriv_deriv_powerLaw, Cosmology.FLRW.FriedmannEquation.hubbleConstant_powerLaw, Cosmology.FLRW.FriedmannEquation.decelerationParameter_powerLaw, Cosmology.FLRW.FriedmannEquation.powerLaw_firstOrderFriedmann, Cosmology.FLRW.FriedmannEquation.powerLaw_secondOrderFriedmann, Cosmology.FLRW.FriedmannEquation.radiationScaleFactor, Cosmology.FLRW.FriedmannEquation.radiationScaleFactor_firstOrderFriedmann
statement: formalized
proof: formalized
---

# Exact solutions of the Friedmann equations

The module `Physlib.Cosmology.FLRW.Solutions`, [Physlib/Cosmology/FLRW/Solutions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean): 27 declarations, 25 with a docstring.

## i. Overview

> …
>
> The flat power-law solutions are also given as FLRW models: `FLRW.powerLaw` in
> `Physlib.Cosmology.FLRW.SpecificCases.PowerLaw`, `FLRW.radiationDominated` in
> `Physlib.Cosmology.FLRW.SpecificCases.RadiationDominated` and `FLRW.einsteinDeSitter` in
> `Physlib.Cosmology.FLRW.SpecificCases.EinsteinDeSitter`.
>
> Each solution is a scale factor `a : Time → ℝ` given by an explicit function of the time
> coordinate `t.val`. Its time derivative `∂ₜ a` is computed through the bridge
> `deriv_comp_toRealCLE_of_hasDerivAt` from Mathlib's `HasDerivAt` on `ℝ`.

## ii. Key results

> - `hubbleConstant_powerLaw`, `decelerationParameter_powerLaw`, `powerLaw_firstOrderFriedmann`,
>   `powerLaw_secondOrderFriedmann`: the flat power-law solutions `a = (t / t₀) ^ n`, stated
>   inline, have Hubble parameter `n / t` and deceleration parameter `(1 - n) / n`, and solve the
>   flat (`k = 0`, `Λ = 0`) Friedmann equations with the density `ρ = 3 n² / (8 π G t²)` and the
>   pressure `p = w ρ c²`, `1 + 3 w = 2 (1 - n) / n`, for `t > 0`.
> - `radiationScaleFactor_firstOrderFriedmann`, `radiationScaleFactor_secondOrderFriedmann`:
>   `a = (t / t₀) ^ (1/2)` solves the flat Friedmann equations with the density
>   `ρ = 3 / (32 π G t²)` and the radiation pressure `p = ρ c² / 3`; `q = 1` and
>   `H(t₀) = 1 / (2 t₀)`.
> - `einsteinDeSitterScaleFactor_firstOrderFriedmann`,
>   `einsteinDeSitterScaleFactor_secondOrderFriedmann`: `a = (t / t₀) ^ (2/3)` solves the flat
>   Friedmann equations with the dust density `ρ = 1 / (6 π G t²)` and `p = 0`; `q = 1 / 2` and
>   `H(t₀) = 2 / (3 t₀)`.
>
> - `milneScaleFactor_firstOrderFriedmann`, `milneScaleFactor_secondOrderFriedmann`: the Milne
>   scale factor `a = c t` solves the empty (`ρ = 0`, `p = 0`, `Λ = 0`) Friedmann equations with
>   `k = -1`; `q = 0`. `FLRW.milne`, `FLRW.friedmannSolution_milne`: the Milne model on the
>   interval `t > 0`, with the saddle geometry of curvature parameter `-1`, filled with the empty
>   cosmic fluid solves the Friedmann equations.
> - `einsteinStatic_density`, `einsteinStatic_curvature`: if `∂ₜ a = ∂ₜ ∂ₜ a = 0` at `t` and the
>   Friedmann equations hold there with `p = 0`, then `ρ = Λ c² / (4 π G)` and
>   `k c² / a² = 4 π G ρ`, so that `k > 0` when `ρ > 0` (`einsteinStatic_curvature_pos`).
>
> In the power-law solutions `t₀ : Time` is the normalisation epoch (`a(t₀) = 1`) and the Big
> Bang is at the origin `t.val = 0` of the time chart.

## A. The spatially flat power-law solutions

> The radiation-dominated and Einstein-de Sitter solutions are both of the form
> `a(t) = (t / t₀) ^ n`; the Hubble parameter is `n / t` and the deceleration parameter
> `(1 - n) / n`. Their densities are imposed by the first-order Friedmann equation with `k = 0`
> and `Λ = 0`: `ρ = 3 H² / (8 π G) = 3 n² / (8 π G t²)`. The general power-law solution is
> stated inline, only the two named solutions get a definition.
>
> Throughout, `t₀` is the normalisation epoch, `a(t₀) = 1`, the Big Bang sits at the origin
> `t.val = 0` of the time chart (`Time` has no distinguished origin by itself), and the values
> for `t.val ≤ 0` are junk (`Real.rpow` on a non-positive base); every statement therefore
> assumes `0 < t.val`.

### A.1. Derivatives of the power-law scale factor

**`Cosmology.FLRW.FriedmannEquation.deriv_powerLaw`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L105).

> `∂ₜ (t / t₀) ^ n = n / t₀ (t / t₀) ^ (n - 1)` away from `t.val = 0`.

```lean
lemma deriv_powerLaw {t₀ : Time} (ht₀ : t₀.val ≠ 0) (n : ℝ) {t : Time} (ht : t.val ≠ 0) :
    ∂ₜ (fun s : Time => (s.val / t₀.val) ^ n) t = n / t₀.val * (t.val / t₀.val) ^ (n - 1)
```

**`Cosmology.FLRW.FriedmannEquation.deriv_deriv_powerLaw`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L119).

> `∂ₜ ∂ₜ (t / t₀) ^ n = n (n - 1) / t₀² (t / t₀) ^ (n - 2)` for `0 < t.val`. The first
> derivative is only known away from `t.val = 0`, which is enough since `0 < t.val` is an open
> condition.

```lean
lemma deriv_deriv_powerLaw {t₀ : Time} (ht₀ : t₀.val ≠ 0) (n : ℝ) {t : Time}
    (ht : 0 < t.val) :
    ∂ₜ (∂ₜ (fun s : Time => (s.val / t₀.val) ^ n)) t =
      n / t₀.val * ((n - 1) / t₀.val * (t.val / t₀.val) ^ (n - 1 - 1))
```

### A.2. The Hubble and deceleration parameters

**`Cosmology.FLRW.FriedmannEquation.hubbleConstant_powerLaw`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L143).

> The Hubble parameter of the power-law solution is `n / t` for `0 < t.val`.

```lean
lemma hubbleConstant_powerLaw {t₀ : Time} (ht₀ : 0 < t₀.val) (n : ℝ) {t : Time}
    (ht : 0 < t.val) :
    hubbleConstant (fun s : Time => (s.val / t₀.val) ^ n) t = n / t.val
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter_powerLaw`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L153).

> The deceleration parameter of the power-law solution is `(1 - n) / n` for `0 < t.val`,
> `n ≠ 0`.

```lean
lemma decelerationParameter_powerLaw {t₀ : Time} {n : ℝ} (ht₀ : 0 < t₀.val) (hn : n ≠ 0)
    {t : Time} (ht : 0 < t.val) :
    decelerationParameter (fun s : Time => (s.val / t₀.val) ^ n) t = (1 - n) / n
```

**`Cosmology.FLRW.FriedmannEquation.powerLaw_firstOrderFriedmann`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L165).

> The flat power-law solution solves the first-order Friedmann equation with `k = 0`,
> `Λ = 0` and the density `ρ = 3 n² / (8 π G t²)` that it imposes, for `0 < t.val`.

```lean
lemma powerLaw_firstOrderFriedmann {t₀ : Time} {G : ℝ} {c : SpeedOfLight} (ht₀ : 0 < t₀.val)
    (hG : 0 < G) (n : ℝ) {t : Time} (ht : 0 < t.val) :
    FirstOrderFriedmann (fun s : Time => (s.val / t₀.val) ^ n)
      (fun s => 3 * n ^ 2 / (8 * π * G * s.val ^ 2)) 0 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.powerLaw_secondOrderFriedmann`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L179).

> The second-order Friedmann equation for the flat power-law solution with the pressure
> `p = w ρ c²`, where `1 + 3 w = 2 (1 - n) / n`, for `0 < t.val`.

```lean
lemma powerLaw_secondOrderFriedmann {t₀ : Time} {G : ℝ} {c : SpeedOfLight} {n w : ℝ}
    (ht₀ : 0 < t₀.val) (hG : 0 < G) (hn : n ≠ 0) (hw : 1 + 3 * w = 2 * (1 - n) / n) {t : Time}
    (ht : 0 < t.val) :
    SecondOrderFriedmann (fun s : Time => (s.val / t₀.val) ^ n)
      (fun s => 3 * n ^ 2 / (8 * π * G * s.val ^ 2))
      (fun s => w * (3 * n ^ 2 / (8 * π * G * s.val ^ 2)) * (c : ℝ) ^ 2) 0 G c t
```

### A.3. The radiation-dominated solution

**`Cosmology.FLRW.FriedmannEquation.radiationScaleFactor`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L204).

> The radiation-dominated scale factor `a(t) = (t / t₀) ^ (1/2)`, normalised by `a(t₀) = 1`.
> The Big Bang is at the origin `t.val = 0` of the time chart; the values for `t.val ≤ 0` are
> junk.

```lean
noncomputable def radiationScaleFactor (t₀ : Time) : Time → ℝ
```

**`Cosmology.FLRW.FriedmannEquation.radiationScaleFactor_firstOrderFriedmann`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L209).

> The radiation-dominated solution solves the first-order Friedmann equation with `k = 0`,
> `Λ = 0` and the density `ρ = 3 / (32 π G t²)`, for `0 < t.val`.

```lean
lemma radiationScaleFactor_firstOrderFriedmann {t₀ : Time} {G : ℝ} {c : SpeedOfLight}
    (ht₀ : 0 < t₀.val) (hG : 0 < G) {t : Time} (ht : 0 < t.val) :
    FirstOrderFriedmann (radiationScaleFactor t₀) (fun s => 3 / (32 * π * G * s.val ^ 2))
      0 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.radiationScaleFactor_secondOrderFriedmann`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L223).

> The radiation-dominated solution solves the second-order Friedmann equation with the
> density `ρ = 3 / (32 π G t²)`, the pressure `p = ρ c² / 3` and `Λ = 0`, for `0 < t.val`.

```lean
lemma radiationScaleFactor_secondOrderFriedmann {t₀ : Time} {G : ℝ} {c : SpeedOfLight}
    (ht₀ : 0 < t₀.val) (hG : 0 < G) {t : Time} (ht : 0 < t.val) :
    SecondOrderFriedmann (radiationScaleFactor t₀) (fun s => 3 / (32 * π * G * s.val ^ 2))
      (fun s => 3 / (32 * π * G * s.val ^ 2) * (c : ℝ) ^ 2 / 3) 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter_radiationScaleFactor`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L238).

> The deceleration parameter of the radiation-dominated solution is `q = 1`.

```lean
lemma decelerationParameter_radiationScaleFactor {t₀ : Time} (ht₀ : 0 < t₀.val) {t : Time}
    (ht : 0 < t.val) :
    decelerationParameter (radiationScaleFactor t₀) t = 1
```

**`Cosmology.FLRW.FriedmannEquation.hubbleConstant_radiationScaleFactor_t₀`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L246).

> `H(t₀) = 1 / (2 t₀)` for the radiation-dominated solution, that is `t₀ = 1 / (2 H₀)`.

```lean
lemma hubbleConstant_radiationScaleFactor_t₀ {t₀ : Time} (ht₀ : 0 < t₀.val) :
    hubbleConstant (radiationScaleFactor t₀) t₀ = 1 / (2 * t₀.val)
```

### A.4. The Einstein-de Sitter solution

**`Cosmology.FLRW.FriedmannEquation.einsteinDeSitterScaleFactor`**, a def, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L261).

> The Einstein-de Sitter (flat, dust) scale factor `a(t) = (t / t₀) ^ (2/3)`, normalised by
> `a(t₀) = 1`. The Big Bang is at the origin `t.val = 0` of the time chart; the values for
> `t.val ≤ 0` are junk.

```lean
noncomputable def einsteinDeSitterScaleFactor (t₀ : Time) : Time → ℝ
```

**`Cosmology.FLRW.FriedmannEquation.einsteinDeSitterScaleFactor_firstOrderFriedmann`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L266).

> The Einstein-de Sitter solution solves the first-order Friedmann equation with `k = 0`,
> `Λ = 0` and the dust density `ρ = 1 / (6 π G t²)`, for `0 < t.val`.

```lean
lemma einsteinDeSitterScaleFactor_firstOrderFriedmann {t₀ : Time} {G : ℝ} {c : SpeedOfLight}
    (ht₀ : 0 < t₀.val) (hG : 0 < G) {t : Time} (ht : 0 < t.val) :
    FirstOrderFriedmann (einsteinDeSitterScaleFactor t₀) (fun s => 1 / (6 * π * G * s.val ^ 2))
      0 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.einsteinDeSitterScaleFactor_secondOrderFriedmann`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L280).

> The Einstein-de Sitter solution solves the second-order Friedmann equation with the dust
> density `ρ = 1 / (6 π G t²)`, `p = 0` and `Λ = 0`, for `0 < t.val`.

```lean
lemma einsteinDeSitterScaleFactor_secondOrderFriedmann {t₀ : Time} {G : ℝ} {c : SpeedOfLight}
    (ht₀ : 0 < t₀.val) (hG : 0 < G) {t : Time} (ht : 0 < t.val) :
    SecondOrderFriedmann (einsteinDeSitterScaleFactor t₀) (fun s => 1 / (6 * π * G * s.val ^ 2))
      (fun _ => 0) 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter_einsteinDeSitterScaleFactor`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L295).

> The deceleration parameter of the Einstein-de Sitter solution is `q = 1 / 2`.

```lean
lemma decelerationParameter_einsteinDeSitterScaleFactor {t₀ : Time} (ht₀ : 0 < t₀.val)
    {t : Time} (ht : 0 < t.val) :
    decelerationParameter (einsteinDeSitterScaleFactor t₀) t = 1 / 2
```

**`Cosmology.FLRW.FriedmannEquation.hubbleConstant_einsteinDeSitterScaleFactor_t₀`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L303).

> `H(t₀) = 2 / (3 t₀)` for the Einstein-de Sitter solution, that is `t₀ = 2 / (3 H₀)`.

```lean
lemma hubbleConstant_einsteinDeSitterScaleFactor_t₀ {t₀ : Time} (ht₀ : 0 < t₀.val) :
    hubbleConstant (einsteinDeSitterScaleFactor t₀) t₀ = 2 / (3 * t₀.val)
```

## B. The Milne solution

> The Milne universe is the empty (`ρ = 0`, `p = 0`, `Λ = 0`) solution with `k = -1` and
> `a(t) = c t` for `t > 0`. That it is Minkowski space in expanding coordinates (vanishing
> curvature) is not stated here: the FLRW metric is not yet an object of Physlib.

**`Cosmology.FLRW.FriedmannEquation.milneScaleFactor`**, a def, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L321).

> The Milne scale factor `a(t) = c t`. The Big Bang is at the origin `t.val = 0` of the time
> chart; the values for `t.val ≤ 0` are not part of the model.

```lean
noncomputable def milneScaleFactor (c : SpeedOfLight) : Time → ℝ
```

**`Cosmology.FLRW.FriedmannEquation.deriv_milneScaleFactor`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L324).

```lean
lemma deriv_milneScaleFactor (c : SpeedOfLight) : ∂ₜ (milneScaleFactor c) = fun _ => (c : ℝ)
```

**`Cosmology.FLRW.FriedmannEquation.deriv_deriv_milneScaleFactor`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L329).

```lean
lemma deriv_deriv_milneScaleFactor (c : SpeedOfLight) :
    ∂ₜ (∂ₜ (milneScaleFactor c)) = fun _ => 0
```

**`Cosmology.FLRW.FriedmannEquation.milneScaleFactor_firstOrderFriedmann`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L337).

> The Milne solution solves the first-order Friedmann equation with `ρ = 0`, `k = -1` and
> `Λ = 0`, for `t > 0`.

```lean
lemma milneScaleFactor_firstOrderFriedmann {G : ℝ} {c : SpeedOfLight} {t : Time} (ht : 0 < t.val) :
    FirstOrderFriedmann (milneScaleFactor c) (fun _ => 0) (-1) 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.milneScaleFactor_secondOrderFriedmann`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L348).

> The Milne solution solves the second-order Friedmann equation with `ρ = 0`, `p = 0` and
> `Λ = 0`.

```lean
lemma milneScaleFactor_secondOrderFriedmann {G : ℝ} {c : SpeedOfLight} (t : Time) :
    SecondOrderFriedmann (milneScaleFactor c) (fun _ => 0) (fun _ => 0) 0 G c t
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter_milneScaleFactor`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L355).

> The deceleration parameter of the Milne solution is `q = 0`.

```lean
lemma decelerationParameter_milneScaleFactor (c : SpeedOfLight) (t : Time) :
    decelerationParameter (milneScaleFactor c) t = 0
```

**`Cosmology.FLRW.milne`**, a def, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L364).

> The Milne model, defined on the interval `I = {t | 0 < t.val}` after the Big Bang at
> `t.val = 0`: the FLRW model with the scale factor `milneScaleFactor c` and the saddle
> geometry `Saddle 1` of curvature parameter `-1`.

```lean
noncomputable def _root_.Cosmology.FLRW.milne (c : SpeedOfLight) : FLRW
```

**`Cosmology.FLRW.friedmannSolution_milne`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L381).

> The Milne model filled with the empty cosmic fluid solves the Friedmann equations with
> `Λ = 0` on its interval `t > 0`.

```lean
lemma _root_.Cosmology.FLRW.friedmannSolution_milne (G : ℝ) (c : SpeedOfLight) :
    (FLRW.milne c).FriedmannSolution CosmicFluid.empty 0 G c
```

## C. The Einstein static universe

> At an instant where `∂ₜ a = ∂ₜ ∂ₜ a = 0`, the two Friedmann equations with dust (`p = 0`)
> force the density `ρ = Λ c² / (4 π G)` (twice the density `Λ c² / (8 π G)` that the
> cosmological constant carries as a `w = -1` fluid, a matter-content statement that belongs to
> `Physlib.Cosmology.FLRW.MatterContent`) and `k c² / a² = 4 π G ρ`, hence a positive curvature
> parameter when `ρ > 0`. That this equilibrium is unstable is not stated here.

**`Cosmology.FLRW.FriedmannEquation.einsteinStatic_density`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L404).

> In the Einstein static universe the dust density is `ρ = Λ c² / (4 π G)`.

```lean
lemma einsteinStatic_density {a ρ : Time → ℝ} {Λ G : ℝ} {c : SpeedOfLight} {t : Time}
    (hG : 0 < G) (h2 : ∂ₜ (∂ₜ a) t = 0) (hF2 : SecondOrderFriedmann a ρ (fun _ => 0) Λ G c t) :
    ρ t = Λ * (c : ℝ) ^ 2 / (4 * π * G)
```

**`Cosmology.FLRW.FriedmannEquation.einsteinStatic_curvature`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L415).

> In the Einstein static universe `k c² / a² = 4 π G ρ`.

```lean
lemma einsteinStatic_curvature {a ρ : Time → ℝ} {k Λ G : ℝ} {c : SpeedOfLight} {t : Time}
    (h1 : ∂ₜ a t = 0) (h2 : ∂ₜ (∂ₜ a) t = 0) (hF1 : FirstOrderFriedmann a ρ k Λ G c t)
    (hF2 : SecondOrderFriedmann a ρ (fun _ => 0) Λ G c t) :
    k * (c : ℝ) ^ 2 / (a t) ^ 2 = 4 * π * G * ρ t
```

**`Cosmology.FLRW.FriedmannEquation.einsteinStatic_curvature_pos`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean#L428).

> In the Einstein static universe with positive density, the curvature parameter is
> positive.

```lean
lemma einsteinStatic_curvature_pos {a ρ : Time → ℝ} {k Λ G : ℝ} {c : SpeedOfLight} {t : Time}
    (hG : 0 < G) (ha : a t ≠ 0) (hρ : 0 < ρ t) (h1 : ∂ₜ a t = 0) (h2 : ∂ₜ (∂ₜ a) t = 0)
    (hF1 : FirstOrderFriedmann a ρ k Λ G c t)
    (hF2 : SecondOrderFriedmann a ρ (fun _ => 0) Λ G c t) :
    0 < k
```

…

## Depends on

- [The Friedmann-Lemaître-Robertson-Walker metric](basic.md)

## Sources

- [Physlib/Cosmology/FLRW/Solutions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Solutions.lean)
