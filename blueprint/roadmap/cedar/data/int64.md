---
catalog: module
lean: Int64.MIN, Int64.MAX, Int64.ofIntChecked, Int64.ofInt?, Int64.ofInt?_some_iff, Int64.ofInt?_none_iff, Int64.add?, Int64.sub?, Int64.mul?, Int64.neg?, Int64.natAbs, Int64.smod, Int64.smod_result_nonneg, Int64.toInt_smod, Int64.ofInt?_toInt, Int64.ofInt?_some_toInt, Int64.toInt_nonneg_of_ge_zero, Int64.toInt_neg_of_not_ge_zero, Int64.lt_def_toInt, Int64.le_def_toInt, Int64.strictLT
statement: formalized
proof: formalized
---

# Int64

`Cedar.Data.Int64`, in [Cedar/Data/Int64.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean).

> This file defines a signed 64-bit integer datatype similar to Rust's `i64`
> by adding checked arithmetic operations to Lean's Int64 datatype.

`Int64.MIN` (definition, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L29))

```lean
public def MIN : Int
```

`Int64.MAX` (definition, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L31))

```lean
public def MAX : Int
```

`Int64.ofIntChecked` (definition, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L36))

```lean
public def ofIntChecked (i : Int) (_ : MIN ≤ i ∧ i ≤ MAX) : Int64
```

`Int64.ofInt?` (definition, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L39))

```lean
public def ofInt? (i : Int) : Option Int64
```

`Int64.ofInt?_some_iff` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L46))

> We don't @[expose] the definition of `ofInt?`; but callers can use this
> theorem, which specifies its behavior

```lean
public theorem ofInt?_some_iff {i : Int} :
  MIN ≤ i ∧ i ≤ MAX ↔ (ofInt? i) = some (Int64.ofInt i)
```

`Int64.ofInt?_none_iff` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L51))

> Inverse of the above

```lean
public theorem ofInt?_none_iff {i : Int} :
  i < MIN ∨ i > MAX ↔ (ofInt? i) = none
```

`Int64.add?` (definition, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L55))

```lean
public def add? (i₁ i₂ : Int64) : Option Int64
```

`Int64.sub?` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L57))

```lean
public def sub? (i₁ i₂ : Int64) : Option Int64
```

`Int64.mul?` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L59))

```lean
public def mul? (i₁ i₂ : Int64) : Option Int64
```

`Int64.neg?` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L61))

```lean
public def neg? (i₁ : Int64) : Option Int64
```

`Int64.natAbs` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L63))

```lean
public def natAbs (i₁ : Int64) : Nat
```

`Int64.smod` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L70))

> A version of Int64.mod with the property that
>   b > 0 →
>   ∀ a, 0 <= smod a b < b

```lean
public def smod (a b : Int64) : Int64
```

`Int64.smod_result_nonneg` (theorem, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L76))

```lean
public theorem smod_result_nonneg {a b : Int64} :
  b > 0 →
  0 <= smod a b ∧ smod a b < b
```

`Int64.toInt_smod` (theorem, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L86))

```lean
public theorem toInt_smod (a b : Int64) : (smod a b).toInt = a.toInt.fmod b.toInt
```

`Int64.ofInt?_toInt` (theorem, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L89))

```lean
public theorem ofInt?_toInt (v : Int64) : ofInt? v.toInt = some v
```

`Int64.ofInt?_some_toInt` (theorem, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L101))

> `ofInt?` roundtrip: when it succeeds, coercing the result back to `Int` recovers the original
> value. This is the converse companion to `ofInt?_toInt`.

```lean
public theorem ofInt?_some_toInt {n : Int} {i : Int64} (h : ofInt? n = some i) : i.toInt = n
```

`Int64.toInt_nonneg_of_ge_zero` (theorem, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L111))

```lean
public theorem toInt_nonneg_of_ge_zero {v : Int64} (h : v ≥ 0) : v.toInt ≥ 0
```

`Int64.toInt_neg_of_not_ge_zero` (theorem, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L115))

```lean
public theorem toInt_neg_of_not_ge_zero {v : Int64} (h : ¬(v ≥ 0)) : v.toInt < 0
```

`Int64.lt_def_toInt` (theorem, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L131))

```lean
public theorem lt_def_toInt {i₁ i₂ : Int64} : i₁ < i₂ ↔ i₁.toInt < i₂.toInt
```

`Int64.le_def_toInt` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L134))

```lean
public theorem le_def_toInt {i₁ i₂ : Int64} : i₁ ≤ i₂ ↔ i₁.toInt ≤ i₂.toInt
```

`Int64.strictLT` (instance, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean#L139))

```lean
public instance strictLT : Cedar.Data.StrictLT Int64
```

## Depends on

- [Cedar/Data/LT](lt.md)

## Sources

- [Cedar/Data/Int64.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/Int64.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Data.Int64.json)
