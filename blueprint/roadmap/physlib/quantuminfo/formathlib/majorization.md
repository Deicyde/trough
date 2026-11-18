---
declaration: module
origin: cited
lean: singularValues, singularValues_nonneg, singularValuesSorted, singularValuesSorted_nonneg, sum_singularValues_rpow_eq_sum_sorted, singularValuesSorted_antitone, antitone_mul_of_antitone_nonneg, AllOrdered.fintypeLinearOrderClassical
statement: formalized
proof: formalized
---

# Majorization and weak log-majorization

The module `QuantumInfo.ForMathlib.Majorization`, [QuantumInfo/ForMathlib/Majorization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean): 41 declarations, 34 with a docstring.

> This file develops the theory of majorization for finite sequences, leading to
> the key singular value inequality needed for the Schatten–Hölder inequality.

## Main results

> * `sum_rpow_singularValues_mul_le`: for `r > 0`, the singular values of `A * B`
>   satisfy `∑ σᵢ(AB)^r ≤ ∑ σ↓ᵢ(A)^r · σ↓ᵢ(B)^r`.
> * `holder_step_for_singularValues`: the Hölder step giving
>   `∑ σ↓ᵢ(A)^r · σ↓ᵢ(B)^r ≤ (∑ σᵢ(A)^p)^{r/p} · (∑ σᵢ(B)^q)^{r/q}`.

## Sorted singular values

**`singularValues`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L41).

> The singular values of a square complex matrix `A`, defined as the square
> roots of the eigenvalues of `A†A`. These are indexed by `d` without a
> particular ordering.
>
> Note: We use `A.conjTranspose` as the argument to `isHermitian_mul_conjTranspose_self`
> so that the underlying Hermitian matrix is `A† * A` (matching the convention in `schattenNorm`).

```lean
def singularValues (A : Matrix d d ℂ) : d → ℝ
```

**`singularValues_nonneg`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L45).

> Singular values are nonneg.

```lean
lemma singularValues_nonneg (A : Matrix d d ℂ) (i : d) :
    0 ≤ singularValues A i
```

**`singularValuesSorted`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L53).

> The sorted singular values of a square complex matrix, in decreasing order,
> indexed by `Fin (Fintype.card d)`.
>
> We define them by sorting the multiset of singular values.

```lean
noncomputable def singularValuesSorted (A : Matrix d d ℂ) :
    Fin (Fintype.card d) → ℝ
```

**`singularValuesSorted_nonneg`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L61).

> Sorted singular values are nonneg.

```lean
lemma singularValuesSorted_nonneg (A : Matrix d d ℂ) (i : Fin (Fintype.card d)) :
    0 ≤ singularValuesSorted A i
```

**`sum_singularValues_rpow_eq_sum_sorted`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L76).

> The sum `∑ singularValues A i ^ p` equals the sum over sorted singular values.

```lean
lemma sum_singularValues_rpow_eq_sum_sorted (A : Matrix d d ℂ) (p : ℝ) :
    ∑ i : d, singularValues A i ^ p =
    ∑ i : Fin (Fintype.card d), singularValuesSorted A i ^ p
```

## Weak log-majorization and its consequences

**`singularValuesSorted_antitone`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L95).

> Sorted singular values are antitone (decreasing).

```lean
lemma singularValuesSorted_antitone (A : Matrix d d ℂ) :
    Antitone (singularValuesSorted A)
```

**`antitone_mul_of_antitone_nonneg`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L103).

> The product of nonneg antitone sequences is antitone.

```lean
lemma antitone_mul_of_antitone_nonneg {n : ℕ}
    {f g : Fin n → ℝ} (hf : Antitone f) (hg : Antitone g)
    (hf_nn : ∀ i, 0 ≤ f i) (hg_nn : ∀ i, 0 ≤ g i) :
    Antitone (fun i => f i * g i)
```

### Compound matrices and auxiliary lemmas for Horn's inequality

