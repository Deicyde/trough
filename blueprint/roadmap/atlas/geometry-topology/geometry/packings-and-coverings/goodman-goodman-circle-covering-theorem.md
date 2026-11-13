---
declaration: section
origin: cited
lean: MathlibExt.Geometry.ErdosProblem1121Wanted.conjecture, MathlibExt.Geometry.ErdosProblem1121Wanted.conjecture_holds
statement: formalized
---

# Goodman–Goodman circle covering theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/goodman-goodman-circle-covering-theorem/index.html).

## Erdős Problem 1121 (circle covering)

Write $B(c, r)$ for the closed ball with centre
$c$ and radius $r$ in Euclidean space $\mathbb{R}^d$. Call balls $B(c_1, r_1), \dots,
B(c_n, r_n)$ in $\mathbb{R}^d$ *nonseparable* if for every nonzero vector $v$ and every real
$t$ such that no point $p$ of any of the balls satisfies $\langle v, p \rangle = t$, either
$\langle v, c_i \rangle < t$ for all $i$ or $\langle v, c_i \rangle > t$ for all $i$. The
statement is the conjunction of two parts. First, for every natural number $n$, all points
$c_1, \dots, c_n \in \mathbb{R}^2$ and all reals $r_1, \dots, r_n > 0$ such that the discs
$B(c_i, r_i)$ are nonseparable, there is a point $z$ such that the closed disc
$B(z, r_1 + \dots + r_n)$ contains every $B(c_i, r_i)$. Second, the same holds in
$\mathbb{R}^d$ for every natural number $d$, with closed balls in place of discs.

Formalized by `MathlibExt.Geometry.ErdosProblem1121Wanted.conjecture`, a definition declared in [WantedExt/Geometry/ErdosProblem1121Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ErdosProblem1121Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/goodman-goodman-circle-covering-theorem/index.html#conjecture).

## Circle covering theorem (Erdős Problem 1121)

Both parts of Erdős Problem 1121 hold. For
every natural number $d$, and in particular in the plane ($d = 2$): if $B(c_1, r_1), \dots,
B(c_n, r_n)$ are closed balls in Euclidean space $\mathbb{R}^d$ with centres $c_i$ and radii
$r_i > 0$ such that every hyperplane meeting none of the balls has all the centres $c_i$
strictly on the same side, then some closed ball of radius $r_1 + \dots + r_n$ contains all of
the balls.

Goodman and Goodman [GoGo45] proved this in the plane and in higher dimensions; Hadwiger [Ha47]
extended it to convex bodies.

## Sources

- Goodman and Goodman [GoGo45] (planar case and higher dimensions), per erdosproblems.com/1121, https://www.erdosproblems.com/1121.

Stated but not proved: `MathlibExt.Geometry.ErdosProblem1121Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/ErdosProblem1121Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ErdosProblem1121Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/goodman-goodman-circle-covering-theorem/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Goodman–Goodman circle covering theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/packings-and-coverings/goodman-goodman-circle-covering-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/packings-and-coverings/goodman-goodman-circle-covering-theorem)
