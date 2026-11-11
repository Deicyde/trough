---
declaration: section
origin: cited
lean: MetaMathlibExt.planeRegionCount, MetaMathlibExt.planeRegionCount_empty, MetaMathlibExt.isGreatest_planeRegionCount_threeArmedV, MetaMathlibExt.isGreatest_planeRegionCount_threeChain, MetaMathlibExt.isGreatest_planeRegionCount_longLeggedA, MetaMathlibExt.cos_sub_neg_of_tbar_inter_ncard_four, MetaMathlibExt.cos_sub_neg_of_lollipop_good_pair
statement: formalized
---

# Pancake cutting with exotic knives

7 results, 2 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html).

## Number of regions cut out of the plane

For a set $K \subseteq \mathbb{R}^2$ of cuts, the
number of regions into which $K$ divides the plane is the number of connected components of the
complement $\mathbb{R}^2 \setminus K$, or $0$ if there are infinitely many components.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Section 1.

Formalized by `MetaMathlibExt.planeRegionCount`, a definition declared in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#plane-region-count).

## No cuts, one region

The empty set of cuts divides the plane into exactly one region.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Section 1 (`n = 0`).

Formalized by `MetaMathlibExt.planeRegionCount_empty`, a theorem declared in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#plane-region-count-empty).

## Maximum region count for three-armed V's

A long-legged three-armed V is the union of
three rays $\{c + s u_j : s \ge 0\}$, $j = 1, 2, 3$, from a common tip $c \in \mathbb{R}^2$, with
nonzero direction vectors $u_1, u_2, u_3 \in \mathbb{R}^2$ in arbitrary directions. For every
natural number $n$, the largest number of regions into which the union of $n$ long-legged
three-armed V's can divide the plane is $(9n^2 - 5n + 2)/2$.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Theorem 1 (`jis-2026-26.4.5-thm-1`), with the definition in the section *The k-armed V*.

Stated but not proved: `MetaMathlibExt.isGreatest_planeRegionCount_threeArmedV` is written with `theorem_wanted` in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#is-greatest-plane-region-count-three-arm).

## Maximum region count for 3-chains

For points $p, q \in \mathbb{R}^2$ and nonzero vectors
$u, v \in \mathbb{R}^2$, the 3-chain is the union of the ray $\{p + s u : s \ge 0\}$, the segment
$[p, q]$ and the ray $\{q + s v : s \ge 0\}$; the directions are arbitrary and the 3-chain may
intersect itself. For every natural number $n$, the largest number of regions into which the
union of $n$ 3-chains can divide the plane is $(9n^2 - 5n + 2)/2$.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Theorem 1 (`jis-2026-26.4.5-thm-1`), with the definition in the section *The k-chain*.

Stated but not proved: `MetaMathlibExt.isGreatest_planeRegionCount_threeChain` is written with `theorem_wanted` in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#is-greatest-plane-region-count-three-cha).

## Maximum region count for long-legged A's

For a tip $c \in \mathbb{R}^2$, nonzero vectors
$u_1, u_2 \in \mathbb{R}^2$ and reals $a, b > 0$, the long-legged A is the union of the rays
$\{c + s u_1 : s \ge 0\}$ and $\{c + s u_2 : s \ge 0\}$ and the crossbar segment
$[c + a u_1, c + b u_2]$. For every natural number $n$, the largest number of regions into which
the union of $n$ long-legged A's can divide the plane is $(9n^2 - 5n + 2)/2$.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Theorem 1 (`jis-2026-26.4.5-thm-1`), with the definition in the section *The long-legged A*.

Stated but not proved: `MetaMathlibExt.isGreatest_planeRegionCount_longLeggedA` is written with `theorem_wanted` in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#is-greatest-plane-region-count-long-legg).

## Four-point intersections of constrained T's

For a point $c \in \mathbb{R}^2$ and an angle
$\theta \in \mathbb{R}$, the constrained long-legged T $\bar T(c, \theta)$ is the union of the
crossbar, the line $\{c + s(-\sin\theta, \cos\theta) : s \in \mathbb{R}\}$, and the stem, the ray
$\{c + s(\cos\theta, \sin\theta) : s \ge 0\}$. For all $c_1, c_2 \in \mathbb{R}^2$ and
$\theta_1, \theta_2 \in \mathbb{R}$, if $\bar T(c_1, \theta_1) \cap \bar T(c_2, \theta_2)$ has
exactly four points, then $\cos(\theta_1 - \theta_2) < 0$, that is, the two stem directions make
an angle greater than $\pi/2$.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Lemma 2 (`jis-2026-26.4.5-lem-2`), with the definition in the subsection *The constrained long-legged T̄*.

Stated but not proved: `MetaMathlibExt.cos_sub_neg_of_tbar_inter_ncard_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#cos-sub-neg-of-tbar-inter-ncard-four).

## Stem–circle intersections of two lollipops

For a point $c = (a, b) \in \mathbb{R}^2$, a
radius $r > 0$ and an angle $\theta \in \mathbb{R}$, the lollipop with center $c$, radius $r$ and
stem direction $(\cos\theta, \sin\theta)$ consists of the circle
$\{(x, y) \in \mathbb{R}^2 : (x - a)^2 + (y - b)^2 = r^2\}$ and the stem
$\{c + s(\cos\theta, \sin\theta) : s \ge r\}$, the part of the ray from $c$ in that direction
outside the open disc. For all $c_1, c_2 \in \mathbb{R}^2$, $r_1, r_2 > 0$ and
$\theta_1, \theta_2 \in \mathbb{R}$, consider the lollipops with centers $c_i$, radii $r_i$ and
stem directions $(\cos\theta_i, \sin\theta_i)$. If the number of points where the stem of the
first meets the circle of the second plus the number of points where the stem of the second meets
the circle of the first is $3$ or $4$, then $\cos(\theta_1 - \theta_2) < 0$.

## Sources

- David O. H. Cutler, Jonas Karlsson and Neil J. A. Sloane, *Cutting a Pancake with an Exotic Knife*, Journal of Integer Sequences 29 (2026), Article 26.4.5, Lemma 3 (`jis-2026-26.4.5-lem-3`), with the definition in the subsection *The lollipop or qoppa*.

Stated but not proved: `MetaMathlibExt.cos_sub_neg_of_lollipop_good_pair` is written with `theorem_wanted` in [WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ExoticKnifePancakeWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html#cos-sub-neg-of-lollipop-good-pair).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pancake cutting with exotic knives](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/pancake-cutting-with-exotic-knives)
