---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.IsPolyBounded, PhyslibAlpha.Hydrogen.IsPolyBounded.one_le_one_add_norm, PhyslibAlpha.Hydrogen.IsPolyBounded.const, PhyslibAlpha.Hydrogen.IsPolyBounded.add, PhyslibAlpha.Hydrogen.IsPolyBounded.mul, PhyslibAlpha.Hydrogen.IsPolyBounded.pow, PhyslibAlpha.Hydrogen.IsPolyBounded.coord, PhyslibAlpha.Hydrogen.IsPolyBounded.norm
statement: formalized
proof: formalized
---

# Polynomially bounded functions and integrability on `Space d`

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.PolyBounded`, [PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean): 21 declarations, 10 with a docstring.

## i. Overview

> A function `f : Space d → ℝ` is polynomially bounded if `|f y| ≤ C (1 + ‖y‖)^k`. Such functions
> form an algebra containing the coordinates, `‖y‖` and polynomials; multiplied by `e^(-c‖y‖)`
> (`c > 0`) they are square integrable, multiplied by a Schwartz map they are integrable, and for
> `d ≥ 2` this stays true after an additional factor `‖y‖⁻¹`.

## ii. Key results

> - `IsPolyBounded` : at most polynomial growth `|f y| ≤ C (1 + ‖y‖)^k`.
> - `integrable_sq_of_le_mul_exp` : `f²` is integrable if `|f| ≤ |g| e^(-c‖y‖)` with `g` polynomially
>   bounded and `c > 0`.
> - `IsPolyBounded.integrable_ofReal_mul_schwartz` : polynomially bounded times Schwartz is
>   integrable.
> - `IsPolyBounded.integrable_inv_norm_mul` : the same with an extra factor `‖y‖⁻¹`, for `d ≥ 2`.

## iv. References

> - None.

## A. Polynomially bounded functions

**`PhyslibAlpha.Hydrogen.IsPolyBounded`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L55).

> `f` grows at most polynomially: `|f y| ≤ C (1 + ‖y‖)^k` for some `C ≥ 0` and `k`.

```lean
def IsPolyBounded {d : ℕ} (f : Space d → ℝ) : Prop
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.one_le_one_add_norm`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L62).

```lean
lemma one_le_one_add_norm (y : Space d) : 1 ≤ 1 + ‖y‖
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.const`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L65).

```lean
lemma const (a : ℝ) : IsPolyBounded (fun _ : Space d => a)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.add`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L68).

```lean
lemma add (hf : IsPolyBounded f) (hg : IsPolyBounded g) :
    IsPolyBounded (fun y => f y + g y)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.mul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L82).

```lean
lemma mul (hf : IsPolyBounded f) (hg : IsPolyBounded g) :
    IsPolyBounded (fun y => f y * g y)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.pow`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L92).

```lean
lemma pow (hf : IsPolyBounded f) (n : ℕ) : IsPolyBounded (fun y => f y ^ n)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.coord`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L97).

```lean
lemma coord (i : Fin d) : IsPolyBounded (fun y : Space d => y i)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.norm`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L103).

```lean
lemma norm : IsPolyBounded (fun y : Space d => ‖y‖)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.toFun`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L109).

> Polynomials in the coordinates are polynomially bounded.

```lean
lemma toFun (P : MvPolynomial (Fin d) ℝ) : IsPolyBounded (toFun P)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.polynomial_eval`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L116).

> A polynomial of a polynomially bounded function is polynomially bounded.

```lean
lemma polynomial_eval (p : Polynomial ℝ) (hf : IsPolyBounded f) :
    IsPolyBounded (fun y => p.eval (f y))
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.sum`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L124).

```lean
lemma sum {ι : Type*} (s : Finset ι) {F : ι → Space d → ℝ} (h : ∀ i ∈ s, IsPolyBounded (F i)) :
    IsPolyBounded (fun y => ∑ i ∈ s, F i y)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.mono`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L134).

```lean
lemma mono (hf : IsPolyBounded f) {c : ℝ} (hc : 0 ≤ c) (h : ∀ y, |g y| ≤ c * |f y|) :
    IsPolyBounded g
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.of_abs_le_const`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L140).

```lean
lemma of_abs_le_const {c : ℝ} (h : ∀ y, |g y| ≤ c) : IsPolyBounded g
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.neg`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L144).

