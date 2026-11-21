---
catalog: module
lean: Montgomery.Native64x8.Mont64x8Field, Montgomery.Native64x8.Mont64x8Field.modulus_pos, Montgomery.Native64x8.Mont64x8Field.modulus_lt, Montgomery.Native64x8.Mont64x8Field.q_toNat, Montgomery.Native64x8.Mont64x8Field.negInv_mul_q, Montgomery.Native64x8.Mont64x8Field.two_ne_zero, Montgomery.Native64x8.Mont64x8Field.r_ne_zero, Montgomery.Native64x8.FastField, Montgomery.Native64x8.FastField.val_bounded, Montgomery.Native64x8.FastField.val_lt, Montgomery.Native64x8.FastField.zero, Montgomery.Native64x8.FastField.one, Montgomery.Native64x8.FastField.add, Montgomery.Native64x8.FastField.sub, Montgomery.Native64x8.FastField.neg, Montgomery.Native64x8.FastField.mul, Montgomery.Native64x8.FastField.square, Montgomery.Native64x8.FastField.pow, Montgomery.Native64x8.FastField.inv, Montgomery.Native64x8.FastField.div, Montgomery.Native64x8.FastField.toLimbs8, Montgomery.Native64x8.FastField.toNat, Montgomery.Native64x8.FastField.toField, Montgomery.Native64x8.FastField.ofCanonicalNat, Montgomery.Native64x8.FastField.ofNat, Montgomery.Native64x8.FastField.ofField, Montgomery.Native64x8.FastField.ofInt, Montgomery.Native64x8.FastField.zero_def, Montgomery.Native64x8.FastField.one_def, Montgomery.Native64x8.FastField.add_def, Montgomery.Native64x8.FastField.neg_def, Montgomery.Native64x8.FastField.sub_def, Montgomery.Native64x8.FastField.mul_def, Montgomery.Native64x8.FastField.inv_def, Montgomery.Native64x8.FastField.div_def, Montgomery.Native64x8.FastField.square_def, Montgomery.Native64x8.FastField.toNat_lt, Montgomery.Native64x8.FastField.toField_ofCanonicalNat, Montgomery.Native64x8.FastField.toNat_ofCanonicalNat, Montgomery.Native64x8.FastField.toField_ofField, Montgomery.Native64x8.FastField.ofField_toField, Montgomery.Native64x8.FastField.toField_injective, Montgomery.Native64x8.FastField.toField_zero, Montgomery.Native64x8.FastField.toField_one, Montgomery.Native64x8.FastField.toField_add, Montgomery.Native64x8.FastField.toField_sub, Montgomery.Native64x8.FastField.toField_neg, Montgomery.Native64x8.FastField.toField_mul, Montgomery.Native64x8.FastField.toField_square, Montgomery.Native64x8.FastField.toField_pow, Montgomery.Native64x8.FastField.toField_inv, Montgomery.Native64x8.FastField.toField_div, Montgomery.Native64x8.FastField.toField_natCast, Montgomery.Native64x8.FastField.toField_intCast, Montgomery.Native64x8.FastField.toField_nsmul, Montgomery.Native64x8.FastField.toField_zsmul, Montgomery.Native64x8.FastField.toField_npow, Montgomery.Native64x8.FastField.toField_zpow, Montgomery.Native64x8.FastField.toField_nnratCast, Montgomery.Native64x8.FastField.toField_ratCast, Montgomery.Native64x8.FastField.toField_nnqsmul, Montgomery.Native64x8.FastField.toField_qsmul, Montgomery.Native64x8.FastField.ringEquiv, Montgomery.Native64x8.FastField.ringEquiv_apply, Montgomery.Native64x8.FastField.ringEquiv_symm_apply, Montgomery.Native64x8.FastField.instField, Montgomery.Native64x8.FastField.instNonBinaryField
statement: formalized
proof: formalized
---

# Fast eight-limb Montgomery fields

`CompPoly.Fields.Montgomery.Native64x8Field`, in [CompPoly/Fields/Montgomery/Native64x8Field.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean), by Gregor Mitscha-Baude.

