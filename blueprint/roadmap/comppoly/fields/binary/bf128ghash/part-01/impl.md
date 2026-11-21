---
catalog: module
lean: BF128Ghash.R_val_eq_ghashTail, BF128Ghash.toPoly_split_256, BF128Ghash.poly_reduce_step, BF128Ghash.fold_step_mod_eq, BF128Ghash.reduce_clMul_correct, BF128Ghash.PolyQuot, BF128Ghash.toQuot, BF128Ghash.toQuot_pow_card, BF128Ghash.toQuot_injective, BF128Ghash.toQuot_add, BF128Ghash.toQuot_zero, BF128Ghash.toQuot_one, BF128Ghash.eq_of_toQuot_eq, BF128Ghash.toQuot_ne_zero, BF128Ghash.toQuot_mul, BF128Ghash.mul_assoc, BF128Ghash.one_mul, BF128Ghash.mul_one, BF128Ghash.left_distrib, BF128Ghash.right_distrib, BF128Ghash.zero_mul, BF128Ghash.mul_zero, BF128Ghash.instSemigroupConcreteBF128Ghash, BF128Ghash.instRingConcreteBF128Ghash, BF128Ghash.toQuot_square, BF128Ghash.toQuot_powTwoPow, BF128Ghash.target_val, BF128Ghash.itoh_tsujii_step, BF128Ghash.toQuot_invItohTsujii, BF128Ghash.pow_2k, BF128Ghash.inv_itoh_tsujii, BF128Ghash.toQuot_pow_2k, BF128Ghash.toQuot_inv_itoh_tsujii, BF128Ghash.exists_pair_ne, BF128Ghash.mul_inv_cancel, BF128Ghash.mul_comm, BF128Ghash.isField_concrete, BF128Ghash.instFieldConcreteBF128Ghash, BF128Ghash.instDivisionRingConcreteBF128Ghash, BF128Ghash.inv_def, BF128Ghash.div_def, BF128Ghash.npow_def, BF128Ghash.zpow_def, BF128Ghash.toQuot_inv
statement: formalized
proof: formalized
---

# GHASH Polynomial-Basis Field

`CompPoly.Fields.Binary.BF128Ghash.Impl`, in [CompPoly/Fields/Binary/BF128Ghash/Impl.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean), by Chung Thai Nguyen, Quang Dao, Dimitris Mitsios.

> The nominal carrier stores polynomial-basis `BitVec 128` coordinates: bit `i` is the
> coefficient of `X^i`. Explicit coordinate maps separate this presentation from raw machine
> words and other binary fields. Addition, multiplication, and the named inversion algorithm
> are executable, with an injective interpretation in
> `GF(2)[X] / (X^128 + X^7 + X^2 + X + 1)` proving their algebraic laws.
> The `Field` instance uses the same executable operations, with binary exponentiation for
> natural and integer powers. These coordinates describe polynomial coefficients; they do not
> introduce a byte or wire-format conversion. Import
> `CompPoly.Fields.Binary.BF128Ghash.Arithmetic` for the nominal carrier and executable
> operations without the quotient or irreducibility certificates.
>
> ## Main Definitions
>
> - `ConcreteBF128Ghash`: Nominal elements with `BitVec 128` polynomial coordinates
> - `ofBitVec`, `ConcreteBF128Ghash.toBitVec`: Explicit inverse coordinate maps
> - `instFieldConcreteBF128Ghash`: The field instance for `ConcreteBF128Ghash`
> - `toQuot`: The canonical map from `ConcreteBF128Ghash` to `AdjoinRoot ghashPoly`
> - `reduce_clMul`: The reduction of the carry-less multiplication
> - `powTwoPow`: Repeated squaring in the nominal field
> - `invItohTsujii`: The Itoh-Tsujii inversion algorithm
> - `toQuot_invItohTsujii`: The lemma that `invItohTsujii` computes `a^(2^128 - 2)`
>
> ## References
> * [NIST-SP-800-38D] Dworkin, M. Recommendation for Block Cipher Modes of Operation:
>   Galois/Counter Mode (GCM) and GMAC. NIST Special Publication 800-38D.
>   https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf

`BF128Ghash.R_val_eq_ghashTail` (lemma, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L60))

```lean
lemma R_val_eq_ghashTail : toPoly R_val = ghashTail
```

`BF128Ghash.toPoly_split_256` (lemma, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L70))

> Decomposition: x = h * X^128 + l where h and l are the high and low 128-bit parts.

```lean
lemma toPoly_split_256 (x : B256) :
    let h := x.extractLsb 255 128
    let l := x.extractLsb 127 0
    toPoly x = (toPoly h) * X^128 + (toPoly l)
```

`BF128Ghash.poly_reduce_step` (lemma, [line 165](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L165))

> The Algebraic Identity: A * X^128 ≡ A * R (mod P)

