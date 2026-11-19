---
catalog: module
lean: Cedar.Thm.compile_attr_expr_wfs, Cedar.Thm.prod_map_id_comp_eq, Cedar.Thm.interpret_attr_terms_wfls, Cedar.Thm.compile_interpret_record, Cedar.Thm.compile_evaluate_record
statement: formalized
proof: formalized
---

# Compiler/Record

`Cedar.Thm.SymCC.Compiler.Record`, in [Cedar/Thm/SymCC/Compiler/Record.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean).

> This file proves the compilation lemmas for `.record` expressions.
> -

`Cedar.Thm.compile_attr_expr_wfs` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean#L30))

```lean
theorem compile_attr_expr_wfs {εnv : SymEnv} {axs : List (Attr × Expr)} {ats : List (Attr × Term)}
  (hwε : ∀ (ax : Attr × Expr), ax ∈ axs → SymEnv.WellFormedFor εnv ax.snd)
  (hok : List.Forall₂ (λ px pt => px.fst = pt.fst ∧ compile px.snd εnv = Except.ok pt.snd) axs ats) :
  ∀ a t, (a, t) ∈ ats → t.WellFormed εnv.entities ∧ ∃ ty, t.typeOf = .option ty
```

`Cedar.Thm.prod_map_id_comp_eq` (theorem, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean#L94))

```lean
theorem prod_map_id_comp_eq {f g : β → β} :
  Prod.map (@id α) f ∘ Prod.map id g = Prod.map id (f ∘ g)
```

`Cedar.Thm.interpret_attr_terms_wfls` (theorem, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean#L139))

```lean
theorem interpret_attr_terms_wfls {ats : List (Attr × Term)} {I : Interpretation} {εs : SymEntities}
  (hI  : Interpretation.WellFormed I εs)
  (hwφ : ∀ a t, (a, t) ∈ ats → Term.WellFormed εs t ∧ ∃ ty, Term.typeOf t = TermType.option ty) :
  ∀ t ∈ ats.map (Term.interpret I ∘ Prod.snd),
    Term.WellFormedLiteral εs t ∧ ∃ ty, Term.typeOf t = TermType.option ty
```

`Cedar.Thm.compile_interpret_record` (theorem, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean#L171))

```lean
theorem compile_interpret_record {axs : List (Attr × Expr)} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.record axs))
  (hok : compile (.record axs) εnv = .ok t)
  (ih  : ∀ a x, (a, x) ∈ axs → CompileInterpret x) :
  compile (.record axs) (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_evaluate_record` (theorem, [line 289](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean#L289))

```lean
theorem compile_evaluate_record {axs : List (Attr × Expr)} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.record axs))
  (hwε : εnv.WellFormedFor (.record axs))
  (hok : compile (.record axs) εnv = .ok t)
  (ih  : ∀ a x, (a, x) ∈ axs → CompileEvaluate x) :
  evaluate (.record axs) env.request env.entities ∼ t
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Compiler/WF](wf.md)
- [Interpretation of Factory functions](../term/interpret/factory.md)
- [Properties of the `Same` predicate on Terms](../term/same.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Record.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Record.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Record.json)
