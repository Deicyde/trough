---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsGalois.intermediateFieldEquivSubgroup
mathlib_file: Mathlib/FieldTheory/Galois/Basic.lean
---

# Galois correspondence

The Galois correspondence from intermediate fields to subgroups.

```lean
IsGalois.intermediateFieldEquivSubgroup.{u_1, u_2} {F : Type u_1} [Field F] {E : Type u_2} [Field E]
  [Algebra F E] [FiniteDimensional F E] [IsGalois F E] :
  IntermediateField F E ≃o (Subgroup Gal(E/F))ᵒᵈ
```

## Depends on

- [Algebraic extension](algebraic-extension.md)
- [Field](field.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Separable polynomial](../polynomials-and-power-series/separable-polynomial.md)
- [Subfield](subfield.md)
- [Subgroup](../group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `IsGalois.intermediateFieldEquivSubgroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Galois/Basic.html#IsGalois.intermediateFieldEquivSubgroup)
- [Source of `IsGalois.intermediateFieldEquivSubgroup` in Mathlib/FieldTheory/Galois/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/Galois/Basic.lean#L369)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L134)