```lean
lemma poly_reduce_step (A : Polynomial (ZMod 2)) :
    (A * X^128) % ghashPoly = (A * ghashTail) % ghashPoly
```

`BF128Ghash.fold_step_mod_eq` (lemma, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L184))

> One fold preserves the value modulo P.

```lean
lemma fold_step_mod_eq (x : B256) :
    toPoly (fold_step x) % ghashPoly = toPoly x % ghashPoly
```

`BF128Ghash.reduce_clMul_correct` (lemma, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L201))

> Main Theorem: reduce_clMul correctly computes modulo P.

```lean
lemma reduce_clMul_correct (prod : B256) :
    toPoly (reduce_clMul prod) = toPoly prod % ghashPoly
```

`BF128Ghash.PolyQuot` (abbreviation, [line 340](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L340))

```lean
abbrev PolyQuot
```

`BF128Ghash.toQuot` (definition, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L343))

> Interpret polynomial-basis coordinates in the quotient by the defining polynomial.

```lean
noncomputable def toQuot (a : ConcreteBF128Ghash) : PolyQuot
```

`BF128Ghash.toQuot_pow_card` (lemma, [line 347](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L347))

> Frobenius property: a^(2^128) = a in GF(2^128).

```lean
lemma toQuot_pow_card (a : ConcreteBF128Ghash) : (toQuot a)^(2^128) = toQuot a
```

`BF128Ghash.toQuot_injective` (lemma, [line 353](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L353))

> The quotient interpretation is injective: coordinate polynomials have degree below 128,
> whereas the defining polynomial has degree 128.

```lean
lemma toQuot_injective : Function.Injective toQuot
```

`BF128Ghash.toQuot_add` (lemma, [line 384](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L384))

```lean
lemma toQuot_add (a b : ConcreteBF128Ghash) : toQuot (a + b) = toQuot a + toQuot b
```

`BF128Ghash.toQuot_zero` (lemma, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L389))

```lean
lemma toQuot_zero : toQuot 0 = 0
```

`BF128Ghash.toQuot_one` (lemma, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L392))

```lean
lemma toQuot_one : toQuot 1 = 1
```

`BF128Ghash.eq_of_toQuot_eq` (lemma, [line 396](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L396))

```lean
lemma eq_of_toQuot_eq {a b : ConcreteBF128Ghash} (h : toQuot a = toQuot b) : a = b
```

`BF128Ghash.toQuot_ne_zero` (lemma, [line 399](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L399))

```lean
lemma toQuot_ne_zero (a : ConcreteBF128Ghash) (h_a_ne_zero : a ≠ 0) : toQuot a ≠ 0
```

`BF128Ghash.toQuot_mul` (lemma, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L406))

> Interpreting a reduced carry-less product agrees with multiplication in the quotient.

```lean
lemma toQuot_mul (a b : ConcreteBF128Ghash) : toQuot (a * b) = toQuot a * toQuot b
```

`BF128Ghash.mul_assoc` (lemma, [line 421](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L421))

```lean
lemma mul_assoc (a b c : ConcreteBF128Ghash) : a * b * c = a * (b * c)
```

`BF128Ghash.one_mul` (lemma, [line 426](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L426))

```lean
lemma one_mul (a : ConcreteBF128Ghash) : 1 * a = a
```

`BF128Ghash.mul_one` (lemma, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L431))

```lean
lemma mul_one (a : ConcreteBF128Ghash) : a * 1 = a
```

`BF128Ghash.left_distrib` (lemma, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L436))

```lean
lemma left_distrib (a b c : ConcreteBF128Ghash) : a * (b + c) = a * b + a * c
```

`BF128Ghash.right_distrib` (lemma, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L441))

```lean
lemma right_distrib (a b c : ConcreteBF128Ghash) : (a + b) * c = a * c + b * c
```

`BF128Ghash.zero_mul` (lemma, [line 446](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L446))

```lean
lemma zero_mul (a : ConcreteBF128Ghash) : 0 * a = 0
```

`BF128Ghash.mul_zero` (lemma, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L451))

```lean
lemma mul_zero (a : ConcreteBF128Ghash) : a * 0 = 0
```

`BF128Ghash.instSemigroupConcreteBF128Ghash` (instance, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L455))

```lean
instance instSemigroupConcreteBF128Ghash : Semigroup ConcreteBF128Ghash
```

`BF128Ghash.instRingConcreteBF128Ghash` (instance, [line 458](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L458))

```lean
instance instRingConcreteBF128Ghash : Ring ConcreteBF128Ghash
```

`BF128Ghash.toQuot_square` (lemma, [line 480](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L480))

```lean
lemma toQuot_square (a : ConcreteBF128Ghash) : toQuot (square a) = (toQuot a)^2
```

`BF128Ghash.toQuot_powTwoPow` (lemma, [line 484](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L484))

```lean
lemma toQuot_powTwoPow (a : ConcreteBF128Ghash) (k : Nat) :
    toQuot (powTwoPow a k) = (toQuot a)^(2^k)
```

