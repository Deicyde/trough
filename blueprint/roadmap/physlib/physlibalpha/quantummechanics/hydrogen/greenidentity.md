---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.deriv_ofReal, PhyslibAlpha.Hydrogen.deriv_schwartz, PhyslibAlpha.Hydrogen.integral_ofReal_mul_sum_deriv_deriv, PhyslibAlpha.Hydrogen.deriv_radial_mul, PhyslibAlpha.Hydrogen.deriv_deriv_radial_mul, PhyslibAlpha.Hydrogen.regG, PhyslibAlpha.Hydrogen.regG', PhyslibAlpha.Hydrogen.regG''
statement: formalized
proof: formalized
---

# Green's identity and regularised radial functions

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.GreenIdentity`, [PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean): 18 declarations, 12 with a docstring.

## i. Overview

> For a `C²` function `u` on `Space d` such that `u`, `∂ᵢu` and `∂ᵢ∂ᵢu` are polynomially bounded and
> a Schwartz map `f`, Green's identity `∫ u Δf = ∫ (Δu) f` holds (two integrations by parts).
> Functions of the form `R(‖y‖) Q(y)` are in general not smooth at the origin; replacing `‖y‖` by
> the regularised radius `ρ_ε = √(‖y‖² + ε²)` makes them smooth for `ε ≠ 0`. This module provides
> the derivatives of `G(‖y‖²) Q(y)` and the polynomial bounds needed to apply Green's identity to the
> regularised functions, uniformly in `|ε| ≤ 1` when `R` is a polynomial times `e^(-κr)`.

## ii. Key results

> - `integral_ofReal_mul_sum_deriv_deriv` : Green's identity `∫ u Σᵢ∂ᵢ∂ᵢf = ∫ (Σᵢ∂ᵢ∂ᵢu) f`.
> - `deriv_radial_mul`, `deriv_deriv_radial_mul` : first and second coordinate derivatives of
>   `G(‖y‖²) Q(y)` at every point.
> - `regG`, `hasDerivAt_regG`, `hasDerivAt_regG'` : the regularised profile `s ↦ f(√(s + ε²))` and
>   its derivatives.
> - `isPolyBounded_regG`, `isPolyBounded_regG'`, `isPolyBounded_regG''`,
>   `exists_abs_poly_exp_regRadius_le` : polynomial bounds, uniform in `|ε| ≤ 1`.

## iv. References

> - None.

## A. Green's identity for smooth functions

**`PhyslibAlpha.Hydrogen.deriv_ofReal`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L60).

> The derivative of a real function, viewed as a complex function.

```lean
lemma deriv_ofReal {d : ℕ} {u : Space d → ℝ} (hu : Differentiable ℝ u) (i : Fin d) (y : Space d) :
    ∂[i] (fun y => (u y : ℂ)) y = ((∂[i] u y : ℝ) : ℂ)
```

**`PhyslibAlpha.Hydrogen.deriv_schwartz`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L68).

> The coordinate derivative of a Schwartz map, as a Schwartz map.

```lean
lemma deriv_schwartz {d : ℕ} (f : 𝓢(Space d, ℂ)) (i : Fin d) :
    ∂[i] ⇑f = ⇑(∂_{Space.basis i} f : 𝓢(Space d, ℂ))
```

**`PhyslibAlpha.Hydrogen.integral_ofReal_mul_sum_deriv_deriv`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L75).

> **Green's identity for smooth functions.** If `u` is `C²` and `u`, `∂ᵢu`, `∂ᵢ∂ᵢu` are
> polynomially bounded, then `∫ u Σᵢ ∂ᵢ∂ᵢ f = ∫ (Σᵢ ∂ᵢ∂ᵢ u) f` for every Schwartz map `f`.

