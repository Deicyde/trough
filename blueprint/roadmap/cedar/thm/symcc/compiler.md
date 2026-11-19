---
catalog: module
lean: Cedar.Thm.compile_evaluate, Cedar.Thm.compile_interpret, Cedar.Thm.compile_bisimulation
statement: formalized
proof: formalized
---

# Thm/SymCC/Compiler

`Cedar.Thm.SymCC.Compiler`, in [Cedar/Thm/SymCC/Compiler.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler.lean).

> This file proves two key auxiliary lemmas used to show the soundness
> and completeness of Cedar's symbolic compiler.
> -

`Cedar.Thm.compile_evaluate` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler.lean#L48))

> The lemma shows that the symbolic compiler (`compile`) behaves like the
> concrete evaluator (`evaluate`) on literal inputs.
>
> In particular, let `x` be an expression, `εnv` a well-formed symbolic
> environment for `x`, and `env` a well-formed concrete environment for `x` that
> is equivalent to `εnv`. Then, the result produced by the symbolic compiler on
> `x` and `εnv` is equivalent to the result produced by the concrete evaluator `x`
> and `env`.

```lean
theorem compile_evaluate {x : Expr} {env : Env} {εnv : SymEnv} {t : Term} :
  env ∼ εnv →
  env.WellFormedFor x →
  εnv.WellFormedFor x →
  compile x εnv = .ok t →
  evaluate x env.request env.entities ∼ t
```

`Cedar.Thm.compile_interpret` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler.lean#L112))

> The lemma shows that `interpret` and `compile` can be applied in any order to get
> the same result. In particular, let `x` be an expression, `εnv` a well-formed
> symbolic environment for `x`, and `I` a well-formed interpretion for `εnv`.
> Then, compiling `x` with respect to `(εnv.interpret I)` gives the same result as
> interpreting the output of compiling `x` with respect to `εnv`.

```lean
theorem compile_interpret {x : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term} :
  I.WellFormed εnv.entities →
  εnv.WellFormedFor x →
  compile x εnv = .ok t →
  compile x (εnv.interpret I) = .ok (t.interpret I)
```

`Cedar.Thm.compile_bisimulation` (theorem, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler.lean#L168))

```lean
theorem compile_bisimulation {x : Expr} {env : Env} {εnv : SymEnv} {t : Term} {I : Interpretation} :
  εnv.WellFormedFor x →
  env.WellFormedFor x →
  I.WellFormed εnv.entities →
  env ∼ εnv.interpret I →
  compile x εnv = .ok t →
  evaluate x env.request env.entities ∼ t.interpret I
```

## Depends on

- [Spec/Evaluator](../../spec/evaluator.md)
- [Well-formedness and interpretations](data/basic.md)

## Proof depends on

- [Compiler/Binary](compiler-2/binary.md)
- [Compiler/Call](compiler-2/call.md)
- [Compiler/Control](compiler-2/control.md)
- [Compiler/ExtHasAttr](compiler-2/exthasattr.md)
- [Compiler/LitVar](compiler-2/litvar.md)
- [Compiler/Record](compiler-2/record.md)
- [Compiler/Set](compiler-2/set.md)
- [Compiler/Unary](compiler-2/unary.md)

## Sources

- [Cedar/Thm/SymCC/Compiler.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.json)
