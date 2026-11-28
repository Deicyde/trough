---
catalog: module
lean: Float.Category, Float.signMask, Float.exponentMask, Float.significandMask, Float.classify, Float.isNormal, Float.isSubnormal, Float.signBit, Float.copySign, Float.nextUp, Float.nextDown, Float.ulp, Float.toOrdinal, Float.toOrdinal?, Float.toOrdinal!, Float.ulpDistance, Float.ulpDistance?, Float.ulpDistance!, Float.toOrdinal?_eq_some, Float.toOrdinal?_eq_none, Float.toOrdinal!_eq, Float.ulpDistance?_eq_some, Float.ulpDistance?_eq_none, Float.ulpDistance!_eq, Float32.signMask, Float32.exponentMask, Float32.significandMask, Float32.classify, Float32.isNormal, Float32.isSubnormal, Float32.signBit, Float32.copySign, Float32.nextUp, Float32.nextDown, Float32.ulp, Float32.toOrdinal, Float32.toOrdinal?, Float32.toOrdinal!, Float32.ulpDistance, Float32.ulpDistance?, Float32.ulpDistance!, Float32.toOrdinal?_eq_some, Float32.toOrdinal?_eq_none, Float32.toOrdinal!_eq, Float32.ulpDistance?_eq_some, Float32.ulpDistance?_eq_none, Float32.ulpDistance!_eq
statement: formalized
proof: formalized
---

# Bit-level utilities for `Float` and `Float32`

`Batteries.Data.Float.Bits`, in [Batteries/Data/Float/Bits.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean).

> Classification, sign manipulation and neighbor functions from IEEE 754-2019 §5.3.1, §5.5.1 and
> §5.7.2, together with unit in the last place and distance in units in the last place.
>
> All functions are defined in terms of `toBits` and `ofBits` and check for `NaN` first. The logical
> model of Lean's floats has a single canonical `NaN`, while compiled code may see any `NaN` bit
> pattern, so this keeps the compiled behavior in line with the model. As a consequence, `NaN` has
> no sign here: `signBit nan = false`, and `copySign x nan` is `x` with a positive sign.

`Float.Category` (inductive type, [line 21](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L21))

> The class of a floating-point number, following IEEE 754-2019 §5.7.2.

```lean
public inductive Float.Category where
  /-- Not a number. -/
  | nan
  /-- Positive or negative infinity. -/
  | infinite
  /-- Positive or negative zero. -/
  | zero
  /-- A nonzero number whose exponent field is zero. -/
  | subnormal
  /-- A finite number whose exponent field is not zero. -/
  | normal
deriving DecidableEq, Repr, Inhabited
```

`Float.signMask` (definition, [line 37](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L37))

> The sign bit of a `Float`.

```lean
public def signMask : UInt64
```

`Float.exponentMask` (definition, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L40))

> The exponent field of a `Float`.

```lean
public def exponentMask : UInt64
```

`Float.significandMask` (definition, [line 43](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L43))

> The significand field of a `Float`.

```lean
public def significandMask : UInt64
```

`Float.classify` (definition, [line 46](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L46))

> The class of `x`, as in IEEE 754-2019 §5.7.2.

```lean
public def classify (x : Float) : Category
```

`Float.isNormal` (definition, [line 55](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L55))

> Whether `x` is a normal number: finite, nonzero and not subnormal.

```lean
public def isNormal (x : Float) : Bool
```

`Float.isSubnormal` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L58))

> Whether `x` is a subnormal number.

```lean
public def isSubnormal (x : Float) : Bool
```

`Float.signBit` (definition, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L65))

> Whether the sign bit of `x` is set, as in IEEE 754-2019 §5.7.2 `isSignMinus`.
>
> This is `true` for `-0` and `false` for `NaN`, since Lean's floats have a single `NaN` value.

```lean
public def signBit (x : Float) : Bool
```

`Float.copySign` (definition, [line 73](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L73))

> The value `x` with the sign of `y`, as in IEEE 754-2019 §5.5.1.
>
> `NaN` inputs follow `signBit`: `copySign nan y = nan` and `copySign x nan` has a positive sign.

```lean
public def copySign (x y : Float) : Float
```

`Float.nextUp` (definition, [line 83](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L83))

