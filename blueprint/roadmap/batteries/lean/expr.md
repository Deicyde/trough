---
catalog: module
lean: Lean.Expr.toSyntax, Lean.Expr.withApp', Lean.Expr.getAppArgs', Lean.Expr.traverseApp', Lean.Expr.withAppRev', Lean.Expr.getAppRevArgs', Lean.Expr.getRevArgD', Lean.Expr.getArgD', Lean.Expr.isAppOf', Lean.Expr.natLit!, Lean.Expr.intLit!, Lean.Expr.addLocalVarInfoForBinderIdent
statement: formalized
proof: formalized
---

# Additional operations on Expr and related types

`Batteries.Lean.Expr`, in [Batteries/Lean/Expr.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean), by Mario Carneiro.

> This file defines basic operations on the types expr, name, declaration, level, environment.
>
> This file is mostly for non-tactics.

`Lean.Expr.toSyntax` (definition, [line 25](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L25))

> Converts an `Expr` into a `Syntax`, by creating a fresh metavariable
> assigned to the expr and  returning a named metavariable syntax `?a`.

```lean
def toSyntax (e : Expr) : TermElabM Syntax.Term
```

`Lean.Expr.withApp'` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L33))

> Like `withApp` but ignores metadata.

```lean
def withApp' (e : Expr) (k : Expr → Array Expr → α) : α
```

`Lean.Expr.getAppArgs'` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L47))

> Like `getAppArgs` but ignores metadata.

```lean
def getAppArgs' (e : Expr) : Array Expr
```

`Lean.Expr.traverseApp'` (definition, [line 51](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L51))

> Like `traverseApp` but ignores metadata.

```lean
def traverseApp' {m} [Monad m]
  (f : Expr → m Expr) (e : Expr) : m Expr
```

`Lean.Expr.withAppRev'` (definition, [line 57](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L57))

> Like `withAppRev` but ignores metadata.

```lean
def withAppRev' (e : Expr) (k : Expr → Array Expr → α) : α
```

`Lean.Expr.getAppRevArgs'` (definition, [line 69](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L69))

> Like `getAppRevArgs` but ignores metadata.

```lean
def getAppRevArgs' (e : Expr) : Array Expr
```

`Lean.Expr.getRevArgD'` (definition, [line 73](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L73))

> Like `getRevArgD` but ignores metadata.

```lean
def getRevArgD' : Expr → Nat → Expr → Expr
```

`Lean.Expr.getArgD'` (definition, [line 81](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L81))

> Like `getArgD` but ignores metadata.

```lean
def getArgD' (e : Expr) (i : Nat) (v₀ : Expr) (n := e.getAppNumArgs') : Expr
```

`Lean.Expr.isAppOf'` (definition, [line 85](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L85))

> Like `isAppOf` but ignores metadata.

```lean
def isAppOf' (e : Expr) (n : Name) : Bool
```

`Lean.Expr.natLit!` (definition, [line 91](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L91))

> Turns an expression that is a natural number literal into a natural number.

```lean
def natLit! : Expr → Nat
```

`Lean.Expr.intLit!` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L97))

> Turns an expression that is a constructor of `Int` applied to a natural number literal
> into an integer.

```lean
def intLit! (e : Expr) : Int
```

`Lean.Expr.addLocalVarInfoForBinderIdent` (definition, [line 108](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean#L108))

> Annotates a `binderIdent` with the binder information from an `fvar`.

```lean
def addLocalVarInfoForBinderIdent (fvar : Expr) (tk : TSyntax ``binderIdent) : MetaM Unit
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Expr.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/Expr.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.Expr.json)