> The bounded carrier, conversions, arithmetic, and field instances built on the raw eight-limb
> Montgomery operations of `Montgomery/Native64x8`.  This is the multi-limb analogue of
> `Montgomery/Native32Field`, for any prime modulus below `2 ^ 256`.
>
> A carrier element stores the Montgomery residue `x * 2 ^ 256 mod q` as eight 32-bit limbs;
> `toField` divides that residue by `2 ^ 256` again and lands in `ZMod modulus`.  All arithmetic
> is transported along `toField`, which is a ring isomorphism onto `ZMod modulus`.
>
> ## Main results
>
> * `FastField` — the carrier, `{ x : Limbs8 // x.Bounded ∧ x.toNat < modulus }`
> * `toField_add`, `toField_mul`, … — `@[simp]` equivalences with the canonical field
> * `Mont64x8Field` — the per-field constants class
> * `ringEquiv`, `instField` — the ring isomorphism and the transferred `Field` instance

> ## Per-field constants

`Montgomery.Native64x8.Mont64x8Field` (class, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L41))

> Per-field data for a fast eight-limb Montgomery field with radix `R = 2 ^ 256`.  All
> side conditions are concrete numeral facts, discharged by `decide` at instantiation.

```lean
class Mont64x8Field (modulus : ℕ) where
  /-- `modulus` is prime. -/
  prime : modulus.Prime
  /-- The modulus in eight 32-bit limbs. -/
  modulusLimbs : Limbs8
  /-- `2 ^ 256 mod modulus`, the Montgomery representation of one. -/
  rModModulus : Limbs8
  /-- `(2 ^ 256) ^ 2 mod modulus`, used to enter Montgomery form. -/
  r2ModModulus : Limbs8
  /-- `-modulus⁻¹ mod 2 ^ 32`, used by Montgomery reduction. -/
  montgomeryNegInv : UInt64
  modulusLimbs_bounded : modulusLimbs.Bounded := by decide
  modulusLimbs_toNat : modulusLimbs.toNat = modulus := by decide
  two_lt_modulus : 2 < modulus := by decide
  rModModulus_bounded : rModModulus.Bounded := by decide
  rModModulus_toNat : rModModulus.toNat = 2 ^ 256 % modulus := by decide
  r2ModModulus_bounded : r2ModModulus.Bounded := by decide
  r2ModModulus_toNat : r2ModModulus.toNat = (2 ^ 256) ^ 2 % modulus := by decide
  montgomeryNegInv_lt : montgomeryNegInv.toNat < 2 ^ 32 := by decide
  montgomeryNegInv_mul_modulus_mod_two_pow_32 :
    montgomeryNegInv.toNat * modulus % 2 ^ 32 = 2 ^ 32 - 1 := by decide
```

> ## Modulus facts

`Montgomery.Native64x8.Mont64x8Field.modulus_pos` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L71))

```lean
theorem modulus_pos : 0 < modulus
```

`Montgomery.Native64x8.Mont64x8Field.modulus_lt` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L73))

```lean
theorem modulus_lt : modulus < 2 ^ 256
```

`Montgomery.Native64x8.Mont64x8Field.q_toNat` (theorem, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L77))

```lean
theorem q_toNat : P.modulusLimbs.toNat = modulus
```

`Montgomery.Native64x8.Mont64x8Field.negInv_mul_q` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L79))

```lean
theorem negInv_mul_q : P.montgomeryNegInv.toNat * P.modulusLimbs.toNat % 2 ^ 32 = 2 ^ 32 - 1
```

`Montgomery.Native64x8.Mont64x8Field.two_ne_zero` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L85))

```lean
theorem two_ne_zero : (2 : ZMod modulus) ≠ 0
```

`Montgomery.Native64x8.Mont64x8Field.r_ne_zero` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L90))

```lean
theorem r_ne_zero : ((2 ^ 256 : ℕ) : ZMod modulus) ≠ 0
```

> ## The carrier

`Montgomery.Native64x8.FastField` (definition, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L101))

> The fast carrier for a prime modulus: eight 32-bit limbs holding a value below `modulus`,
> interpreted as a Montgomery residue.  At runtime this erases to `Limbs8`.

