---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BlumenthalMinimaxAngleErdosProblem504Wanted.minimaxAngle, MathlibExt.Combinatorics.BlumenthalMinimaxAngleErdosProblem504Wanted.minimaxAngleValues, MathlibExt.Combinatorics.BlumenthalMinimaxAngleErdosProblem504Wanted.minimaxAngleValues_holds
statement: formalized
---

# Blumenthal's minimax angle problem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/blumenthal-s-minimax-angle-problem/index.html).

## Minimax angle

For a natural number $N$, the minimax angle $\alpha_N$ is the supremum of
the $\alpha \in [0, \pi]$ such that every set of $N$ points in the Euclidean plane contains three
distinct points $x, y, z$ with $\angle xyz \ge \alpha$, where $\angle xyz$ is the unoriented angle
at $y$.

For $N \le 2$ no set of $N$ points has three distinct points, so the set of such $\alpha$ is empty
and $\alpha_N$ is $0$ by the convention for the supremum of the empty set.

Formalized by `MathlibExt.Combinatorics.BlumenthalMinimaxAngleErdosProblem504Wanted.minimaxAngle`, a definition declared in [WantedExt/Combinatorics/BlumenthalMinimaxAngleErdosProblem504Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BlumenthalMinimaxAngleErdosProblem504Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/blumenthal-s-minimax-angle-problem/index.html#minimax-angle).

## Blumenthal's minimax angle values (Erdős Problem 504)

For a natural number $N$, let
$\alpha_N$ be the minimax angle of $N$ points in the plane: the supremum of the
$\alpha \in [0, \pi]$ such that every set of $N$ points in the plane contains three distinct
points $x, y, z$ with $\angle xyz \ge \alpha$ (the angle at $y$). The statement is Sendov's
answer: $\alpha_3 = \pi/3$, $\alpha_4 = \pi/2$, and for all natural numbers $n \ge 2$ and $N$,
if $2^n < N \le 2^n + 2^{n-2}$, then $\alpha_N = \left(1 - \frac{2}{2n + 1}\right)\pi$, and if
$2^n + 2^{n-2} < N \le 2^{n+1}$, then $\alpha_N = \left(1 - \frac{1}{n + 1}\right)\pi$.

Formalized by `MathlibExt.Combinatorics.BlumenthalMinimaxAngleErdosProblem504Wanted.minimaxAngleValues`, a definition declared in [WantedExt/Combinatorics/BlumenthalMinimaxAngleErdosProblem504Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BlumenthalMinimaxAngleErdosProblem504Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/blumenthal-s-minimax-angle-problem/index.html#minimax-angle-values).

## Sendov's solution of Blumenthal's minimax angle problem (Erdős Problem 504)

For a natural
number $N$, let $\alpha_N$ be the minimax angle of $N$ points in the plane: the supremum of the
$\alpha \in [0, \pi]$ such that every set of $N$ points in the plane contains three distinct points
$x, y, z$ with $\angle xyz \ge \alpha$ (the angle at $y$). Then $\alpha_3 = \pi/3$,
$\alpha_4 = \pi/2$, and for all natural numbers $n \ge 2$ and $N$: if $2^n < N \le 2^n + 2^{n-2}$,
then $\alpha_N = \left(1 - \frac{2}{2n + 1}\right)\pi$, and if $2^n + 2^{n-2} < N \le 2^{n+1}$,
then $\alpha_N = \left(1 - \frac{1}{n + 1}\right)\pi$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #504, https://www.erdosproblems.com/504 (status SOLVED); resolution: Bl. Sendov, Minimax of the angles in a plane configuration of points, Acta Math. Hungar. 69 (1995), 27-46, main theorem, as stated in Zbl 0853.52009: α(N) = (1 - 2/(2n+1))π for 2^n < N ≤ 2^n + 2^{n-2} and (1 - 1/(n+1))π for 2^n + 2^{n-2} < N ≤ 2^{n+1}, n ≥ 2; α(3) = π/3, α(4) = π/2, https://doi.org/10.1007/BF01874605.

Stated but not proved: `MathlibExt.Combinatorics.BlumenthalMinimaxAngleErdosProblem504Wanted.minimaxAngleValues_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/BlumenthalMinimaxAngleErdosProblem504Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BlumenthalMinimaxAngleErdosProblem504Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/blumenthal-s-minimax-angle-problem/index.html#minimax-angle-values-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Blumenthal's minimax angle problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/blumenthal-s-minimax-angle-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/blumenthal-s-minimax-angle-problem)
