---
catalog: module
lean: Cedar.Spec.Error, Cedar.Spec.Result, Cedar.Spec.Id, Cedar.Spec.Name, Cedar.Spec.EntityType, Cedar.Spec.EntityUID, Cedar.Spec.Prim, Cedar.Spec.Attr, Cedar.Spec.Value, Cedar.Spec.Value.sizeOf_set', Cedar.Spec.Value.sizeOf_record', Cedar.Spec.Value.asEntityUID, Cedar.Spec.Value.asSet, Cedar.Spec.Value.asBool, Cedar.Spec.Value.asString, Cedar.Spec.Value.asInt, Cedar.Spec.Result.as, Cedar.Spec.decValue, Cedar.Spec.Name.lt, Cedar.Spec.Name.decLt, Cedar.Spec.EntityUID.lt, Cedar.Spec.EntityUID.decLt, Cedar.Spec.Prim.lt, Cedar.Spec.Prim.decLt, Cedar.Spec.Value.lt, Cedar.Spec.Values.lt, Cedar.Spec.ValueAttrs.lt, Cedar.Spec.Value.decLt
statement: formalized
proof: formalized
---

# Value

`Cedar.Spec.Value`, in [Cedar/Spec/Value.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean).

> This file defines Cedar values and results.

`Cedar.Spec.Error` (inductive type, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L30))

```lean
public inductive Error where
  | entityDoesNotExist
  | attrDoesNotExist
  | tagDoesNotExist
  | typeError
  | arithBoundsError
  | extensionError
```

`Cedar.Spec.Result` (abbreviation, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L38))

```lean
public abbrev Result (α)
```

`Cedar.Spec.Id` (abbreviation, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L40))

```lean
public abbrev Id
```

`Cedar.Spec.Name` (structure, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L42))

```lean
public structure Name where
  id : Id
  path : List Id
```

`Cedar.Spec.EntityType` (abbreviation, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L49))

```lean
public abbrev EntityType
```

`Cedar.Spec.EntityUID` (structure, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L54))

```lean
public structure EntityUID where
  ty : EntityType
  eid : String
```

`Cedar.Spec.Prim` (inductive type, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L61))

```lean
public inductive Prim where
  | bool (b : Bool)
  | int (i : Int64)
  | string (s : String)
  | entityUID (uid : EntityUID)
```

`Cedar.Spec.Attr` (abbreviation, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L67))

```lean
public abbrev Attr
```

`Cedar.Spec.Value` (inductive type, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L69))

```lean
public inductive Value where
  | prim (p : Prim)
  | set (s : Set Value)
  | record (m : Map Attr Value)
  | ext (x : Ext)
```

`Cedar.Spec.Value.sizeOf_set'` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L77))

```lean
public theorem Value.sizeOf_set' (s : Set Value) :
  sizeOf (Value.set s) = 1 + sizeOf s
```

`Cedar.Spec.Value.sizeOf_record'` (theorem, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L81))

```lean
public theorem Value.sizeOf_record' (m : Map Attr Value) :
  sizeOf (Value.record m) = 1 + sizeOf m
```

`Cedar.Spec.Value.asEntityUID` (definition, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L88))

```lean
public def Value.asEntityUID : Value → Result EntityUID
```

`Cedar.Spec.Value.asSet` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L93))

```lean
public def Value.asSet : Value → Result (Data.Set Value)
```

`Cedar.Spec.Value.asBool` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L98))

```lean
public def Value.asBool : Value → Result Bool
```

`Cedar.Spec.Value.asString` (definition, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L103))

```lean
public def Value.asString : Value →  Result String
```

`Cedar.Spec.Value.asInt` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L108))

```lean
public def Value.asInt : Value →  Result Int64
```

`Cedar.Spec.Result.as` (definition, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L113))

```lean
public def Result.as {α} (β) [Coe α (Result β)] : Result α → Result β
```

`Cedar.Spec.decValue` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L184))

```lean
public def decValue (v₁ v₂ : Value) : Decidable (v₁ = v₂)
```

`Cedar.Spec.Name.lt` (definition, [line 226](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L226))

```lean
public def Name.lt (a b : Name) : Bool
```

`Cedar.Spec.Name.decLt` (instance, [line 232](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L232))

```lean
public instance Name.decLt (a b : Name) : Decidable (a < b)
```

`Cedar.Spec.EntityUID.lt` (definition, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L235))

```lean
public def EntityUID.lt (a b : EntityUID) : Bool
```

`Cedar.Spec.EntityUID.decLt` (instance, [line 241](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L241))

```lean
public instance EntityUID.decLt (a b : EntityUID) : Decidable (a < b)
```

`Cedar.Spec.Prim.lt` (definition, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L244))

```lean
public def Prim.lt : Prim → Prim → Bool
```

`Cedar.Spec.Prim.decLt` (instance, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L260))

```lean
public instance Prim.decLt (a b : Prim) : Decidable (a < b)
```

`Cedar.Spec.Value.lt` (definition, [line 264](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L264))

```lean
public def Value.lt : Value → Value → Bool
```

`Cedar.Spec.Values.lt` (definition, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L283))

```lean
public def Values.lt : List Value → List Value → Bool
```

`Cedar.Spec.ValueAttrs.lt` (definition, [line 290](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L290))

```lean
public def ValueAttrs.lt : List (Attr × Value) → List (Attr × Value) → Bool
```

`Cedar.Spec.Value.decLt` (instance, [line 303](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean#L303))

```lean
public instance Value.decLt (a b : Value) : Decidable (a < b)
```

## Depends on

- [Map](../data/map.md)
- [Ext](ext.md)

## Sources

- [Cedar/Spec/Value.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Value.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Value.json)
