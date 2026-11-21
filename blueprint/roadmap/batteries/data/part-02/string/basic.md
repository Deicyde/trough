---
catalog: module
lean: String.count, String.toAsciiByteArray
statement: formalized
proof: formalized
---

# String/Basic

`Batteries.Data.String.Basic`, in [Batteries/Data/String/Basic.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/String/Basic.lean), by Jannis Limperg, James Gallicchio, F. G. Dorais.

`String.count` (definition, [line 15](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/String/Basic.lean#L15))

> Count the occurrences of a character in a string.

```lean
def count (s : String) (c : Char) : Nat
```

`String.toAsciiByteArray` (definition, [line 25](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/String/Basic.lean#L25))

> Convert a string of assumed-ASCII characters into a byte array.
> (If any characters are non-ASCII they will be reduced modulo 256.)
>
> Note: if you just need the underlying `ByteArray` of a non-ASCII string,
> use `String.toUTF8`.

```lean
def toAsciiByteArray (s : String) : ByteArray
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/String/Basic.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/String/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.String.Basic.json)
