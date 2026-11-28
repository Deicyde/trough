---
catalog: module
lean: Lean.Meta.Simp.mkEqSymm, Lean.Meta.Simp.mkCast, Lean.Meta.Simp.mkDischargeWrapper, Lean.Meta.Simp.mkSimpContext'
statement: formalized
proof: formalized
---

# Helper functions for using the simplifier

`Batteries.Lean.Meta.Simp`, in [Batteries/Lean/Meta/Simp.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Simp.lean), by Kim Morrison, Gabriel Ebner, Floris van Doorn.

> …

`Lean.Meta.Simp.mkEqSymm` (definition, [line 26](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Simp.lean#L26))

> Flip the proof in a `Simp.Result`.

```lean
def mkEqSymm (e : Expr) (r : Simp.Result) : MetaM Simp.Result
```

`Lean.Meta.Simp.mkCast` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Simp.lean#L33))

> Construct the `Expr` `cast h e`, from a `Simp.Result` with proof `h`.

```lean
def mkCast (r : Simp.Result) (e : Expr) : MetaM Expr
```

`Lean.Meta.Simp.mkDischargeWrapper` (definition, [line 37](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Simp.lean#L37))

> Construct a `Simp.DischargeWrapper` from the `Syntax` for a `simp` discharger.

```lean
nonrec def mkDischargeWrapper
```

`Lean.Meta.Simp.mkSimpContext'` (definition, [line 45](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Simp.lean#L45))

> If `ctx == false`, the config argument is assumed to have type `Meta.Simp.Config`,
> and `Meta.Simp.ConfigCtx` otherwise.
> If `ctx == false`, the `discharge` option must be none

```lean
def mkSimpContext' (simpTheorems : SimpTheorems) (stx : Syntax) (eraseLocal : Bool)
    (kind := SimpKind.simp) (ctx := false) (ignoreStarArg : Bool := false) :
    TacticM MkSimpContextResult
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Meta/Simp.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Lean/Meta/Simp.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Meta.Simp.json)
