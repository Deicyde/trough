---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.IsUnitStepWalk, MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.HasThreeAP, MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.unitStepWalkThreeAPIff, MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.unitStepWalkThreeAPIff_holds
statement: formalized
---

# Three-term progressions in unit-step walks

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks/index.html).

## Unit-step walks

Let $d$ be a natural number. A sequence
$a_0, a_1, a_2, \dots$ of points of $\mathbb{R}^d$ is a unit-step walk when for every $i$ the
step $a_{i+1} - a_i$ is a standard unit vector $e_j$ of $\mathbb{R}^d$ for some $j$.

Formalized by `MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.IsUnitStepWalk`, a definition declared in [WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks/index.html#is-unit-step-walk).

## Three-term arithmetic progressions in a sequence of points

Let $d$ be a natural number
and let $a_0, a_1, a_2, \dots$ be a sequence of points of $\mathbb{R}^d$. The sequence contains a
three-term arithmetic progression when there are indices $i$, $j$, $k$ with $a_i \ne a_j$ and
$a_i + a_k = 2 a_j$.

Formalized by `MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.HasThreeAP`, a definition declared in [WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks/index.html#has-three-ap).

## Erdős Problem 192 on three-term progressions in unit-step walks

The statement that for
every natural number $d$, every sequence $a_0, a_1, a_2, \dots$ of points of $\mathbb{R}^d$ whose
steps $a_{i+1} - a_i$ are all standard unit vectors contains a three-term arithmetic progression
(indices $i$, $j$, $k$ with $a_i \ne a_j$ and $a_i + a_k = 2 a_j$) if and only if $d \le 3$.

Formalized by `MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.unitStepWalkThreeAPIff`, a definition declared in [WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks/index.html#unit-step-walk-three-apiff).

## Solution of Erdős Problem 192 on three-term progressions in unit-step walks

For every
natural number $d$, every sequence $a_0, a_1, a_2, \dots$ of points of $\mathbb{R}^d$ whose steps
$a_{i+1} - a_i$ are all standard unit vectors contains a three-term arithmetic progression
(indices $i$, $j$, $k$ with $a_i \ne a_j$ and $a_i + a_k = 2 a_j$) if and only if $d \le 3$.

Points $a_i, a_j, a_k$ form a progression exactly when the step words from $i$ to $j$ and from
$j$ to $k$ are permutations of each other (an abelian square). Over at most three letters every
long enough word contains an abelian square, and Keränen's infinite abelian-square-free word over
four letters gives, for every $d \ge 4$, a walk with no three-term progression.
erdosproblems.com/192 lists the problem as solved.

## Sources

- T. F. Bloom, Erdős Problems, Problem #192, https://www.erdosproblems.com/192 (status SOLVED (LEAN)); resolution: V. Keränen, Abelian squares are avoidable on 4 letters, Automata, Languages and Programming (ICALP 1992), Lecture Notes in Comput. Sci. 623, Springer (1992), 41-52, erdosproblems.com/192: true for d ≤ 3 and false for d ≥ 4, via an infinite abelian-square-free word over 4 letters (Keränen), https://doi.org/10.1007/3-540-55719-9_62.

Stated but not proved: `MathlibExt.Combinatorics.UnitStepWalkThreeTermProgressionErdosProblem192Wanted.unitStepWalkThreeAPIff_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnitStepWalkThreeTermProgressionErdosProblem192Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks/index.html#unit-step-walk-three-apiff-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Three-term progressions in unit-step walks](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/three-term-progressions-in-unit-step-walks)
