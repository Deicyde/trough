---
catalog: module
lean: Float.Model.UnpackedFloat.Sign.neg_neg, Float.Model.UnpackedFloat.Sign.neg_mul, Float.Model.UnpackedFloat.Sign.mul_neg, Float.Model.UnpackedFloat.Sign.neg_div, Float.Model.UnpackedFloat.Sign.div_neg, Float.Model.UnpackedFloat.Sign.mul_comm, Float.Model.UnpackedFloat.neg_neg, Float.Model.UnpackedFloat.unpack_packComponents_neg, Float.Model.UnpackedFloat.flipSign, Float.Model.UnpackedFloat.unpack_flipSign, Float.Model.UnpackedFloat.unpack_pack_neg_unpack, Float.Model.UnpackedFloat.flipSign_packComponents, Float.Model.UnpackedFloat.pack_neg, Float.Model.UnpackedFloat.roundWithAccuracy_neg, Float.Model.UnpackedFloat.neg_mul, Float.Model.UnpackedFloat.mul_neg, Float.Model.UnpackedFloat.neg_div, Float.Model.UnpackedFloat.div_neg, Float.Model.UnpackedFloat.mul_comm, Float.Model.UnpackedFloat.add_comm, Float.Model.UnpackedFloat.fma_comm, Float.Model.unpack_pack_unpack, Float.Model.unpack_pack_neg_unpack, Float.Model.pack_unpack, Float.Model.neg_pack, Float.Model.neg_neg, Float.Model.neg_mul, Float.Model.mul_neg, Float.Model.neg_div, Float.Model.div_neg, Float.Model.mul_comm, Float.Model.add_comm, Float.Model.fma_comm, Float.neg_neg, Float.neg_mul, Float.mul_neg, Float.neg_div, Float.div_neg, Float.mul_comm, Float.add_comm, Float.fma_comm, Float32.Model.unpack_pack_unpack, Float32.Model.unpack_pack_neg_unpack, Float32.Model.pack_unpack, Float32.Model.neg_pack, Float32.Model.neg_neg, Float32.Model.neg_mul, Float32.Model.mul_neg, Float32.Model.neg_div, Float32.Model.div_neg, Float32.Model.mul_comm, Float32.Model.add_comm, Float32.Model.fma_comm, Float32.neg_neg, Float32.neg_mul, Float32.mul_neg, Float32.neg_div, Float32.div_neg, Float32.mul_comm, Float32.add_comm, Float32.fma_comm
statement: formalized
proof: formalized
---

# Sign and commutativity lemmas for `Float` and `Float32`

`Batteries.Data.Float.Lemmas.Arithmetic`, in [Batteries/Data/Float/Lemmas/Arithmetic.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean), by François G. Dorais.

> The lemmas are proved through the logical models `Float.Model` and `Float32.Model`.

`Float.Model.UnpackedFloat.Sign.neg_neg` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L22))

```lean
protected theorem neg_neg (s : Sign) : - -s = s
```

`Float.Model.UnpackedFloat.Sign.neg_mul` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L24))

```lean
protected theorem neg_mul (s t : Sign) : -s * t = -(s * t)
```

`Float.Model.UnpackedFloat.Sign.mul_neg` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L26))

```lean
protected theorem mul_neg (s t : Sign) : s * -t = -(s * t)
```

`Float.Model.UnpackedFloat.Sign.neg_div` (theorem, [line 28](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L28))

```lean
protected theorem neg_div (s t : Sign) : -s / t = -(s / t)
```

`Float.Model.UnpackedFloat.Sign.div_neg` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L30))

```lean
protected theorem div_neg (s t : Sign) : s / -t = -(s / t)
```

`Float.Model.UnpackedFloat.Sign.mul_comm` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L32))

```lean
protected theorem mul_comm (s t : Sign) : s * t = t * s
```

`Float.Model.UnpackedFloat.neg_neg` (theorem, [line 36](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L36))

```lean
protected theorem neg_neg (u : UnpackedFloat) : u.neg.neg = u
```

`Float.Model.UnpackedFloat.unpack_packComponents_neg` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L39))

```lean
theorem unpack_packComponents_neg {spec : Format} (s e m) :
    unpack spec (packComponents spec (-s) e m) = (unpack spec (packComponents spec s e m)).neg
```

`Float.Model.UnpackedFloat.flipSign` (definition, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L51))

> The bit pattern `b` with its sign bit flipped.

```lean
def flipSign {spec : Format} (b : BitVec spec.numBits) : BitVec spec.numBits
```

`Float.Model.UnpackedFloat.unpack_flipSign` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L54))

```lean
theorem unpack_flipSign {spec : Format} (b : BitVec spec.numBits) :
    unpack spec (flipSign b) = (unpack spec b).neg
```

