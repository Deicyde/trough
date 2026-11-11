---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Asymptotics.BenderProductCoefficient.bender_product_coefficient_asymptotic_general, MathlibExt.Analysis.Asymptotics.BenderProductCoefficient.bender_product_coefficient_asymptotic
statement: formalized
proof: formalized
---

# Bender's lemma

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/bender-s-lemma/index.html).

## Bender's lemma without a radius condition on the second series

Let $(a_n)$ and $(b_n)$
be real sequences, let $A(z) = \sum_n a_n z^n$ have radius of convergence $\alpha \in [0, \infty]$,
and let $\beta \ge 0$ be a real number with $\beta < \alpha$. Suppose that $b_n \neq 0$ for all
sufficiently large $n$, that $b_{n-1} / b_n \to \beta$ as $n \to \infty$, and that
$A(\beta) \neq 0$. Then the coefficients $c_n = \sum_{k=0}^{n} a_k b_{n-k}$ of the product of the
formal power series $\sum_n a_n z^n$ and $\sum_n b_n z^n$ satisfy $c_n \sim A(\beta) \, b_n$ as
$n \to \infty$.

Unlike Bender's original lemma, nothing is assumed about the radius of convergence of
$\sum_n b_n z^n$.

Formalized by `MathlibExt.Analysis.Asymptotics.BenderProductCoefficient.bender_product_coefficient_asymptotic_general`, a theorem declared in [MathlibExt/Analysis/Asymptotics/BenderProductCoefficient.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/BenderProductCoefficient.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/bender-s-lemma/index.html#bender-product-coefficient-asymptotic-ge).

## Bender's lemma on coefficients of a product of power series

Let $(a_n)$ and $(b_n)$ be
real sequences such that $A(z) = \sum_n a_n z^n$ has radius of convergence $\alpha \in [0, \infty]$
and $\sum_n b_n z^n$ has radius of convergence $\beta$, where $\beta \ge 0$ is a real number with
$\beta < \alpha$. Suppose that $b_n \neq 0$ for all sufficiently large $n$, that
$b_{n-1} / b_n \to \beta$ as $n \to \infty$, and that $A(\beta) \neq 0$. Then the coefficients
$c_n = \sum_{k=0}^{n} a_k b_{n-k}$ of the product of the formal power series $\sum_n a_n z^n$ and
$\sum_n b_n z^n$ satisfy $c_n \sim A(\beta) \, b_n$ as $n \to \infty$.

The hypothesis that $b_n$ is eventually nonzero makes the ratios $b_{n-1} / b_n$ meaningful; with
the convention $x / 0 = 0$ the statement fails at $\beta = 0$ without it: for $A(z) = 1 + z$ and
$b$ vanishing at every even index and growing fast at odd indices, every ratio is $0$ while the
even product coefficients stay nonzero.

## Sources

- Dennis E. Davenport, Louis W. Shapiro, Lara K. Pudwell, and Leon C. Woodson, "The Boundary of Ordered Trees," Journal of Integer Sequences 18 (2015). Source file: <https://cs.uwaterloo.ca/journals/JIS/VOL18/Davenport/dav3.tex> (Bender's lemma, lines 521-523). It follows from `bender_product_coefficient_asymptotic_general`; the hypothesis `hB` is unused and keeps the source's shape.

Formalized by `MathlibExt.Analysis.Asymptotics.BenderProductCoefficient.bender_product_coefficient_asymptotic`, a theorem declared in [MathlibExt/Analysis/Asymptotics/BenderProductCoefficient.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/BenderProductCoefficient.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/bender-s-lemma/index.html#bender-product-coefficient-asymptotic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bender's lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/bender-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/asymptotic-analysis/bender-s-lemma)
