---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook91Wanted.ScottishBookProblem91Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook91Wanted.mazur91_refuted
statement: formalized
---

# Normed spaces isometric to their duals

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/normed-spaces-isometric-to-their-duals/index.html).

## Mazur's Problem 91 (Scottish Book), Banach-space form

This is the proposition that
every finite-dimensional real normed space $E$ that is linearly isometric to its dual
space $E^*$ (the continuous linear functionals on $E$ with the operator norm) is an inner
product space, that is, its norm is induced by some inner product on $E$.

Mazur's original formulation asks whether, for every $n$, a convex body in $\mathbb{R}^n$
that is affinely equivalent to its conjugate (polar) body is necessarily an ellipsoid.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook91Wanted.ScottishBookProblem91Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook91Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook91Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/normed-spaces-isometric-to-their-duals/index.html#scottish-book-problem91-claim).

## Mazur's Problem 91 has a negative answer

There is a finite-dimensional real normed
space $E$ that is linearly isometric to its dual space $E^*$ (the continuous linear
functionals on $E$ with the operator norm) but whose norm is not induced by any inner
product on $E$. Thus the Banach-space form of Mazur's Problem 91 is false.

## Sources

- S. Mazur, Problem 91 of the Scottish Book. The typescript itself records the negative answer when `n` is even (for example, `ℓ¹ 2`, whose unit ball is a diamond, is linearly isometric to its dual `ℓ^∞ 2` but is not a Hilbert space, since its norm does not satisfy the parallelogram law); the odd-dimensional case is not needed to refute the universal claim.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook91Wanted.mazur91_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook91Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook91Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/normed-spaces-isometric-to-their-duals/index.html#mazur91-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normed spaces isometric to their duals](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/normed-spaces-isometric-to-their-duals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/normed-spaces-isometric-to-their-duals)
