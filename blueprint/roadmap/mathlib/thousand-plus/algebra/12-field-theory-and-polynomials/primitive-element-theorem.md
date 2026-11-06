---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Field.exists_primitive_element
mathlib_file: Mathlib/FieldTheory/PrimitiveElement.lean
---

# Primitive element theorem

**Primitive element theorem**: a finite separable field extension `E` of `F` has a
primitive element, i.e. there is an `α ∈ E` such that `F⟮α⟯ = (⊤ : Subalgebra F E)`.

```lean
Field.exists_primitive_element.{u_1, u_2} (F : Type u_1) (E : Type u_2) [Field F] [Field E]
  [Algebra F E] [FiniteDimensional F E] [Algebra.IsSeparable F E] : ∃ α, F⟮α⟯ = ⊤
```

## Depends on

- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Minimal polynomial](../../../overview/linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Separable polynomial](../../../overview/general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Subfield](../../../overview/general-algebra/field-theory/subfield.md)

## Proof depends on

- [$K\[X\]$ is Euclidean](../../../overview/general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md)
- [Greatest Common Divisor Algorithm](../../../hundred-theorems/part-03/greatest-common-divisor-algorithm.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Splitting field](../../../overview/general-algebra/field-theory/splitting-field.md)

## Sources

- [Mathlib documentation: `Field.exists_primitive_element`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/PrimitiveElement.html#Field.exists_primitive_element)
- [Source of `Field.exists_primitive_element` in Mathlib/FieldTheory/PrimitiveElement.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/PrimitiveElement.lean#L206)
- [1000+ theorems list: Q2093886](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2007)
- [1000+ theorems project: Q2093886](https://1000-plus.github.io/all.html?length=-1#Q2093886)
- [Wikipedia: Primitive element theorem](https://en.wikipedia.org/wiki/Primitive_element_theorem)
- [Wikidata: Q2093886](https://www.wikidata.org/wiki/Q2093886)
