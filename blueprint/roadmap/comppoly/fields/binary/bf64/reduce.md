---
catalog: module
lean: BF64.highHalf, BF64.lowHalf, BF64.highHalf_testBit, BF64.lowHalf_testBit, BF64.toPoly_halves, BF64.highHalf_lt, BF64.lowHalf_lt, BF64.carryLessMul_lt, BF64.reductionConstant, BF64.toPoly_reductionConstant, BF64.reductionConstant_lt, BF64.foldStep, BF64.foldStep_mod, BF64.foldStep_lt, BF64.reduce, BF64.foldStep_foldStep_lt, BF64.toPoly_lowHalf_of_lt, BF64.toPoly_reduce
statement: formalized
proof: formalized
---

# Reducing a carry-less product modulo the `GF(2^64)` modulus

`CompPoly.Fields.Binary.BF64.Reduce`, in [CompPoly/Fields/Binary/BF64/Reduce.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean), by Nicolas Schleicher.

> A product of two 64-bit values occupies 128 bits. Because `x^64 ≡ x^4 + x^3 + x + 1`
> (`BF64.mul_pow_reduce`), the high half can be folded back down by a single carry-less
> multiplication by `reductionConstant = 0x1B`. Each fold shrinks the excess, and two folds
> land back inside 64 bits — no long division is needed.
>
> This mirrors `CompPoly.Fields.Binary.BF128Ghash`'s reduction for the GHASH polynomial,
> at the 64-bit width and with this modulus.
>
> ## Main definitions
>
> * `highHalf`, `lowHalf` — the two 64-bit halves of a 128-bit value.
> * `reductionConstant` — `0x1B`, the modulus below its leading term.
> * `foldStep` — one reduction fold.
> * `reduce` — two folds and a truncation.
>
> ## Main statements
>
> * `toPoly_reductionConstant` — `0x1B` denotes `baseTail`.
> * `foldStep_mod` — a fold preserves the residue modulo the modulus.
> * `foldStep_lt` — a fold shrinks the value.
> * `toPoly_reduce` — `reduce` computes the remainder modulo the modulus.

> ## Halves of a double-width value

`BF64.highHalf` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L46))

> The high 64 bits of a 128-bit value.

```lean
def highHalf (x : BitVec 128) : BitVec 64
```

`BF64.lowHalf` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L49))

> The low 64 bits of a 128-bit value.

```lean
def lowHalf (x : BitVec 128) : BitVec 64
```

`BF64.highHalf_testBit` (theorem, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L52))

> Bit `i` of the high half is bit `64 + i` of the whole.

```lean
theorem highHalf_testBit (x : BitVec 128) (i : ℕ) (h : i < 64) :
    (highHalf x).toNat.testBit i = x.toNat.testBit (64 + i)
```

`BF64.lowHalf_testBit` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L59))

> Bit `i` of the low half is bit `i` of the whole.

```lean
theorem lowHalf_testBit (x : BitVec 128) (i : ℕ) (h : i < 64) :
    (lowHalf x).toNat.testBit i = x.toNat.testBit i
```

`BF64.toPoly_halves` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L66))

> Splitting a 128-bit value into `high * x^64 + low`.

```lean
theorem toPoly_halves (x : BitVec 128) :
    toPoly x = toPoly (highHalf x) * X ^ 64 + toPoly (lowHalf x)
```

`BF64.highHalf_lt` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L84))

> If `x < 2 ^ (64 + d)` then its high half is below `2 ^ d`.

```lean
theorem highHalf_lt (x : BitVec 128) {d : ℕ} (hx : x.toNat < 2 ^ (64 + d)) :
    (highHalf x).toNat < 2 ^ d
```

`BF64.lowHalf_lt` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L93))

> The low half is always below `2 ^ 64`, being 64 bits wide.

```lean
theorem lowHalf_lt (x : BitVec 128) : (lowHalf x).toNat < 2 ^ 64
```

`BF64.carryLessMul_lt` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L96))

> A carry-less product of values below `2 ^ p` and `2 ^ q` is below `2 ^ (p + q)`.

```lean
theorem carryLessMul_lt {v w : ℕ} (a b : BitVec v) {p q : ℕ}
    (ha : a.toNat < 2 ^ p) (hb : b.toNat < 2 ^ q) (h : v + v ≤ w) :
    (carryLessMul (w := w) a b).toNat < 2 ^ (p + q)
```

> ## The reduction fold

`BF64.reductionConstant` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L116))

> The reduction constant `0x1B`: the modulus below its leading term,
> `x^4 + x^3 + x + 1`.

```lean
def reductionConstant : BitVec 64
```

`BF64.toPoly_reductionConstant` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L122))

> **The reduction constant is the right one**: `0x1B` denotes `x^4 + x^3 + x + 1`.
>
> A wrong constant here would compile and silently give a different field, so this ties the
> bit pattern to the polynomial rather than leaving it to the reader.

```lean
theorem toPoly_reductionConstant : toPoly reductionConstant = baseTail
```

`BF64.reductionConstant_lt` (theorem, [line 134](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L134))

> The reduction constant fits in five bits, which bounds how much a fold can grow.

```lean
theorem reductionConstant_lt : reductionConstant.toNat < 2 ^ 5
```

`BF64.foldStep` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L137))

> One reduction fold: replace the high half's factor of `x^64` by `baseTail`.

```lean
def foldStep (x : BitVec 128) : BitVec 128
```

`BF64.foldStep_mod` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L141))

> A fold preserves the residue modulo the modulus.

```lean
theorem foldStep_mod (x : BitVec 128) :
    toPoly (foldStep x) % basePoly = toPoly x % basePoly
```

`BF64.foldStep_lt` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L151))

> A fold of a value below `2 ^ (64 + d)` lands below `2 ^ (max 64 (d + 5))`.

```lean
theorem foldStep_lt (x : BitVec 128) {d : ℕ} (hx : x.toNat < 2 ^ (64 + d)) :
    (foldStep x).toNat < 2 ^ (max 64 (d + 5))
```

> ## Full reduction

`BF64.reduce` (definition, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L167))

> Reduce a 128-bit carry-less product into the base field: two folds, then truncate.

```lean
def reduce (x : BitVec 128) : BitVec 64
```

`BF64.foldStep_foldStep_lt` (theorem, [line 170](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L170))

> Two folds bring any 128-bit value below `2 ^ 64`.

```lean
theorem foldStep_foldStep_lt (x : BitVec 128) : (foldStep (foldStep x)).toNat < 2 ^ 64
```

`BF64.toPoly_lowHalf_of_lt` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L176))

> Truncation is faithful on values already below `2 ^ 64`.

```lean
theorem toPoly_lowHalf_of_lt (x : BitVec 128) (h : x.toNat < 2 ^ 64) :
    toPoly (lowHalf x) = toPoly x
```

`BF64.toPoly_reduce` (theorem, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean#L186))

> `reduce` computes the remainder of the denoted polynomial modulo the modulus.

```lean
theorem toPoly_reduce (x : BitVec 128) :
    toPoly (reduce x) = toPoly x % basePoly
```

## Depends on

- [`GF(2^64)` in a polynomial basis](basic.md)
- [Common Utilities for Binary Fields](../common.md)

## Sources

- [CompPoly/Fields/Binary/BF64/Reduce.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/BF64/Reduce.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.BF64.Reduce.json)