> The proof of Horn's inequality uses the *compound matrix* (or *k-th exterior power*
> of a matrix).  For a `d × d` matrix `M` and `k ≤ card d`, the `k`-th compound matrix
> `C_k(M)` is indexed by `k`-element subsets of the index type, with entry `(S, T)` being
> the minor `det M[S, T]`.
>
> The key properties are:
> 1. **Cauchy–Binet**: `C_k(M N) = C_k(M) · C_k(N)`.
> 2. **Spectral characterisation**: the largest singular value of `C_k(M)` is
>    `∏_{i=1}^k σ↓ᵢ(M)`.
> 3. **Operator-norm submultiplicativity**: `σ₁(A B) ≤ σ₁(A) · σ₁(B)`.
>
> Combining these gives Horn's inequality:
>   `∏ σ↓(AB) = σ₁(C\_k(AB)) = σ₁(C\_k(A) C\_k(B)) ≤ σ₁(C\_k(A)) σ₁(C\_k(B))
>             = (∏ σ↓(A))(∏ σ↓(B))`.

**`AllOrdered.fintypeLinearOrderClassical`**, an instance, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L130).

> A `LinearOrder` on any `Fintype`, obtained classically via well-ordering.

```lean
scoped instance fintypeLinearOrderClassical (α : Type*) [Fintype α] [DecidableEq α] :
    LinearOrder α
```

**`compoundMatrix`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L140).

> The `k`-th compound (exterior-power) matrix of `M`.

```lean
noncomputable def compoundMatrix (M : Matrix d d ℂ) (k : ℕ) :
    Matrix {S : Finset d // S.card = k} {S : Finset d // S.card = k} ℂ
```

**`cauchyBinet`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L150).

> **Cauchy–Binet formula** for rectangular matrices: if `A` is `m × n` and `B` is
> `n × m`, then `det(A * B) = ∑_S det(A[:,S]) * det(B[S,:])` where the sum is
> over `m`-element subsets `S` of the column/row index.

```lean
lemma cauchyBinet {m : ℕ} {n : Type*} [Fintype n] [DecidableEq n] [LinearOrder n]
    {R : Type*} [CommRing R]
    (A : Matrix (Fin m) n R) (B : Matrix n (Fin m) R) :
    (A * B).det = ∑ S : {S : Finset n // S.card = m},
      (A.submatrix id (S.1.orderEmbOfFin S.2)).det *
      (B.submatrix (S.1.orderEmbOfFin S.2) id).det
```

**`compoundMatrix_mul`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L237).

> The `compoundMatrix` of a product is the product of the `compoundMatrix`s.

```lean
lemma compoundMatrix_mul (M N : Matrix d d ℂ) (k : ℕ) :
    compoundMatrix (M * N) k = compoundMatrix M k * compoundMatrix N k
```

**`compoundMatrix_conjTranspose`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L244).

> `compoundMatrix` commutes with `conjTranspose`.

```lean
lemma compoundMatrix_conjTranspose (M : Matrix d d ℂ) (k : ℕ) :
    compoundMatrix M.conjTranspose k = (compoundMatrix M k).conjTranspose
```

**`compoundMatrix_diagonal`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L255).

> The compound matrix of a diagonal matrix is diagonal, with entries being
> products of eigenvalues over k-subsets.

```lean
lemma compoundMatrix_diagonal (f : d → ℂ) (k : ℕ) :
    compoundMatrix (Matrix.diagonal f) k =
    Matrix.diagonal (fun S : {S : Finset d // S.card = k} =>
      ∏ i : Fin k, f (S.1.orderEmbOfFin S.2 i))
```

**`compoundMatrix_unitary`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L278).

> The compound matrix of a unitary matrix is unitary.

```lean
lemma compoundMatrix_unitary (U : Matrix d d ℂ)
    (hU : U ∈ Matrix.unitaryGroup d ℂ) (k : ℕ) :
    compoundMatrix U k ∈ Matrix.unitaryGroup {S : Finset d // S.card = k} ℂ
```

**`compoundUnitary`**, a def, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L287).

