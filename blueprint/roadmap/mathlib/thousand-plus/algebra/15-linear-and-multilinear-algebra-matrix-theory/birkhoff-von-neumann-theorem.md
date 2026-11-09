# Birkhoff–Von Neumann theorem

**Birkhoff's theorem**
The set of doubly stochastic matrices is the convex hull of the permutation matrices.  Note
`exists_eq_sum_perm_of_mem_doublyStochastic` gives a convex weighting of each permutation matrix
directly.  To show `doublyStochastic n` is convex, use `convex_doublyStochastic`.

```lean
doublyStochastic_eq_convexHull_permMatrix.{u_1, u_2} {R : Type u_1} {n : Type u_2} [Fintype n]
  [DecidableEq n] [Field R] [LinearOrder R] [IsStrictOrderedRing R] :
  ↑(doublyStochastic R n) = (convexHull R) {x | ∃ σ, Equiv.Perm.permMatrix R σ = x}
```

## Depends on

- [Convex hull of a subset of an affine real space](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Ring-valued matrix](../../../overview/linear-algebra/matrices/ring-valued-matrix.md)

## Proof depends on

- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Hall's marriage theorem](../../../overview/combinatorics/transversals/halls-marriage-theorem.md)

## Sources

- [Mathlib documentation: `doublyStochastic_eq_convexHull_permMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Birkhoff.html#doublyStochastic_eq_convexHull_permMatrix)
- [Source of `doublyStochastic_eq_convexHull_permMatrix` in Mathlib/Analysis/Convex/Birkhoff.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Convex/Birkhoff.lean#L158)
- [1000+ theorems list: Q1243340](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1567)
- [1000+ theorems project: Q1243340](https://1000-plus.github.io/all.html?length=-1#Q1243340)
- [Wikipedia: Birkhoff–Von Neumann theorem](https://en.wikipedia.org/wiki/Birkhoff%E2%80%93Von_Neumann_theorem)
- [Wikidata: Q1243340](https://www.wikidata.org/wiki/Q1243340)
