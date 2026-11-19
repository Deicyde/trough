---
catalog: module
lean: Cedar.Thm.residual_well_typed_is_sound_val, Cedar.Thm.residual_well_typed_is_sound_var, Cedar.Thm.residual_well_typed_is_sound_and, Cedar.Thm.residual_well_typed_is_sound_or, Cedar.Thm.residual_well_typed_is_sound_ite, Cedar.Thm.residual_well_typed_is_sound_unary_app, Cedar.Thm.residual_well_typed_is_sound_binary_app, Cedar.Thm.residual_well_typed_is_sound_ext_has_attr_entity, Cedar.Thm.residual_well_typed_is_sound_ext_has_attr_record, Cedar.Thm.residual_well_typed_is_sound_has_attr_entity, Cedar.Thm.residual_well_typed_is_sound_has_attr_record, Cedar.Thm.residual_well_typed_is_sound_get_attr_entity, Cedar.Thm.residual_well_typed_is_sound_get_attr_record, Cedar.Thm.residual_well_typed_is_sound_set, Cedar.Thm.residual_attr_value_has_attrType, Cedar.Thm.residual_well_typed_is_sound_record, Cedar.Thm.residual_well_typed_is_sound_call
statement: formalized
proof: formalized
---

# Residual/Soundness

`Cedar.Thm.WellTyped.Residual.Soundness`, in [Cedar/Thm/WellTyped/Residual/Soundness.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean).

> This file contains residual-specific lemmas of the theorem `residual_well_typed_is_sound`

`Cedar.Thm.residual_well_typed_is_sound_val` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L36))

```lean
theorem residual_well_typed_is_sound_val
{v : Value}
{v' : Value}
{env : TypeEnv}
{request : Request}
{entities : Entities}
{ty : CedarType}
(h₁ : InstanceOfType env v' ty)
(h₂ : (Residual.val v' ty).evaluate request entities = Except.ok v) : (InstanceOfType env v (Residual.val v' ty).typeOf)
```

`Cedar.Thm.residual_well_typed_is_sound_var` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L51))

```lean
theorem residual_well_typed_is_sound_var
{v : Value}
{var : Var}
{env : TypeEnv}
{request : Request}
{entities : Entities}
{ty : CedarType}
(h₁ : InstanceOfWellFormedEnvironment request entities env)
(h₂ : Var.WellTyped env var ty)
(h₃ : (Residual.var var ty).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.var var ty).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_and` (theorem, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L89))

```lean
theorem residual_well_typed_is_sound_and
{v : Value}
{x₁ x₂ : Residual}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₁ : x₁.typeOf = CedarType.bool BoolType.anyBool)
(h₂ : x₂.typeOf = CedarType.bool BoolType.anyBool)
(hᵢ₁ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(hᵢ₂ : ∀ {v : Value}, x₂.evaluate request entities = Except.ok v → InstanceOfType env v x₂.typeOf)
(h₃ : (Residual.and x₁ x₂ (CedarType.bool BoolType.anyBool)).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.and x₁ x₂ (CedarType.bool BoolType.anyBool)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_or` (theorem, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L132))

```lean
theorem residual_well_typed_is_sound_or
{v : Value}
{x₁ x₂ : Residual}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₁ : x₁.typeOf = CedarType.bool BoolType.anyBool)
(h₂ : x₂.typeOf = CedarType.bool BoolType.anyBool)
(hᵢ₁ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(hᵢ₂ : ∀ {v : Value}, x₂.evaluate request entities = Except.ok v → InstanceOfType env v x₂.typeOf)
(h₃ : (Residual.or x₁ x₂ (CedarType.bool BoolType.anyBool)).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.or x₁ x₂ (CedarType.bool BoolType.anyBool)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_ite` (theorem, [line 175](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L175))