> The least floating-point number that compares greater than `x`, as in IEEE 754-2019 §5.3.1.
>
> Special cases: `nextUp nan = nan`, `nextUp inf = inf`, `nextUp (-inf)` is the most negative
> finite number, and `nextUp` of either zero is the smallest positive subnormal number.

```lean
public def nextUp (x : Float) : Float
```

`Float.nextDown` (definition, [line 96](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L96))

> The greatest floating-point number that compares less than `x`, as in IEEE 754-2019 §5.3.1.
>
> This is `-nextUp (-x)`.

```lean
public def nextDown (x : Float) : Float
```

`Float.ulp` (definition, [line 106](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L106))

> The unit in the last place of `x`: the distance from `|x|` to the next number of larger
> magnitude. For the largest finite number, it is the distance to the next number of smaller
> magnitude. This agrees with Julia's `eps(x)`.
>
> Special cases: `ulp 0` is the smallest positive subnormal number, and `ulp x = nan` when `x` is
> infinite or `NaN`.

```lean
public def ulp (x : Float) : Float
```

`Float.toOrdinal` (definition, [line 119](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L119))

> The position of `x` on the number line that counts floating-point numbers, with both zeros at
> `0`, positive numbers at their bit pattern and negative numbers at the negation of the bit
> pattern of their absolute value. Infinities sit one step past the largest finite numbers.
> `x` must not be `NaN`; see also `toOrdinal?` and `toOrdinal!`.

```lean
public def toOrdinal (x : Float) (_ : x.isNaN = false) : Int
```

`Float.toOrdinal?` (definition, [line 125](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L125))

> The position of `x` on the number line that counts floating-point numbers, as in
> `toOrdinal`, or `none` when `x` is `NaN`.

```lean
public def toOrdinal? (x : Float) : Option Int
```

`Float.toOrdinal!` (definition, [line 130](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L130))

> The position of `x` on the number line that counts floating-point numbers, as in
> `toOrdinal`. Panics when `x` is `NaN`.

```lean
public def toOrdinal! (x : Float) : Int
```

`Float.ulpDistance` (definition, [line 139](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L139))

> The number of floating-point numbers between `x` and `y`, counting one of the endpoints: the
> distance between them in units in the last place. Both zeros count as the same point and the
> infinities are one step beyond the largest finite numbers. Neither argument may be `NaN`; see
> also `ulpDistance?` and `ulpDistance!`.

```lean
public def ulpDistance (x y : Float) (hx : x.isNaN = false) (hy : y.isNaN = false) :
    Nat
```

`Float.ulpDistance?` (definition, [line 145](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L145))

> The distance between `x` and `y` in units in the last place, as in `ulpDistance`, or
> `none` when either argument is `NaN`.

```lean
public def ulpDistance? (x y : Float) : Option Nat
```

`Float.ulpDistance!` (definition, [line 150](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L150))

> The distance between `x` and `y` in units in the last place, as in `ulpDistance`.
> Panics when either argument is `NaN`.

```lean
public def ulpDistance! (x y : Float) : Nat
```

`Float.toOrdinal?_eq_some` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L154))

```lean
public theorem toOrdinal?_eq_some {x : Float} (h : x.isNaN = false) :
    x.toOrdinal? = some (x.toOrdinal h)
```

`Float.toOrdinal?_eq_none` (theorem, [line 157](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L157))

```lean
public theorem toOrdinal?_eq_none {x : Float} (h : x.isNaN = true) : x.toOrdinal? = none
```

`Float.toOrdinal!_eq` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L160))

```lean
public theorem toOrdinal!_eq {x : Float} (h : x.isNaN = false) : x.toOrdinal! = x.toOrdinal h
```

`Float.ulpDistance?_eq_some` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L163))

```lean
public theorem ulpDistance?_eq_some {x y : Float} (hx : x.isNaN = false) (hy : y.isNaN = false) :
    ulpDistance? x y = some (ulpDistance x y hx hy)
```

`Float.ulpDistance?_eq_none` (theorem, [line 166](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L166))

```lean
public theorem ulpDistance?_eq_none {x y : Float} (h : x.isNaN = true ∨ y.isNaN = true) :
    ulpDistance? x y = none
```

`Float.ulpDistance!_eq` (theorem, [line 170](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L170))

```lean
public theorem ulpDistance!_eq {x y : Float} (hx : x.isNaN = false) (hy : y.isNaN = false) :
    ulpDistance! x y = ulpDistance x y hx hy
```

