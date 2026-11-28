---
catalog: module
lean: Montgomery.Native64x4.mulHi, Montgomery.Native64x4.adc, Montgomery.Native64x4.sbb, Montgomery.Native64x4.mac, Montgomery.Native64x4.montM, Montgomery.Native64x4.Limbs4, Montgomery.Native64x4.Limbs4.zero, Montgomery.Native64x4.Limbs4.one, Montgomery.Native64x4.Limbs4.ofNat, Montgomery.Native64x4.Limbs4.toNat, Montgomery.Native64x4.addLimbs, Montgomery.Native64x4.subLimbs, Montgomery.Native64x4.condSub, Montgomery.Native64x4.add, Montgomery.Native64x4.sub, Montgomery.Native64x4.neg, Montgomery.Native64x4.State5, Montgomery.Native64x4.State6, Montgomery.Native64x4.State5.zero, Montgomery.Native64x4.State5.toLimbs4, Montgomery.Native64x4.State5.toNat, Montgomery.Native64x4.State6.toNat, Montgomery.Native64x4.mulAccum, Montgomery.Native64x4.mulReduce, Montgomery.Native64x4.mulRound, Montgomery.Native64x4.condSubWide, Montgomery.Native64x4.mul, Montgomery.Native64x4.square
statement: formalized
proof: formalized
---

# Four-limb Montgomery arithmetic: runtime definitions (zero-import)

`CompPoly.Fields.Montgomery.Native64x4Defs`, in [CompPoly/Fields/Montgomery/Native64x4Defs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean), by Georgios Raikos.

> The runtime definitions of the four-limb Montgomery arithmetic over 64-bit limbs; all
> correctness statements live in `CompPoly.Fields.Montgomery.Native64x4`, which imports this
> one.  Products widen through `mulHi` (four 32-bit partial products) and every word helper
> returns a pair the caller destructures, so nothing is boxed.
>
> This module deliberately has **zero imports**, for `precompileModules` consumers.

> ## Word helpers

`Montgomery.Native64x4.mulHi` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L27))

> High word of the 64-bit product `a * b`, from four 32-bit partial products.

```lean
def mulHi (a b : UInt64) : UInt64
```

`Montgomery.Native64x4.adc` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L39))

> Add-with-carry: the low word and the carry-out of `x + y + c`, for `c ≤ 1`.

```lean
def adc (x y c : UInt64) : UInt64 × UInt64
```

`Montgomery.Native64x4.sbb` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L45))

> Subtract-with-borrow: the low word and the borrow-out of `x - y - b`, for `b ≤ 1`.

```lean
def sbb (x y b : UInt64) : UInt64 × UInt64
```

`Montgomery.Native64x4.mac` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L50))

> Multiply-accumulate: the low and high words of `t + a * b + c`.

```lean
def mac (t a b c : UInt64) : UInt64 × UInt64
```

`Montgomery.Native64x4.montM` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L56))

> The Montgomery multiplier of a limb: `(s * negInv) mod 2 ^ 64`.

```lean
def montM (s negInv : UInt64) : UInt64
```

> ## Four-limb values

`Montgomery.Native64x4.Limbs4` (structure, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L61))

> A 256-bit value as four little-endian 64-bit limbs.

```lean
structure Limbs4 where
  /-- Limb of weight `2 ^ 0`. -/
  l0 : UInt64
  /-- Limb of weight `2 ^ 64`. -/
  l1 : UInt64
  /-- Limb of weight `2 ^ 128`. -/
  l2 : UInt64
  /-- Limb of weight `2 ^ 192`. -/
  l3 : UInt64
deriving DecidableEq, Repr, Inhabited
```

`Montgomery.Native64x4.Limbs4.zero` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L75))

> The zero value.

```lean
def zero : Limbs4
```

`Montgomery.Native64x4.Limbs4.one` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L78))

> The value one.

```lean
def one : Limbs4
```

`Montgomery.Native64x4.Limbs4.ofNat` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L81))

> Split a natural number into four 64-bit limbs, discarding bits above `2 ^ 256`.

```lean
def ofNat (n : Nat) : Limbs4
```

`Montgomery.Native64x4.Limbs4.toNat` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L85))

> The natural number represented by the limbs: `∑ lᵢ * 2 ^ (64 * i)`.

```lean
def toNat (x : Limbs4) : Nat
```

> ## Limbwise addition and subtraction
>
> Chains return flat words and a `Limbs4` is built only inside a branch: one bound before the
> branch is allocated whether or not that side runs.

`Montgomery.Native64x4.addLimbs` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L96))

> Limbwise add-with-carry: the four sum limbs and the carry out of the top limb.

```lean
def addLimbs (a b : Limbs4) : UInt64 × UInt64 × UInt64 × UInt64 × UInt64
```

`Montgomery.Native64x4.subLimbs` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L105))

> Limbwise subtract-with-borrow: the four difference limbs and the borrow out of the top
> limb.

