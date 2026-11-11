---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook88Wanted.ScottishBookProblem88Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook88Wanted.mazur88_refuted
statement: formalized
---

# Summability of Hankel matrix entries

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/summability-of-hankel-matrix-entries/index.html).

## Scottish Book Problem 88 (Mazur)

The claim that every real sequence $(a_n)_{n \ge 0}$
with the following property satisfies $\sum_n n |a_n| < \infty$: for every real sequence
$(x_n)_{n \ge 0}$ with $|x_n| \le 1$ for all $n$, each series $\sum_n a_{m+n} x_n$ with $m \ge 0$
converges, as the limit of its partial sums, to some $L_m$, and $\sum_m |L_m| < \infty$.

The inner series is required to converge as a limit of partial sums, not absolutely, as in
Mazur's original question.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook88Wanted.ScottishBookProblem88Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook88Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook88Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/summability-of-hankel-matrix-entries/index.html#scottish-book-problem88-claim).

## Mazur's Scottish Book Problem 88 fails

The Scottish Book Problem 88 claim is false: there is
a real sequence $(a_n)_{n \ge 0}$ such that for every real sequence $(x_n)_{n \ge 0}$ with
$|x_n| \le 1$ for all $n$, each series $\sum_n a_{m+n} x_n$ with $m \ge 0$ converges, as the
limit of its partial sums, to some $L_m$, and $\sum_m |L_m| < \infty$, but $\sum_n n |a_n|$
diverges.

## Sources

- S. Mazur, Problem 88 of the Scottish Book; negative solution as an immediate consequence of Peller (1982), J. Operator Theory 7, 341-372, §5, via V. V. Peller, "On S. Mazur's Problems 8 and 88 from the Scottish Book", arXiv:math/0703716: a Hankel matrix in the injective tensor product need not have finite sum of moduli of its entries.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook88Wanted.mazur88_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook88Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook88Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/summability-of-hankel-matrix-entries/index.html#mazur88-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Summability of Hankel matrix entries](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/summability-of-hankel-matrix-entries/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/summability-of-hankel-matrix-entries)
