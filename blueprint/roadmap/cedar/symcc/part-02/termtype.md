---
catalog: module
lean: Cedar.SymCC.TermPrimType, Cedar.SymCC.TermType, Cedar.SymCC.TermType.bool, Cedar.SymCC.TermType.bitvec, Cedar.SymCC.TermType.string, Cedar.SymCC.TermType.entity, Cedar.SymCC.TermType.ext, Cedar.SymCC.TermType.tagFor, Cedar.SymCC.TermType.isPrimType, Cedar.SymCC.TermType.isEntityType, Cedar.SymCC.TermType.isBitVecType, Cedar.SymCC.TermType.isRecordType, Cedar.SymCC.TermType.isOptionType, Cedar.SymCC.TermType.isOptionEntityType, Cedar.SymCC.TermType.ofType, Cedar.SymCC.TermType.ofRecordType, Cedar.SymCC.TermType.ofQualifiedType, Cedar.SymCC.TermType.hasDecEq, Cedar.SymCC.TermPrimType.mkName, Cedar.SymCC.TermType.mkName, Cedar.Validation.ExtType.lt, Cedar.Validation.ExtType.decLt, Cedar.SymCC.TermPrimType.lt, Cedar.SymCC.TermPrimType.decLt, Cedar.SymCC.TermType.lt, Cedar.SymCC.TermType.decLt
statement: formalized
proof: formalized
---

# TermType

`Cedar.SymCC.TermType`, in [Cedar/SymCC/TermType.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean).

> This file defines the types of Cedar Terms.  See `Term.lean` for the
> definition of the Term language.

`Cedar.SymCC.TermPrimType` (inductive type, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L35))

```lean
public inductive TermPrimType where
  | bool
  | bitvec (n : Nat)
  | string
  | entity (ety : EntityType)
  | ext (xty : ExtType)
```

`Cedar.SymCC.TermType` (inductive type, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L42))

```lean
public inductive TermType where
  | prim (pty : TermPrimType)
  | option (ty : TermType)
  | set (ty : TermType)
  | record (rty : Map Attr TermType)
```

`Cedar.SymCC.TermType.bool` (abbreviation, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L48))

```lean
public abbrev TermType.bool : TermType
```

`Cedar.SymCC.TermType.bitvec` (abbreviation, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L49))

```lean
public abbrev TermType.bitvec (n : Nat) : TermType
```

`Cedar.SymCC.TermType.string` (abbreviation, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L50))

```lean
public abbrev TermType.string : TermType
```

`Cedar.SymCC.TermType.entity` (abbreviation, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L51))

```lean
public abbrev TermType.entity (ety : EntityType) : TermType
```

`Cedar.SymCC.TermType.ext` (abbreviation, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L52))

```lean
public abbrev TermType.ext (xty : ExtType) : TermType
```

`Cedar.SymCC.TermType.tagFor` (abbreviation, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L54))

```lean
public abbrev TermType.tagFor (ety : EntityType) : TermType
```

`Cedar.SymCC.TermType.isPrimType` (definition, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L58))

```lean
public def TermType.isPrimType : TermType → Bool
```

`Cedar.SymCC.TermType.isEntityType` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L63))

```lean
public def TermType.isEntityType : TermType → Bool
```

`Cedar.SymCC.TermType.isBitVecType` (definition, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L68))

```lean
public def TermType.isBitVecType : TermType → Bool
```

`Cedar.SymCC.TermType.isRecordType` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L73))

```lean
public def TermType.isRecordType : TermType → Bool
```

`Cedar.SymCC.TermType.isOptionType` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L78))

```lean
public def TermType.isOptionType : TermType → Bool
```

`Cedar.SymCC.TermType.isOptionEntityType` (definition, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L83))

```lean
public def TermType.isOptionEntityType : TermType → Bool
```

`Cedar.SymCC.TermType.ofType` (definition, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L89))

```lean
public def TermType.ofType (ty : CedarType) : TermType
```

`Cedar.SymCC.TermType.ofRecordType` (definition, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L99))

```lean
public def TermType.ofRecordType : List (Attr × QualifiedType) → List (Attr × TermType)
```

`Cedar.SymCC.TermType.ofQualifiedType` (definition, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L103))

```lean
public def TermType.ofQualifiedType : QualifiedType → TermType
```

`Cedar.SymCC.TermType.hasDecEq` (definition, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L114))

```lean
public def TermType.hasDecEq (ty₁ ty₂ : TermType) : Decidable (ty₁ = ty₂)
```

`Cedar.SymCC.TermPrimType.mkName` (definition, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L146))

```lean
public def TermPrimType.mkName : TermPrimType → String
```

`Cedar.SymCC.TermType.mkName` (definition, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L153))

```lean
public def TermType.mkName : TermType → String
```

`Cedar.Validation.ExtType.lt` (definition, [line 162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L162))

```lean
public def ExtType.lt : ExtType → ExtType → Bool
```

`Cedar.Validation.ExtType.decLt` (instance, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L174))

```lean
public instance ExtType.decLt (x y : ExtType) : Decidable (x < y)
```

`Cedar.SymCC.TermPrimType.lt` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L184))

```lean
public def TermPrimType.lt : TermPrimType → TermPrimType → Bool
```

`Cedar.SymCC.TermPrimType.decLt` (instance, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L193))

```lean
public instance TermPrimType.decLt (x y : TermPrimType) : Decidable (x < y)
```

`Cedar.SymCC.TermType.lt` (definition, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L198))

```lean
public def TermType.lt : TermType → TermType → Bool
```

`Cedar.SymCC.TermType.decLt` (instance, [line 220](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean#L220))

```lean
public instance TermType.decLt (x y : TermType) : Decidable (x < y)
```

## Depends on

- [Data](../part-01/data.md)
- [Validation/Types](../../validation/types.md)

## Sources

- [Cedar/SymCC/TermType.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/TermType.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.TermType.json)
