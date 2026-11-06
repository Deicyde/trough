# Orthonormal bases

An orthonormal set in a finite-dimensional `InnerProductSpace` is maximal, if and only if it
is a basis.

```lean
maximal_orthonormal_iff_basis_of_finiteDimensional.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {v : Set E} [FiniteDimensional 𝕜 E]
  (hv : Orthonormal 𝕜 Subtype.val) :
  (∀ u ⊇ v, Orthonormal 𝕜 Subtype.val → u = v) ↔ ∃ b, ⇑b = Subtype.val
```

## Depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Orthogonal complement](../../../overview/analysis/hilbert-spaces/orthogonal-complement.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `maximal_orthonormal_iff_basis_of_finiteDimensional`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Projection/FiniteDimensional.html#maximal_orthonormal_iff_basis_of_finiteDimensional)
- [Source of `maximal_orthonormal_iff_basis_of_finiteDimensional` in Mathlib/Analysis/InnerProductSpace/Projection/FiniteDimensional.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Projection/FiniteDimensional.lean#L402)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Euclidean and Hermitian spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L221)
