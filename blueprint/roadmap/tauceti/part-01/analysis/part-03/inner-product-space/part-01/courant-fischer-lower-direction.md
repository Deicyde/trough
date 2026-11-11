---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner, LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue, LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue_of_le_finrank
statement: formalized
proof: formalized
---

# Courant–Fischer, lower direction

There is a subspace `V` of dimension
`k + 1` on which every unit vector `x` satisfies `λₖ(T) ≤ re ⟪T x, x⟫`, where
`λ` is the decreasing enumeration `LinearMap.IsSymmetric.eigenvalues` of the
eigenvalues of the symmetric operator `T`.

Witness: `V = span {bᵢ : i ≤ k}`; on it the quadratic form is bounded below by
`λₖ` since all involved eigenvalues are `≥ λₖ`.

```lean
LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ}
  [FiniteDimensional 𝕜 E] {T : E →ₗ[𝕜] E} (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  (k : Fin n) :
  ∃ V,
    Module.finrank 𝕜 ↥V = ↑k + 1 ∧
      ∀ x ∈ V, ‖x‖ = 1 → hT.eigenvalues hn k ≤ RCLike.re (inner 𝕜 (T x) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner).

## Other forms

**Courant–Fischer, upper direction.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue).

```lean
LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ}
  [FiniteDimensional 𝕜 E] {T : E →ₗ[𝕜] E} (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  (k : Fin n) (V : Submodule 𝕜 E) (hV : Module.finrank 𝕜 ↥V = ↑k + 1) :
  ∃ x ∈ V, ‖x‖ = 1 ∧ RCLike.re (inner 𝕜 (T x) x) ≤ hT.eigenvalues hn k
```

**Courant–Fischer, upper direction, for large subspaces.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue_of_le_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue_of_le_finrank).

```lean
LinearMap.IsSymmetric.exists_unit_vector_re_inner_le_eigenvalue_of_le_finrank.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {n : ℕ}
  [FiniteDimensional 𝕜 E] {T : E →ₗ[𝕜] E} (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  (k : Fin n) (V : Submodule 𝕜 E) (hV : ↑k + 1 ≤ Module.finrank 𝕜 ↥V) :
  ∃ x ∈ V, ‖x‖ = 1 ∧ RCLike.re (inner 𝕜 (T x) x) ≤ hT.eigenvalues hn k
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/CourantFischer.html#LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner)
- [Source of `LinearMap.IsSymmetric.exists_submodule_forall_unit_eigenvalue_le_re_inner` in TauCeti/Analysis/InnerProductSpace/CourantFischer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/CourantFischer.lean#L228)
