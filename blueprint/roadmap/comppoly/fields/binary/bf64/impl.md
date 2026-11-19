---
catalog: module
lean: BF64, BF64.ofBitVec, BF64.toBitVec_ofBitVec, BF64.ofBitVec_toBitVec, BF64.toBitVec_injective, BF64.ext, BF64.equivBitVec, BF64.toBitVec_zero, BF64.toBitVec_one, BF64.mul, BF64.toPolyBF64, BF64.toQuot, BF64.add_def, BF64.mul_def, BF64.toBitVec_mul, BF64.toPolyBF64_zero, BF64.toQuot_zero, BF64.toPolyBF64_add, BF64.toQuot_add, BF64.toQuot_mul, BF64.toQuot_injective, BF64.toPolyBF64_one, BF64.toQuot_one, BF64.toQuot_inj, BF64.add_self, BF64.natCast, BF64.natCast_succ, BF64.npow_def, BF64.toQuot_neg, BF64.toQuot_sub, BF64.npow_eq_npowRec, BF64.toQuot_npow, BF64.toQuot_natCast, BF64.powTwoPow, BF64.toQuot_powTwoPow, BF64.invItohTsujii, BF64.toQuot_invItohTsujii, BF64.toQuot_eq_zero_iff, BF64.exists_pair_ne, BF64.equivFin, BF64.nat_card_bf64, BF64.card_bf64, BF64.toQuot_surjective, BF64.mul_invItohTsujii, BF64.exists_mul_inv, BF64.inv_def, BF64.div_def, BF64.inv_zero_bf64, BF64.isField_bf64
statement: formalized
proof: formalized
---

# The computable `GF(2^64)` carrier

`CompPoly.Fields.Binary.BF64.Impl`, in [CompPoly/Fields/Binary/BF64/Impl.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean), by Nicolas Schleicher.

> An element stores a 64-bit word whose bit `i` is the coefficient of `x^i`. Addition is `xor`,
> multiplication is a carry-less product followed by `reduce`, and inversion is the
> Itoh-Tsujii addition chain. The carrier maps into `AdjoinRoot basePoly` through
> `BF64.toQuot`, so Mathlib's field theory applies while the operations stay executable.
> The nominal carrier separates this polynomial presentation from raw words and binary towers.
> `ofBitVec` and `toBitVec` expose its coordinates; field numerals use characteristic-two casts.
> Finiteness is supplied as a proposition, with cardinality stated using `Nat.card`. Enumeration
> is an explicit proof-side choice and is never constructed during native module startup.
>
> ## Main definitions
>
> * `BF64` — the nominal carrier with `Add`, `Mul`, `Inv`, `CommRing` and `Field`.
> * `BF64.ofBitVec`, `BF64.toBitVec` — explicit maps to and from its 64-bit coordinates.
> * `BF64.toQuot` — the bridge into `BF64Quot`.
> * `BF64.powTwoPow` — repeated squaring, `a ^ (2 ^ k)`.
> * `BF64.invItohTsujii` — inversion by the Itoh-Tsujii addition chain.
>
> ## Main statements
>
> * `BF64.toQuot_add`, `BF64.toQuot_mul` — the bridge is a ring homomorphism.
> * `BF64.toQuot_injective`, `BF64.toQuot_surjective` — it is a bijection.
> * `BF64.mul_invItohTsujii` — the addition chain really inverts.
> * `BF64.nat_card_bf64` — `Nat.card BF64 = 2 ^ 64`.
>
> ## Implementation notes
>
> The algebraic instances are written out field-by-field rather than obtained from
> `Function.Injective.commRing`. That transport takes the bridge map as *data*, which makes
> the whole structure noncomputable and shadows the computable `Mul` and `Pow`; because
> `CompPoly.Extension.Ext.mul` reaches through the base field's `Field` instance, a
> noncomputable base field would take the extension in `BF64/Ext3.lean` down with it too.
> The `#guard` checks in `tests/CompPolyTests/Fields/Binary/BF64.lean` run the compiled
> arithmetic and so fail the build if this ever regresses.
>
> `Pow` is `npowBinRec`, binary exponentiation, matching
> `CompPoly.Extension.Ext.instPowNat`. The linear `npowRec` would need `2 ^ 64`
> multiplications for a full-order exponent and is unusable in the kernel.

