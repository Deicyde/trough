---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_val, Cedar.Thm.partial_evaluate_is_sound_var
statement: formalized
proof: formalized
---

# Soundness/Var

`Cedar.Thm.TPE.Soundness.Var`, in [Cedar/Thm/TPE/Soundness/Var.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Var.lean).

`Cedar.Thm.partial_evaluate_is_sound_val` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Var.lean#L37))

```lean
theorem partial_evaluate_is_sound_val
{v : Value}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{ty : CedarType} :
  Except.toOption ((Residual.val v ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.val v ty) preq pes).evaluate req es)
```

`Cedar.Thm.partial_evaluate_is_sound_var` (theorem, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Var.lean#L50))

```lean
theorem partial_evaluate_is_sound_var
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{v : Var}
{ty : CedarType}
(h₄ : RequestAndEntitiesRefine req es preq pes) :
  Except.toOption ((Residual.var v ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.var v ty) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)
- [Residual/Soundness](../../welltyped/residual-2/soundness.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Var.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Var.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Var.json)
