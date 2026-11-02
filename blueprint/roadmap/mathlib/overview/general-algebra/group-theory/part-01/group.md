---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Group
mathlib_file: Mathlib/Algebra/Group/Defs.lean
---

# Group

A `Group` is a `Monoid` with an operation `⁻¹` satisfying `a⁻¹ * a = 1`.

There is also a division operation `/` such that `a / b = a * b⁻¹`,
with a default so that `a / b = a * b⁻¹` holds by definition.

Use `Group.ofLeftAxioms` or `Group.ofRightAxioms` to define a group structure
on a type with the minimum proof obligations.

[Wikidata Q83478](https://www.wikidata.org/wiki/Q83478)

```lean
Group.{u_2} (G : Type u_2) : Type u_2
```

## Depends on

- [Integer](../../numbers/integer.md)

## Sources

- [Mathlib documentation: `Group`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html#Group)
- [Source of `Group` in Mathlib/Algebra/Group/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Defs.lean#L25)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L33)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L79)