`BF64` (structure, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L58))

> An element of `GF(2)[X] / (X^64 + X^4 + X^3 + X + 1)`, stored in a polynomial basis.

```lean
structure BF64 where
  /-- Bit `i` is the coefficient of `X^i`. -/
  toBitVec : BitVec 64
  deriving DecidableEq, BEq
```

`BF64.ofBitVec` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L66))

> Construct a field element from its polynomial-basis bits.

```lean
def ofBitVec (a : BitVec 64) : BF64
```

`BF64.toBitVec_ofBitVec` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L69))

> Reading the coordinates of a constructed element recovers the input word.

```lean
theorem toBitVec_ofBitVec (a : BitVec 64) : (ofBitVec a).toBitVec = a
```

`BF64.ofBitVec_toBitVec` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L72))

> Reconstructing an element from its coordinates recovers that element.

```lean
theorem ofBitVec_toBitVec (a : BF64) : ofBitVec a.toBitVec = a
```

`BF64.toBitVec_injective` (theorem, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L75))

> Polynomial-basis bits uniquely determine a field element.

```lean
theorem toBitVec_injective : Function.Injective toBitVec
```

`BF64.ext` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L83))

> Elements with equal polynomial-basis coordinates are equal.

```lean
theorem ext {a b : BF64} (h : a.toBitVec = b.toBitVec) : a = b
```

`BF64.equivBitVec` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L87))

> The equivalence between field elements and their polynomial-basis coordinates.

```lean
def equivBitVec : BF64 ≃ BitVec 64
```

`BF64.toBitVec_zero` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L106))

> Zero has every polynomial-basis coefficient equal to zero.

```lean
theorem toBitVec_zero : (0 : BF64).toBitVec = 0#64
```

`BF64.toBitVec_one` (theorem, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L109))

> One has only its constant coefficient equal to one.

```lean
theorem toBitVec_one : (1 : BF64).toBitVec = 1#64
```

`BF64.mul` (definition, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L120))

> Multiply by reducing the carry-less product of the polynomial-basis words.

```lean
def mul (a b : BF64) : BF64
```

`BF64.toPolyBF64` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L126))

> The polynomial denoted by a carrier value.

```lean
noncomputable def toPolyBF64 (a : BF64) : Polynomial (ZMod 2)
```

`BF64.toQuot` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L130))

> The bridge into the quotient.

```lean
noncomputable def toQuot (a : BF64) : BF64Quot
```

> ## Equation lemmas for the operations

`BF64.add_def` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L136))

> Addition unfolds to `xor`.

```lean
theorem add_def (a b : BF64) : a + b = ofBitVec (a.toBitVec ^^^ b.toBitVec)
```

`BF64.mul_def` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L139))

> Multiplication uses the named executable product.

```lean
theorem mul_def (a b : BF64) : a * b = mul a b
```

`BF64.toBitVec_mul` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L142))

> The product word is the reduced carry-less product of the input words.

```lean
theorem toBitVec_mul (a b : BF64) :
    (a * b).toBitVec = reduce (carryLessMul (w := 128) a.toBitVec b.toBitVec)
```

> ## The bridge is a ring homomorphism

`BF64.toPolyBF64_zero` (theorem, [line 147](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L147))

```lean
theorem toPolyBF64_zero : toPolyBF64 0 = 0
```

`BF64.toQuot_zero` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L151))

```lean
theorem toQuot_zero : toQuot 0 = 0
```

`BF64.toPolyBF64_add` (theorem, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L154))

```lean
theorem toPolyBF64_add (a b : BF64) :
    toPolyBF64 (a + b) = toPolyBF64 a + toPolyBF64 b
```

`BF64.toQuot_add` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L159))

```lean
theorem toQuot_add (a b : BF64) : toQuot (a + b) = toQuot a + toQuot b
```

`BF64.toQuot_mul` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L163))

> Multiplication agrees with the quotient's, because `reduce` computes the remainder.

```lean
theorem toQuot_mul (a b : BF64) : toQuot (a * b) = toQuot a * toQuot b
```

