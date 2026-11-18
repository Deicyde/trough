---
declaration: module
origin: cited
lean: Matrix.IsHermitian.cfc_eq_any_isometry, Matrix.IsHermitian.cfc_eq_any_unitary, LinearMap.IsSymmetric.orthogonalFamily_eigenspace_inf_eigenspace', iSup_mono_bot, LinearMap.IsSymmetric.directSum_isInternal_of_commute', Matrix.SharedEigenbasis.sharedEigenvectorUnitary_mulVec, Matrix.SharedEigenbasis.mulVec_sharedEigenbasisA, Matrix.SharedEigenbasis.star_shared_mul_B_mul_IsDiag
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Isometry

The module `QuantumInfo.ForMathlib.Isometry`, [QuantumInfo/ForMathlib/Isometry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean): 42 declarations (1 instance with no name), 11 with a docstring, 10 listed as significant; 1 private, not shown.

**`Matrix.Isometry`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L28).

> An isometry is a matrix `A` such that `AAᴴ = 1`. Compare with a unitary, which
> requires `AAᴴ = AᴴA = 1`. It is common to claim that, in a finite-dimensional vector
> space, a two-sided isometry (`A.Isometry ∧ Aᴴ.Isometry`) must be square and therefore unitary;
> this is does not work out so well here, since a `Matrix m n R` can be a two-sided isometry,
> but cannot be a `unitary` since the rows and columns are index by different labels.

```lean
def Matrix.Isometry (A : Matrix d d₂ R) : Prop
```

**`Matrix.submatrix_one_isometry`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L32).

```lean
lemma Matrix.submatrix_one_isometry {e : d₂ → d} {f : d₃ → d} (he : e.Bijective) (hf : f.Injective) :
    (submatrix (α := R) 1 e f).Isometry
```

**`Matrix.submatrix_one_id_left_isometry`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L65).

```lean
lemma Matrix.submatrix_one_id_left_isometry {e : d₂ → d} (he : e.Bijective) :
    (submatrix (1 : Matrix d d R) e id).Isometry
```

**`Matrix.submatrix_one_id_right_isometry`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L70).

```lean
lemma Matrix.submatrix_one_id_right_isometry {e : d₂ → d} (he : e.Injective) :
    (submatrix (1 : Matrix d d R) id e).Isometry
```

**`Matrix.mem_unitaryGroup_iff_isometry`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L74).

```lean
lemma Matrix.mem_unitaryGroup_iff_isometry (A : Matrix d d R) :
    A ∈ unitaryGroup d R ↔ A.Isometry ∧ Aᴴ.Isometry
```

**`Equiv.Perm.permMatrix_mem_unitaryGroup`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L79).

```lean
lemma Equiv.Perm.permMatrix_mem_unitaryGroup (e : Perm d) :
    e.permMatrix R ∈ Matrix.unitaryGroup d R
```

**`Matrix.reindex_one_isometry`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L95).

```lean
lemma Matrix.reindex_one_isometry (e : d ≃ d₂) (f : d ≃ d₃) :
    (reindex (α := R) e f 1).Isometry
```

**`Matrix.reindex_one_mem_unitaryGroup`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L104).

```lean
lemma Matrix.reindex_one_mem_unitaryGroup (e : d ≃ d₂)  :
    reindex (α := R) e e 1 ∈ unitaryGroup d₂ R
```

**`Matrix.reindex_eq_conj`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L114).

```lean
lemma Matrix.reindex_eq_conj (A : Matrix d d R) (e : d ≃ d₂) : reindex e e A =
    (reindex (α := R) e (.refl d) 1) * A * (reindex (α := R) (.refl d) e 1)
```

**`Matrix.reindex_eq_conj_unitaryGroup'`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L120).

```lean
lemma Matrix.reindex_eq_conj_unitaryGroup' (A : Matrix d d R) (e : Equiv.Perm d) : reindex e e A =
    (⟨_, e⁻¹.permMatrix_mem_unitaryGroup⟩ : unitaryGroup d R) * A * (⟨_, e.permMatrix_mem_unitaryGroup⟩ : unitaryGroup d R)
```

**`Matrix.IsHermitian.eigenvalue_ext`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L126).

```lean
lemma Matrix.IsHermitian.eigenvalue_ext (hA : A.IsHermitian)
  (h : ∀ (v : d → 𝕜) (lam : 𝕜), A *ᵥ v = lam • v → B *ᵥ v = lam • v) :
    A = B
```

