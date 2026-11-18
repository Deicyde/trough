---
declaration: module
origin: cited
lean: HermitianMat.cfc_congr_of_nonneg, HermitianMat.cfc_congr_of_posDef, HermitianMat.cfc_reindex, HermitianMat.cfc_toMat_eq_sum_smul_proj, HermitianMat.mat_cfc_mul, HermitianMat.cfc_nonneg_of_nonneg, HermitianMat.continuous_cfc_fun, HermitianMat.continuousOn_cfc_fun
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.CFC

The module `QuantumInfo.ForMathlib.HermitianMat.CFC`, [QuantumInfo/ForMathlib/HermitianMat/CFC.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean): 92 declarations, 24 with a docstring, 13 listed as significant.

> Matrix operations on HermitianMats with the CFC

**`HermitianMat.isSelfAdjoint`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L32).

```lean
lemma isSelfAdjoint : IsSelfAdjoint A.mat
```

**`HermitianMat.continuousOn_finite`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L37).

```lean
lemma continuousOn_finite {α β : Type*} (f : α → β) (S : Set α)
    [TopologicalSpace α] [TopologicalSpace β] [T1Space α] [Finite S] : ContinuousOn f S
```

**`HermitianMat.conjTranspose_cfc`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L43).

```lean
lemma conjTranspose_cfc : (cfc f A.mat).conjTranspose = cfc f A.mat
```

**`HermitianMat.cfc`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L46).

```lean
protected def cfc : HermitianMat d 𝕜
```

**`HermitianMat.cfc_eq`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L49).

```lean
lemma cfc_eq : A.cfc f = ⟨cfc f A.mat, cfc_predicate f A.mat⟩
```

**`HermitianMat.mat_cfc`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L53).

```lean
lemma mat_cfc : (A.cfc f).mat = _root_.cfc f A.mat
```

**`HermitianMat.cfc_eq_cfc_iff_eqOn`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L60).

```lean
lemma cfc_eq_cfc_iff_eqOn (f g : ℝ → ℝ) :
    A.cfc f = A.cfc g ↔ Set.EqOn f g (spectrum ℝ A.mat)
```

**`HermitianMat.cfc_congr`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L65).

```lean
nonrec lemma cfc_congr (hfg : Set.EqOn f g (spectrum ℝ A.mat)) :
    A.cfc f = A.cfc g
```

**`HermitianMat.cfc_congr_of_nonneg`**, a theorem, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L71). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Version of `cfc_congr` specialized to PSD matrices.

```lean
nonrec theorem cfc_congr_of_nonneg (hA : 0 ≤ A) (hfg : Set.EqOn f g (Set.Ici 0)) :
    A.cfc f = A.cfc g
```

**`HermitianMat.cfc_congr_of_posDef`**, a theorem, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L79). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Version of `cfc_congr` specialized to positive definite matrices.

```lean
nonrec theorem cfc_congr_of_posDef (hA : A.mat.PosDef) (hfg : Set.EqOn f g (Set.Ioi 0)) :
    A.cfc f = A.cfc g
```

**`Commute.cfc_left`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L91).

```lean
lemma _root_.Commute.cfc_left (hAB : Commute A.mat B.mat) :
    Commute (A.cfc f).mat B.mat
```

**`Commute.cfc_right`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L96).

```lean
lemma _root_.Commute.cfc_right (hAB : Commute A.mat B.mat) :
    Commute A.mat (B.cfc f).mat
```

**`HermitianMat.cfc_commute`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L100).

```lean
lemma cfc_commute (f g : ℝ → ℝ) (hAB : Commute A.mat B.mat) :
    Commute (A.cfc f).mat (B.cfc g).mat
```

**`HermitianMat.cfc_self_commute`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L105).

```lean
lemma cfc_self_commute (A : HermitianMat d 𝕜) (f g : ℝ → ℝ) :
    Commute (A.cfc f).mat (A.cfc g).mat
```

**`HermitianMat.cfc_reindex`**, a theorem, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L113). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Reindexing a matrix commutes with applying the CFC.

