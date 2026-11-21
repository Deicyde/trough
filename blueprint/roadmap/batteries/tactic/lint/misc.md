---
catalog: module
lean: Batteries.Tactic.Lint.unusedArguments, Batteries.Tactic.Lint.docBlame, Batteries.Tactic.Lint.docBlameThm, Batteries.Tactic.Lint.checkType, Batteries.Tactic.Lint.synTaut, Batteries.Tactic.Lint.findUnusedHaves, Batteries.Tactic.Lint.unusedHavesSuffices, Batteries.Tactic.Lint.explicitVarsOfIff
statement: formalized
proof: formalized
---

# Various linters

`Batteries.Tactic.Lint.Misc`, in [Batteries/Tactic/Lint/Misc.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean), by Floris van Doorn, Robert Y. Lewis, Arthur Paulino, Gabriel Ebner.

> This file defines several small linters.

`Batteries.Tactic.Lint.unusedArguments` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L29))

> A linter for checking for unused arguments. We skip all declarations that contain `sorry` in
> their value, and allow arguments starting with `_` to be unused.

```lean
def unusedArguments : Linter
```

`Batteries.Tactic.Lint.docBlame` (definition, [line 83](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L83))

> A linter for checking definition doc strings.

```lean
def docBlame : Linter
```

`Batteries.Tactic.Lint.docBlameThm` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L111))

> A linter for checking theorem doc strings.

```lean
def docBlameThm : Linter
```

`Batteries.Tactic.Lint.checkType` (definition, [line 132](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L132))

> A linter for checking whether statements of declarations are well-typed.

```lean
def checkType : Linter
```

`Batteries.Tactic.Lint.synTaut` (definition, [line 149](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L149))

> A linter for checking that declarations aren't syntactic tautologies.
> Checks whether a lemma is a declaration of the form `∀ a b ... z, e₁ = e₂`
> where `e₁` and `e₂` are identical exprs.
> We call declarations of this form syntactic tautologies.
> Such lemmas are (mostly) useless and sometimes introduced unintentionally when proving basic facts
> with rfl when elaboration results in a different term than the user intended.

```lean
def synTaut : Linter
```

`Batteries.Tactic.Lint.findUnusedHaves` (definition, [line 174](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L174))

> Return a list of unused `let_fun` terms in an expression that introduce proofs.

```lean
def findUnusedHaves (_ : Expr) : MetaM (Array MessageData)
```

`Batteries.Tactic.Lint.unusedHavesSuffices` (definition, [line 194](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L194))

> A linter for checking that declarations don't have unused term mode have statements.

```lean
def unusedHavesSuffices : Linter
```

`Batteries.Tactic.Lint.explicitVarsOfIff` (definition, [line 221](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean#L221))

> A linter for checking if variables appearing on both sides of an iff are explicit. Ideally, such
> variables should be implicit instead.

```lean
def explicitVarsOfIff : Linter
```

## Depends on

- [Basic linter types and attributes](basic.md)

## Sources

- [Batteries/Tactic/Lint/Misc.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/Lint/Misc.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Tactic.Lint.Misc.json)
