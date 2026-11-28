---
catalog: module
lean: Nat.and_self_left, Nat.and_self_right, Nat.and_left_comm, Nat.and_right_comm, Nat.or_self_left, Nat.or_self_right, Nat.or_left_comm, Nat.or_right_comm, Nat.xor_left_comm, Nat.xor_right_comm, Nat.xor_xor_cancel_left, Nat.xor_xor_cancel_right, Nat.eq_of_xor_eq_zero, Nat.xor_eq_zero_iff, Nat.xor_ne_zero_iff, Nat.xor_right_injective, Nat.xor_left_injective, Nat.xor_right_inj, Nat.xor_left_inj, Nat.and_or_right_injective, Nat.and_or_right_inj, Nat.and_or_left_injective, Nat.and_or_left_inj
statement: formalized
proof: formalized
---

# Bitwise Lemmas

`Batteries.Data.Nat.Bitwise.Lemmas`, in [Batteries/Data/Nat/Bitwise/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean), by François G. Dorais.

> This module defines properties of the bitwise operations on natural numbers.
>
> This file is complements `Init.Data.Nat.Bitwise.Lemmas` with properties that
> are not necessary for the bitvector library.

> ### and

`Nat.and_self_left` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L23))

```lean
theorem and_self_left (a b : Nat) : a &&& (a &&& b) = a &&& b
```

`Nat.and_self_right` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L26))

```lean
theorem and_self_right (a b : Nat) : ((a &&& b) &&& b) = (a &&& b)
```

`Nat.and_left_comm` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L29))

```lean
theorem and_left_comm (x y z : Nat) : x &&& (y &&& z) = y &&& (x &&& z)
```

`Nat.and_right_comm` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L32))

```lean
theorem and_right_comm (x y z : Nat) : (x &&& y) &&& z = (x &&& z) &&& y
```

> ### or

`Nat.or_self_left` (theorem, [line 37](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L37))

```lean
theorem or_self_left (a b : Nat) : a ||| (a ||| b) = a ||| b
```

`Nat.or_self_right` (theorem, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L40))

```lean
theorem or_self_right (a b : Nat) : (a ||| b) ||| b = a ||| b
```

`Nat.or_left_comm` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L43))

```lean
theorem or_left_comm (x y z : Nat) : x ||| (y ||| z) = y ||| (x ||| z)
```

`Nat.or_right_comm` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L46))

```lean
theorem or_right_comm (x y z : Nat) : (x ||| y) ||| z = (x ||| z) ||| y
```

> ### xor

`Nat.xor_left_comm` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L51))

```lean
theorem xor_left_comm (x y z : Nat) : x ^^^ (y ^^^ z) = y ^^^ (x ^^^ z)
```

`Nat.xor_right_comm` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L54))

```lean
theorem xor_right_comm (x y z : Nat) : (x ^^^ y) ^^^ z = (x ^^^ z) ^^^ y
```

`Nat.xor_xor_cancel_left` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L57))

```lean
theorem xor_xor_cancel_left (x y : Nat) : x ^^^ (x ^^^ y) = y
```

`Nat.xor_xor_cancel_right` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L60))

```lean
theorem xor_xor_cancel_right (x y : Nat) : (x ^^^ y) ^^^ y = x
```

`Nat.eq_of_xor_eq_zero` (theorem, [line 63](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L63))

```lean
theorem eq_of_xor_eq_zero {x y : Nat} : x ^^^ y = 0 → x = y
```

`Nat.xor_eq_zero_iff` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L66))

```lean
theorem xor_eq_zero_iff {x y : Nat} : x ^^^ y = 0 ↔ x = y
```

`Nat.xor_ne_zero_iff` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L69))

```lean
theorem xor_ne_zero_iff {x y : Nat} : x ^^^ y ≠ 0 ↔ x ≠ y
```

> ### injectivity lemmas

`Nat.xor_right_injective` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L73))

```lean
theorem xor_right_injective {x : Nat} : Function.Injective (x ^^^ ·)
```

`Nat.xor_left_injective` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L76))

```lean
theorem xor_left_injective {x : Nat} : Function.Injective (· ^^^ x)
```

`Nat.xor_right_inj` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L79))

```lean
theorem xor_right_inj {x y z : Nat} : x ^^^ y = x ^^^ z ↔ y = z
```

`Nat.xor_left_inj` (theorem, [line 82](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L82))

```lean
theorem xor_left_inj {x y z : Nat} : x ^^^ z = y ^^^ z ↔ x = y
```

`Nat.and_or_right_injective` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L85))

```lean
theorem and_or_right_injective {m x y : Nat} : x &&& m = y &&& m → x ||| m = y ||| m → x = y
```

`Nat.and_or_right_inj` (theorem, [line 92](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L92))

```lean
theorem and_or_right_inj {m x y : Nat} : x &&& m = y &&& m ∧ x ||| m = y ||| m ↔ x = y
```

`Nat.and_or_left_injective` (theorem, [line 95](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L95))

```lean
theorem and_or_left_injective {m x y : Nat} : m &&& x = m &&& y → m ||| x = m ||| y → x = y
```

`Nat.and_or_left_inj` (theorem, [line 102](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean#L102))

```lean
theorem and_or_left_inj {m x y : Nat} : m &&& x = m &&& y ∧ m ||| x = m ||| y ↔ x = y
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Nat/Bitwise/Lemmas.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bitwise/Lemmas.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.Nat.Bitwise.Lemmas.json)
