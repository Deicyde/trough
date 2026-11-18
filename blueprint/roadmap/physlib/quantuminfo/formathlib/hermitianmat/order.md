---
declaration: module
origin: cited
lean: HermitianMat.kronecker_nonneg, HermitianMat.kronecker_self_mono, HermitianMat.kronecker_pos, HermitianMat.conj_nonneg, HermitianMat.le_smul_one_imp_eigenvalues_le, HermitianMat.eigenvalues_le_imp_le_smul_one, HermitianMat.eigenvalues_nonneg, HermitianMat.mat_nonneg
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Order

The module `QuantumInfo.ForMathlib.HermitianMat.Order`, [QuantumInfo/ForMathlib/HermitianMat/Order.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean): 62 declarations (7 instances with no name), 25 with a docstring, 11 listed as significant; 1 private, not shown.

**An instance with no name**, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L25).

> The `MatrixOrder` instance for Matrix (the Loewner order) we keep open for
> HermitianMat, always.

```lean
instance : PartialOrder (HermitianMat n 𝕜)
```

**An instance with no name**, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L29).

```lean
instance : IsOrderedAddMonoid (HermitianMat n 𝕜)
```

**`HermitianMat.le_iff`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L33).

```lean
lemma le_iff : A ≤ B ↔ (B - A).mat.PosSemidef
```

**`HermitianMat.zero_le_iff`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L37).

```lean
lemma zero_le_iff : 0 ≤ A ↔ A.mat.PosSemidef
```

**`HermitianMat.le_iff_mulVec_le`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L40).

```lean
lemma le_iff_mulVec_le : A ≤ B ↔
    ∀ x, star x ⬝ᵥ A.mat *ᵥ x ≤ star x ⬝ᵥ B.mat *ᵥ x
```

**An instance with no name**, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L44).

```lean
instance [DecidableEq n] : ZeroLEOneClass (HermitianMat n 𝕜)
```

**`HermitianMat.lt_iff_posdef`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L50).

```lean
lemma lt_iff_posdef : A < B ↔ (B - A).mat.PosSemidef ∧ A ≠ B
```

**An instance with no name**, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L53).

```lean
instance : IsStrictOrderedModule ℝ (HermitianMat n 𝕜)
```

**`HermitianMat.posSemidef_iff_spectrum_Ici`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L71).

```lean
lemma posSemidef_iff_spectrum_Ici [DecidableEq n] (A : HermitianMat n 𝕜) :
    0 ≤ A ↔ spectrum ℝ A.mat ⊆ Set.Ici 0
```

**`HermitianMat.posSemidef_iff_spectrum_nonneg`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L76).

```lean
lemma posSemidef_iff_spectrum_nonneg [DecidableEq n] (A : HermitianMat n 𝕜) :
    0 ≤ A ↔ ∀ x ∈ spectrum ℝ A.mat, 0 ≤ x
```

**`HermitianMat.trace_nonneg`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L80).

```lean
lemma trace_nonneg (hA : 0 ≤ A) : 0 ≤ A.trace
```

**`HermitianMat.trace_pos`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L83).

```lean
lemma trace_pos (hA : 0 < A) : 0 < A.trace
```

**`HermitianMat.evalHermitianMatTrace`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L96).

> Positivity extension for `HermitianMat.trace`: nonneg when the matrix is nonneg,
> positive when the matrix is positive.

```lean
meta def evalHermitianMatTrace : PositivityExt
```

**An instance with no name**, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L108).

```lean
instance : PosSMulMono ℝ (HermitianMat n 𝕜)
```

**An instance with no name**, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L110).

```lean
instance : SMulPosMono ℝ (HermitianMat n 𝕜)
```

**An instance with no name**, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L113).

```lean
instance : PosSMulReflectLE ℝ (HermitianMat n 𝕜)
```

**`HermitianMat.le_trace_smul_one`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L116).

```lean
lemma le_trace_smul_one [DecidableEq n] (hA : 0 ≤ A) : A ≤ A.trace • 1
```

**`HermitianMat.kronecker_nonneg`**, a theorem, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L124). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Kronecker product of two nonnegative Hermitian matrices is nonnegative.

```lean
theorem kronecker_nonneg {A : HermitianMat m 𝕜} (hA : 0 ≤ A) (hB : 0 ≤ B) : 0 ≤ A ⊗ₖ B
```

**`HermitianMat.kronecker_self_mono`**, a theorem, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L129). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The self-Kronecker map `A ↦ A ⊗ₖ A` is monotone on nonnegative Hermitian matrices.

