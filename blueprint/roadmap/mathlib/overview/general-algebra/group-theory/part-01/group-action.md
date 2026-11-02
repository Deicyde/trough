---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: MulAction
mathlib_file: Mathlib/Algebra/Group/Action/Defs.lean
---

# Group action

Type class for monoid actions on types, with notation `g • p`.

The `MulAction G P` typeclass says that the monoid `G` acts multiplicatively on a type `P`.
More precisely this means that the action satisfies the two axioms `1 • p = p` and
`(g₁ * g₂) • p = g₁ • (g₂ • p)`. A mathematician might simply say that the monoid `G`
acts on `P`.

For example, if `G` is a group and `X` is a type, if a mathematician says
say "let `G` act on the set `X`" they will probably mean `[MulAction G X]`.

[Wikidata Q288465](https://www.wikidata.org/wiki/Q288465)

```lean
MulAction.{u_9, u_10} (α : Type u_9) (β : Type u_10) [Monoid α] : Type (max u_10 u_9)
```

## Depends on

- [Natural number](../../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `MulAction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Defs.html#MulAction)
- [Source of `MulAction` in Mathlib/Algebra/Group/Action/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Action/Defs.lean#L121)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L35)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L87)
