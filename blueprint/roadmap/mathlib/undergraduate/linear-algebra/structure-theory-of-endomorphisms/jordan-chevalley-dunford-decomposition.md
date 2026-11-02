---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Module.End.exists_isNilpotent_isSemisimple
mathlib_file: Mathlib/LinearAlgebra/JordanChevalley.lean
---

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
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Separable polynomial](../../../overview/general-algebra/polynomials-and-power-series/separable-polynomial.md)
- [Sum of subspaces](../fundamentals/sum-of-subspaces.md)

## Proof depends on

- [$A\[X\]$ has gcd and lcm if $A$ does](../../../overview/general-algebra/polynomials-and-power-series/a-x-has-gcd-and-lcm-if-a-does.md)
- [$K\[X\]$ is Euclidean](../../../overview/general-algebra/polynomials-and-power-series/k-x-is-euclidean.md)
- [Algebraic elements](../../ring-theory/field-theory/part-01/algebraic-elements.md)
- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Cayley-Hamilton theorem](../../../overview/linear-algebra/endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Chinese remainder theorem](../../../overview/general-algebra/ideals-and-quotients/chinese-remainder-theorem.md)
- [Existence of bases](../fundamentals/existence-of-bases.md)
- [Kernel of a linear map](../fundamentals/kernel-of-a-linear-map.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Minimal polynomial](../../../overview/linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Prime spectrum](../../../overview/geometry/algebraic-geometry/prime-spectrum.md)
- [Product of rings](../../ring-theory/fundamentals/product-of-rings.md)
- [Product of vector spaces](../fundamentals/product-of-vector-spaces.md)
- [Rupture field](../../../overview/general-algebra/field-theory/rupture-field.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Sources

- [Mathlib documentation: `Module.End.exists_isNilpotent_isSemisimple`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/JordanChevalley.html#Module.End.exists_isNilpotent_isSemisimple)
- [Source of `Module.End.exists_isNilpotent_isSemisimple` in Mathlib/LinearAlgebra/JordanChevalley.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/JordanChevalley.lean#L73)
- [Mathlib undergraduate list: Linear algebra › Structure theory of endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L66)