```lean
theorem cfc_reindex (e : d ≃ d₂) : (A.reindex e).cfc f = (A.cfc f).reindex e
```

**`HermitianMat.spectrum_cfc_eq_image`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L118).

```lean
lemma spectrum_cfc_eq_image (A : HermitianMat d 𝕜) (f : ℝ → ℝ) :
    spectrum ℝ (A.cfc f).mat = f '' (spectrum ℝ A.mat)
```

**`HermitianMat.cfc_toMat_eq_sum_smul_proj`**, a theorem, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L126). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Spectral decomposition of `A.cfc f` as a sum of scaled projections (matrix version).

```lean
theorem cfc_toMat_eq_sum_smul_proj : (A.cfc f).mat =
    ∑ i, f (A.H.eigenvalues i) • (A.H.eigenvectorUnitary.val * (Matrix.single i i 1) * A.H.eigenvectorUnitary.val.conjTranspose)
```

**`HermitianMat.cfc_eigenvalues`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L147).

```lean
lemma cfc_eigenvalues (A : HermitianMat d 𝕜) :
    ∃ (e : d ≃ d), (A.cfc f).H.eigenvalues = f ∘ A.H.eigenvalues ∘ e
```

> Here we give HermitianMat versions of many cfc theorems, like `cfc_id`, `cfc_sub`, `cfc_comp`,
> etc. We need these because (as above) `HermitianMat.cfc` is different from `_root_.cfc`.

**`HermitianMat.cfc_id`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L155).

```lean
nonrec lemma cfc_id : A.cfc id = A
```

**`HermitianMat.cfc_id'`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L159).

```lean
nonrec lemma cfc_id' : A.cfc (·) = A
```

**`HermitianMat.cfc_add`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L162).

```lean
nonrec lemma cfc_add : A.cfc (f + g) = A.cfc f + A.cfc g
```

**`HermitianMat.cfc_add_apply`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L165).

```lean
lemma cfc_add_apply : A.cfc (fun x ↦ f x + g x) = A.cfc f + A.cfc g
```

**`HermitianMat.cfc_sub`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L168).

```lean
nonrec lemma cfc_sub : A.cfc (f - g) = A.cfc f - A.cfc g
```

**`HermitianMat.cfc_sub_apply`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L171).

```lean
lemma cfc_sub_apply : A.cfc (fun x ↦ f x - g x) = A.cfc f - A.cfc g
```

**`HermitianMat.cfc_neg`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L174).

```lean
nonrec lemma cfc_neg : A.cfc (-f) = -A.cfc f
```

**`HermitianMat.cfc_neg_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L177).

```lean
lemma cfc_neg_apply : A.cfc (fun x ↦ -f x) = -A.cfc f
```

**`HermitianMat.mat_cfc_mul`**, a theorem, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L184). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> We don't have a direct analog of `cfc_mul`, since we can't generally multiply
> to HermitianMat's to get another one, so the theorem statement wouldn't be well-typed.
> But, we can say that the matrices are always equal. See `cfc_conj` for the coe-free
> analog to multiplication.

```lean
theorem mat_cfc_mul : (A.cfc (f * g)).mat = A.cfc f * A.cfc g
```

**`HermitianMat.mat_cfc_mul_apply`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L188).

```lean
lemma mat_cfc_mul_apply : (A.cfc (fun x ↦ f x * g x)).mat = A.cfc f * A.cfc g
```

**`HermitianMat.cfc_comp`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L191).

```lean
nonrec lemma cfc_comp : A.cfc (g ∘ f) = (A.cfc f).cfc g
```

**`HermitianMat.cfc_comp_apply`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L194).

```lean
lemma cfc_comp_apply : A.cfc (fun x ↦ g (f x)) = (A.cfc f).cfc g
```

**`HermitianMat.cfc_conj`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L197).

```lean
nonrec lemma cfc_conj : (A.cfc f).conj (A.cfc g) = A.cfc (f * g^2)
```

**`HermitianMat.cfc_diagonal`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L204).

```lean
lemma cfc_diagonal (g : d → ℝ) : (diagonal 𝕜 g).cfc f = diagonal 𝕜 (f ∘ g)
```

**`HermitianMat.cfc_conj_unitary`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L208).

```lean
lemma cfc_conj_unitary (U : Matrix.unitaryGroup d 𝕜) :
    (A.conj U.val).cfc f = (A.cfc f).conj U
