---
catalog: module
lean: BF128Ghash.ghashPoly, BF128Ghash.ghashTail, BF128Ghash.ghashPoly_eq_X_pow_add_tail, BF128Ghash.ghashTail_natDegree, BF128Ghash.ghashTail_monic, BF128Ghash.ghashTail_ne_zero, BF128Ghash.ghashTail_degree, BF128Ghash.ghashPoly_natDegree, BF128Ghash.ghashPoly_monic, BF128Ghash.ghashPoly_ne_zero, BF128Ghash.ghashPoly_degree, BF128Ghash.X_mod_ghashPoly, BF128Ghash.X_pow_128_mod_ghashPoly, BF128Ghash.reduce_degree_step, BF128Ghash.P_val, BF128Ghash.ghashPoly_eq_P_val, BF128Ghash.X_val, BF128Ghash.X_ZMod2Poly, BF128Ghash.X_ZMod2Poly_eq_X, BF128Ghash.chain_step, BF128Ghash.clMulNat, BF128Ghash.clSqNat, BF128Ghash.mulByP_Nat, BF128Ghash.checkSquareStep, BF128Ghash.checkDivStep, BF128Ghash.clMulNat_high_bits_zero, BF128Ghash.to256_truncate_128, BF128Ghash.toPoly_truncate_128, BF128Ghash.toPoly_clMul_B256, BF128Ghash.verify_square_step_correct, BF128Ghash.verify_div_step_bounded, BF128Ghash.verify_div_step
statement: formalized
proof: formalized
---

# BinaryField128Ghash Prelude

`CompPoly.Fields.Binary.BF128Ghash.Prelude`, in [CompPoly/Fields/Binary/BF128Ghash/Prelude.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean), by Chung Thai Nguyen, Quang Dao, Dimitris Mitsios.

> Define GF(2^128) as a single field extension over GF(2) using the GHASH polynomial
> from AES-GCM: P(X) = X^128 + X^7 + X^2 + X + 1.
>
> ## Main Definitions
>
> ### Polynomial Definitions
> - `ghashPoly`: The defining polynomial X^128 + X^7 + X^2 + X + 1 over GF(2)
> - `ghashTail`: The tail polynomial X^7 + X^2 + X + 1
>
> ### Verification Functions
> - `checkSquareStep`: Verifies a modular squaring step
> - `verify_square_step_correct`: Correctness theorem for square step verification
> - `checkDivStep`: Verifies a division step
> - `verify_div_step`: Correctness theorem for division step verification
>
> For BitVec operations (`clMul`, `clSq`, `toPoly`) and shared lemmas, see
> `ArkLib.Data.FieldTheory.BinaryField.Common`.

`BF128Ghash.ghashPoly` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L50))

> The GHASH polynomial: P(X) = X^128 + X^7 + X^2 + X + 1 over GF(2).
> This is the irreducible polynomial used in AES-GCM.

```lean
noncomputable def ghashPoly : Polynomial (ZMod 2)
```

`BF128Ghash.ghashTail` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L57))

> The tail of GHASH poly: T(X) = X^7 + X^2 + X + 1

```lean
noncomputable def ghashTail : Polynomial (ZMod 2)
```

`BF128Ghash.ghashPoly_eq_X_pow_add_tail` (lemma, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L60))

```lean
lemma ghashPoly_eq_X_pow_add_tail : ghashPoly = X^128 + ghashTail
```

`BF128Ghash.ghashTail_natDegree` (lemma, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L65))

```lean
lemma ghashTail_natDegree : ghashTail.natDegree = 7
```

`BF128Ghash.ghashTail_monic` (lemma, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L80))

> The GHASH polynomial is monic.

```lean
lemma ghashTail_monic : Monic ghashTail
```

`BF128Ghash.ghashTail_ne_zero` (lemma, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L96))

```lean
lemma ghashTail_ne_zero : ghashTail ≠ 0
```

`BF128Ghash.ghashTail_degree` (lemma, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L98))

```lean
lemma ghashTail_degree : (ghashTail).degree = 7
```

`BF128Ghash.ghashPoly_natDegree` (lemma, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L103))

> The degree of the GHASH polynomial is 128.

```lean
lemma ghashPoly_natDegree : (ghashPoly).natDegree = 128
```

`BF128Ghash.ghashPoly_monic` (lemma, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L116))

> The GHASH polynomial is monic.

```lean
lemma ghashPoly_monic : Monic ghashPoly
```

`BF128Ghash.ghashPoly_ne_zero` (lemma, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L134))

> The GHASH polynomial is nonzero.

```lean
lemma ghashPoly_ne_zero : ghashPoly ≠ 0
```

`BF128Ghash.ghashPoly_degree` (lemma, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L136))

```lean
lemma ghashPoly_degree : (ghashPoly).degree = 128
```

`BF128Ghash.X_mod_ghashPoly` (lemma, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L140))

```lean
lemma X_mod_ghashPoly : X % ghashPoly = X
```

`BF128Ghash.X_pow_128_mod_ghashPoly` (lemma, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L147))

> Reduction rule: X^128 % ghashPoly = ghashTail

```lean
lemma X_pow_128_mod_ghashPoly : X^128 % ghashPoly = ghashTail
```

`BF128Ghash.reduce_degree_step` (lemma, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L164))

> General reduction step: `(X^k * X^128) % P = (X^k * tail) % P`
> This allows reducing terms like `X^130` to `X^2 * tail`.
> Actually, we want `X^(128+k) % P = (X^k * tail) % P`.

```lean
lemma reduce_degree_step (k : ℕ) : (X^(128+k)) % ghashPoly = (X^k * ghashTail) % ghashPoly
```

