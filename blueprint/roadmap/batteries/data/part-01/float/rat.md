---
catalog: module
lean: Rat.toFloat, Float.toRat?, Float.toRat0
statement: formalized
proof: formalized
---

# Rational Numbers and Float

`Batteries.Data.Float.Rat`, in [Batteries/Data/Float/Rat.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Rat.lean), by Mario Carneiro.

`Rat.toFloat` (definition, [line 17](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Rat.lean#L17))

> Convert this rational number to a `Float` value.

```lean
protected def toFloat (a : Rat) : Float
```

`Float.toRat?` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Rat.lean#L20))

> Convert this floating point number to a rational value.

```lean
protected def _root_.Float.toRat? (a : Float) : Option Rat
```

`Float.toRat0` (definition, [line 28](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Rat.lean#L28))

> Convert this floating point number to a rational value,
> mapping non-finite values (`inf`, `-inf`, `nan`) to 0.

```lean
protected def _root_.Float.toRat0 (a : Float) : Rat
```

## Depends on

- [Float/Basic](basic.md)

## Sources

- [Batteries/Data/Float/Rat.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Float/Rat.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Float.Rat.json)
