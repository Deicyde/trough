---
catalog: module
lean: Cedar.Thm.interpret_terms_wfls, Cedar.Thm.pe_interpret_terms_of_type_option, Cedar.Thm.compile_interpret_set, Cedar.Thm.compile_evaluate_set
statement: formalized
proof: formalized
---

# Compiler/Set

`Cedar.Thm.SymCC.Compiler.Set`, in [Cedar/Thm/SymCC/Compiler/Set.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Set.lean).

> This file proves the compilation lemmas for `.set` expressions.
> -

`Cedar.Thm.interpret_terms_wfls` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Set.lean#L30))

```lean
theorem interpret_terms_wfls {ts : List Term} {ty : TermType} {I : Interpretation} {εs : SymEntities}
  (hI  : Interpretation.WellFormed I εs)
  (hwφ : ∀ t ∈ ts, Term.WellFormed εs t)
  (hty : ∀ t ∈ ts, Term.typeOf t = ty) :
  ∀ t ∈ ts, (t.interpret I).WellFormedLiteral εs ∧ (t.interpret I).typeOf = ty
```

`Cedar.Thm.pe_interpret_terms_of_type_option` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Set.lean#L40))

```lean
theorem pe_interpret_terms_of_type_option {ts : List Term} {ty : TermType} {I : Interpretation} {εs : SymEntities}
  (hwi : ∀ t ∈ ts, (t.interpret I).WellFormedLiteral εs ∧ (t.interpret I).typeOf = .option ty) :
  (∃ ty, .none ty ∈ ts.map (Term.interpret I)) ∨
  (∃ ts', List.map (Term.interpret I) ts = List.map Term.some ts')
```

`Cedar.Thm.compile_interpret_set` (theorem, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Set.lean#L100))

```lean
theorem compile_interpret_set {xs : List Expr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.set xs))
  (hok : compile (.set xs) εnv = .ok t)
  (ih  : ∀ x ∈ xs, CompileInterpret x) :
  compile (.set xs) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_evaluate_set` (theorem, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Set.lean#L202))

```lean
theorem compile_evaluate_set {xs : List Expr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.set xs))
  (hwε : εnv.WellFormedFor (.set xs))
  (hok : compile (.set xs) εnv = .ok t)
  (ih  : ∀ x ∈ xs, CompileEvaluate x) :
  evaluate (.set xs) env.request env.entities ∼ t
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Args](args.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Set.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Set.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Set.json)
