---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.EntireCoeff, PhyslibAlpha.Hydrogen.psum, PhyslibAlpha.Hydrogen.dcoeff, PhyslibAlpha.Hydrogen.succ_mul_pow_le_pow_succ, PhyslibAlpha.Hydrogen.EntireCoeff.summable, PhyslibAlpha.Hydrogen.EntireCoeff.derivCoeff, PhyslibAlpha.Hydrogen.EntireCoeff.shift, PhyslibAlpha.Hydrogen.psum_eq_add
statement: formalized
proof: formalized
---

# Quantisation of the hydrogen levels

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.RadialQuantization`, [PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean): 33 declarations, 15 with a docstring.

> Why the bound-state energies of hydrogen are discrete: a square integrable solution of the radial
> equation of the form `ρ^(l+1) e^(-κρ) × (power series)` exists only for `κ = 1/ν` with a natural
> number `ν > l`, and is then the radial function `u_{νl}` of `RadialFunctions`.

## i. Overview

> In Rydberg units a bound state of energy `-κ²`, `κ > 0`, and angular momentum `l` has a reduced
> radial function solving
>
> `u'' = (l(l+1)/ρ² - 2/ρ + κ²) u`   on `(0, ∞)`.
>
> We take the standard ansatz `u(ρ) = ρ^(l+1) e^(-κρ) Σ_k c_k ρ^k` with an everywhere convergent
> power series and `c_0 ≠ 0` (`radialSeries`). Then:
>
> - the series can be differentiated termwise (`hasDerivAt_psum`), and the radial equation turns
>   into `ρ W'' + (2l + 2 - 2κρ) W' + (2 - 2κ(l + 1)) W = 0` for `W = Σ c_k ρ^k`; comparing
>   coefficients (`coeff_eq_zero_of_psum`) gives the recursion
>   `(k + 1)(k + 2l + 2) c_{k+1} = (2κ(k + l + 1) - 2) c_k` (`recursion_of_radial_ode`);
> - if `κ(N + l + 1) = 1` for some `N`, the recursion stops after `c_N` and reproduces the Laguerre
>   polynomial `L_N^(2l+1)(2κρ)`, so `u` is a multiple of `u_{νl}` with `ν = N + l + 1`
>   (`radialSeries_eq_of_terminating`);
> - otherwise all `c_k` are non-zero and eventually `c_{k+1}/c_k ≥ (3κ/2)/(k + 1)`, so
>   `W(ρ) ≥ δ e^(3κρ/2) - (polynomial)`; then `u(ρ)² ≥ 1` for large `ρ` and `u` is not square
>   integrable (`not_integrableOn_of_nonterminating`).
>
> Together this is `radial_quantization`: normalisability forces `E = -1/ν²`.
>
> What is assumed here: the power series ansatz, i.e. that the solution regular at the origin is
> `ρ^(l+1) e^(-κρ)` times an entire function. That every solution with `u(ρ) → 0` as `ρ → 0⁺` has
> this form is `radial_regular_solution` in `RadialCompleteness`, which also states the
> quantisation without the ansatz (`radial_quantization_of_tendsto`).

## ii. Key results

> - `hasDerivAt_psum`, `coeff_eq_zero_of_psum`: termwise differentiation and the identity theorem
>   for everywhere convergent power series on `(0, ∞)`.
> - `recursion_of_radial_ode`: the coefficient recursion.
> - `radialSeries_eq_of_terminating`: the terminating solutions are the hydrogen radial functions.
> - `not_integrableOn_of_nonterminating`: non-terminating solutions are not normalisable.
> - `radial_quantization`: the quantisation of the hydrogen levels.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.7.
> - H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*, Springer
>   (1957).

## A. Power series with infinite radius of convergence

**`PhyslibAlpha.Hydrogen.EntireCoeff`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L84).

> The coefficients `c` define a power series that converges absolutely on all of `ℝ`.

```lean
def EntireCoeff (c : ℕ → ℝ) : Prop
```

**`PhyslibAlpha.Hydrogen.psum`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L87).

> The power series `Σ c_k x^k`.

```lean
def psum (c : ℕ → ℝ) (x : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.dcoeff`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L90).

> The coefficients of the derivative, `(k + 1) c_{k+1}`.

