# Lie's theorem

**Lie's theorem**: Lie modules of solvable Lie algebras over fields of characteristic 0
have a common eigenvector for the action of all elements of the Lie algebra.

See `LieModule.exists_nontrivial_weightSpace_of_isNilpotent` for the variant that
assumes that `L` is nilpotent and drops the condition that `k` is of characteristic zero.

```lean
LieModule.exists_nontrivial_weightSpace_of_isSolvable.{u_1, u_2, u_3} (k : Type u_1) [Field k]
  (L : Type u_2) [LieRing L] [LieAlgebra k L] (V : Type u_3) [AddCommGroup V] [_root_.Module k V]
  [LieRingModule L V] [LieModule k L V] [CharZero k] [Module.Finite k V] [Nontrivial V]
  [LieAlgebra.IsSolvable L] [LieModule.IsTriangularizable k L V] :
  ∃ χ, Nontrivial ↥(LieModule.weightSpace V ⇑χ)
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Dual vector space](../../../overview/linear-algebra/duality/dual-vector-space.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Generalized eigenspaces](../../../undergraduate/linear-algebra/structure-theory-of-endomorphisms/generalized-eigenspaces.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Lie algebra](../../../overview/general-algebra/algebras-over-a-ring/lie-algebra.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Eigenvalue](../../../overview/linear-algebra/structure-theory-of-endomorphisms/eigenvalue.md)
- [Eigenvector](../../../overview/linear-algebra/structure-theory-of-endomorphisms/eigenvector.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Principal ideal domain](../../../overview/general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LieModule.exists_nontrivial_weightSpace_of_isSolvable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/LieTheorem.html#LieModule.exists_nontrivial_weightSpace_of_isSolvable)
- [Source of `LieModule.exists_nontrivial_weightSpace_of_isSolvable` in Mathlib/Algebra/Lie/LieTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Lie/LieTheorem.lean#L236)
- [1000+ theorems list: Q20971632](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L4194)
- [1000+ theorems project: Q20971632](https://1000-plus.github.io/all.html?length=-1#Q20971632)
- [Wikipedia: Lie's theorem](https://en.wikipedia.org/wiki/Lie's_theorem)
- [Wikidata: Q20971632](https://www.wikidata.org/wiki/Q20971632)
