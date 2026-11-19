---
catalog: module
lean: Cedar.Thm.SubstituteActionPreservesEvaluation, Cedar.Thm.substitute_action_preserves_evaluation_ite, Cedar.Thm.substitute_action_preserves_evaluation_getAttr, Cedar.Thm.substitute_action_preserves_evaluation_hasAttr, Cedar.Thm.substitute_action_preserves_evaluation_unaryApp, Cedar.Thm.substitute_action_preserves_evaluation_binaryApp, Cedar.Thm.substitute_action_preserves_evaluation_and, Cedar.Thm.substitute_action_preserves_evaluation_or, Cedar.Thm.substitute_action_nil_set, Cedar.Thm.substitute_action_cons_set, Cedar.Thm.substitute_action_preserves_evaluation_set, Cedar.Thm.substitute_action_nil_record, Cedar.Thm.substitute_action_cons_record, Cedar.Thm.substitute_action_preserves_evaluation_record, Cedar.Thm.substitute_action_nil_call, Cedar.Thm.substitute_action_cons_call, Cedar.Thm.substitute_action_preserves_evaluation_call, Cedar.Thm.substitute_action_preserves_evaluation, Cedar.Thm.substitute_action_preserves_evaluates_to
statement: formalized
proof: formalized
---

# SubstituteAction

`Cedar.Thm.Validation.SubstituteAction`, in [Cedar/Thm/Validation/SubstituteAction.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean).

`Cedar.Thm.SubstituteActionPreservesEvaluation` (definition, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L34))

```lean
def SubstituteActionPreservesEvaluation (expr : Expr) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.substitute_action_preserves_evaluation_ite` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L38))

```lean
theorem substitute_action_preserves_evaluation_ite {i t e : Expr} {request : Request} {entities : Entities}
  (ih₁ : SubstituteActionPreservesEvaluation i request entities)
  (ih₂ : SubstituteActionPreservesEvaluation t request entities)
  (ih₃ : SubstituteActionPreservesEvaluation e request entities) :
  evaluate (substituteAction request.action (Expr.ite i t e)) request entities =
  evaluate (Expr.ite i t e) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation_getAttr` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L48))

```lean
theorem substitute_action_preserves_evaluation_getAttr {e : Expr} {attr : Attr} {request : Request} {entities : Entities}
(ih₁ : SubstituteActionPreservesEvaluation e request entities) :
  evaluate (substituteAction request.action (Expr.getAttr e attr)) request entities =
  evaluate (Expr.getAttr e attr) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation_hasAttr` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L57))

```lean
theorem substitute_action_preserves_evaluation_hasAttr {e : Expr} {attr : Attr} {request : Request} {entities : Entities}
(ih₁ : SubstituteActionPreservesEvaluation e request entities) :
  evaluate (substituteAction request.action (Expr.hasAttr e attr)) request entities =
  evaluate (Expr.hasAttr e attr) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation_unaryApp` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L66))

```lean
theorem substitute_action_preserves_evaluation_unaryApp {op : UnaryOp} {e : Expr} {request : Request} {entities : Entities}
(ih₁ : SubstituteActionPreservesEvaluation e request entities) :
  evaluate (substituteAction request.action (Expr.unaryApp op e)) request entities =
  evaluate (Expr.unaryApp op e) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation_binaryApp` (theorem, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L75))

```lean
theorem substitute_action_preserves_evaluation_binaryApp {op : BinaryOp} {a b : Expr} {request : Request} {entities : Entities}
(ih₁ : SubstituteActionPreservesEvaluation a request entities)
(ih₂ : SubstituteActionPreservesEvaluation b request entities) :
  evaluate (substituteAction request.action (Expr.binaryApp op a b)) request entities =
  evaluate (Expr.binaryApp op a b) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation_and` (theorem, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L85))

```lean
theorem substitute_action_preserves_evaluation_and {a b : Expr} {request : Request} {entities : Entities}
(ih₁ : SubstituteActionPreservesEvaluation a request entities)
(ih₂ : SubstituteActionPreservesEvaluation b request entities) :
  evaluate (substituteAction request.action (Expr.and a b)) request entities =
  evaluate (Expr.and a b) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation_or` (theorem, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L94))

```lean
theorem substitute_action_preserves_evaluation_or {a b : Expr} {request : Request} {entities : Entities}
(ih₁ : SubstituteActionPreservesEvaluation a request entities)
(ih₂ : SubstituteActionPreservesEvaluation b request entities) :
  evaluate (substituteAction request.action (Expr.or a b)) request entities =
  evaluate (Expr.or a b) request entities
```