```lean
def dcoeff (c : ℕ → ℝ) (k : ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.succ_mul_pow_le_pow_succ`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L94).

```lean
lemma succ_mul_pow_le_pow_succ {r : ℝ} (hr : 0 ≤ r) (k : ℕ) :
    ((k : ℝ) + 1) * r ^ k ≤ (1 + r) ^ (k + 1)
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.summable`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L105).

```lean
lemma EntireCoeff.summable (hc : EntireCoeff c) (x : ℝ) : Summable fun k => c k * x ^ k
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.derivCoeff`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L109).

```lean
lemma EntireCoeff.derivCoeff (hc : EntireCoeff c) : EntireCoeff (dcoeff c)
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.shift`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L118).

```lean
lemma EntireCoeff.shift (hc : EntireCoeff c) : EntireCoeff fun k => c (k + 1)
```

**`PhyslibAlpha.Hydrogen.psum_eq_add`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L126).

```lean
lemma psum_eq_add (hc : EntireCoeff c) (x : ℝ) :
    psum c x = c 0 + x * psum (fun k => c (k + 1)) x
```

**`PhyslibAlpha.Hydrogen.psum_zero`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L133).

```lean
lemma psum_zero (c : ℕ → ℝ) : psum c 0 = c 0
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_psum`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L138).

> Termwise differentiation of an everywhere convergent power series.

```lean
lemma hasDerivAt_psum (hc : EntireCoeff c) (x : ℝ) :
    HasDerivAt (psum c) (psum (dcoeff c) x) x
```

**`PhyslibAlpha.Hydrogen.coeff_eq_zero_of_psum`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L173).

> A power series that vanishes on `(0, ∞)` has vanishing coefficients.

```lean
lemma coeff_eq_zero_of_psum (n : ℕ) : ∀ c : ℕ → ℝ, EntireCoeff c →
    (∀ x : ℝ, 0 < x → psum c x = 0) → c n = 0
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.unshift`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L198).

```lean
lemma EntireCoeff.unshift (h : EntireCoeff fun k => c (k + 1)) : EntireCoeff c
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.add`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L203).

```lean
lemma EntireCoeff.add {c' : ℕ → ℝ} (hc : EntireCoeff c) (hc' : EntireCoeff c') :
    EntireCoeff fun k => c k + c' k
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.const_mul`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L211).

```lean
lemma EntireCoeff.const_mul (hc : EntireCoeff c) (a : ℝ) : EntireCoeff fun k => a * c k
```

**`PhyslibAlpha.Hydrogen.psum_add`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L215).

```lean
lemma psum_add {c' : ℕ → ℝ} (hc : EntireCoeff c) (hc' : EntireCoeff c') (x : ℝ) :
    psum (fun k => c k + c' k) x = psum c x + psum c' x
```

**`PhyslibAlpha.Hydrogen.psum_const_mul`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L220).

```lean
lemma psum_const_mul (c : ℕ → ℝ) (a x : ℝ) : psum (fun k => a * c k) x = a * psum c x
```

**`PhyslibAlpha.Hydrogen.dcoeff_eq`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L224).

```lean
lemma dcoeff_eq (c : ℕ → ℝ) : (fun k : ℕ => ((k + 1 : ℕ) : ℝ) * c (k + 1)) = dcoeff c
```

**`PhyslibAlpha.Hydrogen.EntireCoeff.natMul`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L227).

```lean
lemma EntireCoeff.natMul (hc : EntireCoeff c) : EntireCoeff fun k => (k : ℝ) * c k
```

**`PhyslibAlpha.Hydrogen.mul_psum_dcoeff`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L233).

> `x Σ_k (k + 1) c_{k+1} x^k = Σ_k k c_k x^k`.

```lean
lemma mul_psum_dcoeff (hc : EntireCoeff c) (x : ℝ) :
    x * psum (dcoeff c) x = psum (fun k => (k : ℝ) * c k) x
```

## B. The radial equation for a power series ansatz

**`PhyslibAlpha.Hydrogen.radialSeries`**, a def, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L245).

> The ansatz `u(ρ) = ρ^(l+1) e^(-κρ) Σ_k c_k ρ^k` for a bound state of energy `-κ²`.

```lean
def radialSeries (κ : ℝ) (l : ℕ) (c : ℕ → ℝ) (ρ : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_exp_neg_mul`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L250).

