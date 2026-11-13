---
declaration: module
origin: cited
lean: Polynomial.physHermite, Polynomial.physHermite_succ, Polynomial.physHermite_eq_iterate, Polynomial.physHermite_zero, Polynomial.physHermite_one, Polynomial.derivative_physHermite_succ, Polynomial.derivative_physHermite, Polynomial.physHermite_succ'
statement: formalized
proof: formalized
---

# Physicist's Hermite Polynomials

The module `Physlib.Mathematics.SpecialFunctions.PhysHermite`, [Physlib/Mathematics/SpecialFunctions/PhysHermite.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean): 53 declarations (1 instance with no name), 7 with a docstring.

> This file may eventually be upstreamed to Mathlib.

## i. Overview

> The physicist's Hermite polynomials are a family of orthogonal polynomials defined by the recursion
> $H_0(x) = 1$ and $H_{n+1}(x) = 2x\,H_n(x) - H_n'(x)$.
> These are a rescaling of the so-called probabalist's Hermite polynomials (`Polynomial.hermite`)
> and, up to numerical factors, satisfy all of the same properties.

## ii. Key results

## iv. References

> * None.

## A. Recursive definition

**`Polynomial.physHermite`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L64).

> The physicist's Hermite polynomials are defined as polynomials over `ℤ` in `X` recursively
> with `physHermite 0 = 1` and
>
> `physHermite (n + 1) = 2 • X * physHermite n - derivative (physHermite n)`.
>
> This polynomial will often be cast as a function `ℝ → ℝ` by evaluating the polynomial at `X`.

```lean
noncomputable def physHermite : ℕ → Polynomial ℤ
```

**`Polynomial.physHermite_succ`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L69).

> The defining recursion `physHermite (n + 1) = (2x - d/dx) (physHermite n)`.

```lean
lemma physHermite_succ (n : ℕ) :
    physHermite (n + 1) = 2 • X * physHermite n - derivative (physHermite n)
```

**`Polynomial.physHermite_eq_iterate`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L74).

> The Rodrigues formula `physHermite n = (2x - d/dx)ⁿ 1`.

```lean
lemma physHermite_eq_iterate (n : ℕ) :
    physHermite n = (fun p => 2 * X * p - derivative p)^[n] 1
```

**`Polynomial.physHermite_zero`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L81).

```lean
lemma physHermite_zero : physHermite 0 = C 1
```

**`Polynomial.physHermite_one`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L84).

```lean
lemma physHermite_one : physHermite 1 = 2 * X
```

**`Polynomial.derivative_physHermite_succ`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L86).

```lean
lemma derivative_physHermite_succ : (n : ℕ) →
    derivative (physHermite (n + 1)) = 2 * (n + 1) • physHermite n
```

**`Polynomial.derivative_physHermite`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L97).

```lean
lemma derivative_physHermite : (n : ℕ) →
    derivative (physHermite n) = 2 * n • physHermite (n - 1)
```

**`Polynomial.physHermite_succ'`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L102).

```lean
lemma physHermite_succ' (n : ℕ) :
    physHermite (n + 1) = 2 • X * physHermite n - 2 * n • physHermite (n - 1)
```

## B. Coefficients & degree

**`Polynomial.coeff_physHermite_succ_zero`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L110).

```lean
lemma coeff_physHermite_succ_zero (n : ℕ) :
    coeff (physHermite (n + 1)) 0 = - coeff (physHermite n) 1
```

**`Polynomial.coeff_physHermite_succ_succ`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L114).

```lean
lemma coeff_physHermite_succ_succ (n k : ℕ) : coeff (physHermite (n + 1)) (k + 1) =
    2 * coeff (physHermite n) k - (k + 2) * coeff (physHermite n) (k + 2)
```

**`Polynomial.coeff_physHermite_of_lt`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L120).

```lean
lemma coeff_physHermite_of_lt {n k : ℕ} (hnk : n < k) : coeff (physHermite n) k = 0
```

**`Polynomial.coeff_physHermite_self`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L131).

```lean
lemma coeff_physHermite_self (n : ℕ) : coeff (physHermite n) n = 2 ^ n
```

