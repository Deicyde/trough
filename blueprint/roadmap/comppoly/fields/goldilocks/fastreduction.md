---
catalog: module
lean: Goldilocks.Fast.modulus_toNat, Goldilocks.Fast.negModulus_toNat, Goldilocks.Fast.fieldSize_pos, Goldilocks.Fast.fieldSize_lt_uint64Size, Goldilocks.Fast.uint64_toNat_lt_two_fieldSize, Goldilocks.Fast.uint64_cast_eq_negModulus, Goldilocks.Fast.pow32_mul_negModulus_cast, Goldilocks.Fast.shiftRight32_toNat, Goldilocks.Fast.and_negModulus_toNat, Goldilocks.Fast.subBorrow_cast, Goldilocks.Fast.addOverflowBounded_cast, Goldilocks.Fast.mul_negModulus_toNat_of_lt, Goldilocks.Fast.mul_negModulus_toNat_le, Goldilocks.Fast.hi_split_cast, Goldilocks.Fast.uint64_split32, Goldilocks.Fast.uint64_low32_lt, Goldilocks.Fast.uint64_high32_lt, Goldilocks.Fast.mul32_toNat, Goldilocks.Fast.product_split32, Goldilocks.Fast.wideMul_low_toNat, Goldilocks.Fast.wideMul_snd_toNat, Goldilocks.Fast.wideMul_cast, Goldilocks.Fast.reduceUInt64Raw_lt, Goldilocks.Fast.reduceUInt64Raw_cast, Goldilocks.Fast.shiftLeft32_sub_low, Goldilocks.Fast.foldUInt128Lazy_cast, Goldilocks.Fast.reduceUInt128Raw_lt, Goldilocks.Fast.reduceUInt128Raw_cast, Goldilocks.Fast.mulLazy_cast, Goldilocks.Fast.reduceMulRaw_lt, Goldilocks.Fast.reduceMulRaw_cast, Goldilocks.Fast.addRaw_toNat, Goldilocks.Fast.addRaw_lt, Goldilocks.Fast.addRaw_cast, Goldilocks.Fast.negRaw_lt, Goldilocks.Fast.negRaw_cast, Goldilocks.Fast.subRaw_lt, Goldilocks.Fast.subRaw_cast, Goldilocks.Fast.powLazy_cast, Goldilocks.Fast.squareNLazy_cast, Goldilocks.Fast.invLazy_cast
statement: formalized
proof: formalized
---

# Fast Goldilocks: word-level correctness

`CompPoly.Fields.Goldilocks.FastReduction`, in [CompPoly/Fields/Goldilocks/FastReduction.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean), by Varun Thakore.

> Correctness of the raw `UInt64` kernels in `CompPoly.Fields.Goldilocks.FastDefs`:
> low-level word lemmas (limb splitting, borrow and overflow correction, the 64-by-64
> product decomposition), then for each kernel a bound showing the result is below the
> modulus and a cast lemma identifying it with the corresponding operation in
> `Goldilocks.Field`.
>
> The field carrier and its API are built on these in
> `CompPoly.Fields.Goldilocks.Fast`.

> ## Low-level `UInt64` lemmas

`Goldilocks.Fast.modulus_toNat` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L33))

> The native `UInt64` modulus agrees with the mathematical Goldilocks modulus.

```lean
theorem modulus_toNat : modulus.toNat = Goldilocks.fieldSize
```

`Goldilocks.Fast.negModulus_toNat` (theorem, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L38))

> The native negated-modulus constant agrees with `2^32 - 1`.

```lean
theorem negModulus_toNat : negModulus.toNat = 2 ^ 32 - 1
```

`Goldilocks.Fast.fieldSize_pos` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L42))

> The Goldilocks modulus is positive.

```lean
theorem fieldSize_pos : 0 < Goldilocks.fieldSize
```

`Goldilocks.Fast.fieldSize_lt_uint64Size` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L46))

> The Goldilocks modulus fits in a `UInt64`.

```lean
theorem fieldSize_lt_uint64Size : Goldilocks.fieldSize < UInt64.size
```

`Goldilocks.Fast.uint64_toNat_lt_two_fieldSize` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L50))

> Every `UInt64` value is below twice the Goldilocks modulus.

```lean
theorem uint64_toNat_lt_two_fieldSize (x : UInt64) :
    x.toNat < 2 * Goldilocks.fieldSize
```

`Goldilocks.Fast.uint64_cast_eq_negModulus` (theorem, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L58))

> The folding congruence used by the Goldilocks reducer.
>
> `2^64 ≡ 2^32 - 1 (mod p)`.

