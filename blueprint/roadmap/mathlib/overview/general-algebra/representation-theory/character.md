---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: FDRep.character
mathlib_file: Mathlib/RepresentationTheory/Character.lean
---

# Character

The character of a representation `V : FDRep k G` is the function associating to `g : G` the
trace of the linear map `V.ρ g`.

```lean
FDRep.character.{u, v} {k : Type u} [Field k] {G : Type v} [Monoid G] (V : FDRep k G) (g : G) : k
```

## Depends on

- [Category of finite-dimensional representations](category-of-finite-dimensional-representations.md)
- [Field](../field-theory/field.md)
- [Matrix representation of a linear map](../../linear-algebra/matrices/matrix-representation-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `FDRep.character`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Character.html#FDRep.character)
- [Source of `FDRep.character` in Mathlib/RepresentationTheory/Character.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/Character.lean#L166)
- [Mathlib overview: General algebra › Representation theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L164)
- [Mathlib undergraduate list: Group Theory › Representation theory of finite groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L119)
