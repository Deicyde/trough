---
declaration: module
origin: cited
lean: LinearMap.IsSymmetric.re_inner_apply_self_eq_sum_of_eigenbasis, LinearMap.IsSymmetric.le_re_inner_of_eigenbasis, LinearMap.IsSymmetric.re_inner_le_of_eigenbasis, LinearMap.IsSymmetric.re_inner_apply_self_eq_sum_eigenvalues_mul_sq, LinearMap.IsSymmetric.re_inner_apply_self_le_of_mem_spanIndices, LinearMap.IsSymmetric.le_re_inner_apply_self_of_mem_spanIndices, LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue, LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner
statement: formalized
proof: formalized
---

# Courant–Fischer min–max theorem and Weyl's inequality

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.InnerProductSpace.CourantFischer`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean): 26 declarations, 26 with a docstring; 2 private, not shown.

> For a finite-dimensional inner-product space over `ℝ` or `ℂ`, the min–max theorem characterizes the
> decreasingly sorted eigenvalues of a symmetric endomorphism through its Rayleigh form.

## i. Overview

> For a finite-dimensional inner-product space over `ℝ` or `ℂ`, the min–max theorem
> characterizes the decreasingly sorted eigenvalues of a symmetric endomorphism
> through its Rayleigh form.  The same argument gives monotonicity under quadratic-
> form domination and Weyl's perturbation bound.

## ii. Key results

> * `LinearMap.IsSymmetric.re_inner_apply_self_eq_sum_eigenvalues_mul_sq`:
>   diagonal expansion of the Rayleigh form in an eigenbasis.
> * `LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue` and
>   `LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner`:
>   the two min–max directions.
> * `LinearMap.IsSymmetric.eigenvalues_eq_iSup_iInf_re_inner`:
>   the Courant–Fischer equality.
> * `LinearMap.IsSymmetric.eigenvalue_mono`:
>   monotonicity of sorted eigenvalues under quadratic-form order.
> * `LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le` and
>   `LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm`:
>   Weyl's perturbation inequality.
> * `LinearMap.IsSymmetric.eigenvalue_compression_le` and
>   `LinearMap.IsSymmetric.eigenvalue_le_eigenvalue_compression`:
>   Cauchy interlacing for an operator on a subspace with the same quadratic form, such as the
>   compression `LinearMap.IsSymmetric.compression`.
> * `LinearMap.IsSymmetric.eigenvalue_ascending_le_ritz`: the Hylleraas–Undheim–MacDonald
>   bound, the `k`-th lowest Ritz value bounds the `k`-th lowest eigenvalue from above.

## iv. References

> * R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed.,
>   Theorems 4.2.6 and 4.3.1.
> * R. Bhatia, *Matrix Analysis*, Corollary III.2.6.
> * E. A. Hylleraas and B. Undheim, *Numerische Berechnung der 2S-Terme von Ortho- und
>   Par-Helium*, Z. Phys. 65 (1930) 759–772, pp. 763–764. [ref: hylleraas\_undheim\_1930]
> * J. K. L. MacDonald, *Successive Approximations by the Rayleigh-Ritz Variation Method*,
>   Phys. Rev. 43 (1933) 830–833, rule (1) and Corollary 1.1. [ref: macdonald\_1933]
>
> Provenance: Ported and adapted from
> [`ForTauCeti/Analysis/InnerProductSpace/CourantFischer.lean`](https://github.com/AIQ-Kitware/aiq-dkps-formalization/blob/main/ForTauCeti/Analysis/InnerProductSpace/CourantFischer.lean)
> in Kitware's DKPS formalization (Apache-2.0).  The original proof development
> was by Claude Fable 5, with polishing by Claude Opus 4.8 and oversight by
> Jon Crall.

## A. Development

**`LinearMap.IsSymmetric.re_inner_apply_self_eq_sum_of_eigenbasis`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L101).

> Diagonalization of the quadratic form in any orthonormal eigenbasis: if
> `S (w i) = μ i • w i` for all `i`, then
> `re ⟪S x, x⟫ = ∑ i, μ i * ‖w.repr x i‖ ^ 2`.

```lean
lemma re_inner_apply_self_eq_sum_of_eigenbasis
    (hS : S.IsSymmetric) (w : OrthonormalBasis (Fin n) 𝕜 E) {μ : Fin n → ℝ}
    (hw : ∀ i, S (w i) = (μ i : 𝕜) • w i) (x : E) :
    RCLike.re ⟪S x, x⟫_𝕜 = ∑ i : Fin n, μ i * ‖w.repr x i‖ ^ 2
