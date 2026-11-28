---
catalog: module
lean: AdditiveNTT.evaluationPointω, AdditiveNTT.twiddleFactor, AdditiveNTT.evaluationPointω_eq_twiddleFactor_of_div_2, AdditiveNTT.eval_point_ω_eq_next_twiddleFactor_comp_qmap, AdditiveNTT.tileCoeffs, AdditiveNTT.NTTStage, AdditiveNTT.additiveNTT, AdditiveNTT.coeffsBySuffix, AdditiveNTT.base_coeffsBySuffix, AdditiveNTT.evenRefinement_eq_novel_poly_of_0_leading_suffix, AdditiveNTT.oddRefinement_eq_novel_poly_of_1_leading_suffix, AdditiveNTT.additiveNTTInvariant
statement: formalized
proof: formalized
---

# Additive NTT Algorithm

`CompPoly.Fields.Binary.AdditiveNTT.Algorithm`, in [CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean), by Chung Thai Nguyen, Quang Dao.

> Core Additive NTT data flow: evaluation points, twiddle factors, stage/update
> definitions, coefficient tiling, and the stage invariant.

> ## 2. The Additive NTT Algorithm and Correctness
>
> This section describes the construction of the evaluation points,
> the tiling of coefficients, the main loop invariant, and the final
> correctness theorem for the Additive NTT algorithm.

`AdditiveNTT.evaluationPointω` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L45))

> Constructs an evaluation point in `sDomain i` from its Nat.getBit representation.
>
> The index is loose (`i : Fin r`); `h_i` records that it is an Additive-NTT level.

```lean
noncomputable def evaluationPointω (i : Fin r) (h_i : i ≤ ℓ)
    (x : Fin (2 ^ (ℓ + R_rate - i))) : L
```

`AdditiveNTT.twiddleFactor` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L60))

> The twiddle factor at a strict NTT stage `i`.
>
> It is the evaluation point with the stage bit set to zero, i.e. the `x₀` term of
> the butterfly identity.

```lean
noncomputable def twiddleFactor (i : Fin r) (h_i : i < ℓ)
  (u : Fin (2 ^ (ℓ + R_rate - i - 1))) : L
```

`AdditiveNTT.evaluationPointω_eq_twiddleFactor_of_div_2` (lemma, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L75))

```lean
lemma evaluationPointω_eq_twiddleFactor_of_div_2 (i : Fin r) (h_i : i < ℓ)
    (x : Fin (2 ^ (ℓ + R_rate - i))) :
  evaluationPointω 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega) x =
  twiddleFactor 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega) ⟨x/2, by
    have h := div_two_pow_lt_two_pow (x:=x) (i := ℓ + R_rate - i - 1) (j:=1) (by
      rw [Nat.sub_add_cancel (by omega)]; omega)
    simp only [pow_one] at h
    calc _ < 2 ^ (ℓ + R_rate - i - 1) := by omega
      _ = _ := by rfl
  ⟩ + (x.val % 2: ℕ) * eval (β ⟨i, by omega⟩) (normalizedW 𝔽q β ⟨i, by omega⟩)
```

`AdditiveNTT.eval_point_ω_eq_next_twiddleFactor_comp_qmap` (lemma, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L127))

```lean
lemma eval_point_ω_eq_next_twiddleFactor_comp_qmap
    (i : Fin r) (h_i : i < ℓ) (x : Fin (2 ^ (ℓ + R_rate - (i + 1)))) :
  -- `j = u||b||v` => x here means u at level i
  evaluationPointω 𝔽q β h_ℓ_add_R_rate (i := ⟨i.val+1, by omega⟩) (h_i := by simp only; omega) x =
  eval (twiddleFactor 𝔽q β h_ℓ_add_R_rate (i := i) (h_i := by omega) (u := ⟨x.val, by
    calc x.val < 2 ^ (ℓ + R_rate - (i.val + 1)) := by omega
      _ = 2 ^ (ℓ + R_rate - i.val - 1) := by rfl
  ⟩)) (qMap 𝔽q β ⟨i, by omega⟩ (by change i.val + 1 < r; omega))
```

