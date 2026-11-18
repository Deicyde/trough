---
declaration: module
origin: cited
lean: GeneralRelativity.IncompressibleSphere, GeneralRelativity.IncompressibleSphere.rs, GeneralRelativity.IncompressibleSphere.chia, GeneralRelativity.IncompressibleSphere.cosChia, GeneralRelativity.IncompressibleSphere.one_sub_sq_div_sq_pos, GeneralRelativity.IncompressibleSphere.cosChia_sq, GeneralRelativity.IncompressibleSphere.cosChia_eq_cos_chia, GeneralRelativity.IncompressibleSphere.cosChia_pos
statement: formalized
proof: formalized
---

# Schwarzschild's incompressible fluid sphere and its junction with the exterior solution

The module `PhyslibAlpha.Relativity.General.Schwarzschild.IncompressibleSphere`, [PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean): 53 declarations, 44 with a docstring.

> Junction of Schwarzschild's incompressible fluid sphere with the exterior Schwarzschild metric.

## i. Overview

> In his second 1916 paper, Schwarzschild solved Einstein's equations for a static sphere of
> incompressible fluid of constant density `ρ₀`. The interior space is a portion of a
> three-sphere of curvature radius `Rc`, with `Rc ^ 2 = 3 / (κ ρ₀)` (`κ = 8 π G`, `c = 1`),
> and the surface of the fluid sits at the polar angle `χ_a` with `sin χ_a = Ra / Rc`, where
> `Ra` is the areal radius of the surface. In the areal radius `r = Rc sin χ` the interior metric
> coefficients are
>
> - `g_tt = ((3 cos χ_a - cos χ) / 2) ^ 2 = (3 / 2 cos χ_a - 1 / 2 √(1 - r ^ 2 / Rc ^ 2)) ^ 2`,
> - `g_rr = 1 / (1 - r ^ 2 / Rc ^ 2)`,
>
> while outside the sphere the metric is the exterior Schwarzschild solution with
> `g_tt = 1 - α / r`, `g_rr = 1 / (1 - α / r)` and `α = Ra ^ 3 / Rc ^ 2`. The pressure is
> `ρ₀ + p = ρ₀ 2 cos χ_a / (3 cos χ_a - cos χ)`.
>
> This file takes the two metrics and the pressure as given (the field equations are not
> verified here) and proves the elementary properties of the junction at `r = Ra`: continuity
> of `g_tt` and `g_rr`, differentiability of the glued `g_tt`, non-differentiability of the glued
> `g_rr` in the curvature coordinate `r`, the vanishing of the pressure at the surface, and the
> Schwarzschild bound `cos χ_a > 1 / 3` (equivalently `Ra > 9 / 8 α`) for the central pressure to
> be positive.

## ii. Key results

> - `IncompressibleSphere` contains the input data: `Rc`, `Ra`, `ρ₀` with `0 < Ra < Rc` and
>   `0 < ρ₀`.
> - `rs_div_Ra`: Schwarzschild's relation (40), `α / Ra = sin χ_a ^ 2`.
> - `pressure_chia`: the pressure vanishes at the surface.
> - `pressure_zero_pos_iff`: the central pressure is positive if and only if `cos χ_a > 1 / 3`.
> - `one_third_lt_cosChia_iff_rs`: `cos χ_a > 1 / 3` if and only if `9 / 8 α < Ra`.
> - `gttIn_Ra`, `grrIn_Ra`: the interior and exterior formulas agree at `r = Ra`.
> - `gttGlue_hasDerivAt`: the glued `g_tt` is differentiable at `Ra` with derivative `Ra / Rc ^ 2`.
> - `grrGlue_not_differentiableAt`: the glued `g_rr` is continuous but not differentiable at
>   `Ra` (one-sided derivatives `2 Ra / (Rc ^ 2 cos χ_a ^ 4)` and `- Ra / (Rc ^ 2 cos χ_a ^ 4)`).

## iv. References

