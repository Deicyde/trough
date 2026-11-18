---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.tensorForm, PhyslibAlpha.Sl2.tensorForm_tmul, PhyslibAlpha.Sl2.tensorBilin_ext, PhyslibAlpha.Sl2.invForm_ρE_apply, PhyslibAlpha.Sl2.invForm_ρH_apply, PhyslibAlpha.Sl2.tensorForm_comm, PhyslibAlpha.Sl2.tensorForm_tensorE, PhyslibAlpha.Sl2.tensorForm_tensorF
statement: formalized
proof: formalized
---

# Clebsch–Gordan coefficients

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.ClebschGordanCoefficients`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean): 45 declarations, 29 with a docstring.

> The orthonormal coupled basis `|J, M⟩` of `V(m) ⊗ V(n)` over `ℝ` and the Clebsch–Gordan
> coefficients `⟨j₁ m₁ j₂ m₂ | J M⟩` in the standard normalisation and phase convention.

## i. Overview

> The contravariant forms on `V(m)` and `V(n)` combine to a symmetric bilinear form on
> `V(m) ⊗ V(n)` for which the diagonal raising and lowering operators are adjoint. For the
> lowering strings `f^l w_k` of the highest-weight vectors `w_k` this gives
>
> `⟨f^a w_k, f^b w_{k'}⟩ = δ_{kk'} δ_{ab} · a! N!/(N - a)! · ⟨w_k, w_k⟩`,  `N = m + n - 2k`,
>
> and `⟨w_k, w_k⟩ > 0`. Normalising gives the orthonormal coupled basis
> `|J, M⟩ = coupledVec m n k l` with `J = (m + n)/2 - k`, `M = J - l`, on which `J₊, J₋`
> act by the textbook formulas. The Clebsch–Gordan coefficient is the inner product
>
> `⟨j₁ m₁ j₂ m₂ | J M⟩ = cgCoefficient m n k l a b = ⟨u_a ⊗ u_b, |J, M⟩⟩`
>
> with `j₁ = m/2`, `m₁ = j₁ - a`, `j₂ = n/2`, `m₂ = j₂ - b`. This file proves:
>
> - the coupled states are orthonormal and satisfy the ladder relations of `|J, M⟩`;
> - `⟨j₁ m₁ j₂ m₂ | J M⟩ = 0` unless `m₁ + m₂ = M`;
> - the Condon–Shortley phase convention `⟨j₁ j₁ j₂ (J - j₁) | J J⟩ > 0`;
> - every coupled state is `Σ ⟨j₁ m₁ j₂ m₂ | J M⟩ |j₁ m₁⟩ ⊗ |j₂ m₂⟩`, and the orthogonality
>   relation `Σ_{m₁ m₂} ⟨j₁ m₁ j₂ m₂ | J M⟩ ⟨j₁ m₁ j₂ m₂ | J' M'⟩ = δ_{JJ'} δ_{MM'}`;
> - the values `⟨j₁ j₁ j₂ j₂ | j₁+j₂, j₁+j₂⟩ = 1`, and for two spins `1/2` the singlet
>   `⟨½ ½ ½ -½ | 0 0⟩ = 1/√2`, `⟨½ -½ ½ ½ | 0 0⟩ = -1/√2` and the triplet
>   `⟨½ ½ ½ -½ | 1 0⟩ = ⟨½ -½ ½ ½ | 1 0⟩ = 1/√2`, `⟨½ -½ ½ -½ | 1 -1⟩ = 1`.
>
> These properties determine the Clebsch–Gordan coefficients uniquely, so they agree with the
> tabulated values. A closed formula (Racah's formula) is not proved here.

## ii. Key results

> - `tensorForm`, `tensorForm_tensorF` (contravariance) and `tensorForm_stringVec`.
> - `hwNormSq_pos`, `coupledVec`, `tensorForm_coupledVec` (orthonormality),
>   `tensorF_coupledVec`, `tensorE_coupledVec_succ` (ladder relations).
> - `cgCoefficient`, `cgCoefficient_eq_zero_of_ne`, `cgCoefficient_top_pos`,
>   `coupledVec_eq_sum`, `sum_cgCoefficient_mul`.
> - `cgCoefficient_stretched`, `cgCoefficient_singlet_up`, `cgCoefficient_singlet_down`,
>   `cgCoefficient_triplet_zero_up`, `cgCoefficient_triplet_zero_down`,
>   `cgCoefficient_triplet_minus`.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.8.

## A. The form on the tensor product

**`PhyslibAlpha.Sl2.tensorForm`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L90).

> The contravariant form on `V(m) ⊗ V(n)`: `⟨x ⊗ y, x' ⊗ y'⟩ = ⟨x, x'⟩ ⟨y, y'⟩`.

```lean
def tensorForm : LinearMap.BilinForm ℝ (StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n)
```

**`PhyslibAlpha.Sl2.tensorForm_tmul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L93).

