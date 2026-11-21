---
catalog: module
lean: AdditiveNTT.run_foldlM_modify_eq_foldl, AdditiveNTT.bitsToU_bijective, AdditiveNTT.evalWAt_eq_W, AdditiveNTT.evalNormalizedWAt_eq_normalizedW, AdditiveNTT.computableTwiddleFactor_eq_twiddleFactor, AdditiveNTT.computableNTTStage_eq_NTTStage, AdditiveNTT.W_eval_succ_eq_mul_add, AdditiveNTT.evalWAtCachedConstantsLoop_eq_W_of_correct, AdditiveNTT.evalWAtCachedConstants_eq_W_of_correct, AdditiveNTT.subspacePolynomialConstantsArrayLoop_spec, AdditiveNTT.subspacePolynomialConstantsArrayLoop_size, AdditiveNTT.subspacePolynomialConstantsArray_size, AdditiveNTT.subspacePolynomialConstantsArray_getD, AdditiveNTT.evalWAtCachedConstants_subspacePolynomialConstantsArray_eq_W, AdditiveNTT.computableNormalizedWValuesArray_getD, AdditiveNTT.computableTwiddleTableArray_getD, AdditiveNTT.arrayToFinFunction_tileCoeffsArray, AdditiveNTT.computableNTTStageArray_eq_computableNTTStage, AdditiveNTT.computableAdditiveNTT_eq_additiveNTT, AdditiveNTT.computableAdditiveNTTFastAction_run_eq_fold, AdditiveNTT.computableAdditiveNTTFast_eq_computableAdditiveNTT, AdditiveNTT.computableAdditiveNTTFast_eq_additiveNTT, AdditiveNTT.initial_tiled_coeffs_correctness, AdditiveNTT.NTTStage_correctness, AdditiveNTT.foldl_NTTStage_inductive_aux, AdditiveNTT.additiveNTT_correctness
statement: formalized
proof: formalized
---

# Additive NTT Correctness

`CompPoly.Fields.Binary.AdditiveNTT.Correctness`, in [CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean), by Chung Thai Nguyen, Quang Dao.

> The stage-wise correctness argument and the final correctness theorem for the
> Additive NTT.

`AdditiveNTT.run_foldlM_modify_eq_foldl` (lemma, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L29))

> Running a state fold made only of state updates gives the same final state as
> the corresponding pure fold.

```lean
lemma run_foldlM_modify_eq_foldl {σ : Type} (n : Nat) (f : σ → Fin n → σ) (init : σ) :
    ((Fin.foldlM (m := StateM σ) (n := n)
      (f := fun (_ : Unit) i => do
        modifyThe σ fun current => f current i
        pure ()) (init := ())).run init).2 =
      Fin.foldl n f init
```

`AdditiveNTT.bitsToU_bijective` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L61))

> The `bitsToU` mapping is a bijection: showing that iterating bits corresponds
> exactly to the linear span.

```lean
theorem bitsToU_bijective (i : Fin r) :
    Function.Bijective (bitsToU (𝔽q := 𝔽q) (β := β) (ℓ := ℓ) (R_rate := R_rate) i)
```

`AdditiveNTT.evalWAt_eq_W` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L139))

> Prove that `evalWAt` equals the standard definition of `W_i(x)`.

```lean
theorem evalWAt_eq_W (i : Fin r) (x : L) :
    evalWAt (β := β) (ℓ := ℓ) (R_rate := R_rate) (i := i) x =
    (W (𝔽q := 𝔽q) (β := β) (i := i)).eval x
```

`AdditiveNTT.evalNormalizedWAt_eq_normalizedW` (theorem, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L177))

> Prove that `evalNormalizedWAt` equals the standard definition of `Ŵ_i(x)`.

```lean
theorem evalNormalizedWAt_eq_normalizedW (i : Fin r) (x : L) :
    evalNormalizedWAt (β := β) (ℓ := ℓ) (R_rate := R_rate) (i := i) x
    = (normalizedW (𝔽q := 𝔽q) (β := β) (i := i)).eval x
```

`AdditiveNTT.computableTwiddleFactor_eq_twiddleFactor` (theorem, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L191))

