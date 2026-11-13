---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.tensorForm_coupledVec_stringVec, PhyslibAlpha.Sl2.eq_sum_coupledVec, PhyslibAlpha.Sl2.sum_cgCoefficient_mul_cgCoefficient, PhyslibAlpha.Sl2.factorialSum, PhyslibAlpha.Sl2.factorialSum_succ, PhyslibAlpha.Sl2.factorialSum_mul, PhyslibAlpha.Sl2.sum_choose_mul_factorial, PhyslibAlpha.Sl2.hwNormNum
statement: formalized
proof: formalized
---

# Closed formulas for the Clebsch–Gordan coefficients

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.ClebschGordanFormula`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean): 38 declarations, 28 with a docstring.

> The second orthogonality relation, an explicit single-sum formula and Racah's formula for
> `⟨j₁ m₁ j₂ m₂ | J M⟩`.

## i. Overview

> The coupled states `|J, M⟩` form an orthonormal basis of `V(m) ⊗ V(n)`, so every vector is
> `Σ_{J M} ⟨J M | x⟩ |J M⟩`. Applied to product states this gives the second orthogonality relation
> `Σ_{J M} ⟨j₁ m₁ j₂ m₂ | J M⟩ ⟨j₁ m₁' j₂ m₂' | J M⟩ = δ_{m₁ m₁'} δ_{m₂ m₂'}`.
>
> For the closed formula, two computations are combined.
>
> - The squared norm of the highest-weight vector `w_k` has the closed form
>   `⟨w_k, w_k⟩ = k! m! n! (m - k)! (n - k)! (m + n - k + 1)! / (m + n - 2k + 1)!`.
>   It reduces to the factorial identity
>   `Σ_a C(k, a) (p + a)! (k + s - a)! · (p + s + 1)! = (p + k + s + 1)! p! s!`, proved by induction
>   on `k` with Pascal's rule.
> - The lowering operator on `V(m) ⊗ V(n)` is `f ⊗ 1 + 1 ⊗ f` with commuting summands, so the
>   binomial theorem gives `f^l (v_a ⊗ v_b) = Σ_i C(l, i) v_{a+i} ⊗ v_{b+l-i}`.
>
> Together with the coefficients of `w_k` from `TensorHighestWeight` this yields, with
> `J = (m + n)/2 - k`, `M = J - l`, `m₁ = m/2 - α`, `m₂ = n/2 - β` and `α + β = k + l`, a formula
> `⟨j₁ m₁ j₂ m₂ | J M⟩ = S · √(…)` with the single alternating sum
> `S = Σ_a (-1)^a C(k, a) C(l, α - a) (n - k + a)! (m - a)!`.
>
> Racah's formula has a different alternating sum. After dividing out factorials both sums become
> binomial sums,
> `L(k, α, s) = Σ_a (-1)^a C(k, a) C(r + k - a, α - a) C(p + a, s + a)` and
> `R(k, α, s) = Σ_z (-1)^z C(k, z) C(r, α - z) C(p, s + z)`,
> with lower indices in `ℤ` (`C(n, j) = 0` for `j < 0`). Pascal's rule shows that both satisfy
> `X(k + 1, α, s) = X(k, α, s) - X(k, α - 1, s + 1)`, and they agree for `k = 0`, so `L = R`.
> This proves Racah's formula.
>
> For `n = 1`, coupling a spin `j₁ = m/2` with a spin `½`, the single sum has at most two terms and
> the closed formula gives the four coefficients in square-root form, with `J = j₁ ± ½`.

## ii. Key results

> - `eq_sum_coupledVec` and `sum_cgCoefficient_mul_cgCoefficient`: completeness of the coupled basis
>   and the second orthogonality relation.
> - `sum_choose_mul_factorial` and `hwNormSq_closed`: the closed norm of `w_k`.
> - `tensorF_pow_tmul_vNat`: the explicit lowering.
> - `cgCoefficient_eq_cgSum` and `cgCoefficient_closed`: the closed single-sum formula.
> - `racahL_eq_racahR` and `cgCoefficient_racah`: Racah's formula.
> - `cgCoefficient_add_half_up`, `cgCoefficient_add_half_down`, `cgCoefficient_sub_half_up`,
>   `cgCoefficient_sub_half_down`: the coefficients for coupling with a spin `½`.

## iv. References

> - G. Racah, *Theory of complex spectra. II*, Phys. Rev. 62, 438 (1942).
> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.8.
> - D. A. Varshalovich, A. N. Moskalev, V. K. Khersonskii, *Quantum Theory of Angular Momentum:
>   Irreducible Tensors, Spherical Harmonics, Vector Coupling Coefficients, 3nj Symbols*, World
>   Scientific (1988), Table 8.1, p. 271.

## A. Completeness and the second orthogonality relation

**`PhyslibAlpha.Sl2.tensorForm_coupledVec_stringVec`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L100).

> `⟨|J, M⟩, f^{l'} w_{k'}⟩ = δ_{kk'} δ_{ll'} √(normSq N l · ⟨w_k, w_k⟩)`.

```lean
lemma tensorForm_coupledVec_stringVec (hmn : 0 < m + n) {k k' l l' : ℕ} (hkm : k ≤ m)
    (hkn : k ≤ n) (hk'm : k' ≤ m) (hk'n : k' ≤ n) (hl : l ≤ m + n - 2 * k) :
    tensorForm m n (coupledVec m n k l) (stringVec m n k' l') =
      if k = k' ∧ l = l' then
        Real.sqrt ((normSq (m + n - 2 * k) l : ℝ) * hwNormSq m n k)
      else 0