> - K. Schwarzschild, "Uber das Gravitationsfeld einer Kugel aus inkompressibler Flussigkeit nach
>   der Einsteinschen Theorie", Sitzungsberichte der Koniglich Preussischen Akademie der
>   Wissenschaften (1916), 424-434. English translation by S. Antoci, arXiv:physics/9912033.
>   Equations (28), (29), (30), (35), (36), (39), (40) and the discussion on pages 8-9 of the
>   translation (pressure diverging at `cos χ_a = 1 / 3`, limit `9 / 8 α`).
> - A. Lichnerowicz, "Theories relativistes de la gravitation et de l'electromagnetisme",
>   Masson (1955), chapter III, sections 27-29 (junction conditions).

## A. The input data

> The sphere is specified by the curvature radius `Rc` of the interior space, the areal radius
> `Ra` of its surface and the constant density `ρ₀`. The sphere is a proper part of the spherical
> space (`Ra < Rc`, so that `χ_a < π / 2`).

**`GeneralRelativity.IncompressibleSphere`**, a structure, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L107).

> Schwarzschild's incompressible fluid sphere: the curvature radius `Rc` of the interior
> spherical space (`Rc ^ 2 = 3 / (κ ρ₀)`, Schwarzschild (37)), the areal radius `Ra` of the
> surface (Schwarzschild's `P_o`, (39)) and the constant density `ρ₀`, with `0 < Ra < Rc` and
> `0 < ρ₀`.

```lean
structure IncompressibleSphere where
  /-- The curvature radius of the interior spherical space. -/
  Rc : ℝ
  /-- The areal radius of the surface of the fluid. -/
  Ra : ℝ
  /-- The constant density of the fluid. -/
  ρ₀ : ℝ
  /-- The curvature radius is positive. -/
  Rc_pos : 0 < Rc
  /-- The radius of the surface is positive. -/
  Ra_pos : 0 < Ra
  /-- The sphere is a proper part of the spherical space. -/
  Ra_lt_Rc : Ra < Rc
  /-- The density is positive. -/
  ρ₀_pos : 0 < ρ₀
```

## B. The Schwarzschild radius and the angle of the surface

**`GeneralRelativity.IncompressibleSphere.rs`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L135).

> The Schwarzschild radius `α = (κ ρ₀ / 3) P_o ^ 3 = Ra ^ 3 / Rc ^ 2` of the sphere,
> Schwarzschild (40).

```lean
def rs : ℝ
```

**`GeneralRelativity.IncompressibleSphere.chia`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L138).

> The polar angle `χ_a` of the surface, `sin χ_a = Ra / Rc`, Schwarzschild (28).

```lean
def chia : ℝ
```

**`GeneralRelativity.IncompressibleSphere.cosChia`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L141).

> The cosine of the angle of the surface, written as `√(1 - Ra ^ 2 / Rc ^ 2)`.

```lean
def cosChia : ℝ
```

**`GeneralRelativity.IncompressibleSphere.one_sub_sq_div_sq_pos`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L143).

```lean
lemma one_sub_sq_div_sq_pos : 0 < 1 - S.Ra ^ 2 / S.Rc ^ 2
```

**`GeneralRelativity.IncompressibleSphere.cosChia_sq`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L149).

```lean
lemma cosChia_sq : S.cosChia ^ 2 = 1 - S.Ra ^ 2 / S.Rc ^ 2
```

**`GeneralRelativity.IncompressibleSphere.cosChia_eq_cos_chia`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L154).

> `cosChia` is the cosine of `chia`.

```lean
lemma cosChia_eq_cos_chia : S.cosChia = Real.cos S.chia
```

**`GeneralRelativity.IncompressibleSphere.cosChia_pos`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L158).

```lean
lemma cosChia_pos : 0 < S.cosChia
```

**`GeneralRelativity.IncompressibleSphere.cosChia_lt_one`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L162).

```lean
lemma cosChia_lt_one : S.cosChia < 1
```

**`GeneralRelativity.IncompressibleSphere.rs_div_Ra`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L169).

> Schwarzschild (40): `α / P_o = sin χ_a ^ 2`.

```lean
lemma rs_div_Ra : S.rs / S.Ra = Real.sin S.chia ^ 2
```

**`GeneralRelativity.IncompressibleSphere.rs_lt_Ra`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L183).

> The surface of the sphere lies outside its Schwarzschild radius.

```lean
lemma rs_lt_Ra : S.rs < S.Ra
```

