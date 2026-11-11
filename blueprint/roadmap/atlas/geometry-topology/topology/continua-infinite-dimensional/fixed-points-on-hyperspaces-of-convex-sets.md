---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook42Wanted.HausdorffContinuousOnConvexCompacts, MathlibExt.Topology.ScottishBook42Wanted.fixed_point_for_convex_hyperspace_map
statement: formalized
---

# Fixed points on hyperspaces of convex sets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/fixed-points-on-hyperspaces-of-convex-sets/index.html).

## Hausdorff continuity on compact convex sets

Let $E$ be a real normed space, let
$K \subseteq E$, let $f$ be a map from subsets of $E$ to subsets of $E$, and write $d_H$ for the
Hausdorff distance between subsets of $E$. Then $f$ is Hausdorff continuous on the compact convex
subsets of $K$ if for every nonempty compact convex set $X \subseteq K$ and every
$\varepsilon > 0$ there is $\delta > 0$ such that every nonempty compact convex set
$Y \subseteq K$ with $d_H(X, Y) < \delta$ satisfies $d_H(f(X), f(Y)) < \varepsilon$.

Here $d_H$ is taken to be $0$ where the Hausdorff distance is infinite, in particular when exactly
one of the two sets is empty. The values $f(X)$ are not required to be compact, convex or
nonempty.

Formalized by `MathlibExt.Topology.ScottishBook42Wanted.HausdorffContinuousOnConvexCompacts`, a definition declared in [WantedExt/Topology/ScottishBook42Wanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook42Wanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/fixed-points-on-hyperspaces-of-convex-sets/index.html#hausdorff-continuous-on-convex-compacts).

## Fixed point theorem for maps of compact convex sets

Let $n \ge 0$ and let $B$ be the
closed unit ball about the origin in the Euclidean space $\mathbb{R}^n$. Let $f$ be a map from
subsets of $\mathbb{R}^n$ to subsets of $\mathbb{R}^n$ that sends every nonempty compact convex
subset of $B$ to a nonempty compact convex subset of $B$, and that is continuous in the Hausdorff
metric on the nonempty compact convex subsets of $B$. Then there is a nonempty compact convex set
$X_0 \subseteq B$ with $f(X_0) = X_0$.

This answers Ulam's Problem 42 of the Scottish Book, which asks this for closed convex sets inside
a ball $K$; inside a ball the closed convex sets are the compact ones, and the typescript's
"sphere $K$" is read as the solid ball. All sets are required to be nonempty, because the
Hausdorff distance used is degenerate at the empty set. The answer is yes: for $n \ge 2$ the space
of nonempty compact convex subsets of $B$ is homeomorphic to the Hilbert cube (Nadler, Quinn and
Stavrokas), which has the fixed-point property; for $n \le 1$ that space is a point or a $2$-cell,
and Brouwer's theorem applies.

## Sources

- S. Ulam, Problem 42 of the Scottish Book; S. B. Nadler, J. Quinn and N. Stavrokas, Pacific J. Math. 83 (1979), 441-462; the fixed-point theorem for the Hilbert cube; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook42Wanted.fixed_point_for_convex_hyperspace_map` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook42Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook42Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/fixed-points-on-hyperspaces-of-convex-sets/index.html#fixed-point-for-convex-hyperspace-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed points on hyperspaces of convex sets](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/fixed-points-on-hyperspaces-of-convex-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/continua-infinite-dimensional/fixed-points-on-hyperspaces-of-convex-sets)
