---
declaration: module
origin: cited
lean: V_rho_isometry, V_sigma_isometry, Matrix.opNorm_mul_le, Matrix.opNorm_conjTranspose_eq_opNorm, W_mat_sq_le_one, intermediate_ineq, operator_ineq_SSA, Sᵥₙ_strong_subadditivity
statement: formalized
proof: formalized
---

# QuantumInfo.Entropy.SSA

The module `QuantumInfo.Entropy.SSA`, [QuantumInfo/Entropy/SSA.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean): 43 declarations, 28 with a docstring, 18 listed as significant; 36 private, not shown.

> Quantities of quantum \_relative entropy\_, namely the (standard) quantum relative
> entropy, and generalizations such as sandwiched Rényi relative entropy.

**`Matrix.opNorm`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L35).

> The operator norm of a matrix, with respect to the Euclidean norm (l2 norm) on the domain and codomain.

```lean
noncomputable def Matrix.opNorm (A : Matrix m n 𝕜) : ℝ
```

**`Matrix.isometry_preserves_norm`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L41).

```lean
lemma Matrix.isometry_preserves_norm (A : Matrix n m 𝕜) (hA : A.Isometry) (x : EuclideanSpace 𝕜 m) :
    ‖Matrix.toEuclideanLin A x‖ = ‖x‖
```

**`Matrix.opNorm_isometry`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L60).

```lean
lemma Matrix.opNorm_isometry [Nonempty m] (A : Matrix n m 𝕜) (hA : A.Isometry) : Matrix.opNorm A = 1
```

**`map_to_tensor_MES`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L73).

> The matrix representation of the map $v \mapsto v \otimes \sum_k |k\rangle|k\rangle$.
> The output index is `(d1 \times d2) \times d2`.

```lean
def map_to_tensor_MES : Matrix ((d₁ × d₂) × d₂) d₁ ℂ
```

**`map_to_tensor_MES_prop`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L76).

```lean
lemma map_to_tensor_MES_prop (A : Matrix (d₁ × d₂) (d₁ × d₂) ℂ) :
    (map_to_tensor_MES d₁ d₂).conjTranspose * (Matrix.kronecker A (1 : Matrix d₂ d₂ ℂ)) * (map_to_tensor_MES d₁ d₂) =
    A.traceRight
```

**`V_rho`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L91).

> The isometry V\_rho from the paper.

```lean
noncomputable def V_rho (ρAB : HermitianMat (dA × dB) ℂ) : Matrix ((dA × dB) × dB) dA ℂ
```

**`V_sigma`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L102).

> The isometry V\_sigma from the paper.

```lean
noncomputable def V_sigma (σBC : HermitianMat (dB × dC) ℂ) : Matrix (dB × (dB × dC)) dC ℂ
```

**`V_rho_conj_mul_self_eq`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L110).

> V\_rho^H * V\_rho simplifies to sandwiching the traceRight by the inverse square root.

```lean
lemma V_rho_conj_mul_self_eq (ρAB : HermitianMat (dA × dB) ℂ) (hρ : ρAB.mat.PosDef) :
    let ρA := ρAB.traceRight
    let ρA_inv_sqrt := (ρA⁻¹.sqrt : Matrix dA dA ℂ)
    (V_rho ρAB)ᴴ * (V_rho ρAB) = ρA_inv_sqrt * ρAB.traceRight.mat * ρA_inv_sqrt
```

**`PosDef_traceRight`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L140).

> The partial trace (left) of a positive definite matrix is positive definite.

```lean
lemma PosDef_traceRight [Nonempty dB] (A : HermitianMat (dA × dB) ℂ) (hA : A.mat.PosDef) :
    A.traceRight.mat.PosDef
```

**`PosDef_traceLeft`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L190).

```lean
lemma PosDef_traceLeft [Nonempty dA] (A : HermitianMat (dA × dB) ℂ) (hA : A.mat.PosDef) :
    A.traceLeft.mat.PosDef
```

**`V_rho_isometry`**, a theorem, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L197). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> V\_rho is an isometry.

```lean
theorem V_rho_isometry [Nonempty dB] (ρAB : HermitianMat (dA × dB) ℂ) (hρ : ρAB.mat.PosDef) :
    (V_rho ρAB)ᴴ * (V_rho ρAB) = 1
```

**`V_sigma_isometry`**, a theorem, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L209). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> V\_sigma is an isometry.

```lean
theorem V_sigma_isometry [Nonempty dB] (σBC : HermitianMat (dB × dC) ℂ) (hσ : σBC.mat.PosDef) :
    (V_sigma σBC).conjTranspose * (V_sigma σBC) = 1
```

**`W_mat`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L226).

> The operator W from the paper, defined as a matrix product.

