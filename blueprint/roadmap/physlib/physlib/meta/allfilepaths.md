---
declaration: module
origin: cited
lean: allFilePaths.go, getFilePaths, allFilePaths, allPhyslibModules
statement: formalized
proof: formalized
---

# Physlib.Meta.AllFilePaths

The module `Physlib.Meta.AllFilePaths`, [Physlib/Meta/AllFilePaths.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/AllFilePaths.lean): 4 declarations, 4 with a docstring.

## Getting an array of all file paths in Physlib.

**`allFilePaths.go`**, a def, [line 19](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/AllFilePaths.lean#L19).

> The recursive function underlying `allFilePaths`.

```lean
partial def allFilePaths.go (prev : Array FilePath)
  (root : String) (path : FilePath) : IO (Array FilePath)
```

**`getFilePaths`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/AllFilePaths.lean#L30).

> Gets an array of all file paths in the supplied directory.

```lean
partial def getFilePaths (moduleName : String) : IO (Array FilePath)
```

**`allFilePaths`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/AllFilePaths.lean#L34).

> Gets an array of all file paths in `Physlib`.

```lean
partial def allFilePaths : IO (Array FilePath)
```

**`allPhyslibModules`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/AllFilePaths.lean#L38).

> Gets an array of all module names in `Physlib`.

```lean
def allPhyslibModules : IO (Array Lean.Name)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/AllFilePaths.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/AllFilePaths.lean)
