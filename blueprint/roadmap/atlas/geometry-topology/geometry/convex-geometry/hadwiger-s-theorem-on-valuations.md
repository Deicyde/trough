---
declaration: section
origin: cited
lean: MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.E, MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.IsValuation, MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.valuations, MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.hadwiger
statement: formalized
---

# Hadwiger's theorem on valuations

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations/index.html).

## Model space for convex bodies

For a natural number $n$, $E_n$ is the real Euclidean
space $\mathbb{R}^n$ with its standard inner product and Euclidean norm.

Formalized by `MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.E`, an abbreviation declared in [WantedExt/Geometry/HadwigerWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HadwigerWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations/index.html#e).

## Continuous invariant valuation

For a natural number $n$, a real-valued function $f$ on
the convex bodies (nonempty compact convex subsets) of the Euclidean space $\mathbb{R}^n$ is a
continuous invariant valuation if: $f$ is continuous for the Hausdorff metric;
$f(A) + f(B) = f(C) + f(D)$ for all convex bodies $A, B, C, D$ with $A = C \cup D$ and
$B = C \cap D$; $f(e(A)) = f(A)$ for every convex body $A$ and every linear isometry $e$ of
$\mathbb{R}^n$; and $f(A + t) = f(A)$ for every convex body $A$ and every $t \in \mathbb{R}^n$.

Formalized by `MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.IsValuation`, a definition declared in [WantedExt/Geometry/HadwigerWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HadwigerWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations/index.html#is-valuation).

## The space of continuous invariant valuations

For a natural number $n$, the continuous
invariant valuations on the convex bodies of $\mathbb{R}^n$ form a real linear subspace of the
vector space of all functions from the convex bodies of $\mathbb{R}^n$ to $\mathbb{R}$.

Formalized by `MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.valuations`, a definition declared in [WantedExt/Geometry/HadwigerWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HadwigerWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations/index.html#valuations).

## Hadwiger's theorem

For every natural number $n$, the real vector space of continuous
invariant valuations on the convex bodies of $\mathbb{R}^n$ (continuous, additive, and invariant
under linear isometries and translations) is finite-dimensional of dimension $n + 1$.

## Sources

- H. Hadwiger (1937). Listed as §31 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `hadwiger` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.HadwigerWanted.ConvexGeometry.hadwiger` is written with `theorem_wanted` in [WantedExt/Geometry/HadwigerWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HadwigerWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations/index.html#hadwiger).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hadwiger's theorem on valuations](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/convex-geometry/hadwiger-s-theorem-on-valuations)
