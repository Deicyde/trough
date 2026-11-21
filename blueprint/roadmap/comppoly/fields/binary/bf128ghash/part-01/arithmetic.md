---
catalog: module
lean: BF128Ghash.ConcreteBF128Ghash, BF128Ghash.ofBitVec, BF128Ghash.toBitVec_ofBitVec, BF128Ghash.ofBitVec_toBitVec, BF128Ghash.toBitVec_injective, BF128Ghash.ConcreteBF128Ghash.ext, BF128Ghash.equivBitVec, BF128Ghash.R_val, BF128Ghash.fold_step, BF128Ghash.reduce_clMul, BF128Ghash.toBitVec_zero, BF128Ghash.toBitVec_one, BF128Ghash.toBitVec_add, BF128Ghash.mul, BF128Ghash.toBitVec_mul, BF128Ghash.add_assoc, BF128Ghash.add_comm, BF128Ghash.add_zero, BF128Ghash.zero_add, BF128Ghash.neg_add_cancel, BF128Ghash.add_self_cancel, BF128Ghash.nsmul_succ, BF128Ghash.zsmul_succ, BF128Ghash.int_neg_mod_two, BF128Ghash.zsmul_neg, BF128Ghash.natCast, BF128Ghash.natCast_eq, BF128Ghash.natCast_zero, BF128Ghash.natCast_succ, BF128Ghash.intCast, BF128Ghash.intCast_ofNat, BF128Ghash.intCast_negSucc, BF128Ghash.square, BF128Ghash.powTwoPow, BF128Ghash.invItohTsujii, BF128Ghash.inv_zero, BF128Ghash.instDivConcreteBF128Ghash, BF128Ghash.instHDivConcreteBF128Ghash, BF128Ghash.div_eq_mul_inv
statement: formalized
proof: formalized
---

# GHASH polynomial-basis arithmetic

`CompPoly.Fields.Binary.BF128Ghash.Arithmetic`, in [CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean), by Chung Thai Nguyen, Quang Dao, Dimitris Mitsios.

> The nominal carrier stores 128 polynomial coefficients, with bit `i` representing `X^i`.
> Multiplication folds the full carry-less product modulo `X^128 + X^7 + X^2 + X + 1`.
> Inversion uses repeated squaring and a fixed addition chain, sending zero to zero.
> These operations and the explicit word maps require no irreducibility certificate.
>
> `CompPoly.Fields.Binary.BF128Ghash.Impl` proves correspondence with the polynomial quotient
> and supplies the canonical ring and field instances. The coordinates here describe
> polynomial coefficients; byte and wire formats require an explicit conversion.
>
> ## References
>
> * Dworkin, M., *Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode
>   (GCM) and GMAC*, NIST SP 800-38D.
>   https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf

`BF128Ghash.ConcreteBF128Ghash` (structure, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L38))

> An element of `GF(2)[X] / (X^128 + X^7 + X^2 + X + 1)` in a polynomial basis.

```lean
structure ConcreteBF128Ghash where
  /-- Bit `i` is the coefficient of `X^i`. -/
  toBitVec : BitVec 128
  deriving DecidableEq, BEq
```

`BF128Ghash.ofBitVec` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L44))

> Construct a field element from its polynomial-basis coordinates.

```lean
def ofBitVec (a : BitVec 128) : ConcreteBF128Ghash
```

`BF128Ghash.toBitVec_ofBitVec` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L47))

> Reading the coordinates of a constructed element recovers the input word.

```lean
theorem toBitVec_ofBitVec (a : BitVec 128) : (ofBitVec a).toBitVec = a
```

`BF128Ghash.ofBitVec_toBitVec` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L50))

> Reconstructing an element from its coordinates recovers that element.

```lean
theorem ofBitVec_toBitVec (a : ConcreteBF128Ghash) : ofBitVec a.toBitVec = a
```

`BF128Ghash.toBitVec_injective` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L53))

> Polynomial-basis coordinates uniquely determine a field element.

