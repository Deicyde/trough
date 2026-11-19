---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_get_attr
statement: formalized
proof: formalized
---

# Soundness/GetAttr

`Cedar.Thm.TPE.Soundness.GetAttr`, in [Cedar/Thm/TPE/Soundness/GetAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/GetAttr.lean).

`Cedar.Thm.partial_evaluate_is_sound_get_attr` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/GetAttr.lean#L37))

```lean
theorem partial_evaluate_is_sound_get_attr
{x₁ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{attr : Attr}
{ty : CedarType}
(h₄ : RequestAndEntitiesRefine req es preq pes)
(hᵢ₁ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es)) :
  Except.toOption ((x₁.getAttr attr ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (x₁.getAttr attr ty) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)

## Proof depends on

- [WellTyped/GetAttr](../welltyped-2/getattr.md)
- [Residual/Soundness](../../welltyped/residual-2/soundness.md)

## Sources

- [Cedar/Thm/TPE/Soundness/GetAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/GetAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.GetAttr.json)
