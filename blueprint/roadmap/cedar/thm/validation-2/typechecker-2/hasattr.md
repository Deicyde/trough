---
catalog: module
lean: Cedar.Thm.hasAttrInRecord_has_empty_or_singleton_capabilities, Cedar.Thm.type_of_hasAttr_inversion, Cedar.Thm.type_of_hasAttr_is_sound_for_records, Cedar.Thm.type_of_hasAttr_is_sound_for_entities, Cedar.Thm.type_of_hasAttr_is_sound
statement: formalized
proof: formalized
---

# Typechecker/HasAttr

`Cedar.Thm.Validation.Typechecker.HasAttr`, in [Cedar/Thm/Validation/Typechecker/HasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean).

> This file proves that typechecking of `.hasAttr` expressions is sound.

`Cedar.Thm.hasAttrInRecord_has_empty_or_singleton_capabilities` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean#L35))

```lean
theorem hasAttrInRecord_has_empty_or_singleton_capabilities {x₁ : Expr} {a : Attr} {c₁ c₂ : Capabilities} {rty : RecordType} {ty₁ : CedarType} :
  hasAttrInRecord rty x₁ a c₁ b = Except.ok (ty₁, c₂) →
  c₂ = ∅ ∨ c₂ = Capabilities.singleton x₁ (.attr a)
```

`Cedar.Thm.type_of_hasAttr_inversion` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean#L46))

```lean
theorem type_of_hasAttr_inversion {x₁ : Expr} {a : Attr} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.hasAttr x₁ a) c₁ env = Except.ok (tx, c₂)) :
  (c₂ = ∅ ∨ c₂ = Capabilities.singleton x₁ (.attr a)) ∧
  ∃ tx₁ c₁',
    typeOf x₁ c₁ env = .ok (tx₁, c₁') ∧
    tx = .hasAttr tx₁ a tx.typeOf ∧
    ((∃ ety, tx₁.typeOf = .entity ety) ∨
     (∃ rty, tx₁.typeOf = .record rty))
```

`Cedar.Thm.type_of_hasAttr_is_sound_for_records` (theorem, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean#L78))

```lean
theorem type_of_hasAttr_is_sound_for_records {x₁ : Expr} {a : Attr} {c₁ c₁' : Capabilities} {env : TypeEnv} {rty : RecordType} {request : Request} {entities : Entities} {v₁ : Value}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : typeOf (Expr.hasAttr x₁ a) c₁ env = Except.ok (ty, c₂))
  (h₃ : (typeOf x₁ c₁ env).typeOf = Except.ok (CedarType.record rty, c₁'))
  (h₄ : evaluate x₁ request entities = Except.ok v₁)
  (h₅ : InstanceOfType env v₁ (CedarType.record rty)) :
  ∃ v,
  (hasAttr v₁ a entities = Except.error Error.entityDoesNotExist ∨
   hasAttr v₁ a entities = Except.error Error.extensionError ∨
   hasAttr v₁ a entities = Except.error Error.arithBoundsError ∨
   hasAttr v₁ a entities = Except.ok v) ∧
  InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_hasAttr_is_sound_for_entities` (theorem, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean#L124))

```lean
theorem type_of_hasAttr_is_sound_for_entities {x₁ : Expr} {a : Attr} {c₁ c₁' : Capabilities} {env : TypeEnv} {ety : EntityType} {request : Request} {entities : Entities} {v₁ : Value}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.hasAttr x₁ a) c₁ env = Except.ok (ty, c₂))
  (h₄ : (typeOf x₁ c₁ env).typeOf = Except.ok (CedarType.entity ety, c₁'))
  (h₅ : evaluate x₁ request entities = Except.ok v₁)
  (h₆ : InstanceOfType env v₁ (CedarType.entity ety)) :
  ∃ v,
  (hasAttr v₁ a entities = Except.error Error.entityDoesNotExist ∨
   hasAttr v₁ a entities = Except.error Error.extensionError ∨
   hasAttr v₁ a entities = Except.error Error.arithBoundsError ∨
   hasAttr v₁ a entities = Except.ok v) ∧
   InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_hasAttr_is_sound` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean#L194))

```lean
theorem type_of_hasAttr_is_sound {x₁ : Expr} {a : Attr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.hasAttr x₁ a) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.hasAttr x₁ a) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.hasAttr x₁ a) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/HasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/HasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.HasAttr.json)