```lean
lemma hasDerivAt_exp_neg_mul (κ ρ : ℝ) :
    HasDerivAt (fun ρ => Real.exp (-(κ * ρ))) (Real.exp (-(κ * ρ)) * (-κ)) ρ
```

**`PhyslibAlpha.Hydrogen.radialSeriesD`**, a def, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L255).

> The first derivative of `radialSeries`.

```lean
def radialSeriesD (κ : ℝ) (l : ℕ) (c : ℕ → ℝ) (ρ : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_radialSeries`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L259).

```lean
lemma hasDerivAt_radialSeries (hc : EntireCoeff c) (ρ : ℝ) :
    HasDerivAt (radialSeries κ l c) (radialSeriesD κ l c ρ) ρ
```

**`PhyslibAlpha.Hydrogen.hasDerivAt_radialSeriesD`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L268).

```lean
lemma hasDerivAt_radialSeriesD (hc : EntireCoeff c) (ρ : ℝ) :
    HasDerivAt (radialSeriesD κ l c) (Real.exp (-(κ * ρ)) *
      (-κ * ((((l : ℝ) + 1) * ρ ^ l - κ * ρ ^ (l + 1)) * psum c ρ +
        ρ ^ (l + 1) * psum (dcoeff c) ρ) +
      ((((l : ℝ) + 1) * (l * ρ ^ (l - 1)) - κ * (((l : ℝ) + 1) * ρ ^ l)) * psum c ρ +
        (((l : ℝ) + 1) * ρ ^ l - κ * ρ ^ (l + 1)) * psum (dcoeff c) ρ +
          ((((l : ℝ) + 1) * ρ ^ l) * psum (dcoeff c) ρ +
            ρ ^ (l + 1) * psum (dcoeff (dcoeff c)) ρ)))) ρ
```

**`PhyslibAlpha.Hydrogen.radial_identity`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L287).

> The radial operator applied to the ansatz, in terms of the series `W`, `W'`, `W''`.

```lean
lemma radial_identity (κ ρ W W₁ W₂ E : ℝ) (l : ℕ) (hρ : ρ ≠ 0) :
    E * (-κ * ((((l : ℝ) + 1) * ρ ^ l - κ * ρ ^ (l + 1)) * W + ρ ^ (l + 1) * W₁) +
      ((((l : ℝ) + 1) * (l * ρ ^ (l - 1)) - κ * (((l : ℝ) + 1) * ρ ^ l)) * W +
        (((l : ℝ) + 1) * ρ ^ l - κ * ρ ^ (l + 1)) * W₁ +
          ((((l : ℝ) + 1) * ρ ^ l) * W₁ + ρ ^ (l + 1) * W₂))) -
      ((l : ℝ) * (l + 1) / ρ ^ 2 - 2 / ρ + κ ^ 2) * (ρ ^ (l + 1) * E * W) =
    ρ ^ l * E * (ρ * W₂ + (2 * l + 2 - 2 * κ * ρ) * W₁ + (2 - 2 * κ * (l + 1)) * W)
```

**`PhyslibAlpha.Hydrogen.recursion_of_radial_ode`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L306).

> **The coefficient recursion.** If the ansatz solves the radial equation with energy `-κ²`, the
> coefficients satisfy `(k + 1)(k + 2l + 2) c_{k+1} = (2κ(k + l + 1) - 2) c_k`.

```lean
lemma recursion_of_radial_ode (hc : EntireCoeff c)
    (hode : ∀ ρ : ℝ, 0 < ρ → deriv (deriv (radialSeries κ l c)) ρ =
      ((l : ℝ) * (l + 1) / ρ ^ 2 - 2 / ρ + κ ^ 2) * radialSeries κ l c ρ) (k : ℕ) :
    ((k : ℝ) + 1) * (k + 2 * l + 2) * c (k + 1) = (2 * κ * (k + l + 1) - 2) * c k
```

## C. Terminating series: the Laguerre polynomials

**`PhyslibAlpha.Hydrogen.RadialRec`**, an abbrev, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L342).

> The coefficient recursion `(k + 1)(k + 2l + 2) c_{k+1} = (2κ(k + l + 1) - 2) c_k`.

```lean
abbrev RadialRec (κ : ℝ) (l : ℕ) (c : ℕ → ℝ) : Prop
```