```lean
lemma neg (hf : IsPolyBounded f) : IsPolyBounded (fun y => -f y)
```

## B. Exponential decay and integrability

**`PhyslibAlpha.Hydrogen.one_add_pow_mul_exp_neg_le`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L156).

> `(1 + t)^m e^(-c t) ≤ e^c m! / c^m` for `c > 0` and `t ≥ 0`, from `x^m / m! ≤ e^x`.

```lean
lemma one_add_pow_mul_exp_neg_le {c : ℝ} (hc : 0 < c) (m : ℕ) {t : ℝ} (ht : 0 ≤ t) :
    (1 + t) ^ m * Real.exp (-(c * t)) ≤ Real.exp c * m.factorial / c ^ m
```

**`PhyslibAlpha.Hydrogen.integrable_sq_of_le_mul_exp`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L171).

> If `|f y| ≤ |g y| e^(-c‖y‖)` with `g` polynomially bounded and `c > 0`, then `f²` is
> integrable: it is bounded by a multiple of `(1 + ‖y‖)^(-(d+1))`.

```lean
lemma integrable_sq_of_le_mul_exp {d : ℕ} {f g : Space d → ℝ} {c : ℝ} (hc : 0 < c)
    (hfm : AEStronglyMeasurable f) (hg : IsPolyBounded g)
    (hfg : ∀ y, |f y| ≤ |g y| * Real.exp (-(c * ‖y‖))) :
    Integrable (fun y => f y ^ 2)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.integrable_ofReal_mul_schwartz`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L202).

> A polynomially bounded function times a Schwartz map is integrable.

```lean
lemma IsPolyBounded.integrable_ofReal_mul_schwartz {d : ℕ} {u : Space d → ℝ}
    (hu : IsPolyBounded u) (hm : AEStronglyMeasurable u) (g : 𝓢(Space d, ℂ)) :
    Integrable (fun y => (u y : ℂ) * g y)
```

**`PhyslibAlpha.Hydrogen.integrable_inv_norm_mul_one_add_norm_pow`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L225).

> `‖y‖⁻¹ (1 + ‖y‖)^(-M)` is integrable on `Space d` for `d ≥ 2` and `M ≥ d`, by polar
> coordinates: the radial integrand `r^(d-2) (1 + r)^(-M)` is at most `(1 + r)^(-2)`.

```lean
lemma integrable_inv_norm_mul_one_add_norm_pow {d : ℕ} (hd : 2 ≤ d) {M : ℕ} (hM : d ≤ M) :
    Integrable (fun y : Space d => ‖y‖⁻¹ * ((1 + ‖y‖) ^ M)⁻¹)
```

**`PhyslibAlpha.Hydrogen.Polynomial.exists_abs_eval_le`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L257).

> A real polynomial grows at most polynomially: `|p(t)| ≤ C (1 + |t|)^k`.

```lean
lemma Polynomial.exists_abs_eval_le (p : Polynomial ℝ) :
    ∃ (C : ℝ) (k : ℕ), 0 ≤ C ∧ ∀ t, |p.eval t| ≤ C * (1 + |t|) ^ k
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.integrable_abs_mul_norm_schwartz`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L279).

> A polynomially bounded function times the norm of a Schwartz map is integrable.

```lean
lemma IsPolyBounded.integrable_abs_mul_norm_schwartz {d : ℕ} {u : Space d → ℝ}
    (hu : IsPolyBounded u) (hm : AEStronglyMeasurable u) (g : 𝓢(Space d, ℂ)) :
    Integrable (fun y => |u y| * ‖g y‖)
```

**`PhyslibAlpha.Hydrogen.IsPolyBounded.integrable_inv_norm_mul`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean#L286).

> `‖y‖⁻¹` times a polynomially bounded function times the norm of a Schwartz map is integrable
> in dimension `d ≥ 2`.

```lean
lemma IsPolyBounded.integrable_inv_norm_mul {d : ℕ} (hd : 2 ≤ d) {u : Space d → ℝ}
    (hu : IsPolyBounded u) (hm : AEStronglyMeasurable u) (g : 𝓢(Space d, ℂ)) :
    Integrable (fun y => ‖y‖⁻¹ * (|u y| * ‖g y‖))
```

## Depends on

- [The degeneracy of the hydrogen bound states](degeneracy.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/PolyBounded.lean)