```lean
noncomputable def W_mat (ρAB : HermitianMat (dA × dB) ℂ) (σBC : HermitianMat (dB × dC) ℂ) : Matrix ((dA × dB) × dC) ((dA × dB) × dC) ℂ
```

**`Matrix.opNorm_mul_le`**, a theorem, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L243). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The operator norm of a matrix product is at most the product of the operator norms.

```lean
theorem Matrix.opNorm_mul_le {l m n 𝕜 : Type*} [Fintype l] [Fintype m] [Fintype n]
    [DecidableEq l] [DecidableEq m] [DecidableEq n] [RCLike 𝕜]
    (A : Matrix l m 𝕜) (B : Matrix m n 𝕜) :
    Matrix.opNorm (A * B) ≤ Matrix.opNorm A * Matrix.opNorm B
```

**`Matrix.opNorm_reindex_proven`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L253).

```lean
lemma Matrix.opNorm_reindex_proven {l m n p : Type*} [Fintype l] [Fintype m] [Fintype n] [Fintype p]
    [DecidableEq l] [DecidableEq m] [DecidableEq n] [DecidableEq p]
    (e : m ≃ l) (f : n ≃ p) (A : Matrix m n 𝕜) :
    Matrix.opNorm (A.reindex e f) = Matrix.opNorm A
```

**`U_rho`**, a def, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L279).

> Define U\_rho as the Kronecker product of V\_rho and the identity.

```lean
noncomputable def U_rho (ρAB : HermitianMat (dA × dB) ℂ) : Matrix (((dA × dB) × dB) × dC) (dA × dC) ℂ
```

**`U_sigma`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L285).

> Define U\_sigma as the Kronecker product of the identity and V\_sigma.

```lean
noncomputable def U_sigma (σBC : HermitianMat (dB × dC) ℂ) : Matrix (dA × (dB × (dB × dC))) (dA × dC) ℂ
```

**`Matrix.opNorm_conjTranspose_eq_opNorm`**, a theorem, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L291). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The operator norm of the conjugate transpose is equal to the operator norm.

```lean
theorem Matrix.opNorm_conjTranspose_eq_opNorm {m n : Type*} [Fintype m] [Fintype n]
    [DecidableEq m] [DecidableEq n] (A : Matrix m n 𝕜) :
    Matrix.opNorm Aᴴ = Matrix.opNorm A
```

**`isometry_mul_conjTranspose_le_one`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L299).

```lean
lemma isometry_mul_conjTranspose_le_one {m n : Type*} [Fintype m] [Fintype n]
    [DecidableEq m] [DecidableEq n]
    (V : Matrix m n ℂ) (hV : V.conjTranspose * V = 1) :
    V * V.conjTranspose ≤ 1
```

**`conjTranspose_isometry_mul_isometry_le_one`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L316).

```lean
lemma conjTranspose_isometry_mul_isometry_le_one {m n k : Type*}
    [Fintype m] [Fintype n] [Fintype k] [DecidableEq m] [DecidableEq n] [DecidableEq k]
    (A : Matrix k m ℂ) (B : Matrix k n ℂ)
    (hA : A.conjTranspose * A = 1) (hB : B.conjTranspose * B = 1) :
    (A.conjTranspose * B).conjTranspose * (A.conjTranspose * B) ≤ 1
```

### Helper lemmas for operator\_ineq\_SSA

**`HermitianMat.reindex_le_reindex_iff`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L335).

```lean
lemma HermitianMat.reindex_le_reindex_iff {d d₂ : Type*} [Fintype d] [DecidableEq d]
    [Fintype d₂] [DecidableEq d₂] (e : d ≃ d₂) (A B : HermitianMat d ℂ) :
    A.reindex e ≤ B.reindex e ↔ A ≤ B
```

**`HermitianMat.inv_kronecker`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L341).

```lean
lemma HermitianMat.inv_kronecker {m n : Type*} [Fintype m] [DecidableEq m]
    [Fintype n] [DecidableEq n] [Nonempty m] [Nonempty n]
    (A : HermitianMat m ℂ) (B : HermitianMat n ℂ)
    [A.NonSingular] [B.NonSingular] :
    (A ⊗ₖ B)⁻¹ = A⁻¹ ⊗ₖ B⁻¹
```

**`HermitianMat.inv_reindex`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L356).

```lean
lemma HermitianMat.inv_reindex {d d₂ : Type*} [Fintype d] [DecidableEq d]
    [Fintype d₂] [DecidableEq d₂] (A : HermitianMat d ℂ) (e : d ≃ d₂) :
    (A.reindex e)⁻¹ = A⁻¹.reindex e
```

**`HermitianMat.PosDef_kronecker`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L363).