> Prove that `computableTwiddleFactor` equals the standard definition of `twiddleFactor`.

```lean
theorem computableTwiddleFactor_eq_twiddleFactor (i : Fin ℓ) :
    computableTwiddleFactor (r := r) (ℓ := ℓ) (β := β) (L := L)
    (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := ⟨i, by omega⟩) =
  twiddleFactor (𝔽q := 𝔽q) (L := L) (β := β) (h_ℓ_add_R_rate := h_ℓ_add_R_rate)
    (i := ⟨i, by omega⟩) (h_i := by exact i.isLt)
```

`AdditiveNTT.computableNTTStage_eq_NTTStage` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L202))

> Prove that `computableNTTStage` equals the standard definition of `NTTStage`.

```lean
theorem computableNTTStage_eq_NTTStage (i : Fin ℓ) :
    computableNTTStage (𝔽q := 𝔽q) (r := r) (L := L) (ℓ := ℓ) (β := β) (R_rate := R_rate)
    (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := ⟨i, by omega⟩) =
  NTTStage (𝔽q := 𝔽q) (L := L) (β := β) (h_ℓ_add_R_rate := h_ℓ_add_R_rate)
    (i := ⟨i, by omega⟩) (h_i := by exact i.isLt)
```

`AdditiveNTT.W_eval_succ_eq_mul_add` (lemma, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L215))

> In the binary-field setting, the subspace vanishing polynomials satisfy the
> runtime recurrence used by `evalWAtCachedConstants`.

```lean
lemma W_eval_succ_eq_mul_add (i : Fin r) (h_i_add_1 : i + 1 < r) (x : L) :
    (W (𝔽q := 𝔽q) (β := β) (i := i + 1)).eval x =
      (W (𝔽q := 𝔽q) (β := β) (i := i)).eval x *
        ((W (𝔽q := 𝔽q) (β := β) (i := i)).eval x +
          (W (𝔽q := 𝔽q) (β := β) (i := i)).eval (β i))
```

`AdditiveNTT.evalWAtCachedConstantsLoop_eq_W_of_correct` (lemma, [line 236](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L236))

> The cached evaluator computes `W_i(x)` when the cache stores exactly
> `W_k(β_k)` for `k < i`. This is stated for the internal loop so later proofs can
> resume from a partially consumed cache.

```lean
lemma evalWAtCachedConstantsLoop_eq_W_of_correct (constants : Array L) (i : Fin r)
    (j : Nat) (x acc : L)
    (hsize : constants.size = i.val) (hj_le : j ≤ i.val) (hj_lt_r : j < r)
    (hacc : acc = (W (𝔽q := 𝔽q) (β := β) (i := ⟨j, hj_lt_r⟩)).eval x)
    (hcorrect : ∀ k, j ≤ k → (hki : k < i.val) →
      constants.getD k 0 =
        (W (𝔽q := 𝔽q) (β := β) (i := ⟨k, Nat.lt_trans hki i.isLt⟩)).eval
          (β ⟨k, Nat.lt_trans hki i.isLt⟩)) :
    evalWAtCachedConstantsLoop constants j acc =
      (W (𝔽q := 𝔽q) (β := β) (i := i)).eval x
```

`AdditiveNTT.evalWAtCachedConstants_eq_W_of_correct` (lemma, [line 277](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L277))

> The cached evaluator computes `W_i(x)` from a complete cache for stage `i`.

```lean
lemma evalWAtCachedConstants_eq_W_of_correct (constants : Array L) (i : Fin r) (x : L)
    (hsize : constants.size = i.val)
    (hcorrect : ∀ k, (hki : k < i.val) →
      constants.getD k 0 =
        (W (𝔽q := 𝔽q) (β := β) (i := ⟨k, Nat.lt_trans hki i.isLt⟩)).eval
          (β ⟨k, Nat.lt_trans hki i.isLt⟩)) :
    evalWAtCachedConstants constants x =
      (W (𝔽q := 𝔽q) (β := β) (i := i)).eval x
```

`AdditiveNTT.subspacePolynomialConstantsArrayLoop_spec` (lemma, [line 299](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L299))

> The constants-array builder preserves the invariant that entry `k` stores
> `W_k(β_k)`, and finishes with one entry for every `k < i`.

