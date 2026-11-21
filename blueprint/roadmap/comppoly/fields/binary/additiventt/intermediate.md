---
catalog: module
lean: AdditiveNTT.intermediateNormVpoly, AdditiveNTT.intermediateNormVpoly_eval_is_linear_map, AdditiveNTT.base_intermediateNormVpoly, AdditiveNTT.natDegree_intermediateNormVpoly, AdditiveNTT.degree_intermediateNormVpoly, AdditiveNTT.Polynomial.foldl_comp, AdditiveNTT.intermediateNormVpoly_comp_qmap, AdditiveNTT.intermediateNormVpoly_comp, AdditiveNTT.iteratedQuotientMap, AdditiveNTT.iteratedQuotientMap_congr_k, AdditiveNTT.iteratedQuotientMap_succ_comp, AdditiveNTT.qMap_eval_mem_sDomain_succ, AdditiveNTT.iteratedQuotientMap_k_eq_1_is_qMap, AdditiveNTT.getSDomainBasisCoeff_of_sum_repr, AdditiveNTT.getSDomainBasisCoeff_of_iteratedQuotientMap, AdditiveNTT.sDomain.lift, AdditiveNTT.basis_repr_of_sDomain_lift, AdditiveNTT.intermediateNormVpoly_comp_qmap_helper, AdditiveNTT.intermediateNovelBasisX, AdditiveNTT.base_intermediateNovelBasisX, AdditiveNTT.intermediateNovelBasisX_zero_eq_one, AdditiveNTT.degree_intermediateNovelBasisX, AdditiveNTT.even_index_intermediate_novel_basis_decomposition, AdditiveNTT.odd_index_intermediate_novel_basis_decomposition, AdditiveNTT.intermediateEvaluationPoly, AdditiveNTT.degree_intermediateEvaluationPoly_lt, AdditiveNTT.intermediateBasisVectors, AdditiveNTT.IntermediateCoeffVecSpace, AdditiveNTT.intermediateToCoeffsVec, AdditiveNTT.intermediateChangeOfBasisMatrix, AdditiveNTT.intermediateChangeOfBasisMatrix_lower_triangular, AdditiveNTT.intermediateChangeOfBasisMatrix_diag_ne_zero, AdditiveNTT.intermediateChangeOfBasisMatrix_det_ne_zero, AdditiveNTT.intermediateChangeOfBasisMatrix_invertible, AdditiveNTT.monomialToINovelCoeffs, AdditiveNTT.iNovelToMonomialCoeffs, AdditiveNTT.getINovelCoeffs, AdditiveNTT.monomialToINovel_iNovelToMonomial_inverse, AdditiveNTT.iNovelToMonomial_monomialToINovel_inverse, AdditiveNTT.intermediateEvaluationPoly_from_inovel_coeffs_eq_self, AdditiveNTT.evenRefinement, AdditiveNTT.oddRefinement, AdditiveNTT.evaluation_poly_split_identity, AdditiveNTT.intermediate_poly_P_base
statement: formalized
proof: formalized
---

# Additive NTT Intermediate Objects

`CompPoly.Fields.Binary.AdditiveNTT.Intermediate`, in [CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean), by Chung Thai Nguyen, Quang Dao.

> Intermediate quotient-chain polynomials, intermediate novel bases, and the
> intermediate evaluation polynomials used by the Additive NTT recursion.

> ### 2. Intermediate Novel Polynomial Bases `Xⱼ⁽ⁱ⁾`  and evaluation polynomials `P⁽ⁱ⁾`

`AdditiveNTT.intermediateNormVpoly` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L59))

> The `k`-step subspace-vanishing polynomial `Ŵₖ⁽ⁱ⁾`.
>
> `i : Fin r` is a loose index and `h_k : i + k ≤ ℓ` supplies its NTT-level bound.
> For `k = 0` this is `X`; otherwise it is `q⁽ⁱ⁺ᵏ⁻¹⁾ ∘ ⋯ ∘ q⁽ⁱ⁾`.