```

**`LinearMap.IsSymmetric.le_re_inner_of_eigenbasis`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L121).

> On the span of the eigenvectors selected by `s`, the quadratic form is
> bounded below by any lower bound on the selected values (general-eigenbasis
> version of `le_re_inner_apply_self_of_mem_spanIndices`).

```lean
lemma le_re_inner_of_eigenbasis
    (hS : S.IsSymmetric) (w : OrthonormalBasis (Fin n) 𝕜 E) {μ : Fin n → ℝ}
    (hw : ∀ i, S (w i) = (μ i : 𝕜) • w i) {s : Set (Fin n)} {c : ℝ}
    (hc : ∀ i ∈ s, c ≤ μ i) {x : E} (hx : x ∈ w.spanIndices s) :
    c * ‖x‖ ^ 2 ≤ RCLike.re ⟪S x, x⟫_𝕜
```

**`LinearMap.IsSymmetric.re_inner_le_of_eigenbasis`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L137).

> Dual of `le_re_inner_of_eigenbasis`.

```lean
lemma re_inner_le_of_eigenbasis
    (hS : S.IsSymmetric) (w : OrthonormalBasis (Fin n) 𝕜 E) {μ : Fin n → ℝ}
    (hw : ∀ i, S (w i) = (μ i : 𝕜) • w i) {s : Set (Fin n)} {c : ℝ}
    (hc : ∀ i ∈ s, μ i ≤ c) {x : E} (hx : x ∈ w.spanIndices s) :
    RCLike.re ⟪S x, x⟫_𝕜 ≤ c * ‖x‖ ^ 2
```

### A.1. The quadratic form in the eigenbasis

**`LinearMap.IsSymmetric.re_inner_apply_self_eq_sum_eigenvalues_mul_sq`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L159).

> The quadratic form `re ⟪T x, x⟫` of a symmetric operator `T` expressed in
> its eigenbasis: it is the eigenvalue-weighted sum of the squared norms of the
> coordinates of `x`.  This is the diagonalization of the quadratic form.  (For
> symmetric `T` the inner product `⟪T x, x⟫` is real, so no information is lost
> by taking the real part.)

```lean
lemma re_inner_apply_self_eq_sum_eigenvalues_mul_sq
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) (x : E) :
    RCLike.re ⟪T x, x⟫_𝕜
      = ∑ i : Fin n, hT.eigenvalues hn i * ‖(hT.eigenvectorBasis hn).repr x i‖ ^ 2
```

**`LinearMap.IsSymmetric.re_inner_apply_self_le_of_mem_spanIndices`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L170).

> On the span of a selected subfamily of the eigenbasis, the quadratic form
> is bounded by any bound on the selected eigenvalues: if
> `x ∈ b.spanIndices s` (so its coordinates vanish off `s`) and every selected
> eigenvalue satisfies `λᵢ ≤ c`, then `re ⟪T x, x⟫ ≤ c ‖x‖²`.

```lean
lemma re_inner_apply_self_le_of_mem_spanIndices
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) {s : Set (Fin n)} {c : ℝ}
    (hc : ∀ i ∈ s, hT.eigenvalues hn i ≤ c)
    {x : E} (hx : x ∈ (hT.eigenvectorBasis hn).spanIndices s) :
    RCLike.re ⟪T x, x⟫_𝕜 ≤ c * ‖x‖ ^ 2