**`Polynomial.degree_physHermite`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L139).

```lean
lemma degree_physHermite (n : ℕ) : degree (physHermite n) = n
```

**`Polynomial.natDegree_physHermite`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L145).

```lean
lemma natDegree_physHermite (n : ℕ) : (physHermite n).natDegree = n
```

**`Polynomial.physHermite_leadingCoeff`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L149).

```lean
lemma physHermite_leadingCoeff (n : ℕ) : (physHermite n).leadingCoeff = 2 ^ n
```

**`Polynomial.physHermite_ne_zero`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L153).

```lean
lemma physHermite_ne_zero (n : ℕ) : physHermite n ≠ 0
```

## C. Iterated derivatives

**`Polynomial.iterate_derivative_physHermite_of_gt`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L160).

```lean
lemma iterate_derivative_physHermite_of_gt {n m : ℕ} (h : n < m) :
    derivative^[m] (physHermite n) = 0
```

**`Polynomial.iterate_derivative_physHermite_self`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L165).

```lean
lemma iterate_derivative_physHermite_self (n : ℕ) :
    derivative^[n] (physHermite n) = C (n ! * 2 ^ n : ℤ)
```

## D. As functions `ℝ → ℝ`

**`Polynomial.realEval`**, an abbrev, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L182).

> Cast an integer polynomial to a function `ℝ → ℝ` by evaluation of the indeterminant.

```lean
noncomputable abbrev realEval (p : Polynomial ℤ) : ℝ → ℝ
```

**An instance with no name**, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L184).

```lean
noncomputable instance : CoeFun (Polynomial ℤ) (fun _ ↦ ℝ → ℝ)
```

### D.1. Recursion

**`Polynomial.physHermite_zero_coe`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L190).

```lean
lemma physHermite_zero_coe : (physHermite 0 : ℝ → ℝ) = fun _ ↦ 1
```

**`Polynomial.physHermite_succ_coe`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L193).

> The defining recursion for `physHermite` as functions `ℝ → ℝ` (c.f. `physHermite_succ`).

```lean
lemma physHermite_succ_coe (n : ℕ) :
    (physHermite (n + 1) : ℝ → ℝ) =
      2 • (fun x => x) * (physHermite n : ℝ → ℝ) - deriv (physHermite n)
```

**`Polynomial.physHermite_succ_apply`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L199).

```lean
lemma physHermite_succ_apply (n : ℕ) (x : ℝ) :
    physHermite (n + 1) x = 2 * x * physHermite n x - deriv (physHermite n) x
```

**`Polynomial.physHermite_succ_coe'`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L204).

> The two-term recursion for `physHermite` as functions `ℝ → ℝ` (c.f. `physHermite_succ'`).

```lean
lemma physHermite_succ_coe' (n : ℕ) :
    (physHermite (n + 1) : ℝ → ℝ) =
      2 • (fun x => x) * (physHermite n : ℝ → ℝ) - (2 * n) • (physHermite (n - 1) : ℝ → ℝ)
```

**`Polynomial.physHermite_succ_apply'`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L210).

```lean
lemma physHermite_succ_apply' (n : ℕ) (x : ℝ) :
    physHermite (n + 1) x = 2 * x * physHermite n x - 2 * n * physHermite (n - 1) x
```

**`Polynomial.deriv_physHermite`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L214).

```lean
lemma deriv_physHermite (n : ℕ) : deriv (physHermite n) = 2 * n * physHermite (n - 1)
```

**`Polynomial.iterate_deriv_physHermite_eq_iterate_derivative`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L218).

```lean
lemma iterate_deriv_physHermite_eq_iterate_derivative (n m : ℕ) :
    deriv^[m] (physHermite n) = derivative^[m] (physHermite n)
```

**`Polynomial.fderiv_physHermite`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L226).

```lean
lemma fderiv_physHermite (n : ℕ) (x : ℝ) :
    fderiv ℝ (physHermite n) x = (1 : ℝ →L[ℝ] ℝ).smulRight (deriv (physHermite n) x)
```

