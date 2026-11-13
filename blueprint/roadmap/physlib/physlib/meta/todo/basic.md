---
declaration: module
origin: cited
lean: Physlib.todoInfo, Physlib.elabTODO
statement: formalized
proof: formalized
---

# Basic underlying structure for TODOs.

The module `Physlib.Meta.TODO.Basic`, [Physlib/Meta/TODO/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TODO/Basic.lean): 2 declarations, 2 with a docstring.

**`Physlib.todoInfo`**, a structure, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TODO/Basic.lean#L22).

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

**`Physlib.elabTODO`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TODO/Basic.lean#L45).

```lean
meta def elabTODO : Elab.Command.CommandElab
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/TODO/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/TODO/Basic.lean)