```lean
noncomputable def intermediateNormVpoly
    (i: Fin r) {k : ℕ} (h_k : i.val + k ≤ ℓ) : L[X]
```

`AdditiveNTT.intermediateNormVpoly_eval_is_linear_map` (lemma, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L66))

```lean
lemma intermediateNormVpoly_eval_is_linear_map (i : Fin r) {k : ℕ} (h_k : i.val + k ≤ ℓ) :
    IsLinearMap 𝔽q (fun x : L =>
      (intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate i h_k).eval x)
```

`AdditiveNTT.base_intermediateNormVpoly` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L107))

```lean
theorem base_intermediateNormVpoly
    (k : Fin r) (h_k : k.val ≤ ℓ) :
  intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate 0 (k := k)
    (h_k := by simp only [Fin.coe_ofNat_eq_mod, Nat.zero_mod, zero_add]; omega) =
  normalizedW 𝔽q β k
```

`AdditiveNTT.natDegree_intermediateNormVpoly` (lemma, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L120))

> The natDegree of `Ŵₖ⁽ⁱ⁾(X)` is `2^k`.

```lean
lemma natDegree_intermediateNormVpoly (i : Fin r) {k : ℕ} (h_k : i.val + k ≤ ℓ) :
    (intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate i (k := k) (h_k := h_k)).natDegree = 2 ^ k
```

`AdditiveNTT.degree_intermediateNormVpoly` (lemma, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L152))

> The degree of `Ŵₖ⁽ⁱ⁾(X)` is `2^k`.

```lean
lemma degree_intermediateNormVpoly (i : Fin r) {k : ℕ} (h_k : i.val + k ≤ ℓ) :
    (intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate i (k := k) (h_k := h_k)).degree = 2 ^ k
```

`AdditiveNTT.Polynomial.foldl_comp` (theorem, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L160))

```lean
theorem Polynomial.foldl_comp (n : ℕ) (f : Fin n → L[X]) : ∀ initInner initOuter: L[X],
    Fin.foldl (n:=n) (fun acc j => (f j).comp acc) (initOuter.comp initInner)
    = (Fin.foldl (n:=n) (fun acc j => (f j).comp acc) (initOuter)).comp initInner
```

`AdditiveNTT.intermediateNormVpoly_comp_qmap` (theorem, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L179))

> If `i < ℓ` and `i + k + 1 ≤ ℓ`, then
> `Ŵₖ₊₁⁽ⁱ⁾ = Ŵₖ⁽ⁱ⁺¹⁾ ∘ q⁽ⁱ⁾`.

```lean
theorem intermediateNormVpoly_comp_qmap (i : Fin r)
    {destIdx : Fin r} (h_destIdx : destIdx = i.val + 1)
    (k : ℕ) (h_k : i.val + k + 1 ≤ ℓ) :
    -- corresponds to intermediateNormVpoly_comp where `k = k, l = 1`
    intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate (i := i) (k := k + 1) (h_k := by omega)=
    (intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate (i := destIdx)
      (k := k) (h_k := by omega)).comp
        (qMap 𝔽q β i (by omega))
```

`AdditiveNTT.intermediateNormVpoly_comp` (theorem, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L203))

```lean
theorem intermediateNormVpoly_comp (i : Fin r) {destIdx : Fin r}
    {k l : ℕ} (h_destIdx : destIdx = i.val + k)
  (h_k : i.val + k ≤ ℓ) (h_l : i.val + k + l ≤ ℓ) :
  intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate (i := i) (k:=k + l) (h_k := by omega) =
    (intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate (i := destIdx) (k:=l) (h_k := by omega)).comp (
  intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate (i := i) (k:=k) (h_k := by omega))
```

`AdditiveNTT.iteratedQuotientMap` (definition, [line 243](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L243))

