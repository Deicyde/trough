---
catalog: module
lean: Lean.Meta.evalExprWithSorryCheck
statement: formalized
---

# Eval

`Batteries.Util.Eval`, in [Batteries/Util/Eval.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Eval.lean), by Robin Arnez.

`Lean.Meta.evalExprWithSorryCheck` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Eval.lean#L20)). Its value holds `sorry`.

> An alternative of `evalExpr` that also errors in the presence of `sorry` unless `allowSorry` is
> true. If there is an alternative command that does allow `sorry`s, you can specify it in
> `alternative?`.

```lean
unsafe def Lean.Meta.evalExprWithSorryCheck (α) (type value : Expr)
    (safety := DefinitionSafety.safe) (checkMeta : Bool := true)
    (allowSorry : Bool := false) (alternative? : Option String := none) : MetaM α
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/Eval.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Util/Eval.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Util.Eval.json)