`Cedar.Thm.substitute_action_nil_set` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L103))

```lean
theorem substitute_action_nil_set : ∀ (uid : EntityUID),
  substituteAction uid (.set []) = .set []
```

`Cedar.Thm.substitute_action_cons_set` (theorem, [line 109](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L109))

```lean
theorem substitute_action_cons_set : ∀ (h : Expr) (t : List Expr) (uid : EntityUID),
  substituteAction uid (.set (h :: t)) = .set ((substituteAction uid h) :: t.map (substituteAction uid))
```

`Cedar.Thm.substitute_action_preserves_evaluation_set` (theorem, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L118))

```lean
theorem substitute_action_preserves_evaluation_set {xs : List Expr} {request : Request} {entities : Entities}
(ih₁ : ∀ xᵢ, xᵢ ∈ xs → SubstituteActionPreservesEvaluation xᵢ request entities) :
  evaluate (substituteAction request.action (Expr.set xs)) request entities =
  evaluate (Expr.set xs) request entities
```

`Cedar.Thm.substitute_action_nil_record` (theorem, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L141))

```lean
theorem substitute_action_nil_record : ∀ (uid : EntityUID),
  substituteAction uid (.record []) = .record []
```

`Cedar.Thm.substitute_action_cons_record` (theorem, [line 147](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L147))

```lean
theorem substitute_action_cons_record : ∀ (ax : Attr × Expr) (axs : List (Attr × Expr)) (uid : EntityUID),
  substituteAction uid (.record (ax :: axs)) =
  .record ((ax.fst, substituteAction uid ax.snd) :: axs.map (fun (a, e) => (a, substituteAction uid e)))
```

`Cedar.Thm.substitute_action_preserves_evaluation_record` (theorem, [line 154](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L154))

```lean
theorem substitute_action_preserves_evaluation_record {axs : List (Attr × Expr)} {request : Request} {entities : Entities}
(ih₁ : ∀ axᵢ, axᵢ ∈ axs → SubstituteActionPreservesEvaluation axᵢ.snd request entities) :
  evaluate (substituteAction request.action (Expr.record axs)) request entities =
  evaluate (Expr.record axs) request entities
```

`Cedar.Thm.substitute_action_nil_call` (theorem, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L186))

```lean
theorem substitute_action_nil_call : ∀ (uid : EntityUID) (xfn : ExtFun),
  substituteAction uid (.call xfn []) = .call xfn []
```

`Cedar.Thm.substitute_action_cons_call` (theorem, [line 192](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L192))

```lean
theorem substitute_action_cons_call : ∀ (x : Expr) (xs : List Expr) (uid : EntityUID) (xfn : ExtFun),
  substituteAction uid (.call xfn (x :: xs)) = .call xfn ((substituteAction uid x) :: xs.map (substituteAction uid))
```

`Cedar.Thm.substitute_action_preserves_evaluation_call` (theorem, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L202))

```lean
theorem substitute_action_preserves_evaluation_call {xfn : ExtFun} {xs : List Expr} {request : Request} {entities : Entities}
(ih₁ : ∀ xᵢ, xᵢ ∈ xs → SubstituteActionPreservesEvaluation xᵢ request entities) :
  evaluate (substituteAction request.action (Expr.call xfn xs)) request entities =
  evaluate (Expr.call xfn xs) request entities
```

`Cedar.Thm.substitute_action_preserves_evaluation` (theorem, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L225))

```lean
theorem substitute_action_preserves_evaluation (expr : Expr) (request : Request) (entities : Entities) :
  evaluate (substituteAction request.action expr) request entities =
  evaluate expr request entities
```

`Cedar.Thm.substitute_action_preserves_evaluates_to` (theorem, [line 284](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean#L284))

```lean
theorem substitute_action_preserves_evaluates_to {expr : Expr} {request : Request} {entities : Entities} {v : Value}:
  EvaluatesTo (substituteAction request.action expr) request entities v ↔
  EvaluatesTo expr request entities v
```

## Depends on

- [Typechecker/Basic](typechecker-2/basic.md)
- [Cedar/Validation/Validator](../../validation/validator.md)

## Proof depends on

- [Authorization/Evaluator](../authorization-2/evaluator.md)

## Sources

- [Cedar/Thm/Validation/SubstituteAction.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/SubstituteAction.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.SubstituteAction.json)