```

**`HermitianMat.cfc_const`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L214).

```lean
nonrec lemma cfc_const : (A.cfc (fun _ ↦ r)) = r • 1
```

**`HermitianMat.cfc_const_mul_id`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L221).

```lean
nonrec lemma cfc_const_mul_id : A.cfc (fun x ↦ r * x) = r • A
```

**`HermitianMat.cfc_const_mul`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L226).

```lean
nonrec lemma cfc_const_mul : A.cfc (fun x ↦ r * f x) = r • A.cfc f
```

**`HermitianMat.cfc_apply_zero`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L231).

```lean
nonrec lemma cfc_apply_zero : (0 : HermitianMat d 𝕜).cfc f = f 0 • 1
```

**`HermitianMat.cfc_apply_one`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L235).

```lean
nonrec lemma cfc_apply_one : (1 : HermitianMat d 𝕜).cfc f = f 1 • 1
```

**`HermitianMat.cfc_pow`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L238).

```lean
lemma cfc_pow {n : ℕ} : A.cfc (· ^ n) = A ^ n
```

**`HermitianMat.cfc_nonneg_iff`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L246).

```lean
lemma cfc_nonneg_iff : 0 ≤ A.cfc f ↔ ∀ i, 0 ≤ f (A.H.eigenvalues i)
```

**`HermitianMat.cfc_posDef`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L253).

```lean
lemma cfc_posDef : (A.cfc f).mat.PosDef ↔ ∀ i, 0 < f (A.H.eigenvalues i)
```

**`HermitianMat.cfc_nonneg_of_nonneg`**, a theorem, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L262). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a rael function preserves nonnegativity, the CFC preserves PSDness.

```lean
theorem cfc_nonneg_of_nonneg (hA : 0 ≤ A) (hf : ∀ i ≥ 0, 0 ≤ f i) :
    0 ≤ A.cfc f
```

**`HermitianMat.cfc_nonSingular`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L269).

```lean
lemma cfc_nonSingular (hf : ∀ i, f (A.H.eigenvalues i) ≠ 0) : NonSingular (A.cfc f)
```

**`HermitianMat.trace_mul_cfc`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L276).

```lean
lemma trace_mul_cfc (A : HermitianMat d 𝕜) (f : ℝ → ℝ) :
    (A.mat * (A.cfc f).mat).trace = ∑ i, A.H.eigenvalues i * f (A.H.eigenvalues i)
```

**`HermitianMat.norm_eq_sum_eigenvalues_sq`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L283).

```lean
lemma norm_eq_sum_eigenvalues_sq (A : HermitianMat d 𝕜) :
    ‖A‖ ^ 2 = ∑ i, (A.H.eigenvalues i)^2
```

**`HermitianMat.lt_smul_of_norm_lt`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L294).

```lean
lemma lt_smul_of_norm_lt {r : ℝ} (h : ‖A‖ ≤ r) : A ≤ r • 1
```

**`HermitianMat.ball_subset_Icc`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L314).

```lean
lemma ball_subset_Icc : Metric.ball A r ⊆ Set.Icc (A - r • 1) (A + r • 1)
```

**`HermitianMat.spectrum_subset_of_mem_Icc`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L325).

```lean
lemma spectrum_subset_of_mem_Icc (A B : HermitianMat d 𝕜) :
    ∃ a b, ∀ x, A ≤ x ∧ x ≤ B → spectrum ℝ x.mat ⊆ Set.Icc a b
```

**`HermitianMat.cfc_continuous`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L358).

```lean
protected lemma cfc_continuous {f : ℝ → ℝ} (hf : Continuous f) :
    Continuous (HermitianMat.cfc · f : HermitianMat d ℂ → HermitianMat d ℂ)
