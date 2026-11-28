---
catalog: module
lean: AdditiveNTT.Array.toFinVec, AdditiveNTT.arrayToFinFunction, AdditiveNTT.List.prod_finRange_eq_finset_prod, AdditiveNTT.bitsToU, AdditiveNTT.getUElements, AdditiveNTT.evalWAt, AdditiveNTT.evalNormalizedWAt, AdditiveNTT.computableTwiddleFactor, AdditiveNTT.computableNTTStage, AdditiveNTT.computableAdditiveNTT, AdditiveNTT.tileCoeffsArray, AdditiveNTT.evalWAtCachedConstantsLoop, AdditiveNTT.evalWAtCachedConstants, AdditiveNTT.subspacePolynomialConstantsArrayLoop, AdditiveNTT.subspacePolynomialConstantsArray, AdditiveNTT.computableNormalizedWValuesArray, AdditiveNTT.computableTwiddleTableArray, AdditiveNTT.computableNTTStageArray, AdditiveNTT.computableAdditiveNTTFastStages, AdditiveNTT.computableAdditiveNTTFastAction, AdditiveNTT.computableAdditiveNTTFast
statement: formalized
proof: formalized
---

# Executable additive NTT algorithms

`CompPoly.Fields.Binary.AdditiveNTT.Executable`, in [CompPoly/Fields/Binary/AdditiveNTT/Executable.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean), by Chung Thai Nguyen, Quang Dao.

> Generic function-backed and array-backed additive NTT implementations over a finite field,
> with an explicitly supplied binary-subfield algebra and independent basis vectors. The
> function-backed transform mirrors the abstract stages; the array-backed transform caches
> subspace-polynomial constants and twiddle tables.
>
> `CompPoly.Fields.Binary.AdditiveNTT.Correctness` relates these implementations to the
> abstract algorithm and its evaluation specification. Concrete tower instances and the
> compatibility entry point remain in `CompPoly.Fields.Binary.AdditiveNTT.Impl`.
>
> The coefficient tiling, twiddle factors, and descending butterfly stages follow the
> Lin–Chung–Han additive NTT presentation in [DP24], Algorithm 2. The array-backed path
> caches quantities used by these same stages.
>
> ## References
>
> * [Diamond, B. E. and Posen, J., *Polylogarithmic proofs for multilinears over binary towers*][DP24]

`AdditiveNTT.Array.toFinVec` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L38))

> Read an array of length `n` as a function on `Fin n`.

```lean
def Array.toFinVec {α : Type _} (n : ℕ) (arr : Array α) (h : arr.size = n) : Fin n → α
```

`AdditiveNTT.arrayToFinFunction` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L42))

> Converts an array to a `Fin n` function, using `0` for missing entries.

```lean
def arrayToFinFunction {α : Type _} [Zero α] (n : ℕ) (arr : Array α) : Fin n → α
```

`AdditiveNTT.List.prod_finRange_eq_finset_prod` (lemma, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L46))

> The product of a function over the list of finite indices equals its finite product.

```lean
lemma List.prod_finRange_eq_finset_prod {M : Type*} [CommMonoid M] {n : ℕ} (f : Fin n → M) :
    ((List.finRange n).map f).prod = ∏ i : Fin n, f i
```

`AdditiveNTT.bitsToU` (definition, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L67))

> Map the numeric mask `k` to the sum of the first `i` basis vectors selected by its bits,
> as an element of their linear span.

```lean
def bitsToU (i : Fin r) (k : Fin (2 ^ i.val)) :
    AdditiveNTT.U (L := L) (𝔽q := 𝔽q) (β := β) i
```

`AdditiveNTT.getUElements` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L86))

> Computes the elements of the subspace: `U_i = span({β_0, ..., β_{i-1}})`.

```lean
def getUElements (i : Fin r) : List L
```

`AdditiveNTT.evalWAt` (definition, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L94))

> Evaluates the subspace vanishing polynomial `W_i(x) = ∏_{u ∈ U_i} (x - u).`

```lean
def evalWAt (i : Fin r) (x : L) : L
```

`AdditiveNTT.evalNormalizedWAt` (definition, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L98))

> Evaluates the normalized subspace vanishing polynomial `Ŵ_i(x) = W_i(x) / W_i(β_i)`.

```lean
def evalNormalizedWAt (i : Fin r) (x : L) : L
```

`AdditiveNTT.computableTwiddleFactor` (definition, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L106))

> Compute the stage-`i` twiddle factor by summing normalized subspace-polynomial
> evaluations selected by the bits of `u`.

```lean
def computableTwiddleFactor (i : Fin ℓ) (u : Fin (2 ^ (ℓ + R_rate - i - 1))) : L
```

`AdditiveNTT.computableNTTStage` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L118))

> Perform stage `i` on the coefficient buffer `b`, pairing entries whose indices differ
> in bit `i` and applying the corresponding twiddle factor.