```lean
lemma HermitianMat.PosDef_kronecker {m n : Type*} [Fintype m] [DecidableEq m]
    [Fintype n] [DecidableEq n]
    (A : HermitianMat m ℂ) (B : HermitianMat n ℂ)
    (hA : A.mat.PosDef) (hB : B.mat.PosDef) :
    (A ⊗ₖ B).mat.PosDef
```

**`HermitianMat.PosDef_reindex`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L371).

```lean
lemma HermitianMat.PosDef_reindex {d d₂ : Type*} [Fintype d] [DecidableEq d]
    [Fintype d₂] [DecidableEq d₂] (A : HermitianMat d ℂ) (e : d ≃ d₂)
    (hA : A.mat.PosDef) :
    (A.reindex e).mat.PosDef
```

**`BigIdx`**, an abbrev, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L500).

```lean
abbrev BigIdx (dA dB dC : Type*)
```

**`SmallIdx`**, an abbrev, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L501).

```lean
abbrev SmallIdx (dA dB dC : Type*)
```

**`MidIdx`**, an abbrev, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L502).

```lean
abbrev MidIdx (dA dB dC : Type*)
```

**`W_mat_sq_le_one`**, a theorem, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L718). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Core inequality: W†W ≤ I.
> This is the key step, following from the isometry argument:
> V\_rho ⊗ I\_C and I\_A ⊗ V\_sigma are isometries, their cross product has norm ≤ 1,
> and the result can be related to W\_mat through the MES computation (Eq. 6 in Lin-Kim-Hsieh).

```lean
theorem W_mat_sq_le_one [Nonempty dA] [Nonempty dB] [Nonempty dC]
    (ρAB : HermitianMat (dA × dB) ℂ) (σBC : HermitianMat (dB × dC) ℂ)
    (hρ : ρAB.mat.PosDef) (hσ : σBC.mat.PosDef) :
    (W_mat ρAB σBC)ᴴ * (W_mat ρAB σBC) ≤ 1
```

**`intermediate_ineq`**, a theorem, [line 762](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L762). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The intermediate operator inequality: ρ\_AB ⊗ σ\_C⁻¹ ≤ (ρ\_A ⊗ σ\_BC⁻¹).reindex(assoc⁻¹).
> This is derived from W\_mat\_sq\_le\_one by algebraic manipulation (conjugation and simplification).

```lean
theorem intermediate_ineq [Nonempty dA] [Nonempty dB] [Nonempty dC]
    (ρAB : HermitianMat (dA × dB) ℂ) (σBC : HermitianMat (dB × dC) ℂ)
    (hρ : ρAB.mat.PosDef) (hσ : σBC.mat.PosDef) :
    ρAB ⊗ₖ (σBC.traceLeft)⁻¹ ≤
      (ρAB.traceRight ⊗ₖ σBC⁻¹).reindex (Equiv.prodAssoc dA dB dC).symm
```

**`operator_ineq_SSA`**, a theorem, [line 793](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L793). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Operator extension of SSA** (Main result of Lin-Kim-Hsieh).
> For positive definite ρ\_AB and σ\_BC:
> `ρ_A⁻¹ ⊗ σ_BC ≤ ρ_AB⁻¹ ⊗ σ_C`
> where ρ\_A = Tr\_B(ρ\_AB) and σ\_C = Tr\_B(σ\_BC), and the RHS is reindexed
> via the associator `(dA × dB) × dC ≃ dA × (dB × dC)`.

```lean
theorem operator_ineq_SSA [Nonempty dA] [Nonempty dB] [Nonempty dC]
    (ρAB : HermitianMat (dA × dB) ℂ) (σBC : HermitianMat (dB × dC) ℂ)
    (hρ : ρAB.mat.PosDef) (hσ : σBC.mat.PosDef) :
    ρAB.traceRight⁻¹ ⊗ₖ σBC ≤
      (ρAB⁻¹ ⊗ₖ σBC.traceLeft).reindex (Equiv.prodAssoc dA dB dC)
```

### Weak monotonicity and SSA proof infrastructure

**`Sᵥₙ_wm`**, a lemma, [line 1055](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1055).

> Weak monotonicity, version with partial traces.

```lean
lemma Sᵥₙ_wm (ρ : MState (d₁ × d₂ × d₃)) :
    Sᵥₙ ρ.traceRight + Sᵥₙ ρ.traceLeft.traceLeft ≤
    Sᵥₙ ρ.assoc'.traceRight + Sᵥₙ ρ.traceLeft
```

**`Sᵥₙ_strong_subadditivity`**, a theorem, [line 1189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1189). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Strong subadditivity on a tripartite system

