---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_error, Cedar.Thm.partial_evaluate_is_sound
statement: formalized
proof: formalized
---

# TPE/Soundness

`Cedar.Thm.TPE.Soundness`, in [Cedar/Thm/TPE/Soundness.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness.lean).

`Cedar.Thm.partial_evaluate_is_sound_error` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness.lean#L48))

```lean
theorem partial_evaluate_is_sound_error
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{ty : CedarType} :
  Except.toOption ((Residual.error ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.error ty) preq pes).evaluate req es)
```

`Cedar.Thm.partial_evaluate_is_sound` (theorem, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness.lean#L64))

> The main lemma: Evaluating a residual derived from partially evaluating
> a well-typed expression is equivalent to that of evaluating the original
> expression, provided that requests and entities are consistent. The equivalency
> is defined using `Except.toOption`.

```lean
theorem partial_evaluate_is_sound
  {x : Residual}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {env : TypeEnv} :
  Residual.WellTyped env x →
  InstanceOfWellFormedEnvironment req es env →
  RequestAndEntitiesRefine req es preq pes →
  (x.evaluate req es).toOption = ((Cedar.TPE.evaluate env x preq pes).evaluate req es).toOption
```

## Depends on

- [TPE/Evaluator](../../tpe/evaluator.md)
- [Thm/TPE/Input](input.md)
- [Residual/Definition](../welltyped/residual-2/definition.md)

## Proof depends on

- [Soundness/And](soundness-2/and.md)
- [Soundness/Binary](soundness-2/binary.md)
- [Soundness/Call](soundness-2/call.md)
- [Soundness/ExtHasAttr](soundness-2/exthasattr.md)
- [Soundness/GetAttr](soundness-2/getattr.md)
- [Soundness/IfThenElse](soundness-2/ifthenelse.md)
- [Soundness/Or](soundness-2/or.md)
- [Soundness/Record](soundness-2/record.md)
- [Soundness/Set](soundness-2/set.md)
- [Soundness/Unary](soundness-2/unary.md)
- [Soundness/Var](soundness-2/var.md)

## Sources

- [Cedar/Thm/TPE/Soundness.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.Soundness.json)
