---
catalog: module
lean: Char.not_isLower_of_isUpper, Char.not_isUpper_of_isLower, Char.toLower_eq_of_not_isUpper, Char.toLower_eq_of_isUpper, Char.toUpper_eq_of_not_isLower, Char.toUpper_eq_of_isLower, Char.isUpper_toLower_eq_false, Char.isLower_toUpper_eq_false, Char.isLower_toLower_eq_isAlpha, Char.isUpper_toUpper_eq_isAlpha, Char.isAlpha_toLower_eq_isAlpha, Char.isAlpha_toUpper_eq_isAlpha, Char.toLower_toLower_eq_toLower, Char.toLower_toUpper_eq_toLower, Char.toUpper_toUpper_eq_toUpper, Char.toUpper_toLower_eq_toUpper, Char.caseFoldAsciiOnly, Char.beqCaseInsensitiveAsciiOnly, Char.beqCaseInsensitiveAsciiOnly.eqv, Char.beqCaseInsensitiveAsciiOnly.isSetoid, Char.cmpCaseInsensitiveAsciiOnly
statement: formalized
proof: formalized
---

# Lemmas for ASCII-casing

`Batteries.Data.Char.AsciiCasing`, in [Batteries/Data/Char/AsciiCasing.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean), by François G. Dorais.

> These facts apply for ASCII characters only. Recall that `isAlpha`, `isLower`, `isUpper`, `toLower`,
> `toUpper` do not consider characters outside the ASCII character range (code points less than 128).

`Char.not_isLower_of_isUpper` (theorem, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L20))

```lean
theorem not_isLower_of_isUpper {c : Char} : c.isUpper → ¬ c.isLower
```

`Char.not_isUpper_of_isLower` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L24))

```lean
theorem not_isUpper_of_isLower {c : Char} : c.isLower → ¬ c.isUpper
```

`Char.toLower_eq_of_not_isUpper` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L29))

```lean
theorem toLower_eq_of_not_isUpper {c : Char} (h : ¬ c.isUpper) : c.toLower = c
```

`Char.toLower_eq_of_isUpper` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L33))

```lean
theorem toLower_eq_of_isUpper {c : Char} (h : c.isUpper) : c.toLower = ofNat (c.toNat + 32)
```

`Char.toUpper_eq_of_not_isLower` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L39))

```lean
theorem toUpper_eq_of_not_isLower {c : Char} (h : ¬ c.isLower) : c.toUpper = c
```

`Char.toUpper_eq_of_isLower` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L43))

```lean
theorem toUpper_eq_of_isLower {c : Char} (h : c.isLower) : c.toUpper = ofNat (c.toNat - 32)
```

`Char.isUpper_toLower_eq_false` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L50))

```lean
theorem isUpper_toLower_eq_false (c : Char) : c.toLower.isUpper = false
```

`Char.isLower_toUpper_eq_false` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L54))

```lean
theorem isLower_toUpper_eq_false (c : Char) : c.toUpper.isLower = false
```

`Char.isLower_toLower_eq_isAlpha` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L58))

```lean
theorem isLower_toLower_eq_isAlpha (c : Char) : c.toLower.isLower = c.isAlpha
```

`Char.isUpper_toUpper_eq_isAlpha` (theorem, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L70))

```lean
theorem isUpper_toUpper_eq_isAlpha (c : Char) : c.toUpper.isUpper = c.isAlpha
```

`Char.isAlpha_toLower_eq_isAlpha` (theorem, [line 83](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L83))

```lean
theorem isAlpha_toLower_eq_isAlpha (c : Char) : c.toLower.isAlpha = c.isAlpha
```

`Char.isAlpha_toUpper_eq_isAlpha` (theorem, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L86))

```lean
theorem isAlpha_toUpper_eq_isAlpha (c : Char) : c.toUpper.isAlpha = c.isAlpha
```

