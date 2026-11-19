---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_call
statement: formalized
proof: formalized
---

# Soundness/Call

`Cedar.Thm.TPE.Soundness.Call`, in [Cedar/Thm/TPE/Soundness/Call.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Call.lean).

`Cedar.Thm.partial_evaluate_is_sound_call` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Call.lean#L37))

```lean
theorem partial_evaluate_is_sound_call
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{xfn : ExtFun}
{args : List Residual}
{ty : CedarType}
(hᵢ₁ : ∀ (x : Residual),
  x ∈ args →
    Except.toOption (x.evaluate req es) = Except.toOption ((TPE.evaluate env x preq pes).evaluate req es)) :
  Except.toOption ((Residual.call xfn args ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.call xfn args ty) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)

## Proof depends on

- [Soundness/Basic](basic.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Call.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Call.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Call.json)