```lean
lemma subspacePolynomialConstantsArrayLoop_spec (i : Fin r) (k : Nat) (constants : Array L)
    (hsize : constants.size = k) (hk_le : k ≤ i.val)
    (hcorrect : ∀ m, (hmk : m < k) →
      constants.getD m 0 =
        (W (𝔽q := 𝔽q) (β := β) (i := ⟨m, by omega⟩)).eval (β ⟨m, by omega⟩)) :
    let result := subspacePolynomialConstantsArrayLoop (β := β) (ℓ := ℓ)
      (R_rate := R_rate) i k constants
    result.size = i.val ∧
      ∀ m, (hmi : m < i.val) →
        result.getD m 0 =
          (W (𝔽q := 𝔽q) (β := β) (i := ⟨m, Nat.lt_trans hmi i.isLt⟩)).eval
            (β ⟨m, Nat.lt_trans hmi i.isLt⟩)
```

`AdditiveNTT.subspacePolynomialConstantsArrayLoop_size` (lemma, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L353))

```lean
lemma subspacePolynomialConstantsArrayLoop_size (i : Fin r) (k : Nat) (constants : Array L)
    (hsize : constants.size = k) (hk_le : k ≤ i.val) :
    (subspacePolynomialConstantsArrayLoop (β := β) (ℓ := ℓ)
      (R_rate := R_rate) i k constants).size = i.val
```

`AdditiveNTT.subspacePolynomialConstantsArray_size` (lemma, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L378))

```lean
lemma subspacePolynomialConstantsArray_size (i : Fin r) :
    (subspacePolynomialConstantsArray (β := β) (ℓ := ℓ) (R_rate := R_rate) i).size =
      i.val
```

`AdditiveNTT.subspacePolynomialConstantsArray_getD` (lemma, [line 386](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L386))

```lean
lemma subspacePolynomialConstantsArray_getD (i : Fin r) (m : Nat) (hm : m < i.val) :
    (subspacePolynomialConstantsArray (β := β) (ℓ := ℓ) (R_rate := R_rate) i).getD m 0 =
      (W (𝔽q := 𝔽q) (β := β) (i := ⟨m, Nat.lt_trans hm i.isLt⟩)).eval
        (β ⟨m, Nat.lt_trans hm i.isLt⟩)
```

`AdditiveNTT.evalWAtCachedConstants_subspacePolynomialConstantsArray_eq_W` (lemma, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L395))

```lean
lemma evalWAtCachedConstants_subspacePolynomialConstantsArray_eq_W (i : Fin r) (x : L) :
    evalWAtCachedConstants
      (subspacePolynomialConstantsArray (β := β) (ℓ := ℓ) (R_rate := R_rate) i) x =
      (W (𝔽q := 𝔽q) (β := β) (i := i)).eval x
```

`AdditiveNTT.computableNormalizedWValuesArray_getD` (lemma, [line 407](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L407))

```lean
lemma computableNormalizedWValuesArray_getD (i : Fin ℓ)
    (k : Fin (ℓ + R_rate - i - 1)) :
    (computableNormalizedWValuesArray (β := β) (ℓ := ℓ) (R_rate := R_rate)
      (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := i)).getD k.val 0 =
      (normalizedW (𝔽q := 𝔽q) (β := β) (i := ⟨i, by omega⟩)).eval
        (β ⟨i + 1 + k.val, by omega⟩)
```

`AdditiveNTT.computableTwiddleTableArray_getD` (lemma, [line 422](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L422))

```lean
lemma computableTwiddleTableArray_getD (i : Fin ℓ)
    (u : Fin (2 ^ (ℓ + R_rate - i - 1))) :
    (computableTwiddleTableArray (β := β) (ℓ := ℓ) (R_rate := R_rate)
      (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := i)).getD u.val 0 =
      twiddleFactor (𝔽q := 𝔽q) (L := L) (ℓ := ℓ) (R_rate := R_rate)
        (β := β) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := ⟨i, by omega⟩)
        (h_i := by exact i.isLt) (u := u)
```

`AdditiveNTT.arrayToFinFunction_tileCoeffsArray` (lemma, [line 440](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L440))