## C. The pressure

**`GeneralRelativity.IncompressibleSphere.pressure`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L197).

> The pressure of the fluid at the polar angle `χ`, Schwarzschild (30):
> `ρ₀ + p = ρ₀ 2 cos χ_a / (3 cos χ_a - cos χ)`.

```lean
def pressure (χ : ℝ) : ℝ
```

### C.1. Pressure at the surface and at the centre

**`GeneralRelativity.IncompressibleSphere.pressure_chia`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L207).

> The pressure vanishes at the surface of the fluid.

```lean
lemma pressure_chia : S.pressure S.chia = 0
```

**`GeneralRelativity.IncompressibleSphere.pressure_zero`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L216).

> The pressure at the centre, away from the critical value `cos χ_a = 1 / 3`.

```lean
lemma pressure_zero (h : 3 * S.cosChia ≠ 1) :
    S.pressure 0 = S.ρ₀ * (1 - S.cosChia) / (3 * S.cosChia - 1)
```

**`GeneralRelativity.IncompressibleSphere.pressure_zero_pos`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L224).

```lean
lemma pressure_zero_pos (hsub : 1 / 3 < S.cosChia) : 0 < S.pressure 0
```

**`GeneralRelativity.IncompressibleSphere.pressure_zero_pos_iff`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L239).

> The central pressure is positive if and only if `cos χ_a > 1 / 3`. For `cos χ_a < 1 / 3`
> the formula (30) is negative at the centre; at `cos χ_a = 1 / 3` the division by zero of
> Lean gives `pressure 0 = - ρ₀`. The divergence of the pressure at the critical value is not
> a statement of this file.

```lean
lemma pressure_zero_pos_iff : 0 < S.pressure 0 ↔ 1 / 3 < S.cosChia
```

### C.2. The bound `cos χ_a > 1 / 3`

> Schwarzschild, page 9 of the translation: the pressure at the centre stays finite as long as
> `Ra > 9 / 8 α`.

**`GeneralRelativity.IncompressibleSphere.one_third_lt_cosChia_iff_sq`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L269).

```lean
lemma one_third_lt_cosChia_iff_sq : 1 / 3 < S.cosChia ↔ S.Ra ^ 2 < 8 / 9 * S.Rc ^ 2
```

**`GeneralRelativity.IncompressibleSphere.one_third_lt_cosChia_iff_Ra_lt`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L280).

> `cos χ_a > 1 / 3` if and only if `Ra < √(8 / 9) Rc`.

```lean
lemma one_third_lt_cosChia_iff_Ra_lt : 1 / 3 < S.cosChia ↔ S.Ra < √(8 / 9) * S.Rc
```

**`GeneralRelativity.IncompressibleSphere.one_third_lt_cosChia_iff_rs`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L287).

> `cos χ_a > 1 / 3` if and only if `9 / 8 α < Ra` (Schwarzschild, page 9).

```lean
lemma one_third_lt_cosChia_iff_rs : 1 / 3 < S.cosChia ↔ 9 / 8 * S.rs < S.Ra
```

**`GeneralRelativity.IncompressibleSphere.Ra_div_Rc_of_cosChia_eq`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L303).

> At the critical value `cos χ_a = 1 / 3` the ratio `Ra / Rc = sin χ_a` (Schwarzschild's
> fall velocity, (42)) equals `√(8 / 9)`.

```lean
lemma Ra_div_Rc_of_cosChia_eq (hc : S.cosChia = 1 / 3) : S.Ra / S.Rc = √(8 / 9)
```

## D. The metric coefficients

> The interior metric (35) is written in the areal radius `r = Rc sin χ`; the relation with the
> form in `χ` is a lemma (`gttIn_Rc_mul_sin`, `grrIn_Rc_mul_sin`), not a definition. The metric
> coefficients are taken up to the sign of the signature.

**`GeneralRelativity.IncompressibleSphere.gttIn`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L323).

> The interior coefficient `g_tt` in the areal radius `r`, Schwarzschild (35):
> `(3 / 2 cos χ_a - 1 / 2 √(1 - r ^ 2 / Rc ^ 2)) ^ 2`.

```lean
def gttIn (r : ℝ) : ℝ
```

