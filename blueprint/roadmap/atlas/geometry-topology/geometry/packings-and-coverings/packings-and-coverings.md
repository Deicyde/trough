---
declaration: section
origin: cited
lean: MathlibExt.Geometry.KlartagPackingWanted.Geometry.KlartagPacking.klartag_packing
statement: formalized
---

# Packings and coverings: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/index.html).

Optimal arrangements of congruent bodies in space and the smallest sets or fewest translates needed to cover given families of shapes.

## Klartag's lattice packing theorem

There is a real constant $c > 0$ such that for every
integer $n \ge 1$ there is a linear map $\varphi : \mathbb{R}^n \to \mathbb{R}^n$ for which the
ellipsoid $E = \varphi(B)$, the image of the open Euclidean unit ball $B$ about the origin, has
volume exactly $c n^2$ and the origin is the only point of $E$ whose coordinates are all integers.

The map $\varphi$ is not required to be invertible; a degenerate $\varphi$ would give volume $0$.

## Sources

-. Problem `klartag_packing` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.KlartagPackingWanted.Geometry.KlartagPacking.klartag_packing` is written with `theorem_wanted` in [WantedExt/Geometry/KlartagPackingWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/KlartagPackingWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/index.html#klartag-packing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Packings and coverings](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/packings-and-coverings)
