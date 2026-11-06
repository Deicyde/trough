# Wedderburn–Artin theorem

Mathlib records this with 2 declarations.

`IsSimpleRing.exists_algEquiv_matrix_divisionRing`: The **Wedderburn–Artin Theorem**, algebra form: an Artinian simple algebra is isomorphic
to a matrix algebra over a division algebra.

```lean
IsSimpleRing.exists_algEquiv_matrix_divisionRing.{u, u_1} (R₀ : Type u_1) (R : Type u)
  [CommSemiring R₀] [Ring R] [Algebra R₀ R] [IsSimpleRing R] [IsArtinianRing R] :
  ∃ n, ∃ (_ : NeZero n), ∃ D x x_1, Nonempty (R ≃ₐ[R₀] Matrix (Fin n) (Fin n) D)
```

`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`: The **Wedderburn–Artin Theorem**, algebra form: a semisimple algebra is isomorphic to a
product of matrix algebras over division algebras.

```lean
IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing.{u, u_1} (R₀ : Type u_1) (R : Type u)
  [CommSemiring R₀] [Ring R] [Algebra R₀ R] [IsSemisimpleRing R] :
  ∃ n D d x x_1,
    (∀ (i : Fin n), NeZero (d i)) ∧
      Nonempty (R ≃ₐ[R₀] (i : Fin n) → Matrix (Fin (d i)) (Fin (d i)) (D i))
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Ideal of a commutative ring](../../../overview/general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Noetherian module](../../../overview/linear-algebra/fundamentals/noetherian-module.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `IsSimpleRing.exists_algEquiv_matrix_divisionRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/SimpleModule/WedderburnArtin.html#IsSimpleRing.exists_algEquiv_matrix_divisionRing)
- [Source of `IsSimpleRing.exists_algEquiv_matrix_divisionRing` in Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean#L118)
- [Mathlib documentation: `IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/SimpleModule/WedderburnArtin.html#IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing)
- [Source of `IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing` in Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/SimpleModule/WedderburnArtin.lean#L196)
- [1000+ theorems list: Q776578](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L871)
- [1000+ theorems project: Q776578](https://1000-plus.github.io/all.html?length=-1#Q776578)
- [Wikipedia: Artin–Wedderburn theorem](https://en.wikipedia.org/wiki/Artin%E2%80%93Wedderburn_theorem)
- [Wikidata: Q776578](https://www.wikidata.org/wiki/Q776578)
