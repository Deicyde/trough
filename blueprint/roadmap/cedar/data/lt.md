---
catalog: module
lean: Cedar.Data.StrictLT, Cedar.Data.StrictLT.irreflexive, Cedar.Data.StrictLT.if_not_lt_gt_then_eq, Cedar.Data.StrictLT.if_not_lt_eq_then_gt, Cedar.Data.StrictLT.not_eq, List.cons_lt_cons, List.slt_irrefl, List.slt_trans, List.slt_asymm, List.lt_conn, List.strictLT, Bool.lt, Bool.decLt, Bool.strictLT, Nat.strictLT, Int.strictLT, UInt32.strictLT, Char.strictLT, String.strictLT
statement: formalized
proof: formalized
---

# Cedar/Data/LT

`Cedar.Data.LT`, in [Cedar/Data/LT.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean).

> This file contains utilities for working with strict and decidable LT relations.

`Cedar.Data.StrictLT` (class, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L30))

```lean
public class StrictLT (α) [LT α] : Prop where
  asymmetric : ∀ (a b : α), a < b → ¬ b < a
  transitive : ∀ (a b c : α), a < b → b < c → a < c
  connected  : ∀ (a b : α), a ≠ b → (a < b ∨ b < a)
```

`Cedar.Data.StrictLT.irreflexive` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L35))

```lean
public theorem StrictLT.irreflexive [LT α] [StrictLT α] (x : α) :
  ¬ x < x
```

`Cedar.Data.StrictLT.if_not_lt_gt_then_eq` (theorem, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L42))

```lean
public theorem StrictLT.if_not_lt_gt_then_eq [LT α] [StrictLT α] (x y : α) :
  ¬ x < y → ¬ y < x → x = y
```

`Cedar.Data.StrictLT.if_not_lt_eq_then_gt` (theorem, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L50))

```lean
public theorem StrictLT.if_not_lt_eq_then_gt [LT α] [StrictLT α] (x y : α) :
  ¬ x < y → ¬ x = y → x > y
```

`Cedar.Data.StrictLT.not_eq` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L58))

```lean
public theorem StrictLT.not_eq [LT α] [StrictLT α] (x y : α) :
  x < y → ¬ x = y
```

`List.cons_lt_cons` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L80))

```lean
public theorem List.cons_lt_cons [LT α] [StrictLT α] (x : α) (xs ys : List α) :
  xs < ys → x :: xs < x :: ys
```

`List.slt_irrefl` (theorem, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L87))

```lean
public theorem List.slt_irrefl [LT α] [StrictLT α] [DecidableLT α] (xs : List α) :
  ¬ xs < xs
```

`List.slt_trans` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L98))

```lean
public theorem List.slt_trans [LT α] [StrictLT α] {xs ys zs : List α} :
  xs < ys → ys < zs → xs < zs
```

`List.slt_asymm` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L117))

```lean
public theorem List.slt_asymm [LT α] [StrictLT α] [DecidableLT α] {xs ys : List α} :
  xs < ys → ¬ ys < xs
```

`List.lt_conn` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L134))

```lean
public theorem List.lt_conn [LT α] [StrictLT α] {xs ys : List α} :
  xs ≠ ys → (xs < ys ∨ ys < xs)
```

`List.strictLT` (instance, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L173))

```lean
public instance List.strictLT (α) [LT α] [StrictLT α] [DecidableLT α] : StrictLT (List α)
```

`Bool.lt` (definition, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L178))

```lean
public def Bool.lt (a b : Bool) : Bool
```

`Bool.decLt` (instance, [line 185](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L185))

```lean
public instance Bool.decLt (a b : Bool) : Decidable (a < b)
```

`Bool.strictLT` (instance, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L188))

```lean
public instance Bool.strictLT : StrictLT Bool
```

`Nat.strictLT` (instance, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L203))

```lean
public instance Nat.strictLT : StrictLT Nat
```

`Int.strictLT` (instance, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L208))

```lean
public instance Int.strictLT : StrictLT Int
```

`UInt32.strictLT` (instance, [line 213](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L213))

```lean
public instance UInt32.strictLT : StrictLT UInt32
```

`Char.strictLT` (instance, [line 221](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L221))

```lean
public instance Char.strictLT : StrictLT Char
```

`String.strictLT` (instance, [line 231](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean#L231))

```lean
public instance String.strictLT : StrictLT String
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Data/LT.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Data/LT.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Data.LT.json)