```lean
def computableNTTStage [Fact (LinearIndependent 𝔽q β)]
    (i : Fin ℓ) (b : Fin (2 ^ (ℓ + R_rate)) → L) : Fin (2^(ℓ + R_rate)) → L
```

`AdditiveNTT.computableAdditiveNTT` (definition, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L194))

> Transform `2 ^ ℓ` novel-basis coefficients into `2 ^ (ℓ + R_rate)` values by first
> tiling the coefficients and then applying stages `ℓ - 1` down to `0`. The basis has length
> `r`, and `ℓ + R_rate < r` bounds the evaluation domain.

```lean
def computableAdditiveNTT (a : Fin (2 ^ ℓ) → L) : Fin (2^(ℓ + R_rate)) → L
```

`AdditiveNTT.tileCoeffsArray` (definition, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L202))

> Array-backed coefficient tiling for the fast additive NTT path.

```lean
def tileCoeffsArray (R_rate : ℕ) (a : Fin (2 ^ ℓ) → L) : Array L
```

`AdditiveNTT.evalWAtCachedConstantsLoop` (definition, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L211))

> Starting from `acc`, iterate `acc ↦ acc * (acc + constants[k])` for indices
> `k` from `j` to `constants.size - 1`. Return `acc` unchanged when `constants.size ≤ j`.
>
> For `j ≤ constants.size`, if the initial accumulator is `W_j(x)` and the remaining
> constants are `W_k(β_k)`, the result is `W_{constants.size}(x)`.

```lean
def evalWAtCachedConstantsLoop (constants : Array L) (j : Nat) (acc : L) : L
```

`AdditiveNTT.evalWAtCachedConstants` (definition, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L223))

> Evaluate a subspace polynomial using cached constants `W_k(β_k)`.
>
> Starting from `W_0(x) = x`, each cached constant advances the recurrence
> `W_{k+1}(x) = W_k(x) * (W_k(x) + W_k(β_k))`.

```lean
def evalWAtCachedConstants (constants : Array L) (x : L) : L
```

`AdditiveNTT.subspacePolynomialConstantsArrayLoop` (definition, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L232))

> Extend the supplied `constants` array, starting at index `k` and stopping before `i`.
> Each step evaluates the polynomial recurrence encoded by the current array at `β_k`
> and appends the result. Return the array unchanged when `i ≤ k`.
>
> If the supplied array has length `k` and entry `j` is `W_j(β_j)` for every `j < k`,
> each appended entry has the same interpretation at its index.

```lean
def subspacePolynomialConstantsArrayLoop (i : Fin r) (k : Nat) (constants : Array L) : Array L
```

`AdditiveNTT.subspacePolynomialConstantsArray` (definition, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L242))

> Precompute the constants `W_k(β_k)` needed by the recursive subspace
> polynomial evaluator up to stage `i`.

```lean
def subspacePolynomialConstantsArray (i : Fin r) : Array L
```

`AdditiveNTT.computableNormalizedWValuesArray` (definition, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L246))

> Precompute normalized vanishing evaluations used by one stage's twiddle factors.

```lean
def computableNormalizedWValuesArray (i : Fin ℓ) : Array L
```

`AdditiveNTT.computableTwiddleTableArray` (definition, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L258))

> Precompute all twiddle factors for one additive NTT stage.
>
> The table entry for `u` is the subset sum of the cached normalized values
> selected by the set bits of `u`.

```lean
def computableTwiddleTableArray (i : Fin ℓ) : Array L
```

`AdditiveNTT.computableNTTStageArray` (definition, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L270))

> Array update for one additive NTT stage.
>
> The `twiddles` array is intended to store the values of `computableTwiddleFactor`
> for this stage, indexed by `u`. Missing entries in either input array are read as zero.

```lean
def computableNTTStageArray (i : Fin ℓ) (twiddles : Array L) (b : Array L) : Array L
```

`AdditiveNTT.computableAdditiveNTTFastStages` (definition, [line 292](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L292))

> Fast additive NTT stage driver over an `Array L` state.
>
> The state is expected to contain the initialized output buffer. Each stage
> updates that buffer using the array transition from
> `computableNTTStageArray`.

```lean
def computableAdditiveNTTFastStages : StateM (Array L) Unit
```

`AdditiveNTT.computableAdditiveNTTFastAction` (definition, [line 304](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L304))

> Fast additive NTT array producer as a state action.

```lean
def computableAdditiveNTTFastAction (a : Fin (2 ^ ℓ) → L) :
    StateM (Array L) (Array L)
```

`AdditiveNTT.computableAdditiveNTTFast` (definition, [line 312](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean#L312))

> Fast additive NTT array producer.

```lean
def computableAdditiveNTTFast (a : Fin (2 ^ ℓ) → L) : Array L
```

## Depends on

- [Additive NTT Algorithm](algorithm.md)

## Sources

- [CompPoly/Fields/Binary/AdditiveNTT/Executable.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/AdditiveNTT/Executable.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.AdditiveNTT.Executable.json)
