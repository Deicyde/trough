---
catalog: module
lean: Montgomery.Native64x8.mask, Montgomery.Native64x8.adcLo, Montgomery.Native64x8.adcCo, Montgomery.Native64x8.sbbLo, Montgomery.Native64x8.sbbBo, Montgomery.Native64x8.macLo, Montgomery.Native64x8.macHi, Montgomery.Native64x8.montM, Montgomery.Native64x8.Limbs8, Montgomery.Native64x8.Limbs8.zero, Montgomery.Native64x8.Limbs8.one, Montgomery.Native64x8.Limbs8.ofNat, Montgomery.Native64x8.Limbs8.toNat, Montgomery.Native64x8.Limbs8.Bounded, Montgomery.Native64x8.addLimbs, Montgomery.Native64x8.addCarry, Montgomery.Native64x8.subLimbs, Montgomery.Native64x8.subBorrow, Montgomery.Native64x8.condSub, Montgomery.Native64x8.add, Montgomery.Native64x8.sub, Montgomery.Native64x8.neg, Montgomery.Native64x8.State9, Montgomery.Native64x8.State9.zero, Montgomery.Native64x8.State9.toLimbs8, Montgomery.Native64x8.State9.toNat, Montgomery.Native64x8.State9.Bounded, Montgomery.Native64x8.mulAccum, Montgomery.Native64x8.mulReduce, Montgomery.Native64x8.mulRound, Montgomery.Native64x8.condSubWide, Montgomery.Native64x8.mul, Montgomery.Native64x8.square
statement: formalized
proof: formalized
---

# Eight-limb Montgomery arithmetic: runtime definitions (zero-import)

`CompPoly.Fields.Montgomery.Native64x8Defs`, in [CompPoly/Fields/Montgomery/Native64x8Defs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean), by Gregor Mitscha-Baude.

> The runtime definitions of the eight-limb Montgomery arithmetic, split out of
> `CompPoly.Fields.Montgomery.Native64x8` verbatim.  All correctness statements about them
> live in that sibling module, which imports this one.
>
> This module deliberately has **zero imports**: downstream consumers put it into
> `precompileModules` native-compilation lanes, and `precompileModules` compiles the
> entire import closure — so the runtime definitions must not pull in mathlib.

> ## Word helpers

`Montgomery.Native64x8.mask` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L28))

> Mask selecting the low 32 bits of a `UInt64`.

```lean
def mask : UInt64
```

`Montgomery.Native64x8.adcLo` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L31))

> Low limb of add-with-carry: `(x + y + c) mod 2 ^ 32`.

```lean
def adcLo (x y c : UInt64) : UInt64
```

`Montgomery.Native64x8.adcCo` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L34))

> Carry-out of add-with-carry: `(x + y + c) / 2 ^ 32`.

```lean
def adcCo (x y c : UInt64) : UInt64
```

`Montgomery.Native64x8.sbbLo` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L37))

> Low limb of subtract-with-borrow: `(x - y - b) mod 2 ^ 32`.

```lean
def sbbLo (x y b : UInt64) : UInt64
```

`Montgomery.Native64x8.sbbBo` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L40))

> Borrow-out of subtract-with-borrow, read off the sign bit of the 64-bit difference.

```lean
def sbbBo (x y b : UInt64) : UInt64
```

`Montgomery.Native64x8.macLo` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L43))

> Low limb of multiply-accumulate: `(t + x * y + c) mod 2 ^ 32`.

```lean
def macLo (t x y c : UInt64) : UInt64
```

`Montgomery.Native64x8.macHi` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L46))

> High word of multiply-accumulate: `(t + x * y + c) / 2 ^ 32`.

```lean
def macHi (t x y c : UInt64) : UInt64
```

`Montgomery.Native64x8.montM` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L49))

> The Montgomery multiplier of a limb: `(s * negInv) mod 2 ^ 32`.

```lean
def montM (s negInv : UInt64) : UInt64
```

> ## Eight-limb values

`Montgomery.Native64x8.Limbs8` (structure, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L54))

> A 256-bit value as eight little-endian 32-bit limbs, each stored in a `UInt64`.

```lean
structure Limbs8 where
  /-- Limb of weight `2 ^ 0`. -/
  l0 : UInt64
  /-- Limb of weight `2 ^ 32`. -/
  l1 : UInt64
  /-- Limb of weight `2 ^ 64`. -/
  l2 : UInt64
  /-- Limb of weight `2 ^ 96`. -/
  l3 : UInt64
  /-- Limb of weight `2 ^ 128`. -/
  l4 : UInt64
  /-- Limb of weight `2 ^ 160`. -/
  l5 : UInt64
  /-- Limb of weight `2 ^ 192`. -/
  l6 : UInt64
  /-- Limb of weight `2 ^ 224`. -/
  l7 : UInt64
deriving DecidableEq, Repr, Inhabited
```

`Montgomery.Native64x8.Limbs8.zero` (definition, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L76))

> The zero value.

```lean
def zero : Limbs8
```

`Montgomery.Native64x8.Limbs8.one` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L79))

> The value one.

```lean
def one : Limbs8
```

`Montgomery.Native64x8.Limbs8.ofNat` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L82))

> Split a natural number into eight 32-bit limbs, discarding bits above `2 ^ 256`.

```lean
def ofNat (n : Nat) : Limbs8
```

`Montgomery.Native64x8.Limbs8.toNat` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L89))

> The natural number represented by the limbs: `∑ lᵢ * 2 ^ (32 * i)`.