```lean
lemma arrayToFinFunction_tileCoeffsArray (a : Fin (2 ^ ℓ) → L) :
    arrayToFinFunction (2 ^ (ℓ + R_rate))
      (tileCoeffsArray (L := L) (ℓ := ℓ) R_rate a) =
      tileCoeffs (L := L) (ℓ := ℓ) (R_rate := R_rate) a
```

`AdditiveNTT.computableNTTStageArray_eq_computableNTTStage` (lemma, [line 449](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L449))

```lean
lemma computableNTTStageArray_eq_computableNTTStage (i : Fin ℓ) (b : Array L) :
    arrayToFinFunction (2 ^ (ℓ + R_rate))
        (computableNTTStageArray (L := L) (ℓ := ℓ) (R_rate := R_rate)
          (i := i)
          (twiddles := computableTwiddleTableArray (β := β) (ℓ := ℓ)
            (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := i)) b) =
      computableNTTStage (𝔽q := 𝔽q) (r := r) (L := L) (ℓ := ℓ) (R_rate := R_rate)
        (β := β) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := ⟨i, by omega⟩)
        (b := arrayToFinFunction (2 ^ (ℓ + R_rate)) b)
```

`AdditiveNTT.computableAdditiveNTT_eq_additiveNTT` (theorem, [line 495](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L495))

> The proof-oriented computable additive NTT agrees with the abstract
> additive NTT specification.

```lean
theorem computableAdditiveNTT_eq_additiveNTT (a : Fin (2 ^ ℓ) → L) :
    computableAdditiveNTT (𝔽q := 𝔽q) (L := L) (r := r) (β := β)
      (ℓ := ℓ) (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (a := a) =
    additiveNTT (𝔽q := 𝔽q) (L := L) (β := β)
      (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (a := a)
```

`AdditiveNTT.computableAdditiveNTTFastAction_run_eq_fold` (lemma, [line 509](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L509))

```lean
lemma computableAdditiveNTTFastAction_run_eq_fold (a : Fin (2 ^ ℓ) → L) :
    ((computableAdditiveNTTFastAction (L := L) (r := r) (β := β)
      (ℓ := ℓ) (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) a).run #[]).1 =
    Fin.foldl (n := ℓ) (fun current i =>
      let stage : Fin ℓ := ⟨ℓ - i - 1, by omega⟩
      let twiddles := computableTwiddleTableArray (β := β) (ℓ := ℓ)
        (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (i := stage)
      computableNTTStageArray (ℓ := ℓ) (R_rate := R_rate)
        (i := stage) (twiddles := twiddles) current)
      (tileCoeffsArray (L := L) (ℓ := ℓ) R_rate a)
```

`AdditiveNTT.computableAdditiveNTTFast_eq_computableAdditiveNTT` (theorem, [line 554](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L554))

> The fast additive NTT array implementation is extensionally equal to the
> proof-oriented computable implementation after converting its output array to a
> `Fin`-indexed function.
>
> This is the preferred proof boundary for the fast path: once this theorem is
> proved, correctness against the abstract additive NTT specification follows from
> `computableAdditiveNTT_eq_additiveNTT`.

```lean
theorem computableAdditiveNTTFast_eq_computableAdditiveNTT (a : Fin (2 ^ ℓ) → L) :
    AdditiveNTT.arrayToFinFunction (2^(ℓ + R_rate))
      (computableAdditiveNTTFast (L := L) (r := r) (β := β)
        (ℓ := ℓ) (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (a := a)) =
    computableAdditiveNTT (𝔽q := 𝔽q) (L := L) (r := r) (β := β)
      (ℓ := ℓ) (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (a := a)
```

`AdditiveNTT.computableAdditiveNTTFast_eq_additiveNTT` (theorem, [line 597](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L597))

> The fast additive NTT array implementation is correct against the abstract
> additive NTT specification after converting its output array to a `Fin`-indexed
> function.

