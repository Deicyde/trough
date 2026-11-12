---
declaration: section
origin: cited
lean: OAI.ScalarConductivity.main_nonuniqueness
statement: formalized
proof: formalized
---

# 365. Joint metric and connection recovery from one boundary patch

3 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Zero-frequency measurements on any nonempty open boundary patch determine a smooth metric and smooth unitary connection on a trivial Hermitian rank-two bundle over a compact connected manifold of dimension at least three, up to diffeomorphism and gauge fixed on that patch. Inputs and observations use the same patch. In contrast, distinct uniformly positive bounded measurable scalar conductivities on a three-dimensional ball can have identical full-boundary data.

## Determination of a metric and a unitary connection from one boundary patch

We prove that zero-frequency boundary measurements on any nonempty open boundary patch determine both a smooth Riemannian metric and a smooth unitary connection on the trivial Hermitian rank-two bundle over a compact connected smooth manifold of dimension at least three with smooth boundary. Both inputs and observations are restricted to the same patch. The metric and connection are determined up to a diffeomorphism and a unitary gauge that restrict to the identity on the measured patch.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf).

## Smooth anisotropic uniqueness in the Calderón problem from one boundary patch

We resolve the smooth anisotropic Calderón uniqueness problem with arbitrary same-patch measurements. A smooth Riemannian metric on a compact connected manifold of dimension at least three is determined, up to a diffeomorphism fixing the measured patch, by its zero-frequency Dirichlet-to-Neumann energy form with both input and observation on any nonempty open boundary patch.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf).

## Nonuniqueness for bounded measurable scalar conductivities in three dimensions

We construct two distinct uniformly positive bounded measurable scalar conductivities on a ball in ℝ$^{3}$ with the same full Dirichlet-to-Neumann operator. Both conductivities equal one near the boundary. This gives nonuniqueness in the scalar Calderón problem at bounded measurable regularity.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Calderón inverse problem asks whether boundary measurements determine an interior conductivity. The formalized result gives nonuniqueness for bounded measurable scalar conductivities on the ball $B(0,3)\subset\mathbb R^3$: two uniformly positive conductivities differ on a set of positive volume, equal $1$ near the boundary, and have the same full weak Dirichlet-to-Neumann operator. Weak solutions exist uniquely for every boundary trace.

## Lean: Scalar conductivity nonuniqueness

Stated in [Conductivity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Conductivity.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_nonuniqueness : MainStatement
```

Proved in [lean/OAI/Analysis/Conductivity/Main.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Conductivity/Main.lean#L73).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/365.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/365.md)
