---
declaration: module
origin: cited
lean: GellMann.Index, GellMann.diagProfile, GellMann.diagNorm, GellMann.matrix, GellMann.sum_diagProfile, GellMann.sum_diagProfile_mul, GellMann.diagNorm_mul_self, GellMann.trace_matrix_inl_mul
statement: formalized
proof: formalized
---

# The generalized Gell-Mann matrices

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.GellMann`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean): 33 declarations, 29 with a docstring; 6 private, not shown.

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

**`GellMann.Index`**, an abbrev, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L66).

> The labels of the generalized Gell-Mann matrices: a pair `j < k` for each symmetric and each
> antisymmetric matrix, and `l : Fin (N - 1)` for the diagonal matrix of size `n = l + 1`.

```lean
abbrev Index (N : ℕ) : Type
```

**`GellMann.diagProfile`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L73).

> The diagonal profile of size `n = l + 1`: `1` on the first `n` entries, `-n` on the next, and
> `0` beyond.

```lean
def diagProfile (l : Fin (N - 1)) (m : Fin N) : ℂ
```

**`GellMann.diagNorm`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L77).

> The normalization `√(2 / (n (n + 1)))` of the diagonal matrix of size `n = l + 1`.

```lean
noncomputable def diagNorm (l : Fin (N - 1)) : ℂ
```

**`GellMann.matrix`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L81).

> The generalized Gell-Mann matrices.

```lean
noncomputable def matrix : Index N → Matrix (Fin N) (Fin N) ℂ
```

## B. The diagonal profiles

**`GellMann.sum_diagProfile`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L107).

```lean
lemma sum_diagProfile (l : Fin (N - 1)) : ∑ m, diagProfile l m = 0
```

**`GellMann.sum_diagProfile_mul`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L144).

> The diagonal profiles are orthogonal, with `∑ d_l (m)² = n (n + 1)` for `n = l + 1`.

```lean
lemma sum_diagProfile_mul (l l' : Fin (N - 1)) :
    ∑ m, diagProfile l m * diagProfile l' m
      = if l = l' then ((l.val + 1 : ℕ) : ℂ) * ((l.val + 2 : ℕ) : ℂ) else 0
```

**`GellMann.diagNorm_mul_self`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L171).

> The square of the normalization of the diagonal matrix of size `n = l + 1` is
> `2 / (n (n + 1))`.

```lean
lemma diagNorm_mul_self (l : Fin (N - 1)) :
    diagNorm l * diagNorm l * (((l.val + 1 : ℕ) : ℂ) * ((l.val + 2 : ℕ) : ℂ)) = 2
```

## C. Orthogonality

**`GellMann.trace_matrix_inl_mul`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L186).

> The trace of a symmetric Gell-Mann matrix against `X`.

```lean
lemma trace_matrix_inl_mul (p : {p : Fin N × Fin N // p.1 < p.2}) (X : Matrix (Fin N) (Fin N) ℂ) :
    (matrix (.inl p) * X).trace = X p.1.2 p.1.1 + X p.1.1 p.1.2
```

**`GellMann.trace_matrix_inr_inl_mul`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L191).

> The trace of an antisymmetric Gell-Mann matrix against `X`.

```lean
lemma trace_matrix_inr_inl_mul (p : {p : Fin N × Fin N // p.1 < p.2})
    (X : Matrix (Fin N) (Fin N) ℂ) :
    (matrix (.inr (.inl p)) * X).trace
      = -Complex.I * X p.1.2 p.1.1 + Complex.I * X p.1.1 p.1.2
```

**`GellMann.trace_matrix_inr_inr_mul`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L198).

> The trace of a diagonal Gell-Mann matrix against `X`.

```lean
lemma trace_matrix_inr_inr_mul (l : Fin (N - 1)) (X : Matrix (Fin N) (Fin N) ℂ) :
    (matrix (.inr (.inr l)) * X).trace = diagNorm l * ∑ m, diagProfile l m * X m m
```

**`GellMann.matrix_inl_apply`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L203).

> The entries of a symmetric Gell-Mann matrix.

```lean
lemma matrix_inl_apply (p : {p : Fin N × Fin N // p.1 < p.2}) (m n : Fin N) :
    matrix (.inl p) m n
      = (if p.1.1 = m ∧ p.1.2 = n then 1 else 0) + (if p.1.2 = m ∧ p.1.1 = n then 1 else 0)
```

**`GellMann.matrix_inr_inl_apply`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L209).

> The entries of an antisymmetric Gell-Mann matrix.

```lean
lemma matrix_inr_inl_apply (p : {p : Fin N × Fin N // p.1 < p.2}) (m n : Fin N) :
    matrix (.inr (.inl p)) m n = (if p.1.1 = m ∧ p.1.2 = n then -Complex.I else 0)
      + (if p.1.2 = m ∧ p.1.1 = n then Complex.I else 0)
```

**`GellMann.matrix_inr_inr_apply`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L215).

> The entries of a diagonal Gell-Mann matrix.

```lean
lemma matrix_inr_inr_apply (l : Fin (N - 1)) (m n : Fin N) :
    matrix (.inr (.inr l)) m n = if m = n then diagNorm l * diagProfile l m else 0
```

**`GellMann.trace_matrix_inl_mul_matrix`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L225).

> The symmetric Gell-Mann matrices are orthogonal to all others and have norm `2`.

```lean
lemma trace_matrix_inl_mul_matrix (p : {p : Fin N × Fin N // p.1 < p.2}) (b : Index N) :
    (matrix (.inl p) * matrix b).trace = if .inl p = b then 2 else 0
```

**`GellMann.trace_matrix_inr_inl_mul_matrix`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L255).

> The antisymmetric Gell-Mann matrices are orthogonal to all others and have norm `2`.

```lean
lemma trace_matrix_inr_inl_mul_matrix (p : {p : Fin N × Fin N // p.1 < p.2}) (b : Index N) :
    (matrix (.inr (.inl p)) * matrix b).trace = if .inr (.inl p) = b then 2 else 0
```

**`GellMann.trace_matrix_inr_inr_mul_matrix`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L286).

> The diagonal Gell-Mann matrices are orthogonal to all others and have norm `2`.

```lean
lemma trace_matrix_inr_inr_mul_matrix (l : Fin (N - 1)) (b : Index N) :
    (matrix (.inr (.inr l)) * matrix b).trace = if .inr (.inr l) = b then 2 else 0
```

**`GellMann.trace_matrix_mul_matrix`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L317).

> The generalized Gell-Mann matrices are orthogonal under the trace form:
> `tr (λ_a λ_b) = 2 δ_ab`.

```lean
lemma trace_matrix_mul_matrix (a b : Index N) :
    (matrix a * matrix b).trace = if a = b then 2 else 0
```

## D. The basis

**`GellMann.trace_matrix`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L331).

> The generalized Gell-Mann matrices are traceless.

```lean
lemma trace_matrix (a : Index N) : (matrix a).trace = 0
```

**`GellMann.conjTranspose_matrix`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L342).

> The generalized Gell-Mann matrices are hermitian.

```lean
lemma conjTranspose_matrix (a : Index N) : (matrix a)ᴴ = matrix a
```

**`GellMann.traceless`**, a def, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L355).

> The generalized Gell-Mann matrices as traceless matrices.

```lean
noncomputable def traceless (a : Index N) :
    ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))
```

**`GellMann.linearIndependent_traceless`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L360).

> The generalized Gell-Mann matrices are linearly independent, by orthogonality.

```lean
lemma linearIndependent_traceless : LinearIndependent ℂ (traceless (N := N))
```

**`GellMann.two_mul_card_lt_add`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L373).

> There are `N² - 1` ordered pairs with `j < k`, counted twice, and `N - 1` diagonal labels:
> `2 #{j < k} + N = N²`.

```lean
lemma two_mul_card_lt_add :
    2 * Fintype.card {p : Fin N × Fin N // p.1 < p.2} + N = N * N
```

**`GellMann.finrank_traceless`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L396).

> The traceless `N × N` matrices have dimension `N² - 1`.

```lean
lemma finrank_traceless :
    finrank ℂ ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ)) = N * N - 1
```

**`GellMann.card_index`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L407).

```lean
lemma card_index : Fintype.card (Index N)
    = finrank ℂ ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))
```

**`GellMann.basis`**, a def, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L416).

> **The generalized Gell-Mann basis** of the traceless complex `N × N` matrices.

```lean
noncomputable def basis : Basis (Index N) ℂ ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))
```

**`GellMann.basis_apply_val`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L420).

```lean
lemma basis_apply_val (a : Index N) : (basis a).1 = matrix a
```

**`GellMann.basis_repr_apply`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L425).

> The coordinates of a traceless matrix in the Gell-Mann basis are read off by the trace form,
> `x = ∑ (tr (λ_a x) / 2) λ_a`.

```lean
lemma basis_repr_apply (x : ↥(LinearMap.ker (Matrix.traceLinearMap (Fin N) ℂ ℂ))) (a : Index N) :
    basis.repr x a = (matrix a * x.1).trace / 2
```

## E. The real basis of `su(N)`

**`GellMann.hermitian`**, a def, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L440).

> The generalized Gell-Mann matrices as elements of the real Lie algebra `su(N)`.

```lean
noncomputable def hermitian (a : Index N) : SUAlgebraOver ℂ N
```

**`GellMann.linearIndependent_hermitian`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L444).

> The generalized Gell-Mann matrices are linearly independent over the reals.

```lean
lemma linearIndependent_hermitian : LinearIndependent ℝ (hermitian (N := N))
```

**`GellMann.trace_mul_ofReal_re`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L455).

> The trace pairing of two hermitian matrices is real.

```lean
lemma trace_mul_ofReal_re {A H : Matrix (Fin N) (Fin N) ℂ} (hA : Aᴴ = A) (hH : Hᴴ = H) :
    (((A * H).trace.re : ℝ) : ℂ) = (A * H).trace
```

**`GellMann.eq_sum_re_trace_smul_hermitian`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L463).

> A traceless hermitian matrix is the real combination `∑ (tr (λ_a H) / 2) λ_a` of the
> generalized Gell-Mann matrices.

```lean
lemma eq_sum_re_trace_smul_hermitian (H : SUAlgebraOver ℂ N) :
    ∑ a, ((matrix a * H.1).trace.re / 2) • hermitian a = H
```

**`GellMann.realBasis`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L477).

> **The generalized Gell-Mann basis** of the real Lie algebra `su(N)`.

```lean
noncomputable def realBasis : Basis (Index N) ℝ (SUAlgebraOver ℂ N)
```

**`GellMann.realBasis_apply_val`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean#L482).

```lean
lemma realBasis_apply_val (a : Index N) : (realBasis a).1 = matrix a
```

## Depends on

- [The Lie algebra `su(n)` over a `*`-algebra](localgaugedata-su-algebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/GellMann.lean)
