---
catalog: module
lean: Char.le_antisymm_iff, Char.toNat_ofNatAux, Char.toNat_ofNat, Char.val_ofNat, Char.ofNat_toNat_eq_val, Char.max, Char.maxSurrogate, Char.minSurrogate, Char.count, Char.toNat_le_max, Char.toNat_not_surrogate, Char.isAscii, Char.isAscii_iff_toNat_lt, Char.isAscii_of_isUpper, Char.isAscii_of_isLower, Char.isAscii_of_isAlpha, Char.isAscii_of_isDigit, Char.isAscii_of_isAlphanum, Char.isAscii_of_isWhitespace, Char.all, Char.eq_true_of_all_eq_true, Char.exists_eq_false_of_all_eq_false, Char.all_eq_true_iff_forall_eq_true, Char.any, Char.exists_eq_true_of_any_eq_true, Char.eq_false_of_any_eq_false, Char.any_eq_true_iff_exists_eq_true
statement: formalized
proof: formalized
---

# Char/Basic

`Batteries.Data.Char.Basic`, in [Batteries/Data/Char/Basic.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean), by Jannis Limperg, François G. Dorais.

`Char.le_antisymm_iff` (theorem, [line 14](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L14))

```lean
theorem le_antisymm_iff {x y : Char} : x = y ↔ x ≤ y ∧ y ≤ x
```

`Char.toNat_ofNatAux` (theorem, [line 21](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L21))

```lean
theorem toNat_ofNatAux {n : Nat} (h : n.isValidChar) : toNat (ofNatAux n h) = n
```

`Char.toNat_ofNat` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L24))

```lean
theorem toNat_ofNat (n : Nat) : toNat (ofNat n) = if n.isValidChar then n else 0
```

`Char.val_ofNat` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L30))

```lean
theorem val_ofNat (hn : Nat.isValidChar n) : (ofNat n).val = UInt32.ofNat n
```

`Char.ofNat_toNat_eq_val` (theorem, [line 34](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L34))

```lean
theorem ofNat_toNat_eq_val {c : Char} : UInt32.ofNat c.toNat = c.val
```

`Char.max` (abbreviation, [line 41](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L41))

> Maximum character code point.
> (See [unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value).)

```lean
protected abbrev max
```

`Char.maxSurrogate` (abbreviation, [line 47](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L47))

> Maximum surrogate code point.
> (See [unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value).)

```lean
protected abbrev maxSurrogate
```

`Char.minSurrogate` (abbreviation, [line 53](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L53))

> Minimum surrogate code point.
> (See [unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value).)

```lean
protected abbrev minSurrogate
```

`Char.count` (abbreviation, [line 59](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L59))

> Number of valid character code points.
> (See [unicode scalar value](https://www.unicode.org/glossary/#unicode_scalar_value).)

```lean
protected abbrev count
```

`Char.toNat_le_max` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L61))

```lean
theorem toNat_le_max (c : Char) : c.toNat ≤ Char.max
```

`Char.toNat_not_surrogate` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L66))

```lean
theorem toNat_not_surrogate (c : Char) :
    ¬(Char.minSurrogate ≤ c.toNat ∧ c.toNat ≤ Char.maxSurrogate)
```

`Char.isAscii` (definition, [line 73](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L73))

> Checks whether a character is in the ASCII range, that is, its code point is less than 128.

```lean
def isAscii (c : Char) : Bool
```

`Char.isAscii_iff_toNat_lt` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L75))

```lean
theorem isAscii_iff_toNat_lt {c : Char} : c.isAscii ↔ c.toNat < 128
```

`Char.isAscii_of_isUpper` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L78))

```lean
theorem isAscii_of_isUpper {c : Char} (h : c.isUpper) : c.isAscii
```

`Char.isAscii_of_isLower` (theorem, [line 82](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L82))

```lean
theorem isAscii_of_isLower {c : Char} (h : c.isLower) : c.isAscii
```

`Char.isAscii_of_isAlpha` (theorem, [line 86](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L86))

```lean
theorem isAscii_of_isAlpha {c : Char} (h : c.isAlpha) : c.isAscii
```

`Char.isAscii_of_isDigit` (theorem, [line 90](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L90))

```lean
theorem isAscii_of_isDigit {c : Char} (h : c.isDigit) : c.isAscii
```

`Char.isAscii_of_isAlphanum` (theorem, [line 94](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L94))

```lean
theorem isAscii_of_isAlphanum {c : Char} (h : c.isAlphanum) : c.isAscii
```

`Char.isAscii_of_isWhitespace` (theorem, [line 98](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L98))

```lean
theorem isAscii_of_isWhitespace {c : Char} (h : c.isWhitespace) : c.isAscii
```

`Char.all` (definition, [line 103](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L103))

> Returns `true` if `p` returns true for every `Char`.

```lean
protected def all (p : Char → Bool) : Bool
```

`Char.eq_true_of_all_eq_true` (theorem, [line 119](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L119))

```lean
theorem eq_true_of_all_eq_true (h : Char.all p) (c : Char) : p c
```

`Char.exists_eq_false_of_all_eq_false` (theorem, [line 124](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L124))

```lean
theorem exists_eq_false_of_all_eq_false (h : Char.all p = false) :
    ∃ c, p c = false
```

`Char.all_eq_true_iff_forall_eq_true` (theorem, [line 132](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L132))

```lean
theorem all_eq_true_iff_forall_eq_true : Char.all p = true ↔ ∀ c, p c = true
```

`Char.any` (definition, [line 142](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L142))

> Returns `true` if `p` returns true for some `Char`.

```lean
protected def any (p : Char → Bool) : Bool
```

`Char.exists_eq_true_of_any_eq_true` (theorem, [line 147](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L147))

```lean
theorem exists_eq_true_of_any_eq_true (h : Char.any p = true) : ∃ c, p c = true
```

`Char.eq_false_of_any_eq_false` (theorem, [line 165](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L165))

```lean
theorem eq_false_of_any_eq_false (h : Char.any p = false) (c : Char) : p c = false
```

`Char.any_eq_true_iff_exists_eq_true` (theorem, [line 170](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean#L170))

```lean
theorem any_eq_true_iff_exists_eq_true : Char.any p = true ↔ ∃ c, p c = true
```

## Depends on

- [Order](../../../classes/order.md)

## Sources

- [Batteries/Data/Char/Basic.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Char/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Char.Basic.json)
