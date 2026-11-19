---
catalog: module
lean: Cedar.Thm.has_attr_false_of_absent_in_record_type, Cedar.Thm.has_attr_false_of_absent_in_entity_type, Cedar.Thm.try_decide_has_residual_sound, Cedar.Thm.partial_evaluate_is_sound_has_attr
statement: formalized
proof: formalized
---

# Soundness/HasAttr

`Cedar.Thm.TPE.Soundness.HasAttr`, in [Cedar/Thm/TPE/Soundness/HasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/HasAttr.lean).

`Cedar.Thm.has_attr_false_of_absent_in_record_type` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/HasAttr.lean#L40))

> A record value whose type does not declare an attribute `a` does not have `a`.

```lean
theorem has_attr_false_of_absent_in_record_type
  {env : TypeEnv} {r : Map Attr Value} {rty : RecordType} {a : Attr} {es : Entities}
  (hinst : InstanceOfType env (.record r) (.record rty))
  (hnone : rty.find? a = .none) :
  Spec.hasAttr (.record r) a es = .ok (.prim (.bool false))
```

`Cedar.Thm.has_attr_false_of_absent_in_entity_type` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/HasAttr.lean#L51))

> If the schema does not declare an attribute `a` for an entity, then it does not have `a`.

```lean
theorem has_attr_false_of_absent_in_entity_type
  {env : TypeEnv} {request : Request} {entities : Entities}
  {uid : EntityUID} {rty : RecordType} {a : Attr}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (hattrs : EntitySchema.attrs? env.ets uid.ty = some rty)
  (hnone : rty.find? a = .none) :
  Spec.hasAttr (.prim (.entityUID uid)) a entities = .ok (.prim (.bool false))
```

`Cedar.Thm.try_decide_has_residual_sound` (theorem, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/HasAttr.lean#L72))

> If `tryDecideHasResidual` decides a `has` expression from the operand's type,
> then concrete evaluation agrees.

```lean
theorem try_decide_has_residual_sound
{env : TypeEnv}
{r₁ : Residual}
{req : Request}
{es : Entities}
{attr : Attr}
{v : Value}
(hwf : InstanceOfWellFormedEnvironment req es env)
(hwt : Residual.WellTyped env r₁)
(hdec : TPE.tryDecideHasResidual env r₁ attr = .some v) :
  ∃ v', r₁.evaluate req es = .ok v' ∧ Spec.hasAttr v' attr es = .ok v
```

`Cedar.Thm.partial_evaluate_is_sound_has_attr` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/HasAttr.lean#L122))

```lean
theorem partial_evaluate_is_sound_has_attr
{env : TypeEnv}
{x₁ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{attr : Attr}
(h₂ : InstanceOfWellFormedEnvironment req es env)
(hwt : Residual.WellTyped env x₁)
(h₄ : RequestAndEntitiesRefine req es preq pes)
(hᵢ₁ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es)) :
  Except.toOption ((x₁.hasAttr attr (CedarType.bool BoolType.anyBool)).evaluate req es) =
  Except.toOption ((TPE.evaluate env (x₁.hasAttr attr (CedarType.bool BoolType.anyBool)) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Proof depends on

- [ErrorFree](../errorfree.md)
- [TPE/WellTyped](../welltyped.md)

## Sources

- [Cedar/Thm/TPE/Soundness/HasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/HasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.HasAttr.json)
