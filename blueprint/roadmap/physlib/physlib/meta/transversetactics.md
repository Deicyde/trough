---
declaration: module
origin: cited
lean: transverseTactics.processCommands, transverseTactics.visitInfo, transverseTactics.traverseForest, transverseTactics
statement: formalized
proof: formalized
---

# Physlib.Meta.TransverseTactics

The module `Physlib.Meta.TransverseTactics`, [Physlib/Meta/TransverseTactics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TransverseTactics.lean): 4 declarations, 4 with a docstring.

> This file enables us to transverse tactics and test for conditions.

## References

> The content of this file is based on the following sources (released under the Apache 2.0
> license), with modifications made to the original content here.
>
> * https://github.com/dwrensha/tryAtEachStep/blob/main/tryAtEachStep.lean.
>   [ref: github\_tryateachstep]
> * https://github.com/lean-dojo/LeanDojo/blob/main/src/lean\_dojo/data\_extraction/ExtractData.lean.
>   [ref: github\_leandojo\_extractdata]
> * See also: https://leanprover.zulipchat.com/#narrow/stream/270676-lean4/topic/Memory.20increase.20in.20loops.2E.

**`transverseTactics.processCommands`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TransverseTactics.lean#L34).

> Takes in a file and returns the infostates of commands and the corresponding
> environment before the command is processed.

```lean
partial def processCommands : Frontend.FrontendM (List (Environment × InfoState))
```

**`transverseTactics.visitInfo`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TransverseTactics.lean#L59).

> Tests if a given `info` is `ofTacticInfo` and if so runs `visitTacticInfo`.

```lean
def visitInfo (file : FilePath) (env : Environment)
    (visitTacticInfo : FilePath → ContextInfo → TacticInfo → MetaM Unit) (ci : ContextInfo)
    (info : Info) (acc : List (IO Unit)) : List (IO Unit)
```

**`transverseTactics.traverseForest`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TransverseTactics.lean#L72).

> Applies `visitInfo` to each node of the info trees.

```lean
def traverseForest (file : FilePath)
    (visitTacticInfo : FilePath → ContextInfo → TacticInfo → MetaM Unit)
    (steps : List (Environment × InfoState)) : List (IO Unit)
```

**`transverseTactics`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TransverseTactics.lean#L87).

> Applies `visitTacticInfo` to each tactic in a file.

```lean
unsafe def transverseTactics (file : FilePath)
  (visitTacticInfo : FilePath → ContextInfo → TacticInfo → MetaM Unit) : IO Unit
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/TransverseTactics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TransverseTactics.lean)
