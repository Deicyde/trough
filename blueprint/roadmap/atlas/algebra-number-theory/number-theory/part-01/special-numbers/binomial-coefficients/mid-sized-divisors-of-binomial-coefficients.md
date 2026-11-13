---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.BinomialMidrangeDivisorWanted.conjecture, MathlibExt.NumberTheory.BinomialMidrangeDivisorWanted.conjecture_refuted
statement: formalized
---

# Mid-sized divisors of binomial coefficients

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/mid-sized-divisors-of-binomial-coefficients/index.html).

## Erdős Problem 387

The proposition that there is a real number $c > 0$ such that for all
natural numbers $n$ and $k$ with $1 \le k < n$, the binomial coefficient $\binom{n}{k}$ has a
divisor $d$ with $cn < d \le n$.

Formalized by `MathlibExt.NumberTheory.BinomialMidrangeDivisorWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/BinomialMidrangeDivisorWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialMidrangeDivisorWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/mid-sized-divisors-of-binomial-coefficients/index.html#conjecture).

## Erdős Problem 387 is false

There is no real number $c > 0$ such that for all natural
numbers $n$ and $k$ with $1 \le k < n$ the binomial coefficient $\binom{n}{k}$ has a divisor
$d$ with $cn < d \le n$.

This follows from Theorem 1.4 of Bui, Naprienko, Pratt and Zaharescu: for arbitrarily large
$k$ there are infinitely many $n$ such that $\binom{n}{k}$ has no divisor in the interval
$(241\, n \log\log k / \log k,\ n]$.

## Sources

- H. M. Bui, S. Naprienko, K. Pratt, A. Zaharescu, Binomial coefficients with divisors avoiding an interval, arXiv preprint (2026), arXiv:2605.21221, https://arxiv.org/abs/2605.21221.

Stated but not proved: `MathlibExt.NumberTheory.BinomialMidrangeDivisorWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomialMidrangeDivisorWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BinomialMidrangeDivisorWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/mid-sized-divisors-of-binomial-coefficients/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mid-sized divisors of binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/mid-sized-divisors-of-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/mid-sized-divisors-of-binomial-coefficients)