```

**`LinearMap.IsSymmetric.le_re_inner_apply_self_of_mem_spanIndices`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L181).

> Dual of `re_inner_apply_self_le_of_mem_spanIndices`: if
> `x ∈ b.spanIndices s` and every selected eigenvalue satisfies `c ≤ λᵢ`, then
> `c ‖x‖² ≤ re ⟪T x, x⟫`.

```lean
lemma le_re_inner_apply_self_of_mem_spanIndices
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) {s : Set (Fin n)} {c : ℝ}
    (hc : ∀ i ∈ s, c ≤ hT.eigenvalues hn i)
    {x : E} (hx : x ∈ (hT.eigenvectorBasis hn).spanIndices s) :
    c * ‖x‖ ^ 2 ≤ RCLike.re ⟪T x, x⟫_𝕜
```

### A.2. Discrete Courant–Fischer directional bounds

**`LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L195).

> **Courant–Fischer, upper direction.** On any subspace `V` of dimension
> `k + 1` there is a unit vector `x` with `re ⟪T x, x⟫ ≤ λₖ(T)`, where `λ` is the
> decreasing enumeration `LinearMap.IsSymmetric.eigenvalues` of the eigenvalues
> of the symmetric operator `T`.

```lean
lemma exists_unit_vector_re_inner_le_eigenvalue
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) (k : Fin n)
    (V : Submodule 𝕜 E) (hV : finrank 𝕜 V = (k : ℕ) + 1) :
    ∃ x ∈ V, ‖x‖ = 1 ∧ RCLike.re ⟪T x, x⟫_𝕜 ≤ hT.eigenvalues hn k
```

**`LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L233).

> **Courant–Fischer, lower direction.** There is a subspace `V` of dimension
> `k + 1` on which every unit vector `x` satisfies `λₖ(T) ≤ re ⟪T x, x⟫`, where
> `λ` is the decreasing enumeration `LinearMap.IsSymmetric.eigenvalues` of the
> eigenvalues of the symmetric operator `T`.
>
> Witness: `V = span {bᵢ : i ≤ k}`; on it the quadratic form is bounded below by
> `λₖ` since all involved eigenvalues are `≥ λₖ`.

```lean
lemma exists_submodule_forall_unit_eigenvalue_le_re_inner
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) (k : Fin n) :
    ∃ V : Submodule 𝕜 E, finrank 𝕜 V = (k : ℕ) + 1 ∧
      ∀ x ∈ V, ‖x‖ = 1 → hT.eigenvalues hn k ≤ RCLike.re ⟪T x, x⟫_𝕜
