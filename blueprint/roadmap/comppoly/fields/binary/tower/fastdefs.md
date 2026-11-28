---
catalog: module
lean: ConcreteBinaryTower.Fast.mul2, ConcreteBinaryTower.Fast.mulByZ1, ConcreteBinaryTower.Fast.sq2, ConcreteBinaryTower.Fast.inv2, ConcreteBinaryTower.Fast.mul4, ConcreteBinaryTower.Fast.mulByZ2, ConcreteBinaryTower.Fast.sq4, ConcreteBinaryTower.Fast.inv4, ConcreteBinaryTower.Fast.mul8, ConcreteBinaryTower.Fast.mulByZ3, ConcreteBinaryTower.Fast.sq8, ConcreteBinaryTower.Fast.inv8, ConcreteBinaryTower.Fast.mul16, ConcreteBinaryTower.Fast.mulByZ4, ConcreteBinaryTower.Fast.sq16, ConcreteBinaryTower.Fast.inv16, ConcreteBinaryTower.Fast.mul32, ConcreteBinaryTower.Fast.mulByZ5, ConcreteBinaryTower.Fast.sq32, ConcreteBinaryTower.Fast.inv32, ConcreteBinaryTower.Fast.mul64, ConcreteBinaryTower.Fast.mulByZ6, ConcreteBinaryTower.Fast.sq64, ConcreteBinaryTower.Fast.inv64, ConcreteBinaryTower.Fast.mul8Table, ConcreteBinaryTower.Fast.mulByZ3Table, ConcreteBinaryTower.Fast.sq8Table, ConcreteBinaryTower.Fast.inv8Table, ConcreteBinaryTower.Fast.mul8T, ConcreteBinaryTower.Fast.mulByZ3T, ConcreteBinaryTower.Fast.sq8T, ConcreteBinaryTower.Fast.inv8T, ConcreteBinaryTower.Fast.mulByZ4T, ConcreteBinaryTower.Fast.mulByZ5T, ConcreteBinaryTower.Fast.mulByZ6T, ConcreteBinaryTower.Fast.mul16T, ConcreteBinaryTower.Fast.mul32T, ConcreteBinaryTower.Fast.mul64T, ConcreteBinaryTower.Fast.sq16T, ConcreteBinaryTower.Fast.sq32T, ConcreteBinaryTower.Fast.sq64T, ConcreteBinaryTower.Fast.inv16T, ConcreteBinaryTower.Fast.inv32T, ConcreteBinaryTower.Fast.inv64T, ConcreteBinaryTower.Fast.FastBT128, ConcreteBinaryTower.Fast.FastBT128.add, ConcreteBinaryTower.Fast.FastBT128.mul, ConcreteBinaryTower.Fast.FastBT128.mulByZ, ConcreteBinaryTower.Fast.FastBT128.square, ConcreteBinaryTower.Fast.FastBT128.inv, ConcreteBinaryTower.Fast.FastBT128.ofNat, ConcreteBinaryTower.Fast.FastBT128.toNat
statement: formalized
proof: formalized
---

# Fast binary tower: runtime definitions (zero-import)

`CompPoly.Fields.Binary.Tower.FastDefs`, in [CompPoly/Fields/Binary/Tower/FastDefs.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean), by Georgios Raikos.

> The runtime definitions of the packed binary tower arithmetic, split out of
> `CompPoly.Fields.Binary.Tower.Fast` verbatim. All correctness statements about them
> live in that sibling module, which imports this one.
>
> This module deliberately has **zero imports**: downstream consumers put it into
> `precompileModules` native-compilation lanes, and `precompileModules` compiles the
> entire import closure, so the runtime definitions must not pull in mathlib.

