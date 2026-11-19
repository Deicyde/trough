---
catalog: module
lean: Cedar.Thm.CompileEvaluate, Cedar.Thm.CompileInterpret
statement: formalized
proof: formalized
---

# Compiler/Basic

`Cedar.Thm.SymCC.Compiler.Basic`, in [Cedar/Thm/SymCC/Compiler/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Basic.lean).

> This file contains basic definitions for proofs about `compile`.
> -

`Cedar.Thm.CompileEvaluate` (definition, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Basic.lean#L31))

```lean
public def CompileEvaluate (x : Expr) : Prop
```

`Cedar.Thm.CompileInterpret` (definition, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Basic.lean#L40))

```lean
public def CompileInterpret (x : Expr) : Prop
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [Well-formedness and interpretations](../data/basic.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/Basic.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.Basic.json)