```lean
def FastField (modulus : ℕ) [Mont64x8Field modulus] : Type
```

`Montgomery.Native64x8.FastField.val_bounded` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L113))

```lean
theorem val_bounded (x : FastField modulus) : x.val.Bounded
```

`Montgomery.Native64x8.FastField.val_lt` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L115))

```lean
theorem val_lt (x : FastField modulus) : x.val.toNat < P.modulusLimbs.toNat
```

> ### Arithmetic

`Montgomery.Native64x8.FastField.zero` (definition, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L122))

> The zero element.

```lean
def zero (modulus : ℕ) [P : Mont64x8Field modulus] : FastField modulus
```

`Montgomery.Native64x8.FastField.one` (definition, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L128))

> The one element, the Montgomery residue `2 ^ 256 mod modulus`.

```lean
def one (modulus : ℕ) [P : Mont64x8Field modulus] : FastField modulus
```

`Montgomery.Native64x8.FastField.add` (definition, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L134))

> Fast modular addition in Montgomery form.

```lean
def add (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.sub` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L142))

> Fast modular subtraction in Montgomery form.

```lean
def sub (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.neg` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L150))

> Fast modular negation in Montgomery form.

```lean
def neg (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.mul` (definition, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L157))

> Fast Montgomery multiplication.

```lean
def mul (x y : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.square` (definition, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L167))

> Fast squaring.

```lean
def square (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.pow` (definition, [line 170](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L170))

> Exponentiation by repeated squaring.

```lean
def pow (x : FastField modulus) (n : ℕ) : FastField modulus
```

`Montgomery.Native64x8.FastField.inv` (definition, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L174))

> Inversion by Fermat's little theorem, `x⁻¹ = x ^ (modulus - 2)`.

```lean
def inv (x : FastField modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.div` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L177))

> Division through inversion.

```lean
def div (x y : FastField modulus) : FastField modulus
```

> ### Conversions

`Montgomery.Native64x8.FastField.toLimbs8` (definition, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L182))

> The canonical limb representative of a fast element: one Montgomery reduction.

```lean
def toLimbs8 (x : FastField modulus) : Limbs8
```

`Montgomery.Native64x8.FastField.toNat` (definition, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L186))

> The canonical natural representative of a fast element.

```lean
def toNat (x : FastField modulus) : ℕ
```

`Montgomery.Native64x8.FastField.toField` (definition, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L189))

> The canonical `ZMod` value of a fast element.

```lean
def toField (x : FastField modulus) : ZMod modulus
```

`Montgomery.Native64x8.FastField.ofCanonicalNat` (definition, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L192))

> Build a fast element from a canonical natural representative.

```lean
def ofCanonicalNat (n : ℕ) (h : n < modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.ofNat` (definition, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L210))

> Convert a natural number into fast Montgomery form.

```lean
def ofNat (modulus : ℕ) [P : Mont64x8Field modulus] (n : ℕ) : FastField modulus
```

`Montgomery.Native64x8.FastField.ofField` (definition, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L214))

> Convert from the canonical field into fast Montgomery form.

```lean
def ofField (x : ZMod modulus) : FastField modulus
```

`Montgomery.Native64x8.FastField.ofInt` (definition, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L218))

> Convert an integer into fast Montgomery form.

```lean
def ofInt (modulus : ℕ) [P : Mont64x8Field modulus] (n : Int) :
    FastField modulus
```

`Montgomery.Native64x8.FastField.zero_def` (theorem, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L246))

```lean
theorem zero_def : (0 : FastField modulus) = FastField.zero modulus
```

`Montgomery.Native64x8.FastField.one_def` (theorem, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L247))

```lean
theorem one_def : (1 : FastField modulus) = FastField.one modulus
```

`Montgomery.Native64x8.FastField.add_def` (theorem, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L248))

```lean
theorem add_def (x y : FastField modulus) : x + y = FastField.add x y
```

`Montgomery.Native64x8.FastField.neg_def` (theorem, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L249))

```lean
theorem neg_def (x : FastField modulus) : -x = FastField.neg x
```

