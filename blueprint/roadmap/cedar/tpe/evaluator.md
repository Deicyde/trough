---
catalog: module
lean: Cedar.TPE.Error, Cedar.TPE.someOrError, Cedar.TPE.someOrSelf, Cedar.TPE.varₚ, Cedar.TPE.ite, Cedar.TPE.and, Cedar.TPE.or, Cedar.TPE.tryDecideResidual₁, Cedar.TPE.apply₁, Cedar.TPE.inₑ, Cedar.TPE.inₛ, Cedar.TPE.hasTag, Cedar.TPE.getTag, Cedar.TPE.tryDecideResidual₂, Cedar.TPE.apply₂, Cedar.TPE.attrsOf, Cedar.TPE.tryDecideHasResidual, Cedar.TPE.hasAttr, Cedar.TPE.extHasAttr, Cedar.TPE.getAttr, Cedar.TPE.set, Cedar.TPE.record, Cedar.TPE.call, Cedar.TPE.evaluate, Cedar.TPE.evaluatePolicy
statement: formalized
proof: formalized
---

# TPE/Evaluator

`Cedar.TPE.Evaluator`, in [Cedar/TPE/Evaluator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean).

`Cedar.TPE.Error` (inductive type, [line 26](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L26))

```lean
inductive Error where
  | evaluation (err : Spec.Error)
  | invalidPolicy (err : TypeError)
  | invalidEnvironment
  | invalidRequestOrEntities
deriving Repr, Inhabited, DecidableEq
```

`Cedar.TPE.someOrError` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L37))

```lean
def someOrError : Option Value → CedarType → Residual
```

`Cedar.TPE.someOrSelf` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L42))

```lean
def someOrSelf : Option Value → CedarType → Residual → Residual
```

`Cedar.TPE.varₚ` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L46))

```lean
def varₚ (req : PartialRequest) (var : Var) (ty : CedarType) : Residual
```

`Cedar.TPE.ite` (definition, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L55))

```lean
def ite (c t e : Residual) (ty : CedarType) : Residual
```

`Cedar.TPE.and` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L61))

```lean
def and : Residual → Residual → CedarType → Residual
```

`Cedar.TPE.or` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L70))

```lean
def or : Residual → Residual → CedarType → Residual
```

`Cedar.TPE.tryDecideResidual₁` (definition, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L80))

```lean
def tryDecideResidual₁ (op₁ : UnaryOp) (r : Residual) : Option Value
```

`Cedar.TPE.apply₁` (definition, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L87))

```lean
def apply₁ (op₁ : UnaryOp) (r : Residual) (ty : CedarType) : Residual
```

`Cedar.TPE.inₑ` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L98))

```lean
def inₑ (uid₁ uid₂ : EntityUID) (es : PartialEntities) : Option Bool
```

`Cedar.TPE.inₛ` (definition, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L101))

```lean
def inₛ (uid : EntityUID) (vs : Set Value) (es : PartialEntities): Option Bool
```

`Cedar.TPE.hasTag` (definition, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L104))

```lean
def hasTag (uid : EntityUID) (tag : String) (es : PartialEntities) : Option Bool
```

`Cedar.TPE.getTag` (definition, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L107))

```lean
def getTag (uid : EntityUID) (tag : String) (es : PartialEntities) (ty : CedarType) : Residual
```

`Cedar.TPE.tryDecideResidual₂` (definition, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L113))

```lean
def tryDecideResidual₂ (env : TypeEnv) (op₂ : BinaryOp) (r₁ r₂ : Residual) : Option Value
```

`Cedar.TPE.apply₂` (definition, [line 123](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L123))

```lean
def apply₂ (env : TypeEnv) (op₂ : BinaryOp) (r₁ r₂ : Residual) (es : PartialEntities) (ty : CedarType) : Residual
```

`Cedar.TPE.attrsOf` (definition, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L173))

```lean
def attrsOf (r : Residual) (lookup : EntityUID → Option (Map Attr Value)) : Option (Map Attr Value)
```

`Cedar.TPE.tryDecideHasResidual` (definition, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L180))

```lean
def tryDecideHasResidual (env : TypeEnv) (r : Residual) (a : Attr) : Option Value
```

`Cedar.TPE.hasAttr` (definition, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L193))

```lean
def hasAttr (env : TypeEnv) (r : Residual) (a : Attr) (es : PartialEntities) (ty : CedarType) : Residual
```

`Cedar.TPE.extHasAttr` (definition, [line 205](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L205))

```lean
def extHasAttr (env : TypeEnv) (r : Residual) (a : Attr) (as : List Attr)
  (es : PartialEntities) (ty : CedarType) : Residual
```

`Cedar.TPE.getAttr` (definition, [line 234](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L234))

```lean
def getAttr (r : Residual) (a : Attr) (es : PartialEntities) (ty : CedarType) : Residual
```

`Cedar.TPE.set` (definition, [line 242](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L242))

```lean
def set (rs : List Residual) (ty : CedarType) : Residual
```

`Cedar.TPE.record` (definition, [line 247](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L247))

```lean
def record (m : List (Attr × Residual)) (ty : CedarType) : Residual
```

`Cedar.TPE.call` (definition, [line 252](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L252))

```lean
def call (xfn : ExtFun) (rs : List Residual) (ty : CedarType) : Residual
```

`Cedar.TPE.evaluate` (definition, [line 257](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L257))

```lean
def evaluate
  (env : TypeEnv)
  (x : Residual)
  (req : PartialRequest)
  (es : PartialEntities) : Residual
```

`Cedar.TPE.evaluatePolicy` (definition, [line 313](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean#L313))

> Partially evaluating a policy.
> Note that this function actually evaluates a type-lifted version of `TypedExpr`
> produced by the type checker, as opposed to evaluating the expression directly.
> This design is to simplify proofs otherwise we need to prove theorems that
> state type-lifting (i.e, `TypedExpr.liftBoolTypes`) do not change the results
> of evaluating residuals. The soundness theorem still holds. That is,
> reauthorizing the residuals produces the same outcome as authorizing the input
> expressions with consistent requests/entities. It is just that the types in the
> residuals are all lifted. We essentially trade efficiency for ease of proofs,
> which I (Shaobo) think is fine because the Lean model is a reference model not
> used in production.

```lean
def evaluatePolicy (schema : Schema)
  (p : Policy)
  (req : PartialRequest)
  (es : PartialEntities)
  : Except Error Residual
```

## Depends on

- [Cedar/TPE/Input](input.md)
- [TPE/Residual](residual.md)

## Sources

- [Cedar/TPE/Evaluator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Evaluator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.TPE.Evaluator.json)
