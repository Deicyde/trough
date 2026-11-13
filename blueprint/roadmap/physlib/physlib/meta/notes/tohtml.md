---
declaration: module
origin: cited
lean: Physlib.NoteFile.sortLE, Physlib.NoteFile.getNodeInfo, Physlib.NoteFile.codeBlockHTML, Physlib.NoteFile.informalDefStyle, Physlib.NoteFile.codeButton, Physlib.NoteFile.mathJaxScript, Physlib.NoteFile.headerHTML, Physlib.NoteFile.titleHTML
statement: formalized
proof: formalized
---

# Physlib.Meta.Notes.ToHTML

The module `Physlib.Meta.Notes.ToHTML`, [Physlib/Meta/Notes/ToHTML.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean): 11 declarations, 11 with a docstring.

## Turns a declaration into a html note structure.

**`Physlib.NoteFile.sortLE`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L26).

> Sorts `NoteInfo`'s by file name then by line number.

```lean
meta def sortLE (ni1 ni2 : HTMLNote) : Bool
```

**`Physlib.NoteFile.getNodeInfo`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L33).

> Returns a sorted list of NodeInfos for a file system.

```lean
meta unsafe def getNodeInfo : CoreM (List HTMLNote)
```

**`Physlib.NoteFile.codeBlockHTML`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L45).

> The HTML code needed to have syntax highlighting.

```lean
meta def codeBlockHTML : String
```

**`Physlib.NoteFile.informalDefStyle`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L73).

> The html styles for informal definitions.

```lean
meta def informalDefStyle : String
```

**`Physlib.NoteFile.codeButton`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L108).

> The html styles for code button.

```lean
meta def codeButton : String
```

**`Physlib.NoteFile.mathJaxScript`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L135).

> HTML allowing the use of mathjax.

```lean
meta def mathJaxScript : String
```

**`Physlib.NoteFile.headerHTML`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L151).

> The header to the html code.

```lean
meta def headerHTML : String
```

**`Physlib.NoteFile.titleHTML`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L162).

> The html code corresponding to the title, abstract and authors.

```lean
meta def titleHTML : String
```

**`Physlib.NoteFile.leanNote`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L168).

> The html code corresponding to a note about Lean and its use.

```lean
meta def leanNote : String
```

**`Physlib.NoteFile.footerHTML`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L184).

> The footer of the html file.

```lean
meta def footerHTML : String
```

**`Physlib.NoteFile.toHTMLString`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean#L189).

> The html file associated to a NoteFile string.

```lean
meta unsafe def toHTMLString : MetaM String
```

## Depends on

- [Physlib.Meta.Notes.HTMLNote](htmlnote.md)
- [Note file](notefile.md)

## Sources

- [Physlib/Meta/Notes/ToHTML.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Notes/ToHTML.lean)
