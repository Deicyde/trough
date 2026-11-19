---
catalog: module
lean: Cedar.Validation.TypeError, Cedar.Validation.Key, Cedar.Validation.Capabilities, Cedar.Validation.Capabilities.singleton, Cedar.Validation.ResultType, Cedar.Validation.ResultType.typeOf, Cedar.Validation.ok, Cedar.Validation.err, Cedar.Validation.typeOfLit, Cedar.Validation.typeOfVar, Cedar.Validation.typeOfIf, Cedar.Validation.typeOfAnd, Cedar.Validation.typeOfOr, Cedar.Validation.typeOfUnaryApp, Cedar.Validation.typeOfEq, Cedar.Validation.entityUID?, Cedar.Validation.entityUIDs?, Cedar.Validation.actionUID?, Cedar.Validation.typeOfInₑ, Cedar.Validation.typeOfInₛ, Cedar.Validation.typeOfHasTag, Cedar.Validation.typeOfGetTag, Cedar.Validation.ifLubThenBool, Cedar.Validation.typeOfBinaryApp, Cedar.Validation.hasAttrInRecord, Cedar.Validation.typeOfHasAttr, Cedar.Validation.getAttrInRecord, Cedar.Validation.typeOfGetAttr, Cedar.Validation.typeOfExtHasAttrLoop, Cedar.Validation.typeOfExtHasAttr, Cedar.Validation.typeOfSet, Cedar.Validation.justType, Cedar.Validation.typeOfConstructor, Cedar.Validation.typeOfIsInRange, Cedar.Validation.typeOfCall, Cedar.Validation.typeOf
statement: formalized
proof: formalized
---

# Cedar/Validation/Typechecker

`Cedar.Validation.Typechecker`, in [Cedar/Validation/Typechecker.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean).

`Cedar.Validation.TypeError` (inductive type, [line 28](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L28))

```lean
public inductive TypeError where
  | lubErr (ty₁ : CedarType) (ty₂ : CedarType)
  | unexpectedType (ty : CedarType)
  | attrNotFound (ty : CedarType) (attr : Attr)
  | tagNotFound (ety : EntityType) (tag : Expr)
  | unknownEntity (ety : EntityType)
  | extensionErr (xs : List Expr)
  | emptySetErr
  | incompatibleSetTypes (ty : List CedarType)
deriving Repr, DecidableEq
```

`Cedar.Validation.Key` (inductive type, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L39))

```lean
public inductive Key where
  | attr (a : Attr)
  | tag (x : Expr)
deriving Repr, DecidableEq
```

`Cedar.Validation.Capabilities` (abbreviation, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L44))

```lean
public abbrev Capabilities
```

`Cedar.Validation.Capabilities.singleton` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L46))

```lean
public def Capabilities.singleton (e : Expr) (k : Key) : Capabilities
```

`Cedar.Validation.ResultType` (abbreviation, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L48))

```lean
public abbrev ResultType
```

`Cedar.Validation.ResultType.typeOf` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L50))

```lean
public def ResultType.typeOf : ResultType -> Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.ok` (definition, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L53))

```lean
public def ok {α : Type} (ty : α) (c : Capabilities := ∅) : Except TypeError (α × Capabilities)
```

`Cedar.Validation.err` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L54))

```lean
public def err {α : Type} (e : TypeError) : Except TypeError (α × Capabilities)
```

`Cedar.Validation.typeOfLit` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L56))

```lean
public def typeOfLit (p : Prim) (env : TypeEnv) : ResultType
```

`Cedar.Validation.typeOfVar` (definition, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L68))

```lean
public def typeOfVar (v : Var) (env : TypeEnv) : ResultType
```

`Cedar.Validation.typeOfIf` (definition, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L76))

```lean
public def typeOfIf (r₁ : TypedExpr × Capabilities) (r₂ r₃ : ResultType) : ResultType
```

`Cedar.Validation.typeOfAnd` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L93))

```lean
public def typeOfAnd (r₁ : TypedExpr × Capabilities) (r₂ : ResultType) : ResultType
```

`Cedar.Validation.typeOfOr` (definition, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L107))

```lean
public def typeOfOr (r₁ : TypedExpr × Capabilities) (r₂ : ResultType) : ResultType
```

`Cedar.Validation.typeOfUnaryApp` (definition, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L127))

```lean
public def typeOfUnaryApp (op : UnaryOp) (ty : TypedExpr) : ResultType
```

`Cedar.Validation.typeOfEq` (definition, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L137))

```lean
public def typeOfEq (ty₁ ty₂ : TypedExpr) (x₁ x₂ : Expr) : ResultType
```

`Cedar.Validation.entityUID?` (definition, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L149))

