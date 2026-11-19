---
catalog: module
lean: UInt8.ext, UInt8.toUInt16_toNat, UInt8.toUInt32_toNat, UInt8.toUInt64_toNat, UInt8.le_iff_toNat_le_toNat, UInt8.lt_iff_toNat_lt_toNat, UInt8.compare_eq_toNat_compare_toNat, UInt8.toNat_max, UInt8.toNat_min, UInt16.ext, UInt16.toUInt8_toNat, UInt16.toUInt32_toNat, UInt16.toUInt64_toNat, UInt16.le_iff_toNat_le_toNat, UInt16.lt_iff_toNat_lt_toNat, UInt16.compare_eq_toNat_compare_toNat, UInt16.toNat_max, UInt16.toNat_min, UInt32.ext, UInt32.toUInt8_toNat, UInt32.toUInt16_toNat, UInt32.toUInt64_toNat, UInt32.le_iff_toNat_le_toNat, UInt32.lt_iff_toNat_lt_toNat, UInt32.compare_eq_toNat_compare_toNat, UInt32.toNat_max, UInt32.toNat_min, UInt64.ext, UInt64.toUInt8_toNat, UInt64.toUInt16_toNat, UInt64.toUInt32_toNat, UInt64.le_iff_toNat_le_toNat, UInt64.lt_iff_toNat_lt_toNat, UInt64.compare_eq_toNat_compare_toNat, UInt64.toNat_max, UInt64.toNat_min, USize.ext, USize.toUInt64_toNat, UInt32.toUSize_toNat, USize.toNat_ofNat_of_le_of_lt, USize.pred_toNat
statement: formalized
proof: formalized
---

# UInt

`Batteries.Data.UInt`, in [Batteries/Data/UInt.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean), by François G. Dorais, Mario Carneiro.

> ### UInt8

`UInt8.ext` (theorem, [line 14](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L14))

```lean
theorem UInt8.ext : {x y : UInt8} → x.toNat = y.toNat → x = y
```

`UInt8.toUInt16_toNat` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L17))

```lean
theorem UInt8.toUInt16_toNat (x : UInt8) : x.toUInt16.toNat = x.toNat
```

`UInt8.toUInt32_toNat` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L19))

```lean
theorem UInt8.toUInt32_toNat (x : UInt8) : x.toUInt32.toNat = x.toNat
```

`UInt8.toUInt64_toNat` (theorem, [line 21](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L21))

```lean
theorem UInt8.toUInt64_toNat (x : UInt8) : x.toUInt64.toNat = x.toNat
```

`UInt8.le_iff_toNat_le_toNat` (theorem, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L27))

```lean
theorem UInt8.le_iff_toNat_le_toNat {x y : UInt8} : x ≤ y ↔ x.toNat ≤ y.toNat
```

`UInt8.lt_iff_toNat_lt_toNat` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L29))

```lean
theorem UInt8.lt_iff_toNat_lt_toNat {x y : UInt8} : x < y ↔ x.toNat < y.toNat
```

`UInt8.compare_eq_toNat_compare_toNat` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L31))

```lean
theorem UInt8.compare_eq_toNat_compare_toNat (x y : UInt8) :
    compare x y = compare x.toNat y.toNat
```

`UInt8.toNat_max` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L35))

```lean
theorem UInt8.toNat_max (x y : UInt8) : (max x y).toNat = max x.toNat y.toNat
```

`UInt8.toNat_min` (theorem, [line 45](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L45))

```lean
theorem UInt8.toNat_min (x y : UInt8) : (min x y).toNat = min x.toNat y.toNat
```

> ### UInt16

`UInt16.ext` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L57))

```lean
theorem UInt16.ext : {x y : UInt16} → x.toNat = y.toNat → x = y
```

`UInt16.toUInt8_toNat` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L60))

```lean
theorem UInt16.toUInt8_toNat (x : UInt16) : x.toUInt8.toNat = x.toNat % 2 ^ 8
```

`UInt16.toUInt32_toNat` (theorem, [line 62](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L62))

```lean
theorem UInt16.toUInt32_toNat (x : UInt16) : x.toUInt32.toNat = x.toNat
```

`UInt16.toUInt64_toNat` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L64))

```lean
theorem UInt16.toUInt64_toNat (x : UInt16) : x.toUInt64.toNat = x.toNat
```

`UInt16.le_iff_toNat_le_toNat` (theorem, [line 70](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L70))

```lean
theorem UInt16.le_iff_toNat_le_toNat {x y : UInt16} : x ≤ y ↔ x.toNat ≤ y.toNat
```

`UInt16.lt_iff_toNat_lt_toNat` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L72))

```lean
theorem UInt16.lt_iff_toNat_lt_toNat {x y : UInt16} : x < y ↔ x.toNat < y.toNat
```

`UInt16.compare_eq_toNat_compare_toNat` (theorem, [line 74](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L74))

```lean
theorem UInt16.compare_eq_toNat_compare_toNat (x y : UInt16) :
    compare x y = compare x.toNat y.toNat
```

`UInt16.toNat_max` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L78))

```lean
theorem UInt16.toNat_max (x y : UInt16) : (max x y).toNat = max x.toNat y.toNat
```

