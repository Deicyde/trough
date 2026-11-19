---
catalog: module
lean: Cedar.Thm.type_of_mem_inversion, Cedar.Thm.entityUID?_some_implies_entity_lit, Cedar.Thm.actionUID?_some_implies_action_lit, Cedar.Thm.entityUIDs?_some_implies_entity_lits, Cedar.Thm.acts_maybeDescendentOf_false_implies_not_ancestor_type, Cedar.Thm.entity_type_in_false_implies_inₑ_false, Cedar.Thm.action_type_in_eq_action_inₑ, Cedar.Thm.type_of_mem_is_soundₑ, Cedar.Thm.entity_set_type_implies_set_of_entities, Cedar.Thm.entity_type_in_false_implies_inₛ_false, Cedar.Thm.mapM'_eval_lits_eq_prims, Cedar.Thm.evaluate_entity_set_eqv, Cedar.Thm.action_type_in_eq_action_inₛ, Cedar.Thm.type_of_mem_is_soundₛ, Cedar.Thm.type_of_mem_is_sound
statement: formalized
proof: formalized
---

# Mem

`Cedar.Thm.Validation.Typechecker.BinaryApp.Mem`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean).

> This file proves that typechecking of `.binaryApp .mem` expressions is sound.

`Cedar.Thm.type_of_mem_inversion` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L40))

```lean
theorem type_of_mem_inversion {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.binaryApp .mem x₁ x₂) c env = Except.ok (ty, c')) :
  c' = ∅ ∧
  ∃ (ety₁ ety₂ : EntityType),
    (∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.entity ety₁, c₁)) ∧
    (∃ c₂,
      ((typeOf x₂ c env).typeOf = Except.ok (.entity ety₂, c₂) ∧
       ty.typeOf = .bool (typeOfInₑ ety₁ ety₂ x₁ x₂ env)) ∨
      ((typeOf x₂ c env).typeOf = Except.ok (.set (.entity ety₂), c₂) ∧
       ty.typeOf = .bool (typeOfInₛ ety₁ ety₂ x₁ x₂ env)))
```

`Cedar.Thm.entityUID?_some_implies_entity_lit` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L66))

```lean
theorem entityUID?_some_implies_entity_lit {x : Expr} {euid : EntityUID}
  (h₁ : entityUID? x = some euid) :
  x = Expr.lit (.entityUID euid)
```

`Cedar.Thm.actionUID?_some_implies_action_lit` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L74))

```lean
theorem actionUID?_some_implies_action_lit {x : Expr} {euid : EntityUID} {acts : ActionSchema}
  (h₁ : actionUID? x acts = some euid) :
  x = Expr.lit (.entityUID euid) ∧
  acts.contains euid = true
```

`Cedar.Thm.entityUIDs?_some_implies_entity_lits` (theorem, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L87))

```lean
theorem entityUIDs?_some_implies_entity_lits {x : Expr} {euids : List EntityUID}
  (h₁ : entityUIDs? x = some euids) :
  x = Expr.set ((List.map (Expr.lit ∘ Prim.entityUID) euids))
```

`Cedar.Thm.acts_maybeDescendentOf_false_implies_not_ancestor_type` (theorem, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L113))

```lean
theorem acts_maybeDescendentOf_false_implies_not_ancestor_type
  {euid : EntityUID} {ety : EntityType} {data : EntityData} {entry : ActionSchemaEntry}
  {env : TypeEnv} {request : Request} {entities : Entities}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (hdesc : env.acts.maybeDescendentOf euid.ty ety = false)
  (hent_found : Map.find? entities euid = some data)
  (hacts_entry : Map.find? env.acts euid = some entry) :
  ∀ euid', euid' ∈ data.ancestors → euid'.ty ≠ ety
```

`Cedar.Thm.entity_type_in_false_implies_inₑ_false` (theorem, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L138))

```lean
theorem entity_type_in_false_implies_inₑ_false
  {euid₁ euid₂ : EntityUID} {env : TypeEnv} {request : Request} {entities : Entities}
  (h₁ : InstanceOfWellFormedEnvironment request entities env)
  (h₂ : env.descendentOf euid₁.ty euid₂.ty = false) :
  inₑ euid₁ euid₂ entities = false
```

`Cedar.Thm.action_type_in_eq_action_inₑ` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L174))

```lean
theorem action_type_in_eq_action_inₑ
  (euid₁ euid₂ : EntityUID)
  {env : TypeEnv} {request : Request} {entities : Entities}
  (h₁ : InstanceOfWellFormedEnvironment request entities env)
  (h₂ : env.acts.contains euid₁) :
  inₑ euid₁ euid₂ entities = ActionSchema.descendentOf env.acts euid₁ euid₂
```