> The `k`-th compound matrix bundled as a unitary.

```lean
noncomputable def compoundUnitary (U : Matrix.unitaryGroup d ℂ) (k : ℕ) :
    Matrix.unitaryGroup {S : Finset d // S.card = k} ℂ
```

**`compound_card_pos`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L293).

> The index set of the `k`-th compound matrix is nonempty when `k ≤ card d`.

```lean
lemma compound_card_pos (k : ℕ) (hk : k ≤ Fintype.card d) :
    0 < Fintype.card {S : Finset d // S.card = k}
```

**`compoundZero`**, a def, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L301).

> The canonical zero index in `Fin (Fintype.card {S : Finset d // S.card = k})`,
> witnessed by `compound_card_pos`.

```lean
def compoundZero (k : ℕ) (hk : k ≤ Fintype.card d) :
    Fin (Fintype.card {S : Finset d // S.card = k})
```

**`singularValues_compoundMatrix_eq`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L311).

> The eigenvalues of the compound matrix of a Hermitian matrix are the products
> of eigenvalues over k-subsets. More precisely, the singular values of
> `compoundMatrix M k` are the square roots of products of eigenvalues of M†M
> over k-subsets.

```lean
lemma singularValues_compoundMatrix_eq (M : Matrix d d ℂ) (k : ℕ) :
    ∀ (S : {S : Finset d // S.card = k}),
    ∃ (j : {S : Finset d // S.card = k}),
    singularValues (compoundMatrix M k) j =
    ∏ i : Fin k, singularValues M (S.1.orderEmbOfFin S.2 i)
```

**`prod_le_prod_sorted`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L344).

> The product of nonneg values over a k-subset is at most the product of the
> k largest values.

```lean
lemma prod_le_prod_sorted {n : ℕ} {f : Fin n → ℝ}
    (hf : Antitone f) (hf_nn : ∀ i, 0 ≤ f i)
    (k : ℕ) (hk : k ≤ n)
    (g : Fin k → Fin n) (hg : Function.Injective g) :
    ∏ i : Fin k, f (g i) ≤ ∏ i : Fin k, f ⟨i.val, by omega⟩
```

**`singularValuesSorted_zero_eq_sup`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L383).

> The 0th sorted singular value is the maximum of the singular values.

```lean
lemma singularValuesSorted_zero_eq_sup {e : Type*} [Fintype e] [DecidableEq e]
    (A : Matrix e e ℂ) (h : 0 < Fintype.card e) :
    singularValuesSorted A ⟨0, h⟩ = Finset.sup' Finset.univ
      (Finset.univ_nonempty_iff.mpr (Fintype.card_pos_iff.mp h))
      (singularValues A)
```

**`singularValues_mem_sorted`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L407).

> Each singular value appears in the sorted list.

```lean
lemma singularValues_mem_sorted {e : Type*} [Fintype e] [DecidableEq e]
    (A : Matrix e e ℂ) (i : e) :
    ∃ j : Fin (Fintype.card e), singularValues A i = singularValuesSorted A j
```

**`singularValuesSorted_mem_values`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L416).

> Each sorted singular value appears among the original singular values.

```lean
lemma singularValuesSorted_mem_values {e : Type*} [Fintype e] [DecidableEq e]
    (A : Matrix e e ℂ) (j : Fin (Fintype.card e)) :
    ∃ i : e, singularValuesSorted A j = singularValues A i
```

**`singularValues_compoundMatrix_perm`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L427).

> Stronger version of `singularValues_compoundMatrix_eq` that exposes the permutation.

```lean
lemma singularValues_compoundMatrix_perm (M : Matrix d d ℂ) (k : ℕ) :
    ∃ σ : {S : Finset d // S.card = k} ≃ {S : Finset d // S.card = k},
    ∀ S, singularValues (compoundMatrix M k) (σ S) =
    ∏ i : Fin k, singularValues M (S.1.orderEmbOfFin S.2 i)
```

**`singularValues_compoundMatrix_rev`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L459).

