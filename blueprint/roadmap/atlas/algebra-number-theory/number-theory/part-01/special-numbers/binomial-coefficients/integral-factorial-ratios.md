---
declaration: section
origin: cited
lean: factorialProd, IsIntegralFactorialRatio, factorialProd_zero, factorialProd_dvd_zero, isIntegralFactorialRatio_iff, isIntegralFactorialRatio_perm_left, isIntegralFactorialRatio_perm_right, isIntegralFactorialRatio_perm
statement: formalized
---

# Integral factorial ratios

15 results, 13 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html).

## Product of scaled factorials

For a list $L$ of natural numbers and a natural number
$n$, the product of scaled factorials of $L$ at $n$ is $\prod_{a \in L} (an)!$, the product of the
factorials $(an)!$ over the entries $a$ of $L$, counted with multiplicity; for the empty list it
is $1$.

Formalized by `factorialProd`, a definition declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#factorial-prod).

## Integral factorial ratio

For lists $A = (a_1, \dots, a_k)$ and
$B = (b_1, \dots, b_l)$ of natural numbers, the pair $(A, B)$ is an integral
factorial ratio when every $a_i$ and every $b_j$ is positive,
$a_1 + \dots + a_k = b_1 + \dots + b_l$, and for every natural number $n$ the product
$(b_1 n)! \cdots (b_l n)!$ divides $(a_1 n)! \cdots (a_k n)!$; equivalently, the quotient
$\frac{(a_1 n)! \cdots (a_k n)!}{(b_1 n)! \cdots (b_l n)!}$ is a natural number.

## Sources

- K. Soundararajan, *Integral factorial ratios* (arXiv 1901.05133).

Formalized by `IsIntegralFactorialRatio`, a definition declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio).

## Scaled factorial product at index zero

For every list $L$ of natural numbers,
$\prod_{a \in L} (a \cdot 0)! = 1$, since every factor equals $0! = 1$.

Formalized by `factorialProd_zero`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#factorial-prod-zero).

## Scaled factorial products at index zero divide

For all lists $A$ and $B$ of natural
numbers, $\prod_{b \in B} (b \cdot 0)!$ divides $\prod_{a \in A} (a \cdot 0)!$, since both
products equal $1$.

Formalized by `factorialProd_dvd_zero`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#factorial-prod-dvd-zero).

## Characterization of integral factorial ratios

For lists $A$ and $B$ of natural numbers,
$(A, B)$ is an integral factorial ratio if and only if every entry of $A$ is positive, every
entry of $B$ is positive, the entries of $A$ and the entries of $B$ have the same sum, and for
every natural number $n$ the product $\prod_{b \in B} (bn)!$ divides $\prod_{a \in A} (an)!$.

Formalized by `isIntegralFactorialRatio_iff`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-iff).

## Permuting the numerator of an integral factorial ratio

Let $A$, $A'$ and $B$ be lists of
natural numbers such that $A'$ is a permutation of $A$. If $(A, B)$ is an integral factorial
ratio, then so is $(A', B)$.

Formalized by `isIntegralFactorialRatio_perm_left`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-perm-left).

## Permuting the denominator of an integral factorial ratio

Let $A$, $B$ and $B'$ be lists
of natural numbers such that $B'$ is a permutation of $B$. If $(A, B)$ is an integral factorial
ratio, then so is $(A, B')$.

Formalized by `isIntegralFactorialRatio_perm_right`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-perm-right).

## Integral factorial ratios are invariant under permutation

Let $A$, $A'$, $B$ and $B'$ be
lists of natural numbers such that $A'$ is a permutation of $A$ and $B'$ is a permutation of
$B$. If $(A, B)$ is an integral factorial ratio, then so is $(A', B')$.

Formalized by `isIntegralFactorialRatio_perm`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-perm).

## Equal tuples form an integral factorial ratio

If every entry of a list $L$ of natural
numbers is positive, then $(L, L)$ is an integral factorial ratio.

Formalized by `isIntegralFactorialRatio_refl`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-refl).

## Equal singletons form an integral factorial ratio

For every positive natural number
$c$, the one-entry tuples $(c)$ and $(c)$ form an integral factorial ratio.

Formalized by `isIntegralFactorialRatio_singleton_self`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-singleton-se).

## The central binomial factorial ratio is integral

The tuples $(2)$ and $(1, 1)$ form an
integral factorial ratio: their entries are positive, their sums agree ($2 = 1 + 1$), and for
every natural number $n$, $n! \cdot n!$ divides $(2n)!$.

Formalized by `isIntegralFactorialRatio_centralBinom`, a theorem declared in [MathlibExt/NumberTheory/FactorialRatio.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FactorialRatio.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#is-integral-factorial-ratio-central-bino).

## Erdős Problem 728

The proposition that there is a real number $\delta > 0$ such that for
every real number $\varepsilon$ with $0 < \varepsilon < \delta$ and all real numbers $C > 0$ and
$C' > C$, there are natural numbers $a$, $b$ and $n \ge 1$ with $a > \varepsilon n$,
$b > \varepsilon n$, $a! \, b! \mid n! \, (a + b - n)!$ and $n + C \log n < a + b < n + C' \log n$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem728Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem728Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem728Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#conjecture).

## Erdős Problem 728 holds

There is a real number $\delta > 0$ such that for every real number
$\varepsilon$ with $0 < \varepsilon < \delta$ and all real numbers $C > 0$ and $C' > C$, there are
natural numbers $a$, $b$ and $n \ge 1$ with $a > \varepsilon n$, $b > \varepsilon n$,
$a! \, b! \mid n! \, (a + b - n)!$ and $n + C \log n < a + b < n + C' \log n$.

The statement was resolved in the affirmative by Barreto and ChatGPT-5.2.

## Sources

- N. Sothanaphan, Resolution of Erdős Problem #728: a writeup of Aristotle's Lean proof, arXiv:2601.07421 (2026), https://arxiv.org/abs/2601.07421.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem728Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem728Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem728Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#conjecture-holds).

## Erdős Problem 729

The proposition that for every real number $C > 0$ there is a natural
number $K \ge 3$ such that there are infinitely many triples $(a, b, n)$ of positive integers with
$a + b > n + C \log n$ for which no prime $p > K$ divides the denominator of the rational number
$n! / (a! \, b!)$ in lowest terms.

Formalized by `MathlibExt.NumberTheory.ErdosProblem729Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem729Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem729Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#conjecture-2).

## Erdős Problem 729 holds

For every real number $C > 0$ there is a natural number $K \ge 3$
such that there are infinitely many triples $(a, b, n)$ of positive integers with
$a + b > n + C \log n$ for which no prime $p > K$ divides the denominator of the rational number
$n! / (a! \, b!)$ in lowest terms.

The statement was resolved in the affirmative by Barreto and Leeham.

## Sources

- External Lean proof of Erdős Problem 729, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos729.lean.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem729Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem729Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem729Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html#conjecture-holds-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integral factorial ratios](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/integral-factorial-ratios)