```

### A.3. The Courant–Fischer min-max equality

**`LinearMap.IsSymmetric.eigenvalues_eq_iSup_iInf_re_inner`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L258).

> **Courant–Fischer min-max equality.** The `k`-th (decreasingly sorted)
> eigenvalue of a symmetric operator on a finite-dimensional inner product space
> over `𝕜 = ℝ, ℂ` is the supremum, over the subspaces `V` of dimension `k + 1`,
> of the infimum of the Rayleigh quotient `re ⟪T x, x⟫` over the unit vectors of
> `V`.
>
> Horn & Johnson, *Matrix Analysis* 2nd ed., Theorem 4.2.6.

```lean
lemma eigenvalues_eq_iSup_iInf_re_inner
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) (k : Fin n) :
    hT.eigenvalues hn k =
      ⨆ V : {V : Submodule 𝕜 E // finrank 𝕜 V = (k : ℕ) + 1},
        ⨅ x : {x : E // x ∈ (V : Submodule 𝕜 E) ∧ ‖x‖ = 1},
          RCLike.re ⟪T (x : E), (x : E)⟫_𝕜
```

### A.4. Sorted-eigenvalue uniqueness and Loewner monotonicity

> Courant–Fischer consequences needed by the Ky Fan / unitarily-invariant-norm
> development: an antitone list diagonalizing a symmetric operator in *some*
> orthonormal basis is *the* sorted eigenvalue list, and the sorted eigenvalues
> are monotone in the quadratic form (Loewner order).

**`LinearMap.IsSymmetric.eigenvalues_eq_of_eigenbasis`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L332).

> **Sorted-eigenvalue uniqueness.**  If an orthonormal basis `w`
> diagonalizes the symmetric operator `S` with an *antitone* value list `μ`,
> then `μ` is the sorted eigenvalue list: `hS.eigenvalues hn = μ`.
> (Courant–Fischer: both lists satisfy the same minimax characterization.)

```lean
lemma eigenvalues_eq_of_eigenbasis
    (hS : S.IsSymmetric) (hn : finrank 𝕜 E = n) (w : OrthonormalBasis (Fin n) 𝕜 E)
    {μ : Fin n → ℝ} (hμ : Antitone μ) (hw : ∀ i, S (w i) = (μ i : 𝕜) • w i) :
    hS.eigenvalues hn = μ
```

**`LinearMap.IsSymmetric.eigenvalue_mono`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L370).

> **Loewner monotonicity of the sorted eigenvalues.**  If the quadratic form
> of `T` is dominated by that of `S`, then so is every sorted eigenvalue.

```lean
lemma eigenvalue_mono
    (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : finrank 𝕜 E = n)
    (h : ∀ x, RCLike.re ⟪T x, x⟫_𝕜 ≤ RCLike.re ⟪S x, x⟫_𝕜) (k : Fin n) :
    hT.eigenvalues hn k ≤ hS.eigenvalues hn k
```

**`LinearMap.IsSymmetric.map_mem_spanIndices`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L384).

> The span of a selected subfamily of the eigenbasis of a symmetric operator
> is invariant under the operator.

```lean
lemma map_mem_spanIndices (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n)
    (s : Set (Fin n)) {x : E}
    (hx : x ∈ (hT.eigenvectorBasis hn).spanIndices s) :
    T x ∈ (hT.eigenvectorBasis hn).spanIndices s
```

### A.5. Weyl's inequality

**`LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L447).

> **Weyl's inequality** for symmetric operators on a finite-dimensional inner
> product space over `𝕜 = ℝ, ℂ`: the `k`-th (decreasingly sorted) eigenvalues of
> `T` and `S` differ by at most the operator norm of `T − S`.
>
> At `LinearMap` level there is no operator norm, so the bound is supplied as the
> pointwise hypothesis `∀ x, ‖(T − S) x‖ ≤ ε * ‖x‖`; see
> `LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm` for the continuous-linear-map
> operator-norm form.
>
> Horn & Johnson, *Matrix Analysis* 2nd ed., Theorem 4.3.1; Bhatia,
> *Matrix Analysis*, Corollary III.2.6.

```lean
lemma abs_eigenvalue_sub_eigenvalue_le
    (hT : T.IsSymmetric) (hS : S.IsSymmetric) (hn : finrank 𝕜 E = n)
    {ε : ℝ} (hε : ∀ x : E, ‖(T - S) x‖ ≤ ε * ‖x‖) (k : Fin n) :
    |hT.eigenvalues hn k - hS.eigenvalues hn k| ≤ ε
```

**`LinearMap.IsSymmetric.abs_eigenvalue_sub_eigenvalue_le_norm`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L474).

> **Weyl's inequality**, operator-norm form, for symmetric (equivalently,
> self-adjoint) continuous linear maps on a finite-dimensional inner product
> space: the `k`-th sorted eigenvalues of `T` and `S` differ by at most
> `‖T − S‖`.  The symmetry hypotheses are stated on the underlying linear maps
> so that the signature does not require the adjoint star structure (whose
> instance needs `CompleteSpace E`, which `FiniteDimensional` deliberately does
> not register as an instance).
>
> The bound is expressed directly in the norm of a continuous linear map.

```lean
lemma abs_eigenvalue_sub_eigenvalue_le_norm
    {T S : E →L[𝕜] E}
    (hT : LinearMap.IsSymmetric (T : E →ₗ[𝕜] E))
    (hS : LinearMap.IsSymmetric (S : E →ₗ[𝕜] E))
    (hn : finrank 𝕜 E = n) (k : Fin n) :
    |hT.eigenvalues hn k - hS.eigenvalues hn k| ≤ ‖T - S‖
```

**`LinearMap.IsSymmetric.abs_eigenvalues_sub_le_opNorm`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L486).