```

**`HermitianMat.Matrix.PosDef.spectrum_subset_Ioi`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L382).

```lean
lemma Matrix.PosDef.spectrum_subset_Ioi {d 𝕜 : Type*} [Fintype d] [DecidableEq d] [RCLike 𝕜]
    {A : Matrix d d 𝕜} (hA : A.PosDef) : spectrum ℝ A ⊆ Set.Ioi 0
```

**`HermitianMat.continuous_cfc_fun`**, a theorem, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L396). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If f is a continuous family of functions parameterized by x, then (fun x => A.cfc (f x)) is also continuous.

```lean
theorem continuous_cfc_fun {f : X → ℝ → ℝ} (hf : ∀ i, Continuous (f · i)) :
    Continuous (fun x ↦ A.cfc (f x))
```

**`HermitianMat.continuousOn_cfc_fun`**, a theorem, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L407). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> ContinuousOn variant for when all the matrices (A x) have a spectrum in a set T, and f is continuous on a set S.

```lean
theorem continuousOn_cfc_fun {T : Set ℝ}
  (hf : ∀ i ∈ T, ContinuousOn (f · i) S) (hA : spectrum ℝ A.mat ⊆ T) :
    ContinuousOn (fun x ↦ A.cfc (f x)) S
```

**`HermitianMat.norm_cfc_le_sqrt_card_mul_bound`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L425).

> Bound the Frobenius norm of a functional calculus application.

```lean
lemma norm_cfc_le_sqrt_card_mul_bound {A : HermitianMat d ℂ} {f : ℝ → ℝ} {C : ℝ}
    (hC : 0 ≤ C) (hf : ∀ x ∈ spectrum ℝ A.mat, ‖f x‖ ≤ C) :
    ‖A.cfc f‖ ≤ Real.sqrt (Fintype.card d) * C
```

**`HermitianMat.norm_cfc_sub_cfc_le_sqrt_card`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L449).

```lean
lemma norm_cfc_sub_cfc_le_sqrt_card {A : HermitianMat d ℂ} {f g : ℝ → ℝ} :
    ‖A.cfc f - A.cfc g‖ ≤ Real.sqrt (Fintype.card d) * ⨆ x ∈ spectrum ℝ A.mat, ‖f x - g x‖
```

**`HermitianMat.norm_cfc_sub_le_of_sup_le`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L471).

```lean
lemma norm_cfc_sub_le_of_sup_le {A : HermitianMat d ℂ} {f g : ℝ → ℝ} {T : Set ℝ} {ε : ℝ}
    (hT : spectrum ℝ A.mat ⊆ T) (hε : 0 ≤ ε) (h_sup : ∀ x ∈ T, ‖f x - g x‖ ≤ ε) :
    ‖A.cfc f - A.cfc g‖ ≤ Real.sqrt (Fintype.card d) * ε
```

**`HermitianMat.dist_lt_of_continuous'`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L482).

> If $f$ is jointly continuous on $S \times T$ and $T$ is compact, then $x \mapsto f(x, \cdot)$ is continuous into the space of bounded functions on $T$ with the uniform norm.

```lean
lemma dist_lt_of_continuous' {X : Type*} [TopologicalSpace X]
    {f : X → ℝ → ℝ} {S : Set X} {T : Set ℝ}
    (hT : IsCompact T)
    (hf : ContinuousOn (fun (p : X × ℝ) ↦ f p.1 p.2) (S ×ˢ T))
    {x₀ : X} (hx₀ : x₀ ∈ S) {ε : ℝ} (hε : 0 < ε) :
    ∃ U ∈ nhds x₀, ∀ x ∈ U ∩ S, ∀ t ∈ T, ‖f x t - f x₀ t‖ < ε
```

**`HermitianMat.continuousOn_cfc_of_compact`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L516).

> The functional calculus is continuous on matrices with spectrum in a compact set.