```lean
lemma tensorForm_tmul (x x' : StandardSl2Module ℝ m) (y y' : StandardSl2Module ℝ n) :
    tensorForm m n (x ⊗ₜ y) (x' ⊗ₜ y') = invForm ℝ m x x' * invForm ℝ n y y'
```

**`PhyslibAlpha.Sl2.tensorBilin_ext`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L98).

> Two bilinear forms on `V(m) ⊗ V(n)` agree if they agree on pure tensors.

```lean
lemma tensorBilin_ext
    {B B' : LinearMap.BilinForm ℝ (StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n)}
    (h : ∀ x y x' y', B (x ⊗ₜ y) (x' ⊗ₜ y') = B' (x ⊗ₜ y) (x' ⊗ₜ y')) : B = B'
```

**`PhyslibAlpha.Sl2.invForm_ρE_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L103).

```lean
lemma invForm_ρE_apply (x y : StandardSl2Module ℝ n) :
    invForm ℝ n (ρE x) y = invForm ℝ n x (ρF y)
```

**`PhyslibAlpha.Sl2.invForm_ρH_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L107).

```lean
lemma invForm_ρH_apply (x y : StandardSl2Module ℝ n) :
    invForm ℝ n (ρH x) y = invForm ℝ n x (ρH y)
```

**`PhyslibAlpha.Sl2.tensorForm_comm`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L112).

> The form on the tensor product is symmetric.

```lean
lemma tensorForm_comm (x y : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    tensorForm m n x y = tensorForm m n y x
```

**`PhyslibAlpha.Sl2.tensorForm_tensorE`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L119).

> The diagonal raising and lowering operators are adjoint: `⟨E x, y⟩ = ⟨x, F y⟩`.

```lean
lemma tensorForm_tensorE (x y : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    tensorForm m n (tensorE m n x) y = tensorForm m n x (tensorF m n y)
```

**`PhyslibAlpha.Sl2.tensorForm_tensorF`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L129).

> `⟨F x, y⟩ = ⟨x, E y⟩`.

```lean
lemma tensorForm_tensorF (x y : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    tensorForm m n (tensorF m n x) y = tensorForm m n x (tensorE m n y)
```

**`PhyslibAlpha.Sl2.tensorForm_tensorH`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L134).

> The diagonal weight operator is symmetric.

```lean
lemma tensorForm_tensorH (x y : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    tensorForm m n (tensorH m n x) y = tensorForm m n x (tensorH m n y)
```

## B. Inner products of the lowering strings

**`PhyslibAlpha.Sl2.tensorForm_hwVec_of_ne`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L150).

> Highest-weight vectors of different weight are orthogonal.

```lean
lemma tensorForm_hwVec_of_ne {k k' : ℕ} (hk : k ≠ k') :
    tensorForm m n (hwVec m n k) (hwVec m n k') = 0
```

**`PhyslibAlpha.Sl2.stringVec_zero'`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L163).

```lean
lemma stringVec_zero' (k : ℕ) : stringVec (K := ℝ) m n k 0 = hwVec m n k
```

**`PhyslibAlpha.Sl2.tensorForm_stringVec`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L168).

> The inner products of the lowering strings:
> `⟨f^a w_k, f^b w_{k'}⟩ = δ_{kk'} δ_{ab} · normSq (m + n - 2k) a · ⟨w_k, w_k⟩`.

```lean
lemma tensorForm_stringVec (hmn : 0 < m + n) {k k' : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hk'm : k' ≤ m) (hk'n : k' ≤ n) (a b : ℕ) :
    tensorForm m n (stringVec m n k a) (stringVec m n k' b) =
      if k = k' ∧ a = b then
        (normSq (m + n - 2 * k) a : ℝ) * tensorForm m n (hwVec m n k) (hwVec m n k)
      else 0
```

**`PhyslibAlpha.Sl2.hwNormSq`**, a def, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L206).