```lean
theorem kronecker_self_mono (hA : 0 ≤ A) (hB : 0 ≤ B) (hAB : A ≤ B) :
    A ⊗ₖ A ≤ B ⊗ₖ B
```

**`HermitianMat.kronecker_pos`**, a theorem, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L151). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Kronecker product of two positive Hermitian matrices is positive.

```lean
theorem kronecker_pos {A : HermitianMat m 𝕜} (hA : 0 < A) (hB : 0 < B) : 0 < A ⊗ₖ B
```

**`HermitianMat.posSemidef_to_nonneg`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L162).

```lean
lemma posSemidef_to_nonneg {A : Matrix n n 𝕜} (hA : A.PosSemidef) : 0 ≤ A
```

**`HermitianMat.posDef_to_pos`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L166).

```lean
lemma posDef_to_pos {A : Matrix n n 𝕜} (hA : A.PosDef) [Nonempty n] : 0 < A
```

**`HermitianMat.findMatrixPSDInExpr`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L176).

> Given an expression `e` (a matrix) and a proof expression `p` whose type may be
> `Matrix.PosSemidef A`, `Matrix.PosDef A`, or `And P Q` (syntactically), attempt to
> find a proof of nonnegativity or positivity for `e`. Only syntactic matching on the
> head constant is used; `isDefEq` is used only to compare the matrix argument.

```lean
meta partial def findMatrixPSDInExpr (e : Expr) (p : Expr) (ty : Expr) :
    MetaM (Option (Bool × Expr))
```

**`HermitianMat.evalMatrixPSD`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L221).

> Positivity extension for `Matrix`: looks for `A.PosSemidef` or `A.PosDef` in the
> local context (including syntactic `And` conjunctions) to prove `0 ≤ A` or `0 < A`.

```lean
meta def evalMatrixPSD : PositivityExt
```

**`HermitianMat.mat_posSemidef_to_nonneg`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L240).

```lean
lemma mat_posSemidef_to_nonneg (hA : A.mat.PosSemidef) : 0 ≤ A
```

**`HermitianMat.mat_posDef_to_pos`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L243).

```lean
lemma mat_posDef_to_pos [Nonempty n] (hA : A.mat.PosDef) : 0 < A
```

**`HermitianMat.findHermitianMatPSDInExpr`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L251).

> Given an expression `e` (a `HermitianMat`) and a proof expression `p` whose type may be
> `Matrix.PosSemidef A.mat`, `Matrix.PosDef A.mat`, or `And P Q` (syntactically), attempt to
> find a proof of nonnegativity or positivity for `e`. Only syntactic matching on the
> head constant is used; `isDefEq` is used only to compare the `HermitianMat` argument.

```lean
meta partial def findHermitianMatPSDInExpr (e : Expr) (p : Expr) (ty : Expr) :
    MetaM (Option (Bool × Expr))
```

**`HermitianMat.evalHermitianMatPSD`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L299).

> Positivity extension for `HermitianMat`: looks for `A.mat.PosSemidef` or `A.mat.PosDef` in
> the local context (including syntactic `And` conjunctions) to prove `0 ≤ A` or `0 < A`.

```lean
meta def evalHermitianMatPSD : PositivityExt
```

**`HermitianMat.evalHermitianMatKronecker`**, a def, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L320).

> Positivity extension for `HermitianMat.kronecker`: nonneg when both factors are.

```lean
meta def evalHermitianMatKronecker : PositivityExt
```

**`HermitianMat.conj_nonneg`**, a theorem, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L336). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Positivity extension for `HermitianMat.conj`: nonneg when the inner matrix is.

```lean
theorem conj_nonneg (hA : 0 ≤ A) : 0 ≤ A.conj M
```

**`HermitianMat.conj_pos`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L340).

```lean
lemma conj_pos [DecidableEq n] {A : HermitianMat n 𝕜} {M : Matrix m n 𝕜} (hA : 0 < A)
    (h : LinearMap.ker M.toEuclideanLin ≤ A.ker) : 0 < A.conj M
```

**`HermitianMat.evalHermitianMatConj`**, a def, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L347).

> Positivity extension for `HermitianMat.conj`: nonneg when the inner matrix is.

```lean
meta def evalHermitianMatConj : PositivityExt
```

**`HermitianMat.convex_cone`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L379).

