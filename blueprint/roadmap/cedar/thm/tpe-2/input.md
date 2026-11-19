---
catalog: module
lean: Cedar.Thm.decide_eq_implies_eq, Cedar.Thm.PartialIsValid, Cedar.Thm.PartialIsValid.some_inv, Cedar.Thm.partial_is_valid_rfl, Cedar.Thm.RequestRefines, Cedar.Thm.EntitiesRefine, Cedar.Thm.RequestAndEntitiesRefine, Cedar.Thm.validatePartialRequest_ok_environment?, Cedar.Thm.entitiesIsConsistent_implies_refines, Cedar.Thm.requestIsConsistent_implies_refines, Cedar.Thm.consistent_checks_ensure_refinement
statement: formalized
proof: formalized
---

# Thm/TPE/Input

`Cedar.Thm.TPE.Input`, in [Cedar/Thm/TPE/Input.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean).

> This file defines theorems related to the inputs of TPE.

`Cedar.Thm.decide_eq_implies_eq` (theorem, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L33))

```lean
theorem decide_eq_implies_eq {α} [DecidableEq α] {y : α} :
  ∀ x, decide (x = y) → x = y
```

`Cedar.Thm.PartialIsValid` (inductive type, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L37))

```lean
inductive PartialIsValid {α} (p : α → Prop) (o : Option α) : Prop
  | some (x : α) (heq : o = .some x) (h : p x) :
    PartialIsValid p o
  | none (heq : o = .none) :
    PartialIsValid p o
```

`Cedar.Thm.PartialIsValid.some_inv` (theorem, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L44))

```lean
theorem PartialIsValid.some_inv {p : α → Prop} {x : α} :  (PartialIsValid p (.some x)) ↔ p x
```

`Cedar.Thm.partial_is_valid_rfl` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L52))

```lean
theorem partial_is_valid_rfl {f : α → Bool} {p : α → Prop} {o : Option α} :
  (∀ x, f x = true → p x) → partialIsValid o f → PartialIsValid p o
```

`Cedar.Thm.RequestRefines` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L62))

```lean
def RequestRefines (req : Request) (preq : PartialRequest) : Prop
```

`Cedar.Thm.EntitiesRefine` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L70))

```lean
def EntitiesRefine (es : Entities) (pes : PartialEntities) : Prop
```

`Cedar.Thm.RequestAndEntitiesRefine` (definition, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L79))

> Concrete request `req` and entities `es` refine their partial counterparts
> `peq` and `pes`.

```lean
def RequestAndEntitiesRefine (req : Request) (es : Entities) (preq : PartialRequest) (pes : PartialEntities) : Prop
```

`Cedar.Thm.validatePartialRequest_ok_environment?` (theorem, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L82))

```lean
theorem validatePartialRequest_ok_environment? {schema : Schema} {req : PartialRequest} {env : TypeEnv} :
  validatePartialRequest schema req = .ok env →
  schema.environment? req.principal.ty req.resource.ty req.action = .some env
```

`Cedar.Thm.entitiesIsConsistent_implies_refines` (theorem, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L95))

```lean
theorem entitiesIsConsistent_implies_refines {es : Entities} {pes : PartialEntities} :
  entitiesIsConsistent es pes → EntitiesRefine es pes
```

`Cedar.Thm.requestIsConsistent_implies_refines` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L112))

```lean
theorem requestIsConsistent_implies_refines {req : Request} {preq : PartialRequest} :
  requestIsConsistent req preq →
  RequestRefines req preq
```

`Cedar.Thm.consistent_checks_ensure_refinement` (theorem, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean#L128))

> Requests and entities that pass `isValidAndConsistent` satisfy `RequestAndEntitiesRefine`.

```lean
theorem consistent_checks_ensure_refinement {schema : Schema} {req : Request} {es : Entities} {preq : PartialRequest} {pes : PartialEntities} :
  isValidAndConsistent schema req es preq pes = .ok () → RequestAndEntitiesRefine req es preq pes
```

## Depends on

- [Cedar/TPE/Input](../../tpe/input.md)

## Sources

- [Cedar/Thm/TPE/Input.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Input.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.Input.json)
