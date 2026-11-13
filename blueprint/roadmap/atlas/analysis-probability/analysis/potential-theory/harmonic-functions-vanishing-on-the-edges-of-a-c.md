---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook151Wanted.Cube, MathlibExt.Analysis.ScottishBook151Wanted.CubeEdges, MathlibExt.Analysis.ScottishBook151Wanted.harmonicFunctionVanishesOnCubeEdges
statement: formalized
---

# Harmonic functions vanishing on the edges of a cube

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-functions-vanishing-on-the-edges-of-a-c/index.html).

## The closed cube $(-1, 1)^3$

The closed cube $[-1, 1]^3$ in $\mathbb{R}^3$: the set of
points of three-dimensional Euclidean space all of whose coordinates lie in $[-1, 1]$.

Formalized by `MathlibExt.Analysis.ScottishBook151Wanted.Cube`, a definition declared in [WantedExt/Analysis/ScottishBook151Wanted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook151Wanted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-functions-vanishing-on-the-edges-of-a-c/index.html#cube).

## Edges of the cube $(-1, 1)^3$

The union of the edges of the cube $[-1, 1]^3$ in
$\mathbb{R}^3$: the set of points $x$ with every coordinate in $[-1, 1]$ such that at least two
distinct coordinates $x_i$ and $x_j$ are each equal to $1$ or $-1$.

Formalized by `MathlibExt.Analysis.ScottishBook151Wanted.CubeEdges`, a definition declared in [WantedExt/Analysis/ScottishBook151Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook151Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-functions-vanishing-on-the-edges-of-a-c/index.html#cube-edges).

## Scottish Book Problem 151: a harmonic function vanishing on the edges of a cube

There
exist an open set $U \subseteq \mathbb{R}^3$ whose interior contains the closed cube
$[-1, 1]^3$ and a function $f : \mathbb{R}^3 \to \mathbb{R}$ that is harmonic at every point of
$U$, vanishes at every point of the edges of the cube $[-1, 1]^3$, and satisfies $f(x) \neq 0$
for some $x \in U$.

## Sources

- R. Wavre, Problem 151 of the Scottish Book; the affirmative answer is given by I. Vasilyev, "On the zero sets of harmonic polynomials", arXiv:2506.24116, Theorem 1, as reported in the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867). The typescript notes a prize of a "fondue" in Geneva.

Stated but not proved: `MathlibExt.Analysis.ScottishBook151Wanted.harmonicFunctionVanishesOnCubeEdges` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook151Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook151Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-functions-vanishing-on-the-edges-of-a-c/index.html#harmonic-function-vanishes-on-cube-edges).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Harmonic functions vanishing on the edges of a cube](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/harmonic-functions-vanishing-on-the-edges-of-a-c/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/potential-theory/harmonic-functions-vanishing-on-the-edges-of-a-c)