### D.2. Parity

**`Polynomial.physHermite_neg`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L236).

> The `physHermite` polynomials are alternately even and odd.

```lean
lemma physHermite_neg (n : ℕ) (x : ℝ) : physHermite n (-x) = (-1) ^ n * physHermite n x
```

**`Polynomial.physHermite_even`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L242).

```lean
lemma physHermite_even {n : ℕ} (hn : Even n) : Function.Even (physHermite n)
```

**`Polynomial.physHermite_odd`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L244).

```lean
lemma physHermite_odd {n : ℕ} (hn : Odd n) : Function.Odd (physHermite n)
```

### D.3. Differentiability

**`Polynomial.physHermite_differentiable`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L251).

```lean
lemma physHermite_differentiable (n : ℕ) : Differentiable ℝ (physHermite n)
```

**`Polynomial.deriv_physHermite_differentiable`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L255).

```lean
lemma deriv_physHermite_differentiable (n m : ℕ) : Differentiable ℝ (deriv^[m] (physHermite n))
```

**`Polynomial.physHermite_continuous`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L259).

```lean
lemma physHermite_continuous (n : ℕ) : Continuous (physHermite n)
```

**`Polynomial.physHermite_contDiff`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L262).

```lean
lemma physHermite_contDiff (n : ℕ) (m : WithTop ℕ∞) : ContDiff ℝ m (physHermite n)
```

### D.4. Temperate growth

**`Polynomial.physHermite_hasTemperateGrowth`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L271).

```lean
lemma physHermite_hasTemperateGrowth (n : ℕ) : HasTemperateGrowth (physHermite n)
```

## E. Relationship to Gaussians

**`Polynomial.deriv_gaussian_eq_physHermite_mul_gaussian`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L288).

```lean
lemma deriv_gaussian_eq_physHermite_mul_gaussian (n : ℕ) (x : ℝ) :
    deriv^[n] (fun y => Real.exp (- y ^ 2)) x =
    (-1 : ℝ) ^ n * physHermite n x * Real.exp (- x ^ 2)
```

**`Polynomial.physHermite_eq_deriv_gaussian`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L306).

```lean
lemma physHermite_eq_deriv_gaussian (n : ℕ) (x : ℝ) :
    physHermite n x = (-1 : ℝ) ^ n * deriv^[n]
    (fun y => Real.exp (- y ^ 2)) x / Real.exp (- x ^ 2)
```

**`Polynomial.physHermite_eq_deriv_gaussian'`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L312).

```lean
lemma physHermite_eq_deriv_gaussian' (n : ℕ) (x : ℝ) :
    physHermite n x = (-1 : ℝ) ^ n * deriv^[n] (fun y => Real.exp (- y ^ 2)) x *
    Real.exp (x ^ 2)
```

**`Polynomial.guassian_integrable_polynomial_cons`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L319).

```lean
lemma guassian_integrable_polynomial_cons {b c : ℝ} (hb : 0 < b) (P : Polynomial ℤ) :
    MeasureTheory.Integrable fun x : ℝ => (P.aeval (c * x)) * Real.exp (-b * x ^ 2)
```

**`Polynomial.guassian_integrable_polynomial`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L332).

```lean
lemma guassian_integrable_polynomial {b : ℝ} (hb : 0 < b) (P : Polynomial ℤ) :
    MeasureTheory.Integrable fun x : ℝ => (P.aeval x) * Real.exp (-b * x ^ 2)
```

**`Polynomial.physHermite_gaussian_integrable`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L337).

```lean
lemma physHermite_gaussian_integrable (n p m : ℕ) :
    MeasureTheory.Integrable (deriv^[m] (physHermite p) * deriv^[n] fun x => Real.exp (-x ^ 2))
    MeasureTheory.volume
```

**`Polynomial.integral_physHermite_mul_physHermite_eq_integral_deriv_exp`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L352).

```lean
lemma integral_physHermite_mul_physHermite_eq_integral_deriv_exp (n m : ℕ) :
    ∫ x : ℝ, (physHermite n x * physHermite m x) * Real.exp (-x ^ 2) =
    (-1 : ℝ) ^ m * ∫ x : ℝ, (physHermite n x * (deriv^[m] fun x => Real.exp (-x ^ 2)) x)
```

