---
declaration: module
origin: cited
lean: lorentzAlgebra, lorentzAlgebra.transpose_eta, lorentzAlgebra.mem_of_transpose_eta_eq_eta_mul_self, lorentzAlgebra.mem_iff, lorentzAlgebra.mem_iff', lorentzAlgebra.diag_comp, lorentzAlgebra.time_comps, lorentzAlgebra.space_comps
statement: formalized
proof: formalized
---

# The Lorentz Algebra

The module `Physlib.Relativity.LorentzAlgebra.Basic`, [Physlib/Relativity/LorentzAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean): 8 declarations, 1 with a docstring.

> We define
>
> - Define `lorentzAlgebra` via `LieAlgebra.Orthogonal.so'` as a subalgebra of
>   `Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ`.
> - In `mem_iff` prove that a matrix is in the Lorentz algebra if and only if it satisfies the
>   condition `Aᵀ * η = - η * A`.

**`lorentzAlgebra`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L29).

> The Lorentz algebra as a subalgebra of `Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ`.

```lean
def lorentzAlgebra : LieSubalgebra ℝ (Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ)
```

**`lorentzAlgebra.transpose_eta`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L35).

```lean
lemma transpose_eta (A : lorentzAlgebra) : A.1ᵀ * η = - η * A.1
```

**`lorentzAlgebra.mem_of_transpose_eta_eq_eta_mul_self`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L40).

```lean
lemma mem_of_transpose_eta_eq_eta_mul_self {A : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ}
    (h : Aᵀ * η = - η * A) : A ∈ lorentzAlgebra
```

**`lorentzAlgebra.mem_iff`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L47).

```lean
lemma mem_iff {A : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ} :
    A ∈ lorentzAlgebra ↔ Aᵀ * η = - η * A
```

**`lorentzAlgebra.mem_iff'`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L51).

```lean
lemma mem_iff' (A : Matrix (Fin 1 ⊕ Fin 3) (Fin 1 ⊕ Fin 3) ℝ) :
    A ∈ lorentzAlgebra ↔ A = - η * Aᵀ * η
```

**`lorentzAlgebra.diag_comp`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L61).

```lean
lemma diag_comp (Λ : lorentzAlgebra) (μ : Fin 1 ⊕ Fin 3) : Λ.1 μ μ = 0
```

**`lorentzAlgebra.time_comps`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L69).

```lean
lemma time_comps (Λ : lorentzAlgebra) (i : Fin 3) :
    Λ.1 (Sum.inr i) (Sum.inl 0) = Λ.1 (Sum.inl 0) (Sum.inr i)
```

**`lorentzAlgebra.space_comps`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean#L75).

```lean
lemma space_comps (Λ : lorentzAlgebra) (i j : Fin 3) :
    Λ.1 (Sum.inr i) (Sum.inr j) = - Λ.1 (Sum.inr j) (Sum.inr i)
```

## Depends on

- [The Minkowski matrix](../minkowskimatrix.md)

## Sources

- [Physlib/Relativity/LorentzAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzAlgebra/Basic.lean)