> Weyl's inequality for linear maps, using the operator norm of the
> corresponding continuous linear map.  Unlike the preceding theorem, the symmetry
> hypotheses and eigenvalue enumeration are directly attached to `LinearMap`s.

```lean
lemma abs_eigenvalues_sub_le_opNorm
    {T S : E →ₗ[𝕜] E} (hT : T.IsSymmetric) (hS : S.IsSymmetric)
    (hn : finrank 𝕜 E = n) (k : Fin n) :
    |hT.eigenvalues hn k - hS.eigenvalues hn k|
      ≤ ‖LinearMap.toContinuousLinearMap (T - S)‖
```

**`LinearMap.IsSymmetric.eigenvalues_congr`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L497).

> Sorted eigenvalues are congruent along an operator equality (the eigenvalue
> enumeration depends only on the operator, not on the symmetry proof).

```lean
lemma eigenvalues_congr {S₁ S₂ : E →ₗ[𝕜] E} (h : S₁ = S₂)
    (hS₁ : S₁.IsSymmetric) (hS₂ : S₂.IsSymmetric) (hn : finrank 𝕜 E = n) :
    hS₁.eigenvalues hn = hS₂.eigenvalues hn
```

**`LinearMap.IsSymmetric.eigenvalues_cast`**, a lemma, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L510).

> The eigenvalue enumeration does not depend on which witness of the dimension indexes
> it: two witnesses `finrank 𝕜 E = m` and `finrank 𝕜 E = n` enumerate the same eigenvalues,
> read across the induced `Fin m ≃ Fin n`.
>
> Both spellings occur in practice.  A matrix over `Fin n` has
> `Matrix.IsHermitian.eigenvalues₀` indexed by `Fin (Fintype.card (Fin n))`, while the
> operator theory it is transported to indexes by `Fin n`; `Fintype.card (Fin n) = n` is a
> theorem and not definitional, so the two index types are genuinely different.

```lean
lemma eigenvalues_cast {T : E →ₗ[𝕜] E} (hT : T.IsSymmetric) {m : ℕ}
    (hm : finrank 𝕜 E = m) (hn : finrank 𝕜 E = n) (hmn : m = n) (i : Fin m) :
    hT.eigenvalues hm i = hT.eigenvalues hn (Fin.cast hmn i)
```

### A.6. Courant–Fischer on subspaces of larger dimension

**`LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue_of_le`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L519).

> **Courant–Fischer, upper direction, for large subspaces.** On any subspace `W` of dimension
> at least `k + 1` there is a unit vector `x` with `re ⟪T x, x⟫ ≤ λₖ(T)`.

```lean
lemma exists_unit_vector_re_inner_le_eigenvalue_of_le
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n) (k : Fin n)
    (W : Submodule 𝕜 E) (hW : (k : ℕ) + 1 ≤ finrank 𝕜 W) :
    ∃ x ∈ W, ‖x‖ = 1 ∧ RCLike.re ⟪T x, x⟫_𝕜 ≤ hT.eigenvalues hn k
```

### A.7. Cauchy interlacing and Rayleigh–Ritz bounds

**`LinearMap.IsSymmetric.eigenvalue_compression_le`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L552).

> **Upper Cauchy interlacing.** If the quadratic form of the symmetric operator `A` on `V`
> agrees with that of `T`, then `μₖ(A) ≤ λₖ(T)` for every `k < m`.

```lean
lemma eigenvalue_compression_le
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n)
    (hA : A.IsSymmetric) (hm : finrank 𝕜 V = m)
    (hcomp : ∀ y : V, RCLike.re ⟪A y, y⟫_𝕜 = RCLike.re ⟪T y, y⟫_𝕜)
    (k : Fin m) (hk : (k : ℕ) < n) :
    hA.eigenvalues hm k ≤ hT.eigenvalues hn ⟨k, hk⟩
```

**`LinearMap.IsSymmetric.eigenvalue_le_eigenvalue_compression`**, a lemma, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L570).