```lean
lemma convex_cone (hA : 0 ≤ A) (hB : 0 ≤ B) {c₁ c₂ : ℝ} (hc₁ : 0 ≤ c₁) (hc₂ : 0 ≤ c₂) :
    0 ≤ (c₁ • A + c₂ • B)
```

**`HermitianMat.sq_nonneg`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L384).

```lean
lemma sq_nonneg [DecidableEq n] : 0 ≤ A ^ 2
```

**`HermitianMat.ker_antitone`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L389).

```lean
lemma ker_antitone [DecidableEq n] (hA : 0 ≤ A) : A ≤ B → B.ker ≤ A.ker
```

**`HermitianMat.diagonal_le_diagonal`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L401).

```lean
lemma diagonal_le_diagonal [DecidableEq n] {f g : n → ℝ} : diagonal 𝕜 f ≤ diagonal 𝕜 g ↔ f ≤ g
```

**`HermitianMat.diagonal_nonneg`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L407).

```lean
lemma diagonal_nonneg [DecidableEq n] {f : n → ℝ} : 0 ≤ diagonal 𝕜 f ↔ 0 ≤ f
```

**`HermitianMat.conj_mono`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L410).

```lean
lemma conj_mono (h : A ≤ B) : A.conj M ≤ B.conj M
```

**`HermitianMat.conj_posDef`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L417).

```lean
lemma conj_posDef [DecidableEq n] (hA : A.mat.PosDef) (hN : IsUnit N) :
    (A.conj N).mat.PosDef
```

**`HermitianMat.inv_conj`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L434).

```lean
lemma inv_conj [DecidableEq n] {M : Matrix n n 𝕜} (hM : IsUnit M) :
    (A.conj M)⁻¹ = A⁻¹.conj (M⁻¹)ᴴ
```

**`HermitianMat.le_iff_mulVec_le_mulVec`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L444).

```lean
lemma le_iff_mulVec_le_mulVec (A B : HermitianMat n 𝕜) :
    A ≤ B ↔ ∀ v : n → 𝕜, star v ⬝ᵥ A.mat *ᵥ v ≤ star v ⬝ᵥ B.mat *ᵥ v
```

**`HermitianMat.inner_mulVec_nonneg`**, a lemma, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L452).

```lean
lemma inner_mulVec_nonneg (hA : 0 ≤ A) (v : n → 𝕜) :
    0 ≤ star v ⬝ᵥ A.mat *ᵥ v
```

**`HermitianMat.mem_ker_of_inner_mulVec_zero`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L457).

```lean
lemma mem_ker_of_inner_mulVec_zero [DecidableEq n] (hA : 0 ≤ A) (v : EuclideanSpace 𝕜 n)
    (h : star v ⬝ᵥ A.mat *ᵥ v = 0) : v ∈ A.ker
```

**`HermitianMat.ker_add`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L462).

```lean
lemma ker_add [DecidableEq n] (hA : 0 ≤ A) (hB : 0 ≤ B) :
    (A + B).ker = A.ker ⊓ B.ker
```

**`HermitianMat.ker_sum`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L478).

```lean
lemma ker_sum [DecidableEq n] (f : ι → HermitianMat n 𝕜) (hf : ∀ i, 0 ≤ f i) :
    (∑ i, f i).ker = ⨅ i, (f i).ker
```

**`HermitianMat.ker_conj`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L500).

```lean
lemma ker_conj [DecidableEq n] (hA : 0 ≤ A) (B : Matrix n n 𝕜) :
    (A.conj B).ker = Submodule.comap (Matrix.toEuclideanLin B.conjTranspose) A.ker
```

**`HermitianMat.ker_le_of_le_smul`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L518).

```lean
lemma ker_le_of_le_smul {α : ℝ} [DecidableEq n] (hα : α ≠ 0) (hA : 0 ≤ A) (hAB : A ≤ α • B) : B.ker ≤ A.ker
```

**`HermitianMat.le_smul_one_imp_eigenvalues_le`**, a theorem, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L523). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a Hermitian matrix is bounded by `M * I`, then all its eigenvalues are at most `M`.

```lean
theorem le_smul_one_imp_eigenvalues_le [DecidableEq n] (A : HermitianMat n ℂ) (M : ℝ)
    (h : A ≤ M • (1 : HermitianMat n ℂ)) (i : n) :
    A.H.eigenvalues i ≤ M
```

**`HermitianMat.eigenvalues_le_imp_le_smul_one`**, a theorem, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L545). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If all eigenvalues of a Hermitian matrix are at most `M`, then it is bounded by `M * I`.

