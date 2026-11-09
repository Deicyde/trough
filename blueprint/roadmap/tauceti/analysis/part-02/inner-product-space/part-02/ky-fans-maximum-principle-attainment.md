---
declaration: theorem
origin: cited
lean: LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum, LinearMap.norm_sum_inner_le_kyFanSum, LinearMap.norm_sum_inner_add_inner_le_kyFanSum, LinearMap.IsPositive.exists_orthonormal_sum_re_inner_eq_kyFanSum
statement: formalized
proof: formalized
---

# Ky Fan's maximum principle, attainment

the first `k` right singular vectors and the
corresponding unit left singular vectors, completed where the singular value vanishes, are
orthonormal families with `∑ᵢ ⟪uᵢ, A vᵢ⟫ = σ₀(A) + ⋯ + σₖ₋₁(A)`.

```lean
LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F] (A : E →ₗ[𝕜] F) {k : ℕ}
  (hkE : k ≤ Module.finrank 𝕜 E) (hkF : k ≤ Module.finrank 𝕜 F) :
  ∃ u v, Orthonormal 𝕜 u ∧ Orthonormal 𝕜 v ∧ ∑ i, inner 𝕜 (u i) (A (v i)) = ↑(A.kyFanSum k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abel's inequality, comparison form](../../../../algebra/other-results/abels-inequality-comparison-form.md)
- [Bessel's inequality for a functional](../part-01/bessels-inequality-for-a-functional.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum).

## Other forms

**Ky Fan's maximum principle, the upper bound.** Formalized in Tau Ceti as [`LinearMap.norm_sum_inner_le_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.norm_sum_inner_le_kyFanSum).

```lean
LinearMap.norm_sum_inner_le_kyFanSum.{u_1, u_2, u_3, u_6} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F] {ι : Type u_6} [Fintype ι]
  (A : E →ₗ[𝕜] F) {u : ι → F} {v : ι → E} (hu : Orthonormal 𝕜 u) (hv : Orthonormal 𝕜 v) :
  ‖∑ i, inner 𝕜 (u i) (A (v i))‖ ≤ A.kyFanSum (Fintype.card ι)
```

**Ky Fan's maximum principle for pairs of contractions.** Formalized in Tau Ceti as [`LinearMap.norm_sum_inner_add_inner_le_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.norm_sum_inner_add_inner_le_kyFanSum).

```lean
LinearMap.norm_sum_inner_add_inner_le_kyFanSum.{u_1, u_2, u_3, u_6} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F] {ι : Type u_6} [Fintype ι]
  (A : E →ₗ[𝕜] F) {P₁ Q₁ : F →ₗ[𝕜] F} {P₂ Q₂ : E →ₗ[𝕜] E} (hP₁ : P₁.IsSymmetric)
  (hQ₁ : Q₁.IsSymmetric) (hP₂ : P₂.IsSymmetric) (hQ₂ : Q₂.IsSymmetric)
  (h₁ : ∀ (y : F), ‖P₁ y‖ ^ 2 + ‖Q₁ y‖ ^ 2 ≤ ‖y‖ ^ 2)
  (h₂ : ∀ (x : E), ‖P₂ x‖ ^ 2 + ‖Q₂ x‖ ^ 2 ≤ ‖x‖ ^ 2) {u : ι → F} {v : ι → E} (hu : Orthonormal 𝕜 u)
  (hv : Orthonormal 𝕜 v) :
  ‖∑ i, (inner 𝕜 (P₁ (u i)) (A (P₂ (v i))) + inner 𝕜 (Q₁ (u i)) (A (Q₂ (v i))))‖ ≤
    A.kyFanSum (Fintype.card ι)
```

**Ky Fan's maximum principle for positive endomorphisms, attainment.** Formalized in Tau Ceti as [`LinearMap.IsPositive.exists_orthonormal_sum_re_inner_eq_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.IsPositive.exists_orthonormal_sum_re_inner_eq_kyFanSum).

```lean
LinearMap.IsPositive.exists_orthonormal_sum_re_inner_eq_kyFanSum.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  {A : E →ₗ[𝕜] E} (hA : A.IsPositive) {k : ℕ} (hk : k ≤ Module.finrank 𝕜 E) :
  ∃ v, Orthonormal 𝕜 v ∧ ∑ i, RCLike.re (inner 𝕜 (v i) (A (v i))) = A.kyFanSum k
```

## Sources

- [Tau Ceti documentation: `LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum)
- [Source of `LinearMap.exists_orthonormal_sum_inner_eq_kyFanSum` in TauCeti/Analysis/InnerProductSpace/KyFan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/KyFan.lean#L318)
