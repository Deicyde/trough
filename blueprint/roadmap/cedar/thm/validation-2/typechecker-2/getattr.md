---
catalog: module
lean: Cedar.Thm.getAttrInRecord_has_empty_capabilities, Cedar.Thm.type_of_getAttr_inversion, Cedar.Thm.type_of_getAttr_is_sound_for_records, Cedar.Thm.type_of_getAttr_is_sound_for_entities, Cedar.Thm.type_of_getAttr_is_sound
statement: formalized
proof: formalized
---

# Typechecker/GetAttr

`Cedar.Thm.Validation.Typechecker.GetAttr`, in [Cedar/Thm/Validation/Typechecker/GetAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean).

> This file proves that typechecking of `.getAttr` expressions is sound.

`Cedar.Thm.getAttrInRecord_has_empty_capabilities` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean#L35))

```lean
theorem getAttrInRecord_has_empty_capabilities {x₁ : Expr} {a : Attr} {c₁ c₂ : Capabilities} {rty : RecordType} {ty ty₁ : CedarType} :
  getAttrInRecord ty rty x₁ a c₁ = Except.ok (ty₁, c₂) →
  c₂ = ∅
```

`Cedar.Thm.type_of_getAttr_inversion` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean#L46))

```lean
theorem type_of_getAttr_inversion {x₁ : Expr} {a : Attr} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.getAttr x₁ a) c₁ env = Except.ok (tx, c₂)) :
  c₂ = ∅ ∧
  ∃ tx₁ c₁',
    typeOf x₁ c₁ env = .ok (tx₁, c₁') ∧
    tx = .getAttr tx₁ a tx.typeOf ∧
      ((∃ ety, tx₁.typeOf = .entity ety) ∨
       (∃ rty, tx₁.typeOf = .record rty))
```

`Cedar.Thm.type_of_getAttr_is_sound_for_records` (theorem, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean#L76))

```lean
theorem type_of_getAttr_is_sound_for_records {x₁ : Expr} {a : Attr} {c₁ c₁' : Capabilities} {env : TypeEnv} {rty : RecordType} {request : Request} {entities : Entities} {v₁ : Value}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : typeOf (Expr.getAttr x₁ a) c₁ env = Except.ok (ty, ∅))
  (h₃ : (typeOf x₁ c₁ env).typeOf = Except.ok (CedarType.record rty, c₁'))
  (h₄ : evaluate x₁ request entities = Except.ok v₁)
  (h₅ : InstanceOfType env v₁ (CedarType.record rty)) :
  ∃ v,
  (getAttr v₁ a entities = Except.error Error.entityDoesNotExist ∨
   getAttr v₁ a entities = Except.error Error.extensionError ∨
   getAttr v₁ a entities = Except.error Error.arithBoundsError ∨
   getAttr v₁ a entities = Except.ok v) ∧
   InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_getAttr_is_sound_for_entities` (theorem, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean#L139))

```lean
theorem type_of_getAttr_is_sound_for_entities {x₁ : Expr} {a : Attr} {c₁ c₁' : Capabilities} {env : TypeEnv} {ety : EntityType} {request : Request} {entities : Entities} {v₁ : Value}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.getAttr x₁ a) c₁ env = Except.ok (ty, ∅))
  (h₄ : (typeOf x₁ c₁ env).typeOf = Except.ok (CedarType.entity ety, c₁'))
  (h₅ : evaluate x₁ request entities = Except.ok v₁)
  (h₆ : InstanceOfType env v₁ (CedarType.entity ety)) :
  ∃ v,
  (getAttr v₁ a entities = Except.error Error.entityDoesNotExist ∨
   getAttr v₁ a entities = Except.error Error.extensionError ∨
   getAttr v₁ a entities = Except.error Error.arithBoundsError ∨
   getAttr v₁ a entities = Except.ok v) ∧
   InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_getAttr_is_sound` (theorem, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean#L203))

```lean
theorem type_of_getAttr_is_sound {x₁ : Expr} {a : Attr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.getAttr x₁ a) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.getAttr x₁ a) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.getAttr x₁ a) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/GetAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/GetAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.GetAttr.json)