> Maps a point from `sDomain i` to `sDomain destIdx` by a `k`-step quotient map.
>
> `i` and `destIdx` are loose `Fin r` indices. `h_destIdx` identifies the destination
> as `i + k`, and `h_destIdx_le` supplies the NTT-level bound.

```lean
noncomputable def iteratedQuotientMap (i : Fin r) {destIdx : Fin r} {k : ℕ}
    (h_destIdx : destIdx = i.val + k) (h_destIdx_le : destIdx.val ≤ ℓ)
    (x : (sDomain 𝔽q β h_ℓ_add_R_rate) i) :
    (sDomain 𝔽q β h_ℓ_add_R_rate) destIdx
```

`AdditiveNTT.iteratedQuotientMap_congr_k` (lemma, [line 292](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L292))

```lean
lemma iteratedQuotientMap_congr_k
    (i : Fin r) {destIdx : Fin r} {k₁ k₂ : ℕ}
    (hk : k₁ = k₂)
    (h_destIdx₁ : destIdx.val = i.val + k₁)
    (h_destIdx₂ : destIdx.val = i.val + k₂)
    (h_destIdx_le : destIdx.val ≤ ℓ)
    (x : sDomain 𝔽q β h_ℓ_add_R_rate i) :
    iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate
      (i := i) (k := k₁) (h_destIdx := h_destIdx₁) (h_destIdx_le := h_destIdx_le) x
    =
    iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate
      (i := i) (k := k₂) (h_destIdx := h_destIdx₂) (h_destIdx_le := h_destIdx_le) x
```

`AdditiveNTT.iteratedQuotientMap_succ_comp` (theorem, [line 309](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L309))

> Composing one quotient step with a `steps`-step quotient map equals the
> `steps + 1` step quotient map.

```lean
theorem iteratedQuotientMap_succ_comp
    (i : Fin r) {midIdx destIdx : Fin r} (steps : ℕ)
    (h_midIdx : midIdx.val = i.val + 1)
    (h_destIdx : destIdx.val = i.val + (steps + 1))
    (h_destIdx_le : destIdx ≤ ℓ)
    (x : sDomain 𝔽q β h_ℓ_add_R_rate i) :
    iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate
      (i := i) (k := steps + 1) (h_destIdx := h_destIdx) (h_destIdx_le := h_destIdx_le) x
    =
    iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate
      (i := midIdx) (k := steps)
      (h_destIdx := by omega)
      (h_destIdx_le := h_destIdx_le)
      (iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate
        (i := i) (k := 1) (h_destIdx := h_midIdx) (h_destIdx_le := by omega) x)
```

`AdditiveNTT.qMap_eval_mem_sDomain_succ` (lemma, [line 341](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L341))

> The evaluation of qMap on an element from sDomain i belongs to sDomain (i+1).
> This is a key property that qMap maps between successive domains.

```lean
lemma qMap_eval_mem_sDomain_succ (i : Fin r) {destIdx : Fin r}
    (h_destIdx : destIdx = i.val + 1) (x : (sDomain 𝔽q β h_ℓ_add_R_rate) i) :
    (qMap 𝔽q β i (by omega)).eval (x.val : L) ∈
      sDomain 𝔽q β h_ℓ_add_R_rate destIdx
```

`AdditiveNTT.iteratedQuotientMap_k_eq_1_is_qMap` (theorem, [line 362](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L362))

> When k = 1, iteratedQuotientMap reduces to evaluating qMap directly.
> This shows that iteratedQuotientMap with k = 1 is equivalent to the single-step quotient map.

```lean
theorem iteratedQuotientMap_k_eq_1_is_qMap (i : Fin r) {destIdx : Fin r}
    (h_destIdx : destIdx = i.val + 1) (h_destIdx_le : destIdx.val ≤ ℓ)
    (x : (sDomain 𝔽q β h_ℓ_add_R_rate) i) :
    (iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate (i := i) (k := 1) (h_destIdx := h_destIdx)
      (h_destIdx_le := h_destIdx_le) x : sDomain 𝔽q β h_ℓ_add_R_rate destIdx)
    = ⟨(qMap 𝔽q β i (by omega)).eval (x.val : L),
      qMap_eval_mem_sDomain_succ 𝔽q β h_ℓ_add_R_rate i h_destIdx x⟩
```