```lean
def subLimbs (a b : Limbs4) : UInt64 × UInt64 × UInt64 × UInt64 × UInt64
```

> ## Conditional subtraction and field operations

`Montgomery.Native64x4.condSub` (definition, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L115))

> Subtract the modulus once if the value is at least the modulus.

```lean
def condSub (q t : Limbs4) : Limbs4
```

`Montgomery.Native64x4.add` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L121))

> Modular addition; a carry out of the top limb forces the (wrapping, exact) subtraction
> of the modulus, and never happens for a modulus below `2 ^ 255`.

```lean
def add (q a b : Limbs4) : Limbs4
```

`Montgomery.Native64x4.sub` (definition, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L127))

> Modular subtraction: on a borrow, the modulus is added back.

```lean
def sub (q a b : Limbs4) : Limbs4
```

`Montgomery.Native64x4.neg` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L135))

> Modular negation.

```lean
def neg (q a : Limbs4) : Limbs4
```

> ## CIOS multiplication

`Montgomery.Native64x4.State5` (structure, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L140))

> The CIOS accumulator between rounds: four limbs plus one head limb.

```lean
structure State5 where
  /-- Limb of weight `2 ^ 0`. -/
  t0 : UInt64
  /-- Limb of weight `2 ^ 64`. -/
  t1 : UInt64
  /-- Limb of weight `2 ^ 128`. -/
  t2 : UInt64
  /-- Limb of weight `2 ^ 192`. -/
  t3 : UInt64
  /-- Head limb of weight `2 ^ 256`. -/
  t4 : UInt64
deriving DecidableEq, Repr, Inhabited
```

`Montgomery.Native64x4.State6` (structure, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L154))

> The CIOS accumulator after the multiply half of a round: five limbs plus a carry limb.

```lean
structure State6 where
  /-- Limb of weight `2 ^ 0`. -/
  t0 : UInt64
  /-- Limb of weight `2 ^ 64`. -/
  t1 : UInt64
  /-- Limb of weight `2 ^ 128`. -/
  t2 : UInt64
  /-- Limb of weight `2 ^ 192`. -/
  t3 : UInt64
  /-- Limb of weight `2 ^ 256`. -/
  t4 : UInt64
  /-- Carry limb of weight `2 ^ 320`. -/
  t5 : UInt64
deriving DecidableEq, Repr, Inhabited
```

`Montgomery.Native64x4.State5.zero` (definition, [line 172](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L172))

> The zero accumulator.

```lean
def zero : State5
```

`Montgomery.Native64x4.State5.toLimbs4` (definition, [line 175](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L175))

> The four low limbs of the accumulator.

```lean
def toLimbs4 (t : State5) : Limbs4
```

`Montgomery.Native64x4.State5.toNat` (definition, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L178))

> The natural number represented by the accumulator.

```lean
def toNat (t : State5) : Nat
```

`Montgomery.Native64x4.State6.toNat` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L185))

> The natural number represented by the accumulator.

```lean
def toNat (t : State6) : Nat
```

`Montgomery.Native64x4.mulAccum` (definition, [line 192](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L192))

> The multiply half of a CIOS round, `t + a * bi`, keeping the carry out of the head limb.

```lean
def mulAccum (a : Limbs4) (bi : UInt64) (t : State5) : State6
```

`Montgomery.Native64x4.mulReduce` (definition, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L202))

> The reduce half of a CIOS round: add `montM s.t0 negInv * q`, which cancels the low limb,
> and drop that limb; `negInv` must be `-q⁻¹ mod 2 ^ 64`.

```lean
def mulReduce (q : Limbs4) (negInv : UInt64) (s : State6) : State5
```

`Montgomery.Native64x4.mulRound` (definition, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L213))

> One CIOS outer round: accumulate `a * bi` into the accumulator, then reduce away one
> limb.

```lean
def mulRound (q : Limbs4) (negInv : UInt64) (a : Limbs4) (bi : UInt64)
    (t : State5) : State5
```

`Montgomery.Native64x4.condSubWide` (definition, [line 219](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L219))

> `condSub` for an accumulator below `2 * q`; a set head limb forces the (wrapping, exact)
> subtraction of the modulus, and never happens for a modulus below `2 ^ 255`.

```lean
def condSubWide (q : Limbs4) (t : State5) : Limbs4
```

`Montgomery.Native64x4.mul` (definition, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L225))

> CIOS Montgomery multiplication: four rounds followed by one conditional subtraction.

```lean
def mul (q : Limbs4) (negInv : UInt64) (a b : Limbs4) : Limbs4
```

`Montgomery.Native64x4.square` (definition, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean#L233))

> Montgomery squaring.

```lean
def square (q : Limbs4) (negInv : UInt64) (a : Limbs4) : Limbs4
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Montgomery/Native64x4Defs.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Montgomery/Native64x4Defs.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Montgomery.Native64x4Defs.json)
