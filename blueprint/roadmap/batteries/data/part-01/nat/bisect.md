---
catalog: module
lean: Nat.avg, Nat.avg_comm, Nat.avg_le_left, Nat.avg_le_right, Nat.avg_lt_left, Nat.avg_lt_right, Nat.le_avg_left, Nat.le_avg_right, Nat.le_add_one_of_avg_eq_left, Nat.le_add_one_of_avg_eq_right, Nat.bisect, Nat.bisect_lt_stop, Nat.start_le_bisect, Nat.bisect_true, Nat.bisect_add_one_false
statement: formalized
proof: formalized
---

# Bisect

`Batteries.Data.Nat.Bisect`, in [Batteries/Data/Nat/Bisect.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean), by François G. Dorais.

`Nat.avg` (abbreviation, [line 15](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L15))

> Average of two natural numbers rounded toward zero.

```lean
abbrev avg (a b : Nat)
```

`Nat.avg_comm` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L17))

```lean
theorem avg_comm (a b : Nat) : avg a b = avg b a
```

`Nat.avg_le_left` (theorem, [line 20](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L20))

```lean
theorem avg_le_left (h : b ≤ a) : avg a b ≤ a
```

`Nat.avg_le_right` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L23))

```lean
theorem avg_le_right (h : a ≤ b) : avg a b ≤ b
```

`Nat.avg_lt_left` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L26))

```lean
theorem avg_lt_left (h : b < a) : avg a b < a
```

`Nat.avg_lt_right` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L29))

```lean
theorem avg_lt_right (h : a < b) : avg a b < b
```

`Nat.le_avg_left` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L32))

```lean
theorem le_avg_left (h : a ≤ b) : a ≤ avg a b
```

`Nat.le_avg_right` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L35))

```lean
theorem le_avg_right (h : b ≤ a) : b ≤ avg a b
```

`Nat.le_add_one_of_avg_eq_left` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L38))

```lean
theorem le_add_one_of_avg_eq_left (h : avg a b = a) : b ≤ a + 1
```

`Nat.le_add_one_of_avg_eq_right` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L47))

```lean
theorem le_add_one_of_avg_eq_right (h : avg a b = b) : a ≤ b + 1
```

`Nat.bisect` (definition, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L60))

> Given natural numbers `a < b` such that `p a = true` and `p b = false`, `bisect` finds a natural
> number `a ≤ c < b` such that `p c = true` and `p (c+1) = false`.

```lean
def bisect {p : Nat → Bool} (h : start < stop) (hstart : p start = true) (hstop : p stop = false)
```

`Nat.bisect_lt_stop` (theorem, [line 71](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L71))

```lean
theorem bisect_lt_stop {p : Nat → Bool} (h : start < stop) (hstart : p start = true)
    (hstop : p stop = false) : bisect h hstart hstop < stop
```

`Nat.start_le_bisect` (theorem, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L87))

```lean
theorem start_le_bisect {p : Nat → Bool} (h : start < stop) (hstart : p start = true)
    (hstop : p stop = false) : start ≤ bisect h hstart hstop
```

`Nat.bisect_true` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L104))

```lean
theorem bisect_true {p : Nat → Bool} (h : start < stop) (hstart : p start = true)
    (hstop : p stop = false) : p (bisect h hstart hstop) = true
```

`Nat.bisect_add_one_false` (theorem, [line 121](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean#L121))

```lean
theorem bisect_add_one_false {p : Nat → Bool} (h : start < stop) (hstart : p start = true)
    (hstop : p stop = false) : p (bisect h hstart hstop + 1) = false
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Nat/Bisect.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Nat/Bisect.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Nat.Bisect.json)