```lean
lemma continuousOn_cfc_of_compact {K : Set ℝ} {g : ℝ → ℝ} (hK : IsCompact K) (hg : ContinuousOn g K) :
    ContinuousOn (fun (A : HermitianMat d ℂ) ↦ A.cfc g) {A | spectrum ℝ A.mat ⊆ K}
```

**`HermitianMat.continuous_cfc_joint_compact`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L566).

```lean
lemma continuous_cfc_joint_compact {X d : Type*} [TopologicalSpace X] [Fintype d] [DecidableEq d]
  {f : X → ℝ → ℝ} {A : X → HermitianMat d ℂ} {S : Set X} {T : Set ℝ}
  (hT : IsCompact T)
  (hf : ContinuousOn (fun (p : X × ℝ) ↦ f p.1 p.2) (S ×ˢ T))
  (hA₁ : ∀ x ∈ S, spectrum ℝ (A x).mat ⊆ T)
  (hA₂ : ContinuousOn (fun x ↦ A x) S) :
    ContinuousOn (fun x ↦ (A x).cfc (f x)) S
```

**`HermitianMat.eigenvalue_norm_le`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L607).

```lean
lemma eigenvalue_norm_le (A : HermitianMat d ℂ) (i : d) :
    |A.H.eigenvalues i| ≤ ‖A‖
```

**`HermitianMat.spectrum_subset_closedBall`**, a lemma, [line 618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L618).

> The spectrum of a `HermitianMat` is contained in the closed ball of radius `‖A‖` around 0.

```lean
lemma spectrum_subset_closedBall (A : HermitianMat d ℂ) :
    spectrum ℝ A.mat ⊆ Metric.closedBall (0 : ℝ) ‖A‖
```

**`HermitianMat.spectrum_subset_of_isOpen`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L639).

```lean
lemma spectrum_subset_of_isOpen (A₀ : HermitianMat d ℂ) (U : Set ℝ)
    (hU : IsOpen U) (hAU : spectrum ℝ A₀.mat ⊆ U) :
    ∀ᶠ B in nhds A₀, spectrum ℝ B.mat ⊆ U
```

**`HermitianMat.continuousWithinAt_cfc_of_continuousOn`**, a lemma, [line 737](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L737).

```lean
lemma continuousWithinAt_cfc_of_continuousOn {T : Set ℝ} {g : ℝ → ℝ}
    {A₀ : HermitianMat d ℂ}
    (hg : ContinuousOn g T) (hA₀ : spectrum ℝ A₀.mat ⊆ T) :
    ContinuousWithinAt (fun B ↦ B.cfc g) {B | spectrum ℝ B.mat ⊆ T} A₀
```

**`HermitianMat.dist_lt_of_continuous_spectrum`**, a lemma, [line 839](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L839).

```lean
lemma dist_lt_of_continuous_spectrum {X : Type*} [TopologicalSpace X]
    {f : X → ℝ → ℝ} {A : X → HermitianMat d ℂ} {S : Set X} {T : Set ℝ}
    (hf : ContinuousOn (fun (p : X × ℝ) ↦ f p.1 p.2) (S ×ˢ T))
    (hA₁ : ∀ x ∈ S, spectrum ℝ (A x).mat ⊆ T)
    (hA₂ : ContinuousOn (fun x ↦ A x) S)
    {x₀ : X} (hx₀ : x₀ ∈ S) {ε : ℝ} (hε : 0 < ε) :
    ∃ U ∈ nhds x₀, ∀ y ∈ U ∩ S, ∀ t ∈ spectrum ℝ (A y).mat, ‖f y t - f x₀ t‖ < ε
```

**`HermitianMat.continuous_cfc_joint`**, a lemma, [line 944](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L944).

```lean
lemma continuous_cfc_joint {X d : Type*} [TopologicalSpace X] [Fintype d] [DecidableEq d]
  {f : X → ℝ → ℝ} {A : X → HermitianMat d ℂ} {S : Set X} {T : Set ℝ}
  (hf : ContinuousOn (fun (p : X × ℝ) ↦ f p.1 p.2) (S ×ˢ T))
  (hA₁ : ∀ x ∈ S, spectrum ℝ (A x).mat ⊆ T)
  (hA₂ : ContinuousOn (fun x ↦ A x) S) :
    ContinuousOn (fun x ↦ (A x).cfc (f x)) S
```