`AdditiveNTT.tileCoeffs` (definition, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L191))

> The `2^R_rate`-fold tiling of coefficients `a` into the initial buffer `b`.
> `b(v) = aⱼ`, where `j` are the `ℓ` LSBs of `v`.

```lean
def tileCoeffs (a : Fin (2 ^ ℓ) → L) : Fin (2^(ℓ + R_rate)) → L
```

`AdditiveNTT.NTTStage` (definition, [line 198](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L198))

> A single Additive-NTT stage.
>
> `i : Fin r` is a loose index, while `h_i : i < ℓ` restricts it to a stage of the
> `for i from ℓ - 1 down to 0` loop.

```lean
noncomputable def NTTStage (i : Fin r) (h_i : i < ℓ) (b : Fin (2 ^ (ℓ + R_rate)) → L) :
    Fin (2^(ℓ + R_rate)) → L
```

`AdditiveNTT.additiveNTT` (definition, [line 275](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L275))

> **The Additive NTT Algorithm (Algorithm 2)**
>
> Computes the Additive NTT on a given set of coefficients from the novel basis.
> - `a`: The initial coefficient array `(a₀, ..., a_{2^ℓ-1})`.

```lean
noncomputable def additiveNTT (a : Fin (2 ^ ℓ) → L) : Fin (2^(ℓ + R_rate)) → L
```

`AdditiveNTT.coeffsBySuffix` (definition, [line 285](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L285))

> The coefficients of the level-`i` polynomial selected by the low-bit suffix `v`.
>
> The loose index `i : Fin r` is constrained by `h_i : i ≤ ℓ`; at `i = ℓ` this is
> the initially tiled buffer.

```lean
def coeffsBySuffix (a : Fin (2 ^ ℓ) → L) (i : Fin r) (h_i : i ≤ ℓ) (v : Fin (2 ^ i.val)) :
    Fin (2 ^ (ℓ - i)) → L
```

`AdditiveNTT.base_coeffsBySuffix` (lemma, [line 298](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L298))

```lean
lemma base_coeffsBySuffix (a : Fin (2 ^ ℓ) → L) :
    coeffsBySuffix (r:=r) (R_rate := R_rate) (a := a) (i := 0)
    (h_i := by simp only [Fin.coe_ofNat_eq_mod,
    Nat.zero_mod, zero_le]) 0 = a
```

`AdditiveNTT.evenRefinement_eq_novel_poly_of_0_leading_suffix` (theorem, [line 311](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L311))

> `P₀, ₍ᵥ₎⁽ⁱ⁺¹⁾(X) = P₍₀ᵥ₎⁽ⁱ⁺¹⁾(X)`, where `v` consists of exactly `i` bits
> Note that the even refinement `P₀, ₍ᵥ₎⁽ⁱ⁺¹⁾(X)` is constructed from the view of
> stage `i`, while the novel polynomial `P₍₀ᵥ₎⁽ⁱ⁺¹⁾(X)` is constructed from the view of stage `i+1`.

```lean
theorem evenRefinement_eq_novel_poly_of_0_leading_suffix (i : Fin r) (h_i : i < ℓ)
    (v : Fin (2 ^ i.val))
    (original_coeffs : Fin (2 ^ ℓ) → L) :
    have h_v: v.val < 2 ^ (i.val + 1) := by
      calc v.val < 2 ^ i.val
```

`AdditiveNTT.oddRefinement_eq_novel_poly_of_1_leading_suffix` (theorem, [line 367](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L367))

> `P₁, ₍ᵥ₎⁽ⁱ⁺¹⁾(X) = P₍₁ᵥ₎⁽ⁱ⁺¹⁾(X)`, where `v` consists of exactly `i` bits
> Note that the odd refinement `P₁,₍ᵥ₎⁽ⁱ⁺¹⁾(X)` is constructed from the view of stage `i`,
> while the novel polynomial `P₍₁ᵥ₎⁽ⁱ⁺¹⁾(X)` is constructed from the view of stage `i+1`.