`BF64.toQuot_injective` (theorem, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L174))

> Distinct carrier values denote distinct quotient elements.
>
> A difference of two carrier values has degree below 64, while the modulus has degree
> exactly 64, so the modulus can divide it only when it is zero.

```lean
theorem toQuot_injective : Function.Injective toQuot
```

> ## Algebraic structure
>
> Every law is discharged by pushing through the injective `toQuot` into the quotient,
> where it holds because `BF64Quot` is a commutative ring. The instances are
> built field-by-field rather than by `Function.Injective.commRing`, because that transport
> takes `toQuot` as data and would make the operations noncomputable.

`BF64.toPolyBF64_one` (theorem, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L200))

```lean
theorem toPolyBF64_one : toPolyBF64 1 = 1
```

`BF64.toQuot_one` (theorem, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L203))

```lean
theorem toQuot_one : toQuot 1 = 1
```

`BF64.toQuot_inj` (theorem, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L206))

```lean
theorem toQuot_inj {a b : BF64} : toQuot a = toQuot b ↔ a = b
```

`BF64.add_self` (theorem, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L210))

> Addition is self-cancelling: the field has characteristic two.

```lean
theorem add_self (a : BF64) : a + a = 0
```

> ### Scalar and power operations
>
> Scalar multiples use the additive recursion. Natural casts use parity, and integer casts
> use the corresponding natural cast and negation. Raw polynomial-basis words enter through
> `ofBitVec`, independently of numeral casting.

`BF64.natCast` (definition, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L225))

> Cast a natural number by its parity in characteristic two.

```lean
def natCast (n : ℕ) : BF64
```

`BF64.natCast_succ` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L230))

> Casting a successor adds the multiplicative unit.

```lean
theorem natCast_succ (n : ℕ) : natCast (n + 1) = natCast n + 1
```

`BF64.npow_def` (theorem, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L238))

```lean
theorem npow_def (a : BF64) (n : ℕ) : a ^ n = npowBinRec n a
```

> ### The commutative-ring structure
>
> Every law is discharged by pushing through the injective `toQuot` into `BF64Quot`,
> where it holds because the quotient is a commutative ring. The instances are written out
> field-by-field rather than via `Function.Injective.commRing`: that transport takes `toQuot`
> as *data*, which would make the whole structure noncomputable and shadow the computable
> operations. This mirrors `CompPoly.Extension.Ext.instCommRing`.

`BF64.toQuot_neg` (theorem, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L249))

```lean
theorem toQuot_neg (a : BF64) : toQuot (-a) = -toQuot a
```

`BF64.toQuot_sub` (theorem, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L253))

```lean
theorem toQuot_sub (a b : BF64) : toQuot (a - b) = toQuot a - toQuot b
```

`BF64.npow_eq_npowRec` (theorem, [line 281](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L281))

> `npowBinRec` agrees with the linear `npowRec`, so the power can be reasoned about by
> ordinary recursion on the exponent while still *evaluating* by binary exponentiation.
> Mathlib's `npowBinRec_succ` needs a `Semigroup`, which is not available until `mul_assoc`
> below, so associativity is supplied here from the quotient.

```lean
theorem npow_eq_npowRec (a : BF64) (n : ℕ) : a ^ n = npowRec n a
```

`BF64.toQuot_npow` (theorem, [line 287](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L287))

```lean
theorem toQuot_npow (a : BF64) (n : ℕ) : toQuot (a ^ n) = toQuot a ^ n
```

`BF64.toQuot_natCast` (theorem, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L297))

```lean
theorem toQuot_natCast (n : ℕ) : toQuot (n : BF64) = (n : BF64Quot)
```

> ### Inversion by Itoh-Tsujii
>
> Inversion uses the Itoh-Tsujii addition chain: `a⁻¹ = a^(2^64 - 2) = (a^(2^63 - 1))^2`,
> with `a^(2^k - 1)` built along `1, 2, 3, 6, 7, 14, 15, 30, 31, 62, 63`. This is an
> explicit algorithm rather than an existence proof, so the resulting inverse evaluates.
> `BF128Ghash.inv_itoh_tsujii` is the analogous chain at degree 128.

`BF64.powTwoPow` (definition, [line 334](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L334))