**`HermitianMat.continuousOn_cfc_fun_nonsingular`**, a theorem, [line 991](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L991). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Specialization of `continuousOn_cfc_fun` for nonsingular matrices.

```lean
theorem continuousOn_cfc_fun_nonsingular {f : X → ℝ → ℝ} {S : Set X}
  (hf : ∀ i ≠ 0, ContinuousOn (f · i) S) [NonSingular A] :
    ContinuousOn (fun x ↦ A.cfc (f x)) S
```

**`HermitianMat.continuousOn_cfc_fun_nonneg`**, a theorem, [line 1000](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1000). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Specialization of `continuousOn_cfc_fun` for positive semidefinite matrices.

```lean
theorem continuousOn_cfc_fun_nonneg {f : X → ℝ → ℝ} {S : Set X}
  (hf : ∀ i ≥ 0, ContinuousOn (f · i) S) (hA : 0 ≤ A) :
    ContinuousOn (fun x ↦ A.cfc (f x)) S
```

**`HermitianMat.continuousOn_cfc_fun_posDef`**, a theorem, [line 1011](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1011). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Specialization of `continuousOn_cfc_fun` for positive definite matrices.

```lean
theorem continuousOn_cfc_fun_posDef {f : X → ℝ → ℝ} {S : Set X}
  (hf : ∀ i > 0, ContinuousOn (f · i) S) (hA : A.mat.PosDef) :
    ContinuousOn (fun x ↦ A.cfc (f x)) S
```

**`HermitianMat.inv_cfc_eq_cfc_inv`**, a lemma, [line 1023](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1023).

> The inverse of the CFC is the CFC of the inverse function.

```lean
lemma inv_cfc_eq_cfc_inv (hf : ∀ i, f (A.H.eigenvalues i) ≠ 0) :
    (A.cfc f)⁻¹ = A.cfc (fun u ↦ (f u)⁻¹)
```

**`HermitianMat.cfc_inv`**, a lemma, [line 1049](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1049).

```lean
lemma cfc_inv [NonSingular A] : A.cfc (fun u ↦ u⁻¹) = A⁻¹
```

**`HermitianMat.integral_toMat`**, a lemma, [line 1062](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1062).

> The integral of a Hermitian matrix function commutes with `toMat`.

```lean
lemma integral_toMat (A : ℝ → HermitianMat d 𝕜) (T₁ T₂ : ℝ) {μ : Measure ℝ}
  (hA : IntervalIntegrable A μ T₁ T₂) :
    (∫ t in T₁..T₂, A t ∂μ).mat = ∫ t in T₁..T₂, (A t).mat ∂μ
```

**`HermitianMat.intervalIntegrable_sum_smul_const`**, a lemma, [line 1071](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1071).

> A sum of scaled constant matrices is integrable if the scalar functions are integrable.

```lean
lemma intervalIntegrable_sum_smul_const (T₁ T₂ : ℝ) {μ : Measure ℝ} (g : ℝ → d → ℝ)
    (P : d → Matrix d d 𝕜) (hg : ∀ i, IntervalIntegrable (fun t ↦ g t i) μ T₁ T₂) :
    IntervalIntegrable (fun t ↦ ∑ i, g t i • P i) μ T₁ T₂
```

**`HermitianMat.intervalIntegrable_toMat_iff`**, a lemma, [line 1081](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1081).

> A function to Hermitian matrices is integrable iff its matrix values are integrable.

```lean
lemma intervalIntegrable_toMat_iff (A : ℝ → HermitianMat d 𝕜) (T₁ T₂ : ℝ) {μ : Measure ℝ} :
    IntervalIntegrable (fun t ↦ (A t).mat) μ T₁ T₂ ↔ IntervalIntegrable A μ T₁ T₂
```