```lean
def toNat (x : Limbs8) : Nat
```

`Montgomery.Native64x8.Limbs8.Bounded` (definition, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L94))

> Every limb holds at most 32 significant bits.

```lean
def Bounded (x : Limbs8) : Prop
```

> ## Limbwise addition and subtraction

`Montgomery.Native64x8.addLimbs` (definition, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L107))

> Limbwise add-with-carry, discarding the carry out of the top limb.

```lean
def addLimbs (a b : Limbs8) : Limbs8
```

`Montgomery.Native64x8.addCarry` (definition, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L119))

> Carry out of the top limb of `addLimbs`.

```lean
def addCarry (a b : Limbs8) : UInt64
```

`Montgomery.Native64x8.subLimbs` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L130))

> Limbwise subtract-with-borrow.

```lean
def subLimbs (a b : Limbs8) : Limbs8
```

`Montgomery.Native64x8.subBorrow` (definition, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L142))

> Borrow out of the top limb of `subLimbs`.

```lean
def subBorrow (a b : Limbs8) : UInt64
```

> ## Conditional subtraction and field operations

`Montgomery.Native64x8.condSub` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L156))

> Subtract the modulus once if the value is at least the modulus.  The borrow chain
> decides the branch, so no comparison is needed.

```lean
def condSub (q t : Limbs8) : Limbs8
```

`Montgomery.Native64x8.add` (definition, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L161))

> Modular addition; a carry out of the top limb forces the (wrapping, exact) subtraction
> of the modulus, and never happens for a modulus below `2 ^ 255`.

```lean
def add (q a b : Limbs8) : Limbs8
```

`Montgomery.Native64x8.sub` (definition, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L166))

> Modular subtraction: on a borrow, the modulus is added back.

```lean
def sub (q a b : Limbs8) : Limbs8
```

`Montgomery.Native64x8.neg` (definition, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L171))

> Modular negation.

```lean
def neg (q a : Limbs8) : Limbs8
```

> ## CIOS multiplication

`Montgomery.Native64x8.State9` (structure, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L176))

> The CIOS accumulator: eight limbs plus one head limb.

```lean
structure State9 where
  /-- Limb of weight `2 ^ 0`. -/
  t0 : UInt64
  /-- Limb of weight `2 ^ 32`. -/
  t1 : UInt64
  /-- Limb of weight `2 ^ 64`. -/
  t2 : UInt64
  /-- Limb of weight `2 ^ 96`. -/
  t3 : UInt64
  /-- Limb of weight `2 ^ 128`. -/
  t4 : UInt64
  /-- Limb of weight `2 ^ 160`. -/
  t5 : UInt64
  /-- Limb of weight `2 ^ 192`. -/
  t6 : UInt64
  /-- Limb of weight `2 ^ 224`. -/
  t7 : UInt64
  /-- Head limb of weight `2 ^ 256`. -/
  t8 : UInt64
deriving DecidableEq, Repr, Inhabited
```

`Montgomery.Native64x8.State9.zero` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L200))

> The zero accumulator.

```lean
def zero : State9
```

`Montgomery.Native64x8.State9.toLimbs8` (definition, [line 203](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L203))

> The eight low limbs of the accumulator.

```lean
def toLimbs8 (t : State9) : Limbs8
```

`Montgomery.Native64x8.State9.toNat` (definition, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L206))

> The natural number represented by the accumulator.

```lean
def toNat (t : State9) : Nat
```

`Montgomery.Native64x8.State9.Bounded` (definition, [line 209](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L209))

> Every limb of the accumulator holds at most 32 significant bits.

```lean
def Bounded (t : State9) : Prop
```

`Montgomery.Native64x8.mulAccum` (definition, [line 215](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L215))

> The multiply half of a CIOS round: accumulate `a * bi` into the accumulator.  The carry
> out of the top limb is kept in the head limb, so no information is lost.

```lean
def mulAccum (a : Limbs8) (bi : UInt64) (t : State9) : State9
```

`Montgomery.Native64x8.mulReduce` (definition, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L230))

> The reduce half of a CIOS round: add the multiple `montM s.t0 negInv` of the modulus that
> cancels the low limb, then drop that limb.  `negInv` has to be `-q⁻¹ mod 2 ^ 32`.

```lean
def mulReduce (q : Limbs8) (negInv : UInt64) (s : State9) : State9
```

`Montgomery.Native64x8.mulRound` (definition, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L246))

> One CIOS outer round: accumulate `a * bi` into the accumulator, then reduce away one
> limb.

```lean
def mulRound (q : Limbs8) (negInv : UInt64) (a : Limbs8) (bi : UInt64)
    (t : State9) : State9
```

`Montgomery.Native64x8.condSubWide` (definition, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L252))

> `condSub` for an accumulator below `2 * q`; a set head limb forces the (wrapping, exact)
> subtraction of the modulus, and never happens for a modulus below `2 ^ 255`.

```lean
def condSubWide (q : Limbs8) (t : State9) : Limbs8
```

`Montgomery.Native64x8.mul` (definition, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L258))

> CIOS Montgomery multiplication: eight rounds followed by one conditional
> subtraction.

```lean
def mul (q : Limbs8) (negInv : UInt64) (a b : Limbs8) : Limbs8
```

`Montgomery.Native64x8.square` (definition, [line 270](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean#L270))

> Montgomery squaring.

```lean
def square (q : Limbs8) (negInv : UInt64) (a : Limbs8) : Limbs8
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Montgomery/Native64x8Defs.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Montgomery/Native64x8Defs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x8Defs.json)
