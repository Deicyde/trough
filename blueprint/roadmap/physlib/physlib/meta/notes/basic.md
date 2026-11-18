---
declaration: module
origin: cited
lean: Physlib.NoteInfo, Physlib.elabNote
statement: formalized
proof: formalized
---

# Physlib.Meta.Notes.Basic

The module `Physlib.Meta.Notes.Basic`, [Physlib/Meta/Notes/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/Basic.lean): 2 declarations, 2 with a docstring.

## Underlying structure for notes

> This file contains the necessary structures that must be imported into a file
> for it to be turned into a Lean note.
>
> It allows for the
> - `note ...` command to be used to add notes to a Lean file
> - `note_attr` attribute to be used to display formally verified commands within a note.
> - `note_attr_informal` attribute to be used to display informal commands within a note.
>
> Other results relating to notes are in other files.

**`Physlib.NoteInfo`**, a structure, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/Basic.lean#L32).

> The information from a `note ...` command. To be used in a note file

```lean
structure NoteInfo where
  /-- The content of the note. -/
  content : String
  /-- The file name where the note came from. -/
  fileName : Name
  /-- The line from where the note came from. -/
  line : Nat
```

**`Physlib.elabNote`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/Basic.lean#L53).

> Elaborator for the `note ...` command

```lean
meta def elabNote : Lean.Elab.Command.CommandElab
```

## Note attribute

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Notes/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/Basic.lean)