> The squared norm `⟨w_k, w_k⟩` of the highest-weight vector `w_k`.

```lean
def hwNormSq (k : ℕ) : ℝ
```

**`PhyslibAlpha.Sl2.hwNormSq_eq`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L209).

> `⟨w_k, w_k⟩ = Σ_a cgCoeff(a)² · normSq m a · normSq n (k - a)`.

```lean
lemma hwNormSq_eq {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) :
    hwNormSq m n k = ∑ a ∈ Finset.range (k + 1),
      cgCoeff (K := ℝ) m n k a ^ 2 * (normSq m a : ℝ) * (normSq n (k - a) : ℝ)
```

**`PhyslibAlpha.Sl2.cgCoeff_zero`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L225).

```lean
lemma cgCoeff_zero (k : ℕ) :
    cgCoeff (K := ℝ) m n k 0 = ((n - k).factorial * m.factorial : ℕ)
```

**`PhyslibAlpha.Sl2.hwNormSq_pos`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L230).

> `⟨w_k, w_k⟩ > 0`.

```lean
lemma hwNormSq_pos {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) : 0 < hwNormSq m n k
```

## C. The orthonormal coupled basis

**`PhyslibAlpha.Sl2.coupledVec`**, a def, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L247).

> The normalised coupled state `|J, M⟩` with `J = (m + n)/2 - k`, `M = J - l`.

```lean
def coupledVec (k l : ℕ) : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n
```

**`PhyslibAlpha.Sl2.tensorForm_coupledVec`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L251).

> The coupled states are orthonormal.

```lean
lemma tensorForm_coupledVec (hmn : 0 < m + n) {k k' l l' : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hk'm : k' ≤ m) (hk'n : k' ≤ n) (hl : l ≤ m + n - 2 * k) :
    tensorForm m n (coupledVec m n k l) (coupledVec m n k' l') =
      if k = k' ∧ l = l' then 1 else 0
```

**`PhyslibAlpha.Sl2.sqrt_coupled_succ`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L269).

```lean
lemma sqrt_coupled_succ {k l : ℕ} :
    Real.sqrt ((normSq (m + n - 2 * k) (l + 1) : ℝ) * hwNormSq m n k) =
      Real.sqrt ((normSq (m + n - 2 * k) l : ℝ) * hwNormSq m n k) *
        Real.sqrt (((l : ℝ) + 1) * (((m + n - 2 * k : ℕ) : ℝ) - l))
```

**`PhyslibAlpha.Sl2.tensorF_coupledVec`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L278).

> `J₋ |J, M⟩ = √((J + M)(J - M + 1)) |J, M - 1⟩`.

```lean
lemma tensorF_coupledVec {k l : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (hl : l < m + n - 2 * k) :
    tensorF m n (coupledVec m n k l) =
      Real.sqrt (((l : ℝ) + 1) * (((m + n - 2 * k : ℕ) : ℝ) - l)) • coupledVec m n k (l + 1)
```

**`PhyslibAlpha.Sl2.tensorE_coupledVec_succ`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L293).

> `J₊ |J, M⟩ = √((J - M)(J + M + 1)) |J, M + 1⟩`.

```lean
lemma tensorE_coupledVec_succ (hmn : 0 < m + n) {k l : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hl : l < m + n - 2 * k) :
    tensorE m n (coupledVec m n k (l + 1)) =
      Real.sqrt (((l : ℝ) + 1) * (((m + n - 2 * k : ℕ) : ℝ) - l)) • coupledVec m n k l
```

## D. Clebsch–Gordan coefficients

### D.1. Definition, weight rule and phase

**`PhyslibAlpha.Sl2.cgCoefficient`**, a def, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L322).

> The Clebsch–Gordan coefficient `⟨j₁ m₁ j₂ m₂ | J M⟩ = ⟨u_a ⊗ u_b, |J, M⟩⟩` with `j₁ = m/2`,
> `m₁ = j₁ - a`, `j₂ = n/2`, `m₂ = j₂ - b`, `J = (m + n)/2 - k` and `M = J - l`.

```lean
def cgCoefficient (k l a b : ℕ) : ℝ
```

**`PhyslibAlpha.Sl2.tensorH_normVec_tmul`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L325).

```lean
lemma tensorH_normVec_tmul (a b : ℕ) :
    tensorH m n (normVec m a ⊗ₜ normVec n b) =
      (((m : ℝ) - 2 * a) + ((n : ℝ) - 2 * b)) • (normVec m a ⊗ₜ normVec n b)
```

