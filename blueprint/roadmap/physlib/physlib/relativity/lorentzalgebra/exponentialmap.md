---
declaration: module
origin: cited
lean: lorentzAlgebra.exp_mem_lorentzGroup, lorentzAlgebra.exp_isProper, lorentzAlgebra.exp_isOrthochronous, lorentzAlgebra.exp_mem_restricted_lorentzGroup, lorentzAlgebra.transpose_eq_neg_eta_conj, lorentzAlgebra.exp_transpose_of_mem_algebra, lorentzAlgebra.trace_eq_sum_diagonal, lorentzAlgebra.trace_of_mem_is_zero
statement: formalized
proof: formalized
---

# Exponential map from the Lorentz algebra to the restricted Lorentz group

The module `Physlib.Relativity.LorentzAlgebra.ExponentialMap`, [Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean): 11 declarations (1 instance with no name), 8 with a docstring, 4 listed as significant.

> In 1+3 Minkowski space with metric η, the Lie algebra `lorentzAlgebra` exponentiates
> onto the proper orthochronous Lorentz group (`LorentzGroup.restricted 3`). We prove:
> * exp\_mem\_lorentzGroup : `NormedSpace.exp ℝ A.1 ∈ LorentzGroup 3` (η-preserving).
> * exp\_transpose\_of\_mem\_algebra : `exp (A.1ᵀ) = η * exp (−A.1) * η`.
> * exp\_isProper : `det (exp A) = 1`.
> * exp\_isOrthochronous : `(exp A)₀₀ ≥ 1`.
> Hence `exp A ∈ LorentzGroup.restricted 3`.

**`lorentzAlgebra.transpose_eq_neg_eta_conj`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L41).

> A key property of a Lorentz algebra element `A` is that its transpose
> is related to its conjugation by the Minkowski metric η.

```lean
lemma transpose_eq_neg_eta_conj (A : lorentzAlgebra) :
    A.1ᵀ = - (η * A.1 * η)
```

**`lorentzAlgebra.exp_transpose_of_mem_algebra`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L55).

> The exponential of the transpose of a Lorentz algebra element.
> This connects `exp(Aᵀ)` to a conjugation of `exp(-A)`.

```lean
lemma exp_transpose_of_mem_algebra (A : lorentzAlgebra) :
    NormedSpace.exp (A.1ᵀ) = η * (NormedSpace.exp (-A.1)) * η
```

**`lorentzAlgebra.exp_mem_lorentzGroup`**, a theorem, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L70). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The exponential of an element of the Lorentz algebra is a member of the Lorentz group.

```lean
theorem exp_mem_lorentzGroup (A : lorentzAlgebra) : NormedSpace.exp A.1 ∈ LorentzGroup 3
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L91).

```lean
instance [UniformSpace 𝕂] : UniformSpace (Matrix m n 𝕂)
```

**`lorentzAlgebra.trace_eq_sum_diagonal`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L94).

> The trace of a matrix equals the sum of its diagonal elements.

```lean
lemma trace_eq_sum_diagonal (A : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ) :
    trace A = ∑ i, A i i
```

**`lorentzAlgebra.trace_of_mem_is_zero`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L98).

> The trace of any element of the Lorentz algebra is zero.

```lean
lemma trace_of_mem_is_zero (A : lorentzAlgebra) : trace A.1 = 0
```

**`lorentzAlgebra.Matrix.trace_reindex`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L108).

```lean
lemma trace_reindex [Semiring R] [Fintype ι] (e : n ≃ ι) (A : Matrix n n R) :
    trace (A.submatrix e.symm e.symm) = trace A
```

**`lorentzAlgebra.Matrix.exp_reindex`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L116).

```lean
lemma exp_reindex {k : Type*}
    [RCLike k] [Fintype ι] [DecidableEq ι] (e : n ≃ ι) (A : Matrix n n k) :
    NormedSpace.exp (A.submatrix e.symm e.symm) = reindex e e (NormedSpace.exp A)
```

**`lorentzAlgebra.exp_isProper`**, a theorem, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L131). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The exponential of an element of the Lorentz algebra is proper (has determinant 1).

```lean
theorem exp_isProper (A : lorentzAlgebra) :
    LorentzGroup.IsProper ⟨NormedSpace.exp A.1, exp_mem_lorentzGroup A⟩
```

**`lorentzAlgebra.exp_isOrthochronous`**, a theorem, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L141). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The exponential of an element of the Lorentz algebra is orthochronous.

```lean
theorem exp_isOrthochronous (A : lorentzAlgebra) :
    LorentzGroup.IsOrthochronous ⟨NormedSpace.exp A.1, exp_mem_lorentzGroup A⟩
```

**`lorentzAlgebra.exp_mem_restricted_lorentzGroup`**, a theorem, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean#L175). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The exponential of an element of the Lorentz algebra is a member of the
> restricted Lorentz group.

```lean
theorem exp_mem_restricted_lorentzGroup (A : lorentzAlgebra) :
    (⟨NormedSpace.exp A.1, exp_mem_lorentzGroup A⟩ : LorentzGroup 3) ∈
    LorentzGroup.restricted 3
```

## Depends on

- [The Lorentz Algebra](basic.md)
- [The Restricted Lorentz Group](../lorentzgroup/restricted-basic.md)

## Proof depends on

- [Lie's Trace Formula](../../mathematics/formathlib/datastructures-matrix-lietrace.md)

## Sources

- [Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/ExponentialMap.lean)
