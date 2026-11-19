---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_set
statement: formalized
proof: formalized
---

# Soundness/Set

`Cedar.Thm.TPE.Soundness.Set`, in [Cedar/Thm/TPE/Soundness/Set.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Set.lean).

`Cedar.Thm.partial_evaluate_is_sound_set` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Set.lean#L37))

```lean
theorem partial_evaluate_is_sound_set
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{ls : List Residual}
{ty : CedarType}
(hᵢ₁ : ∀ (x : Residual),
  x ∈ ls →
    Except.toOption (x.evaluate req es) = Except.toOption ((TPE.evaluate env x preq pes).evaluate req es)) :
  Except.toOption ((Residual.set ls ty.set).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.set ls ty.set) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)

## Proof depends on

- [Soundness/Basic](basic.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Set.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Set.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Set.json)