```lean
lemma integral_ofReal_mul_sum_deriv_deriv {d : ℕ} {u : Space d → ℝ} (hu : ContDiff ℝ 2 u)
    (hb0 : IsPolyBounded u) (hb1 : ∀ i, IsPolyBounded (∂[i] u))
    (hb2 : ∀ i, IsPolyBounded (∂[i] (∂[i] u))) (f : 𝓢(Space d, ℂ)) :
    ∫ y, (u y : ℂ) * ∑ i, ∂[i] (∂[i] ⇑f) y =
      ∫ y, ((∑ i, ∂[i] (∂[i] u) y : ℝ) : ℂ) * f y
```

## B. Derivatives of radial functions

**`PhyslibAlpha.Hydrogen.deriv_radial_mul`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L138).

> `∂ᵢ (G(‖y‖²) Q) = G ∂ᵢQ + Q G' 2yᵢ` at every point, if `G` is differentiable on `[0, ∞)`.

```lean
lemma deriv_radial_mul {d : ℕ} {G G' : ℝ → ℝ} (hG : ∀ s, 0 ≤ s → HasDerivAt G (G' s) s)
    {Q : Space d → ℝ} (hQ : Differentiable ℝ Q) (i : Fin d) :
    ∂[i] (fun y => G (‖y‖ ^ 2) * Q y) =
      fun y => G (‖y‖ ^ 2) * ∂[i] Q y + Q y * (G' (‖y‖ ^ 2) * (2 * y i))
```

**`PhyslibAlpha.Hydrogen.deriv_deriv_radial_mul`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L147).

> `∂ᵢ∂ᵢ (G(‖y‖²) Q) = G ∂ᵢ∂ᵢQ + 4 G' yᵢ ∂ᵢQ + (2 G' + 4 yᵢ² G'') Q` at every point.

```lean
lemma deriv_deriv_radial_mul {d : ℕ} {G G' G'' : ℝ → ℝ}
    (hG : ∀ s, 0 ≤ s → HasDerivAt G (G' s) s) (hG' : ∀ s, 0 ≤ s → HasDerivAt G' (G'' s) s)
    {Q : Space d → ℝ} (hQ : ContDiff ℝ 2 Q) (i : Fin d) (x : Space d) :
    ∂[i] (∂[i] (fun y => G (‖y‖ ^ 2) * Q y)) x = G (‖x‖ ^ 2) * ∂[i] (∂[i] Q) x +
      4 * G' (‖x‖ ^ 2) * (x i * ∂[i] Q x) +
        (2 * G' (‖x‖ ^ 2) + 4 * x i ^ 2 * G'' (‖x‖ ^ 2)) * Q x
```

## C. Regularised radial profiles

**`PhyslibAlpha.Hydrogen.regG`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L181).

> The regularised radial profile `s ↦ f(√(s + ε²))`, smooth also at `s = 0`.

```lean
def regG (f : ℝ → ℝ) (ε s : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.regG'`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L184).

> The derivative of `regG f ε`.

```lean
def regG' (f' : ℝ → ℝ) (ε s : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.regG''`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L188).

> The second derivative of `regG f ε`.

```lean
def regG'' (f' f'' : ℝ → ℝ) (ε s : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_regG`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L192).

```lean
lemma hasDerivAt_regG {f f' : ℝ → ℝ} (hf : ∀ r, 0 < r → HasDerivAt f (f' r) r) {ε s : ℝ}
    (hs : 0 < s + ε ^ 2) : HasDerivAt (regG f ε) (regG' f' ε s) s
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_regG'`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L199).

```lean
lemma hasDerivAt_regG' {f' f'' : ℝ → ℝ} (hf : ∀ r, 0 < r → HasDerivAt f' (f'' r) r) {ε s : ℝ}
    (hs : 0 < s + ε ^ 2) : HasDerivAt (regG' f' ε) (regG'' f' f'' ε s) s
```

**`PhyslibAlpha.Hydrogen.abs_le_regRadius`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L208).

> The regularised radius `√(‖y‖² + ε²)` is at least `|ε|`.

