---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook138Wanted.IsAbsoluteRetract, MathlibExt.Topology.ScottishBook138Wanted.IsWilsonConvex, MathlibExt.Topology.ScottishBook138Wanted.eilenbergCompactConvexAbsoluteRetract
statement: formalized
---

# Absolute retracts

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/absolute-retracts/index.html).

## Absolute retract

A topological space $K$ is an absolute retract when $K$ is compact
and, for every separable metrizable space $X$ and every topological embedding
$e \colon K \to X$, there is a continuous map $r \colon X \to K$ with $r(e(k)) = k$ for all
$k \in K$.

Formalized by `MathlibExt.Topology.ScottishBook138Wanted.IsAbsoluteRetract`, a definition declared in [WantedExt/Topology/ScottishBook138Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook138Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/absolute-retracts/index.html#is-absolute-retract).

## Wilson convexity

A subset $K$ of a pseudometric space $X$ with distance $d$ is convex in
the sense of Wilson when for all $x, y \in K$ and every real $t$ with $0 \le t \le 1$ there is
exactly one $z \in K$ with $d(x, z) = t \, d(x, y)$ and $d(z, y) = (1 - t) \, d(x, y)$.

Formalized by `MathlibExt.Topology.ScottishBook138Wanted.IsWilsonConvex`, a definition declared in [WantedExt/Topology/ScottishBook138Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook138Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/absolute-retracts/index.html#is-wilson-convex).

## Eilenberg's theorem on compact convex absolute retracts

(a) Every nonempty compact
convex subset of a complete metrizable locally convex topological vector space over
$\mathbb{R}$ is an absolute retract. (b) Every nonempty compact subset of a pseudometric
space that is convex in the sense of Wilson is an absolute retract.

The spaces in part (a) are the real Fréchet spaces, the spaces of type (B0).

## Sources

- S. Eilenberg, Problem 138 of the Scottish Book; the typescript heads the entry "Theorem; Eilenberg" and states both (a) and (b) as theorems. Part (a) is also the Dugundji theorem, see the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867), which notes that every nonempty convex subset of a locally convex metrizable topological vector space is an absolute retract.

Stated but not proved: `MathlibExt.Topology.ScottishBook138Wanted.eilenbergCompactConvexAbsoluteRetract` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook138Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook138Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/absolute-retracts/index.html#eilenberg-compact-convex-absolute-retrac).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Absolute retracts](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/absolute-retracts/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/continua-infinite-dimensional/absolute-retracts)