> ## Raw word operations
>
> Names carry the operand bit width (`mul8` multiplies level-3 values in the low 8 bits);
> `mulByZk` multiplies by the tower generator `Z k`. A multiplication rung recombines the
> Karatsuba half-products `p0 = a₀b₀`, `p2 = a₁b₁`, `p1 = (a₀+a₁)(b₀+b₁)` as
> `lo = p0 + p2`, `hi = p1 + lo + Z·p2`; squaring drops the cross term; inversion is the
> quadratic descent of `concrete_inv`. Inputs are assumed in range.

`ConcreteBinaryTower.Fast.mul2` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L34))

> GF(4) multiplication (level 1). `Z 0 = 1` collapses the generic recombination
> `hi = p1 + lo + Z·p2` to `hi = p1 + p0`, saving a xor on the ladder's hottest rung.

```lean
def mul2 (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ1` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L45))

> Multiplication by the level-1 generator `Z 1`.

```lean
def mulByZ1 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq2` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L51))

> GF(4) squaring.

```lean
def sq2 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv2` (definition, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L58))

> GF(4) inversion (`0 ↦ 0`), in the shape of the recursive twin so `inv2_eq_rec`
> is `rfl`.

```lean
def inv2 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul4` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L66))

> GF(2^4) multiplication (level 2).

```lean
def mul4 (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ2` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L78))

> Multiplication by the level-2 generator `Z 2`.

```lean
def mulByZ2 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq4` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L84))

> GF(2^4) squaring.

```lean
def sq4 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv4` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L90))

> GF(2^4) inversion (`0 ↦ 0`).

```lean
def inv4 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul8` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L99))

> GF(2^8) multiplication (level 3).

```lean
def mul8 (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ3` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L111))

> Multiplication by the level-3 generator `Z 3`.

```lean
def mulByZ3 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq8` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L117))

> GF(2^8) squaring.

```lean
def sq8 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv8` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L123))

> GF(2^8) inversion (`0 ↦ 0`).

```lean
def inv8 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul16` (definition, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L132))

> GF(2^16) multiplication (level 4).

```lean
def mul16 (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ4` (definition, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L144))

> Multiplication by the level-4 generator `Z 4`.

```lean
def mulByZ4 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq16` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L150))

> GF(2^16) squaring.

```lean
def sq16 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv16` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L156))

> GF(2^16) inversion (`0 ↦ 0`).

```lean
def inv16 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul32` (definition, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L166))

> GF(2^32) multiplication (level 5). Outlined: inlining the whole ladder above this
> width exceeds the compiler's recursion depth.

```lean
def mul32 (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ5` (definition, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L178))

> Multiplication by the level-5 generator `Z 5`.

```lean
def mulByZ5 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq32` (definition, [line 184](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L184))

> GF(2^32) squaring.

```lean
def sq32 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv32` (definition, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L190))

> GF(2^32) inversion (`0 ↦ 0`).

```lean
def inv32 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul64` (definition, [line 199](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L199))

> GF(2^64) multiplication (level 6). Outlined, see `mul32`.

```lean
def mul64 (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ6` (definition, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L211))

> Multiplication by the level-6 generator `Z 6`.

```lean
def mulByZ6 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq64` (definition, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L217))

> GF(2^64) squaring.

```lean
def sq64 (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv64` (definition, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L223))

> GF(2^64) inversion (`0 ↦ 0`).

```lean
def inv64 (v : UInt64) : UInt64
```

> ## GF(2^8) tables and table-based rungs
>
> Level-3 operations as byte-table lookups, tables generated from the ladder by
> `Array.ofFn`; the wider `*T` rungs rebuild the ladder on the table base.

`ConcreteBinaryTower.Fast.mul8Table` (definition, [line 237](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L237))

> `mul8` product table.

```lean
def mul8Table : ByteArray
```

`ConcreteBinaryTower.Fast.mulByZ3Table` (definition, [line 242](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L242))

> `mulByZ3` table.

```lean
def mulByZ3Table : ByteArray
```

`ConcreteBinaryTower.Fast.sq8Table` (definition, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L246))

> `sq8` table.