**`Polynomial.integral_physHermite_mul_physHermite_eq_integral_deriv_inductive`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L362).

```lean
lemma integral_physHermite_mul_physHermite_eq_integral_deriv_inductive (n m : ℕ) :
    (p : ℕ) → (hpm : p ≤ m) →
    ∫ x : ℝ, (physHermite n x * physHermite m x) * Real.exp (- x ^ 2) =
    (-1 : ℝ) ^ (m - p) * ∫ x : ℝ, (deriv^[p] (physHermite n) x *
    (deriv^[m - p] fun x => Real.exp (-x ^ 2)) x)
```

**`Polynomial.integral_physHermite_mul_physHermite_eq_integral_deriv`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L395).

```lean
lemma integral_physHermite_mul_physHermite_eq_integral_deriv (n m : ℕ) :
    ∫ x : ℝ, (physHermite n x * physHermite m x) * Real.exp (- x ^ 2) =
    ∫ x : ℝ, (deriv^[m] (physHermite n) x * (Real.exp (-x ^ 2)))
```

**`Polynomial.physHermite_orthogonal_lt`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L400).

```lean
lemma physHermite_orthogonal_lt {n m : ℕ} (hnm : n < m) :
    ∫ x : ℝ, (physHermite n x * physHermite m x) * Real.exp (- x ^ 2) = 0
```

**`Polynomial.physHermite_orthogonal`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L405).

```lean
lemma physHermite_orthogonal {n m : ℕ} (hnm : n ≠ m) :
    ∫ x : ℝ, (physHermite n x * physHermite m x) * Real.exp (- x ^ 2) = 0
```

**`Polynomial.physHermite_orthogonal_cons`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L411).

```lean
lemma physHermite_orthogonal_cons {n m : ℕ} (hnm : n ≠ m) (c : ℝ) :
    ∫ x : ℝ, (physHermite n (c * x) * physHermite m (c * x)) *
    Real.exp (- c ^ 2 * x ^ 2) = 0
```

**`Polynomial.physHermite_norm`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L419).

```lean
lemma physHermite_norm (n : ℕ) :
    ∫ x : ℝ, (physHermite n x * physHermite n x) * Real.exp (- x ^ 2) =
    ↑n ! * 2 ^ n * √Real.pi
```

**`Polynomial.physHermite_norm_cons`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L427).

```lean
lemma physHermite_norm_cons (n : ℕ) (c : ℝ) :
    ∫ x : ℝ, (physHermite n (c * x) * physHermite n (c * x)) * Real.exp (- c ^ 2 * x ^ 2) =
    |c⁻¹| • (↑n ! * 2 ^ n * √Real.pi)
```

**`Polynomial.polynomial_mem_physHermite_span_induction`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L435).

```lean
lemma polynomial_mem_physHermite_span_induction (P : Polynomial ℤ) : (n : ℕ) →
    (hn : P.natDegree = n) →
    (P : ℝ → ℝ) ∈ Submodule.span ℝ (Set.range (fun n => (physHermite n : ℝ → ℝ)))
  | 0, h => by
    obtain ⟨x, rfl⟩
```

**`Polynomial.polynomial_mem_physHermite_span`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L479).

```lean
lemma polynomial_mem_physHermite_span (P : Polynomial ℤ) :
    (P : ℝ → ℝ) ∈ Submodule.span ℝ (Set.range (fun n => (physHermite n : ℝ → ℝ)))
```

**`Polynomial.cos_mem_physHermite_span_topologicalClosure`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean#L483).

```lean
lemma cos_mem_physHermite_span_topologicalClosure (c : ℝ) :
    (fun (x : ℝ) => Real.cos (c * x)) ∈
    (Submodule.span ℝ (Set.range (fun n => (physHermite n : ℝ → ℝ)))).topologicalClosure
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/SpecialFunctions/PhysHermite.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/SpecialFunctions/PhysHermite.lean)
