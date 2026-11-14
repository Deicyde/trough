---
declaration: module
origin: cited
lean: Physlib.HTMLNote, Physlib.HTMLNote.ofNodeInfo, Physlib.HTMLNote.ofFormal, Physlib.HTMLNote.ofInformal
statement: formalized
proof: formalized
---

# Physlib.Meta.Notes.HTMLNote

The module `Physlib.Meta.Notes.HTMLNote`, [Physlib/Meta/Notes/HTMLNote.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/HTMLNote.lean): 4 declarations, 4 with a docstring.

## Turns a declaration into a html note structure.

**`Physlib.HTMLNote`**, a structure, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/HTMLNote.lean#L25).

> A `HTMLNote` is a structure containing the html information from
> individual contributions (commands, informal commands, note ..) etc. to a note file.

```lean
structure HTMLNote where
  /-- The name of the file the contribution came from. -/
  fileName : Name
  /-- The html contribution of the content. -/
  content : String
  /-- The line in the file where the contribution came from. -/
  line : Nat
```

**`Physlib.HTMLNote.ofNodeInfo`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/HTMLNote.lean#L34).

> Converts a note info into a HTMLNote.

```lean
def HTMLNote.ofNodeInfo (ni : NoteInfo) : HTMLNote
```

**`Physlib.HTMLNote.ofFormal`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/HTMLNote.lean#L38).

> An formal definition or lemma to html for a note.

```lean
def HTMLNote.ofFormal (name : Name) : CoreM HTMLNote
```

**`Physlib.HTMLNote.ofInformal`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/HTMLNote.lean#L51).

> An informal definition or lemma to html for a note.

```lean
unsafe def HTMLNote.ofInformal (name : Name) : CoreM HTMLNote
```

## Depends on

- [Physlib.Meta.Basic](../basic.md)
- [Physlib.Meta.Notes.Basic](basic.md)

## Sources

- [Physlib/Meta/Notes/HTMLNote.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/HTMLNote.lean)
