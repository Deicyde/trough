---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook8Wanted.ScottishBookProblem8Claim, MathlibExt.Analysis.ScottishBook8Wanted.mazur8CauchyProduct_refuted
statement: formalized
---

# Averaged Cauchy products of convergent sequences

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/averaged-cauchy-products-of-convergent-sequences/index.html).

## The claim of Scottish Book Problem 8

This is the statement, asked about in form (b) of
Mazur's Problem 8 in the Scottish Book typescript, that every convergent sequence
$(z_n)_{n \ge 0}$ of real numbers can be written as
$z_n = \frac{1}{n+1} \sum_{k=0}^{n} x_k y_{n-k}$ for all $n \ge 0$, where $(x_n)_{n \ge 0}$
and $(y_n)_{n \ge 0}$ are convergent sequences of real numbers.

Indices are shifted to start at $0$.

Formalized by `MathlibExt.Analysis.ScottishBook8Wanted.ScottishBookProblem8Claim`, a definition declared in [WantedExt/Analysis/ScottishBook8Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook8Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/averaged-cauchy-products-of-convergent-sequences/index.html#scottish-book-problem8-claim).

## Mazur's Problem 8 has a negative answer

There is a convergent sequence
$(z_n)_{n \ge 0}$ of real numbers that cannot be written as
$z_n = \frac{1}{n+1} \sum_{k=0}^{n} x_k y_{n-k}$ for all $n \ge 0$ with convergent sequences
$(x_n)_{n \ge 0}$ and $(y_n)_{n \ge 0}$ of real numbers. That is, the claim of Scottish Book
Problem 8 is false.

## Sources

- S. Mazur, Problem 8 of the Scottish Book; negative solution by V. V. Peller, "On S. Mazur's Problems 8 and 88 from the Scottish Book", arXiv:math/0703716, building on Peller, J. Operator Theory 7 (1982) 341-372; independently Kwapien-Pelczynski and Eggermont-Leung, Proc. Amer. Math. Soc. 96 (1986) 269-274.

Stated but not proved: `MathlibExt.Analysis.ScottishBook8Wanted.mazur8CauchyProduct_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook8Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook8Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/averaged-cauchy-products-of-convergent-sequences/index.html#mazur8-cauchy-product-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Averaged Cauchy products of convergent sequences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/averaged-cauchy-products-of-convergent-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/convergence/averaged-cauchy-products-of-convergent-sequences)
