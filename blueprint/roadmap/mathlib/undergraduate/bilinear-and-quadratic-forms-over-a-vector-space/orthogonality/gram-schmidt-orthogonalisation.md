---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: InnerProductSpace.gramSchmidt_orthogonal
mathlib_file: Mathlib/Analysis/InnerProductSpace/GramSchmidtOrtho.lean
---

# Gram-Schmidt orthogonalisation

**Gram-Schmidt Orthogonalisation**:
`gramSchmidt` produces an orthogonal system of vectors.

```lean
InnerProductSpace.gramSchmidt_orthogonal.{u_1, u_2, u_3} (𝕜 : Type u_1) {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {ι : Type u_3} [LinearOrder ι]
  [LocallyFiniteOrderBot ι] (f : ι → E) {a b : ι} (h₀ : a ≠ b) :
  inner 𝕜 (InnerProductSpace.gramSchmidt 𝕜 f a) (InnerProductSpace.gramSchmidt 𝕜 f b) = 0
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Generating sets](../../linear-algebra/fundamentals/generating-sets.md)
- [Orthogonal projection](../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)

## Proof depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)

## Sources

- [Mathlib documentation: `InnerProductSpace.gramSchmidt_orthogonal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/GramSchmidtOrtho.html#InnerProductSpace.gramSchmidt_orthogonal)
- [Source of `InnerProductSpace.gramSchmidt_orthogonal` in Mathlib/Analysis/InnerProductSpace/GramSchmidtOrtho.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/GramSchmidtOrtho.lean#L78)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L213)
