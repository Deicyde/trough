---
catalog: module
lean: Cedar.Thm.compile_evaluate_extHasAttr, Cedar.Thm.compile_interpret_extHasAttr
statement: formalized
proof: formalized
---

# Compiler/ExtHasAttr

`Cedar.Thm.SymCC.Compiler.ExtHasAttr`, in [Cedar/Thm/SymCC/Compiler/ExtHasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttr.lean).

`Cedar.Thm.compile_evaluate_extHasAttr` (theorem, [line 394](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttr.lean#L394))

```lean
theorem compile_evaluate_extHasAttr {x₁ : Expr} {a : Attr} {l : List Attr} {env : Env} {εnv : SymEnv} {t : Term}
  (heq : env ∼ εnv)
  (hwe : env.WellFormedFor (.extHasAttr x₁ a l))
  (hwε : εnv.WellFormedFor (.extHasAttr x₁ a l))
  (hok : compile (.extHasAttr x₁ a l) εnv = .ok t)
  (ih  : CompileEvaluate x₁) :
  evaluate (.extHasAttr x₁ a l) env.request env.entities ∼ t
```

`Cedar.Thm.compile_interpret_extHasAttr` (theorem, [line 653](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttr.lean#L653))

```lean
theorem compile_interpret_extHasAttr {x₁ : Expr} {a : Attr} {l : List Attr} {εnv : SymEnv} {I : Interpretation} {t : Term}
  (hI  : I.WellFormed εnv.entities)
  (hwε : εnv.WellFormedFor (.extHasAttr x₁ a l))
  (hok : compile (.extHasAttr x₁ a l) εnv = .ok t)
  (ih  : CompileInterpret x₁) :
  compile (.extHasAttr x₁ a l) (εnv.interpret I) = .ok (t.interpret I)
```

## Depends on

- [Compiler/Basic](basic.md)

## Proof depends on

- [Authorization/Authorizer](../../authorization-2/authorizer.md)
- [Attr](attr.md)

## Sources

- [Cedar/Thm/SymCC/Compiler/ExtHasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Compiler/ExtHasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Compiler.ExtHasAttr.json)