**`PhyslibAlpha.Sl2.tensorH_coupledVec`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L331).

```lean
lemma tensorH_coupledVec (hmn : 0 < m + n) {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (l : ℕ) :
    tensorH m n (coupledVec m n k l) =
      (((m + n - 2 * k : ℕ) : ℝ) - 2 * l) • coupledVec m n k l
```

**`PhyslibAlpha.Sl2.cgCoefficient_eq_zero_of_ne`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L337).

> **Weight rule.** `⟨j₁ m₁ j₂ m₂ | J M⟩ = 0` unless `m₁ + m₂ = M`, i.e. `a + b = k + l`.

```lean
lemma cgCoefficient_eq_zero_of_ne (hmn : 0 < m + n) {k l a b : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (h : a + b ≠ k + l) : cgCoefficient m n k l a b = 0
```

**`PhyslibAlpha.Sl2.invForm_normVec_vNat`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L358).

```lean
lemma invForm_normVec_vNat {a : ℕ} (ha : a ≤ n) (c : ℕ) :
    invForm ℝ n (normVec n a) (vNat n c) = if a = c then Real.sqrt (normSq n a) else 0
```

**`PhyslibAlpha.Sl2.tensorForm_normVec_hwVec`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L371).

```lean
lemma tensorForm_normVec_hwVec {k a : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (ha : a ≤ k) :
    tensorForm m n (normVec m a ⊗ₜ normVec n (k - a)) (hwVec m n k) =
      cgCoeff m n k a * Real.sqrt (normSq m a) * Real.sqrt (normSq n (k - a))
```

**`PhyslibAlpha.Sl2.cgCoefficient_top`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L387).

> The coefficients of the top state `|J, J⟩`:
> `⟨j₁ m₁ j₂ m₂ | J J⟩ = cgCoeff(a) · √(normSq m a) · √(normSq n (k - a)) / √⟨w_k, w_k⟩`.

```lean
lemma cgCoefficient_top {k a : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (ha : a ≤ k) :
    cgCoefficient m n k 0 a (k - a) =
      cgCoeff m n k a * Real.sqrt (normSq m a) * Real.sqrt (normSq n (k - a)) /
        Real.sqrt (hwNormSq m n k)
```

**`PhyslibAlpha.Sl2.cgCoefficient_top_pos`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L397).

> **Condon–Shortley phase convention.** `⟨j₁ j₁ j₂ (J - j₁) | J J⟩ > 0`.

```lean
lemma cgCoefficient_top_pos {k : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) :
    0 < cgCoefficient m n k 0 0 k
```

### D.2. Expansion and orthogonality

**`PhyslibAlpha.Sl2.eq_sum_normVec`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L416).

> Every vector of `V(n)` is `Σ_a ⟨u_a, x⟩ u_a`.

```lean
lemma eq_sum_normVec (x : StandardSl2Module ℝ n) :
    x = ∑ a ∈ Finset.range (n + 1), invForm ℝ n (normVec n a) x • normVec n a
```

**`PhyslibAlpha.Sl2.eq_sum_normVec_tmul`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L438).

> Every vector of `V(m) ⊗ V(n)` is `Σ_{a b} ⟨u_a ⊗ u_b, x⟩ u_a ⊗ u_b`.

```lean
lemma eq_sum_normVec_tmul (x : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    x = ∑ a ∈ Finset.range (m + 1), ∑ b ∈ Finset.range (n + 1),
      tensorForm m n (normVec m a ⊗ₜ normVec n b) x • (normVec m a ⊗ₜ normVec n b)
```

**`PhyslibAlpha.Sl2.coupledVec_eq_sum`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L455).

> `|J, M⟩ = Σ_{m₁ m₂} ⟨j₁ m₁ j₂ m₂ | J M⟩ |j₁ m₁⟩ ⊗ |j₂ m₂⟩`.

```lean
lemma coupledVec_eq_sum (k l : ℕ) :
    coupledVec m n k l = ∑ a ∈ Finset.range (m + 1), ∑ b ∈ Finset.range (n + 1),
      cgCoefficient m n k l a b • (normVec m a ⊗ₜ normVec n b)
```

**`PhyslibAlpha.Sl2.sum_cgCoefficient_mul`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L462).