```lean
theorem computableAdditiveNTTFast_eq_additiveNTT (a : Fin (2 ^ ℓ) → L) :
    AdditiveNTT.arrayToFinFunction (2^(ℓ + R_rate))
      (computableAdditiveNTTFast (L := L) (r := r) (β := β)
        (ℓ := ℓ) (R_rate := R_rate) (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (a := a)) =
    additiveNTT (𝔽q := 𝔽q) (L := L) (β := β)
      (h_ℓ_add_R_rate := h_ℓ_add_R_rate) (a := a)
```

`AdditiveNTT.initial_tiled_coeffs_correctness` (lemma, [line 626](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L626))

```lean
lemma initial_tiled_coeffs_correctness (h_ℓ : ℓ ≤ r) (a : Fin (2 ^ ℓ) → L) :
    let b: Fin (2^(ℓ + R_rate)) → L := tileCoeffs a
    additiveNTTInvariant 𝔽q β h_ℓ_add_R_rate b a (i := ⟨ℓ, by omega⟩)
      (h_i := by change ℓ ≤ ℓ; omega)
```

`AdditiveNTT.NTTStage_correctness` (lemma, [line 680](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L680))

> The correctness theorem for the `NTTStage` function. This is the inductive step
> in the main proof. It asserts that if the invariant holds for `i+1`, then after
> applying `NTTStage i`, the invariant holds for `i ∈ {0, ..., ℓ-1}`.

```lean
lemma NTTStage_correctness (i : Fin (ℓ))
    (input_buffer : Fin (2 ^ (ℓ + R_rate)) → L) (original_coeffs : Fin (2 ^ ℓ) → L) :
    additiveNTTInvariant 𝔽q β h_ℓ_add_R_rate (evaluation_buffer:=input_buffer)
      (original_coeffs:=original_coeffs) (i := ⟨i.val + 1, by omega⟩)
        (h_i := by change i.val + 1 ≤ ℓ; omega) →
    additiveNTTInvariant 𝔽q β h_ℓ_add_R_rate (evaluation_buffer:=NTTStage 𝔽q β h_ℓ_add_R_rate
      (i := ⟨i, by omega⟩) (h_i := by simp only; omega) input_buffer)
      (original_coeffs:=original_coeffs) (i := ⟨i, by omega⟩)
        (h_i := by change i.val ≤ ℓ; omega)
```

`AdditiveNTT.foldl_NTTStage_inductive_aux` (lemma, [line 1083](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L1083))

```lean
lemma foldl_NTTStage_inductive_aux (h_ℓ : ℓ ≤ r) (k : Fin (ℓ + 1))
    (original_coeffs : Fin (2 ^ ℓ) → L) :
    additiveNTTInvariant 𝔽q β h_ℓ_add_R_rate
    (Fin.foldl k (fun current_b i ↦ NTTStage 𝔽q β h_ℓ_add_R_rate
      (i := ⟨ℓ - i -1, by omega⟩) (h_i := by simp only; omega) current_b)
      (tileCoeffs original_coeffs))
    original_coeffs ⟨ℓ - k, by omega⟩ (by change ℓ - k.val ≤ ℓ; omega)
```

`AdditiveNTT.additiveNTT_correctness` (theorem, [line 1119](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean#L1119))

> **Main Correctness Theorem for Additive NTT**
> If `b` is the output of `additiveNTT` on input `a`, then for all `j`, `b j`
> is the evaluation of the polynomial `P` (from the novel basis coefficients `a`)
> at the evaluation point `ω_{0, j}` in the domain `S⁰`.

```lean
theorem additiveNTT_correctness (h_ℓ : ℓ ≤ r)
    (original_coeffs : Fin (2 ^ ℓ) → L)
    (output_buffer : Fin (2 ^ (ℓ + R_rate)) → L)
    (h_alg : output_buffer = additiveNTT 𝔽q β h_ℓ_add_R_rate original_coeffs) :
    let P := polynomialFromNovelCoeffs 𝔽q β ℓ h_ℓ original_coeffs
    ∀ (j : Fin (2^(ℓ + R_rate))),
      output_buffer j = P.eval (evaluationPointω 𝔽q β h_ℓ_add_R_rate
        (i := ⟨0, by omega⟩) (h_i := by simp only; omega) j)
```

## Depends on

- [Executable additive NTT algorithms](executable.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/AdditiveNTT/Correctness.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Correctness.json)
