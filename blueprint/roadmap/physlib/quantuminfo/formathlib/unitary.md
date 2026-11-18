---
declaration: module
origin: cited
lean: LinearMap.IsSymmetric.conj_unitary_IsSymmetric, LinearMap.unitary_star_apply_eq, LinearMap.unitary_apply_star_eq, LinearMap.conj_unitary_eigenspace_equiv, LinearMap.IsSymmetric.conj_unitary_eigenvalue_equiv
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Unitary

The module `QuantumInfo.ForMathlib.Unitary`, [QuantumInfo/ForMathlib/Unitary.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean): 5 declarations, 3 with a docstring, 1 listed as significant.

**`LinearMap.unitary_star_apply_eq`**, a lemma, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean#L25).

```lean
lemma unitary_star_apply_eq (U : unitary (E →ₗ[𝕜] E)) (v : E) :
    (star U.val) (U.val v) = v
```

**`LinearMap.unitary_apply_star_eq`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean#L30).

```lean
lemma unitary_apply_star_eq (U : unitary (E →ₗ[𝕜] E)) (v : E) :
    U.val ((star U.val) v) = v
```

**`LinearMap.conj_unitary_eigenspace_equiv`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean#L36).

> Conjugating a linear map by a unitary operator gives a map whose μ-eigenspace is
> isomorphic (same dimension) as those of the original linear map.

```lean
noncomputable def conj_unitary_eigenspace_equiv (T : E →ₗ[𝕜] E) (U : unitary (E →ₗ[𝕜] E)) (μ : 𝕜) :
    eigenspace T μ ≃ₗ[𝕜] eigenspace (U.val * T * star (U.val)) μ
```

**`LinearMap.IsSymmetric.conj_unitary_IsSymmetric`**, a theorem, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean#L62). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A symmetric operator conjugated by a unitary is symmetric.

```lean
theorem conj_unitary_IsSymmetric (U : unitary (E →ₗ[𝕜] E)) (hT : T.IsSymmetric) :
    (U.val * T * star U.val).IsSymmetric
```

**`LinearMap.IsSymmetric.conj_unitary_eigenvalue_equiv`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean#L73).

> There is an equivalence between the eigenvalues of a finite dimensional symmetric operator,
> and the eigenvalues of that operator conjugated by a unitary.

```lean
def conj_unitary_eigenvalue_equiv (U : unitary (E →ₗ[𝕜] E)) (hT : T.IsSymmetric) :
    { σ : Equiv.Perm (Fin n) //
      (hT.conj_unitary_IsSymmetric U).eigenvalues hn = hT.eigenvalues hn ∘ σ }
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/Unitary.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Unitary.lean)
