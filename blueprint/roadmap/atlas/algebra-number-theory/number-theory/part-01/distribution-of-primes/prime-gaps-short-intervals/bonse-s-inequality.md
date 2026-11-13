---
declaration: section
origin: cited
lean: MetaMathlibExt.bonse_primes_infinite, MetaMathlibExt.bonse_nth_strictMono, MetaMathlibExt.bonse_nth_prime, MetaMathlibExt.bonse_nth_five, MetaMathlibExt.bonse_nth_succ_lt, MetaMathlibExt.bonse_inequality, MathlibExt.NumberTheory.BonseWanted.primeNth, MathlibExt.NumberTheory.BonseWanted.IsBonseSeq
statement: formalized
---

# Bonse's inequality

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html).

## Infinitely many primes

The set of prime natural numbers is infinite.

Here a natural number $p$ is prime in the sense of prime elements of a commutative monoid with
zero: $p$ is neither $0$ nor a unit, and $p \mid ab$ implies $p \mid a$ or $p \mid b$. For natural
numbers this agrees with the usual notion of a prime number.

Formalized by `MetaMathlibExt.bonse_primes_infinite`, a theorem declared in [MathlibExt/NumberTheory/BonseInequality.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BonseInequality.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#bonse-primes-infinite).

## The enumeration of the primes is strictly increasing

For $k \ge 1$ let $p_k$ be the
$k$-th smallest prime number. If $i < j$, then $p_i < p_j$.

Formalized by `MetaMathlibExt.bonse_nth_strictMono`, a theorem declared in [MathlibExt/NumberTheory/BonseInequality.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BonseInequality.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#bonse-nth-strict-mono).

## The enumeration of the primes takes prime values

For every $k \ge 1$, the $k$-th
smallest prime number exists and is prime.

Formalized by `MetaMathlibExt.bonse_nth_prime`, a theorem declared in [MathlibExt/NumberTheory/BonseInequality.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BonseInequality.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#bonse-nth-prime).

## The sixth prime is thirteen

The sixth prime number, counting $2$ as the first, is $13$.

Formalized by `MetaMathlibExt.bonse_nth_five`, a theorem declared in [MathlibExt/NumberTheory/BonseInequality.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BonseInequality.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#bonse-nth-five).

## Bertrand's postulate for consecutive primes

Let $p_1 < p_2 < p_3 < \cdots$ be the prime
numbers in increasing order. For every $k \ge 1$, $p_{k+1} < 2 p_k$.

Formalized by `MetaMathlibExt.bonse_nth_succ_lt`, a theorem declared in [MathlibExt/NumberTheory/BonseInequality.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BonseInequality.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#bonse-nth-succ-lt).

## Bonse's inequality

Let $p_1 = 2, p_2 = 3, p_3 = 5, \dots$ be the prime numbers in
increasing order. For every natural number $k > 4$, the square of the $(k+1)$-st prime is
smaller than the product of the first $k$ primes: $p_{k+1}^2 < p_1 p_2 \cdots p_k$.

## Sources

- Robert J. Betts, "Using Bonse's Inequality to Find Upper Bounds on Prime Gaps," Journal of Integer Sequences 10 (2007), Article 07.3.8, Proposition [Bonse's inequality], lines 142–148, <https://cs.uwaterloo.ca/journals/JIS/VOL10/Betts/betts7.tex>.

Formalized by `MetaMathlibExt.bonse_inequality`, a theorem declared in [MathlibExt/NumberTheory/BonseInequality.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BonseInequality.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#bonse-inequality).

## The $m$-th prime, counted from one

For $m \ge 1$, $p_m$ is the $m$-th prime, so that
$p_1 = 2$, $p_2 = 3$, $p_3 = 5$; at $m = 0$ the value is also $2$.

Formalized by `MathlibExt.NumberTheory.BonseWanted.primeNth`, a definition declared in [WantedExt/NumberTheory/BonseSequenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BonseSequenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#prime-nth).

## Bonse sequence of prime indices

For $m \ge 1$ let $p_m$ be the $m$-th prime, so that
$p_1 = 2$, and set $p_0 = 2$. A sequence $a_0, a_1, a_2, \ldots$ of natural numbers is a Bonse
sequence if $p_{a_n}^2 < p_{a_0} p_{a_1} \cdots p_{a_{n-1}}$ for all sufficiently large $n$.

In the paper's 1-based indexing the condition reads $p_{a_1} \cdots p_{a_n} > p_{a_{n+1}}^2$ for
all sufficiently large $n$.

Formalized by `MathlibExt.NumberTheory.BonseWanted.IsBonseSeq`, a definition declared in [WantedExt/NumberTheory/BonseSequenceWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BonseSequenceWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#is-bonse-seq).

## A sufficient condition for a Bonse sequence

Let $a_0 < a_1 < a_2 < \cdots$ be a strictly
increasing sequence of positive integers and write $A_n = a_0 a_1 \cdots a_{n-1}$ for the product
of its first $n$ terms. If there is a real number $c > 2$ such that $\log A_n / \log a_n > c$ for
all sufficiently large $n$, then $a$ is a Bonse sequence.

The hypothesis is equivalent to $\liminf_n \log A_n / \log a_n > 2$, an infinite limit inferior
included. In the paper's 1-based indexing it reads $\liminf \log A_n / \log a_{n+1} > 2$ with
$A_n = a_1 \cdots a_n$.

## Sources

- Diego Marques, "Bonse's Inequality along Subsequences of Primes", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.BonseWanted.isBonseSeq_of_liminf_gt` is written with `theorem_wanted` in [WantedExt/NumberTheory/BonseSequenceWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BonseSequenceWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#is-bonse-seq-of-liminf-gt).

## A sufficient condition for a non-Bonse sequence

Let $a_0 < a_1 < a_2 < \cdots$ be a
strictly increasing sequence of positive integers and write $A_n = a_0 a_1 \cdots a_{n-1}$ for the
product of its first $n$ terms. Suppose that $(n + 1) \log \log a_n / \log a_{n+1} \to 0$ as
$n \to \infty$, and that there is a real number $c < 2$ such that $\log A_n / \log a_n < c$ for
infinitely many $n$. Then $a$ is not a Bonse sequence.

The second hypothesis is equivalent to $\liminf_n \log A_n / \log a_n < 2$. In the paper's
1-based indexing the hypotheses read $n \log \log a_n / \log a_{n+1} \to 0$ and
$\liminf \log A_n / \log a_{n+1} < 2$ with $A_n = a_1 \cdots a_n$.

## Sources

- Diego Marques, "Bonse's Inequality along Subsequences of Primes", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.BonseWanted.not_isBonseSeq_of_liminf_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/BonseSequenceWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BonseSequenceWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html#not-is-bonse-seq-of-liminf-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bonse's inequality](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bonse-s-inequality)