**`GeneralRelativity.IncompressibleSphere.grrIn`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L328).

> The interior coefficient `g_rr` in the areal radius `r`, Schwarzschild (35):
> `1 / (1 - r ^ 2 / Rc ^ 2)`.

```lean
def grrIn (r : ℝ) : ℝ
```

**`GeneralRelativity.IncompressibleSphere.gttOut`**, a def, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L331).

> The exterior coefficient `g_tt = 1 - α / r`, Schwarzschild (36).

```lean
def gttOut (r : ℝ) : ℝ
```

**`GeneralRelativity.IncompressibleSphere.grrOut`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L334).

> The exterior coefficient `g_rr = 1 / (1 - α / r)`, Schwarzschild (36).

```lean
def grrOut (r : ℝ) : ℝ
```

### D.1. The interior metric in the angle `χ`

**`GeneralRelativity.IncompressibleSphere.one_sub_sin_sq`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L342).

```lean
lemma one_sub_sin_sq (χ : ℝ) :
    1 - (S.Rc * Real.sin χ) ^ 2 / S.Rc ^ 2 = Real.cos χ ^ 2
```

**`GeneralRelativity.IncompressibleSphere.gttIn_Rc_mul_sin`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L348).

> Schwarzschild (35): in the angle `χ`, `g_tt = ((3 cos χ_a - cos χ) / 2) ^ 2`.

```lean
lemma gttIn_Rc_mul_sin {χ : ℝ} (h0 : 0 ≤ χ) (hπ : χ ≤ π / 2) :
    S.gttIn (S.Rc * Real.sin χ) = ((3 * S.cosChia - Real.cos χ) / 2) ^ 2
```

**`GeneralRelativity.IncompressibleSphere.grrIn_Rc_mul_sin`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L356).

> Schwarzschild (35): in the angle `χ`, the coefficient of `dχ ^ 2` is `Rc ^ 2`.

```lean
lemma grrIn_Rc_mul_sin {χ : ℝ} (hc : Real.cos χ ≠ 0) :
    S.grrIn (S.Rc * Real.sin χ) * (S.Rc * Real.cos χ) ^ 2 = S.Rc ^ 2
```

### D.2. The values at the surface agree

**`GeneralRelativity.IncompressibleSphere.gttIn_Ra`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L369).

> The interior and exterior formulas for `g_tt` take the same value at `r = Ra`.

```lean
lemma gttIn_Ra : S.gttIn S.Ra = S.gttOut S.Ra
```

**`GeneralRelativity.IncompressibleSphere.grrIn_Ra`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L379).

> The interior and exterior formulas for `g_rr` take the same value at `r = Ra`.

```lean
lemma grrIn_Ra : S.grrIn S.Ra = S.grrOut S.Ra
```

**`GeneralRelativity.IncompressibleSphere.eq_rs_of_gttIn_Ra`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L388).

> The exterior form of `g_tt` at the surface determines the Schwarzschild radius: if
> `g_tt (Ra) = 1 - a / Ra` then `a = α = Ra ^ 3 / Rc ^ 2`, which is Schwarzschild (40).

```lean
lemma eq_rs_of_gttIn_Ra {a : ℝ} (h : S.gttIn S.Ra = 1 - a / S.Ra) : a = S.rs
```

**`GeneralRelativity.IncompressibleSphere.gttIn_zero_of_cosChia_eq`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L396).

> At the critical value `cos χ_a = 1 / 3`, `g_tt` vanishes at the centre.

```lean
lemma gttIn_zero_of_cosChia_eq (hcrit : S.cosChia = 1 / 3) : S.gttIn 0 = 0
```

## E. Derivatives of the metric coefficients at the surface

### E.1. Two auxiliary derivatives

**`GeneralRelativity.IncompressibleSphere.hasDerivAt_one_sub_sq_div`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L413).

```lean
lemma hasDerivAt_one_sub_sq_div (Rc r : ℝ) :
    HasDerivAt (fun x : ℝ => 1 - x ^ 2 / Rc ^ 2) (-(2 * r) / Rc ^ 2) r
```

**`GeneralRelativity.IncompressibleSphere.hasDerivAt_sqrt_one_sub_sq_div`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L418).