`Montgomery.Native64x8.FastField.sub_def` (theorem, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L250))

```lean
theorem sub_def (x y : FastField modulus) : x - y = FastField.sub x y
```

`Montgomery.Native64x8.FastField.mul_def` (theorem, [line 251](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L251))

```lean
theorem mul_def (x y : FastField modulus) : x * y = FastField.mul x y
```

`Montgomery.Native64x8.FastField.inv_def` (theorem, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L252))

```lean
theorem inv_def (x : FastField modulus) : x⁻¹ = FastField.inv x
```

`Montgomery.Native64x8.FastField.div_def` (theorem, [line 253](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L253))

```lean
theorem div_def (x y : FastField modulus) : x / y = x * y⁻¹
```

`Montgomery.Native64x8.FastField.square_def` (theorem, [line 254](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L254))

```lean
theorem square_def (x : FastField modulus) : FastField.square x = x * x
```

> ## Correctness

`Montgomery.Native64x8.FastField.toNat_lt` (theorem, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L297))

```lean
theorem toNat_lt (x : FastField modulus) : toNat x < modulus
```

`Montgomery.Native64x8.FastField.toField_ofCanonicalNat` (theorem, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L316))

```lean
theorem toField_ofCanonicalNat {n : ℕ} (h : n < modulus) :
    toField (ofCanonicalNat n h) = (n : ZMod modulus)
```

`Montgomery.Native64x8.FastField.toNat_ofCanonicalNat` (theorem, [line 322](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L322))

```lean
theorem toNat_ofCanonicalNat {n : ℕ} (h : n < modulus) : toNat (ofCanonicalNat n h) = n
```

`Montgomery.Native64x8.FastField.toField_ofField` (theorem, [line 327](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L327))

> Converting from the canonical field to fast form and back is the identity.

```lean
theorem toField_ofField (x : ZMod modulus) : toField (ofField x) = x
```

`Montgomery.Native64x8.FastField.ofField_toField` (theorem, [line 332](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L332))

> Converting from fast form to the canonical field and back is the identity.

```lean
theorem ofField_toField (x : FastField modulus) : ofField (toField x) = x
```

`Montgomery.Native64x8.FastField.toField_injective` (theorem, [line 343](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L343))

> The canonical-field interpretation distinguishes fast values.

```lean
theorem toField_injective : Function.Injective (toField (modulus := modulus))
```

> ### Field operations

`Montgomery.Native64x8.FastField.toField_zero` (theorem, [line 349](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L349))

```lean
theorem toField_zero : toField (0 : FastField modulus) = 0
```

`Montgomery.Native64x8.FastField.toField_one` (theorem, [line 354](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L354))

```lean
theorem toField_one : toField (1 : FastField modulus) = 1
```

`Montgomery.Native64x8.FastField.toField_add` (theorem, [line 360](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L360))

```lean
theorem toField_add (x y : FastField modulus) : toField (x + y) = toField x + toField y
```

`Montgomery.Native64x8.FastField.toField_sub` (theorem, [line 368](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L368))

```lean
theorem toField_sub (x y : FastField modulus) : toField (x - y) = toField x - toField y
```

`Montgomery.Native64x8.FastField.toField_neg` (theorem, [line 377](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L377))

```lean
theorem toField_neg (x : FastField modulus) : toField (-x) = -toField x
```

`Montgomery.Native64x8.FastField.toField_mul` (theorem, [line 385](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L385))

```lean
theorem toField_mul (x y : FastField modulus) : toField (x * y) = toField x * toField y
```

`Montgomery.Native64x8.FastField.toField_square` (theorem, [line 401](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L401))

```lean
theorem toField_square (x : FastField modulus) : toField (square x) = toField x * toField x
```

`Montgomery.Native64x8.FastField.toField_pow` (theorem, [line 405](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L405))

```lean
theorem toField_pow (x : FastField modulus) (n : ℕ) : toField (pow x n) = toField x ^ n
```

`Montgomery.Native64x8.FastField.toField_inv` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L431))

```lean
theorem toField_inv (x : FastField modulus) : toField x⁻¹ = (toField x)⁻¹
```

