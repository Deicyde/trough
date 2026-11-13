---
declaration: module
origin: cited
lean: Physlib.RemarkInfo, Physlib.elabRemark
statement: formalized
proof: formalized
---

# Physlib.Meta.Remark.Basic

The module `Physlib.Meta.Remark.Basic`, [Physlib/Meta/Remark/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Remark/Basic.lean): 2 declarations, 2 with a docstring.

## Underlying structure for remarks

**`Physlib.RemarkInfo`**, a structure, [line 21](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Remark/Basic.lean#L21).

> The information from a `remark ...` command. To be used in a note file

```lean
structure RemarkInfo where
  /-- The content of the remark. -/
  content : String
  /-- The file name where the remark came from. -/
  fileName : Name
  /-- The line from where the remark came from. -/
  line : Nat
  /-- The name of the remark. -/
  name : Name
  /-- The namespace of the remark. -/
  nameSpace : Name
```

**`Physlib.elabRemark`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Remark/Basic.lean#L46).

> Elaborator for the `note ...` command

```lean
meta def elabRemark : Elab.Command.CommandElab
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Remark/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Remark/Basic.lean)
