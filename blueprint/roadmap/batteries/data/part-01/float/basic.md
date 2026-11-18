---
catalog: module
lean: Float.pi, Float.toRatParts, Float.toRatParts', Float.toStringFull, Float32.pi, Float32.toRatParts, Float32.toRatParts', Float32.toStringFull, Nat.divFloat, Int.divFloat
statement: formalized
proof: formalized
---

# Float/Basic

`Batteries.Data.Float.Basic`, in [Batteries/Data/Float/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean).

`Float.pi` (definition, [line 15](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L15))

> The floating point value closest to the mathematical constant `π`.

```lean
def pi : Float
```

`Float.toRatParts` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L20))

> Returns `v, exp` integers such that `f = v * 2^exp`.
> (`e` is not minimal, but `v.abs` will be at most `2^53 - 1`.)
> Returns `none` when `f` is not finite (i.e. `inf`, `-inf` or a `nan`).

```lean
def toRatParts (f : Float) : Option (Int × Int)
```

`Float.toRatParts'` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L35))

> Returns `v, exp` integers such that `f = v * 2^exp`.
> Like `toRatParts`, but `e` is guaranteed to be minimal (`v` is always odd), unless `v = 0`.
> `v.abs` will be at most `2^53 - 1` because `Float` has 53 bits of precision.
> Returns `none` when `f` is not finite (i.e. `inf`, `-inf` or a `nan`).

```lean
partial def toRatParts' (f : Float) : Option (Int × Int)
```

`Float.toStringFull` (definition, [line 52](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L52))

> Converts `f` to a string, including all decimal digits.

```lean
def toStringFull (f : Float) : String
```

`Float32.pi` (definition, [line 77](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L77))

> The floating point value closest to the mathematical constant `π`.

```lean
def pi : Float32
```

`Float32.toRatParts` (definition, [line 82](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L82))

> Returns `v, exp` integers such that `f = v * 2^exp`.
> (`e` is not minimal, but `v.abs` will be at most `2^24 - 1`.)
> Returns `none` when `f` is not finite (i.e. `inf`, `-inf` or a `nan`).

```lean
def toRatParts (f : Float32) : Option (Int × Int)
```

`Float32.toRatParts'` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L97))

> Returns `v, exp` integers such that `f = v * 2^exp`.
> Like `toRatParts`, but `e` is guaranteed to be minimal (`v` is always odd), unless `v = 0`.
> `v.abs` will be at most `2^24 - 1` because `Float32` has 24 bits of precision.
> Returns `none` when `f` is not finite (i.e. `inf`, `-inf` or a `nan`).

```lean
partial def toRatParts' (f : Float32) : Option (Int × Int)
```

`Float32.toStringFull` (definition, [line 112](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L112))

> Converts `f` to a string, including all decimal digits.

```lean
def toStringFull (f : Float32) : String
```

`Nat.divFloat` (definition, [line 137](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L137))

> Divide two natural numbers, to produce a correctly rounded (nearest-ties-to-even) `Float` result.

```lean
protected def Nat.divFloat (a b : Nat) : Float
```

`Int.divFloat` (definition, [line 155](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean#L155))

> Divide two integers, to produce a correctly rounded (nearest-ties-to-even) `Float` result.

```lean
protected def Int.divFloat (a b : Int) : Float
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Float/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Float/Basic.lean)