> Converse of `singularValues_compoundMatrix_eq`: every singular value of the
> compound matrix is a product of singular values of M over some k-subset.

```lean
lemma singularValues_compoundMatrix_rev (M : Matrix d d ℂ) (k : ℕ)
    (j : {S : Finset d // S.card = k}) :
    ∃ (S : {S : Finset d // S.card = k}),
    singularValues (compoundMatrix M k) j =
    ∏ i : Fin k, singularValues M (S.1.orderEmbOfFin S.2 i)
```

**`exists_sorting_equiv`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L470).

> There exists a bijection `σ : Fin (card d) ≃ d` such that
> `singularValues M (σ i) = singularValuesSorted M i` for all `i`.

```lean
lemma exists_sorting_equiv (M : Matrix d d ℂ) :
    ∃ σ : Fin (Fintype.card d) ≃ d,
    ∀ i, singularValues M (σ i) = singularValuesSorted M i
```

**`prod_singularValues_subset_le_sorted_prod`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L524).

> For any k-subset S of d, the product of singular values over S is ≤ the
> product of the top k sorted singular values.

```lean
lemma prod_singularValues_subset_le_sorted_prod (M : Matrix d d ℂ) (k : ℕ)
    (hk : k ≤ Fintype.card d) (S : {S : Finset d // S.card = k}) :
    ∏ i : Fin k, singularValues M (S.1.orderEmbOfFin S.2 i) ≤
    ∏ i : Fin k, singularValuesSorted M ⟨i.val, by omega⟩
```

**`exists_subset_prod_eq_sorted_prod`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L543).

```lean
lemma exists_subset_prod_eq_sorted_prod (M : Matrix d d ℂ) (k : ℕ)
    (hk : k ≤ Fintype.card d) :
    ∃ S : {S : Finset d // S.card = k},
    ∏ i : Fin k, singularValues M (S.1.orderEmbOfFin S.2 i) =
    ∏ i : Fin k, singularValuesSorted M ⟨i.val, by omega⟩
```

**`prod_singularValuesSorted_eq_compoundSV`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L629).

```lean
lemma prod_singularValuesSorted_eq_compoundSV (M : Matrix d d ℂ) (k : ℕ)
    (hk : k ≤ Fintype.card d) :
    ∏ i : Fin k, singularValuesSorted M ⟨i.val, by omega⟩ =
    singularValuesSorted (compoundMatrix M k) ⟨0, by
      have : Fintype.card {S : Finset d // S.card = k} = (Fintype.card d).choose k := by
        simp [Fintype.card_subtype]
      rw [this]; exact Nat.choose_pos hk⟩
```

**`IsHermitian.inner_le_sup_eigenvalue_mul_inner`**, a lemma, [line 654](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L654).

> The **Rayleigh quotient bound**:
> For a Hermitian matrix H with eigenvalues λ, we have
> `v† H v ≤ (max λ) · v† v` for all v.

```lean
lemma IsHermitian.inner_le_sup_eigenvalue_mul_inner
    {e : Type*} [Fintype e] [DecidableEq e]
    (H : Matrix e e ℂ) (hH : H.IsHermitian)
    (he : 0 < Fintype.card e)
    (v : e → ℂ) :
    Complex.re (star v ⬝ᵥ H.mulVec v) ≤
    Finset.sup' Finset.univ
      (Finset.univ_nonempty_iff.mpr (Fintype.card_pos_iff.mp he))
      hH.eigenvalues * Complex.re (star v ⬝ᵥ v)
```

**`eigenvalue_le_singularValuesSorted_sq`**, a lemma, [line 702](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L702).

```lean
lemma eigenvalue_le_singularValuesSorted_sq {e : Type*} [Fintype e] [DecidableEq e]
    (A : Matrix e e ℂ) (h : 0 < Fintype.card e) (i : e) :
  (isHermitian_mul_conjTranspose_self A.conjTranspose).eigenvalues i ≤
    (singularValuesSorted A ⟨0, h⟩) ^ 2
```