`Montgomery.Native64x8.FastField.toField_div` (theorem, [line 440](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L440))

```lean
theorem toField_div (x y : FastField modulus) : toField (x / y) = toField x / toField y
```

`Montgomery.Native64x8.FastField.toField_natCast` (theorem, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L445))

```lean
theorem toField_natCast (n : ℕ) : toField (n : FastField modulus) = (n : ZMod modulus)
```

`Montgomery.Native64x8.FastField.toField_intCast` (theorem, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L451))

```lean
theorem toField_intCast (n : Int) : toField (n : FastField modulus) = (n : ZMod modulus)
```

`Montgomery.Native64x8.FastField.toField_nsmul` (theorem, [line 456](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L456))

```lean
theorem toField_nsmul (n : ℕ) (x : FastField modulus) : toField (n • x) = n • toField x
```

`Montgomery.Native64x8.FastField.toField_zsmul` (theorem, [line 461](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L461))

```lean
theorem toField_zsmul (n : Int) (x : FastField modulus) : toField (n • x) = n • toField x
```

`Montgomery.Native64x8.FastField.toField_npow` (theorem, [line 466](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L466))

```lean
theorem toField_npow (x : FastField modulus) (n : ℕ) : toField (x ^ n) = toField x ^ n
```

`Montgomery.Native64x8.FastField.toField_zpow` (theorem, [line 471](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L471))

```lean
theorem toField_zpow (x : FastField modulus) (n : Int) : toField (x ^ n) = toField x ^ n
```

`Montgomery.Native64x8.FastField.toField_nnratCast` (theorem, [line 485](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L485))

```lean
theorem toField_nnratCast (q : ℚ≥0) : toField (q : FastField modulus) = (q : ZMod modulus)
```

`Montgomery.Native64x8.FastField.toField_ratCast` (theorem, [line 490](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L490))

```lean
theorem toField_ratCast (q : ℚ) : toField (q : FastField modulus) = (q : ZMod modulus)
```

`Montgomery.Native64x8.FastField.toField_nnqsmul` (theorem, [line 495](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L495))

```lean
theorem toField_nnqsmul (q : ℚ≥0) (x : FastField modulus) : toField (q • x) = q • toField x
```

`Montgomery.Native64x8.FastField.toField_qsmul` (theorem, [line 500](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L500))

```lean
theorem toField_qsmul (q : ℚ) (x : FastField modulus) : toField (q • x) = q • toField x
```

> ### Algebraic structure

`Montgomery.Native64x8.FastField.ringEquiv` (definition, [line 507](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L507))

> Ring equivalence between the fast Montgomery representation and the canonical field.

```lean
def ringEquiv (modulus : ℕ) [P : Mont64x8Field modulus] :
    FastField modulus ≃+* ZMod modulus
```

`Montgomery.Native64x8.FastField.ringEquiv_apply` (theorem, [line 517](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L517))

```lean
theorem ringEquiv_apply {x : FastField modulus} : ringEquiv modulus x = toField x
```

`Montgomery.Native64x8.FastField.ringEquiv_symm_apply` (theorem, [line 520](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L520))

```lean
theorem ringEquiv_symm_apply {x : ZMod modulus} : (ringEquiv modulus).symm x = ofField x
```

`Montgomery.Native64x8.FastField.instField` (instance, [line 523](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L523))

> Field instance transferred from the canonical field through `toField`.

```lean
instance instField : _root_.Field (FastField modulus)
```

`Montgomery.Native64x8.FastField.instNonBinaryField` (instance, [line 527](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean#L527))

> A fast eight-limb field is non-binary.

```lean
instance instNonBinaryField : NonBinaryField (FastField modulus)
```

## Depends on

- [Non-binary fields and polynomial utilities](../basic.md)
- [Eight-limb Montgomery arithmetic: runtime definitions (zero-import)](native64x8defs.md)

## Proof depends on

- [Correctness of eight-limb CIOS Montgomery multiplication](native64x8mul.md)

## Sources

- [CompPoly/Fields/Montgomery/Native64x8Field.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Field.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x8Field.json)
