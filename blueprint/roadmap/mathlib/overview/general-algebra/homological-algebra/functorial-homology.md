---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: HomologicalComplex.homology
mathlib_file: Mathlib/Algebra/Homology/ShortComplex/HomologicalComplex.lean
---

# Functorial homology

The homology in degree `i` of a homological complex.

```lean
HomologicalComplex.homology.{v_1, u_1, u_2} {C : Type u_1} [CategoryTheory.Category.{v_1, u_1} C]
  [CategoryTheory.Limits.HasZeroMorphisms C] {ι : Type u_2} {c : ComplexShape ι}
  (K : HomologicalComplex C c) (i : ι) [K.HasHomology i] : C
```

## Depends on

- [Isomorphism](../category-theory/isomorphism.md)
- [Limits](../category-theory/limits.md)
- [Small category](../category-theory/small-category.md)

## Sources

- [Mathlib documentation: `HomologicalComplex.homology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Homology/ShortComplex/HomologicalComplex.html#HomologicalComplex.homology)
- [Source of `HomologicalComplex.homology` in Mathlib/Algebra/Homology/ShortComplex/HomologicalComplex.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Homology/ShortComplex/HomologicalComplex.lean#L88)
- [Mathlib overview: General algebra › Homological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L139)
