---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: FDRep.finrank_hom_simple_simple
mathlib_file: Mathlib/RepresentationTheory/FDRep.lean
---

# Schur's lemma (Linear representations)

Schur's Lemma: the dimension of the `Hom`-space between two irreducible representation is `0` if
they are not isomorphic, and `1` if they are.

```lean
FDRep.finrank_hom_simple_simple.{u, v} {k : Type u} {G : Type v} [Field k] [Monoid G]
  [IsAlgClosed k] (V W : FDRep k G) [CategoryTheory.Simple V] [CategoryTheory.Simple W] :
  Module.finrank k (V ⟶ W) = if Nonempty (V ≅ W) then 1 else 0
```

## Depends on

- [Algebraically closed field](../../../overview/general-algebra/field-theory/algebraically-closed-field.md)
- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Category of finite-dimensional representations](../../../overview/general-algebra/representation-theory/category-of-finite-dimensional-representations.md)
- [Functor](../../../overview/general-algebra/category-theory/functor.md)
- [Isomorphism](../../../overview/general-algebra/category-theory/isomorphism.md)
- [Linear independence](../fundamentals/linear-independence.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Limits](../../../overview/general-algebra/category-theory/limits.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Small category](../../../overview/general-algebra/category-theory/small-category.md)
- [Sum of subspaces](../fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `FDRep.finrank_hom_simple_simple`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/FDRep.html#FDRep.finrank_hom_simple_simple)
- [Source of `FDRep.finrank_hom_simple_simple` in Mathlib/RepresentationTheory/FDRep.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/FDRep.lean#L155)
- [Mathlib undergraduate list: Linear algebra › Linear representations](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L70)
