---
catalog: module
lean: Goldilocks.Fast.modulus, Goldilocks.Fast.negModulus, Goldilocks.Fast.wideMul, Goldilocks.Fast.reduceUInt64Raw, Goldilocks.Fast.foldUInt128Borrow, Goldilocks.Fast.foldUInt128Lazy, Goldilocks.Fast.reduceUInt128Raw, Goldilocks.Fast.mulLazy, Goldilocks.Fast.reduceMulRaw, Goldilocks.Fast.addRaw, Goldilocks.Fast.negRaw, Goldilocks.Fast.subRaw, Goldilocks.Fast.powLazy, Goldilocks.Fast.squareNLazy, Goldilocks.Fast.invLazy
statement: formalized
proof: formalized
---

# Fast Goldilocks: runtime definitions (zero-import)

`CompPoly.Fields.Goldilocks.FastDefs`, in [CompPoly/Fields/Goldilocks/FastDefs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean), by Varun Thakore.

> Runtime word kernels of the native Goldilocks field, proved correct in
> `CompPoly.Fields.Goldilocks.FastReduction`. This module has zero imports so that
> `precompileModules` lanes, which compile the whole import closure, can take it without Mathlib.

> ## Word constants

`Goldilocks.Fast.modulus` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L24))

> Goldilocks modulus `2^64 - 2^32 + 1` as a native word.

```lean
def modulus : UInt64
```

`Goldilocks.Fast.negModulus` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L28))

> Two's complement of the modulus: `2^64 - modulus = 2^32 - 1 = 0xFFFFFFFF`.

```lean
def negModulus : UInt64
```

> ## Raw word kernels
>
> Kernels take and return canonical words below the modulus; the `Lazy` ones take and
> return any congruent word, so a chain canonicalizes once at the end.

`Goldilocks.Fast.wideMul` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L39))

> Full 64-by-64 product as `(lo, hi)` words from 32-bit limbs, in the shape clang fuses
> into one widening multiply.

```lean
def wideMul (x y : UInt64) : UInt64 × UInt64
```

`Goldilocks.Fast.reduceUInt64Raw` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L55))

> Canonicalize a word by one conditional subtraction, since every `UInt64` is below `2 * p`.

```lean
def reduceUInt64Raw (x : UInt64) : UInt64
```

`Goldilocks.Fast.foldUInt128Borrow` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L60))

> Borrow arm of the 128-bit fold, out of line so the common path takes a predicted branch.

```lean
def foldUInt128Borrow (lo hiHi hiLo : UInt64) : UInt64
```

`Goldilocks.Fast.foldUInt128Lazy` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L69))

> Fold `lo + hi * 2^64` into one congruent, not necessarily canonical, word using
> `2^64 ≡ 2^32 - 1`; the middle term is `(hi <<< 32) - hiLo` rather than a multiply.

```lean
def foldUInt128Lazy (lo hi : UInt64) : UInt64
```

`Goldilocks.Fast.reduceUInt128Raw` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L81))

> Raw reduction of a 128-bit integer represented by low and high words modulo Goldilocks.

```lean
def reduceUInt128Raw (lo hi : UInt64) : UInt64
```

`Goldilocks.Fast.mulLazy` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L86))

> Product of two arbitrary words as one congruent, not necessarily canonical, word.

```lean
def mulLazy (x y : UInt64) : UInt64
```

`Goldilocks.Fast.reduceMulRaw` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L92))

> Raw reduction of a 64-by-64 product modulo Goldilocks.

```lean
def reduceMulRaw (x y : UInt64) : UInt64
```

`Goldilocks.Fast.addRaw` (definition, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L97))

> Canonical sum as `x - (p - y)`, which borrows exactly when `x + y < p`.

```lean
def addRaw (x y : UInt64) : UInt64
```

`Goldilocks.Fast.negRaw` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L104))

> Raw modular negation in canonical form.

```lean
def negRaw (x : UInt64) : UInt64
```

`Goldilocks.Fast.subRaw` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L109))

> Raw modular subtraction in canonical form.

```lean
def subRaw (x y : UInt64) : UInt64
```

> ## Lazy exponentiation

`Goldilocks.Fast.powLazy` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L116))

> Square-and-multiply on unreduced words: `powLazy acc x n` computes `acc * x^n`.

```lean
def powLazy (acc x : UInt64) (n : Nat) : UInt64
```

`Goldilocks.Fast.squareNLazy` (definition, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L125))

> `x^(2^n)` on unreduced words.

```lean
def squareNLazy (x : UInt64) : Nat → UInt64
```

`Goldilocks.Fast.invLazy` (definition, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean#L131))

> Fermat chain for `x^(p - 2)` on unreduced words, with
> `p - 2 = (2^32 - 2) * 2^32 + (2^32 - 1)`.

```lean
def invLazy (x : UInt64) : UInt64
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Goldilocks/FastDefs.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Goldilocks/FastDefs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Goldilocks.FastDefs.json)