```lean
theorem toBitVec_injective : Function.Injective ConcreteBF128Ghash.toBitVec
```

`BF128Ghash.ConcreteBF128Ghash.ext` (theorem, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L61))

> Elements with equal polynomial-basis coordinates are equal.

```lean
theorem ConcreteBF128Ghash.ext {a b : ConcreteBF128Ghash}
    (h : a.toBitVec = b.toBitVec) : a = b
```

`BF128Ghash.equivBitVec` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L65))

> The equivalence between field elements and their polynomial-basis coordinates.

```lean
def equivBitVec : ConcreteBF128Ghash ≃ BitVec 128
```

`BF128Ghash.R_val` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L81))

> Folding Constant R = X^7 + X^2 + X + 1.
> Since P = X^128 + R, we have X^128 ≡ R (mod P).

```lean
def R_val : B128
```

`BF128Ghash.fold_step` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L85))

> Replace the high half of a 256-bit polynomial word by its product with
> `X^7 + X^2 + X + 1`, then XOR the low half into the result.

```lean
def fold_step (prod : B256) : B256
```

`BF128Ghash.reduce_clMul` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L92))

> Reduce a 256-bit polynomial word modulo `X^128 + X^7 + X^2 + X + 1` using two
> folds, then retain its low 128 bits.

```lean
def reduce_clMul (prod : B256) : B128
```

`BF128Ghash.toBitVec_zero` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L107))

> Zero has every polynomial-basis coefficient equal to zero.

```lean
theorem toBitVec_zero : (0 : ConcreteBF128Ghash).toBitVec = 0#128
```

`BF128Ghash.toBitVec_one` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L110))

> One has only its constant coefficient equal to one.

```lean
theorem toBitVec_one : (1 : ConcreteBF128Ghash).toBitVec = 1#128
```

`BF128Ghash.toBitVec_add` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L113))

> Addition is coefficientwise exclusive-or in the polynomial basis.

```lean
theorem toBitVec_add (a b : ConcreteBF128Ghash) :
    (a + b).toBitVec = a.toBitVec ^^^ b.toBitVec
```

`BF128Ghash.mul` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L117))

> Multiply by reducing the carry-less product of the polynomial-basis words.

```lean
def mul (a b : ConcreteBF128Ghash) : ConcreteBF128Ghash
```

`BF128Ghash.toBitVec_mul` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L123))

> The product coordinates are the reduced carry-less product of the input coordinates.

```lean
theorem toBitVec_mul (a b : ConcreteBF128Ghash) :
    (a * b).toBitVec = reduce_clMul (clMul a.toBitVec b.toBitVec)
```

`BF128Ghash.add_assoc` (lemma, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L130))

```lean
lemma add_assoc (a b c : ConcreteBF128Ghash) : a + b + c = a + (b + c)
```

`BF128Ghash.add_comm` (lemma, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L134))

```lean
lemma add_comm (a b : ConcreteBF128Ghash) : a + b = b + a
```

`BF128Ghash.add_zero` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L138))

```lean
lemma add_zero (a : ConcreteBF128Ghash) : a + 0 = a
```

`BF128Ghash.zero_add` (lemma, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L142))

```lean
lemma zero_add (a : ConcreteBF128Ghash) : 0 + a = a
```

`BF128Ghash.neg_add_cancel` (lemma, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L147))

```lean
lemma neg_add_cancel (a : ConcreteBF128Ghash) : -a + a = 0
```

`BF128Ghash.add_self_cancel` (lemma, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L151))

```lean
lemma add_self_cancel (a : ConcreteBF128Ghash) : a + a = 0
```

`BF128Ghash.nsmul_succ` (lemma, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L155))

```lean
lemma nsmul_succ (n : ℕ) (x : ConcreteBF128Ghash) :
    (if (n + 1) % 2 = 0 then (0 : ConcreteBF128Ghash) else x)
    = (if n % 2 = 0 then (0 : ConcreteBF128Ghash) else x) + x
```

`BF128Ghash.zsmul_succ` (lemma, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L173))

