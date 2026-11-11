---
declaration: section
origin: cited
lean: MetaMathlibExt.hannerUnitSegment, MetaMathlibExt.hannerInfinitySum, MetaMathlibExt.hannerOneSum, MetaMathlibExt.IsHannerPolytope, MetaMathlibExt.hannerCube, MetaMathlibExt.hannerCrossPolytope, MetaMathlibExt.hannerCube_isHannerPolytope, MetaMathlibExt.hannerCrossPolytope_isHannerPolytope
statement: formalized
proof: formalized
---

# Hanner polytopes

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html).

## Centered unit segment

The centered unit segment is the closed unit ball
$\{x \in \mathbb{R}^1 : \|x\| \le 1\}$, that is, the segment $[-1, 1]$. It is the
one-dimensional leaf in the recursive definition of Hanner polytopes.

Formalized by `MetaMathlibExt.hannerUnitSegment`, a definition declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-unit-segment).

## $\ell_\infty$ sum of bodies

For sets $K \subseteq \mathbb{R}^m$ and
$L \subseteq \mathbb{R}^n$, the $\ell_\infty$ sum of $K$ and $L$ is the set of points of
$\mathbb{R}^{m+n}$ whose first $m$ coordinates form a point of $K$ and whose last $n$
coordinates form a point of $L$; that is, the product $K \times L$ under the identification
$\mathbb{R}^{m+n} = \mathbb{R}^m \times \mathbb{R}^n$.

Formalized by `MetaMathlibExt.hannerInfinitySum`, a definition declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-infinity-sum).

## $\ell_1$ sum of bodies

For sets $K \subseteq \mathbb{R}^m$ and $L \subseteq \mathbb{R}^n$,
the $\ell_1$ sum of $K$ and $L$ is the convex hull in $\mathbb{R}^{m+n}$ of
$(K \times \{0\}) \cup (\{0\} \times L)$, where $\mathbb{R}^{m+n}$ is identified with
$\mathbb{R}^m \times \mathbb{R}^n$ by splitting off the first $m$ coordinates.

Formalized by `MetaMathlibExt.hannerOneSum`, a definition declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-one-sum).

## Hanner polytopes

For $K \subseteq \mathbb{R}^m$ and $L \subseteq \mathbb{R}^n$, identify
$\mathbb{R}^{m+n}$ with $\mathbb{R}^m \times \mathbb{R}^n$ by splitting off the first $m$
coordinates; the $\ell_\infty$ sum of $K$ and $L$ is $K \times L$, and their $\ell_1$ sum is the
convex hull of $(K \times \{0\}) \cup (\{0\} \times L)$, both viewed as subsets of
$\mathbb{R}^{m+n}$. The Hanner polytopes are the smallest family of subsets of the Euclidean
spaces $\mathbb{R}^n$ such that: the unit segment $[-1, 1] \subseteq \mathbb{R}^1$ is a Hanner
polytope; if $K \subseteq \mathbb{R}^n$ is a Hanner polytope and
$e \colon \mathbb{R}^n \to \mathbb{R}^n$ is an invertible linear map, then $e(K)$ is a Hanner
polytope; and if $K \subseteq \mathbb{R}^m$ and $L \subseteq \mathbb{R}^n$ are Hanner polytopes
with $m, n > 0$, then their $\ell_\infty$ sum and their $\ell_1$ sum are Hanner polytopes.

Formalized by `MetaMathlibExt.IsHannerPolytope`, an inductive type declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#is-hanner-polytope).

## Hanner cube

For $n \in \mathbb{N}$, the Hanner cube $C_n \subseteq \mathbb{R}^{n+1}$ is
defined by recursion on $n$: $C_0$ is the centered unit segment $[-1, 1] \subseteq \mathbb{R}^1$,
and $C_{n+1} \subseteq \mathbb{R}^{n+2}$ is the $\ell_\infty$ sum of $C_n$ and the centered
unit segment.

Formalized by `MetaMathlibExt.hannerCube`, a definition declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-cube).

## Hanner cross-polytope

For $n \in \mathbb{N}$, the Hanner cross-polytope
$P_n \subseteq \mathbb{R}^{n+1}$ is defined by recursion on $n$: $P_0$ is the centered unit
segment $[-1, 1] \subseteq \mathbb{R}^1$, and $P_{n+1} \subseteq \mathbb{R}^{n+2}$ is the
$\ell_1$ sum of $P_n$ and the centered unit segment.

