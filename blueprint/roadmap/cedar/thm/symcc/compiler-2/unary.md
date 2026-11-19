---
catalog: module
lean: Cedar.Thm.compile_evaluate_unaryApp, Cedar.Thm.interpret_compileApp₁, Cedar.Thm.compile_interpret_unaryApp
statement: formalized
proof: formalized
---

# Compiler/Unary

`Cedar.Thm.SymCC.Compiler.Unary`, in [Cedar/Thm/SymCC/Compiler/Unary.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Unary.lean).

> This file proves the compilation lemmas for `.unaryApp` expressions.
> -

`Cedar.Thm.compile_evaluate_unaryApp` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Unary.lean#L98))

```lean
theorem compile_evaluate_unaryApp {op₁ : UnaryOp} {x₁ : Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.unaryApp op₁ x₁))
  (hwε : εnv.WellFormedFor (.unaryApp op₁ x₁))
  (hok : compile (.unaryApp op₁ x₁) εnv = .ok t)
  (ih  : CompileEvaluate x₁) :
  evaluate (.unaryApp op₁ x₁) env.request env.entities ∼ t
```

`Cedar.Thm.interpret_compileApp₁` (theorem, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Unary.lean#L126))

```lean
theorem interpret_compileApp₁ {op₁ : UnaryOp} {t t₁: Term} {εs : SymEntities} {I : Interpretation}
  (hI  : Interpretation.WellFormed I εs)
  (hwt : Term.WellFormed εs t₁)
  (hok : compileApp₁ op₁ t₁ = Except.ok t) :
  compileApp₁ op₁ (t₁.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_interpret_unaryApp` (theorem, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Unary.lean#L186))

```lean
theorem compile_interpret_unaryApp {op₁ : UnaryOp} {x₁ : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.unaryApp op₁ x₁))
  (hok : compile (.unaryApp op₁ x₁) εnv = .ok t)
  (ih  : CompileInterpret x₁) :
  compile (.unaryApp op₁ x₁) (εnv.interpret I) = .ok (t.interpret I)
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Compiler/WF](wf.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Unary.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Unary.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Unary.json)
