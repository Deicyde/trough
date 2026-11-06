---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: eigenvalue_mem_ball
mathlib_file: Mathlib/LinearAlgebra/Matrix/Gershgorin.lean
---

# Gershgorin circle theorem

**Gershgorin's circle theorem**: for any eigenvalue `μ` of a square matrix `A`, there exists an
index `k` such that `μ` lies in the closed ball of center the diagonal term `A k k` and of
radius the sum of the norms `∑ j ≠ k, ‖A k j‖`.

```lean
eigenvalue_mem_ball.{u_1, u_2} {K : Type u_1} {n : Type u_2} [NormedField K] [Fintype n]
  [DecidableEq n] {A : Matrix n n K} {μ : K} (hμ : Module.End.HasEigenvalue (Matrix.toLin' A) μ) :
  ∃ k, μ ∈ Metric.closedBall (A k k) (∑ j ∈ Finset.univ.erase k, ‖A k j‖)
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Eigenvalue](../../../overview/linear-algebra/structure-theory-of-endomorphisms/eigenvalue.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)

## Proof depends on

- [Eigenvector](../../../overview/linear-algebra/structure-theory-of-endomorphisms/eigenvector.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)

## Sources

- [Mathlib documentation: `eigenvalue_mem_ball`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Gershgorin.html#eigenvalue_mem_ball)
- [Source of `eigenvalue_mem_ball` in Mathlib/LinearAlgebra/Matrix/Gershgorin.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Gershgorin.lean#L27)
- [1000+ theorems list: Q978688](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1179)
- [1000+ theorems project: Q978688](https://1000-plus.github.io/all.html?length=-1#Q978688)
- [Wikipedia: Gershgorin circle theorem](https://en.wikipedia.org/wiki/Gershgorin_circle_theorem)
- [Wikidata: Q978688](https://www.wikidata.org/wiki/Q978688)