Formalized by `MetaMathlibExt.hannerCrossPolytope`, a definition declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-cross-polytope).

## The Hanner cubes are Hanner polytopes

For every $n \in \mathbb{N}$, the Hanner cube
$C_n \subseteq \mathbb{R}^{n+1}$ is a Hanner polytope.

Formalized by `MetaMathlibExt.hannerCube_isHannerPolytope`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-cube-is-hanner-polytope).

## The Hanner cross-polytopes are Hanner polytopes

For every $n \in \mathbb{N}$, the Hanner
cross-polytope $P_n \subseteq \mathbb{R}^{n+1}$ is a Hanner polytope.

Formalized by `MetaMathlibExt.hannerCrossPolytope_isHannerPolytope`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-cross-polytope-is-hanner-polytope).

## Membership in the Hanner unit segment

A point $x \in \mathbb{R}^1$ lies in the Hanner
unit segment if and only if every coordinate $x_i$ of $x$ satisfies $|x_i| \le 1$.

Formalized by `MetaMathlibExt.mem_hannerUnitSegment_iff`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#mem-hanner-unit-segment-iff).

## Membership in the $\ell_\infty$ Hanner sum

Let $K \subseteq \mathbb{R}^m$ and
$L \subseteq \mathbb{R}^n$. A point $x \in \mathbb{R}^{m+n}$ lies in the $\ell_\infty$ Hanner
sum of $K$ and $L$ if and only if $(x_1, \dots, x_m) \in K$ and
$(x_{m+1}, \dots, x_{m+n}) \in L$.

Formalized by `MetaMathlibExt.mem_hannerInfinitySum_iff`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#mem-hanner-infinity-sum-iff).

## The Hanner cube is the coordinate cube

For every $n \in \mathbb{N}$, the Hanner cube
$C_n \subseteq \mathbb{R}^{n+1}$ equals the coordinate cube
$\{x \in \mathbb{R}^{n+1} : -1 \le x_i \le 1 \text{ for every } i\} = [-1, 1]^{n+1}$.

Formalized by `MetaMathlibExt.hannerCube_eq_coordinateCube`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#hanner-cube-eq-coordinate-cube).

## Hanner polytopes live in positive dimension

If $K \subseteq \mathbb{R}^n$ is a Hanner
polytope, then $0 < n$.

Formalized by `MetaMathlibExt.IsHannerPolytope.dimension_pos`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#dimension-pos).

## Hanner polytopes are centrally symmetric

Every Hanner polytope $K$ is centrally
symmetric about the origin: $-K = K$.

Formalized by `MetaMathlibExt.IsHannerPolytope.neg_eq_self`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#neg-eq-self).

## Negation preserves membership in a Hanner polytope

For every Hanner polytope
$K \subseteq \mathbb{R}^n$ and every $x \in \mathbb{R}^n$, $-x \in K$ if and only if $x \in K$.

Formalized by `MetaMathlibExt.IsHannerPolytope.neg_mem_iff`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#neg-mem-iff).

## Hanner polytopes are convex

Every Hanner polytope $K \subseteq \mathbb{R}^n$ is
convex.

Formalized by `MetaMathlibExt.IsHannerPolytope.convex`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#convex).

## Hanner polytopes contain the origin

The origin belongs to every Hanner polytope.

Formalized by `MetaMathlibExt.IsHannerPolytope.zero_mem`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#zero-mem).

## Hanner polytopes are compact

Every Hanner polytope is compact.

Formalized by `MetaMathlibExt.IsHannerPolytope.isCompact`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#is-compact).

## Hanner polytopes contain the origin in their interior

For every $n \in \mathbb{N}$ and
every Hanner polytope $K \subseteq \mathbb{R}^n$, the origin is an interior point of $K$.

Formalized by `MetaMathlibExt.IsHannerPolytope.zero_mem_interior`, a theorem declared in [MathlibExt/Analysis/Convex/HannerPolytope.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/HannerPolytope.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html#zero-mem-interior).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hanner polytopes](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hanner-polytopes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/convex-geometry/hanner-polytopes)