```

**`PhyslibAlpha.Sl2.eq_sum_coupledVec`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L121).

> **Completeness.** Every vector of `V(m) ⊗ V(n)` is `Σ_{J M} ⟨|J, M⟩, x⟩ |J, M⟩`.

```lean
lemma eq_sum_coupledVec (hmn : 0 < m + n) (x : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    x = ∑ k ∈ Finset.range (min m n + 1), ∑ l ∈ Finset.range (m + n - 2 * k + 1),
      tensorForm m n (coupledVec m n k l) x • coupledVec m n k l
```

**`PhyslibAlpha.Sl2.sum_cgCoefficient_mul_cgCoefficient`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L160).

> **Second orthogonality relation.**
> `Σ_{J M} ⟨j₁ m₁ j₂ m₂ | J M⟩ ⟨j₁ m₁' j₂ m₂' | J M⟩ = δ_{m₁ m₁'} δ_{m₂ m₂'}`.

```lean
lemma sum_cgCoefficient_mul_cgCoefficient (hmn : 0 < m + n) {a b a' b' : ℕ} (ha : a ≤ m)
    (hb : b ≤ n) (ha' : a' ≤ m) (hb' : b' ≤ n) :
    ∑ k ∈ Finset.range (min m n + 1), ∑ l ∈ Finset.range (m + n - 2 * k + 1),
      cgCoefficient m n k l a b * cgCoefficient m n k l a' b' =
        if a = a' ∧ b = b' then 1 else 0
```

## B. The norm of the highest-weight vectors

### B.1. A factorial identity

**`PhyslibAlpha.Sl2.factorialSum`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L185).

> `S(k, p, s) = Σ_{i + j = k} C(k, i) (p + i)! (s + j)!`.

```lean
def factorialSum (k p s : ℕ) : ℕ
```

**`PhyslibAlpha.Sl2.factorialSum_succ`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L189).

> Pascal's rule for `S`.

```lean
lemma factorialSum_succ (k p s : ℕ) :
    factorialSum (k + 1) p s = factorialSum k p (s + 1) + factorialSum k (p + 1) s
```

**`PhyslibAlpha.Sl2.factorialSum_mul`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L203).

> `S(k, p, s) · (p + s + 1)! = (p + k + s + 1)! p! s!`.

```lean
lemma factorialSum_mul (k p s : ℕ) :
    factorialSum k p s * (p + s + 1).factorial =
      (p + k + s + 1).factorial * p.factorial * s.factorial
```

**`PhyslibAlpha.Sl2.sum_choose_mul_factorial`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L224).

> The factorial identity in the form used for `⟨w_k, w_k⟩`:
> `Σ_a C(k, a) (p + a)! (s + k - a)! · (p + s + 1)! = (p + k + s + 1)! p! s!`.

```lean
lemma sum_choose_mul_factorial (k p s : ℕ) :
    (∑ a ∈ Finset.range (k + 1), k.choose a * ((p + a).factorial * (s + (k - a)).factorial)) *
      (p + s + 1).factorial = (p + k + s + 1).factorial * p.factorial * s.factorial
```

### B.2. The closed norm

**`PhyslibAlpha.Sl2.hwNormNum`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L236).

> The numerator `k! m! n! (m + n - k + 1)! (n - k)! (m - k)!` of `⟨w_k, w_k⟩`.

```lean
def hwNormNum (m n k : ℕ) : ℕ
```

**`PhyslibAlpha.Sl2.cgCoeff_sq_mul_normSq`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L240).

```lean
lemma cgCoeff_sq_mul_normSq {k a : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (ha : a ≤ k) :
    cgCoeff (K := ℝ) m n k a ^ 2 * (normSq m a : ℝ) * (normSq n (k - a) : ℝ) =
      ((k.choose a * ((n - k + a).factorial * (m - a).factorial) *
        (k.factorial * m.factorial * n.factorial) : ℕ) : ℝ)
```

**`PhyslibAlpha.Sl2.hwNormSq_mul_factorial`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L259).

> `⟨w_k, w_k⟩ (m + n - 2k + 1)! = k! m! n! (m + n - k + 1)! (n - k)! (m - k)!`.

```lean
lemma hwNormSq_mul_factorial {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) :
    hwNormSq m n k * ((m + n - 2 * k + 1).factorial : ℝ) = hwNormNum m n k
```

**`PhyslibAlpha.Sl2.hwNormSq_closed`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L280).

> **The closed norm.**
> `⟨w_k, w_k⟩ = k! m! n! (m + n - k + 1)! (n - k)! (m - k)! / (m + n - 2k + 1)!`.

```lean
lemma hwNormSq_closed {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) :
    hwNormSq m n k = hwNormNum m n k / ((m + n - 2 * k + 1).factorial : ℝ)
```

## C. The lowering strings in the product basis

**`PhyslibAlpha.Sl2.ρF_pow_vNat`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L290).

```lean
lemma ρF_pow_vNat (a l : ℕ) :
    ((ρF : Module.End ℝ (StandardSl2Module ℝ n)) ^ l) (vNat n a) = vNat n (a + l)
```

**`PhyslibAlpha.Sl2.tensorF_pow_tmul_vNat`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L298).

> The binomial theorem for the lowering operator:
> `f^l (v_a ⊗ v_b) = Σ_i C(l, i) v_{a+i} ⊗ v_{b+l-i}`.

```lean
lemma tensorF_pow_tmul_vNat (a b l : ℕ) :
    (tensorF (K := ℝ) m n ^ l) (vNat m a ⊗ₜ vNat n b) =
      ∑ i ∈ Finset.range (l + 1), (l.choose i : ℝ) • (vNat m (a + i) ⊗ₜ vNat n (b + (l - i)))
```

## D. The closed formula

**`PhyslibAlpha.Sl2.cgSum`**, a def, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L318).

> The alternating sum `Σ_{a ≤ min(k, α)} (-1)^a C(k, a) (n - k + a)! (m - a)! C(l, α - a)`.

```lean
def cgSum (m n k l α : ℕ) : ℝ
```

**`PhyslibAlpha.Sl2.sum_choose_mul_ite`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L321).

```lean
lemma sum_choose_mul_ite {l a α : ℕ} (X : ℝ) :
    ∑ i ∈ Finset.range (l + 1), (l.choose i : ℝ) * (if α = a + i then X else 0) =
      if a ≤ α then (l.choose (α - a) : ℝ) * X else 0
```

**`PhyslibAlpha.Sl2.tensorForm_normVec_tmul_vNat`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L335).

```lean
lemma tensorForm_normVec_tmul_vNat {α β a i k l : ℕ} (hα : α ≤ m) (hβ : β ≤ n)
    (h : α + β = k + l) (hak : a ≤ k) (hil : i ≤ l) :
    tensorForm m n (normVec m α ⊗ₜ normVec n β) (vNat m (a + i) ⊗ₜ vNat n (k - a + (l - i))) =
      if α = a + i then Real.sqrt (normSq m α) * Real.sqrt (normSq n β) else 0
```

**`PhyslibAlpha.Sl2.tensorForm_normVec_stringVec`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L345).

> `⟨u_α ⊗ u_β, f^l w_k⟩ = cgSum · √(normSq m α) √(normSq n β)` for `α + β = k + l`.

```lean
lemma tensorForm_normVec_stringVec {k l α β : ℕ} (hα : α ≤ m) (hβ : β ≤ n)
    (h : α + β = k + l) :
    tensorForm m n (normVec m α ⊗ₜ normVec n β) (stringVec m n k l) =
      cgSum m n k l α * Real.sqrt (normSq m α) * Real.sqrt (normSq n β)
```

**`PhyslibAlpha.Sl2.cgCoefficient_eq_cgSum`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L363).

> The Clebsch–Gordan coefficient as one finite sum, with the norm of `w_k` still unevaluated.

```lean
lemma cgCoefficient_eq_cgSum {k l α β : ℕ} (hα : α ≤ m) (hβ : β ≤ n) (h : α + β = k + l) :
    cgCoefficient m n k l α β =
      (Real.sqrt ((normSq (m + n - 2 * k) l : ℝ) * hwNormSq m n k))⁻¹ *
        (cgSum m n k l α * Real.sqrt (normSq m α) * Real.sqrt (normSq n β))
```

**`PhyslibAlpha.Sl2.cgCoefficient_closed`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L373).

> **Closed formula for the Clebsch–Gordan coefficients.** For `α + β = k + l`, with
> `N = m + n - 2k`,
> `⟨j₁ m₁ j₂ m₂ | J M⟩ = cgSum · √(normSq m α · normSq n β · (N + 1)! / (normSq N l · hwNormNum))`.
> For `α + β ≠ k + l` the coefficient vanishes by `cgCoefficient_eq_zero_of_ne`.

```lean
lemma cgCoefficient_closed {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hl : l ≤ m + n - 2 * k) (hα : α ≤ m) (hβ : β ≤ n) (h : α + β = k + l) :
    cgCoefficient m n k l α β = cgSum m n k l α *
      Real.sqrt ((normSq m α : ℝ) * normSq n β * (m + n - 2 * k + 1).factorial /
        ((normSq (m + n - 2 * k) l : ℝ) * hwNormNum m n k))
```

## E. Racah's formula

### E.1. Binomial coefficients with an integer lower index

**`PhyslibAlpha.Sl2.zchoose`**, a def, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L401).

> `C(n, j)` for `j ≥ 0` and `0` for `j < 0`.

```lean
def zchoose (n : ℕ) (j : ℤ) : ℤ
```

**`PhyslibAlpha.Sl2.zchoose_natCast`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L403).

```lean
lemma zchoose_natCast (n t : ℕ) : zchoose n t = n.choose t
```

**`PhyslibAlpha.Sl2.zchoose_of_neg`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L406).

```lean
lemma zchoose_of_neg {n : ℕ} {j : ℤ} (h : j < 0) : zchoose n j = 0
```

**`PhyslibAlpha.Sl2.zchoose_succ`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L410).

> Pascal's rule `C(n + 1, j) = C(n, j) + C(n, j - 1)` for all integers `j`.

```lean
lemma zchoose_succ (n : ℕ) (j : ℤ) : zchoose (n + 1) j = zchoose n j + zchoose n (j - 1)
```

**`PhyslibAlpha.Sl2.sum_range_choose_succ_mul`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L421).

> Pascal's rule inside a binomial sum.

```lean
lemma sum_range_choose_succ_mul (f : ℕ → ℤ) (k : ℕ) :
    ∑ a ∈ Finset.range (k + 1 + 1), ((k + 1).choose a : ℤ) * f a =
      ∑ a ∈ Finset.range (k + 1), (k.choose a : ℤ) * f a +
        ∑ a ∈ Finset.range (k + 1), (k.choose a : ℤ) * f (a + 1)
```

### E.2. Two binomial sums with the same recursion

**`PhyslibAlpha.Sl2.racahL`**, a def, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L444).

> `L(k, α, s) = Σ_a (-1)^a C(k, a) C(r + k - a, α - a) C(p + a, s + a)`: the sum `cgSum` after
> dividing out factorials.

```lean
def racahL (r p k : ℕ) (α s : ℤ) : ℤ
```

**`PhyslibAlpha.Sl2.racahR`**, a def, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L450).

> `R(k, α, s) = Σ_z (-1)^z C(k, z) C(r, α - z) C(p, s + z)`: Racah's sum after dividing out
> factorials.

```lean
def racahR (r p k : ℕ) (α s : ℤ) : ℤ
```

**`PhyslibAlpha.Sl2.racahL_succ`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L453).

```lean
lemma racahL_succ (r p k : ℕ) (α s : ℤ) :
    racahL r p (k + 1) α s = racahL r p k α s - racahL r p k (α - 1) (s + 1)
```

**`PhyslibAlpha.Sl2.racahR_succ`**, a lemma, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L465).

```lean
lemma racahR_succ (r p k : ℕ) (α s : ℤ) :
    racahR r p (k + 1) α s = racahR r p k α s - racahR r p k (α - 1) (s + 1)
```

**`PhyslibAlpha.Sl2.racahL_eq_racahR`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L475).

> **The transformation.** `L = R`, by induction on `k`: both satisfy
> `X(k + 1, α, s) = X(k, α, s) - X(k, α - 1, s + 1)` and agree for `k = 0`.

```lean
lemma racahL_eq_racahR (r p k : ℕ) (α s : ℤ) : racahL r p k α s = racahR r p k α s
```

### E.3. Racah's formula

**`PhyslibAlpha.Sl2.racahSum`**, a def, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L490).

> Racah's alternating sum
> `Σ_z (-1)^z / (z! (k - z)! (α - z)! (n - β - z)! (m - k - α + z)! (β - k + z)!)`
> over the `z` for which all six arguments are nonnegative. In spin notation the arguments are
> `z`, `j₁ + j₂ - J - z`, `j₁ - m₁ - z`, `j₂ + m₂ - z`, `J - j₂ + m₁ + z` and `J - j₁ - m₂ + z`.

```lean
def racahSum (m n k α β : ℕ) : ℝ
```

**`PhyslibAlpha.Sl2.cgSum_eq_racahL`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L497).

```lean
lemma cgSum_eq_racahL {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (hα : α ≤ m) (hβ : β ≤ n)
    (h : α + β = k + l) :
    cgSum m n k l α = (l.factorial : ℝ) * (m - α).factorial * (n - β).factorial *
      (racahL (m - k) (n - k) k α ((l : ℤ) - α) : ℝ)
```

**`PhyslibAlpha.Sl2.racahR_eq_racahSum`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L536).

```lean
lemma racahR_eq_racahSum {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (h : α + β = k + l) :
    (racahR (m - k) (n - k) k α ((l : ℤ) - α) : ℝ) =
      (k.factorial : ℝ) * (m - k).factorial * (n - k).factorial * racahSum m n k α β
```

**`PhyslibAlpha.Sl2.cgSum_eq_racahSum`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L579).

> `cgSum = l! (m - α)! (n - β)! · k! (m - k)! (n - k)! · racahSum`.

```lean
lemma cgSum_eq_racahSum {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (hα : α ≤ m) (hβ : β ≤ n)
    (h : α + β = k + l) :
    cgSum m n k l α = (l.factorial : ℝ) * (m - α).factorial * (n - β).factorial *
      ((k.factorial : ℝ) * (m - k).factorial * (n - k).factorial) * racahSum m n k α β
```

**`PhyslibAlpha.Sl2.cgCoefficient_racah`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L590).

> **Racah's formula.** For `α + β = k + l`, with `j₁ = m/2`, `m₁ = j₁ - α`, `j₂ = n/2`,
> `m₂ = j₂ - β`, `J = (m + n)/2 - k`, `M = J - l`,
> `⟨j₁ m₁ j₂ m₂ | J M⟩ = √((2J + 1) (J + j₁ - j₂)! (J - j₁ + j₂)! (j₁ + j₂ - J)! / (j₁ + j₂ + J + 1)!)
>   · √((J + M)! (J - M)! (j₁ - m₁)! (j₁ + m₁)! (j₂ - m₂)! (j₂ + m₂)!) · racahSum`.

```lean
lemma cgCoefficient_racah {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hl : l ≤ m + n - 2 * k) (hα : α ≤ m) (hβ : β ≤ n) (h : α + β = k + l) :
    cgCoefficient m n k l α β =
      Real.sqrt (((m + n - 2 * k + 1) * (m - k).factorial * (n - k).factorial * k.factorial : ℕ) /
        ((m + n - k + 1).factorial : ℝ)) *
      Real.sqrt (((m + n - 2 * k - l).factorial * l.factorial * α.factorial * (m - α).factorial *
        β.factorial * (n - β).factorial : ℕ) : ℝ) * racahSum m n k α β
```

## F. Coupling with a spin ½

**`PhyslibAlpha.Sl2.cgCoefficient_add_half_up`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L633).

> `⟨j₁ m₁ ½ ½ | j₁ + ½, M⟩ = √((j₁ + M + ½)/(2j₁ + 1))`: with `j₁ = m/2`, `J = j₁ + ½` (`k = 0`),
> `M = J - l` and `m₁ = j₁ - l`, the value is `√((m + 1 - l)/(m + 1))`.

```lean
lemma cgCoefficient_add_half_up {m l : ℕ} (hl : l ≤ m) :
    cgCoefficient m 1 0 l l 0 = Real.sqrt (((m + 1 - l : ℕ) : ℝ) / (m + 1))
```

**`PhyslibAlpha.Sl2.cgCoefficient_add_half_down`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L652).

> `⟨j₁ m₁ ½ -½ | j₁ + ½, M⟩ = √((j₁ - M + ½)/(2j₁ + 1))`: with `j₁ = m/2`, `J = j₁ + ½`
> (`k = 0`), `M = J - (l + 1)` and `m₁ = j₁ - l`, the value is `√((l + 1)/(m + 1))`.

```lean
lemma cgCoefficient_add_half_down {m l : ℕ} (hl : l ≤ m) :
    cgCoefficient m 1 0 (l + 1) l 1 = Real.sqrt (((l + 1 : ℕ) : ℝ) / (m + 1))
```

**`PhyslibAlpha.Sl2.cgCoefficient_sub_half_up`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L669).

> `⟨j₁ m₁ ½ ½ | j₁ - ½, M⟩ = -√((j₁ - M + ½)/(2j₁ + 1))`: with `j₁ = m/2`, `J = j₁ - ½`
> (`k = 1`), `M = J - l` and `m₁ = j₁ - (l + 1)`, the value is `-√((l + 1)/(m + 1))`.

```lean
lemma cgCoefficient_sub_half_up {m l : ℕ} (hl : l + 1 ≤ m) :
    cgCoefficient m 1 1 l (l + 1) 0 = -Real.sqrt (((l + 1 : ℕ) : ℝ) / (m + 1))
```

**`PhyslibAlpha.Sl2.cgCoefficient_sub_half_down`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean#L689).

> `⟨j₁ m₁ ½ -½ | j₁ - ½, M⟩ = √((j₁ + M + ½)/(2j₁ + 1))`: with `j₁ = m/2`, `J = j₁ - ½`
> (`k = 1`), `M = J - l` and `m₁ = j₁ - l`, the value is `√((m - l)/(m + 1))`.

```lean
lemma cgCoefficient_sub_half_down {m l : ℕ} (hl : l + 1 ≤ m) :
    cgCoefficient m 1 1 l l 1 = Real.sqrt (((m - l : ℕ) : ℝ) / (m + 1))
```

## Depends on

- [Clebsch–Gordan coefficients](clebschgordancoefficients.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanFormula.lean)