```lean
theorem Sᵥₙ_strong_subadditivity (ρ₁₂₃ : MState (d₁ × d₂ × d₃)) :
    let ρ₁₂ := ρ₁₂₃.assoc'.traceRight;
    let ρ₂₃ := ρ₁₂₃.traceLeft;
    let ρ₂ := ρ₁₂₃.traceLeft.traceRight;
    Sᵥₙ ρ₁₂₃ + Sᵥₙ ρ₂ ≤ Sᵥₙ ρ₁₂ + Sᵥₙ ρ₂₃
```

**`Sᵥₙ_subadditivity`**, a theorem, [line 1201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1201). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> "Ordinary" subadditivity of von Neumann entropy

```lean
theorem Sᵥₙ_subadditivity (ρ : MState (d₁ × d₂)) :
    Sᵥₙ ρ ≤ Sᵥₙ ρ.traceRight + Sᵥₙ ρ.traceLeft
```

**`Sᵥₙ_pure_tripartite_triangle`**, a theorem, [line 1214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1214). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Triangle inequality for pure tripartite states: S(A) ≤ S(B) + S(C).

```lean
theorem Sᵥₙ_pure_tripartite_triangle (ψ : Ket ((d₁ × d₂) × d₃)) :
    Sᵥₙ (MState.pure ψ).traceRight.traceRight ≤
    Sᵥₙ (MState.pure ψ).traceRight.traceLeft + Sᵥₙ (MState.pure ψ).traceLeft
```

**`Sᵥₙ_triangle_ineq_one_way`**, a theorem, [line 1224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1224). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> One direction of the Araki-Lieb triangle inequality: S(A) ≤ S(B) + S(AB).

```lean
theorem Sᵥₙ_triangle_ineq_one_way (ρ : MState (d₁ × d₂)) : Sᵥₙ ρ.traceRight ≤ Sᵥₙ ρ.traceLeft + Sᵥₙ ρ
```

**`Sᵥₙ_triangle_subaddivity`**, a theorem, [line 1230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1230). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Araki-Lieb triangle inequality on von Neumann entropy

```lean
theorem Sᵥₙ_triangle_subaddivity (ρ : MState (d₁ × d₂)) :
    abs (Sᵥₙ ρ.traceRight - Sᵥₙ ρ.traceLeft) ≤ Sᵥₙ ρ
```

**`Sᵥₙ_weak_monotonicity`**, a theorem, [line 1241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1241). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Weak monotonicity of quantum conditional entropy: S(A|B) + S(A|C) ≥ 0.

```lean
theorem Sᵥₙ_weak_monotonicity (ρ : MState (dA × dB × dC)) :
    let ρAB := ρ.assoc'.traceRight
    let ρAC := ρ.SWAP.assoc.traceLeft.SWAP
    0 ≤ qConditionalEnt ρAB + qConditionalEnt ρAC
```

**`qConditionalEnt_strong_subadditivity`**, a theorem, [line 1255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1255). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Strong subadditivity, stated in terms of conditional entropies.
> Also called the data processing inequality. H(A|BC) ≤ H(A|B).

```lean
theorem qConditionalEnt_strong_subadditivity (ρ₁₂₃ : MState (d₁ × d₂ × d₃)) :
    qConditionalEnt ρ₁₂₃ ≤ qConditionalEnt ρ₁₂₃.assoc'.traceRight
```

**`qMutualInfo_strong_subadditivity`**, a theorem, [line 1264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1264). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Strong subadditivity, stated in terms of quantum mutual information.
> I(A;BC) ≥ I(A;B).

```lean
theorem qMutualInfo_strong_subadditivity (ρ₁₂₃ : MState (d₁ × d₂ × d₃)) :
    qMutualInfo ρ₁₂₃ ≥ qMutualInfo ρ₁₂₃.assoc'.traceRight
```

**`qcmi_nonneg`**, a theorem, [line 1272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1272). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum conditional mutual information `QCMI` is nonnegative.

```lean
theorem qcmi_nonneg (ρ : MState (dA × dB × dC)) :
    0 ≤ qcmi ρ
```

**`qcmi_le_2_log_dim`**, a theorem, [line 1279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1279). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum conditional mutual information `QCMI ρABC` is at most 2 log dA.

```lean
theorem qcmi_le_2_log_dim (ρ : MState (dA × dB × dC)) :
    qcmi ρ ≤ 2 * Real.log (Fintype.card dA)
```

**`qcmi_le_2_log_dim'`**, a theorem, [line 1286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean#L1286). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum conditional mutual information `QCMI ρABC` is at most 2 log dC.

```lean
theorem qcmi_le_2_log_dim' (ρ : MState (dA × dB × dC)) :
    qcmi ρ ≤ 2 * Real.log (Fintype.card dC)
```

## Depends on

- [QuantumInfo.Entropy.VonNeumann](vonneumann.md)

## Sources

- [QuantumInfo/Entropy/SSA.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/SSA.lean)
