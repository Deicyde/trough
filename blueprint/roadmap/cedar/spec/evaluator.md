---
catalog: module
lean: Cedar.Spec.intOrErr, Cedar.Spec.apply₁, Cedar.Spec.inₑ, Cedar.Spec.inₛ, Cedar.Spec.hasTag, Cedar.Spec.getTag, Cedar.Spec.apply₂, Cedar.Spec.attrsOf, Cedar.Spec.hasAttr, Cedar.Spec.getAttr, Cedar.Spec.hasAttrs, Cedar.Spec.bindAttr, Cedar.Spec.evaluate
statement: formalized
proof: formalized
---

# Spec/Evaluator

`Cedar.Spec.Evaluator`, in [Cedar/Spec/Evaluator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean).

> This file defines the semantics of Cedar operators and expressions.

`Cedar.Spec.intOrErr` (definition, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L34))

```lean
public def intOrErr : Option Int64 → Result Value
```

`Cedar.Spec.apply₁` (definition, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L38))

```lean
public def apply₁ : UnaryOp → Value → Result Value
```

`Cedar.Spec.inₑ` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L46))

```lean
public def inₑ (uid₁ uid₂ : EntityUID) (es : Entities) : Bool
```

`Cedar.Spec.inₛ` (definition, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L49))

```lean
public def inₛ (uid : EntityUID) (vs : Set Value) (es : Entities) : Result Value
```

`Cedar.Spec.hasTag` (definition, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L53))

```lean
public def hasTag (uid : EntityUID) (tag : String) (es : Entities) : Result Value
```

`Cedar.Spec.getTag` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L56))

```lean
public def getTag (uid : EntityUID) (tag : String) (es : Entities) : Result Value
```

`Cedar.Spec.apply₂` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L59))

```lean
public def apply₂ (op₂ : BinaryOp) (v₁ v₂ : Value) (es : Entities) : Result Value
```

`Cedar.Spec.attrsOf` (definition, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L80))

```lean
public def attrsOf (v : Value) (lookup : EntityUID → Result (Map Attr Value)) : Result (Map Attr Value)
```

`Cedar.Spec.hasAttr` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L86))

```lean
public def hasAttr (v : Value) (a : Attr) (es : Entities) : Result Value
```

`Cedar.Spec.getAttr` (definition, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L90))

```lean
public def getAttr (v : Value) (a : Attr) (es : Entities) : Result Value
```

`Cedar.Spec.hasAttrs` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L94))

```lean
public def hasAttrs (v : Value) (a : Attr) (as : List Attr) (es : Entities) : Result Value
```

`Cedar.Spec.bindAttr` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L108))

```lean
public def bindAttr [Monad m] (a : Attr) (res : m α) : m (Attr × α)
```

`Cedar.Spec.evaluate` (definition, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean#L112))

```lean
public def evaluate (x : Expr) (req : Request) (es : Entities) : Result Value
```

## Depends on

- [Entities](entities.md)
- [Spec/Expr](expr.md)
- [Request](request.md)

## Sources

- [Cedar/Spec/Evaluator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Evaluator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Evaluator.json)