```lean
lemma hasDerivAt_sqrt_one_sub_sq_div {Rc r : ℝ} (hu : 0 < 1 - r ^ 2 / Rc ^ 2) :
    HasDerivAt (fun x : ℝ => √(1 - x ^ 2 / Rc ^ 2))
      (-r / (Rc ^ 2 * √(1 - r ^ 2 / Rc ^ 2))) r
```

### E.2. Derivatives of `g_tt`

**`GeneralRelativity.IncompressibleSphere.gttIn_hasDerivAt`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L435).

> The interior `g_tt` is differentiable at `Ra` with derivative `Ra / Rc ^ 2`.

```lean
lemma gttIn_hasDerivAt : HasDerivAt S.gttIn (S.Ra / S.Rc ^ 2) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.deriv_gttIn_Ra`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L455).

> The derivative of the interior `g_tt` at `Ra` is `Ra / Rc ^ 2`.

```lean
lemma deriv_gttIn_Ra : deriv S.gttIn S.Ra = S.Ra / S.Rc ^ 2
```

**`GeneralRelativity.IncompressibleSphere.gttOut_hasDerivAt`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L459).

> The exterior `g_tt` is differentiable at `Ra` with derivative `α / Ra ^ 2 = Ra / Rc ^ 2`.

```lean
lemma gttOut_hasDerivAt : HasDerivAt S.gttOut (S.Ra / S.Rc ^ 2) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.deriv_gttOut_Ra`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L472).

> The derivative of the exterior `g_tt` at `Ra` is `Ra / Rc ^ 2`.

```lean
lemma deriv_gttOut_Ra : deriv S.gttOut S.Ra = S.Ra / S.Rc ^ 2
```

**`GeneralRelativity.IncompressibleSphere.deriv_gttIn_Ra_eq_deriv_gttOut_Ra`**, a lemma, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L476).

> The derivatives of the two formulas for `g_tt` agree at `r = Ra`.

```lean
lemma deriv_gttIn_Ra_eq_deriv_gttOut_Ra : deriv S.gttIn S.Ra = deriv S.gttOut S.Ra
```

### E.3. Derivatives of `g_rr`

**`GeneralRelativity.IncompressibleSphere.grrIn_hasDerivAt`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L487).

> The interior `g_rr` is differentiable at `Ra` with derivative
> `2 Ra / (Rc ^ 2 cos χ_a ^ 4)`.

```lean
lemma grrIn_hasDerivAt :
    HasDerivAt S.grrIn (2 * S.Ra / (S.Rc ^ 2 * S.cosChia ^ 4)) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.deriv_grrIn_Ra`**, a lemma, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L503).

> The derivative of the interior `g_rr` at `Ra`.

```lean
lemma deriv_grrIn_Ra : deriv S.grrIn S.Ra = 2 * S.Ra / (S.Rc ^ 2 * S.cosChia ^ 4)
```

**`GeneralRelativity.IncompressibleSphere.grrOut_hasDerivAt`**, a lemma, [line 508](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L508).

> The exterior `g_rr` is differentiable at `Ra` with derivative
> `- Ra / (Rc ^ 2 cos χ_a ^ 4)`.

```lean
lemma grrOut_hasDerivAt :
    HasDerivAt S.grrOut (-(S.Ra / (S.Rc ^ 2 * S.cosChia ^ 4))) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.deriv_grrOut_Ra`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L531).

> The derivative of the exterior `g_rr` at `Ra`.

```lean
lemma deriv_grrOut_Ra : deriv S.grrOut S.Ra = -(S.Ra / (S.Rc ^ 2 * S.cosChia ^ 4))
```

**`GeneralRelativity.IncompressibleSphere.deriv_grrIn_Ra_ne_deriv_grrOut_Ra`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L536).

> The derivatives of the two formulas for `g_rr` differ at `r = Ra`, in the curvature
> coordinate `r`.

```lean
lemma deriv_grrIn_Ra_ne_deriv_grrOut_Ra : deriv S.grrIn S.Ra ≠ deriv S.grrOut S.Ra
```

## F. The glued metric coefficients