**`quadratic_form_le_singularValuesSorted_sq`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L719).

> The quadratic form of `A† A` is bounded by (max singular value)² * ‖v‖².

```lean
lemma quadratic_form_le_singularValuesSorted_sq {e : Type*} [Fintype e] [DecidableEq e]
    (A : Matrix e e ℂ) (h : 0 < Fintype.card e) (v : e → ℂ) :
  Complex.re (star v ⬝ᵥ (A.conjTranspose * A).mulVec v) ≤
    (singularValuesSorted A ⟨0, h⟩) ^ 2 * Complex.re (star v ⬝ᵥ v)
```

**`singularValuesSorted_mul_le`**, a lemma, [line 735](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L735).

> The largest singular value of a matrix product is at most the product of the
> largest singular values: `σ₁(M * N) ≤ σ₁(M) * σ₁(N)`.
> This is operator-norm submultiplicativity.

```lean
lemma singularValuesSorted_mul_le {e : Type*} [Fintype e] [DecidableEq e]
    (M N : Matrix e e ℂ) (h : 0 < Fintype.card e) :
    singularValuesSorted (M * N) ⟨0, h⟩ ≤
    singularValuesSorted M ⟨0, h⟩ * singularValuesSorted N ⟨0, h⟩
```

**`horn_weak_log_majorization`**, a lemma, [line 776](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L776).

> Horn's inequality (weak log-majorization of singular values):
> For all `k`, `∏_{i<k} σ↓ᵢ(AB) ≤ ∏_{i<k} σ↓ᵢ(A) · σ↓ᵢ(B)`.
> This follows from submultiplicativity of the operator norm applied to
> exterior powers of the matrices.

```lean
lemma horn_weak_log_majorization (A B : Matrix d d ℂ) (k : ℕ)
    (hk : k ≤ Fintype.card d) :
    ∏ i : Fin k, singularValuesSorted (A * B) ⟨i.val, by omega⟩ ≤
    ∏ i : Fin k, (singularValuesSorted A ⟨i.val, by omega⟩ *
                   singularValuesSorted B ⟨i.val, by omega⟩)
```

### Weak log-majorization implies sum of powers inequality

**`rpow_antitone_of_nonneg_antitone`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L804).

> Raising nonneg antitone sequences to a positive power preserves antitonicity.

```lean
lemma rpow_antitone_of_nonneg_antitone {n : ℕ}
    {f : Fin n → ℝ} (hf : Antitone f) (hf_nn : ∀ i, 0 ≤ f i)
    {r : ℝ} (hr : 0 < r) :
    Antitone (fun i => f i ^ r)
```

**`rpow_preserves_weak_log_maj`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L811).

> Weak log-majorization is preserved under positive powers.

```lean
lemma rpow_preserves_weak_log_maj {n : ℕ}
    {x y : Fin n → ℝ}
    (hx_nn : ∀ i, 0 ≤ x i) (hy_nn : ∀ i, 0 ≤ y i)
    (h_log_maj : ∀ (k : ℕ) (_ : k ≤ n),
      ∏ i : Fin k, x ⟨i.val, by omega⟩ ≤
      ∏ i : Fin k, y ⟨i.val, by omega⟩)
    {r : ℝ} (hr : 0 < r) :
    ∀ (k : ℕ) (_ : k ≤ n),
      ∏ i : Fin k, (fun j => x j ^ r) ⟨i.val, by omega⟩ ≤
      ∏ i : Fin k, (fun j => y j ^ r) ⟨i.val, by omega⟩
```

**`sum_mul_log_nonneg_of_weak_log_maj`**, a lemma, [line 849](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L849).

```lean
lemma sum_mul_log_nonneg_of_weak_log_maj {n : ℕ}
    {x y : Fin n → ℝ}
    (hx_pos : ∀ i, 0 < x i) (hy_pos : ∀ i, 0 < y i)
    (hx_anti : Antitone x)
    (h_log_maj : ∀ (k : ℕ) (_ : k ≤ n),
      ∏ i : Fin k, x ⟨i.val, by omega⟩ ≤
      ∏ i : Fin k, y ⟨i.val, by omega⟩) :
    0 ≤ ∑ i, x i * Real.log (y i / x i)
```