`AdditiveNTT.getSDomainBasisCoeff_of_sum_repr` (lemma, [line 382](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L382))

```lean
lemma getSDomainBasisCoeff_of_sum_repr [NeZero R_rate] (i : Fin r) (h_i : i ≤ ℓ)
    (x : (sDomain 𝔽q β h_ℓ_add_R_rate) ⟨i, by omega⟩)
    (x_coeffs : Fin (ℓ + R_rate - i) → 𝔽q)
    (hx : x = ∑ j_x, (x_coeffs j_x) • (sDomain_basis 𝔽q β
      h_ℓ_add_R_rate (i := ⟨i, by omega⟩) (h_i := by
        simp only; apply Nat.lt_add_of_pos_right_of_le; omega) j_x).val) :
    ∀ (j: Fin (ℓ + R_rate - i)), ((sDomain_basis 𝔽q β
      h_ℓ_add_R_rate (i := ⟨i, by omega⟩) (h_i := by
        simp only; apply Nat.lt_add_of_pos_right_of_le; omega)).repr x) j = x_coeffs j
```

`AdditiveNTT.getSDomainBasisCoeff_of_iteratedQuotientMap` (lemma, [line 456](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L456))

```lean
lemma getSDomainBasisCoeff_of_iteratedQuotientMap
    [NeZero R_rate] (i : Fin r) (k : ℕ)
    {destIdx : Fin r} (h_destIdx : destIdx = i.val + k) (h_destIdx_le : destIdx.val ≤ ℓ)
    (x : (sDomain 𝔽q β h_ℓ_add_R_rate) i) :
    let y : (sDomain 𝔽q β h_ℓ_add_R_rate destIdx) := iteratedQuotientMap 𝔽q β h_ℓ_add_R_rate
      (i := i) (k:=k) (h_destIdx:=h_destIdx) (h_destIdx_le:=h_destIdx_le) (x:=x)
    ∀ (j: Fin (ℓ + R_rate - destIdx)),
    ((sDomain_basis 𝔽q β h_ℓ_add_R_rate (i := destIdx) (h_i := by
      apply Nat.lt_add_of_pos_right_of_le; omega)).repr y) j =
    ((sDomain_basis 𝔽q β h_ℓ_add_R_rate (i := i)
      (h_i := by apply Nat.lt_add_of_pos_right_of_le; omega)).repr x) ⟨j + k, by omega⟩
```

`AdditiveNTT.sDomain.lift` (definition, [line 591](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L591))

> Lifts a point `y` from a higher-indexed domain `sDomain j` to the canonical
> base point of its fiber in a lower-indexed domain `sDomain i`,
> by retaining all coeffs for the corresponding basis elements

```lean
noncomputable def sDomain.lift (i j : Fin r) (h_j : j < ℓ + R_rate) (h_le : i ≤ j)
    (y : sDomain 𝔽q β h_ℓ_add_R_rate j) :
    sDomain 𝔽q β h_ℓ_add_R_rate i
```

`AdditiveNTT.basis_repr_of_sDomain_lift` (theorem, [line 606](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L606))

> Applying the forward map to a lifted point returns the original point.

```lean
theorem basis_repr_of_sDomain_lift (i j : Fin r) (h_j : j < ℓ + R_rate) (h_le : i ≤ j)
    (y : sDomain 𝔽q β h_ℓ_add_R_rate (i := j)) :
    let x₀ := sDomain.lift 𝔽q β h_ℓ_add_R_rate i j (by omega) (by omega) y
    ∀ k: Fin (ℓ + R_rate - i),
      (sDomain_basis 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega)).repr x₀ k =
        if hk: k < (j.val - i.val) then 0
        else (sDomain_basis 𝔽q β h_ℓ_add_R_rate (i := j)
          (h_i := by omega)).repr y ⟨k - (j.val - i.val), by omega⟩
```

