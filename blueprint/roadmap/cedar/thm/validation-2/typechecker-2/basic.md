---
catalog: module
lean: Cedar.Thm.EvaluatesTo, Cedar.Thm.CapabilitiesInvariant, Cedar.Thm.GuardedCapabilitiesInvariant, Cedar.Thm.TypeOfIsSound, Cedar.Thm.empty_capabilities_invariant, Cedar.Thm.empty_guarded_capabilities_invariant, Cedar.Thm.capability_implies_record_attribute, Cedar.Thm.capability_implies_entity_attribute, Cedar.Thm.capability_union_invariant, Cedar.Thm.capability_intersection_invariant, Cedar.Thm.type_of_is_inhabited
statement: formalized
proof: formalized
---

# Typechecker/Basic

`Cedar.Thm.Validation.Typechecker.Basic`, in [Cedar/Thm/Validation/Typechecker/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean).

> This file contains useful definitions and lemmas about the `Typechecker` functions.

`Cedar.Thm.EvaluatesTo` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L61))

> The type soundness property says that if the typechecker assigns a type to an
> expression, then it must be the case that the expression `EvaluatesTo` a value
> of that type. The `EvaluatesTo` predicate covers the (obvious) case where
> evaluation has no errors, but it also allows for errors of type
> `entityDoesNotExist`, `extensionError`, and `arithBoundsError`.
>
> The typechecker cannot protect against these errors because they depend on
> runtime information (i.e., the entities passed into the authorization request,
> extension function applications on authorization-time data, and arithmetic
> overflow errors). All other errors (`attrDoesNotExist` and `typeError`) can be
> prevented statically.
>
> _Note_: Currently, `extensionError`s can also be ruled out at validation time
> because the only extension functions that can error are constructors, and all
> constructors are required to be applied to string literals, meaning that they
> can be fully evaluated during validation. This is not guaranteed to be the case
> in the future.
>
> …

```lean
def EvaluatesTo (e: Expr) (request : Request) (entities : Entities) (v : Value) : Prop
```

`Cedar.Thm.CapabilitiesInvariant` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L73))

> On input to the typechecking function, for any (e, .attr k) in the Capabilities,
> e is a record- or entity-typed expression that has attribute k.
> Similarly, for any (e, .tag k) in the Capabilities,
> e is an entity-typed expression that has tag k.

```lean
def CapabilitiesInvariant (c : Capabilities) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.GuardedCapabilitiesInvariant` (definition, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L81))

> The Capabilities output by the typechecking function will satisfy
> `CapabilitiesInvariant` provided that the input expression evaluates to true.

```lean
def GuardedCapabilitiesInvariant (e: Expr) (c: Capabilities) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.TypeOfIsSound` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L85))

```lean
def TypeOfIsSound (x₁ : Expr) : Prop
```

`Cedar.Thm.empty_capabilities_invariant` (theorem, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L95))

```lean
theorem empty_capabilities_invariant (request : Request) (entities : Entities) :
  CapabilitiesInvariant ∅ request entities
```

`Cedar.Thm.empty_guarded_capabilities_invariant` (theorem, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L102))

```lean
theorem empty_guarded_capabilities_invariant {e: Expr} {request : Request} {entities : Entities} :
  GuardedCapabilitiesInvariant e ∅ request entities
```

`Cedar.Thm.capability_implies_record_attribute` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L108))

```lean
theorem capability_implies_record_attribute {x₁ : Expr} {a : Attr} {c₁ : Capabilities} {request : Request} {entities : Entities} {r : Map Attr Value}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : evaluate x₁ request entities = Except.ok (Value.record r))
  (h₃ : (x₁, .attr a) ∈ c₁) :
  ∃ vₐ, r.find? a = some vₐ
```

`Cedar.Thm.capability_implies_entity_attribute` (theorem, [line 119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L119))

```lean
theorem capability_implies_entity_attribute {x₁ : Expr} {a : Attr} {c₁ : Capabilities} {request : Request} {entities : Entities} {uid: EntityUID} {d: EntityData}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : evaluate x₁ request entities = Except.ok (Value.prim (Prim.entityUID uid)))
  (h₃ : Map.find? entities uid = some d)
  (h₄ : (x₁, .attr a) ∈ c₁) :
  ∃ vₐ, d.attrs.find? a = some vₐ
```

`Cedar.Thm.capability_union_invariant` (theorem, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L131))

```lean
theorem capability_union_invariant {c₁ c₂ : Capabilities} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : CapabilitiesInvariant c₂ request entities) :
  CapabilitiesInvariant (c₁ ∪ c₂) request entities
```

`Cedar.Thm.capability_intersection_invariant` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L149))

```lean
theorem capability_intersection_invariant {c₁ c₂ : Capabilities} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities ∨ CapabilitiesInvariant c₂ request entities) :
  CapabilitiesInvariant (c₁ ∩ c₂) request entities
```

`Cedar.Thm.type_of_is_inhabited` (theorem, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean#L178))

> A variant of `type_is_inhabited` assuming instead
> that the type is the result of `typeOf`.

```lean
theorem type_of_is_inhabited
  {e : Expr}
  {c₁ c₂ : Capabilities}
  {env : TypeEnv}
  {tx : TypedExpr}
  (hwf : env.WellFormed)
  (hty : typeOf e c₁ env = .ok (tx, c₂)) :
  ∃ v, InstanceOfType env v tx.typeOf
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [Typechecker/Types](types.md)

## Proof depends on

- [Expr/WF](../../welltyped/expr-2/wf.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Basic.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.Basic.json)