**`HermitianMat.integrable_cfc`**, a lemma, [line 1118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1118).

> The CFC of an integrable function family is integrable.

```lean
lemma integrable_cfc (T₁ T₂ : ℝ) (f : ℝ → ℝ → ℝ) {μ : Measure ℝ}
    (hf : ∀ i, IntervalIntegrable (fun t ↦ f t (A.H.eigenvalues i)) μ T₁ T₂) :
    IntervalIntegrable (fun t ↦ A.cfc (f t)) μ T₁ T₂
```

**`HermitianMat.integral_cfc_eq_cfc_integral`**, a lemma, [line 1131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1131).

> The integral of the CFC is the CFC of the integral.

```lean
lemma integral_cfc_eq_cfc_integral (T₁ T₂ : ℝ) {μ : Measure ℝ} (f : ℝ → ℝ → ℝ)
    (hf : ∀ i, IntervalIntegrable (fun t ↦ f t (A.H.eigenvalues i)) μ T₁ T₂) :
    ∫ t in T₁..T₂, A.cfc (f t) ∂μ = A.cfc (fun u ↦ ∫ t in T₁..T₂, f t u ∂μ)
```

**`HermitianMat.cfc_pos_of_pos`**, a lemma, [line 1146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1146).

```lean
lemma cfc_pos_of_pos {A : HermitianMat d 𝕜} {f : ℝ → ℝ} (hA : 0 < A)
    (hf : ∀ i > 0, 0 < f i) (hf₂ : 0 ≤ f 0) : 0 < A.cfc f
```

**`Commute.exists_HermitianMat_cfc`**, a theorem, [line 1168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1168). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If two matrices A and B commute, then they is a common matrix with which they are both CFCs of.
> This is a variant of the common theorem that "commuting matrices can be simultaneously diagonalized."

```lean
theorem _root_.Commute.exists_HermitianMat_cfc (hAB : Commute A.mat B.mat) :
    ∃ C : HermitianMat d 𝕜, (∃ f : ℝ → ℝ, A = C.cfc f) ∧ (∃ g : ℝ → ℝ, B = C.cfc g)
```

**`HermitianMat.cfc_le_cfc_of_PosDef`**, a lemma, [line 1184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1184).

```lean
lemma cfc_le_cfc_of_PosDef (hfg : ∀ i, 0 < i → f i ≤ g i) (hA : A.mat.PosDef) :
    A.cfc f ≤ A.cfc g
```

**`HermitianMat.cfc_le_cfc_of_commute_monoOn`**, a lemma, [line 1198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1198).

```lean
lemma cfc_le_cfc_of_commute_monoOn (hf : MonotoneOn f (Set.Ioi 0))
  (hAB₁ : Commute A.mat B.mat) (hAB₂ : A ≤ B) (hA : A.mat.PosDef) (hB : B.mat.PosDef) :
    A.cfc f ≤ B.cfc f
```

**`HermitianMat.cfc_le_cfc_of_commute`**, a theorem, [line 1215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1215). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> …

```lean
theorem cfc_le_cfc_of_commute (hf : Monotone f) (hAB₁ : Commute A.mat B.mat) (hAB₂ : A ≤ B) :
    A.cfc f ≤ B.cfc f
```

**`HermitianMat.cfc_monoOn_pos_of_monoOn_posDef`**, a lemma, [line 1229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1229).

```lean
lemma cfc_monoOn_pos_of_monoOn_posDef {d : Type*} [Fintype d] [DecidableEq d]
  {f : ℝ → ℝ} (hf_is_operator_convex : False) :
    MonotoneOn (HermitianMat.cfc · f) { A : HermitianMat d ℂ | A.mat.PosDef }
```

**`HermitianMat.inv_ge_one_of_le_one`**, a lemma, [line 1237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1237).

```lean
lemma inv_ge_one_of_le_one (hA : A.mat.PosDef) (h : A ≤ 1) : 1 ≤ A⁻¹
```

**`HermitianMat.trace_cfc_eq`**, a lemma, [line 1278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1278).