```lean
theorem residual_well_typed_is_sound_ite
{v : Value}
{x₁ x₂ x₃ : Residual}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₁ : x₁.typeOf = CedarType.bool BoolType.anyBool)
(h₂ : x₂.typeOf = x₃.typeOf)
(hᵢ₁ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(hᵢ₂ : ∀ {v : Value}, x₂.evaluate request entities = Except.ok v → InstanceOfType env v x₂.typeOf)
(hᵢ₃ : ∀ {v : Value}, x₃.evaluate request entities = Except.ok v → InstanceOfType env v x₃.typeOf)
(h₃ : (Residual.ite x₁ x₂ x₃ x₂.typeOf).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.ite x₁ x₂ x₃ x₂.typeOf).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_unary_app` (theorem, [line 211](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L211))

```lean
theorem residual_well_typed_is_sound_unary_app
{v : Value}
{op₁ : UnaryOp}
{x₁ : Residual}
{env : TypeEnv}
{request : Request}
{entities : Entities}
{ty : CedarType}
(h₁ : UnaryResidualWellTyped op₁ x₁ ty)
(_ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(h₂ : (Residual.unaryApp op₁ x₁ ty).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.unaryApp op₁ x₁ ty).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_binary_app` (theorem, [line 262](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L262))

```lean
theorem residual_well_typed_is_sound_binary_app
{v : Value}
{op₂ : BinaryOp}
{x₁ x₂ : Residual}
{env : TypeEnv}
{request : Request}
{entities : Entities}
{ty : CedarType}
(h₁ : InstanceOfWellFormedEnvironment request entities env)
(h₄ : BinaryResidualWellTyped env op₂ x₁ x₂ ty)
(hᵢ₁ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(hᵢ₂ : ∀ {v : Value}, x₂.evaluate request entities = Except.ok v → InstanceOfType env v x₂.typeOf)
(h₃ : (Residual.binaryApp op₂ x₁ x₂ ty).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.binaryApp op₂ x₁ x₂ ty).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_ext_has_attr_entity` (theorem, [line 384](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L384))

```lean
theorem residual_well_typed_is_sound_ext_has_attr_entity
{v : Value}
{x₁ : Residual}
{attr : Attr}
{attrs : List Attr}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₃ : (Residual.extHasAttr x₁ attr attrs (CedarType.bool BoolType.anyBool)).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.extHasAttr x₁ attr attrs (CedarType.bool BoolType.anyBool)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_ext_has_attr_record` (theorem, [line 403](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L403))

```lean
theorem residual_well_typed_is_sound_ext_has_attr_record
{v : Value}
{x₁ : Residual}
{attr : Attr}
{attrs : List Attr}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₃ : (Residual.extHasAttr x₁ attr attrs (CedarType.bool BoolType.anyBool)).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.extHasAttr x₁ attr attrs (CedarType.bool BoolType.anyBool)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_has_attr_entity` (theorem, [line 422](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L422))

```lean
theorem residual_well_typed_is_sound_has_attr_entity
{v : Value}
{x₁ : Residual}
{attr : Attr}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₃ : (Residual.hasAttr x₁ attr (CedarType.bool BoolType.anyBool)).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.hasAttr x₁ attr (CedarType.bool BoolType.anyBool)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_has_attr_record` (theorem, [line 440](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L440))

```lean
theorem residual_well_typed_is_sound_has_attr_record
{v : Value}
{x₁ : Residual}
{attr : Attr}
{env : TypeEnv}
{request : Request}
{entities : Entities}
(h₃ : (Residual.hasAttr x₁ attr (CedarType.bool BoolType.anyBool)).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.hasAttr x₁ attr (CedarType.bool BoolType.anyBool)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_get_attr_entity` (theorem, [line 458](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L458))

```lean
theorem residual_well_typed_is_sound_get_attr_entity
{v : Value}
{env : TypeEnv}
{request : Request}
{entities : Entities}
{ety : EntityType}
{rty : RecordType}
{x₁ : Residual}
{attr : Attr}
{ty : CedarType}
(h₁ : InstanceOfWellFormedEnvironment request entities env)
(h₂ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(h₄ : x₁.typeOf = CedarType.entity ety)
(h₅ : (env.ets.attrs? ety).map RecordType.liftBoolTypes = some rty)
(h₆ : Option.map Qualified.getType (Data.Map.find? rty attr) = some ty)
(h₇ : (Residual.getAttr x₁ attr ty).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.getAttr x₁ attr ty).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_get_attr_record` (theorem, [line 528](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L528))

