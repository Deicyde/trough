---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: mk_eq_mk_of_basis
mathlib_file: Mathlib/LinearAlgebra/Dimension/StrongRankCondition.lean
---

# Dimension theorem for vector spaces

The dimension theorem: if `v` and `v'` are two bases, their index types
have the same cardinalities.

```lean
mk_eq_mk_of_basis.{u, v, w, w'} {R : Type u} {M : Type v} [Semiring R] [AddCommMonoid M]
  [_root_.Module R M] {ι : Type w} {ι' : Type w'} [InvariantBasisNumber R] (v : Module.Basis ι R M)
  (v' : Module.Basis ι' R M) :
  Cardinal.lift.{w', w} (Cardinal.mk ι) = Cardinal.lift.{w, w'} (Cardinal.mk ι')
```

## Depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)

## Sources

- [Mathlib documentation: `mk_eq_mk_of_basis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/StrongRankCondition.html#mk_eq_mk_of_basis)
- [Source of `mk_eq_mk_of_basis` in Mathlib/LinearAlgebra/Dimension/StrongRankCondition.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Dimension/StrongRankCondition.lean#L63)
- [1000+ theorems list: Q3527205](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2533)
- [1000+ theorems project: Q3527205](https://1000-plus.github.io/all.html?length=-1#Q3527205)
- [Wikipedia: Dimension theorem for vector spaces](https://en.wikipedia.org/wiki/Dimension_theorem_for_vector_spaces)
- [Wikidata: Q3527205](https://www.wikidata.org/wiki/Q3527205)
