---
catalog: module
lean: Cedar.Thm.producesBool, Cedar.Thm.producesNonBool, Cedar.Thm.and_bool_operands_is_boolean_and, Cedar.Thm.left_false_implies_and_false, Cedar.Thm.left_bool_right_false_implies_and_false, Cedar.Thm.and_true_implies_left_true, Cedar.Thm.and_true_implies_right_true, Cedar.Thm.ways_and_can_error, Cedar.Thm.and_produces_bool_or_error, Cedar.Thm.policy_produces_bool_or_error, Cedar.Thm.record_produces_record_value, Cedar.Thm.record_value_contains_evaluated_attrs, Cedar.Thm.mapM'_asEntityUID_eq_entities
statement: formalized
proof: formalized
---

# Authorization/Evaluator

`Cedar.Thm.Authorization.Evaluator`, in [Cedar/Thm/Authorization/Evaluator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean).

> This file contains useful lemmas about the `Evaluator` functions.

`Cedar.Thm.producesBool` (definition, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L40))

> `producesBool` means the expression evaluates to a bool (and not an error)

```lean
def producesBool (e : Expr) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.producesNonBool` (definition, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L47))

> `producesNonBool` means the expression evaluates to a non-bool (and not an error)

```lean
def producesNonBool (e : Expr) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.and_bool_operands_is_boolean_and` (theorem, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L53))

```lean
theorem and_bool_operands_is_boolean_and {b₁ b₂ : Bool} {e₁ e₂ : Expr} {request : Request} {entities : Entities} :
  evaluate e₁ request entities = .ok b₁ →
  evaluate e₂ request entities = .ok b₂ →
  evaluate (Expr.and e₁ e₂) request entities = .ok (b₁ && b₂)
```

`Cedar.Thm.left_false_implies_and_false` (theorem, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L68))

```lean
theorem left_false_implies_and_false {e₁ e₂ : Expr} {request : Request} {entities : Entities} :
  evaluate e₁ request entities = .ok false →
  evaluate (Expr.and e₁ e₂) request entities = .ok false
```

`Cedar.Thm.left_bool_right_false_implies_and_false` (theorem, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L75))

```lean
theorem left_bool_right_false_implies_and_false {e₁ e₂ : Expr} {request : Request} {entities : Entities} :
  producesBool e₁ request entities →
  evaluate e₂ request entities = .ok false →
  evaluate (Expr.and e₁ e₂) request entities = .ok false
```

`Cedar.Thm.and_true_implies_left_true` (theorem, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L87))

```lean
theorem and_true_implies_left_true {e₁ e₂ : Expr} {request : Request} {entities : Entities} :
  evaluate (Expr.and e₁ e₂) request entities = .ok true →
  evaluate e₁ request entities = .ok true
```

`Cedar.Thm.and_true_implies_right_true` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L108))

```lean
theorem and_true_implies_right_true {e₁ e₂ : Expr} {request : Request} {entities : Entities} :
  evaluate (Expr.and e₁ e₂) request entities = .ok true →
  evaluate e₂ request entities = .ok true
```

`Cedar.Thm.ways_and_can_error` (theorem, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L138))

> If an `and` expression results in an error, it's because either:
> - the left subexpression had that error
> - the right subexpression had that error (and the left subexpression evaluated to .ok true)
> - the left subexpression evaluated to .ok with a non-bool
> - the right subexpression evaluated to .ok with a non-bool (and the left subexpression evaluated to .ok true)

```lean
theorem ways_and_can_error {e₁ e₂ : Expr} {request : Request} {entities : Entities} {err : Error} :
  evaluate (Expr.and e₁ e₂) request entities = .error err →
  evaluate e₁ request entities = .error err ∨
  (evaluate e₁ request entities = .ok true ∧ evaluate e₂ request entities = .error err) ∨
  (err = Error.typeError ∧ producesNonBool e₁ request entities) ∨
  (err = Error.typeError ∧ evaluate e₁ request entities = .ok true ∧ producesNonBool e₂ request entities)
```

`Cedar.Thm.and_produces_bool_or_error` (theorem, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L180))

> Every `and` expression produces either .ok bool or .error

```lean
theorem and_produces_bool_or_error (e₁ e₂ : Expr) (request : Request) (entities : Entities) :
  match (evaluate (Expr.and e₁ e₂) request entities) with
  | .ok (.prim (.bool _)) => true
  | .error _ => true
  | _ => false
```

`Cedar.Thm.policy_produces_bool_or_error` (theorem, [line 215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L215))

> Corollary of the above:
> Evaluating a policy produces either .ok bool or .error

```lean
theorem policy_produces_bool_or_error (p : Policy) (request : Request) (entities : Entities) :
  match (evaluate p.toExpr request entities) with
  | .ok (.prim (.bool _)) => true
  | .error _ => true
  | _ => false
```

`Cedar.Thm.record_produces_record_value` (theorem, [line 227](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L227))

> If evaluating a record produces a value, then it always produces a record value.

```lean
theorem record_produces_record_value {rxs : List (Attr × Expr)} {v : Value} {request : Request} {entities : Entities}
  (he : evaluate (.record rxs) request entities = .ok v) :
  ∃ rvs, .record rvs = v
```

`Cedar.Thm.record_value_contains_evaluated_attrs` (theorem, [line 241](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L241))

> If evaluating a record produces a record value containing an attribute, then
> that attribute existed in the original record, and corresponding expression
> evaluates to the same value.

```lean
theorem record_value_contains_evaluated_attrs {rxs : List (Attr × Expr)} {rvs : Map Attr Value} {a : Attr} {av : Value} {request : Request} {entities : Entities}
  (he : evaluate (.record rxs) request entities = .ok (.record rvs))
  (hfv : rvs.find? a = some av) :
  ∃ x, (Map.make rxs).find? a = some x ∧ evaluate x request entities = .ok av
```

`Cedar.Thm.mapM'_asEntityUID_eq_entities` (theorem, [line 276](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean#L276))

```lean
theorem mapM'_asEntityUID_eq_entities {vs : List Value} {euids : List EntityUID}
  (h₁ : List.mapM' Value.asEntityUID vs = Except.ok euids) :
  vs = List.map (Value.prim ∘ Prim.entityUID) euids
```

## Depends on

- [Spec/Evaluator](../../spec/evaluator.md)
- [Spec/Policy](../../spec/policy.md)

## Proof depends on

- [Map properties](../data/map.md)

## Sources

- [Cedar/Thm/Authorization/Evaluator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Evaluator.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Authorization.Evaluator.json)
