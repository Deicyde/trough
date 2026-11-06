# Jordan-Chevalley-Dunford decomposition

**Jordan-Chevalley-Dunford decomposition**: an endomorphism of a finite-dimensional vector space
over a perfect field may be written as a sum of nilpotent and semisimple endomorphisms. Moreover
these nilpotent and semisimple components are polynomial expressions in the original endomorphism.

```lean
Module.End.exists_isNilpotent_isSemisimple.{u_1, u_2} {K : Type u_1} {V : Type u_2} [Field K]
  [AddCommGroup V] [_root_.Module K V] {f : Module.End K V} [FiniteDimensional K V]
  [PerfectField K] : ∃ n ∈ K[f], ∃ s ∈ K[f], IsNilpotent n ∧ s.IsSemisimple ∧ f = n + s
```

## Depends on

- [Algebra of endomorphisms of a vector space](../fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Separable polynomial](../../../overview/general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Sum of subspaces](../fundamentals/sum-of-subspaces.md)

## Proof depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Minimal polynomial](../../../overview/linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Module.End.exists_isNilpotent_isSemisimple`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/JordanChevalley.html#Module.End.exists_isNilpotent_isSemisimple)
- [Source of `Module.End.exists_isNilpotent_isSemisimple` in Mathlib/LinearAlgebra/JordanChevalley.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/JordanChevalley.lean#L73)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L66)