```lean
lemma abs_le_regRadius {d : ℕ} (ε : ℝ) (y : Space d) : |ε| ≤ Real.sqrt (‖y‖ ^ 2 + ε ^ 2)
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_regRadius`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L211).

```lean
lemma isPolyBounded_regRadius {d : ℕ} (ε : ℝ) :
    IsPolyBounded (fun y : Space d => Real.sqrt (‖y‖ ^ 2 + ε ^ 2))
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_poly_exp_regRadius`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L221).

> A polynomial in the regularised radius times `e^(-κρ)`, `κ ≥ 0`, is polynomially bounded.

```lean
lemma isPolyBounded_poly_exp_regRadius {d : ℕ} (p : Polynomial ℝ) {κ : ℝ} (hκ : 0 ≤ κ)
    (ε : ℝ) : IsPolyBounded (fun y : Space d =>
      p.eval (Real.sqrt (‖y‖ ^ 2 + ε ^ 2)) * Real.exp (-(κ * Real.sqrt (‖y‖ ^ 2 + ε ^ 2))))
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_inv_regRadius`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L229).

```lean
lemma isPolyBounded_inv_regRadius {d : ℕ} {ε : ℝ} (hε : ε ≠ 0) :
    IsPolyBounded (fun y : Space d => (Real.sqrt (‖y‖ ^ 2 + ε ^ 2))⁻¹)
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_regG`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L237).

> The profiles `G_ε`, `G_ε'`, `G_ε''` of `f(r) = p(r) e^(-κr)` on `‖y‖²` are polynomially
> bounded for fixed `ε ≠ 0`.

```lean
lemma isPolyBounded_regG {d : ℕ} (p : Polynomial ℝ) {κ : ℝ} (hκ : 0 ≤ κ) (ε : ℝ) :
    IsPolyBounded (fun y : Space d =>
      regG (fun r => p.eval r * Real.exp (-(κ * r))) ε (‖y‖ ^ 2))
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_regG'`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L242).

```lean
lemma isPolyBounded_regG' {d : ℕ} (q : Polynomial ℝ) {κ : ℝ} (hκ : 0 ≤ κ) {ε : ℝ}
    (hε : ε ≠ 0) :
    IsPolyBounded (fun y : Space d =>
      regG' (fun r => q.eval r * Real.exp (-(κ * r))) ε (‖y‖ ^ 2))
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_regG''`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L253).

```lean
lemma isPolyBounded_regG'' {d : ℕ} (q q' : Polynomial ℝ) {κ : ℝ} (hκ : 0 ≤ κ) {ε : ℝ}
    (hε : ε ≠ 0) :
    IsPolyBounded (fun y : Space d =>
      regG'' (fun r => q.eval r * Real.exp (-(κ * r))) (fun r => q'.eval r * Real.exp (-(κ * r)))
        ε (‖y‖ ^ 2))
```

**`PhyslibAlpha.Hydrogen.exists_abs_poly_exp_regRadius_le`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean#L275).

> A bound for `p(ρ) e^(-κρ)`, `ρ = √(‖y‖² + ε²)`, uniform in `|ε| ≤ 1`.

```lean
lemma exists_abs_poly_exp_regRadius_le {d : ℕ} (p : Polynomial ℝ) {κ : ℝ} (hκ : 0 ≤ κ) :
    ∃ (C : ℝ) (k : ℕ), 0 ≤ C ∧ ∀ ε : ℝ, |ε| ≤ 1 → ∀ y : Space d,
      |p.eval (Real.sqrt (‖y‖ ^ 2 + ε ^ 2)) * Real.exp (-(κ * Real.sqrt (‖y‖ ^ 2 + ε ^ 2)))| ≤
        C * (1 + ‖y‖) ^ k
```

## Depends on

- [Polynomially bounded functions and integrability on `Space d`](polybounded.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/GreenIdentity.lean)
