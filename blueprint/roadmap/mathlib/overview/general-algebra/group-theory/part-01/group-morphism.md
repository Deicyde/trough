---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: MonoidHom
mathlib_file: Mathlib/Algebra/Group/Hom/Defs.lean
---

# Group morphism

`M →* N` is the type of functions `M → N` that preserve the `MulOne` structure.
`MonoidHom` is used for both monoid and group homomorphisms.

When possible, instead of parametrizing results over `(f : M →* N)`,
you should parametrize over `(F : Type*) [MonoidHomClass F M N] (f : F)`.

When you extend this structure, make sure to extend `MonoidHomClass`.

[Wikidata Q868169](https://www.wikidata.org/wiki/Q868169)

```lean
MonoidHom.{u_10, u_11} (M : Type u_10) (N : Type u_11) [MulOne M] [MulOne N] : Type (max u_10 u_11)
```

## Depends on

- [Natural number](../../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `MonoidHom`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html#MonoidHom)
- [Source of `MonoidHom` in Mathlib/Algebra/Group/Hom/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Hom/Defs.lean#L357)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L34)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L80)