`AdditiveNTT.intermediateNormVpoly_comp_qmap_helper` (theorem, [line 622](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L622))

> A helper form of `intermediateNormVpoly_comp_qmap` for the strict stage
> `i < ℓ` and the remaining basis index `k`.

```lean
theorem intermediateNormVpoly_comp_qmap_helper (i : Fin r) (h_i : i < ℓ)
    (k : Fin (ℓ - (↑i + 1))) :
    (intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate
      ⟨↑i + 1, by omega⟩ (k:=k) (h_k := by simp only; omega)).comp
        (qMap 𝔽q β ⟨↑i, by omega⟩ (by change i.val + 1 < r; omega)) =
    intermediateNormVpoly 𝔽q β h_ℓ_add_R_rate
      ⟨↑i, by omega⟩ (k:=k + 1) (h_k := by simp only; omega)
```

`AdditiveNTT.intermediateNovelBasisX` (definition, [line 635](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L635))

> ∀ `i` ∈ {0, ..., ℓ}, The `i`-th order novel polynomial basis `Xⱼ⁽ⁱ⁾`.
> `Xⱼ⁽ⁱ⁾ := Π_{k=0}^{ℓ-i-1} (Ŵₖ⁽ⁱ⁾)^{jₖ}`, ∀ j ∈ {0, ..., 2^(ℓ-i)-1}

```lean
noncomputable def intermediateNovelBasisX (i : Fin r) (h_i : i ≤ ℓ)
    (j : Fin (2 ^ (ℓ - i))) : L[X]
```

`AdditiveNTT.base_intermediateNovelBasisX` (theorem, [line 643](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L643))

```lean
theorem base_intermediateNovelBasisX (j : Fin (2 ^ ℓ)) :
    intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate 0 (h_i := by simp only [Fin.coe_ofNat_eq_mod,
      Nat.zero_mod, zero_le]) j =
    Xⱼ 𝔽q β ℓ (by omega) j
```

`AdditiveNTT.intermediateNovelBasisX_zero_eq_one` (lemma, [line 657](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L657))

```lean
lemma intermediateNovelBasisX_zero_eq_one (i : Fin r) (h_i : i ≤ ℓ) :
    intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate i h_i ⟨0, by
      exact Nat.two_pow_pos (ℓ - ↑i)⟩ = 1
```

`AdditiveNTT.degree_intermediateNovelBasisX` (lemma, [line 667](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L667))

> The degree of an `i`-th order novel polynomial basis element `Xⱼ⁽ⁱ⁾(X)` is exactly `j`.
> Somewhat similar to proof of `degree_Xⱼ`.

```lean
lemma degree_intermediateNovelBasisX (i : Fin r) (h_i : i ≤ ℓ) (j : Fin (2 ^ (ℓ - i))) :
    (intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := h_i) (j := j)).degree = j
```

`AdditiveNTT.even_index_intermediate_novel_basis_decomposition` (lemma, [line 713](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L713))

> `X₂ⱼ⁽ⁱ⁾ = Xⱼ⁽ⁱ⁺¹⁾(q⁽ⁱ⁾(X))` for `i < ℓ` and
> `j < 2^(ℓ - i - 1)`.

```lean
lemma even_index_intermediate_novel_basis_decomposition (i : Fin r)
    (h_i : i < ℓ) (j : Fin (2 ^ (ℓ - i - 1))) :
  intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega) ⟨j * 2, by
    apply mul_two_add_bit_lt_two_pow j (ℓ-i-1) (ℓ-i) ⟨0, by omega⟩ (by omega) (by omega)
  ⟩  = (intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate (i := ⟨i.val+1, by omega⟩)
    (h_i := by simp only; omega) ⟨j, by
    apply lt_two_pow_of_lt_two_pow_exp_le j (ℓ-i-1) (ℓ-(i+1)) (by omega) (by omega)
  ⟩).comp (qMap 𝔽q β i (by omega))
```

