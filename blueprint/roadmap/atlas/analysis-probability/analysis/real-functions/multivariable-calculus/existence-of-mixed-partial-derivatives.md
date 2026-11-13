---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.ScottishBook66Wanted.ScottishBookProblem66Claim, MathlibExt.Analysis.Calculus.ScottishBook66Wanted.mazur66_refuted
statement: formalized
---

# Existence of mixed partial derivatives

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/existence-of-mixed-partial-derivatives/index.html).

## Mazur's mixed partial derivatives claim

This is the following statement, the claim of
Mazur's Problem 66 from the Scottish Book. Let $Q = (0, 1) \times (0, 1)$ be the open unit square.
For every function $f : \mathbb{R}^2 \to \mathbb{R}$ such that, at every point $(x, y) \in Q$, the
functions $s \mapsto f(s, y)$ and $s \mapsto f(x, s)$ are differentiable at $x$ and at $y$
respectively, and their derivatives $\partial_x f(\cdot, y)$ and $\partial_y f(x, \cdot)$ are
again differentiable at $x$ and at $y$ respectively, the mixed partial derivative
$\partial_x \partial_y f$ exists at almost every point of $Q$ for Lebesgue measure: for almost
every $(x, y) \in Q$, the function $s \mapsto \partial_y f(s, y)$ is differentiable at $x$.

Mazur asked whether a function with first partial derivatives and both pure second partial
derivatives must have its mixed second partial derivatives almost everywhere; the claim asks this
only for $\partial_x \partial_y f$.

Formalized by `MathlibExt.Analysis.Calculus.ScottishBook66Wanted.ScottishBookProblem66Claim`, a definition declared in [WantedExt/Analysis/Calculus/ScottishBook66Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/ScottishBook66Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/existence-of-mixed-partial-derivatives/index.html#scottish-book-problem66-claim).

## Mazur's Problem 66 has a negative answer

Mazur's mixed partial derivatives claim is false:
there is a function $f : \mathbb{R}^2 \to \mathbb{R}$ such that, at every point $(x, y)$ of the
open unit square $Q = (0, 1) \times (0, 1)$, the functions $s \mapsto f(s, y)$ and
$s \mapsto f(x, s)$ are differentiable at $x$ and at $y$ respectively, and their derivatives
$\partial_x f(\cdot, y)$ and $\partial_y f(x, \cdot)$ are again differentiable at $x$ and at $y$
respectively, but the set of points $(x, y) \in Q$ at which $s \mapsto \partial_y f(s, y)$ is not
differentiable at $x$ is not a Lebesgue null set.

## Sources

- S. Mazur, Problem 66 of the Scottish Book; refuted by V. Mykhaylyuk and A. Plichko, who construct a separately twice differentiable function on `[0, 1]²` and a set of positive measure on which the mixed derivative `f_xy` does not exist ("On a Mazur problem from 'The Scottish Book' concerning second partial derivatives", Colloq. Math. 141 (2015), 175–181, arXiv:1508.06909).

Stated but not proved: `MathlibExt.Analysis.Calculus.ScottishBook66Wanted.mazur66_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/ScottishBook66Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/ScottishBook66Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/existence-of-mixed-partial-derivatives/index.html#mazur66-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Existence of mixed partial derivatives](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/existence-of-mixed-partial-derivatives/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/existence-of-mixed-partial-derivatives)
