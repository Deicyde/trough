---
catalog: module
lean: Batteries.Tactic.Lint.SimpTheoremInfo, Batteries.Tactic.Lint.isCondition, Batteries.Tactic.Lint.withSimpTheoremInfos, Batteries.Tactic.Lint.isSimpEq, Batteries.Tactic.Lint.checkAllSimpTheoremInfos, Batteries.Tactic.Lint.isSimpTheorem, Lean.Meta.DiscrTree.elements, Batteries.Tactic.Lint.decorateError, Batteries.Tactic.Lint.formatLemmas, Batteries.Tactic.Lint.simpNF, Batteries.Tactic.Lint.simpComm
statement: formalized
proof: formalized
---

# Linter for simplification lemmas

`Batteries.Tactic.Lint.Simp`, in [Batteries/Tactic/Lint/Simp.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean), by Gabriel Ebner.

> This files defines several linters that prevent common mistakes when declaring simp lemmas:
>
>  * `simpNF` checks that the left-hand side of a simp lemma is not simplified by a different lemma.
>  * `simpComm` checks that commutativity lemmas are not marked as simplification lemmas.

`Batteries.Tactic.Lint.SimpTheoremInfo` (structure, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L30))

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

`Batteries.Tactic.Lint.isCondition` (definition, [line 40](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L40))

> Is this hypothesis a condition that might turn into a `simp` side-goal?
> i.e. is it a proposition that isn't marked as instance implicit?

```lean
def isCondition (h : Expr) : MetaM Bool
```

`Batteries.Tactic.Lint.withSimpTheoremInfos` (definition, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L46))

> Runs the continuation on all the simp theorems encoded in the given type.

```lean
def withSimpTheoremInfos (ty : Expr) (k : SimpTheoremInfo → MetaM α) : MetaM (Array α)
```

`Batteries.Tactic.Lint.isSimpEq` (definition, [line 77](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L77))

> Checks whether two expressions are equal for the simplifier. That is,
> they are reducibly-definitional equal, and they have the same head symbol.

```lean
def isSimpEq (a b : Expr) (whnfFirst := true) : MetaM Bool
```

`Batteries.Tactic.Lint.checkAllSimpTheoremInfos` (definition, [line 91](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L91))

> Constructs a message from all the simp theorems encoded in the given type.

```lean
def checkAllSimpTheoremInfos (ty : Expr) (k : SimpTheoremInfo → MetaM (Option MessageData)) :
    MetaM (Option MessageData)
```

`Batteries.Tactic.Lint.isSimpTheorem` (definition, [line 100](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L100))

> Returns true if this is a `@[simp]` declaration.

```lean
def isSimpTheorem (declName : Name) : MetaM Bool
```

`Lean.Meta.DiscrTree.elements` (definition, [line 106](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L106))

> Returns the list of elements in the discrimination tree.

```lean
partial def _root_.Lean.Meta.DiscrTree.elements (d : DiscrTree α) : Array α
```

`Batteries.Tactic.Lint.decorateError` (definition, [line 110](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L110))

> Add message `msg` to any errors thrown inside `k`.

```lean
def decorateError (msg : MessageData) (k : MetaM α) : MetaM α
```

`Batteries.Tactic.Lint.formatLemmas` (definition, [line 114](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L114))

> Render the list of simp lemmas.

```lean
def formatLemmas (usedSimps : Simp.UsedSimps) (simpName : String) (higherOrder : Option Bool) :
    MetaM MessageData
```

`Batteries.Tactic.Lint.simpNF` (definition, [line 126](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L126))

> A linter for simp lemmas whose lhs is not in simp-normal form, and which hence never fire.

```lean
def simpNF : Linter
```

`Batteries.Tactic.Lint.simpComm` (definition, [line 277](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean#L277))

> A linter for commutativity lemmas that are marked simp.

```lean
def simpComm : Linter
```

## Depends on

- [Basic linter types and attributes](basic.md)
- [Define the `library_note` command](../../util/librarynote.md)

## Sources

- [Batteries/Tactic/Lint/Simp.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/Simp.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Tactic.Lint.Simp.json)