`AdditiveNTT.odd_index_intermediate_novel_basis_decomposition` (lemma, [line 768](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L768))

> `X₂ⱼ₊₁⁽ⁱ⁾ = X * Xⱼ⁽ⁱ⁺¹⁾(q⁽ⁱ⁾(X))` for `i < ℓ` and
> `j < 2^(ℓ - i - 1)`.

```lean
lemma odd_index_intermediate_novel_basis_decomposition
    (i : Fin r) (h_i : i < ℓ) (j : Fin (2 ^ (ℓ - i - 1))) :
    intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega) ⟨j * 2 + 1, by
      apply mul_two_add_bit_lt_two_pow j (ℓ-i-1) (ℓ-i) ⟨1, by omega⟩ (by omega) (by omega)
    ⟩  = X * (intermediateNovelBasisX 𝔽q β h_ℓ_add_R_rate (i := ⟨i.val+1, by omega⟩)
    (h_i := by simp only; omega) ⟨j, by
      apply lt_two_pow_of_lt_two_pow_exp_le j (ℓ-i-1) (ℓ-(i+1)) (by omega) (by omega)
    ⟩).comp (qMap 𝔽q β i (by omega))
```

`AdditiveNTT.intermediateEvaluationPoly` (definition, [line 830](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L830))

> ∀ `i` ∈ {0, ..., ℓ}, The `i`-th order evaluation polynomial
> `P⁽ⁱ⁾(X) := ∑_{j=0}^{2^(ℓ-i)-1} coeffsⱼ ⋅ Xⱼ⁽ⁱ⁾(X)` over the domain `S⁽ⁱ⁾`.
>   where the polynomial `P⁽⁰⁾(X)` over the domain `S⁽⁰⁾` is exactly the original
>   polynomial `P(X)` we need to evaluate,
>   and `coeffs` is the list of `2^(ℓ-i)` coefficients of the polynomial.

```lean
noncomputable def intermediateEvaluationPoly (i : Fin r) (h_i : i ≤ ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) : L[X]
```

`AdditiveNTT.degree_intermediateEvaluationPoly_lt` (lemma, [line 836](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L836))

```lean
lemma degree_intermediateEvaluationPoly_lt (i : Fin r) (h_i : i ≤ ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) :
  (intermediateEvaluationPoly 𝔽q β h_ℓ_add_R_rate i h_i coeffs).degree < 2 ^ (ℓ - i)
```

`AdditiveNTT.intermediateBasisVectors` (definition, [line 864](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L864))

> The basis vectors for the intermediate level `i`.

```lean
noncomputable def intermediateBasisVectors (i : Fin r) (h_i : i ≤ ℓ) :
  Fin (2 ^ (ℓ - i)) → L⦃<2^(ℓ - i)⦄[X]
```

`AdditiveNTT.IntermediateCoeffVecSpace` (abbreviation, [line 875](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L875))

> The vector space of coefficients for polynomials of degree < 2^(ℓ-i).

```lean
abbrev IntermediateCoeffVecSpace (i : Fin r)
```

`AdditiveNTT.intermediateToCoeffsVec` (definition, [line 878](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L878))

> The linear map from polynomials (in the subtype) to their coefficient vectors at level `i`.

```lean
def intermediateToCoeffsVec (i : Fin r) : -- (h_i : i ≤ ℓ)
    L⦃<2^(ℓ - i)⦄[X] →ₗ[L] IntermediateCoeffVecSpace (L := L) (ℓ := ℓ) i
```

`AdditiveNTT.intermediateChangeOfBasisMatrix` (definition, [line 886](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L886))

> The Change-of-Basis Matrix from the Intermediate Novel Basis to the Monomial Basis.
> A_jk = coeff of X^k in intermediate basis vector X_j.

