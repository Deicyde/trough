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
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Category of finite-dimensional representations](../../../overview/general-algebra/representation-theory/category-of-finite-dimensional-representations.md)
- [Isomorphism](../../../overview/general-algebra/category-theory/isomorphism.md)
- [Linear independence](../fundamentals/linear-independence.md)
- [The category of modules over a ring](../../../overview/linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md)

## Proof depends on

- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Schur's lemma (1000+ theorems)](../../../thousand-plus/algebra/20-group-theory-and-generalizations/part-03/schurs-lemma.md)
- [Sum of subspaces](../fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `FDRep.finrank_hom_simple_simple`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/FDRep.html#FDRep.finrank_hom_simple_simple)
- [Source of `FDRep.finrank_hom_simple_simple` in Mathlib/RepresentationTheory/FDRep.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/FDRep.lean#L155)
- [Mathlib undergraduate list: Linear algebra › Linear representations](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L70)
