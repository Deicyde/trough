---
declaration: section
origin: cited
lean: MathlibExt.Topology.NonseparatingPlanarContinuumWanted.HasFixedPointProperty, MathlibExt.Topology.NonseparatingPlanarContinuumWanted.conjecture, MathlibExt.Topology.NonseparatingPlanarContinuumWanted.conjecture_holds
statement: formalized
---

# Plane fixed point problem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/plane-fixed-point-problem/index.html).

## Fixed point property

A subset $K$ of the Euclidean plane $\mathbb{R}^2$ has the fixed
point property when every continuous map $f \colon K \to K$ has a fixed point, that is, a point
$x \in K$ with $f(x) = x$.

## Sources

- Open Problem Garden, node ID 37295, http://www.openproblemgarden.org/op/nonseparating_planar_continuum.

Formalized by `MathlibExt.Topology.NonseparatingPlanarContinuumWanted.HasFixedPointProperty`, a definition declared in [WantedExt/Topology/NonseparatingPlanarContinuumWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/NonseparatingPlanarContinuumWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/plane-fixed-point-problem/index.html#has-fixed-point-property).

## Nonseparating planar continuum conjecture

The conjecture asserts that every nonempty,
compact, path-connected subset $K$ of the Euclidean plane $\mathbb{R}^2$ whose complement
$\mathbb{R}^2 \setminus K$ is connected (that is, $K$ does not separate the plane) has the fixed
point property: every continuous map $f \colon K \to K$ has a point $x \in K$ with $f(x) = x$.

## Sources

- Open Problem Garden, node ID 37295, http://www.openproblemgarden.org/op/nonseparating_planar_continuum.

Formalized by `MathlibExt.Topology.NonseparatingPlanarContinuumWanted.conjecture`, a definition declared in [WantedExt/Topology/NonseparatingPlanarContinuumWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/NonseparatingPlanarContinuumWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/plane-fixed-point-problem/index.html#conjecture).

## Path-connected nonseparating plane continua have the fixed point property

Let $K$ be a
nonempty, compact, path-connected subset of the Euclidean plane $\mathbb{R}^2$ whose complement
$\mathbb{R}^2 \setminus K$ is connected. Then $K$ has the fixed point property: every continuous
map $f \colon K \to K$ has a point $x \in K$ with $f(x) = x$.

This answers the nonseparating planar continuum conjecture in the affirmative. Hagopian (A
fixed-point theorem for plane continua, Bull. AMS 77 (1971), 351-354; addendum 1972) proved that
every arcwise connected nonseparating plane continuum has the fixed point property, and compact
path-connected subsets of the plane are arcwise connected.

## Sources

- A. M. Blokh, R. J. Fokkink, J. C. Mayer, L. G. Oversteegen, E. D. Tymchatyn, Fixed point theorems for plane continua with applications, Mem. Amer. Math. Soc. 224 (2013), no. 1053, arXiv:1004.0214 (citing C. L. Hagopian, Bull. Amer. Math. Soc. 77 (1971), 351-354), https://arxiv.org/abs/1004.0214.

Stated but not proved: `MathlibExt.Topology.NonseparatingPlanarContinuumWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Topology/NonseparatingPlanarContinuumWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/NonseparatingPlanarContinuumWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/plane-fixed-point-problem/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Plane fixed point problem](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/plane-fixed-point-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/continua-infinite-dimensional/plane-fixed-point-problem)