**`sub_ge_mul_log_div`**, a lemma, [line 909](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L909).

```lean
lemma sub_ge_mul_log_div {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    b - a ≥ a * Real.log (b / a)
```

**`weak_log_maj_sum_le`**, a lemma, [line 914](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L914).

```lean
lemma weak_log_maj_sum_le {n : ℕ}
    {x y : Fin n → ℝ}
    (hx_nn : ∀ i, 0 ≤ x i) (hy_nn : ∀ i, 0 ≤ y i)
    (hx_anti : Antitone x) (hy_anti : Antitone y)
    (h_log_maj : ∀ (k : ℕ) (_ : k ≤ n),
      ∏ i : Fin k, x ⟨i.val, by omega⟩ ≤
      ∏ i : Fin k, y ⟨i.val, by omega⟩) :
    ∑ i, x i ≤ ∑ i, y i
```

**`weak_log_maj_sum_rpow_le`**, a lemma, [line 944](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L944).

> Weak log-majorization of nonneg antitone sequences implies the sum of
> powers inequality.

```lean
lemma weak_log_maj_sum_rpow_le {n : ℕ}
    {x y : Fin n → ℝ}
    (hx_nn : ∀ i, 0 ≤ x i) (hy_nn : ∀ i, 0 ≤ y i)
    (hx_anti : Antitone x) (hy_anti : Antitone y)
    (h_log_maj : ∀ (k : ℕ) (_ : k ≤ n),
      ∏ i : Fin k, x ⟨i.val, by omega⟩ ≤
      ∏ i : Fin k, y ⟨i.val, by omega⟩)
    {r : ℝ} (hr : 0 < r) :
    ∑ i, x i ^ r ≤ ∑ i, y i ^ r
```

## Key singular value inequality for products

**`sum_rpow_singularValues_mul_le`**, a lemma, [line 962](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L962).

```lean
lemma sum_rpow_singularValues_mul_le (A B : Matrix d d ℂ) {r : ℝ} (hr : 0 < r) :
    ∑ i : Fin (Fintype.card d), singularValuesSorted (A * B) i ^ r ≤
    ∑ i : Fin (Fintype.card d),
      (singularValuesSorted A i ^ r * singularValuesSorted B i ^ r)
```

## Hölder inequality for singular values

**`holder_step_for_singularValues`**, a lemma, [line 995](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean#L995).

> The finite-sum Hölder inequality applied to sequences of r-th powers of
> sorted singular values.
>
> With conjugate exponents `p' = p/r > 1` and `q' = q/r > 1` (which satisfy
> `1/p' + 1/q' = 1` when `1/r = 1/p + 1/q`), this gives:
>   `∑ σ↓ᵢ(A)^r · σ↓ᵢ(B)^r ≤ (∑ σ↓ᵢ(A)^p)^{r/p} · (∑ σ↓ᵢ(B)^q)^{r/q}`
>
> Note: The sums on the RHS don't depend on the ordering, so we can replace
> sorted singular values with unsorted ones.

```lean
lemma holder_step_for_singularValues (A B : Matrix d d ℂ)
    {r p q : ℝ} (hr : 0 < r) (hp : 0 < p) (hq : 0 < q)
    (hpqr : 1 / r = 1 / p + 1 / q) :
    (∑ i : Fin (Fintype.card d),
      (singularValuesSorted A i ^ r * singularValuesSorted B i ^ r)) ≤
    (∑ i : Fin (Fintype.card d), singularValuesSorted A i ^ p) ^ (r / p) *
    (∑ i : Fin (Fintype.card d), singularValuesSorted B i ^ q) ^ (r / q)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [QuantumInfo.ForMathlib.Matrix](matrix.md)

## Sources

- [QuantumInfo/ForMathlib/Majorization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Majorization.lean)