`BF128Ghash.P_val` (definition, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L176))

```lean
def P_val : B256
```

`BF128Ghash.ghashPoly_eq_P_val` (lemma, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L180))

```lean
lemma ghashPoly_eq_P_val : ghashPoly = toPoly P_val
```

`BF128Ghash.X_val` (definition, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L189))

```lean
def X_val : B128
```

`BF128Ghash.X_ZMod2Poly` (definition, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L190))

```lean
noncomputable def X_ZMod2Poly : Polynomial (ZMod 2)
```

`BF128Ghash.X_ZMod2Poly_eq_X` (lemma, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L192))

```lean
lemma X_ZMod2Poly_eq_X : X_ZMod2Poly = X
```

`BF128Ghash.chain_step` (lemma, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L227))

> Helper lemma to chain the modular squaring steps

```lean
lemma chain_step {k : ℕ} {prev next : Polynomial (ZMod 2)} {q_val : B128}
    (h_prev : X ^ (2 ^ k) % ghashPoly = prev % ghashPoly)
    (h_step : prev ^ 2 = (toPoly (to256 q_val)) * ghashPoly + next) :
  X^(2^(k+1)) % ghashPoly = next % ghashPoly
```

> ### Kernel-Efficient Checkers

`BF128Ghash.clMulNat` (definition, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L251))

> Carry-less (polynomial) multiply using structural recursion on `n`,
> iterating over bits `0 .. n-1` of `a`.
> Uses only `Nat.testBit`, `Nat.xor`, `Nat.shiftLeft` —
> no `Finset.fold`, no `BitVec`, no `Nat.mod`.

```lean
def clMulNat (a b : Nat) : Nat → Nat
```

`BF128Ghash.clSqNat` (abbreviation, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L258))

> Carry-less square via `clMulNat`.

```lean
abbrev clSqNat (a n : Nat) : Nat
```

`BF128Ghash.mulByP_Nat` (definition, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L264))

> Specialized carry-less multiply by `P_val` (the GHASH polynomial
> `P(X) = X^128 + X^7 + X^2 + X + 1`).
> `P_val` has bits set at positions `{0, 1, 2, 7, 128}`, so we hardcode the
> 5 XOR-shift operations instead of iterating over all bits.

```lean
def mulByP_Nat (a : Nat) : Nat
```

`BF128Ghash.checkSquareStep` (definition, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L270))

> Kernel-efficient version of `checkSquareStep`.
> The public API stays on `B128`, but the internal computation runs on `Nat`
> using `clSqNat` and the specialized `mulByP_Nat` helper.

```lean
def checkSquareStep (rPrev q rNext : B128) : Bool
```

`BF128Ghash.checkDivStep` (definition, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L278))

> Kernel-efficient version of `checkDivStep`.
> Preserves the full `B256` semantics of the public checker, but computes via
> `Nat` structural recursion instead of the `BitVec` fold.

```lean
def checkDivStep (a q b r : B256) : Bool
```

`BF128Ghash.clMulNat_high_bits_zero` (theorem, [line 284](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L284))

> If `a < 2^m`, then iterating `clMulNat` beyond bit `m-1` is a no-op,
> because `a.testBit i = false` for all `i ≥ m`.

```lean
theorem clMulNat_high_bits_zero (a b m n : Nat) (hmn : m ≤ n) (ha : a < 2 ^ m) :
    clMulNat a b n = clMulNat a b m
```

`BF128Ghash.to256_truncate_128` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L360))

```lean
theorem to256_truncate_128 (v : B256) (hv : v.toNat < 2^128) :
    to256 (v.truncate 128) = v
```

`BF128Ghash.toPoly_truncate_128` (theorem, [line 365](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L365))

```lean
theorem toPoly_truncate_128 (v : B256) (hv : v.toNat < 2^128) :
    toPoly (v.truncate 128) = toPoly v
```

`BF128Ghash.toPoly_clMul_B256` (theorem, [line 369](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L369))

```lean
theorem toPoly_clMul_B256 (q b : B256) (hq : q.toNat < 2^128) (hb : b.toNat < 2^128) :
    toPoly (clMul (q.truncate 128) (b.truncate 128)) = toPoly q * toPoly b
```

`BF128Ghash.verify_square_step_correct` (theorem, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L415))

> Soundness of the kernel-efficient square-step checker.

```lean
theorem verify_square_step_correct (rPrev q rNext : B128) :
    checkSquareStep rPrev q rNext = true →
    (toPoly rPrev) ^ 2 = (toPoly (to256 q)) * (toPoly P_val) + (toPoly rNext)
```

`BF128Ghash.verify_div_step_bounded` (theorem, [line 434](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L434))

> Soundness of the kernel-efficient division-step checker.

```lean
theorem verify_div_step_bounded (a q b r : B256) (hq : q.toNat < 2 ^ 128)
    (hb : b.toNat < 2 ^ 128) :
    a.toNat = clMulNat q.toNat b.toNat 128 ^^^ r.toNat →
    toPoly a = (toPoly q) * (toPoly b) + (toPoly r)
```

`BF128Ghash.verify_div_step` (theorem, [line 450](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean#L450))

> Soundness of the kernel-efficient division-step checker.

```lean
theorem verify_div_step (a q b r : B256) (hq : q.toNat < 2 ^ 128)
    (hb : b.toNat < 2 ^ 128) :
    checkDivStep a q b r = true →
    toPoly a = (toPoly q) * (toPoly b) + (toPoly r)
```

## Depends on

- [Common Utilities for Binary Fields](../../common.md)

## Sources

- [CompPoly/Fields/Binary/BF128Ghash/Prelude.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Prelude.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.BF128Ghash.Prelude.json)
