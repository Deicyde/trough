---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.EquiangularLines, MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.N, MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.spectralRadiusOrder, MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.theorem_1_2
statement: formalized
---

# Equiangular lines

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines/index.html).

## Equiangular systems of unit vectors

For a real number $\alpha$ and a natural number $d$,
an equiangular system with inner product $\pm\alpha$ in $\mathbb{R}^d$ is a set of unit vectors in
$d$-dimensional Euclidean space such that any two distinct vectors $x$ and $y$ in it satisfy
$|\langle x, y \rangle| = \alpha$.

## Sources

- Z. Jiang, J. Tidor, Y. Yao, S. Zhang, and Y. Zhao, `Equiangular lines with a fixed angle`, Annals of Math, 194 (3) 2021, third paragraph of the introduction.

Formalized by `MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.EquiangularLines`, a structure declared in [WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines/index.html#equiangular-lines).

## Maximum number of equiangular lines

For a real number $\alpha$ and a natural number $d$,
$N_\alpha(d)$ is the supremum, taken in $\mathbb{N}$, of the cardinalities of the equiangular
systems of unit vectors in $\mathbb{R}^d$ with inner product $\pm\alpha$. Here an infinite set
counts as having cardinality $0$, and a set of natural numbers that is not bounded above has
supremum $0$.

For $0 \le \alpha < 1$ these cardinalities are at most $\binom{d+1}{2}$ by Gerzon's bound, and a
system contains at most one of $x$ and $-x$, so $N_\alpha(d)$ is the maximum number of lines
through the origin in $\mathbb{R}^d$ with pairwise angle $\arccos \alpha$.

## Sources

- Z. Jiang, J. Tidor, Y. Yao, S. Zhang, and Y. Zhao, `Equiangular lines with a fixed angle`, Annals of Math, 194 (3) 2021, third paragraph of the introduction.

Formalized by `MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.N`, a definition declared in [WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines/index.html#n).

## Spectral radius order

For a real number $\lambda$, the spectral radius order
$k(\lambda) \in \mathbb{N} \cup \{\infty\}$ is the least natural number $k$ such that some simple
graph on $k$ vertices has an adjacency matrix with spectral radius $\max(\lambda, 0)$, and
$k(\lambda) = \infty$ if there is no such graph.

The source defines $k(\lambda)$ only for $\lambda > 0$, where $\max(\lambda, 0) = \lambda$.

## Sources

- Z. Jiang, J. Tidor, Y. Yao, S. Zhang, and Y. Zhao, `Equiangular lines with a fixed angle`, Annals of Math, 194 (3) 2021, Definition 1.1.

Formalized by `MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.spectralRadiusOrder`, a definition declared in [WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines/index.html#spectral-radius-order).

## Equiangular lines with a fixed angle

Fix a real number $\alpha$ with $0 < \alpha < 1$, let
$\lambda = (1 - \alpha)/(2\alpha)$ and let $k = k(\lambda)$ be the spectral radius order of
$\lambda$. Let $N_\alpha(d)$ be the maximum number of equiangular lines in $\mathbb{R}^d$ with
common angle $\arccos \alpha$. Then:
(a) if $k < \infty$, then $N_\alpha(d) = \lfloor k(d - 1)/(k - 1) \rfloor$ for all sufficiently
large $d$;
(b) if $k = \infty$, then $N_\alpha(d) = d + o(d)$ as $d \to \infty$.

## Sources

- Z. Jiang, J. Tidor, Y. Yao, S. Zhang, and Y. Zhao, `Equiangular lines with a fixed angle`, Annals of Math, 194 (3) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_equiangular_lines_fixed_angle` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.EquiangularLinesFixedAngleWanted.EquiangularLinesFixedAngle.theorem_1_2` is written with `theorem_wanted` in [WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/EquiangularLinesFixedAngleWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines/index.html#theorem-1-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equiangular lines](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/discrete-geometry/part-01/equiangular-lines)