`BF128Ghash.target_val` (definition, [line 495](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L495))

> The target value for step k: a^(2^k - 1)

```lean
noncomputable def target_val (a : PolyQuot) (k : ℕ) : PolyQuot
```

`BF128Ghash.itoh_tsujii_step` (lemma, [line 500](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L500))

> Fundamental Itoh-Tsujii Step Lemma:
> If `x = a^(2^n - 1)` and `y = a^(2^m - 1)`, then `(x^(2^m)) * y = a^(2^(n+m) - 1)`.
> This corresponds to the code `(powTwoPow u_n m) * u_m`.

```lean
lemma itoh_tsujii_step {a x y : PolyQuot} {n m : ℕ}
    (hn : n > 0) (hm : m > 0) (hx : x = target_val a n) (hy : y = target_val a m) :
    x^(2^m) * y = target_val a (n + m)
```

`BF128Ghash.toQuot_invItohTsujii` (lemma, [line 544](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L544))

```lean
lemma toQuot_invItohTsujii (a : ConcreteBF128Ghash) (h_ne : a ≠ 0) :
    toQuot (invItohTsujii a) = (toQuot a)^(2^128 - 2)
```

`BF128Ghash.pow_2k` (alias, [line 611](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L611))

```lean
alias pow_2k
```

`BF128Ghash.inv_itoh_tsujii` (alias, [line 612](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L612))

```lean
alias inv_itoh_tsujii
```

`BF128Ghash.toQuot_pow_2k` (alias, [line 613](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L613))

```lean
alias toQuot_pow_2k
```

`BF128Ghash.toQuot_inv_itoh_tsujii` (alias, [line 614](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L614))

```lean
alias toQuot_inv_itoh_tsujii
```

`BF128Ghash.exists_pair_ne` (lemma, [line 620](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L620))

```lean
lemma exists_pair_ne : ∃ x y : ConcreteBF128Ghash, x ≠ y
```

`BF128Ghash.mul_inv_cancel` (lemma, [line 623](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L623))

```lean
lemma mul_inv_cancel (a : ConcreteBF128Ghash) (h : a ≠ 0) : a * a⁻¹ = 1
```

`BF128Ghash.mul_comm` (lemma, [line 641](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L641))

```lean
lemma mul_comm (a b : ConcreteBF128Ghash) : a * b = b * a
```

> ### Field instance
>
> The field structure retains the explicit arithmetic, including the total inversion chain.
> Both natural and integer powers use binary exponentiation.

`BF128Ghash.isField_concrete` (theorem, [line 652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L652))

```lean
theorem isField_concrete : IsField ConcreteBF128Ghash
```

`BF128Ghash.instFieldConcreteBF128Ghash` (instance, [line 658](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L658))

> The GHASH field with executable inversion, division, and binary exponentiation.

```lean
instance instFieldConcreteBF128Ghash : Field ConcreteBF128Ghash
```

`BF128Ghash.instDivisionRingConcreteBF128Ghash` (abbreviation, [line 675](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L675))

> Compatibility name for the division ring inherited from the field.

```lean
abbrev instDivisionRingConcreteBF128Ghash : DivisionRing ConcreteBF128Ghash
```

`BF128Ghash.inv_def` (theorem, [line 679](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L679))

> Inversion is the total Itoh-Tsujii algorithm, including at zero.

```lean
theorem inv_def (a : ConcreteBF128Ghash) : a⁻¹ = invItohTsujii a
```

`BF128Ghash.div_def` (theorem, [line 682](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L682))

> Division multiplies by the total Itoh-Tsujii inverse of the denominator.

```lean
theorem div_def (a b : ConcreteBF128Ghash) : a / b = a * invItohTsujii b
```

`BF128Ghash.npow_def` (theorem, [line 685](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L685))

> Natural powers use binary exponentiation.

```lean
theorem npow_def (a : ConcreteBF128Ghash) (n : ℕ) : a ^ n = npowBinRec n a
```

`BF128Ghash.zpow_def` (theorem, [line 688](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L688))

> Integer powers use binary exponentiation and invert the result for negative exponents.

```lean
theorem zpow_def (a : ConcreteBF128Ghash) (n : ℤ) :
    a ^ n = zpowRec npowBinRecAuto n a
```

`BF128Ghash.toQuot_inv` (theorem, [line 692](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean#L692))

> The quotient interpretation preserves inversion, including at zero.

```lean
theorem toQuot_inv (a : ConcreteBF128Ghash) : toQuot a⁻¹ = (toQuot a)⁻¹
```

## Depends on

- [GHASH polynomial-basis arithmetic](arithmetic.md)
- [BinaryField128Ghash](basic.md)

## Sources

- [CompPoly/Fields/Binary/BF128Ghash/Impl.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF128Ghash/Impl.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Fields.Binary.BF128Ghash.Impl.json)