> Repeated squaring: `a ^ (2 ^ k)`.

```lean
def powTwoPow (a : BF64) (k : ℕ) : BF64
```

`BF64.toQuot_powTwoPow` (theorem, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L339))

```lean
theorem toQuot_powTwoPow (a : BF64) (k : ℕ) :
    toQuot (powTwoPow a k) = toQuot a ^ (2 ^ k)
```

`BF64.invItohTsujii` (definition, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L348))

> The multiplicative inverse, by the Itoh-Tsujii addition chain, with `0⁻¹ = 0`.

```lean
def invItohTsujii (a : BF64) : BF64
```

`BF64.toQuot_invItohTsujii` (theorem, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L389))

> The Itoh-Tsujii chain computes `a ^ (2 ^ 64 - 2)`.

```lean
theorem toQuot_invItohTsujii (a : BF64) (h : a ≠ 0) :
    toQuot (invItohTsujii a) = toQuot a ^ (2 ^ 64 - 2)
```

> ### The field structure
>
> `BF64Quot` is a field because `basePoly` is irreducible, and `toQuot` is an
> injective ring homomorphism onto it, so the carrier is a field too. Following
> `CompPoly.Extension.Ext.instField`, the structure is assembled field-by-field so that every
> operation stays computable.

`BF64.toQuot_eq_zero_iff` (theorem, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L445))

```lean
theorem toQuot_eq_zero_iff {a : BF64} : toQuot a = 0 ↔ a = 0
```

`BF64.exists_pair_ne` (theorem, [line 449](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L449))

```lean
theorem exists_pair_ne : ∃ x y : BF64, x ≠ y
```

`BF64.equivFin` (definition, [line 453](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L453))

> The carrier is in bijection with `Fin (2 ^ 64)`, by its underlying representation.

```lean
def equivFin : BF64 ≃ Fin (2 ^ 64)
```

`BF64.nat_card_bf64` (theorem, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L462))

> `BF64` has `2 ^ 64` elements, independently of an enumeration.

```lean
theorem nat_card_bf64 : Nat.card BF64 = 2 ^ 64
```

`BF64.card_bf64` (theorem, [line 468](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L468))

> Any enumeration of `BF64` has `2 ^ 64` elements.

```lean
theorem card_bf64 [Fintype BF64] : Fintype.card BF64 = 2 ^ 64
```

`BF64.toQuot_surjective` (theorem, [line 472](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L472))

> The bridge is surjective: it is injective between finite types of equal cardinality.

```lean
theorem toQuot_surjective : Function.Surjective toQuot
```

`BF64.mul_invItohTsujii` (theorem, [line 477](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L477))

> The Itoh-Tsujii inverse really is a multiplicative inverse.

```lean
theorem mul_invItohTsujii {a : BF64} (h : a ≠ 0) : a * invItohTsujii a = 1
```

`BF64.exists_mul_inv` (theorem, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L488))

> Every nonzero carrier value has a multiplicative inverse.

```lean
theorem exists_mul_inv {a : BF64} (h : a ≠ 0) : ∃ b : BF64, a * b = 1
```

`BF64.inv_def` (theorem, [line 497](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L497))

> Inversion unfolds to the Itoh-Tsujii chain.

```lean
theorem inv_def (a : BF64) : a⁻¹ = invItohTsujii a
```

`BF64.div_def` (theorem, [line 500](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L500))

> Division unfolds to multiplication by the Itoh-Tsujii inverse.

```lean
theorem div_def (a b : BF64) : a / b = a * invItohTsujii b
```

`BF64.inv_zero_bf64` (theorem, [line 502](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L502))

```lean
theorem inv_zero_bf64 : (0 : BF64)⁻¹ = 0
```

`BF64.isField_bf64` (theorem, [line 506](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean#L506))

> `BF64` satisfies `IsField`, the bundled-data-free form of the field axioms.

```lean
theorem isField_bf64 : IsField BF64
```

## Depends on

- [Reducing a carry-less product modulo the `GF(2^64)` modulus](reduce.md)

## Sources

- [CompPoly/Fields/Binary/BF64/Impl.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Impl.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.BF64.Impl.json)