```lean
theorem oddRefinement_eq_novel_poly_of_1_leading_suffix (i : Fin r) (h_i : i < ℓ)
    (v : Fin (2 ^ i.val))
    (original_coeffs : Fin (2 ^ ℓ) → L) :
    have h_v: v.val ||| (1 <<< i.val) < 2 ^ (i.val + 1) := by
      apply Nat.or_lt_two_pow (x:=v.val) (y:=1 <<< i.val) (n:=i.val + 1) (by omega)
      rw [Nat.shiftLeft_eq, one_mul]
      exact Nat.pow_lt_pow_right (by omega) (by omega)
    oddRefinement 𝔽q β h_ℓ_add_R_rate i h_i (coeffsBySuffix (r:=r) (R_rate:=R_rate)
      original_coeffs (i := i) (h_i := by omega) v) =
    intermediateEvaluationPoly 𝔽q β h_ℓ_add_R_rate (i := ⟨i.val + 1, by omega⟩)
      (h_i := by simp only; omega)
      (coeffsBySuffix (r:=r) (R_rate:=R_rate) original_coeffs
        (i := ⟨i.val+1, by omega⟩) (h_i := by simp only; omega)
        ⟨v ||| (1 <<< i.val), h_v⟩)
```

`AdditiveNTT.additiveNTTInvariant` (definition, [line 472](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean#L472))

> The main loop invariant for the `additiveNTT` algorithm: the evaluation buffer `b`
> at the end of level `i` (`i ∈ {0, ..., ℓ}`, `i=ℓ` means the initial tiled buffer)
> holds the value `P⁽ⁱ⁾(ω_{u, b, i})` for all Nat.getBit mask index
> `(u||b||v) ∈ {0, ..., 2^(ℓ+R_rate)-1}`, where the points `ω_{u, b, i}` are in the domain `S⁽ⁱ⁾`.
>
> **Main statement:**
> After round `i ∈ {ℓ-1, ℓ-2, ..., 0}`: the buffer `b` at index `j` (which can be
> decomposed as `j = (u || b || v)` in little-endian order, where
> - `u` is a bitstring of length `ℓ + R_rate - i - 1`,
> - `b` is a single Nat.getBit (the LSB of the high bits),
> - `v` is a bitstring of length `i` (the LSBs),
> holds the value `P⁽ⁱ⁾(ω_{u, b, i})`,
> where:
>   - `P⁽ⁱ⁾` is the intermediate polynomial at round `i` (in the novel basis),
>   - `ω_{u, b, i}` is the evaluation point in the subspace `S⁽ⁱ⁾` constructed
>   as a linear combination of the basis elements of `S⁽ⁱ⁾`:
>     - the Nat.getBit `b` is the coefficient for `Ŵᵢ(βᵢ)` (the LSB),
>     - the LSB of `u` is the coefficient for `Ŵᵢ(β_{i+1})`, ..., the MSB of `u` is
>     the coefficient for `Ŵᵢ(β_{ℓ+R_rate-1})`.
>   - The value is replicated `2^i` times for each `v`
>     (i.e., the last `i` bits do not affect the value).
>
> More precisely, for all `j : Fin (2^(ℓ + R_rate))`,
> let `u_b_v := j.val` (as a natural number),
> - let `v := u_b_v % 2^i` (the `i` LSBs),
> - let `u_b := u_b_v / 2^i` (the high bits),
> - let `b := u_b % 2` (the LSB of the high bits),
> - let `u := u_b / 2` (the remaining high bits),
> then:
>   b j = P⁽ⁱ⁾(ω_{u, b, i})

```lean
def additiveNTTInvariant (evaluation_buffer : Fin (2 ^ (ℓ + R_rate)) → L)
    (original_coeffs : Fin (2 ^ ℓ) → L) (i : Fin r) (h_i : i ≤ ℓ) : Prop
```

## Depends on

- [Additive NTT Intermediate Objects](intermediate.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Algorithm.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Algorithm.json)