**`Matrix.IsHermitian.cfc_eq_any_isometry`**, a theorem, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L181). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Generalizes `Matrix.IsHermitian.cfc.eq_1`, which gives a definition for the matrix CFC in terms of
> `Matrix.IsHermitian.eigenvalues` and `Matrix.IsHermitian.eigenvectorUnitary`, to show that the CFC works
> similarly for \_any\_ diagonalization by a two-sided isometry.

```lean
theorem Matrix.IsHermitian.cfc_eq_any_isometry {n m 𝕜 : Type*} [RCLike 𝕜]
  [Fintype n] [DecidableEq n] [Fintype m] [DecidableEq m]
  {A : Matrix n n 𝕜} (hA : A.IsHermitian) {U : Matrix n m 𝕜}
  (hU₁ : U * Uᴴ = 1) (hU₂ : Uᴴ * U = 1) {D : m → ℝ}
  (hUD : A = (U * diagonal (RCLike.ofReal ∘ D) : Matrix _ _ _) * Uᴴ) (f : ℝ → ℝ) :
    hA.cfc f = (U * diagonal (RCLike.ofReal ∘ f ∘ D) : Matrix _ _ _) * Uᴴ
```

**`Matrix.IsHermitian.cfc_eq_any_unitary`**, a theorem, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L217). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Generalizes `Matrix.IsHermitian.cfc.eq_1`, which gives a definition for the matrix CFC in terms of
> `Matrix.IsHermitian.eigenvalues` and `Matrix.IsHermitian.eigenvectorUnitary`, to show that the CFC works
> similarly for \_any\_ diagonalization.

```lean
theorem Matrix.IsHermitian.cfc_eq_any_unitary {n 𝕜 : Type*} [RCLike 𝕜] [Fintype n] [DecidableEq n]
  {A : Matrix n n 𝕜} (hA : A.IsHermitian) {U : unitaryGroup n 𝕜} {D : n → ℝ}
  (hUD : A = U.val * diagonal (RCLike.ofReal ∘ D) * star U.val) (f : ℝ → ℝ) :
    hA.cfc f = U.val * diagonal (RCLike.ofReal ∘ f ∘ D) * star U.val
```

**`Matrix.cfc_conj_isometry`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L250).

```lean
lemma Matrix.cfc_conj_isometry (f : ℝ → ℝ) {u : Matrix d₂ d 𝕜}
  (hu₁ : u.Isometry) (hu₂ : uᴴ.Isometry) :
    cfc f (u * A * uᴴ) = u * (cfc f A) * uᴴ
```

**`Matrix.cfc_conj_unitary`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L264).

```lean
lemma Matrix.cfc_conj_unitary (f : ℝ → ℝ) (u : unitaryGroup d 𝕜) :
    cfc f (u * A * u⁻¹) = u * (cfc f A) * u⁻¹
```

**`Matrix.cfc_conj_unitary'`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L270).

```lean
lemma Matrix.cfc_conj_unitary' (f : ℝ → ℝ) (u : unitaryGroup d 𝕜) :
    cfc f (uᴴ * A * u.val) = uᴴ * (cfc f A) * u.val
```

**`Matrix.cfc_reindex`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L276).

```lean
lemma Matrix.cfc_reindex (f : ℝ → ℝ) (e : d ≃ d₂) :
    cfc f (reindex e e A) = reindex e e (cfc f A)
```

**`Matrix.commute_euclideanLin`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L286).

```lean
lemma Matrix.commute_euclideanLin (hAB : Commute A B) :
    Commute A.toEuclideanLin B.toEuclideanLin
```

**`LinearMap.IsSymmetric.orthogonalFamily_eigenspace_inf_eigenspace'`**, a theorem, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L306). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Similar to `LinearMap.IsSymmetric.orthogonalFamily_eigenspace_inf_eigenspace`, but here the direct sum
> is indexed by only the pairs of eigenvalues, as opposed to all pairs of `𝕜` values, giving a finite
> decomposition.

```lean
theorem LinearMap.IsSymmetric.orthogonalFamily_eigenspace_inf_eigenspace' {𝕜 E : Type*} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {A B : E →ₗ[𝕜] E}
  (hA : A.IsSymmetric) (hB : B.IsSymmetric) :
    OrthogonalFamily 𝕜 (fun (μ₁₂ : Eigenvalues A × Eigenvalues B) ↦
      ↥(eigenspace A μ₁₂.1 ⊓ eigenspace B μ₁₂.2)) fun μ₁₂ ↦
    (eigenspace A μ₁₂.1 ⊓ eigenspace B μ₁₂.2).subtypeₗᵢ
```

**`iSup_mono_bot`**, a theorem, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L323). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Variant of `iSup_mono'` that allows for an easier handling of bottom elements.

