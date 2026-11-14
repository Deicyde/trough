---
declaration: module
origin: cited
lean: Physlib.NoteFile, Physlib.NoteFile.imports
statement: formalized
proof: formalized
---

# Note file

The module `Physlib.Meta.Notes.NoteFile`, [Physlib/Meta/Notes/NoteFile.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/NoteFile.lean): 2 declarations, 2 with a docstring.

> A note file is a structure which contains the information to go into a note.

**`Physlib.NoteFile`**, a structure, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/NoteFile.lean#L23).

> A note consists of a title and a list of Lean files which make up the note.

```lean
structure NoteFile where
  /-- The overall title of the note. -/
  title : String
  /-- The abstract of the note. -/
  abstract : String
  /-- A list of authors. -/
  authors : List String
  /-- The files making up the note in the order in which they should appear. -/
  files : List Name
```

**`Physlib.NoteFile.imports`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/NoteFile.lean#L38).

> All imports associated to a note.

```lean
def imports : Array Import
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Notes/NoteFile.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/NoteFile.lean)