> **Orthogonality relation.**
> `Σ_{m₁ m₂} ⟨j₁ m₁ j₂ m₂ | J M⟩ ⟨j₁ m₁ j₂ m₂ | J' M'⟩ = δ_{JJ'} δ_{MM'}`.

```lean
lemma sum_cgCoefficient_mul (hmn : 0 < m + n) {k k' l l' : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hk'm : k' ≤ m) (hk'n : k' ≤ n) (hl : l ≤ m + n - 2 * k) :
    ∑ a ∈ Finset.range (m + 1), ∑ b ∈ Finset.range (n + 1),
      cgCoefficient m n k l a b * cgCoefficient m n k' l' a b =
        if k = k' ∧ l = l' then 1 else 0
```

### D.3. Values

**`PhyslibAlpha.Sl2.hwNormSq_zero`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L478).

```lean
lemma hwNormSq_zero : hwNormSq m n 0 = ((n.factorial * m.factorial : ℕ) : ℝ) ^ 2
```

**`PhyslibAlpha.Sl2.cgCoefficient_stretched`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L483).

> `⟨j₁ j₁ j₂ j₂ | j₁+j₂, j₁+j₂⟩ = 1`.

```lean
lemma cgCoefficient_stretched : cgCoefficient m n 0 0 0 0 = 1
```

**`PhyslibAlpha.Sl2.hwNormSq_one_one`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L492).

```lean
lemma hwNormSq_one_one : hwNormSq 1 1 1 = 2
```

**`PhyslibAlpha.Sl2.cgCoefficient_singlet_up`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L497).

> Singlet: `⟨½ ½ ½ -½ | 0 0⟩ = 1/√2`.

```lean
lemma cgCoefficient_singlet_up : cgCoefficient 1 1 1 0 0 1 = 1 / Real.sqrt 2
```

**`PhyslibAlpha.Sl2.cgCoefficient_singlet_down`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L504).

> Singlet: `⟨½ -½ ½ ½ | 0 0⟩ = -1/√2`.

```lean
lemma cgCoefficient_singlet_down : cgCoefficient 1 1 1 0 1 0 = -1 / Real.sqrt 2
```

**`PhyslibAlpha.Sl2.coupledVec_one_one_zero_one`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L510).

```lean
lemma coupledVec_one_one_zero_one :
    coupledVec 1 1 0 1 = (1 / Real.sqrt 2) • tensorF 1 1 (coupledVec 1 1 0 0)
```

**`PhyslibAlpha.Sl2.ρE_normVec_one_zero`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L517).

```lean
lemma ρE_normVec_one_zero : (ρE : Module.End ℝ (StandardSl2Module ℝ 1)) (normVec 1 0) = 0
```

**`PhyslibAlpha.Sl2.ρE_normVec_one_one`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L520).

```lean
lemma ρE_normVec_one_one :
    (ρE : Module.End ℝ (StandardSl2Module ℝ 1)) (normVec 1 1) = normVec 1 0
```

**`PhyslibAlpha.Sl2.cgCoefficient_triplet_zero_up`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L527).

> Triplet: `⟨½ ½ ½ -½ | 1 0⟩ = 1/√2`.

```lean
lemma cgCoefficient_triplet_zero_up : cgCoefficient 1 1 0 1 0 1 = 1 / Real.sqrt 2
```

**`PhyslibAlpha.Sl2.cgCoefficient_triplet_zero_down`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L536).

> Triplet: `⟨½ -½ ½ ½ | 1 0⟩ = 1/√2`.

```lean
lemma cgCoefficient_triplet_zero_down : cgCoefficient 1 1 0 1 1 0 = 1 / Real.sqrt 2
```

**`PhyslibAlpha.Sl2.coupledVec_one_one_zero_two`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L544).

```lean
lemma coupledVec_one_one_zero_two :
    coupledVec 1 1 0 2 = (1 / Real.sqrt 2) • tensorF 1 1 (coupledVec 1 1 0 1)
```

**`PhyslibAlpha.Sl2.cgCoefficient_triplet_minus`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean#L552).

> Triplet: `⟨½ -½ ½ -½ | 1 -1⟩ = 1`.

```lean
lemma cgCoefficient_triplet_minus : cgCoefficient 1 1 0 2 1 1 = 1
```

## Depends on

- [The equivariant Clebsch–Gordan decomposition](../../mathematics/part-02/representationtheory/sl2-tensordecomposition.md)
- [The invariant form and the normalised basis of the standard modules](normalizedbasis.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/ClebschGordanCoefficients.lean)
