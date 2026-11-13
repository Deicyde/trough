---
declaration: module
origin: cited
lean: PseudoInfo, addPseudofulEntry
statement: formalized
proof: formalized
---

# The `pseudo` attribute

The module `Physlib.Meta.Linters.Pseudo`, [Physlib/Meta/Linters/Pseudo.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Linters/Pseudo.lean): 2 declarations, 2 with a docstring.

> The attribute marking declarations which depend on the `Lean.ofReduceBool` axiom.

## i. Overview

> This module defines the attribute `pseudo`, marking declarations that depend on the
> `Lean.ofReduceBool` axiom, and the environment extension `pseudoExtension` recording them.
> The check that the attribute is correctly applied is `Physlib.pseudoTest` in
> `Physlib.Meta.Pseudo`.

## ii. Key results

> - `pseudoExtension` : The environment extension recording the declarations attributed `pseudo`.
> - `Pseudo_attr` : The `pseudo` attribute.

## iv. References

> * None.

## A. The `pseudo` environment extension

**`PseudoInfo`**, a structure, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Linters/Pseudo.lean#L49).

> The information stored for a declaration marked with `pseudo`.

```lean
structure PseudoInfo where
  /-- Name of result. -/
  name : Name
```

**`addPseudofulEntry`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Linters/Pseudo.lean#L63).

> Adds an entry to `pseudoExtension`.

```lean
def addPseudofulEntry {m : Type → Type} [MonadEnv m]
    (declName : Name) : m Unit
```

## B. The `pseudo` attribute

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Linters/Pseudo.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Linters/Pseudo.lean)