`Float.Model.UnpackedFloat.unpack_pack_neg_unpack` (theorem, [line 59](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L59))

```lean
theorem unpack_pack_neg_unpack {spec : Format} (b : BitVec spec.numBits) :
    unpack spec (pack spec (unpack spec b).neg) = (unpack spec b).neg
```

`Float.Model.UnpackedFloat.flipSign_packComponents` (theorem, [line 63](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L63))

```lean
theorem flipSign_packComponents {spec : Format} (s e m) :
    flipSign (packComponents spec s e m) = packComponents spec (-s) e m
```

`Float.Model.UnpackedFloat.pack_neg` (theorem, [line 68](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L68))

> Packing commutes with negation, except on NaN.

```lean
theorem pack_neg {spec : Format} {u : UnpackedFloat} (h : u ≠ notANumber) :
    pack spec u.neg = flipSign (pack spec u)
```

`Float.Model.UnpackedFloat.roundWithAccuracy_neg` (theorem, [line 80](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L80))

```lean
theorem roundWithAccuracy_neg (spec : Format) (s m e a) :
    roundWithAccuracy spec (-s) m e a = (roundWithAccuracy spec s m e a).neg
```

`Float.Model.UnpackedFloat.neg_mul` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L85))

```lean
protected theorem neg_mul (spec : Format) (u v : UnpackedFloat) :
    mul spec u.neg v = (mul spec u v).neg
```

`Float.Model.UnpackedFloat.mul_neg` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L89))

```lean
protected theorem mul_neg (spec : Format) (u v : UnpackedFloat) :
    mul spec u v.neg = (mul spec u v).neg
```

`Float.Model.UnpackedFloat.neg_div` (theorem, [line 93](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L93))

```lean
protected theorem neg_div (spec : Format) (u v : UnpackedFloat) :
    div spec u.neg v = (div spec u v).neg
```

`Float.Model.UnpackedFloat.div_neg` (theorem, [line 97](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L97))

```lean
protected theorem div_neg (spec : Format) (u v : UnpackedFloat) :
    div spec u v.neg = (div spec u v).neg
```

`Float.Model.UnpackedFloat.mul_comm` (theorem, [line 101](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L101))

```lean
protected theorem mul_comm (spec : Format) (u v : UnpackedFloat) :
    mul spec u v = mul spec v u
```

`Float.Model.UnpackedFloat.add_comm` (theorem, [line 105](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L105))

```lean
protected theorem add_comm (spec : Format) (u v : UnpackedFloat) :
    add spec u v = add spec v u
```

`Float.Model.UnpackedFloat.fma_comm` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L112))

```lean
protected theorem fma_comm (spec : Format) (u v w : UnpackedFloat) :
    fma spec u v w = fma spec v u w
```

`Float.Model.unpack_pack_unpack` (theorem, [line 120](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L120))

```lean
theorem unpack_pack_unpack (a : Float.Model) : (pack a.unpack).unpack = a.unpack
```

`Float.Model.unpack_pack_neg_unpack` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L123))

```lean
theorem unpack_pack_neg_unpack (a : Float.Model) :
    (pack a.unpack.neg).unpack = a.unpack.neg
```

`Float.Model.pack_unpack` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L127))

```lean
theorem pack_unpack (a : Float.Model) : pack a.unpack = a
```

`Float.Model.neg_pack` (theorem, [line 134](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L134))

> Negation of a packed float.

```lean
theorem neg_pack (u : UnpackedFloat) : -(pack u) = pack u.neg
```

`Float.Model.neg_neg` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L143))

```lean
protected theorem neg_neg (a : Float.Model) : - -a = a
```

`Float.Model.neg_mul` (theorem, [line 147](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L147))

```lean
protected theorem neg_mul (a b : Float.Model) : -a * b = -(a * b)
```

`Float.Model.mul_neg` (theorem, [line 151](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L151))

```lean
protected theorem mul_neg (a b : Float.Model) : a * -b = -(a * b)
```

`Float.Model.neg_div` (theorem, [line 155](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L155))

```lean
protected theorem neg_div (a b : Float.Model) : -a / b = -(a / b)
```

`Float.Model.div_neg` (theorem, [line 159](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L159))

```lean
protected theorem div_neg (a b : Float.Model) : a / -b = -(a / b)
```

`Float.Model.mul_comm` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L163))

```lean
protected theorem mul_comm (a b : Float.Model) : a * b = b * a
```

`Float.Model.add_comm` (theorem, [line 167](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L167))

```lean
protected theorem add_comm (a b : Float.Model) : a + b = b + a
```

`Float.Model.fma_comm` (theorem, [line 171](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L171))

```lean
protected theorem fma_comm (a b c : Float.Model) : a.fma b c = b.fma a c
```

