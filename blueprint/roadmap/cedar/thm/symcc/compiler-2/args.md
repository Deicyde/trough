---
catalog: module
lean: Cedar.Thm.compile_wfs, Cedar.Thm.compile_interpret_ihs, Cedar.Thm.compile_interpret_args_not_error, Cedar.Thm.compile_interpret_terms, Cedar.Thm.compile_evaluate_ihs
statement: formalized
proof: formalized
---

# Args

`Cedar.Thm.SymCC.Compiler.Args`, in [Cedar/Thm/SymCC/Compiler/Args.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean).

> This file contains utility lemmas for proving compilation theorems
> about lists of argument terms.
> -

`Cedar.Thm.compile_wfs` (theorem, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean#L29))

```lean
theorem compile_wfs {xs : List Expr} {εnv : SymEnv} {ts : List Term}
  (hwφ : ∀ (x : Expr), x ∈ xs → SymEnv.WellFormedFor εnv x)
  (hok : List.Forall₂ (λ x t => compile x εnv = Except.ok t) xs ts) :
  ∀ t ∈ ts, t.WellFormed εnv.entities
```

`Cedar.Thm.compile_interpret_ihs` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean#L38))

```lean
theorem compile_interpret_ihs {xs : List Expr} {εnv : SymEnv} {I : Interpretation} {ts : List Term}
  (hI  : Interpretation.WellFormed I εnv.entities)
  (hwε : ∀ (x : Expr), x ∈ xs → SymEnv.WellFormedFor εnv x)
  (ih  : ∀ (x : Expr), x ∈ xs → CompileInterpret x)
  (hok : List.Forall₂ (fun x t => compile x εnv = Except.ok t) xs ts) :
  List.Forall₂ (fun x t => compile x (SymEnv.interpret I εnv) = Except.ok (Term.interpret I t)) xs ts
```

`Cedar.Thm.compile_interpret_args_not_error` (theorem, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean#L59))

```lean
theorem compile_interpret_args_not_error {εnv : SymEnv} {I : Interpretation} {xs : List Expr} {ts : List Term} {e : SymCC.Error} :
  List.Forall₂ (fun x t => compile x (SymEnv.interpret I εnv) = Except.ok (Term.interpret I t)) xs ts →
  List.mapM (fun x => compile x (SymEnv.interpret I εnv)) xs = Except.error e →
  False
```

`Cedar.Thm.compile_interpret_terms` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean#L69))

```lean
theorem compile_interpret_terms {xs : List Expr} {εnv : SymEnv} {I : Interpretation} {ts ts' : List Term}
  (h₁ : List.Forall₂ (λ x t => compile x (SymEnv.interpret I εnv) = Except.ok (Term.interpret I t)) xs ts)
  (h₂ : List.Forall₂ (λ x t => compile x (SymEnv.interpret I εnv) = Except.ok t) xs ts') :
  List.Forall₂ (λ t t' => Term.interpret I t = t') ts ts'
```

`Cedar.Thm.compile_evaluate_ihs` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean#L79))

```lean
theorem compile_evaluate_ihs {xs : List Expr} {env : Env} {εnv : SymEnv}
  (heq : env ∼ εnv)
  (hwe : ∀ (x : Expr), x ∈ xs → env.WellFormedFor x)
  (hwε : ∀ (x : Expr), x ∈ xs → εnv.WellFormedFor x)
  (ih  : ∀ (x : Expr), x ∈ xs → CompileEvaluate x)
  (hok : List.Forall₂ (fun x t => compile x εnv = Except.ok t) xs ts) :
  List.Forall₂ (fun x t => evaluate x env.request env.entities ∼ t) xs ts
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Compiler/WF](wf.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Args.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Args.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Args.json)