```lean
theorem iSup_mono_bot {α : Type*} {ι ι' : Sort*} [CompleteLattice α]
  {f : ι → α} {g : ι' → α} (h : ∀ (i : ι), f i = ⊥ ∨ ∃ i', f i ≤ g i') :
    iSup f ≤ iSup g
```

**`Commute.isSymmetric_directSumDecomposition`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L333).

```lean
noncomputable def Commute.isSymmetric_directSumDecomposition  {𝕜 E : Type*} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {A B : E →ₗ[𝕜] E} [FiniteDimensional 𝕜 E]
  (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) :
    DirectSum.Decomposition fun (μ₁₂ : Eigenvalues A × Eigenvalues B) ↦
      (eigenspace A μ₁₂.1 ⊓ eigenspace B μ₁₂.2)
```

**`LinearMap.IsSymmetric.directSum_isInternal_of_commute'`**, a theorem, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L357). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Similar to `LinearMap.IsSymmetric.directSum_isInternal_of_commute`, but here the direct sum
> is indexed by only the pairs of eigenvalues, as opposed to all pairs of `𝕜` values, giving a finite
> decomposition.

```lean
theorem LinearMap.IsSymmetric.directSum_isInternal_of_commute' {𝕜 E : Type*} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {A B : E →ₗ[𝕜] E} [FiniteDimensional 𝕜 E]
  (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) :
    DirectSum.IsInternal fun (μ₁₂ : Eigenvalues A × Eigenvalues B) ↦
      eigenspace A μ₁₂.1 ⊓ eigenspace B μ₁₂.2
```

**`LinearMap.sharedEigenbasis`**, a def, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L404).

```lean
noncomputable def LinearMap.sharedEigenbasis {A B : EuclideanSpace 𝕜 d →ₗ[𝕜] EuclideanSpace 𝕜 d}
  (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) :
    OrthonormalBasis d 𝕜 (EuclideanSpace 𝕜 d)
```

**`LinearMap.sharedEigenvaluesA`**, a def, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L411).

```lean
noncomputable def LinearMap.sharedEigenvaluesA {A B : EuclideanSpace 𝕜 d →ₗ[𝕜] EuclideanSpace 𝕜 d}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) : d → ℝ
```

**`LinearMap.sharedEigenvaluesB`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L415).

```lean
noncomputable def LinearMap.sharedEigenvaluesB {A B : EuclideanSpace 𝕜 d →ₗ[𝕜] EuclideanSpace 𝕜 d}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) : d → ℝ
```

**`LinearMap.mem_eigenspace_inf_of_sharedEigenbasis`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L420).

```lean
lemma LinearMap.mem_eigenspace_inf_of_sharedEigenbasis {A B : EuclideanSpace 𝕜 d →ₗ[𝕜] EuclideanSpace 𝕜 d}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) (i : d) :
    ∃ (μ : Module.End.Eigenvalues A) (ν : Module.End.Eigenvalues B),
      LinearMap.sharedEigenbasis hA hB hAB i ∈ Module.End.eigenspace A μ ⊓ Module.End.eigenspace B ν
```

**`LinearMap.apply_A_sharedEigenbasis`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L436).

```lean
lemma LinearMap.apply_A_sharedEigenbasis {A B : EuclideanSpace 𝕜 d →ₗ[𝕜] EuclideanSpace 𝕜 d}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) (i : d) :
    A (sharedEigenbasis hA hB hAB i) = (sharedEigenvaluesA hA hB hAB i : 𝕜) • (sharedEigenbasis hA hB hAB i)
```

**`LinearMap.apply_B_sharedEigenbasis`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L452).

```lean
lemma LinearMap.apply_B_sharedEigenbasis {A B : EuclideanSpace 𝕜 d →ₗ[𝕜] EuclideanSpace 𝕜 d}
    (hA : A.IsSymmetric) (hB : B.IsSymmetric) (hAB : Commute A B) (i : d) :
    B (sharedEigenbasis hA hB hAB i) = (sharedEigenvaluesB hA hB hAB i : 𝕜) • (sharedEigenbasis hA hB hAB i)
```

**`Matrix.sharedEigenbasis`**, a def, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L467).

```lean
noncomputable def Matrix.sharedEigenbasis
  (hA : A.IsHermitian) (hB : B.IsHermitian) (hAB : Commute A B) :
    OrthonormalBasis d 𝕜 (EuclideanSpace 𝕜 d)
```

**`Matrix.sharedEigenvectorUnitary`**, a def, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L473).

```lean
noncomputable def Matrix.sharedEigenvectorUnitary (hA : A.IsHermitian) (hB : B.IsHermitian)
    (hAB : Commute A B) : Matrix.unitaryGroup d 𝕜
```