```lean
noncomputable def intermediateChangeOfBasisMatrix (i : Fin r) (h_i : i ≤ ℓ) :
    Matrix (Fin (2 ^ (ℓ - i))) (Fin (2 ^ (ℓ - i))) L
```

`AdditiveNTT.intermediateChangeOfBasisMatrix_lower_triangular` (theorem, [line 892](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L892))

```lean
theorem intermediateChangeOfBasisMatrix_lower_triangular (i : Fin r) (h_i : i ≤ ℓ) :
    (intermediateChangeOfBasisMatrix 𝔽q β h_ℓ_add_R_rate i h_i).BlockTriangular
      ⇑OrderDual.toDual
```

`AdditiveNTT.intermediateChangeOfBasisMatrix_diag_ne_zero` (theorem, [line 906](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L906))

```lean
theorem intermediateChangeOfBasisMatrix_diag_ne_zero (i : Fin r) (h_i : i ≤ ℓ) :
    (∀ j, (intermediateChangeOfBasisMatrix 𝔽q β h_ℓ_add_R_rate i h_i) j j ≠ 0)
```

`AdditiveNTT.intermediateChangeOfBasisMatrix_det_ne_zero` (theorem, [line 915](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L915))

```lean
theorem intermediateChangeOfBasisMatrix_det_ne_zero (i : Fin r) (h_i : i ≤ ℓ) :
    (intermediateChangeOfBasisMatrix 𝔽q β h_ℓ_add_R_rate i h_i).det ≠ 0
```

`AdditiveNTT.intermediateChangeOfBasisMatrix_invertible` (definition, [line 925](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L925))

> The intermediate change-of-basis matrix is invertible.

```lean
noncomputable def intermediateChangeOfBasisMatrix_invertible
    (i : Fin r) (h_i : i ≤ ℓ) :
    Invertible (intermediateChangeOfBasisMatrix 𝔽q β h_ℓ_add_R_rate i h_i)
```

`AdditiveNTT.monomialToINovelCoeffs` (definition, [line 933](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L933))

> Convert monomial coefficients to novel coefficients at level `i`.
> n = m * A⁻¹

```lean
noncomputable def monomialToINovelCoeffs (i : Fin r) (h_i : i ≤ ℓ)
    (monomial_coeffs : Fin (2 ^ (ℓ - i)) → L) : Fin (2 ^ (ℓ - i)) → L
```

`AdditiveNTT.iNovelToMonomialCoeffs` (definition, [line 941](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L941))

> Convert novel coefficients to monomial coefficients at level `i`.
> m = n * A

```lean
noncomputable def iNovelToMonomialCoeffs (i : Fin r) (h_i : i ≤ ℓ)
    (novel_coeffs : Fin (2 ^ (ℓ - i)) → L) : Fin (2 ^ (ℓ - i)) → L
```

`AdditiveNTT.getINovelCoeffs` (definition, [line 946](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L946))

```lean
noncomputable def getINovelCoeffs (i : Fin r) (h_i : i ≤ ℓ)
    (P : L[X]) : Fin (2 ^ (ℓ - i.val)) → L
```

`AdditiveNTT.monomialToINovel_iNovelToMonomial_inverse` (theorem, [line 953](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L953))

> Round trip inverse property: Monomial -> Novel -> Monomial

```lean
theorem monomialToINovel_iNovelToMonomial_inverse (i : Fin r) (h_i : i ≤ ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) :
    iNovelToMonomialCoeffs 𝔽q β h_ℓ_add_R_rate i h_i
      (monomialToINovelCoeffs 𝔽q β h_ℓ_add_R_rate i h_i coeffs) = coeffs
```

`AdditiveNTT.iNovelToMonomial_monomialToINovel_inverse` (theorem, [line 965](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L965))

```lean
theorem iNovelToMonomial_monomialToINovel_inverse (i : Fin r) (h_i : i ≤ ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) :
    monomialToINovelCoeffs 𝔽q β h_ℓ_add_R_rate i h_i
      (iNovelToMonomialCoeffs 𝔽q β h_ℓ_add_R_rate i h_i coeffs) = coeffs
```

