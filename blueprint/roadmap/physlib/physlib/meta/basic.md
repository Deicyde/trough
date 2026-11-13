---
declaration: module
origin: cited
lean: Array.flatSize, Array.flatFilterSizeM, Physlib.allImports, Physlib.noImports, Physlib.Imports.getConsts, Physlib.Imports.getUserConsts, Lean.Name.toFilePath, Physlib.Imports.getLines
statement: formalized
proof: formalized
---

# Physlib.Meta.Basic

The module `Physlib.Meta.Basic`, [Physlib/Meta/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean): 27 declarations, 27 with a docstring.

## Basic Lean meta programming commands

**`Array.flatSize`**, a def, [line 18](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L18).

> The size of a flattened array of arrays.

```lean
def Array.flatSize {α} : Array (Array α) → Nat
```

**`Array.flatFilterSizeM`**, a def, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L22).

> The size of a flattened array of arrays after applying an element-wise filter.

```lean
def Array.flatFilterSizeM {α m} [Monad m] (p : α → m Bool) : Array (Array α) → m Nat
```

## Imports

**`Physlib.allImports`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L34).

> Gets all imports within Physlib and QuantumInfo..

```lean
def Physlib.allImports : IO (Array Import)
```

**`Physlib.noImports`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L52).

> Number of files within Physlib.

```lean
def Physlib.noImports : IO Nat
```

**`Physlib.Imports.getConsts`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L57).

> Gets all constants from an import.

```lean
def Physlib.Imports.getConsts (imp : Import) : IO (Array ConstantInfo)
```

**`Physlib.Imports.getUserConsts`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L63).

> Gets all user defined constants from an import.

```lean
def Physlib.Imports.getUserConsts (imp : Import) : CoreM (Array ConstantInfo)
```

**`Lean.Name.toFilePath`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L81).

> Turns a name into a system file path.

```lean
def Lean.Name.toFilePath (c : Name) : System.FilePath
```

**`Physlib.Imports.getLines`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L85).

> Lines from import.

```lean
def Physlib.Imports.getLines (imp : Import) : IO (Array String)
```

## Name

**`Lean.Name.toRelativeFilePath`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L98).

> Turns a name into a Lean file.

```lean
def toRelativeFilePath (c : Name) : System.FilePath
```

**`Lean.Name.toGitHubLink`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L102).

> Turns a name, which represents a module, into a link to github.

```lean
def toGitHubLink (c : Name) (line : Nat) : String
```

**`Lean.Name.lineNumber`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L106).

> Given a name, returns the line number.

```lean
def lineNumber (c : Name) : m Nat
```

**`Lean.Name.fileName`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L112).

> Given a name, returns the file name corresponding to that declaration.

```lean
def fileName (c : Name) : m Name
```

**`Lean.Name.location`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L120).

> Returns the location of a name.

```lean
def location (c : Name) : m String
```

**`Lean.Name.hasPos`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L129).

> Determines if a name has a location.

```lean
def hasPos (c : Name) : m Bool
```

**`Lean.Name.hasDocString`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L134).

> Determines if a name has a doc string.

```lean
def hasDocString (c : Name) : CoreM Bool
```

**`Lean.Name.getDocString`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L139).

> The doc string from a name.

```lean
def getDocString (c : Name) : CoreM String
```

**`Lean.Name.getDeclString`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L147).

> Given a name, returns the source code defining that name, including doc strings.

```lean
def getDeclString (name : Name) : CoreM String
```

**`Lean.Name.getDeclStringNoDoc`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L163).

> Given a name, returns the source code defining that name,
> starting with the def ... or lemma... etc.

```lean
def getDeclStringNoDoc (name : Name) : CoreM String
```

**`Physlib.noDefs`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L180).

> Number of definitions.

```lean
def noDefs : CoreM Nat
```

**`Physlib.noLemmas`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L186).

> Number of definitions.

```lean
def noLemmas : CoreM Nat
```

**`Physlib.allDocStrings`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L192).

> All docstrings present in Physlib.

```lean
def allDocStrings : CoreM (Array String)
```

**`Physlib.noDefsNoDocString`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L200).

> Number of definitions without a doc-string.

```lean
def noDefsNoDocString : CoreM Nat
```

**`Physlib.noLemmasNoDocString`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L207).

> Number of definitions without a doc-string.

```lean
def noLemmasNoDocString : CoreM Nat
```

**`Physlib.noLines`**, a def, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L214).

> The number of lines in Physlib.

```lean
def noLines : IO Nat
```

**`Physlib.noTODOs`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L220).

```lean
def noTODOs : IO Nat
```

**`Physlib.noFilesWithTODOs`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L226).

```lean
def noFilesWithTODOs : IO Nat
```

**`Physlib.allUserConsts`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean#L233).

> All user defined declarations.

```lean
def allUserConsts : CoreM (Array ConstantInfo)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Basic.lean)