**`Matrix.SharedEigenbasis.sharedEigenvectorUnitary_mulVec`**, a theorem, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L483). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Analogous to `Matrix.IsHermitian.eigenvectorUnitary_mulVec` for the shared basis.

```lean
theorem sharedEigenvectorUnitary_mulVec (j : d) : (sharedEigenvectorUnitary hA hB hAB) *ᵥ
    Pi.single j 1 = WithLp.ofLp (sharedEigenbasis hA hB hAB j)
```

**`Matrix.SharedEigenbasis.sharedEigenvalueA`**, a def, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L488).

```lean
noncomputable def sharedEigenvalueA (j : d) : ℝ
```

**`Matrix.SharedEigenbasis.sharedEigenvalueB`**, a def, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L494).

```lean
noncomputable def sharedEigenvalueB (j : d) : ℝ
```

**`Matrix.SharedEigenbasis.mulVec_sharedEigenbasisA`**, a theorem, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L501). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Analogous to `Matrix.IsHermitian.mulVec_eigenvectorBasis` for the shared basis.

```lean
theorem mulVec_sharedEigenbasisA (j : d) :
    A *ᵥ (sharedEigenbasis hA hB hAB j) =
    (sharedEigenvalueA hA hB hAB) j • WithLp.ofLp (sharedEigenbasis hA hB hAB j)
```

**`Matrix.SharedEigenbasis.mulVec_sharedEigenbasisB`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L511).

```lean
lemma mulVec_sharedEigenbasisB (j : d) :
    B *ᵥ (sharedEigenbasis hA hB hAB j) =
    (sharedEigenvalueB hA hB hAB) j • WithLp.ofLp (sharedEigenbasis hA hB hAB j)
```

**`Matrix.SharedEigenbasis.star_shared_mul_A_mul_IsDiag`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L527).

```lean
lemma star_shared_mul_A_mul_IsDiag : IsDiag
    ((star (sharedEigenvectorUnitary hA hB hAB : Matrix d d 𝕜)) * A *
      (sharedEigenvectorUnitary hA hB hAB : Matrix d d 𝕜))
```

**`Matrix.SharedEigenbasis.star_shared_mul_B_mul_IsDiag`**, a theorem, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L546). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Analogous to `Matrix.IsHermitian.star_mul_self_mul_eq_diagonal` for the shared basis.

```lean
theorem star_shared_mul_B_mul_IsDiag : IsDiag
    ((star (sharedEigenvectorUnitary hA hB hAB : Matrix d d 𝕜)) * B *
      (sharedEigenvectorUnitary hA hB hAB : Matrix d d 𝕜))
```

**`Commute.exists_unitary`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L592).

```lean
lemma Commute.exists_unitary (hA : A.IsHermitian) (hB : B.IsHermitian) (hAB : Commute A B) :
    ∃ U : Matrix.unitaryGroup d 𝕜, (U.val * A * Uᴴ).IsDiag ∧ (U.val * B * Uᴴ).IsDiag
```

**`instInvertibleUnitaryGroup`**, an instance, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L603).

```lean
instance instInvertibleUnitaryGroup (U : Matrix.unitaryGroup d 𝕜) : Invertible U
```

**An instance with no name**, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L606).

```lean
instance (U : Matrix.unitaryGroup d 𝕜) : Invertible U.val
```

**`Matrix.IsDiag.exists_cfc`**, a theorem, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L611). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a matrix is diagonalized by a unitary matrix, then it can be written as a
> CFC of a (particular, canonical) diagonal matrix.

```lean
theorem Matrix.IsDiag.exists_cfc {U : Matrix.unitaryGroup d 𝕜} {M : Matrix d d 𝕜}
  (hU : (U.val * M * Uᴴ).IsDiag) (hM : M.IsHermitian) (e : d ≃ Fin (Fintype.card d)) :
       ∃ f : ℝ → ℝ,
    M = cfc f (Uᴴ * (Matrix.diagonal fun x => ↑↑(e x)) * U.val)
```

**`Commute.exists_cfc`**, a theorem, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean#L641). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If two Hermitian matrices commute, there exists a common matrix that they are both a CFC of.

```lean
theorem Commute.exists_cfc (hA : A.IsHermitian) (hB : B.IsHermitian) (hAB : Commute A B) :
    ∃ C : Matrix d d 𝕜, (∃ f : ℝ → ℝ, A = cfc f C) ∧ (∃ g : ℝ → ℝ, B = cfc g C)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [QuantumInfo.ForMathlib.Matrix](matrix.md)

## Sources

- [QuantumInfo/ForMathlib/Isometry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Isometry.lean)
