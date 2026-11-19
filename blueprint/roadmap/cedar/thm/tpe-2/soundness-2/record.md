---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_record
statement: formalized
proof: formalized
---

# Soundness/Record

`Cedar.Thm.TPE.Soundness.Record`, in [Cedar/Thm/TPE/Soundness/Record.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Record.lean).

`Cedar.Thm.partial_evaluate_is_sound_record` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Record.lean#L37))

```lean
theorem partial_evaluate_is_sound_record
{m : List (Attr × Residual)}
{rty : RecordType}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
(hᵢ₁ : ∀ (k : Attr) (v : Residual),
  (k, v) ∈ m →
    Except.toOption (v.evaluate req es) = Except.toOption ((TPE.evaluate env v preq pes).evaluate req es)) :
  Except.toOption ((Residual.record m (CedarType.record rty)).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.record m (CedarType.record rty)) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)

## Proof depends on

- [Soundness/Basic](basic.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Record.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Record.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Record.json)