`UInt16.toNat_min` (theorem, [line 88](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L88))

```lean
theorem UInt16.toNat_min (x y : UInt16) : (min x y).toNat = min x.toNat y.toNat
```

> ### UInt32

`UInt32.ext` (theorem, [line 100](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L100))

```lean
theorem UInt32.ext : {x y : UInt32} → x.toNat = y.toNat → x = y
```

`UInt32.toUInt8_toNat` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L103))

```lean
theorem UInt32.toUInt8_toNat (x : UInt32) : x.toUInt8.toNat = x.toNat % 2 ^ 8
```

`UInt32.toUInt16_toNat` (theorem, [line 105](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L105))

```lean
theorem UInt32.toUInt16_toNat (x : UInt32) : x.toUInt16.toNat = x.toNat % 2 ^ 16
```

`UInt32.toUInt64_toNat` (theorem, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L107))

```lean
theorem UInt32.toUInt64_toNat (x : UInt32) : x.toUInt64.toNat = x.toNat
```

`UInt32.le_iff_toNat_le_toNat` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L113))

```lean
theorem UInt32.le_iff_toNat_le_toNat {x y : UInt32} : x ≤ y ↔ x.toNat ≤ y.toNat
```

`UInt32.lt_iff_toNat_lt_toNat` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L115))

```lean
theorem UInt32.lt_iff_toNat_lt_toNat {x y : UInt32} : x < y ↔ x.toNat < y.toNat
```

`UInt32.compare_eq_toNat_compare_toNat` (theorem, [line 117](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L117))

```lean
theorem UInt32.compare_eq_toNat_compare_toNat (x y : UInt32) :
    compare x y = compare x.toNat y.toNat
```

`UInt32.toNat_max` (theorem, [line 121](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L121))

```lean
theorem UInt32.toNat_max (x y : UInt32) : (max x y).toNat = max x.toNat y.toNat
```

`UInt32.toNat_min` (theorem, [line 131](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L131))

```lean
theorem UInt32.toNat_min (x y : UInt32) : (min x y).toNat = min x.toNat y.toNat
```

> ### UInt64

`UInt64.ext` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L143))

```lean
theorem UInt64.ext : {x y : UInt64} → x.toNat = y.toNat → x = y
```

`UInt64.toUInt8_toNat` (theorem, [line 146](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L146))

```lean
theorem UInt64.toUInt8_toNat (x : UInt64) : x.toUInt8.toNat = x.toNat % 2 ^ 8
```

`UInt64.toUInt16_toNat` (theorem, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L148))

```lean
theorem UInt64.toUInt16_toNat (x : UInt64) : x.toUInt16.toNat = x.toNat % 2 ^ 16
```

`UInt64.toUInt32_toNat` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L150))

```lean
theorem UInt64.toUInt32_toNat (x : UInt64) : x.toUInt32.toNat = x.toNat % 2 ^ 32
```

`UInt64.le_iff_toNat_le_toNat` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L156))

```lean
theorem UInt64.le_iff_toNat_le_toNat {x y : UInt64} : x ≤ y ↔ x.toNat ≤ y.toNat
```

`UInt64.lt_iff_toNat_lt_toNat` (theorem, [line 158](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L158))

```lean
theorem UInt64.lt_iff_toNat_lt_toNat {x y : UInt64} : x < y ↔ x.toNat < y.toNat
```

`UInt64.compare_eq_toNat_compare_toNat` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L160))

```lean
theorem UInt64.compare_eq_toNat_compare_toNat (x y : UInt64) :
    compare x y = compare x.toNat y.toNat
```

`UInt64.toNat_max` (theorem, [line 164](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L164))

```lean
theorem UInt64.toNat_max (x y : UInt64) : (max x y).toNat = max x.toNat y.toNat
```

`UInt64.toNat_min` (theorem, [line 174](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L174))

```lean
theorem UInt64.toNat_min (x y : UInt64) : (min x y).toNat = min x.toNat y.toNat
```

> ### USize

`USize.ext` (theorem, [line 186](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L186))

```lean
theorem USize.ext : {x y : USize} → x.toNat = y.toNat → x = y
```

`USize.toUInt64_toNat` (theorem, [line 189](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L189))

```lean
theorem USize.toUInt64_toNat (x : USize) : x.toUInt64.toNat = x.toNat
```

`UInt32.toUSize_toNat` (theorem, [line 191](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L191))

```lean
theorem UInt32.toUSize_toNat (x : UInt32) : x.toUSize.toNat = x.toNat
```

`USize.toNat_ofNat_of_le_of_lt` (theorem, [line 197](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L197))

```lean
theorem USize.toNat_ofNat_of_le_of_lt (h : n < USize.size) (hn : i ≤ n) :
    (USize.ofNat i).toNat = i
```

`USize.pred_toNat` (theorem, [line 201](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean#L201))

```lean
theorem USize.pred_toNat {i : USize} (h_gt : 0 < i) :
    (i - 1).toNat = i.toNat - 1
```

## Depends on

- [Order](../../classes/order.md)

## Sources

- [Batteries/Data/UInt.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/UInt.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.UInt.json)
