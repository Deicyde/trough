---
catalog: module
lean: Batteries.Util.LibraryNote, Batteries.Util.LibraryNote.LibraryNoteEntry, Batteries.Util.LibraryNote.encodeNameForExport
statement: formalized
proof: formalized
---

# Define the `library_note` command

`Batteries.Util.LibraryNote`, in [Batteries/Util/LibraryNote.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/LibraryNote.lean), by Gabriel Ebner.

`Batteries.Util.LibraryNote` (definition, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/LibraryNote.lean#L22))

> A library note is identified by the name of its declaration, and its content should be contained
> in its doc-string.

```lean
def LibraryNote
```

`Batteries.Util.LibraryNote.LibraryNoteEntry` (definition, [line 31](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/LibraryNote.lean#L31))

> Entry for library notes in the environment extension.
>
> We only store the name, and look up the constant's docstring to find its contents.

```lean
def LibraryNoteEntry
```

`Batteries.Util.LibraryNote.encodeNameForExport` (definition, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/LibraryNote.lean#L44))

> Encode a name to be safe for the Lean export format.
>
> The current export format (used by `lean4export` and consumed by external type checkers like
> `nanoda_lib`) does not support whitespace in declaration names. Library notes often have
> human-readable names with spaces like `«my library note»`, which would produce declarations
> like `LibraryNote.«my library note»` that cannot be exported.
>
> This function replaces spaces with underscores to produce export-safe names like
> `LibraryNote.my_library_note`.

```lean
def encodeNameForExport (n : Name) : Name
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/LibraryNote.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/LibraryNote.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Util.LibraryNote.json)
