---
catalog: module
lean: Int.testBit, Int.ofBits, Int.ofBits_zero, Int.testBit_ofBits_lt, Int.testBit_ofBits_ge, Int.testBit_ofBits
statement: formalized
proof: formalized
---

# Int

`Batteries.Data.Int`, in [Batteries/Data/Int.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean), by François G. Dorais.

`Int.testBit` (definition, [line 19](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean#L19))

> `testBit m n` returns whether the `(n+1)` least significant bit is `1` or `0`, using the two's
> complement convention for negative `m`.

```lean
def testBit : Int → Nat → Bool
```

`Int.ofBits` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean#L29))

> Construct an integer from a sequence of bits using little endian convention.
>
> The sign is determined using the two's complement convention: the result is negative if and only if
> `n > 0` and `f (n-1) = true`.

```lean
def ofBits (f : Fin n → Bool)
```

`Int.ofBits_zero` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean#L35))

```lean
theorem ofBits_zero (f : Fin 0 → Bool) : ofBits f = 0
```

`Int.testBit_ofBits_lt` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean#L38))

```lean
theorem testBit_ofBits_lt {f : Fin n → Bool} (h : i < n) :
    (ofBits f).testBit i = f ⟨i, h⟩
```

`Int.testBit_ofBits_ge` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean#L46))

```lean
theorem testBit_ofBits_ge {f : Fin n → Bool} (h : i ≥ n) :
    (ofBits f).testBit i = decide (ofBits f < 0)
```

`Int.testBit_ofBits` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean#L57))

```lean
theorem testBit_ofBits (f : Fin n → Bool) :
    (ofBits f).testBit i = if h : i < n then f ⟨i, h⟩ else decide (ofBits f < 0)
```

## Depends on

- [Nat/Basic](nat/basic.md)

## Proof depends on

- [Basic lemmas about natural numbers](nat/lemmas.md)

## Sources

- [Batteries/Data/Int.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Int.lean)