```lean
public def entityUID? : Expr → Option EntityUID
```

`Cedar.Validation.entityUIDs?` (definition, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L153))

```lean
public def entityUIDs? : Expr → Option (List EntityUID)
```

`Cedar.Validation.actionUID?` (definition, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L157))

```lean
public def actionUID? (x : Expr) (acts: ActionSchema) : Option EntityUID
```

`Cedar.Validation.typeOfInₑ` (definition, [line 162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L162))

```lean
public def typeOfInₑ (ety₁ ety₂ : EntityType) (x₁ x₂ : Expr) (env : TypeEnv) : BoolType
```

`Cedar.Validation.typeOfInₛ` (definition, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L174))

```lean
public def typeOfInₛ (ety₁ ety₂ : EntityType) (x₁ x₂ : Expr) (env : TypeEnv) : BoolType
```

`Cedar.Validation.typeOfHasTag` (definition, [line 185](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L185))

```lean
public def typeOfHasTag (ety : EntityType) (x : Expr) (t : Expr) (c : Capabilities) (env : TypeEnv) : Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.typeOfGetTag` (definition, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L197))

```lean
public def typeOfGetTag (ety : EntityType) (x : Expr) (t : Expr) (c : Capabilities) (env : TypeEnv) : Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.ifLubThenBool` (definition, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L203))

```lean
public def ifLubThenBool (ty₁ ty₂ : CedarType) : Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.typeOfBinaryApp` (definition, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L208))

```lean
public def typeOfBinaryApp (op₂ : BinaryOp) (ty₁ ty₂ : TypedExpr) (x₁ x₂ : Expr) (c : Capabilities) (env : TypeEnv) : ResultType
```

`Cedar.Validation.hasAttrInRecord` (definition, [line 240](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L240))

```lean
public def hasAttrInRecord (rty : RecordType) (x : Expr) (a : Attr) (c : Capabilities) (knownToExist : Bool) : Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.typeOfHasAttr` (definition, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L248))

```lean
public def typeOfHasAttr (ty : TypedExpr) (x : Expr) (a : Attr) (c : Capabilities) (env : TypeEnv) : ResultType
```

`Cedar.Validation.getAttrInRecord` (definition, [line 265](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L265))

```lean
public def getAttrInRecord (ty : CedarType) (rty : RecordType) (x : Expr) (a : Attr) (c : Capabilities) : Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.typeOfGetAttr` (definition, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L271))

```lean
public def typeOfGetAttr (ty : TypedExpr) (x : Expr) (a : Attr) (c : Capabilities) (env : TypeEnv) : ResultType
```

`Cedar.Validation.typeOfExtHasAttrLoop` (definition, [line 285](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L285))

```lean
public def typeOfExtHasAttrLoop (curTy : TypedExpr) (curExpr : Expr) (prevAttr : Attr)
    (acc : Capabilities) (c : Capabilities) (env : TypeEnv) :
    List Attr → Except TypeError (TypedExpr × Expr × Attr × Capabilities)
```

`Cedar.Validation.typeOfExtHasAttr` (definition, [line 295](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L295))

```lean
public def typeOfExtHasAttr (ty₁ : TypedExpr) (x₁ : Expr) (attrs : List Attr)
    (c : Capabilities) (env : TypeEnv) : Except TypeError (BoolType × Capabilities)
```

`Cedar.Validation.typeOfSet` (definition, [line 328](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L328))

```lean
public def typeOfSet (tys : List TypedExpr) : ResultType
```

`Cedar.Validation.justType` (definition, [line 337](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L337))

```lean
public def justType (r : ResultType) : Except TypeError TypedExpr
```

`Cedar.Validation.typeOfConstructor` (definition, [line 340](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L340))

```lean
public def typeOfConstructor (mk : String → Option α) (xs : List Expr) (ty : CedarType) : Except TypeError (CedarType × Capabilities)
```

`Cedar.Validation.typeOfIsInRange` (definition, [line 348](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L348))

```lean
public def typeOfIsInRange (tys : List TypedExpr) (xs : List Expr) : ResultType
```

`Cedar.Validation.typeOfCall` (definition, [line 356](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L356))

```lean
public def typeOfCall (xfn : ExtFun) (tys : List TypedExpr) (xs : List Expr) : ResultType
```

`Cedar.Validation.typeOf` (definition, [line 395](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean#L395))

```lean
public def typeOf (x : Expr) (c : Capabilities) (env : TypeEnv) : ResultType
```

## Depends on

- [Subtyping](subtyping.md)
- [TypedExpr](typedexpr.md)

## Sources

- [Cedar/Validation/Typechecker.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Typechecker.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.Typechecker.json)
