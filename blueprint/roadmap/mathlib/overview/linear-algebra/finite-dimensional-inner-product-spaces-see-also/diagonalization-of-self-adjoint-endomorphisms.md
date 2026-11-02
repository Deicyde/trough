---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply
mathlib_file: Mathlib/Analysis/InnerProductSpace/Spectrum.lean
---

# Diagonalization of self-adjoint endomorphisms

*Diagonalization theorem*, *spectral theorem*; version 2: A self-adjoint operator `T` on a
finite-dimensional inner product space `E` acts diagonally on the identification of `E` with
Euclidean space induced by an orthonormal basis of eigenvectors of `T`.

```lean
LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {T : E →ₗ[𝕜] E}
  [FiniteDimensional 𝕜 E] {n : ℕ} (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n) (v : E)
  (i : Fin n) :
  ((hT.eigenvectorBasis hn).repr (T v)).ofLp i =
    ↑(hT.eigenvalues hn i) * ((hT.eigenvectorBasis hn).repr v).ofLp i
```

## Depends on

- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Direct sum](../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)
- [Eigenvalue](../structure-theory-of-endomorphisms/eigenvalue.md)
- [Existence of orthonormal basis](existence-of-orthonormal-basis.md)
- [Finite-dimensionality](../finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Isomorphism with $K^n$](../finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Proof depends on

- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Cayley-Hamilton theorem](../endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Eigenvalues from Rayleigh quotient](../../analysis/hilbert-spaces/eigenvalues-from-rayleigh-quotient.md)
- [Extreme value theorem](../../topology/topological-algebra/extreme-value-theorem.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Minimal polynomial](../endomorphism-polynomials/minimal-polynomial.md)
- [Orthogonal projection](../../analysis/hilbert-spaces/orthogonal-projection.md)
- [Roots of a polynomial](../../general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)

## Sources

- [Mathlib documentation: `LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Spectrum.html#LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply)
- [Source of `LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply` in Mathlib/Analysis/InnerProductSpace/Spectrum.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Spectrum.lean#L323)
- [Mathlib overview: Linear algebra › Finite-dimensional inner product spaces (see also Hilbert spaces, below)](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L211)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Endomorphisms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L229)