```lean
theorem uint64_cast_eq_negModulus :
    (UInt64.size : Goldilocks.Field) = (negModulus.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.pow32_mul_negModulus_cast` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L63))

> Multiplying by `2^32 - 1` after shifting by `2^32` is negation modulo Goldilocks.

```lean
theorem pow32_mul_negModulus_cast :
    ((2 ^ 32 : Nat) : Goldilocks.Field) *
        (negModulus.toNat : Goldilocks.Field) =
      -1
```

`Goldilocks.Fast.shiftRight32_toNat` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L70))

> Right shifting a `UInt64` by 32 gives division by `2^32` on naturals.

```lean
theorem shiftRight32_toNat (x : UInt64) :
    (x >>> 32).toNat = x.toNat / 2 ^ 32
```

`Goldilocks.Fast.and_negModulus_toNat` (theorem, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L78))

> Masking with `2^32 - 1` gives the low 32 bits on naturals.

```lean
theorem and_negModulus_toNat (x : UInt64) :
    (x &&& negModulus).toNat = x.toNat % 2 ^ 32
```

`Goldilocks.Fast.subBorrow_cast` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L92))

> A `UInt64` subtraction with the Goldilocks borrow correction represents subtraction modulo `p`.
>
> The assumption says the subtrahend is a 32-bit limb, which is the case for
> `hi >>> 32` in the 128-bit reducer.

```lean
theorem subBorrow_cast (a b : UInt64) (hb : b.toNat < 2 ^ 32) :
    (((if a < b then a - b - negModulus else a - b).toNat) : Goldilocks.Field) =
      (a.toNat : Goldilocks.Field) - (b.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.addOverflowBounded_cast` (theorem, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L135))

> A bounded `UInt64` addition with the Goldilocks overflow correction represents
> addition modulo `p`.

```lean
theorem addOverflowBounded_cast (a b : UInt64)
    (hbound : a.toNat + b.toNat < 2 * UInt64.size - negModulus.toNat) :
    (((if a + b < a then a + b + negModulus else a + b).toNat) :
      Goldilocks.Field) =
      (a.toNat : Goldilocks.Field) + (b.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.mul_negModulus_toNat_of_lt` (theorem, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L182))

> Multiplication by `2^32 - 1` does not overflow for a 32-bit limb.

```lean
theorem mul_negModulus_toNat_of_lt (x : UInt64) (hx : x.toNat < 2 ^ 32) :
    (x * negModulus).toNat = x.toNat * negModulus.toNat
```

`Goldilocks.Fast.mul_negModulus_toNat_le` (theorem, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L190))

> The product of a 32-bit limb by `2^32 - 1` leaves enough headroom for correction.

```lean
theorem mul_negModulus_toNat_le (x : UInt64) (hx : x.toNat < 2 ^ 32) :
    (x * negModulus).toNat ≤ UInt64.size - 2 * negModulus.toNat
```

`Goldilocks.Fast.hi_split_cast` (theorem, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L203))

> Splitting a high word into 32-bit limbs matches the Goldilocks folding congruence.

```lean
theorem hi_split_cast (hi : UInt64) :
    (hi.toNat : Goldilocks.Field) * (UInt64.size : Goldilocks.Field) =
      ((hi &&& negModulus).toNat : Goldilocks.Field) *
          (negModulus.toNat : Goldilocks.Field) -
        ((hi >>> 32).toNat : Goldilocks.Field)
```

`Goldilocks.Fast.uint64_split32` (theorem, [line 229](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L229))

> A `UInt64` value decomposes into its low and high 32-bit limbs.

```lean
theorem uint64_split32 (x : UInt64) :
    x.toNat = (x &&& negModulus).toNat + 2 ^ 32 * (x >>> 32).toNat
```

`Goldilocks.Fast.uint64_low32_lt` (theorem, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L235))

> The low 32-bit limb of a `UInt64` is below `2^32`.

```lean
theorem uint64_low32_lt (x : UInt64) :
    (x &&& negModulus).toNat < 2 ^ 32
```

`Goldilocks.Fast.uint64_high32_lt` (theorem, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L241))

> The high 32-bit limb of a `UInt64` is below `2^32`.

```lean
theorem uint64_high32_lt (x : UInt64) :
    (x >>> 32).toNat < 2 ^ 32
```

`Goldilocks.Fast.mul32_toNat` (theorem, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L249))

> Multiplying two 32-bit limbs does not overflow `UInt64`.

```lean
theorem mul32_toNat (a b : UInt64) (ha : a.toNat < 2 ^ 32) (hb : b.toNat < 2 ^ 32) :
    (a * b).toNat = a.toNat * b.toNat
```

