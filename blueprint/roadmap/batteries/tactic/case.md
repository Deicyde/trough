---
catalog: module
lean: Batteries.Tactic.findGoalOfPatt, Batteries.Tactic.processCasePattBody, Batteries.Tactic.evalCase
statement: formalized
proof: formalized
---

# Extensions to the `case` tactic

`Batteries.Tactic.Case`, in [Batteries/Tactic/Case.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Case.lean), by Kyle Miller.

> Adds a variant of `case` that looks for a goal with a particular type, rather than a goal
> with a particular tag.
> For consistency with `case`, it takes a tag as well, but the tag can be a hole `_`.
>
> Also adds `case'` extensions.

`Batteries.Tactic.findGoalOfPatt` (definition, [line 122](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Case.lean#L122))

> Find the first goal among those matching `tag` whose type unifies with `patt`.
> The `renameI` array consists of names to use to rename inaccessibles.
> The `patt` term is elaborated in the context where the inaccessibles have been renamed.
>
> Returns the found goal, goals caused by elaborating `patt`, and the remaining goals.

```lean
def findGoalOfPatt (gs : List MVarId)
    (tag : TSyntax ``binderIdent) (patt? : Option Term) (renameI : TSyntaxArray `Lean.binderIdent) :
    TacticM (MVarId × List MVarId × List MVarId)
```

`Batteries.Tactic.processCasePattBody` (definition, [line 159](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Case.lean#L159))

> Given a `casePattBody`, either give a synthetic hole or a tactic sequence
> (along with the syntax for the `=>`).
> Converts holes into synthetic holes since they are processed with `elabTermWithHoles`.

```lean
def processCasePattBody (stx : TSyntax ``casePattTac) :
    TacticM (Term ⊕ (Syntax × TSyntax ``Parser.Tactic.tacticSeq))
```

`Batteries.Tactic.evalCase` (definition, [line 168](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Case.lean#L168))

> Implementation for `case` and `case'`.

```lean
def evalCase (close : Bool) (stx : Syntax)
    (tags : Array (TSyntax `Lean.binderIdent))
    (hss : Array (TSyntaxArray `Lean.binderIdent))
    (patts? : Array (Option Term))
    (caseBody : TSyntax `Batteries.Tactic.casePattTac) :
    TacticM Unit
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/Case.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Case.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.Case.json)
