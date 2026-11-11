---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook108Wanted.IsSchauderBasis, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook108Wanted.krein_basis_in_dense_set
statement: formalized
---

# Schauder bases

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/schauder-bases/index.html).

## Schauder basis

A sequence $(e_n)_{n \ge 0}$ in a real normed space $E$ is a Schauder
basis when for every $x \in E$ there is exactly one sequence of real numbers $(a_n)_{n \ge 0}$
such that the partial sums $\sum_{i < N} a_i e_i$ converge to $x$ as $N \to \infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook108Wanted.IsSchauderBasis`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook108Wanted.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook108Wanted.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/schauder-bases/index.html#is-schauder-basis).

## Krein's theorem on bases in dense sets

Let $E$ be a real Banach space that has a Schauder
basis. Then for every dense subset $H \subseteq E$ there is a Schauder basis $(e_n)_{n \ge 0}$ of
$E$ with $e_n \in H$ for all $n$, and likewise for every dense linear subspace $S \subseteq E$
there is a Schauder basis $(e_n)_{n \ge 0}$ of $E$ with $e_n \in S$ for all $n$.

## Sources

- S. Banach, S. Mazur, S. Ulam, Problem 108 of the Scottish Book; affirmative answer (Krein), typescript addendum Ad 108.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook108Wanted.krein_basis_in_dense_set` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook108Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook108Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/schauder-bases/index.html#krein-basis-in-dense-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schauder bases](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/schauder-bases/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/schauder-bases)