> The glued coefficients use the interior formula for `r ≤ Ra` and the exterior formula
> beyond. The glued `g_tt` is differentiable at `Ra`; the glued `g_rr` is continuous but not
> differentiable at `Ra`, since its one-sided derivatives differ.

**`GeneralRelativity.IncompressibleSphere.gttGlue`**, a def, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L557).

> The glued `g_tt`: interior formula for `r ≤ Ra`, exterior formula beyond.

```lean
def gttGlue (r : ℝ) : ℝ
```

**`GeneralRelativity.IncompressibleSphere.grrGlue`**, a def, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L560).

> The glued `g_rr`: interior formula for `r ≤ Ra`, exterior formula beyond.

```lean
def grrGlue (r : ℝ) : ℝ
```

**`GeneralRelativity.IncompressibleSphere.gttGlue_hasDerivAt`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L563).

> The glued `g_tt` is differentiable at `Ra` with derivative `Ra / Rc ^ 2`.

```lean
lemma gttGlue_hasDerivAt : HasDerivAt S.gttGlue (S.Ra / S.Rc ^ 2) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.gttGlue_continuousAt`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L581).

> The glued `g_tt` is continuous at `Ra`.

```lean
lemma gttGlue_continuousAt : ContinuousAt S.gttGlue S.Ra
```

**`GeneralRelativity.IncompressibleSphere.grrGlue_hasDerivWithinAt_Iic`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L585).

> The left derivative of the glued `g_rr` at `Ra` (interior formula).

```lean
lemma grrGlue_hasDerivWithinAt_Iic :
    HasDerivWithinAt S.grrGlue (2 * S.Ra / (S.Rc ^ 2 * S.cosChia ^ 4)) (Set.Iic S.Ra) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.grrGlue_hasDerivWithinAt_Ici`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L593).

> The right derivative of the glued `g_rr` at `Ra` (exterior formula).

```lean
lemma grrGlue_hasDerivWithinAt_Ici :
    HasDerivWithinAt S.grrGlue (-(S.Ra / (S.Rc ^ 2 * S.cosChia ^ 4))) (Set.Ici S.Ra) S.Ra
```

**`GeneralRelativity.IncompressibleSphere.grrGlue_continuousAt`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L604).

> The glued `g_rr` is continuous at `Ra`.

```lean
lemma grrGlue_continuousAt : ContinuousAt S.grrGlue S.Ra
```

**`GeneralRelativity.IncompressibleSphere.grrGlue_not_differentiableAt`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L611).

> The glued `g_rr` is not differentiable at `Ra`: its left and right derivatives, unique on
> `Iic Ra` and `Ici Ra`, differ.

```lean
lemma grrGlue_not_differentiableAt : ¬ DifferentiableAt ℝ S.grrGlue S.Ra
```

## G. Consequences for the junction

> In a Gaussian coordinate `l` along the radius, `dr / dl = 1 / √g_rr` and
> `d g_tt / dl = g_tt' / √g_rr`. Both quantities take the same value at `Ra` from the two
> formulas (Lichnerowicz, chapter III, section 28, evaluated at the surface). The coordinate `l`
> itself is not constructed here.

**`GeneralRelativity.IncompressibleSphere.one_div_sqrt_grrIn_Ra`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L640).

> `dr / dl = 1 / √g_rr` takes the same value at `Ra` from the two formulas.

```lean
lemma one_div_sqrt_grrIn_Ra : 1 / √(S.grrIn S.Ra) = 1 / √(S.grrOut S.Ra)
```

**`GeneralRelativity.IncompressibleSphere.deriv_gttIn_div_sqrt_grrIn_Ra`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean#L644).

> `d g_tt / dl = g_tt' / √g_rr` takes the same value at `Ra` from the two formulas.

```lean
lemma deriv_gttIn_div_sqrt_grrIn_Ra :
    deriv S.gttIn S.Ra / √(S.grrIn S.Ra) = deriv S.gttOut S.Ra / √(S.grrOut S.Ra)
```

## H. A numerical instance

> The sphere with `Rc = 1`, `Ra = 3 / 5` and `ρ₀ = 1`: `cos χ_a = 4 / 5`, `α = 27 / 125`,
> `9 / 8 α < Ra`, central pressure `1 / 7`.

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean)
