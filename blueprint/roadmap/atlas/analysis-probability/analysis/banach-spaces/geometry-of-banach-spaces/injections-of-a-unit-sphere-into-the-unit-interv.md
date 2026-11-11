---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook144Wanted.ScottishBookProblem144Claim, MathlibExt.Analysis.ScottishBook144Wanted.mazurUlam144_refuted
statement: formalized
---

# Injections of a unit sphere into the unit interval

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/injections-of-a-unit-sphere-into-the-unit-interv/index.html).

## Scottish Book Problem 144 (Mazur–Ulam), as a claim

For every separable real Banach
space $E$, with unit sphere $K = \{x \in E : \|x\| = 1\}$, there is an injective map
$f \colon K \to [0, 1]$ such that for every nonempty open subset $U$ of $K$ the image $f(U)$ has
positive Lebesgue outer measure.

Mazur and Ulam ask, in a separable Banach space, whether such a map exists.

Formalized by `MathlibExt.Analysis.ScottishBook144Wanted.ScottishBookProblem144Claim`, a definition declared in [WantedExt/Analysis/ScottishBook144Wanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook144Wanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/injections-of-a-unit-sphere-into-the-unit-interv/index.html#scottish-book-problem144-claim).

## Scottish Book Problem 144 is false as stated

The Scottish Book Problem 144 claim fails: some
separable real Banach space $E$ admits no injective map $f$ from its unit sphere $K$ to $[0, 1]$
such that the image under $f$ of every nonempty open subset of $K$ has positive Lebesgue outer
measure.

For example, take $E = \mathbb{R}$: its unit sphere is $\{-1, 1\}$, so $U = \{1\}$ is a nonempty
open subset of $K$, and its image under any $f$ is a single point, of measure zero. The source
contains no dimension restriction (it says "infinite-dimensional" explicitly when it means it,
e.g. Problem 7), so none is added here.

## Sources

- S. Mazur and S. Ulam, Problem 144 of the Scottish Book, typescript p. 63 (printed), PDF p. 66; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.ScottishBook144Wanted.mazurUlam144_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook144Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook144Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/injections-of-a-unit-sphere-into-the-unit-interv/index.html#mazur-ulam144-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Injections of a unit sphere into the unit interval](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/injections-of-a-unit-sphere-into-the-unit-interv/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/injections-of-a-unit-sphere-into-the-unit-interv)