> **Lower Cauchy interlacing.** If the quadratic form of the symmetric operator `A` on `V`
> agrees with that of `T`, then `λ_{k + (n - m)}(T) ≤ μₖ(A)` for every `k < m`.

```lean
lemma eigenvalue_le_eigenvalue_compression
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n)
    (hA : A.IsSymmetric) (hm : finrank 𝕜 V = m)
    (hcomp : ∀ y : V, RCLike.re ⟪A y, y⟫_𝕜 = RCLike.re ⟪T y, y⟫_𝕜)
    (k : Fin m) (hmn : m ≤ n) :
    hT.eigenvalues hn ⟨k + (n - m), by omega⟩ ≤ hA.eigenvalues hm k
```

**`LinearMap.IsSymmetric.eigenvalue_ascending_le_ritz`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L595).

> **Hylleraas–Undheim–MacDonald.** In ascending order, the `k`-th lowest Ritz value is an upper
> bound for the `k`-th lowest exact eigenvalue: `λ↑ₖ(T) ≤ μ↑ₖ(S)` for every `k < m`.

```lean
lemma eigenvalue_ascending_le_ritz
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n)
    (hA : A.IsSymmetric) (hm : finrank 𝕜 V = m)
    (hcomp : ∀ y : V, RCLike.re ⟪A y, y⟫_𝕜 = RCLike.re ⟪T y, y⟫_𝕜)
    (hmn : m ≤ n) (k : ℕ) (hk : k < m) :
    hT.eigenvalues hn ⟨n - 1 - k, by omega⟩ ≤ hA.eigenvalues hm ⟨m - 1 - k, by omega⟩
```

**`LinearMap.IsSymmetric.eigenvalue_min_le_ritz_min`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L609).

> **Variational ground-state bound.** The lowest Ritz value bounds the lowest exact eigenvalue
> from above.

```lean
lemma eigenvalue_min_le_ritz_min
    (hT : T.IsSymmetric) (hn : finrank 𝕜 E = n)
    (hA : A.IsSymmetric) (hm : finrank 𝕜 V = m)
    (hcomp : ∀ y : V, RCLike.re ⟪A y, y⟫_𝕜 = RCLike.re ⟪T y, y⟫_𝕜)
    (hmn : m ≤ n) (hm0 : 0 < m) :
    hT.eigenvalues hn ⟨n - 1, by omega⟩ ≤ hA.eigenvalues hm ⟨m - 1, by omega⟩
```

### A.8. The orthogonal compression

**`LinearMap.IsSymmetric.compression`**, a def, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L622).

> The compression `P_V ∘ T ∘ ι_V` of `T` to the subspace `V` (the Ritz operator).

```lean
noncomputable def compression (_hT : T.IsSymmetric) (V : Submodule 𝕜 E) : V →ₗ[𝕜] V
```

**`LinearMap.IsSymmetric.inner_compression_left`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L626).

> The compression has the inner products of `T` against vectors of `V`.

```lean
lemma inner_compression_left (hT : T.IsSymmetric) (V : Submodule 𝕜 E) (y z : V) :
    ⟪hT.compression V y, z⟫_𝕜 = ⟪T y, z⟫_𝕜
```

**`LinearMap.IsSymmetric.compression_isSymmetric`**, a lemma, [line 631](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L631).

> The compression of a symmetric operator is symmetric.

```lean
lemma compression_isSymmetric (hT : T.IsSymmetric) (V : Submodule 𝕜 E) :
    (hT.compression V).IsSymmetric
```

**`LinearMap.IsSymmetric.re_inner_compression`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L639).

> The compression has the quadratic form of `T` on `V`, as required by the interlacing
> lemmas.

```lean
lemma re_inner_compression (hT : T.IsSymmetric) (V : Submodule 𝕜 E) (y : V) :
    RCLike.re ⟪hT.compression V y, y⟫_𝕜 = RCLike.re ⟪T y, y⟫_𝕜
```

## Depends on

- [Spans of orthonormal subfamilies](analysis-innerproductspace-basisspan.md)

## Proof depends on

- [Intersections of submodules by dimension](../part-02/linearalgebra-dimension-submodule.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean)