> The trace of cfc(f, A) equals the sum of f applied to eigenvalues.

```lean
lemma trace_cfc_eq (A : HermitianMat d ℂ) (f : ℝ → ℝ) :
    (A.cfc f).trace = ∑ i, f (A.H.eigenvalues i)
```

**`HermitianMat.mulVec_eq_zero_iff_inner_eigenvector_zero`**, a lemma, [line 1296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1296).

```lean
lemma mulVec_eq_zero_iff_inner_eigenvector_zero
    (A : HermitianMat d ℂ) (x : EuclideanSpace ℂ d) :
    A.mat.mulVec x = 0 ↔ ∀ i, A.H.eigenvalues i ≠ 0 → inner ℂ (A.H.eigenvectorBasis i) x = 0
```

**`HermitianMat.cfc_mulVec_expansion`**, a lemma, [line 1336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1336).

```lean
lemma cfc_mulVec_expansion (A : HermitianMat d ℂ) (f : ℝ → ℝ) (x : EuclideanSpace ℂ d) :
    (A.cfc f).mat.mulVec x = ∑ i, (f (A.H.eigenvalues i) : ℂ) • inner ℂ (A.H.eigenvectorBasis i) x • A.H.eigenvectorBasis i
```

**`HermitianMat.ker_cfc_le_ker_on_set`**, a lemma, [line 1363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1363).

```lean
lemma ker_cfc_le_ker_on_set
    (hs : spectrum ℝ A.mat ⊆ s)
    (h : ∀ i ∈ s, f i = 0 → i = 0) :
    (A.cfc f).ker ≤ A.ker
```

**`HermitianMat.ker_cfc_le_ker`**, a lemma, [line 1392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1392).

```lean
lemma ker_cfc_le_ker (h : ∀ i, f i = 0 → i = 0) :
    (A.cfc f).ker ≤ A.ker
```

**`HermitianMat.ker_cfc_le_ker_nonneg`**, a lemma, [line 1396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1396).

```lean
lemma ker_cfc_le_ker_nonneg (hA : 0 ≤ A) (h : ∀ i ≥ 0, f i = 0 → i = 0) :
    (A.cfc f).ker ≤ A.ker
```

**`HermitianMat.ker_le_ker_cfc_on_set`**, a lemma, [line 1401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1401).

```lean
lemma ker_le_ker_cfc_on_set (hs : spectrum ℝ A.mat ⊆ s) (h : ∀ i ∈ s, i = 0 → f i = 0) :
    A.ker ≤ (A.cfc f).ker
```

**`HermitianMat.ker_le_ker_cfc`**, a lemma, [line 1418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1418).

```lean
lemma ker_le_ker_cfc (h : ∀ i, i = 0 → f i = 0) :
    A.ker ≤ (A.cfc f).ker
```

**`HermitianMat.ker_le_ker_cfc_nonneg`**, a lemma, [line 1422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1422).

```lean
lemma ker_le_ker_cfc_nonneg (hA : 0 ≤ A) (h : ∀ i ≥ 0, i = 0 → f i = 0) :
    A.ker ≤ (A.cfc f).ker
```

**`HermitianMat.ker_cfc_eq_ker`**, a lemma, [line 1427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1427).

```lean
lemma ker_cfc_eq_ker (h : ∀ i, f i = 0 ↔ i = 0) :
    (A.cfc f).ker = A.ker
```

**`HermitianMat.ker_cfc_eq_ker_nonneg`**, a lemma, [line 1432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean#L1432).

```lean
lemma ker_cfc_eq_ker_nonneg (hA : 0 ≤ A) (h : ∀ i ≥ 0, f i = 0 ↔ i = 0) :
    (A.cfc f).ker = A.ker
```

## Depends on

- [Inner product of Hermitian Matrices](inner.md)
- [QuantumInfo.ForMathlib.HermitianMat.NonSingular](nonsingular.md)

## Proof depends on

- [QuantumInfo.ForMathlib.Isometry](../isometry.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/CFC.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/CFC.lean)