`Cedar.Thm.type_of_mem_is_soundₑ` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L188))

```lean
theorem type_of_mem_is_soundₑ {x₁ x₂ : Expr} {c₁ c₁' c₂' : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities} {ety₁ ety₂ : EntityType}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : (typeOf x₁ c₁ env).typeOf = Except.ok (CedarType.entity ety₁, c₁'))
  (h₄ : (typeOf x₂ c₁ env).typeOf = Except.ok (CedarType.entity ety₂, c₂'))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  ∃ v,
    EvaluatesTo (Expr.binaryApp BinaryOp.mem x₁ x₂) request entities v ∧
    InstanceOfType env v (CedarType.bool (typeOfInₑ ety₁ ety₂ x₁ x₂ env))
```

`Cedar.Thm.entity_set_type_implies_set_of_entities` (theorem, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L248))

```lean
theorem entity_set_type_implies_set_of_entities {env : TypeEnv} {vs : List Value} {ety : EntityType}
  (h₁ : InstanceOfType env (Value.set (Set.mk vs)) (CedarType.set (CedarType.entity ety))) :
  ∃ (euids : List EntityUID),
    vs.mapM Value.asEntityUID = Except.ok euids ∧
    ∀ euid, euid ∈ euids → euid.ty = ety
```

`Cedar.Thm.entity_type_in_false_implies_inₛ_false` (theorem, [line 278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L278))

```lean
theorem entity_type_in_false_implies_inₛ_false
  {euid : EntityUID} {euids : List EntityUID} {ety : EntityType}
  {env : TypeEnv} {request : Request} {entities : Entities}
  (h₁ : InstanceOfWellFormedEnvironment request entities env)
  (h₂ : env.descendentOf euid.ty ety = false)
  (h₃ : ∀ euid, euid ∈ euids → euid.ty = ety) :
  Set.any (fun x => inₑ euid x entities) (Set.make euids) = false
```

`Cedar.Thm.mapM'_eval_lits_eq_prims` (theorem, [line 330](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L330))

```lean
theorem mapM'_eval_lits_eq_prims {ps : List Prim} {vs : List Value} {request : Request} {entities : Entities}
  (h₁ : List.mapM' (evaluate · request entities) (List.map Expr.lit ps) = Except.ok vs) :
  vs = List.map Value.prim ps
```

`Cedar.Thm.evaluate_entity_set_eqv` (theorem, [line 349](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L349))

```lean
theorem evaluate_entity_set_eqv {vs : List Value} {euids euids' : List EntityUID} {request : Request} {entities : Entities}
  (h₁ : evaluate (Expr.set (List.map (Expr.lit ∘ Prim.entityUID) euids')) request entities =
        Except.ok (Value.set (Set.mk vs)))
  (h₂ : List.mapM Value.asEntityUID vs = Except.ok euids) :
  euids ≡ euids'
```

`Cedar.Thm.action_type_in_eq_action_inₛ` (theorem, [line 372](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L372))

```lean
theorem action_type_in_eq_action_inₛ
  {auid : EntityUID} {euids euids' : List EntityUID}
  {env : TypeEnv} {request : Request} {entities : Entities}
  (h₁ : InstanceOfWellFormedEnvironment request entities env)
  (h₂ : env.acts.contains auid)
  (h₃ : euids ≡ euids') :
  Set.any (fun x => inₑ auid x entities) (Set.make euids) ↔
  ∃ euid, euid ∈ euids' ∧ ActionSchema.descendentOf env.acts auid euid
```

`Cedar.Thm.type_of_mem_is_soundₛ` (theorem, [line 419](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L419))

```lean
theorem type_of_mem_is_soundₛ {x₁ x₂ : Expr} {c₁ c₁' c₂' : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities} {ety₁ ety₂ : EntityType}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : (typeOf x₁ c₁ env).typeOf = Except.ok (CedarType.entity ety₁, c₁'))
  (h₄ : (typeOf x₂ c₁ env).typeOf = Except.ok (CedarType.set (CedarType.entity ety₂), c₂'))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  ∃ v,
    EvaluatesTo (Expr.binaryApp BinaryOp.mem x₁ x₂) request entities v ∧
    InstanceOfType env v (CedarType.bool (typeOfInₛ ety₁ ety₂ x₁ x₂ env))
```

`Cedar.Thm.type_of_mem_is_sound` (theorem, [line 500](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean#L500))

```lean
theorem type_of_mem_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp .mem x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp .mem x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp .mem x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](../basic.md)

## Proof depends on

- [Authorization/Evaluator](../../../authorization-2/evaluator.md)
- [Thm/Data/LT](../../../data/lt.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Mem.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.Mem.json)