`Goldilocks.Fast.product_split32` (theorem, [line 256](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L256))

> Algebraic decomposition of a product after splitting both factors into 32-bit limbs.

```lean
theorem product_split32 (x y : UInt64) :
    x.toNat * y.toNat =
      (x &&& negModulus).toNat * (y &&& negModulus).toNat +
        2 ^ 32 *
          ((x &&& negModulus).toNat * (y >>> 32).toNat +
            (x >>> 32).toNat * (y &&& negModulus).toNat) +
          2 ^ 64 * ((x >>> 32).toNat * (y >>> 32).toNat)
```

`Goldilocks.Fast.wideMul_low_toNat` (theorem, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L267))

> Low word returned by a 64-by-64 product implementation.

```lean
theorem wideMul_low_toNat (lo : UInt64) (x y : UInt64) (hlo : lo = x * y) :
    lo.toNat = x.toNat * y.toNat % UInt64.size
```

`Goldilocks.Fast.wideMul_snd_toNat` (theorem, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L278))

> The high word of `wideMul` is the high half of the product.

```lean
theorem wideMul_snd_toNat (x y : UInt64) :
    (wideMul x y).2.toNat = x.toNat * y.toNat / 2 ^ 64
```

`Goldilocks.Fast.wideMul_cast` (theorem, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L305))

> Combined semantic correctness of a 64-by-64 product represented by low and high words.

```lean
theorem wideMul_cast
    (x y lo hi : UInt64)
    (hlo : lo = x * y)
    (hhi : hi.toNat = x.toNat * y.toNat / UInt64.size) :
    (lo.toNat : Goldilocks.Field) +
        (hi.toNat : Goldilocks.Field) * (UInt64.size : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field) * (y.toNat : Goldilocks.Field)
```

> ## Raw kernel correctness

`Goldilocks.Fast.reduceUInt64Raw_lt` (theorem, [line 319](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L319))

> The raw one-word reducer returns a canonical representative.

```lean
theorem reduceUInt64Raw_lt (x : UInt64) :
    (reduceUInt64Raw x).toNat < Goldilocks.fieldSize
```

`Goldilocks.Fast.reduceUInt64Raw_cast` (theorem, [line 338](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L338))

> One-word reduction preserves the represented canonical field element.

```lean
theorem reduceUInt64Raw_cast (x : UInt64) :
    ((reduceUInt64Raw x).toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.shiftLeft32_sub_low` (theorem, [line 374](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L374))

> The middle limb times `2^32 - 1`, formed as a shift and a subtraction.

```lean
theorem shiftLeft32_sub_low (hi : UInt64) :
    (hi <<< 32) - (hi &&& negModulus) = (hi &&& negModulus) * negModulus
```

`Goldilocks.Fast.foldUInt128Lazy_cast` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L392))

> The lazy fold represents `lo + hi * 2^64`.

```lean
theorem foldUInt128Lazy_cast (lo hi : UInt64) :
    ((foldUInt128Lazy lo hi).toNat : Goldilocks.Field) =
      (lo.toNat : Goldilocks.Field) +
        (hi.toNat : Goldilocks.Field) * (UInt64.size : Goldilocks.Field)
```

`Goldilocks.Fast.reduceUInt128Raw_lt` (theorem, [line 409](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L409))

> The raw 128-bit reducer returns a canonical representative below the modulus.

```lean
theorem reduceUInt128Raw_lt (lo hi : UInt64) :
    (reduceUInt128Raw lo hi).toNat < Goldilocks.fieldSize
```

`Goldilocks.Fast.reduceUInt128Raw_cast` (theorem, [line 414](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L414))

> Semantic correctness of raw 128-bit Goldilocks reduction.

```lean
theorem reduceUInt128Raw_cast (lo hi : UInt64) :
    ((reduceUInt128Raw lo hi).toNat : Goldilocks.Field) =
      (lo.toNat : Goldilocks.Field) +
        (hi.toNat : Goldilocks.Field) * (UInt64.size : Goldilocks.Field)
```

`Goldilocks.Fast.mulLazy_cast` (theorem, [line 423](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L423))

> The lazy product of any two words represents their product.

```lean
theorem mulLazy_cast (x y : UInt64) :
    ((mulLazy x y).toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field) * (y.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.reduceMulRaw_lt` (theorem, [line 431](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L431))

> Product reduction returns a canonical representative below the modulus.

```lean
theorem reduceMulRaw_lt (x y : UInt64) :
    (reduceMulRaw x y).toNat < Goldilocks.fieldSize
```

