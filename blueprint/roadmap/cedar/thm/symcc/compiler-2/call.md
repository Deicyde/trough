---
catalog: module
lean: Cedar.Thm.pe_duration_toMinutes, Cedar.Thm.compileCall_interpret, Cedar.Thm.compile_interpret_call, Cedar.Thm.compile_evaluate_call
statement: formalized
proof: formalized
---

# Compiler/Call

`Cedar.Thm.SymCC.Compiler.Call`, in [Cedar/Thm/SymCC/Compiler/Call.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Call.lean).

> This file proves the compilation lemmas for `.call` expressions.
> -

`Cedar.Thm.pe_duration_toMinutes` (theorem, [line 378](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Call.lean#L378))

```lean
theorem pe_duration_toMinutes {dur : Ext.Datetime.Duration} :
  Duration.toMinutes (.prim (.ext (Ext.duration dur))) = dur.toMinutes
```

`Cedar.Thm.compileCall_interpret` (theorem, [line 1136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Call.lean#L1136))

```lean
theorem compileCall_interpret {xfn : ExtFun} {ts : List Term} {t : Term} {I : Interpretation}
  (hI  : I.WellFormed εs)
  (hwφ : ∀ (t : Term), t ∈ ts → Term.WellFormed εs t)
  (hok : compileCall xfn ts = Except.ok t) :
  compileCall xfn (List.map (Term.interpret I) ts) = Except.ok (Term.interpret I t)
```

`Cedar.Thm.compile_interpret_call` (theorem, [line 1166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Call.lean#L1166))

```lean
theorem compile_interpret_call {f : ExtFun} {xs : List Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.call f xs))
  (hok : compile (.call f xs) εnv = .ok t)
  (ih  : ∀ x ∈ xs, CompileInterpret x) :
  compile (.call f xs) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_evaluate_call` (theorem, [line 1680](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Call.lean#L1680))

```lean
theorem compile_evaluate_call {f : ExtFun} {xs : List Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.call f xs))
  (hwε : εnv.WellFormedFor (.call f xs))
  (hok : compile (.call f xs) εnv = .ok t)
  (ih  : ∀ x ∈ xs, CompileEvaluate x) :
  evaluate (.call f xs) env.request env.entities ∼ t
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Args](args.md)
- [Extension function rewriting lemmas](../data/ext.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Call.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Call.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Call.json)
