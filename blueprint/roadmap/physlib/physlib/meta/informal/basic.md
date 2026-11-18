---
declaration: module
origin: cited
lean: InformalDefinition, InformalLemma
statement: formalized
proof: formalized
---

# Physlib.Meta.Informal.Basic

The module `Physlib.Meta.Informal.Basic`, [Physlib/Meta/Informal/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Basic.lean): 2 declarations, 2 with a docstring.

## Informal definitions and lemmas

> This file contains the necessary structures that must be imported into a file for it to contain
> informal definitions and lemmas.
>
> Everything else about informal definitions and lemmas are in the `Informal.Post` module.

**`InformalDefinition`**, a structure, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Basic.lean#L23).

> The structure representing an informal definition.

```lean
structure InformalDefinition where
  /-- The names of top-level commands we expect this definition to depend on. -/
  deps : List Lean.Name
  /-- The tag of the informal definition. This should be unique amongst informal results
    and todo items. -/
  tag : String
```

**`InformalLemma`**, a structure, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Basic.lean#L31).

> The structure representing an informal lemma.

```lean
structure InformalLemma where
  /-- The names of top-level commands we expect this lemma to depend on. -/
  deps : List Lean.Name
  /-- The tag of the informal lemma. This should be unique amongst informal results
    and todo items. -/
  tag : String
```

## Syntax

> Using macros for syntax rewriting works better with the language server compared to
> `Lake.DSL.LeanLibDecl`. Hovering over any definition of `informal_definition` or `informal_lemma`
> gives a proper type hint like any proper definition using `def` whereas definitions of `lake_lib`
> and `lake_exe` don't show docstrings and infer the type `Lean.Name`.

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Informal/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Basic.lean)