`Char.toLower_toLower_eq_toLower` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L89))

```lean
theorem toLower_toLower_eq_toLower (c : Char) : c.toLower.toLower = c.toLower
```

`Char.toLower_toUpper_eq_toLower` (theorem, [line 92](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L92))

```lean
theorem toLower_toUpper_eq_toLower (c : Char) : c.toUpper.toLower = c.toLower
```

`Char.toUpper_toUpper_eq_toUpper` (theorem, [line 108](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L108))

```lean
theorem toUpper_toUpper_eq_toUpper (c : Char) : c.toUpper.toUpper = c.toUpper
```

`Char.toUpper_toLower_eq_toUpper` (theorem, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L111))

```lean
theorem toUpper_toLower_eq_toUpper (c : Char) : c.toLower.toUpper = c.toUpper
```

`Char.caseFoldAsciiOnly` (abbreviation, [line 137](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L137))

> Case folding for ASCII characters only.
>
> Alphabetic ASCII characters are mapped to their lowercase form, all other characters are left
> unchanged. This agrees with the Unicode case folding algorithm for ASCII characters.
>
> ```
> #eval caseFoldAsciiOnly 'A' == 'a'
> #eval caseFoldAsciiOnly 'a' == 'a'
> #eval caseFoldAsciiOnly 'À' == 'À'
> #eval caseFoldAsciiOnly 'à' == 'à'
> #eval caseFoldAsciiOnly '$' == '$'
> ```

```lean
abbrev caseFoldAsciiOnly
```

`Char.beqCaseInsensitiveAsciiOnly` (definition, [line 151](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L151))

> Bool-valued comparison of two `Char`s for *ASCII*-case insensitive equality.
>
> ```
> #eval beqCaseInsensitiveAsciiOnly 'a' 'A' -- true
> #eval beqCaseInsensitiveAsciiOnly 'a' 'a' -- true
> #eval beqCaseInsensitiveAsciiOnly '$' '$' -- true
> #eval beqCaseInsensitiveAsciiOnly 'a' 'b' -- false
> #eval beqCaseInsensitiveAsciiOnly 'γ' 'Γ' -- false
> #eval beqCaseInsensitiveAsciiOnly 'ä' 'Ä' -- false
> ```

```lean
def beqCaseInsensitiveAsciiOnly (c₁ c₂ : Char) : Bool
```

`Char.beqCaseInsensitiveAsciiOnly.eqv` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L154))

```lean
theorem beqCaseInsensitiveAsciiOnly.eqv : Equivalence (beqCaseInsensitiveAsciiOnly · ·)
```

`Char.beqCaseInsensitiveAsciiOnly.isSetoid` (definition, [line 163](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L163))

> Setoid structure on `Char` using `beqCaseInsensitiveAsciiOnly`

```lean
def beqCaseInsensitiveAsciiOnly.isSetoid : Setoid Char
```

`Char.cmpCaseInsensitiveAsciiOnly` (definition, [line 178](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean#L178))

> ASCII-case insensitive implementation comparison returning an `Ordering`. Useful for sorting.
>
> ```
> #eval cmpCaseInsensitiveAsciiOnly 'a' 'A' -- eq
> #eval cmpCaseInsensitiveAsciiOnly 'a' 'a' -- eq
> #eval cmpCaseInsensitiveAsciiOnly '$' '$' -- eq
> #eval cmpCaseInsensitiveAsciiOnly 'a' 'b' -- lt
> #eval cmpCaseInsensitiveAsciiOnly 'γ' 'Γ' -- gt
> #eval cmpCaseInsensitiveAsciiOnly 'ä' 'Ä' -- gt
> ```

```lean
def cmpCaseInsensitiveAsciiOnly (c₁ c₂ : Char) : Ordering
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [Char/Basic](basic.md)

## Sources

- [Batteries/Data/Char/AsciiCasing.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Char/AsciiCasing.lean)
