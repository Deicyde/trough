---
declaration: module
origin: cited
lean: GellMann.Index, GellMann.diagProfile, GellMann.diagNorm, GellMann.matrix, GellMann.sum_diagProfile, GellMann.sum_diagProfile_mul, GellMann.diagNorm_mul_self, GellMann.trace_matrix_inl_mul
statement: formalized
proof: formalized
---

# The generalized Gell-Mann matrices (PhyslibAlpha)

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.GellMann`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean): 33 declarations, 29 with a docstring; 6 private, not shown.

> A basis of the traceless complex matrices generalizing the Pauli and the Gell-Mann matrices.

## i. Overview

> The generalized Gell-Mann matrices are the standard basis of the traceless complex `N × N`
> matrices, the complexified Lie algebra of `SU(N)`, generalizing the Pauli matrices (`N = 2`) and
> the Gell-Mann matrices (`N = 3`). There are `N² - 1` of them, of three kinds:
>
> - for `j < k` the symmetric matrix `E_jk + E_kj`,
> - for `j < k` the antisymmetric matrix `-i E_jk + i E_kj`,
> - for `1 ≤ n ≤ N - 1` the diagonal matrix `√(2 / (n (n + 1))) (E_00 + ⋯ + E_(n-1)(n-1) - n E_nn)`.
>
> They are hermitian and traceless, and orthogonal under the trace form, `tr (λ_a λ_b) = 2 δ_ab`.
> Orthogonality makes them linearly independent, and there are as many as the dimension of the
> traceless matrices, so they form a basis, `GellMann.basis`, whose coordinates are read off by the
> trace form, `GellMann.basis_repr_apply`. Being hermitian they lie in the real Lie algebra `su(N)`
> of traceless hermitian matrices, and there they form a real basis, `GellMann.realBasis`: the
> coordinates `tr (λ_a H) / 2` of a traceless hermitian matrix `H` are real (E).

## ii. Key results

> - `GellMann.Index` : the labels of the generalized Gell-Mann matrices.
> - `GellMann.matrix` : the generalized Gell-Mann matrices.
> - `GellMann.trace_matrix_mul_matrix` : `tr (λ_a λ_b) = 2 δ_ab`.
> - `GellMann.basis` : the basis of the traceless matrices they form.
> - `GellMann.realBasis` : the basis of the real Lie algebra `su(N)` they form.

## iv. References

> * None.

## A. The matrices

**`GellMann.Index`**, an abbrev, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L68).

> The labels of the generalized Gell-Mann matrices, a pair `j < k` for each symmetric and each
> antisymmetric matrix, and `l : Fin (N - 1)` for the diagonal matrix of size `n = l + 1`.

```lean
abbrev Index (N : ℕ) : Type
```

**`GellMann.diagProfile`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L75).

> The diagonal profile of size `n = l + 1`, `1` on the first `n` entries, `-n` on the next, and
> `0` beyond.

```lean
def diagProfile (l : Fin (N - 1)) (m : Fin N) : ℂ
```

**`GellMann.diagNorm`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L79).

> The normalization `√(2 / (n (n + 1)))` of the diagonal matrix of size `n = l + 1`.

```lean
noncomputable def diagNorm (l : Fin (N - 1)) : ℂ
```

**`GellMann.matrix`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L83).

> The generalized Gell-Mann matrices.

```lean
noncomputable def matrix : Index N → Matrix (Fin N) (Fin N) ℂ
```

## B. The diagonal profiles

**`GellMann.sum_diagProfile`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L109).

```lean
lemma sum_diagProfile (l : Fin (N - 1)) : ∑ m, diagProfile l m = 0
```

**`GellMann.sum_diagProfile_mul`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L146).

> The diagonal profiles are orthogonal, with `∑ d_l (m)² = n (n + 1)` for `n = l + 1`.

```lean
lemma sum_diagProfile_mul (l l' : Fin (N - 1)) :
    ∑ m, diagProfile l m * diagProfile l' m
      = if l = l' then ((l.val + 1 : ℕ) : ℂ) * ((l.val + 2 : ℕ) : ℂ) else 0
```

**`GellMann.diagNorm_mul_self`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L173).

> The square of the normalization of the diagonal matrix of size `n = l + 1` is
> `2 / (n (n + 1))`.

```lean
lemma diagNorm_mul_self (l : Fin (N - 1)) :
    diagNorm l * diagNorm l * (((l.val + 1 : ℕ) : ℂ) * ((l.val + 2 : ℕ) : ℂ)) = 2
```

## C. Orthogonality

**`GellMann.trace_matrix_inl_mul`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L189).

> The trace of the product of a symmetric Gell-Mann matrix with any complex matrix is the sum
> of the two entries of that matrix at the positions of the Gell-Mann matrix's units.

```lean
lemma trace_matrix_inl_mul (p : {p : Fin N × Fin N // p.1 < p.2}) (X : Matrix (Fin N) (Fin N) ℂ) :
    (matrix (.inl p) * X).trace = X p.1.2 p.1.1 + X p.1.1 p.1.2
```

**`GellMann.trace_matrix_inr_inl_mul`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L196).

> The trace of the product of an antisymmetric Gell-Mann matrix with any complex matrix is the
> difference of the two entries of that matrix at the positions of the Gell-Mann matrix's
> units, weighted by `i`.

```lean
lemma trace_matrix_inr_inl_mul (p : {p : Fin N × Fin N // p.1 < p.2})
    (X : Matrix (Fin N) (Fin N) ℂ) :
    (matrix (.inr (.inl p)) * X).trace
      = -Complex.I * X p.1.2 p.1.1 + Complex.I * X p.1.1 p.1.2
```

**`GellMann.trace_matrix_inr_inr_mul`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L205).

> The trace of the product of a diagonal Gell-Mann matrix with any complex matrix is its
> normalization times the sum of the diagonal entries of that matrix weighted by the diagonal
> profile.

```lean
lemma trace_matrix_inr_inr_mul (l : Fin (N - 1)) (X : Matrix (Fin N) (Fin N) ℂ) :
    (matrix (.inr (.inr l)) * X).trace = diagNorm l * ∑ m, diagProfile l m * X m m
```

**`GellMann.matrix_inl_apply`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L210).

> The entries of a symmetric Gell-Mann matrix.

```lean
lemma matrix_inl_apply (p : {p : Fin N × Fin N // p.1 < p.2}) (m n : Fin N) :
    matrix (.inl p) m n
      = (if p.1.1 = m ∧ p.1.2 = n then 1 else 0) + (if p.1.2 = m ∧ p.1.1 = n then 1 else 0)
```

**`GellMann.matrix_inr_inl_apply`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L216).

> The entries of an antisymmetric Gell-Mann matrix.

```lean
lemma matrix_inr_inl_apply (p : {p : Fin N × Fin N // p.1 < p.2}) (m n : Fin N) :
    matrix (.inr (.inl p)) m n = (if p.1.1 = m ∧ p.1.2 = n then -Complex.I else 0)
      + (if p.1.2 = m ∧ p.1.1 = n then Complex.I else 0)
```

**`GellMann.matrix_inr_inr_apply`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L222).

> The entries of a diagonal Gell-Mann matrix.

```lean
lemma matrix_inr_inr_apply (l : Fin (N - 1)) (m n : Fin N) :
    matrix (.inr (.inr l)) m n = if m = n then diagNorm l * diagProfile l m else 0
```

**`GellMann.trace_matrix_inl_mul_matrix`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L232).

> The symmetric Gell-Mann matrices are orthogonal to all others and have norm `2`.

```lean
lemma trace_matrix_inl_mul_matrix (p : {p : Fin N × Fin N // p.1 < p.2}) (b : Index N) :
    (matrix (.inl p) * matrix b).trace = if .inl p = b then 2 else 0
```

**`GellMann.trace_matrix_inr_inl_mul_matrix`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L262).

> The antisymmetric Gell-Mann matrices are orthogonal to all others and have norm `2`.

```lean
lemma trace_matrix_inr_inl_mul_matrix (p : {p : Fin N × Fin N // p.1 < p.2}) (b : Index N) :
    (matrix (.inr (.inl p)) * matrix b).trace = if .inr (.inl p) = b then 2 else 0
```

**`GellMann.trace_matrix_inr_inr_mul_matrix`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L293).

> The diagonal Gell-Mann matrices are orthogonal to all others and have norm `2`.

```lean
lemma trace_matrix_inr_inr_mul_matrix (l : Fin (N - 1)) (b : Index N) :
    (matrix (.inr (.inr l)) * matrix b).trace = if .inr (.inr l) = b then 2 else 0
```

**`GellMann.trace_matrix_mul_matrix`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L324).

> The generalized Gell-Mann matrices are orthogonal under the trace form,
> `tr (λ_a λ_b) = 2 δ_ab`.

```lean
lemma trace_matrix_mul_matrix (a b : Index N) :
    (matrix a * matrix b).trace = if a = b then 2 else 0
```

## D. The basis

**`GellMann.trace_matrix`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L338).

> The generalized Gell-Mann matrices are traceless.

```lean
lemma trace_matrix (a : Index N) : (matrix a).trace = 0
```

**`GellMann.conjTranspose_matrix`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L349).

> The generalized Gell-Mann matrices are hermitian.

```lean
lemma conjTranspose_matrix (a : Index N) : (matrix a)ᴴ = matrix a
```

**`GellMann.traceless`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L362).

> The generalized Gell-Mann matrices as traceless matrices.

```lean
noncomputable def traceless (a : Index N) :
    ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))
```

**`GellMann.linearIndependent_traceless`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L367).

> The generalized Gell-Mann matrices are linearly independent, by orthogonality.

```lean
lemma linearIndependent_traceless : LinearIndependent ℂ (traceless (N := N))
```

**`GellMann.two_mul_card_lt_add`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L380).

> There are `N² - 1` ordered pairs with `j < k`, counted twice, and `N - 1` diagonal labels,
> `2 #{j < k} + N = N²`.

```lean
lemma two_mul_card_lt_add :
    2 * Fintype.card {p : Fin N × Fin N // p.1 < p.2} + N = N * N
```

**`GellMann.finrank_traceless`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L403).

> The traceless `N × N` matrices have dimension `N² - 1`.

```lean
lemma finrank_traceless :
    finrank ℂ ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ)) = N * N - 1
```

**`GellMann.card_index`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L414).

```lean
lemma card_index : Fintype.card (Index N)
    = finrank ℂ ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))
```

**`GellMann.basis`**, a def, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L423).

> The generalized Gell-Mann basis of the traceless complex `N × N` matrices.

```lean
noncomputable def basis : Basis (Index N) ℂ ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))
```

**`GellMann.basis_apply_val`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L427).

```lean
lemma basis_apply_val (a : Index N) : (basis a).1 = matrix a
```

**`GellMann.basis_repr_apply`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L432).

> The coordinates of a traceless matrix in the Gell-Mann basis are read off by the trace form,
> `x = ∑ (tr (λ_a x) / 2) λ_a`.

```lean
lemma basis_repr_apply (x : ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))) (a : Index N) :
    basis.repr x a = (matrix a * x.1).trace / 2
```

## E. The real basis of `su(N)`

**`GellMann.hermitian`**, a def, [line 447](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L447).

> The generalized Gell-Mann matrices as elements of the real Lie algebra `su(N)`.

```lean
noncomputable def hermitian (a : Index N) : SUAlgebraOver ℂ N
```

**`GellMann.linearIndependent_hermitian`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L451).

> The generalized Gell-Mann matrices are linearly independent over the reals.

```lean
lemma linearIndependent_hermitian : LinearIndependent ℝ (hermitian (N := N))
```

**`GellMann.trace_mul_ofReal_re`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L462).

> The trace pairing of two hermitian matrices is real.

```lean
lemma trace_mul_ofReal_re {A H : Matrix (Fin N) (Fin N) ℂ} (hA : Aᴴ = A) (hH : Hᴴ = H) :
    (((A * H).trace.re : ℝ) : ℂ) = (A * H).trace
```

**`GellMann.eq_sum_re_trace_smul_hermitian`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L470).

> A traceless hermitian matrix is the real combination `∑ (tr (λ_a H) / 2) λ_a` of the
> generalized Gell-Mann matrices.

```lean
lemma eq_sum_re_trace_smul_hermitian (H : SUAlgebraOver ℂ N) :
    ∑ a, ((matrix a * H.1).trace.re / 2) • hermitian a = H
```

**`GellMann.realBasis`**, a def, [line 484](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L484).

> The generalized Gell-Mann basis of the real Lie algebra `su(N)`.

```lean
noncomputable def realBasis : Basis (Index N) ℝ (SUAlgebraOver ℂ N)
```

**`GellMann.realBasis_apply_val`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean#L489).

```lean
lemma realBasis_apply_val (a : Index N) : (realBasis a).1 = matrix a
```

## Depends on

- [The Lie algebra `su(n)` over a `*`-algebra](globalgaugegroup-su-algebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/GellMann.lean)
