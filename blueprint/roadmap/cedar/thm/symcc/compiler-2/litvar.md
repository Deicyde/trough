---
catalog: module
lean: Cedar.Thm.compile_evaluate_lit, Cedar.Thm.compile_evaluate_var, Cedar.Thm.compile_interpret_lit, Cedar.Thm.compile_interpret_var
statement: formalized
proof: formalized
---

# Compiler/LitVar

`Cedar.Thm.SymCC.Compiler.LitVar`, in [Cedar/Thm/SymCC/Compiler/LitVar.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/LitVar.lean).

> This file proves the compilation lemmas for `.lit` and `.var` expressions.
> -

`Cedar.Thm.compile_evaluate_lit` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/LitVar.lean#L47))

```lean
public theorem compile_evaluate_lit {p : Prim} {env : Env} {εnv : SymEnv} {t : Term}
  (h₁ : compile (.lit p) εnv = .ok t) :
  evaluate (.lit p) env.request env.entities ∼ t
```

`Cedar.Thm.compile_evaluate_var` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/LitVar.lean#L71))

```lean
public theorem compile_evaluate_var {v : Var} {env : Env} {εnv : SymEnv} {t : Term}
  (h₁ : env ∼ εnv)
  (h₂ : compile (.var v) εnv = .ok t) :
  evaluate (.var v) env.request env.entities ∼ t
```

`Cedar.Thm.compile_interpret_lit` (theorem, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/LitVar.lean#L88))

```lean
public theorem compile_interpret_lit {p : Prim} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (h₁ : compile (.lit p) εnv = .ok t) :
  compile (.lit p) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_interpret_var` (theorem, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/LitVar.lean#L106))

```lean
public theorem compile_interpret_var {v : Var} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (h₁ : I.WellFormed εnv.entities)
  (h₂ : εnv.WellFormedFor (.var v))
  (h₃ : compile (.var v) εnv = .ok t) :
  compile (.var v) (εnv.interpret I) = .ok (t.interpret I)
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [Well-formedness and interpretations](../data/basic.md)

## Proof depends on

- [Properties of interpretations on symbolic environments](../env/interpret.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/LitVar.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/LitVar.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.LitVar.json)
