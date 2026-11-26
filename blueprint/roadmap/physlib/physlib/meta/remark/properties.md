---
declaration: module
origin: cited
lean: Physlib.allRemarkInfo, Physlib.RemarkInfo.toFullName, Physlib.RemarkInfo.IsRemark, Physlib.RemarkInfo.getRemarkInfo
statement: formalized
proof: formalized
---

# Physlib.Meta.Remark.Properties

The module `Physlib.Meta.Remark.Properties`, [Physlib/Meta/Remark/Properties.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/Remark/Properties.lean): 4 declarations, 4 with a docstring.

## Underlying structure for remarks

**`Physlib.allRemarkInfo`**, a def, [line 23](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/Remark/Properties.lean#L23).

> All remarks in the environment.

```lean
meta def allRemarkInfo : m (Array RemarkInfo)
```

**`Physlib.RemarkInfo.toFullName`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/Remark/Properties.lean#L28).

> The full name of a remark (name and namespace).

```lean
meta def RemarkInfo.toFullName (r : RemarkInfo) : Name
```

**`Physlib.RemarkInfo.IsRemark`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/Remark/Properties.lean#L35).

> A Bool which is true if a name corresponds to a remark.

```lean
meta def RemarkInfo.IsRemark (n : Name) : m Bool
```

**`Physlib.RemarkInfo.getRemarkInfo`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/Remark/Properties.lean#L41).

> Gets the remarkInfo from a name corresponding to a remark..

```lean
meta def RemarkInfo.getRemarkInfo (n : Name) : m RemarkInfo
```

## Depends on

- [Physlib.Meta.Remark.Basic](basic.md)

## Sources

- [Physlib/Meta/Remark/Properties.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Meta/Remark/Properties.lean)
