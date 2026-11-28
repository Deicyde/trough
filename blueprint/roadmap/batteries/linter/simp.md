---
catalog: module
lean: Batteries.Linter.SimpTheoremInfo, Batteries.Linter.isCondition, Batteries.Linter.withSimpTheoremInfos, Batteries.Linter.isSimpEq, Batteries.Linter.checkAllSimpTheoremInfos, Batteries.Linter.isSimpTheorem, Lean.Meta.DiscrTree.elements, Batteries.Linter.decorateError, Batteries.Linter.formatLemmas, Batteries.Linter.simpNF, Batteries.Linter.simpComm, Batteries.Tactic.Lint.SimpTheoremInfo, Batteries.Tactic.Lint.SimpTheoremInfo.mk, Batteries.Tactic.Lint.SimpTheoremInfo.hyps, Batteries.Tactic.Lint.SimpTheoremInfo.lhs, Batteries.Tactic.Lint.SimpTheoremInfo.rhs, Batteries.Tactic.Lint.isCondition, Batteries.Tactic.Lint.withSimpTheoremInfos, Batteries.Tactic.Lint.checkAllSimpTheoremInfos, Batteries.Tactic.Lint.isSimpTheorem, Batteries.Tactic.Lint.isSimpEq, Batteries.Tactic.Lint.decorateError, Batteries.Tactic.Lint.formatLemmas, Batteries.Tactic.Lint.linter.simpNF.respectTransparency, Batteries.Tactic.Lint.simpNF, Batteries.Tactic.Lint.simpComm
statement: formalized
proof: formalized
---

# Linter for simplification lemmas

`Batteries.Linter.Simp`, in [Batteries/Linter/Simp.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean), by Gabriel Ebner.

> This files defines several linters that prevent common mistakes when declaring simp lemmas:
>
>  * `simpNF` checks that the left-hand side of a simp lemma is not simplified by a different lemma.
>  * `simpComm` checks that commutativity lemmas are not marked as simplification lemmas.

`Batteries.Linter.SimpTheoremInfo` (structure, [line 31](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L31))

> The data associated to a simp theorem.

```lean
structure SimpTheoremInfo where
  /-- The hypotheses of the theorem -/
  hyps : Array Expr
  /-- The thing to replace -/
  lhs : Expr
  /-- The result of replacement -/
  rhs : Expr
```

`Batteries.Linter.isCondition` (definition, [line 41](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L41))

> Is this hypothesis a condition that might turn into a `simp` side-goal?
> i.e. is it a proposition that isn't marked as instance implicit?

```lean
def isCondition (h : Expr) : MetaM Bool
```

`Batteries.Linter.withSimpTheoremInfos` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L47))

> Runs the continuation on all the simp theorems encoded in the given type.

```lean
def withSimpTheoremInfos (ty : Expr) (k : SimpTheoremInfo → MetaM α) : MetaM (Array α)
```

`Batteries.Linter.isSimpEq` (definition, [line 78](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L78))

> Checks whether two expressions are equal for the simplifier. That is,
> they are reducibly-definitional equal, and they have the same head symbol.

```lean
def isSimpEq (a b : Expr) (whnfFirst := true) : MetaM Bool
```

`Batteries.Linter.checkAllSimpTheoremInfos` (definition, [line 92](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L92))

> Constructs a message from all the simp theorems encoded in the given type.

```lean
def checkAllSimpTheoremInfos (ty : Expr) (k : SimpTheoremInfo → MetaM (Option MessageData)) :
    MetaM (Option MessageData)
```

`Batteries.Linter.isSimpTheorem` (definition, [line 101](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L101))

> Returns true if this is a `@[simp]` declaration.

```lean
def isSimpTheorem (declName : Name) : MetaM Bool
```

`Lean.Meta.DiscrTree.elements` (definition, [line 107](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L107))

> Returns the list of elements in the discrimination tree.

```lean
partial def _root_.Lean.Meta.DiscrTree.elements (d : DiscrTree α) : Array α
```

`Batteries.Linter.decorateError` (definition, [line 111](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L111))

> Add message `msg` to any errors thrown inside `k`.

```lean
def decorateError (msg : MessageData) (k : MetaM α) : MetaM α
```

`Batteries.Linter.formatLemmas` (definition, [line 115](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L115))

> Render the list of simp lemmas.

```lean
def formatLemmas (usedSimps : Simp.UsedSimps) (simpName : String) (higherOrder : Option Bool) :
    MetaM MessageData
```

`Batteries.Linter.simpNF` (definition, [line 127](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L127))

> A linter for simp lemmas whose lhs is not in simp-normal form, and which hence never fire.

```lean
def simpNF : Linter
```

`Batteries.Linter.simpComm` (definition, [line 278](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L278))

> A linter for commutativity lemmas that are marked simp.

```lean
def simpComm : Linter
```

> Deprecated aliases for the former `Batteries.Tactic.Lint` namespace.

`Batteries.Tactic.Lint.SimpTheoremInfo` (abbreviation, [line 307](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L307))

> Deprecated alias of `Batteries.Linter.SimpTheoremInfo`.

```lean
abbrev SimpTheoremInfo
```

`Batteries.Tactic.Lint.SimpTheoremInfo.mk` (alias, [line 310](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L310))

```lean
alias SimpTheoremInfo.mk
```

`Batteries.Tactic.Lint.SimpTheoremInfo.hyps` (alias, [line 312](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L312))

```lean
alias SimpTheoremInfo.hyps
```

`Batteries.Tactic.Lint.SimpTheoremInfo.lhs` (alias, [line 314](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L314))

```lean
alias SimpTheoremInfo.lhs
```

`Batteries.Tactic.Lint.SimpTheoremInfo.rhs` (alias, [line 316](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L316))

```lean
alias SimpTheoremInfo.rhs
```

`Batteries.Tactic.Lint.isCondition` (alias, [line 318](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L318))

```lean
alias isCondition
```

`Batteries.Tactic.Lint.withSimpTheoremInfos` (alias, [line 320](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L320))

```lean
alias withSimpTheoremInfos
```

`Batteries.Tactic.Lint.checkAllSimpTheoremInfos` (alias, [line 322](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L322))

```lean
alias checkAllSimpTheoremInfos
```

`Batteries.Tactic.Lint.isSimpTheorem` (alias, [line 324](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L324))

```lean
alias isSimpTheorem
```

`Batteries.Tactic.Lint.isSimpEq` (alias, [line 326](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L326))

```lean
alias isSimpEq
```

`Batteries.Tactic.Lint.decorateError` (alias, [line 328](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L328))

```lean
alias decorateError
```

`Batteries.Tactic.Lint.formatLemmas` (alias, [line 330](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L330))

```lean
alias formatLemmas
```

`Batteries.Tactic.Lint.linter.simpNF.respectTransparency` (alias, [line 332](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L332))

```lean
alias linter.simpNF.respectTransparency
```

`Batteries.Tactic.Lint.simpNF` (alias, [line 334](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L334))

```lean
alias simpNF
```

`Batteries.Tactic.Lint.simpComm` (alias, [line 336](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean#L336))

```lean
alias simpComm
```

## Depends on

- [Basic linter types and attributes](basic.md)
- [Define the `library_note` command](../util/librarynote.md)

## Sources

- [Batteries/Linter/Simp.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/Simp.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Linter.Simp.json)
