---
declaration: module
origin: cited
lean: WantedInfo, «semiformal_result», elabLemmaWanted
statement: formalized
proof: formalized
---

# Semiformal results

The module `Physlib.Meta.Informal.SemiFormal`, [Physlib/Meta/Informal/SemiFormal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/SemiFormal.lean): 3 declarations, 3 with a docstring.

> Semiformal results sit in between informal and formal results. There type or proposition is
> defined, by the proof or definition is not.
>
> ## Note
>
> The code here is modified from the `Util.ProofWanted` module of the Batteries library.
> Released under the Apache 2.0 license, copyright 2023 Lean FRO, authored by
> David Thrane Christiansen.

**`WantedInfo`**, a structure, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/SemiFormal.lean#L31).

```lean
structure WantedInfo where
  /-- The content of the note. -/
  content : String
  /-- Name of result. -/
  name : Name
  /-- The file name where the note came from. -/
  fileName : Name
  /-- The line from where the note came from. -/
  line : Nat
  /-- The tag of the TODO item -/
  tag : String
```

**`«semiformal_result»`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/SemiFormal.lean#L61).

> A semiformal result is either a
> - definition in which the type is given but not the definition.
> - proof in which the proposition is given but not the proof.
> Semiformal results cannot be used in further code. They are essentially
> forgot about after made.
>
> …

```lean
meta def «semiformal_result»
```

**`elabLemmaWanted`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/SemiFormal.lean#L66).

> The elaborator for semiformal results.

```lean
meta def elabLemmaWanted : CommandElab
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Meta/Informal/SemiFormal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/SemiFormal.lean)
