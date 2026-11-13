---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.IsFullDimensional, MathlibExt.Combinatorics.StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.stanchescuDifferenceBound, MathlibExt.Combinatorics.StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.stanchescuDifferenceBound_holds
statement: formalized
---

# Difference sets of full-dimensional lattice sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/difference-sets-of-full-dimensional-lattice-sets/index.html).

## Full-dimensional sets in $\mathbb{Z}^d$

A finite set $A \subseteq \mathbb{Z}^d$ is
full-dimensional when it is not contained in an affine hyperplane: for every real vector
$a \in \mathbb{R}^d$ and every real number $c$, if $\sum_i a_i x_i = c$ for all $x \in A$, then
$a = 0$.

Formalized by `MathlibExt.Combinatorics.StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.IsFullDimensional`, a definition declared in [WantedExt/Combinatorics/StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/difference-sets-of-full-dimensional-lattice-sets/index.html#is-full-dimensional).

## Statement of Stanchescu's difference set bound

The proposition that for every integer
$d \ge 2$ there is a natural number $N$ such that every full-dimensional finite set
$A \subseteq \mathbb{Z}^d$ (one not contained in an affine hyperplane) with $|A| \ge N$ satisfies
$|A - A| \ge \left(2d - 2 + \frac{1}{d - 1}\right)|A| - (2d^2 - 4d + 3)$, where
$A - A = \{a - b : a, b \in A\}$ is the difference set of $A$.

Formalized by `MathlibExt.Combinatorics.StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.stanchescuDifferenceBound`, a definition declared in [WantedExt/Combinatorics/StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/difference-sets-of-full-dimensional-lattice-sets/index.html#stanchescu-difference-bound).

## Conlon–Lim theorem: Stanchescu's difference set bound holds

For every integer $d \ge 2$ there
is a natural number $N$ such that every finite set $A \subseteq \mathbb{Z}^d$ with $|A| \ge N$ that
is not contained in an affine hyperplane (no nonzero real linear functional is constant on $A$)
satisfies $|A - A| \ge \left(2d - 2 + \frac{1}{d - 1}\right)|A| - (2d^2 - 4d + 3)$, where
$A - A = \{a - b : a, b \in A\}$ is the difference set of $A$.

## Sources

- Problems presented at the workshop on recent trends in additive combinatorics, collected by E. Croot and V. F. Lev, AIM workshop problem list, Problem 2.6 (Y. Stanchescu), https://aimath.org/WWN/additivecomb/additivecomb.pdf; resolution: D. Conlon and J. Lim, Difference sets in ℝ^d, Israel J. Math. 267 (2025) 729-748, arXiv:2110.09053, abstract and main theorem, https://arxiv.org/abs/2110.09053.

Stated but not proved: `MathlibExt.Combinatorics.StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.stanchescuDifferenceBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StanchescuDifferenceSetsAIMCombinatoricsProblem231Wanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/difference-sets-of-full-dimensional-lattice-sets/index.html#stanchescu-difference-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Difference sets of full-dimensional lattice sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/difference-sets-of-full-dimensional-lattice-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/difference-sets-of-full-dimensional-lattice-sets)
