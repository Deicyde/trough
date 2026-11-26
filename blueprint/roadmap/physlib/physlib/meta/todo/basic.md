---
declaration: module
origin: cited
lean: Physlib.todoInfo, Physlib.elabTODO
statement: formalized
proof: formalized
---

# Basic underlying structure for TODOs.

The module `Physlib.Meta.TODO.Basic`, [Physlib/Meta/TODO/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/TODO/Basic.lean): 2 declarations, 2 with a docstring.

**`Physlib.todoInfo`**, a structure, [line 22](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/TODO/Basic.lean#L22).

> The information from a `TODO ...` command.

```lean
structure todoInfo where
  /-- The content of the note. -/
  content : String
  /-- The file name where the note came from. -/
  fileName : Name
  /-- The line from where the note came from. -/
  line : Nat
  /-- The tag of the TODO item -/
  tag : String
```

**`Physlib.elabTODO`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/TODO/Basic.lean#L45).

> Elaborator for the `TODO ...` command

```lean
meta def elabTODO : Elab.Command.CommandElab
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/TODO/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/TODO/Basic.lean)
