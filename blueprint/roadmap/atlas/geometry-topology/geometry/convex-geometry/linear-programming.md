---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Convex.LPDuality.strong_linear_programming_duality, MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.LinearProgram, MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.LinearProgram.feasible, MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.LinearProgram.objective, MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.lp_maximum_principle, MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.simplex_algorithm
statement: formalized
---

# Linear programming

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html).

## Strong linear programming duality

Let $A$ be a real $m \times n$ matrix, and let
$b \in \mathbb{R}^m$ and $c \in \mathbb{R}^n$; inequalities between vectors are componentwise.
Suppose some $x \in \mathbb{R}^n$ satisfies $x \ge 0$ and $Ax \le b$, and that $c \cdot x$ is
bounded above over all such $x$. Then there exist $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^m$
with $x \ge 0$, $Ax \le b$, $y \ge 0$, $A^{\mathsf{T}} y \ge c$ and $c \cdot x = b \cdot y$.

By weak duality, such $x$ and $y$ are optimal solutions of the primal problem of maximizing
$c \cdot x$ subject to $x \ge 0$, $Ax \le b$ and of the dual problem of minimizing $b \cdot y$
subject to $y \ge 0$, $A^{\mathsf{T}} y \ge c$.

Informal source: George B. Dantzig, *Linear Programming and Extensions*,
Princeton University Press, 1963, strong duality theorem.

Formalized by `MathlibExt.Analysis.Convex.LPDuality.strong_linear_programming_duality`, a theorem declared in [MathlibExt/Analysis/Convex/LinearProgrammingDuality.lean, line 930](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Convex/LinearProgrammingDuality.lean#L930). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html#strong-linear-programming-duality).

## Linear program

A linear program in standard inequality form with $m$ variables and
$n$ constraints is given by an objective vector $c \in \mathbb{R}^m$, a right-hand side
$b \in \mathbb{R}^n$ and an $n \times m$ real constraint matrix $A$; it stands for the problem
of maximising $c \cdot x$ over $x \in \mathbb{R}^m$ subject to $A x \le b$ and $x \ge 0$.

Formalized by `MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.LinearProgram`, a structure declared in [WantedExt/Geometry/LinearProgrammingWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LinearProgrammingWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html#linear-program).

## Feasible region of a linear program

The feasible region of a linear program with
$m$ variables, constraint matrix $A$ and right-hand side $b$ is the set of vectors
$x \in \mathbb{R}^m$ with $A x \le b$ and $x \ge 0$, both inequalities holding componentwise.
It is a convex polyhedron in $\mathbb{R}^m$.

Formalized by `MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.LinearProgram.feasible`, a definition declared in [WantedExt/Geometry/LinearProgrammingWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LinearProgrammingWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html#feasible).

## Objective function of a linear program

The objective function of a linear program
with $m$ variables and objective vector $c \in \mathbb{R}^m$ is the map
$f \colon \mathbb{R}^m \to \mathbb{R}$ given by $f(x) = c \cdot x = \sum_i c_i x_i$.

Formalized by `MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.LinearProgram.objective`, a definition declared in [WantedExt/Geometry/LinearProgrammingWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LinearProgrammingWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html#objective).

## Maximum principle for linear programming

Consider a linear program with $m$ variables
and objective vector $c \in \mathbb{R}^m$, let $P \subseteq \mathbb{R}^m$ be its feasible region
and $f(x) = c \cdot x$ its objective function, and let $x \in P$ be a local maximiser of $f$ on
$P$, that is, $f(y) \le f(x)$ for all $y \in P$ in some neighbourhood of $x$. Then $x$ is a
global maximiser of $f$ on $P$, and if $c \ne 0$ then $x$ lies on the topological boundary of
$P$ in $\mathbb{R}^m$.

## Sources

- G. B. Dantzig (1947), simplex algorithm. Listed as §101 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `lp_maximum_principle` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.lp_maximum_principle` is written with `theorem_wanted` in [WantedExt/Geometry/LinearProgrammingWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LinearProgrammingWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html#lp-maximum-principle).

## Optimal vertices of linear programs

Consider a linear program with $m$ variables and
objective vector $c \in \mathbb{R}^m$, and let $P \subseteq \mathbb{R}^m$ be its feasible region
and $f(x) = c \cdot x$ its objective function. If $P$ is nonempty and bounded, then some
$x \in P$ maximises $f$ on $P$ and is an extreme point of $P$, that is, $x$ does not lie in the
open segment between two distinct points of $P$.

## Sources

- G. B. Dantzig (1947), simplex algorithm. Listed as §101 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `lp_maximum_principle` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.LinearProgrammingWanted.ConvexGeometry.simplex_algorithm` is written with `theorem_wanted` in [WantedExt/Geometry/LinearProgrammingWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/LinearProgrammingWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html#simplex-algorithm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear programming](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/linear-programming/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/convex-geometry/linear-programming)