```lean
def sq8Table : ByteArray
```

`ConcreteBinaryTower.Fast.inv8Table` (definition, [line 250](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L250))

> `inv8` table (`0 ↦ 0`).

```lean
def inv8Table : ByteArray
```

`ConcreteBinaryTower.Fast.mul8T` (definition, [line 254](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L254))

> `mul8` by table lookup.

```lean
def mul8T (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ3T` (definition, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L258))

> `mulByZ3` by table lookup.

```lean
def mulByZ3T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq8T` (definition, [line 261](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L261))

> `sq8` by table lookup.

```lean
def sq8T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv8T` (definition, [line 264](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L264))

> `inv8` by table lookup.

```lean
def inv8T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ4T` (definition, [line 267](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L267))

> Table-based twin of `mulByZ4`.

```lean
def mulByZ4T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ5T` (definition, [line 273](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L273))

> Table-based twin of `mulByZ5`.

```lean
def mulByZ5T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mulByZ6T` (definition, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L279))

> Table-based twin of `mulByZ6`.

```lean
def mulByZ6T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul16T` (definition, [line 285](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L285))

> Table-based twin of `mul16`.

```lean
def mul16T (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul32T` (definition, [line 297](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L297))

> Table-based twin of `mul32`.

```lean
def mul32T (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.mul64T` (definition, [line 309](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L309))

> Table-based twin of `mul64`.

```lean
def mul64T (a b : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq16T` (definition, [line 321](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L321))

> Table-based twin of `sq16`.

```lean
def sq16T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq32T` (definition, [line 327](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L327))

> Table-based twin of `sq32`.

```lean
def sq32T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.sq64T` (definition, [line 333](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L333))

> Table-based twin of `sq64`.

```lean
def sq64T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv16T` (definition, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L339))

> Table-based twin of `inv16`.

```lean
def inv16T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv32T` (definition, [line 348](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L348))

> Table-based twin of `inv32`.

```lean
def inv32T (v : UInt64) : UInt64
```

`ConcreteBinaryTower.Fast.inv64T` (definition, [line 357](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L357))

> Table-based twin of `inv64`.

```lean
def inv64T (v : UInt64) : UInt64
```

> ## Level 7: GF(2^128)
>
> The tower split falls on the limb boundary, so the halves are the limbs.

`ConcreteBinaryTower.Fast.FastBT128` (structure, [line 370](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L370))

> A level-7 tower field element as two limbs, `lo` the low half.

```lean
structure FastBT128 where
  lo : UInt64
  hi : UInt64
  deriving DecidableEq, Inhabited
```

`ConcreteBinaryTower.Fast.FastBT128.add` (definition, [line 378](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L378))

> Addition is limbwise XOR.

```lean
def add (a b : FastBT128) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.mul` (definition, [line 381](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L381))

> Multiplication: Karatsuba over the limbs with a `Z 6` generator reduction.

```lean
def mul (a b : FastBT128) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.mulByZ` (definition, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L389))

> Multiply by the level-7 generator `Z 7`: swap halves, fold `Z 6` into the new high.

```lean
def mulByZ (v : FastBT128) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.square` (definition, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L392))

> Squaring: the Karatsuba cross term vanishes in characteristic 2.

```lean
def square (v : FastBT128) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.inv` (definition, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L398))

> Inversion by quadratic descent (`0 ↦ 0`); same recursion as `concrete_inv`.

```lean
def inv (v : FastBT128) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.ofNat` (definition, [line 405](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L405))

> Truncating constructor from `Nat`, low limb first.

```lean
def ofNat (n : Nat) : FastBT128
```

`ConcreteBinaryTower.Fast.FastBT128.toNat` (definition, [line 408](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean#L408))

> The canonical value of a two-limb element.

```lean
def toNat (v : FastBT128) : Nat
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Binary/Tower/FastDefs.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Binary/Tower/FastDefs.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Tower.FastDefs.json)