`AdditiveNTT.intermediateEvaluationPoly_from_inovel_coeffs_eq_self` (lemma, [line 983](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L983))

> **Reconstruction Lemma**:
> If `P` has degree < 2^(ℓ-i), and we convert its coefficients to the intermediate novel basis,
> the resulting `intermediateEvaluationPoly` is exactly `P`.

```lean
lemma intermediateEvaluationPoly_from_inovel_coeffs_eq_self
    (i : Fin r) (h_i : i ≤ ℓ) (P : L[X])
    (hP_deg : P.degree < 2 ^ (ℓ - i.val)) :
    intermediateEvaluationPoly 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := h_i)
      (coeffs := getINovelCoeffs 𝔽q β h_ℓ_add_R_rate i h_i P) = P
```

`AdditiveNTT.evenRefinement` (definition, [line 1055](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L1055))

> The even and odd refinements of `P⁽ⁱ⁾(X)` which are polynomials in the `(i+1)`-th basis.
> `P₀⁽ⁱ⁺¹⁾(Y) = ∑_{j=0}^{2^{ℓ-i-1}-1} a_{2j} ⋅ Xⱼ⁽ⁱ⁺¹⁾(Y)`
> `P₁⁽ⁱ⁺¹⁾(Y) = ∑_{j=0}^{2^{ℓ-i-1}-1} a_{2j+1} ⋅ Xⱼ⁽ⁱ⁺¹⁾(Y)`

```lean
noncomputable def evenRefinement (i : Fin r) (h_i : i < ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) : L[X]
```

`AdditiveNTT.oddRefinement` (definition, [line 1063](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L1063))

```lean
noncomputable def oddRefinement (i : Fin r) (h_i : i < ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) : L[X]
```

`AdditiveNTT.evaluation_poly_split_identity` (theorem, [line 1076](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L1076))

> **Key Polynomial Identity (Equation 39)**. This identity is the foundation for the
> butterfly operation in the Additive NTT. It relates a polynomial in the `i`-th basis to
> its even and odd parts expressed in the `(i+1)`-th basis via the quotient map `q⁽ⁱ⁾`.
> `∀ i ∈ {0, ..., ℓ-1}, P⁽ⁱ⁾(X) = P₀⁽ⁱ⁺¹⁾(q⁽ⁱ⁾(X)) + X ⋅ P₁⁽ⁱ⁺¹⁾(q⁽ⁱ⁾(X))`

```lean
theorem evaluation_poly_split_identity (i : Fin r) (h_i : i < ℓ)
    (coeffs : Fin (2 ^ (ℓ - i)) → L) :
  let P_i: L[X] := intermediateEvaluationPoly 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega) coeffs
  let P_even_i_plus_1: L[X] := evenRefinement 𝔽q β h_ℓ_add_R_rate i h_i coeffs
  let P_odd_i_plus_1: L[X] := oddRefinement 𝔽q β h_ℓ_add_R_rate i h_i coeffs
  let q_i: L[X] := qMap 𝔽q β i (by omega)
  P_i = (P_even_i_plus_1.comp q_i) + X * (P_odd_i_plus_1.comp q_i)
```

`AdditiveNTT.intermediate_poly_P_base` (lemma, [line 1218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean#L1218))

```lean
lemma intermediate_poly_P_base (h_ℓ : ℓ ≤ r) (coeffs : Fin (2 ^ ℓ) → L) :
    intermediateEvaluationPoly 𝔽q β h_ℓ_add_R_rate (i := 0)
    (h_i := by simp only [Fin.coe_ofNat_eq_mod, Nat.zero_mod, zero_le]) coeffs =
    polynomialFromNovelCoeffs 𝔽q β ℓ h_ℓ coeffs
```

## Depends on

- [Additive NTT Domains](domain.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Intermediate.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Intermediate.json)