`Float.neg_neg` (theorem, [line 180](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L180))

```lean
protected theorem neg_neg (x : Float) : - -x = x
```

`Float.neg_mul` (theorem, [line 184](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L184))

```lean
protected theorem neg_mul (x y : Float) : -x * y = -(x * y)
```

`Float.mul_neg` (theorem, [line 188](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L188))

```lean
protected theorem mul_neg (x y : Float) : x * -y = -(x * y)
```

`Float.neg_div` (theorem, [line 192](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L192))

```lean
protected theorem neg_div (x y : Float) : -x / y = -(x / y)
```

`Float.div_neg` (theorem, [line 196](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L196))

```lean
protected theorem div_neg (x y : Float) : x / -y = -(x / y)
```

`Float.mul_comm` (theorem, [line 200](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L200))

```lean
protected theorem mul_comm (x y : Float) : x * y = y * x
```

`Float.add_comm` (theorem, [line 204](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L204))

```lean
protected theorem add_comm (x y : Float) : x + y = y + x
```

`Float.fma_comm` (theorem, [line 208](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L208))

```lean
protected theorem fma_comm (x y z : Float) : x.fma y z = y.fma x z
```

`Float32.Model.unpack_pack_unpack` (theorem, [line 218](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L218))

```lean
theorem unpack_pack_unpack (a : Float32.Model) : (pack a.unpack).unpack = a.unpack
```

`Float32.Model.unpack_pack_neg_unpack` (theorem, [line 221](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L221))

```lean
theorem unpack_pack_neg_unpack (a : Float32.Model) :
    (pack a.unpack.neg).unpack = a.unpack.neg
```

`Float32.Model.pack_unpack` (theorem, [line 225](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L225))

```lean
theorem pack_unpack (a : Float32.Model) : pack a.unpack = a
```

`Float32.Model.neg_pack` (theorem, [line 232](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L232))

> Negation of a packed float.

```lean
theorem neg_pack (u : UnpackedFloat) : -(pack u) = pack u.neg
```

`Float32.Model.neg_neg` (theorem, [line 241](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L241))

```lean
protected theorem neg_neg (a : Float32.Model) : - -a = a
```

`Float32.Model.neg_mul` (theorem, [line 245](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L245))

```lean
protected theorem neg_mul (a b : Float32.Model) : -a * b = -(a * b)
```

`Float32.Model.mul_neg` (theorem, [line 249](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L249))

```lean
protected theorem mul_neg (a b : Float32.Model) : a * -b = -(a * b)
```

`Float32.Model.neg_div` (theorem, [line 253](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L253))

```lean
protected theorem neg_div (a b : Float32.Model) : -a / b = -(a / b)
```

`Float32.Model.div_neg` (theorem, [line 257](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L257))

```lean
protected theorem div_neg (a b : Float32.Model) : a / -b = -(a / b)
```

`Float32.Model.mul_comm` (theorem, [line 261](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L261))

```lean
protected theorem mul_comm (a b : Float32.Model) : a * b = b * a
```

`Float32.Model.add_comm` (theorem, [line 265](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L265))

```lean
protected theorem add_comm (a b : Float32.Model) : a + b = b + a
```

`Float32.Model.fma_comm` (theorem, [line 269](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L269))

```lean
protected theorem fma_comm (a b c : Float32.Model) : a.fma b c = b.fma a c
```

`Float32.neg_neg` (theorem, [line 278](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L278))

```lean
protected theorem neg_neg (x : Float32) : - -x = x
```

`Float32.neg_mul` (theorem, [line 282](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L282))

```lean
protected theorem neg_mul (x y : Float32) : -x * y = -(x * y)
```

`Float32.mul_neg` (theorem, [line 286](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L286))

```lean
protected theorem mul_neg (x y : Float32) : x * -y = -(x * y)
```

`Float32.neg_div` (theorem, [line 290](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L290))

```lean
protected theorem neg_div (x y : Float32) : -x / y = -(x / y)
```

`Float32.div_neg` (theorem, [line 294](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L294))

```lean
protected theorem div_neg (x y : Float32) : x / -y = -(x / y)
```

`Float32.mul_comm` (theorem, [line 298](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L298))

```lean
protected theorem mul_comm (x y : Float32) : x * y = y * x
```

`Float32.add_comm` (theorem, [line 302](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L302))

```lean
protected theorem add_comm (x y : Float32) : x + y = y + x
```

`Float32.fma_comm` (theorem, [line 306](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean#L306))

```lean
protected theorem fma_comm (x y z : Float32) : x.fma y z = y.fma x z
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Lemmas/Basic](basic.md)

## Sources

- [Batteries/Data/Float/Lemmas/Arithmetic.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Lemmas/Arithmetic.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.Float.Lemmas.Arithmetic.json)