```lean
theorem eigenvalues_le_imp_le_smul_one [DecidableEq n] (A : HermitianMat n ℂ) (M : ℝ)
    (h : ∀ i, A.H.eigenvalues i ≤ M) :
    A ≤ M • (1 : HermitianMat n ℂ)
```

## Positivity extensions connecting HermitianMat and Matrix

**`HermitianMat.eigenvalues_nonneg`**, a theorem, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L559). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a HermitianMat is PSD, then its eigenvalues are nonneg.

```lean
theorem eigenvalues_nonneg [DecidableEq n] (hA : 0 ≤ A) (i : n) :
    0 ≤ A.H.eigenvalues i
```

**`HermitianMat.mat_nonneg`**, a theorem, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L566). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a HermitianMat is PSD, its underlying matrix is nonneg in the Loewner order.

```lean
theorem mat_nonneg (hA : 0 ≤ A) : 0 ≤ A.mat
```

**`HermitianMat.mat_pos`**, a theorem, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L572). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a HermitianMat is positive, its underlying matrix is positive in the Loewner order.

```lean
theorem mat_pos (hA : 0 < A) : 0 < A.mat
```

**`Matrix.nonneg_conjTranspose_mul_self`**, a theorem, [line 577](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L577). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `Mᴴ * M` is nonneg in the Loewner order, for any matrix `M`.

```lean
theorem _root_.Matrix.nonneg_conjTranspose_mul_self {m : Type*} [Fintype m]
    (M : Matrix m n 𝕜) : 0 ≤ M.conjTranspose * M
```

**`Matrix.nonneg_self_mul_conjTranspose`**, a theorem, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L583). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `M * Mᴴ` is nonneg in the Loewner order, for any matrix `M`.

```lean
theorem _root_.Matrix.nonneg_self_mul_conjTranspose {m : Type*} [Fintype m]
    (M : Matrix n m 𝕜) : 0 ≤ M * M.conjTranspose
```

**`HermitianMat.subtype_mk_nonneg`**, a lemma, [line 589](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L589).

```lean
lemma subtype_mk_nonneg {M : Matrix m m 𝕜} (h : 0 ≤ M) :
    0 ≤ (⟨M, (Matrix.LE.le.posSemidef h).isHermitian⟩ : HermitianMat m 𝕜)
```

**`HermitianMat.subtype_mk_pos`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L595).

```lean
lemma subtype_mk_pos {M : Matrix m m 𝕜} (h : 0 < M) :
    0 < (⟨M, (Matrix.LE.le.posSemidef h.le).isHermitian⟩ : HermitianMat m 𝕜)
```

**`HermitianMat.evalHermitianMatMat`**, a def, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L606).

> Positivity extension for `A.mat` where `A : HermitianMat`: nonneg when `0 ≤ A`.

```lean
meta def evalHermitianMatMat : PositivityExt
```

**`HermitianMat.evalHermitianMatVal`**, a def, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L617).

> Positivity extension for `A.mat` where `A : HermitianMat`: nonneg when `0 ≤ A`.

```lean
meta def evalHermitianMatVal : PositivityExt
```

**`HermitianMat.evalMatrixSelfMulConjTranspose`**, a def, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L630).

> Positivity extension for `M * Mᴴ` as a Matrix: always nonneg.

```lean
meta def evalMatrixSelfMulConjTranspose : PositivityExt
```

**`HermitianMat.evalMatrixConjTransposeMulSelf`**, a def, [line 638](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L638).

> Positivity extension for `Mᴴ * M` as a Matrix: always nonneg.

```lean
meta def evalMatrixConjTransposeMulSelf : PositivityExt
```

**`HermitianMat.evalHermitianMatMk`**, a def, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L647).

> Positivity extension for `⟨M, (pf : M.IsHermitian)⟩` as a HermitianMat:
> equivalent to `0 ≤ M` in `MatrixOrder`.

```lean
meta def evalHermitianMatMk : PositivityExt
```

**`HermitianMat.evalMatrixEigenvalues`**, a def, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean#L660).

> Positivity extension for eigenvalues of a Matrix: `0 ≤ (_ : M.IsHermitian).eigenvalues i`.
> Will try to prove `0 ≤ M` in the `MatrixOrder`. If the proof is `A.H`, i.e. M comes from a
> HermitianMat, this will give `0 ≤ A.mat` which becomes `0 ≤ A` later.

```lean
meta def evalMatrixEigenvalues : PositivityExt
```

## Depends on

- [Trace of Hermitian Matrices](trace.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Order.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Order.lean)