**`PhyslibAlpha.Hydrogen.coeff_of_terminating`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L347).

> If `κ (N + l + 1) = 1`, the recursion terminates after `c_N` and reproduces the coefficients
> of `L_N^(2l+1)(2κρ)`.

```lean
lemma coeff_of_terminating (hrec : RadialRec κ l c) {N : ℕ} (hN : κ * (N + l + 1) = 1) :
    (∀ k, k ≤ N → c k = c 0 / laguerreCoeff N (2 * l + 1) 0 * laguerreCoeff N (2 * l + 1) k *
      (2 * κ) ^ k) ∧ ∀ k, N < k → c k = 0
```

**`PhyslibAlpha.Hydrogen.radialSeries_eq_of_terminating`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L383).

> In the terminating case the ansatz is a multiple of the hydrogen radial function.

```lean
lemma radialSeries_eq_of_terminating (hrec : RadialRec κ l c) {N : ℕ}
    (hN : κ * (N + l + 1) = 1) (ρ : ℝ) :
    radialSeries κ l c ρ =
      c 0 / laguerreCoeff N (2 * l + 1) 0 * radialU (N + l + 1) l ρ
```

## D. Non-terminating series are not normalisable

**`PhyslibAlpha.Hydrogen.tendsto_pow_mul_exp_neg_mul`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L409).

```lean
lemma tendsto_pow_mul_exp_neg_mul (hκ : 0 < κ) (k : ℕ) :
    Tendsto (fun ρ : ℝ => ρ ^ k * Real.exp (-(κ * ρ))) atTop (𝓝 0)
```

**`PhyslibAlpha.Hydrogen.coeff_ne_zero`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L420).

```lean
lemma coeff_ne_zero (hrec : RadialRec κ l c) (hnt : ∀ N : ℕ, κ * (N + l + 1) ≠ 1)
    (h0 : c 0 ≠ 0) :
    ∀ k, c k ≠ 0
```

**`PhyslibAlpha.Hydrogen.not_integrableOn_of_nonterminating`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L435).

> **Non-terminating series grow like `e^(3κρ/2)`.** Then `u = ρ^(l+1) e^(-κρ) Σ c_k ρ^k` is not
> square integrable.

```lean
lemma not_integrableOn_of_nonterminating (hκ : 0 < κ) (hc : EntireCoeff c)
    (hrec : RadialRec κ l c) (hnt : ∀ N : ℕ, κ * (N + l + 1) ≠ 1) (h0 : c 0 ≠ 0) :
    ¬IntegrableOn (fun ρ => radialSeries κ l c ρ ^ 2) (Ioi 0)
```

## E. Quantisation

**`PhyslibAlpha.Hydrogen.radial_quantization`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean#L596).

> **Quantisation of the hydrogen levels.** Let `u(ρ) = ρ^(l+1) e^(-κρ) Σ_k c_k ρ^k` with an
> everywhere convergent power series, `c_0 ≠ 0` and `κ > 0`, solve the radial equation
> `u'' = (l(l+1)/ρ² - 2/ρ + κ²) u` on `(0, ∞)`, i.e. be an eigenfunction with energy `-κ²` in Rydberg
> units. If `u` is square integrable, then `κ = 1/ν` for a natural number `ν > l`, so the energy is
> the Bohr level `-1/ν²`, and `u` is a multiple of the radial function `u_{νl}`.

```lean
lemma radial_quantization (hκ : 0 < κ) (hc : EntireCoeff c) (h0 : c 0 ≠ 0)
    (hode : ∀ ρ : ℝ, 0 < ρ → deriv (deriv (radialSeries κ l c)) ρ =
      ((l : ℝ) * (l + 1) / ρ ^ 2 - 2 / ρ + κ ^ 2) * radialSeries κ l c ρ)
    (hint : IntegrableOn (fun ρ => radialSeries κ l c ρ ^ 2) (Ioi 0)) :
    ∃ ν : ℕ, l < ν ∧ κ = 1 / (ν : ℝ) ∧
      ∃ C : ℝ, ∀ ρ, radialSeries κ l c ρ = C * radialU ν l ρ
```

## Depends on

- [The radial functions of the hydrogen atom](radialfunctions.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialQuantization.lean)