```lean
theorem residual_well_typed_is_sound_get_attr_record
{v : Value}
{request : Request}
{entities : Entities}
{rty : RecordType}
{x₁ : Residual}
{attr : Attr}
{ty : CedarType}
{env : TypeEnv}
(h₂ : ∀ {v : Value}, x₁.evaluate request entities = Except.ok v → InstanceOfType env v x₁.typeOf)
(h₄ : x₁.typeOf = CedarType.record rty)
(h₅ : Option.map Qualified.getType (Data.Map.find? rty attr) = some ty)
(h₆ : (Residual.getAttr x₁ attr ty).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.getAttr x₁ attr ty).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_set` (theorem, [line 564](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L564))

```lean
theorem residual_well_typed_is_sound_set
{v : Value}
{request : Request}
{entities : Entities}
{ls : List Residual}
{ty : CedarType}
{env : TypeEnv}
(h₁ : ∀ (x : Residual), x ∈ ls → ∀ (v : Value), x.evaluate request entities = Except.ok v → InstanceOfType env v x.typeOf)
(h₂ : ∀ (x : Residual), x ∈ ls → x.typeOf = ty)
(h₃ : (Residual.set ls ty.set).evaluate request entities = Except.ok v)
: InstanceOfType env v (Residual.set ls ty.set).typeOf
```

`Cedar.Thm.residual_attr_value_has_attrType` (theorem, [line 592](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L592))

```lean
theorem residual_attr_value_has_attrType
{request : Request}
{entities : Entities}
{m : List (Attr × Residual)}
{r : List (Attr × Value)}
{env : TypeEnv}
(h₁ : ∀ (k : Attr) (v : Residual),
  (k, v) ∈ m → ∀ (v_1 : Value), v.evaluate request entities = Except.ok v_1 → InstanceOfType env v_1 v.typeOf)
(h₃ : List.Forall₂ (λ x y => Prod.mk x.fst <$> x.snd.evaluate request entities = Except.ok y) m r) :
List.Forall₂ (λ x y => x.fst = y.fst ∧ InstanceOfType env x.snd (Qualified.getType y.snd)) r (List.map
      (fun x =>
        match x with
        | (a, ty) => (a, Qualified.required ty.typeOf))
      m)
```

`Cedar.Thm.residual_well_typed_is_sound_record` (theorem, [line 636](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L636))

```lean
theorem residual_well_typed_is_sound_record
{v : Value}
{request : Request}
{entities : Entities}
{m : List (Attr × Residual)}
{rty : RecordType}
{env : TypeEnv}
(h₁ : ∀ (k : Attr) (v : Residual),
  (k, v) ∈ m → ∀ (v_1 : Value), v.evaluate request entities = Except.ok v_1 → InstanceOfType env v_1 v.typeOf)
(h₂ : rty =
  Data.Map.make
    (List.map
      (fun x =>
        match x with
        | (a, r) => (a, Qualified.required r.typeOf))
      m))
(h₃ : (Residual.record m (CedarType.record rty)).evaluate request entities = Except.ok v) :
  InstanceOfType env v (Residual.record m (CedarType.record rty)).typeOf
```

`Cedar.Thm.residual_well_typed_is_sound_call` (theorem, [line 678](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean#L678))

```lean
theorem residual_well_typed_is_sound_call
{v : Value}
{request : Request}
{entities : Entities}
{xfn : ExtFun}
{args : List Residual}
{ty : CedarType}
{env : TypeEnv}
(h₁ : ExtResidualWellTyped xfn args ty)
(h₂ : (Residual.call xfn args ty).evaluate request entities = Except.ok v) :
InstanceOfType env v (Residual.call xfn args ty).typeOf
```

## Depends on

- [Residual/Definition](definition.md)

## Proof depends on

- [Authorization/Authorizer](../../authorization-2/authorizer.md)
- [Typechecker/Call](../../validation-2/typechecker-2/call.md)
- [Typechecker/Record](../../validation-2/typechecker-2/record.md)

## Sources

- [Cedar/Thm/WellTyped/Residual/Soundness.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Soundness.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.WellTyped.Residual.Soundness.json)
