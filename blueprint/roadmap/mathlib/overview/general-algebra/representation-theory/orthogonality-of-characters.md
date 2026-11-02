---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FDRep.char_orthonormal
mathlib_file: Mathlib/RepresentationTheory/Character.lean
---

# Orthogonality of characters

Orthogonality of characters for irreducible representations of finite group over an
algebraically closed field whose characteristic doesn't divide the order of the group.

```lean
FDRep.char_orthonormal.{u, v} {k : Type u} [Field k] {G : Type v} [Group G] [IsAlgClosed k]
  [Fintype G] [Invertible ↑(Nat.card G)] (V W : FDRep k G) [CategoryTheory.Simple V]
  [CategoryTheory.Simple W] :
  (↑(Nat.card G))⁻¹ * ∑ g, V.character g * W.character g⁻¹ = if Nonempty (V ≅ W) then 1 else 0
```

## Depends on

- [Algebraically closed field](../field-theory/algebraically-closed-field.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Character](character.md)
- [Group](../group-theory/part-01/group.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Isomorphism](../category-theory/isomorphism.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Monoidal category](../category-theory/monoidal-category.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Representation](representation.md)
- [Schur's lemma (Linear representations)](../../../undergraduate/linear-algebra/linear-representations/schurs-lemma.md)
- [Tensor product](../../linear-algebra/fundamentals/tensor-product.md)
- [Transpose of a linear map](../../../undergraduate/linear-algebra/duality/transpose-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `FDRep.char_orthonormal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Character.html#FDRep.char_orthonormal)
- [Source of `FDRep.char_orthonormal` in Mathlib/RepresentationTheory/Character.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/Character.lean#L246)
- [Mathlib overview: General algebra › Representation theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L165)
- [Mathlib undergraduate list: Group Theory › Representation theory of finite groups](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L115)
