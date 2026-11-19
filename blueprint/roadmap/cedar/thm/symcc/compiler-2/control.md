---
catalog: module
lean: Cedar.Thm.compile_evaluate_ite, Cedar.Thm.compile_interpret_ite, Cedar.Thm.compile_evaluate_and, Cedar.Thm.compile_interpret_and, Cedar.Thm.compile_evaluate_or, Cedar.Thm.compile_interpret_or
statement: formalized
proof: formalized
---

# Compiler/Control

`Cedar.Thm.SymCC.Compiler.Control`, in [Cedar/Thm/SymCC/Compiler/Control.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean).

> This file proves the compilation lemmas for `.ite`, `.and`, and `.or` expressions.
> -

`Cedar.Thm.compile_evaluate_ite` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean#L52))

```lean
theorem compile_evaluate_ite {x₁ x₂ x₃ : Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (h₁  : env ∼ εnv)
  (h₂  : env.WellFormedFor (.ite x₁ x₂ x₃))
  (h₃  : εnv.WellFormedFor (.ite x₁ x₂ x₃))
  (h₄  : compile (.ite x₁ x₂ x₃) εnv = .ok t)
  (ih₁ : CompileEvaluate x₁)
  (ih₂ : CompileEvaluate x₂)
  (ih₃ : CompileEvaluate x₃) :
  evaluate (.ite x₁ x₂ x₃) env.request env.entities ∼ t
```

`Cedar.Thm.compile_interpret_ite` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean#L112))

```lean
theorem compile_interpret_ite {x₁ x₂ x₃ : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (h₁  : I.WellFormed εnv.entities)
  (h₂  : εnv.WellFormedFor (.ite x₁ x₂ x₃))
  (h₃  : compile (.ite x₁ x₂ x₃) εnv = .ok t)
  (ih₁ : CompileInterpret x₁)
  (ih₂ : CompileInterpret x₂)
  (ih₃ : CompileInterpret x₃) :
  compile (.ite x₁ x₂ x₃) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_evaluate_and` (theorem, [line 232](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean#L232))

```lean
theorem compile_evaluate_and {x₁ x₂ : Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (h₁  : env ∼ εnv)
  (h₂  : env.WellFormedFor (.and x₁ x₂))
  (h₃  : εnv.WellFormedFor (.and x₁ x₂))
  (h₄  : compile (.and x₁ x₂) εnv = .ok t)
  (ih₁ : CompileEvaluate x₁)
  (ih₂ : CompileEvaluate x₂) :
  evaluate (.and x₁ x₂) env.request env.entities ∼ t
```

`Cedar.Thm.compile_interpret_and` (theorem, [line 289](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean#L289))

```lean
theorem compile_interpret_and {x₁ x₂ : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (h₁  : I.WellFormed εnv.entities)
  (h₂  : εnv.WellFormedFor (.and x₁ x₂))
  (h₃  : compile (.and x₁ x₂) εnv = .ok t)
  (ih₁ : CompileInterpret x₁)
  (ih₂ : CompileInterpret x₂) :
  compile (.and x₁ x₂) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_evaluate_or` (theorem, [line 388](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean#L388))

```lean
theorem compile_evaluate_or {x₁ x₂ : Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (h₁  : env ∼ εnv)
  (h₂  : env.WellFormedFor (.or x₁ x₂))
  (h₃  : εnv.WellFormedFor (.or x₁ x₂))
  (h₄  : compile (.or x₁ x₂) εnv = .ok t)
  (ih₁ : CompileEvaluate x₁)
  (ih₂ : CompileEvaluate x₂) :
  evaluate (.or x₁ x₂) env.request env.entities ∼ t
```

`Cedar.Thm.compile_interpret_or` (theorem, [line 445](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean#L445))

```lean
theorem compile_interpret_or {x₁ x₂ : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (h₁  : I.WellFormed εnv.entities)
  (h₂  : εnv.WellFormedFor (.or x₁ x₂))
  (h₃  : compile (.or x₁ x₂) εnv = .ok t)
  (ih₁ : CompileInterpret x₁)
  (ih₂ : CompileInterpret x₂) :
  compile (.or x₁ x₂) (εnv.interpret I) = .ok (t.interpret I)
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Compiler/WF](wf.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Control.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Control.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Control.json)
