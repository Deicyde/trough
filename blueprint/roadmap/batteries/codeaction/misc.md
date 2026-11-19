---
catalog: module
lean: Batteries.CodeAction.findStack?, Batteries.CodeAction.holeKindToHoleString, Batteries.CodeAction.instanceStub, Batteries.CodeAction.getExplicitArgs, Batteries.CodeAction.getAllArgs, Batteries.CodeAction.eqnStub, Batteries.CodeAction.startTacticStub, Batteries.CodeAction.removeAfterDoneAction, Batteries.CodeAction.getElimExprNames, Batteries.CodeAction.findTermInfo?, Batteries.CodeAction.findTermInfoWithCtx?, Batteries.CodeAction.casesExpand, Batteries.CodeAction.addSubgoalsActionCore, Batteries.CodeAction.addSubgoalsSeqAction, Batteries.CodeAction.addSubgoalsAction
statement: formalized
proof: formalized
---

# Miscellaneous code actions

`Batteries.CodeAction.Misc`, in [Batteries/CodeAction/Misc.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean), by Mario Carneiro.

> This declares some basic tactic code actions, using the `@[tactic_code_action]` API.

`Batteries.CodeAction.findStack?` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L29))

> Return the syntax stack leading to `target` from `root`, if one exists.

```lean
def findStack? (root target : Syntax) : Option Syntax.Stack
```

`Batteries.CodeAction.holeKindToHoleString` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L35))

> Constructs a hole with a kind matching the provided hole elaborator.

```lean
def holeKindToHoleString : (elaborator : Name) → (synthName : String) → String
```

`Batteries.CodeAction.instanceStub` (definition, [line 68](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L68))

> Hole code action used to fill in a structure's field when specifying an instance.
>
> In the following:
> ```lean
> instance : Monad Id := _
> ```
>
> invoking the hole code action "Generate a (minimal) skeleton for the structure under construction."
> produces:
> ```lean
> instance : Monad Id where
>   pure := _
>   bind := _
> ```
>
> and invoking "Generate a (maximal) skeleton for the structure under construction." produces:
> ```lean
> instance : Monad Id where
>   map := _
>   mapConst := _
>   pure := _
>   seq := _
>   seqLeft := _
>   seqRight := _
>   bind := _
> ```

```lean
partial def instanceStub : HoleCodeAction
```

`Batteries.CodeAction.getExplicitArgs` (definition, [line 135](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L135))

> Returns the explicit arguments given a type. The second argument of this
> function is an accumulator.

```lean
def getExplicitArgs : Expr → Array Name → Array Name
```

`Batteries.CodeAction.getAllArgs` (definition, [line 142](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L142))

> Returns all of the arguments given a type. The second argument of this
> function is an accumulator.

```lean
def getAllArgs : Expr → Array Name → Array Name
```

`Batteries.CodeAction.eqnStub` (definition, [line 173](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L173))

> Invoking hole code action "Generate a list of equations for a recursive definition" in the
> following:
> ```lean
> def foo : Expr → Unit := _
> ```
>
> produces:
>
> ```lean
> def foo : Expr → Unit := fun
>   | .bvar deBruijnIndex => _
>   | .fvar fvarId => _
>   | .mvar mvarId => _
>   | .sort u => _
>   | .const declName us => _
>   | .app fn arg => _
>   | .lam binderName binderType body binderInfo => _
>   | .forallE binderName binderType body binderInfo => _
>   | .letE declName type value body nonDep => _
>   | .lit _ => _
>   | .mdata data expr => _
>   | .proj typeName idx struct => _
> ```

```lean
def eqnStub : HoleCodeAction
```

`Batteries.CodeAction.startTacticStub` (definition, [line 206](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L206))

> Invoking hole code action "Start a tactic proof" will fill in a hole with `by done`.

```lean
def startTacticStub : HoleCodeAction
```

`Batteries.CodeAction.removeAfterDoneAction` (definition, [line 234](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L234))

> The "Remove tactics after 'no goals'" code action deletes any tactics following a completed
> proof.
> ```
> example : True := by
>   trivial
>   trivial -- <- remove this, proof is already done
>   rfl
> ```
> is transformed to
> ```
> example : True := by
>   trivial
> ```

```lean
def removeAfterDoneAction : TacticCodeAction
```

`Batteries.CodeAction.getElimExprNames` (definition, [line 256](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L256))

> Similar to `getElimExprInfo`, but returns the names of binders instead of just the numbers;
> intended for code actions which need to name the binders.

```lean
def getElimExprNames (elimType : Expr) : MetaM (Array (Name × Array Name))
```

`Batteries.CodeAction.findTermInfo?` (definition, [line 278](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L278))

> Finds the `TermInfo` for an elaborated term `stx`.

```lean
def findTermInfo? (node : InfoTree) (stx : Term) : Option TermInfo
```

`Batteries.CodeAction.findTermInfoWithCtx?` (definition, [line 289](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L289))

> `findTermInfoWithCtx?` finds the `TermInfo` for an elaborated term `stx`
> and also updates the inputted `ContextInfo` using all the
> `PartialContextInfo` on the path to the returned `TermInfo`.

```lean
partial def findTermInfoWithCtx? (t : InfoTree) (stx : Term) (ctx : ContextInfo)
    : Option (TermInfo × ContextInfo)
```

`Batteries.CodeAction.casesExpand` (definition, [line 328](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L328))

> Invoking tactic code action "Generate an explicit pattern match for 'induction'" in the
> following:
> ```lean
> example (x : Nat) : x = x := by
>   induction x
> ```
> produces:
> ```lean
> example (x : Nat) : x = x := by
>   induction x with
>   | zero => sorry
>   | succ n ih => sorry
> ```
>
> It also works for `cases`.

```lean
def casesExpand : TacticCodeAction
```

`Batteries.CodeAction.addSubgoalsActionCore` (definition, [line 428](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L428))

> The "Add subgoals" code action puts `· done` subgoals for any goals remaining at the end of a
> proof.
> ```
> example : True ∧ True := by
>   constructor
>   -- <- here
> ```
> is transformed to
> ```
> example : True ∧ True := by
>   constructor
>   · done
>   · done
> ```

```lean
def addSubgoalsActionCore (params : Lsp.CodeActionParams)
  (i : Nat) (stk : Syntax.Stack) (goals : List MVarId) : RequestM (Array LazyCodeAction)
```

`Batteries.CodeAction.addSubgoalsSeqAction` (definition, [line 471](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L471))

```lean
def addSubgoalsSeqAction : TacticSeqCodeAction
```

`Batteries.CodeAction.addSubgoalsAction` (definition, [line 477](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean#L477))

```lean
def addSubgoalsAction : TacticCodeAction
```

## Depends on

- [Initial setup for code action attributes](attr.md)
- [Position](../lean/position.md)

## Sources

- [Batteries/CodeAction/Misc.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/CodeAction/Misc.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.CodeAction.Misc.json)