`Goldilocks.Fast.reduceMulRaw_cast` (theorem, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L436))

> Semantic correctness of native 64-by-64 product reduction.

```lean
theorem reduceMulRaw_cast (x y : UInt64) :
    ((reduceMulRaw x y).toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field) * (y.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.addRaw_toNat` (theorem, [line 443](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L443))

> Raw addition of canonical words computes the reduced sum.

```lean
theorem addRaw_toNat {x y : UInt64} (hx : x.toNat < Goldilocks.fieldSize)
    (hy : y.toNat < Goldilocks.fieldSize) :
    (addRaw x y).toNat = (x.toNat + y.toNat) % Goldilocks.fieldSize
```

`Goldilocks.Fast.addRaw_lt` (theorem, [line 455](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L455))

> Raw addition of canonical words returns a canonical representative.

```lean
theorem addRaw_lt {x y : UInt64} (hx : x.toNat < Goldilocks.fieldSize)
    (hy : y.toNat < Goldilocks.fieldSize) :
    (addRaw x y).toNat < Goldilocks.fieldSize
```

`Goldilocks.Fast.addRaw_cast` (theorem, [line 462](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L462))

> Raw addition agrees with canonical-field addition on canonical words.

```lean
theorem addRaw_cast {x y : UInt64} (hx : x.toNat < Goldilocks.fieldSize)
    (hy : y.toNat < Goldilocks.fieldSize) :
    ((addRaw x y).toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field) + (y.toNat : Goldilocks.Field)
```

`Goldilocks.Fast.negRaw_lt` (theorem, [line 469](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L469))

> Raw negation returns a canonical representative when given one.

```lean
theorem negRaw_lt (x : UInt64) (hx : x.toNat < Goldilocks.fieldSize) :
    (negRaw x).toNat < Goldilocks.fieldSize
```

`Goldilocks.Fast.negRaw_cast` (theorem, [line 490](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L490))

> Raw negation agrees with canonical-field negation.

```lean
theorem negRaw_cast (x : UInt64) (hx : x.toNat < Goldilocks.fieldSize) :
    ((negRaw x).toNat : Goldilocks.Field) =
      -((x.toNat : Goldilocks.Field))
```

`Goldilocks.Fast.subRaw_lt` (theorem, [line 512](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L512))

> Raw subtraction returns a canonical representative when given canonical operands.

```lean
theorem subRaw_lt (x y : UInt64)
    (hx : x.toNat < Goldilocks.fieldSize)
    (hy : y.toNat < Goldilocks.fieldSize) :
    (subRaw x y).toNat < Goldilocks.fieldSize
```

`Goldilocks.Fast.subRaw_cast` (theorem, [line 559](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L559))

> Raw subtraction agrees with canonical-field subtraction for canonical operands.

```lean
theorem subRaw_cast (x y : UInt64)
    (_hx : x.toNat < Goldilocks.fieldSize)
    (hy : y.toNat < Goldilocks.fieldSize) :
    ((subRaw x y).toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field) - (y.toNat : Goldilocks.Field)
```

> ## Lazy exponentiation

`Goldilocks.Fast.powLazy_cast` (theorem, [line 613](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L613))

> The lazy ladder computes `acc * x^n`.

```lean
theorem powLazy_cast (acc x : UInt64) (n : Nat) :
    ((powLazy acc x n).toNat : Goldilocks.Field) =
      (acc.toNat : Goldilocks.Field) * (x.toNat : Goldilocks.Field) ^ n
```

`Goldilocks.Fast.squareNLazy_cast` (theorem, [line 635](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L635))

> Lazy repeated squaring computes `x^(2^n)`.

```lean
theorem squareNLazy_cast (x : UInt64) (n : Nat) :
    ((squareNLazy x n).toNat : Goldilocks.Field) = (x.toNat : Goldilocks.Field) ^ (2 ^ n)
```

`Goldilocks.Fast.invLazy_cast` (theorem, [line 649](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean#L649))

> The lazy chain computes the Fermat exponent `p - 2`.

```lean
theorem invLazy_cast (x : UInt64) :
    ((invLazy x).toNat : Goldilocks.Field) =
      (x.toNat : Goldilocks.Field) ^ (Goldilocks.fieldSize - 2)
```

## Depends on

- [Goldilocks prime field `2^{64} - 2^{32} + 1`](basic.md)
- [Fast Goldilocks: runtime definitions (zero-import)](fastdefs.md)

## Sources

- [CompPoly/Fields/Goldilocks/FastReduction.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Goldilocks/FastReduction.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Goldilocks.FastReduction.json)
