---
declaration: section
origin: cited
lean: MathlibExt.Geometry.ErdosProblem898Wanted.conjecture, MathlibExt.Geometry.ErdosProblem898Wanted.conjecture_holds
statement: formalized
---

# Erdős–Mordell inequality

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/erd-s-mordell-inequality/index.html).

## Statement of the Erdős–Mordell inequality

Writing $XY$ for the distance between points
$X$ and $Y$, this is the assertion that for all affinely independent points $A$, $B$, $C$ of the
Euclidean plane, every point $P$ in the interior of the triangle $ABC$, and all points $M$, $N$,
$L$ on the lines $BC$, $AB$, $CA$ such that the lines $PM$, $PN$, $PL$ are perpendicular to $BC$,
$AB$, $CA$ respectively, we have $PA + PB + PC \ge 2(PM + PN + PL)$.

Formalized by `MathlibExt.Geometry.ErdosProblem898Wanted.conjecture`, a definition declared in [WantedExt/Geometry/ErdosProblem898Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ErdosProblem898Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/erd-s-mordell-inequality/index.html#conjecture).

## Erdős–Mordell inequality

Let $A$, $B$, $C$ be affinely independent points of the Euclidean
plane and $P$ a point in the interior of the triangle $ABC$. Let $M$, $N$, $L$ be points on the
lines $BC$, $AB$, $CA$ such that $PM \perp BC$, $PN \perp AB$ and $PL \perp CA$. Then, writing
$XY$ for the distance between points $X$ and $Y$, we have $PA + PB + PC \ge 2(PM + PN + PL)$.

## Sources

- Paul Erdős, L. J. Mordell, and David F. Barrow, Problem 3740, American Mathematical Monthly 44 (1937), 252–254, https://doi.org/10.2307/2300713.

Stated but not proved: `MathlibExt.Geometry.ErdosProblem898Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/ErdosProblem898Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ErdosProblem898Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/erd-s-mordell-inequality/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős–Mordell inequality](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/erd-s-mordell-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/erd-s-mordell-inequality)