`Float32.signMask` (definition, [line 178](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L178))

> The sign bit of a `Float32`.

```lean
public def signMask : UInt32
```

`Float32.exponentMask` (definition, [line 181](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L181))

> The exponent field of a `Float32`.

```lean
public def exponentMask : UInt32
```

`Float32.significandMask` (definition, [line 184](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L184))

> The significand field of a `Float32`.

```lean
public def significandMask : UInt32
```

`Float32.classify` (definition, [line 186](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L186))

```lean
public def classify (x : Float32) : Float.Category
```

`Float32.isNormal` (definition, [line 195](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L195))

```lean
public def isNormal (x : Float32) : Bool
```

`Float32.isSubnormal` (definition, [line 198](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L198))

```lean
public def isSubnormal (x : Float32) : Bool
```

`Float32.signBit` (definition, [line 200](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L200))

```lean
public def signBit (x : Float32) : Bool
```

`Float32.copySign` (definition, [line 203](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L203))

```lean
public def copySign (x y : Float32) : Float32
```

`Float32.nextUp` (definition, [line 207](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L207))

```lean
public def nextUp (x : Float32) : Float32
```

`Float32.nextDown` (definition, [line 215](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L215))

```lean
public def nextDown (x : Float32) : Float32
```

`Float32.ulp` (definition, [line 225](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L225))

> The unit in the last place of `x`: the distance from `|x|` to the next number of larger
> magnitude. For the largest finite number, it is the distance to the next number of smaller
> magnitude. This agrees with Julia's `eps(x)`.
>
> Special cases: `ulp 0` is the smallest positive subnormal number, and `ulp x = nan` when `x` is
> infinite or `NaN`.

```lean
public def ulp (x : Float32) : Float32
```

`Float32.toOrdinal` (definition, [line 233](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L233))

```lean
public def toOrdinal (x : Float32) (_ : x.isNaN = false) : Int
```

`Float32.toOrdinal?` (definition, [line 237](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L237))

```lean
public def toOrdinal? (x : Float32) : Option Int
```

`Float32.toOrdinal!` (definition, [line 240](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L240))

```lean
public def toOrdinal! (x : Float32) : Int
```

`Float32.ulpDistance` (definition, [line 244](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L244))

```lean
public def ulpDistance (x y : Float32) (hx : x.isNaN = false) (hy : y.isNaN = false) : Nat
```

`Float32.ulpDistance?` (definition, [line 247](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L247))

```lean
public def ulpDistance? (x y : Float32) : Option Nat
```

`Float32.ulpDistance!` (definition, [line 250](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L250))

```lean
public def ulpDistance! (x y : Float32) : Nat
```

`Float32.toOrdinal?_eq_some` (theorem, [line 254](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L254))

```lean
public theorem toOrdinal?_eq_some {x : Float32} (h : x.isNaN = false) :
    x.toOrdinal? = some (x.toOrdinal h)
```

`Float32.toOrdinal?_eq_none` (theorem, [line 257](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L257))

```lean
public theorem toOrdinal?_eq_none {x : Float32} (h : x.isNaN = true) : x.toOrdinal? = none
```

`Float32.toOrdinal!_eq` (theorem, [line 260](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L260))

```lean
public theorem toOrdinal!_eq {x : Float32} (h : x.isNaN = false) :
    x.toOrdinal! = x.toOrdinal h
```

`Float32.ulpDistance?_eq_some` (theorem, [line 264](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L264))

```lean
public theorem ulpDistance?_eq_some {x y : Float32} (hx : x.isNaN = false) (hy : y.isNaN = false) :
    ulpDistance? x y = some (ulpDistance x y hx hy)
```

`Float32.ulpDistance?_eq_none` (theorem, [line 267](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L267))

```lean
public theorem ulpDistance?_eq_none {x y : Float32} (h : x.isNaN = true ∨ y.isNaN = true) :
    ulpDistance? x y = none
```

`Float32.ulpDistance!_eq` (theorem, [line 271](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean#L271))

```lean
public theorem ulpDistance!_eq {x y : Float32} (hx : x.isNaN = false) (hy : y.isNaN = false) :
    ulpDistance! x y = ulpDistance x y hx hy
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Float/Bits.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Bits.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Float.Bits.json)