```lean
lemma zsmul_succ (n : ℕ) (x : ConcreteBF128Ghash) :
    (if (n + 1 : ℤ) % 2 = 0 then (0 : ConcreteBF128Ghash) else x)
    = (if (n : ℤ) % 2 = 0 then (0 : ConcreteBF128Ghash) else x) + x
```

`BF128Ghash.int_neg_mod_two` (lemma, [line 179](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L179))

```lean
lemma int_neg_mod_two (n : ℤ) : (-n) % 2 = n % 2
```

`BF128Ghash.zsmul_neg` (lemma, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L182))

```lean
lemma zsmul_neg (n : ℕ) (x : ConcreteBF128Ghash) :
    (if (Int.negSucc n) % 2 = 0 then (0 : ConcreteBF128Ghash) else x)
    = -(if (n + 1 : ℤ) % 2 = 0 then (0 : ConcreteBF128Ghash) else x)
```

`BF128Ghash.natCast` (definition, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L211))

```lean
def natCast (n : ℕ) : ConcreteBF128Ghash
```

`BF128Ghash.natCast_eq` (lemma, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L216))

```lean
lemma natCast_eq (n : ℕ) : (↑n : ConcreteBF128Ghash) = natCast n
```

`BF128Ghash.natCast_zero` (lemma, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L218))

```lean
lemma natCast_zero : natCast 0 = 0
```

`BF128Ghash.natCast_succ` (lemma, [line 220](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L220))

```lean
lemma natCast_succ (n : ℕ) : natCast (n + 1) = natCast n + 1
```

`BF128Ghash.intCast` (definition, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L232))

```lean
def intCast (n : ℤ) : ConcreteBF128Ghash
```

`BF128Ghash.intCast_ofNat` (lemma, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L237))

```lean
lemma intCast_ofNat (n : ℕ) : intCast (n : ℤ) = natCast n
```

`BF128Ghash.intCast_negSucc` (lemma, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L241))

```lean
lemma intCast_negSucc (n : ℕ) : intCast (Int.negSucc n) = -(↑(n + 1) : ConcreteBF128Ghash)
```

`BF128Ghash.square` (definition, [line 259](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L259))

> Squaring in GF(2^128).

```lean
def square (a : ConcreteBF128Ghash) : ConcreteBF128Ghash
```

`BF128Ghash.powTwoPow` (definition, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L262))

> Computes a^(2^k) by repeated squaring.

```lean
def powTwoPow (a : ConcreteBF128Ghash) (k : Nat) : ConcreteBF128Ghash
```

`BF128Ghash.invItohTsujii` (definition, [line 269](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L269))

> Invert using repeated squaring and a fixed addition chain for 127.
> Zero maps to zero; a nonzero element `a` maps to `a^(2^128 - 2)`.

```lean
def invItohTsujii (a : ConcreteBF128Ghash) : ConcreteBF128Ghash
```

`BF128Ghash.inv_zero` (lemma, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L291))

```lean
lemma inv_zero : (0 : ConcreteBF128Ghash)⁻¹ = 0
```

`BF128Ghash.instDivConcreteBF128Ghash` (instance, [line 296](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L296))

```lean
instance instDivConcreteBF128Ghash : Div (ConcreteBF128Ghash)
```

`BF128Ghash.instHDivConcreteBF128Ghash` (abbreviation, [line 301](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L301))

> Compatibility name for division inherited from the homogeneous division instance.

```lean
abbrev instHDivConcreteBF128Ghash :
    HDiv ConcreteBF128Ghash ConcreteBF128Ghash ConcreteBF128Ghash
```

`BF128Ghash.div_eq_mul_inv` (lemma, [line 304](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean#L304))

```lean
lemma div_eq_mul_inv (a b : ConcreteBF128Ghash) : a / b = a * b⁻¹
```

## Depends on

- [Binary polynomial word arithmetic](../../common-2/arithmetic.md)

## Sources

- [CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Arithmetic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.BF128Ghash.Arithmetic.json)
