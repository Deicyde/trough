---
catalog: module
lean: Cedar.Thm.has_tag_false_of_entity_type_tagless, Cedar.Thm.eq_false_of_distinct_entity_types, Cedar.Thm.mem_false_of_cannot_be_inₑ, Cedar.Thm.mem_false_of_cannot_be_inₛ, Cedar.Thm.tpe_inₑ_agrees, Cedar.Thm.try_decide_residual₂_sound, Cedar.Thm.partial_evaluate_is_sound_binary_app
statement: formalized
proof: formalized
---

# Soundness/Binary

`Cedar.Thm.TPE.Soundness.Binary`, in [Cedar/Thm/TPE/Soundness/Binary.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean).

`Cedar.Thm.has_tag_false_of_entity_type_tagless` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L39))

> If the schema does not declare that an entity can have tags, then it does not have any tags.

```lean
theorem has_tag_false_of_entity_type_tagless
  {env : TypeEnv} {request : Request} {entities : Entities}
  {uid : EntityUID} {tag : Tag}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (htagless : EntitySchema.tags? env.ets uid.ty = some .none) :
  Spec.hasTag uid tag entities = .ok (.prim (.bool false))
```

`Cedar.Thm.eq_false_of_distinct_entity_types` (theorem, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L67))

> Two values of distinct entity types cannot be equal.

```lean
theorem eq_false_of_distinct_entity_types
  {env : TypeEnv} {v₁ v₂ : Value} {ety₁ ety₂ : EntityType}
  (hinst₁ : InstanceOfType env v₁ (.entity ety₁))
  (hinst₂ : InstanceOfType env v₂ (.entity ety₂))
  (hne : ety₁ ≠ ety₂) :
  (v₁ == v₂) = false
```

`Cedar.Thm.mem_false_of_cannot_be_inₑ` (theorem, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L83))

> An entity of type `ety₁` cannot be `in` an entity of type `ety₂` when the schema does not declare `ety₂` an ancestor type of `ety₁`.

```lean
theorem mem_false_of_cannot_be_inₑ
  {env : TypeEnv} {request : Request} {entities : Entities}
  {v₁ v₂ : Value} {ety₁ ety₂ : EntityType}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (hinst₁ : InstanceOfType env v₁ (.entity ety₁))
  (hinst₂ : InstanceOfType env v₂ (.entity ety₂))
  (hdesc : env.descendentOf ety₁ ety₂ = false) :
  Spec.apply₂ .mem v₁ v₂ entities = .ok (Value.prim (Prim.bool false))
```

`Cedar.Thm.mem_false_of_cannot_be_inₛ` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L98))

> The set-valued counterpart of `mem_false_of_cannot_be_inₑ`.

```lean
theorem mem_false_of_cannot_be_inₛ
  {env : TypeEnv} {request : Request} {entities : Entities}
  {v₁ v₂ : Value} {ety₁ ety₂ : EntityType}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (hinst₁ : InstanceOfType env v₁ (.entity ety₁))
  (hinst₂ : InstanceOfType env v₂ (.set (.entity ety₂)))
  (hdesc : env.descendentOf ety₁ ety₂ = false) :
  Spec.apply₂ .mem v₁ v₂ entities = .ok (Value.prim (Prim.bool false))
```

`Cedar.Thm.tpe_inₑ_agrees` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L117))

> Whenever `TPE.inₑ` decides `in` for two concrete UIDs, concrete evaluation agrees.

```lean
theorem tpe_inₑ_agrees
{es : Entities}
{pes : PartialEntities}
{uid₁ uid₂ : EntityUID}
{b : Bool}
(href : EntitiesRefine es pes)
(hdec : TPE.inₑ uid₁ uid₂ pes = .some b) :
  Spec.inₑ uid₁ uid₂ es = b
```

`Cedar.Thm.try_decide_residual₂_sound` (theorem, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L144))

> If `tryDecideResidual₂` decides a binary operation from the operands' types,
> then concrete evaluation agrees.

```lean
theorem try_decide_residual₂_sound
{env : TypeEnv}
{op₂ : BinaryOp}
{r₁ r₂ : Residual}
{req : Request}
{es : Entities}
{v : Value}
(hwf : InstanceOfWellFormedEnvironment req es env)
(hwt₁ : Residual.WellTyped env r₁)
(hwt₂ : Residual.WellTyped env r₂)
(hdec : TPE.tryDecideResidual₂ env op₂ r₁ r₂ = .some v) :
  ∃ v₁ v₂, r₁.evaluate req es = .ok v₁ ∧ r₂.evaluate req es = .ok v₂ ∧
    Spec.apply₂ op₂ v₁ v₂ es = .ok v
```

`Cedar.Thm.partial_evaluate_is_sound_binary_app` (theorem, [line 211](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean#L211))

```lean
theorem partial_evaluate_is_sound_binary_app
{op₂ : BinaryOp}
{ty : CedarType}
{x₁ x₂ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{env : TypeEnv}
(h₂ : InstanceOfWellFormedEnvironment req es env)
(h₄ : RequestAndEntitiesRefine req es preq pes)
(hwt₁ : Residual.WellTyped env x₁)
(hwt₂ : Residual.WellTyped env x₂)
(howt : BinaryResidualWellTyped env op₂ x₁ x₂ ty)
(hᵢ₁ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es))
(hᵢ₂ : Except.toOption (x₂.evaluate req es) = Except.toOption ((TPE.evaluate env x₂ preq pes).evaluate req es)) :
  Except.toOption ((Residual.binaryApp op₂ x₁ x₂ ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.binaryApp op₂ x₁ x₂ ty) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Proof depends on

- [ErrorFree](../errorfree.md)
- [Soundness/Basic](basic.md)
- [TPE/WellTyped](../welltyped.md)
- [Mem](../../validation-2/typechecker-2/binaryapp-2/mem.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Binary.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Binary.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Binary.json)
