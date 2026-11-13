---
declaration: section
origin: cited
lean: MetaMathlibExt.almostPrimeIndexSet, MetaMathlibExt.almostPrimeIndexSet_nil, MetaMathlibExt.mem_almostPrimeIndexSet_cons, MetaMathlibExt.nth_prime_dusart_bounds, MetaMathlibExt.summable_inv_almostPrimeIndexSet, MetaMathlibExt.tsum_inv_primes_of_semiprime_index_bounds, MetaMathlibExt.semiprime_count_asymptotic_expansion, MetaMathlibExt.semiprime_reciprocal_sum_explicit_estimate
statement: formalized
---

# Almost primes of almost prime index

22 results, 3 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html).

## Almost primes of almost prime index

For natural numbers $k_1, \dots, k_m$ with $m \ge 1$,
the set $N_{k_1 \cdots k_m}$ of natural numbers is defined by recursion on $m$: $N_{k_1}$ is the
set of $k_1$-almost primes (the $n \ne 0$ with exactly $k_1$ prime factors counted with
multiplicity), and for $m \ge 2$, $N_{k_1 \cdots k_m}$ is the set of the $i$th $k_1$-almost
primes, in increasing order and counted from $1$, for $i \ge 1$ in $N_{k_2 \cdots k_m}$. When
there are fewer than $i$ $k_1$-almost primes (only for $k_1 = 0$, where $1$ is the only one),
the $i$th one is taken to be $0$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Section 1 (definitions of `N_k`, `N_{j,k}`, and `N_{k_1 ⋯ k_m}`).

Formalized by `MetaMathlibExt.almostPrimeIndexSet`, a definition declared in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#almost-prime-index-set).

## Almost prime index sets with one index

For every natural number $k$, the almost prime
index set $N_k$ with the single index $k$ is the set of $k$-almost primes, the natural numbers
$n \ne 0$ with exactly $k$ prime factors counted with multiplicity.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Section 1 (definition of `N_k`).

Formalized by `MetaMathlibExt.almostPrimeIndexSet_nil`, a theorem declared in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#almost-prime-index-set-nil).

## Membership in an almost prime index set

For natural numbers $k$, $j$, $n$ and
$\ell_1, \dots, \ell_r$ (with $r \ge 0$), $n$ lies in the almost prime index set
$N_{k j \ell_1 \cdots \ell_r}$ if and only if there is an $i \ge 1$ in $N_{j \ell_1 \cdots \ell_r}$
such that $n$ is the $i$th $k$-almost prime in increasing order, counted from $1$ (taken to be $0$
if there are fewer than $i$ of them).

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Section 1 (definition of `N_{k_1 ⋯ k_m}`).

Formalized by `MetaMathlibExt.mem_almostPrimeIndexSet_cons`, a theorem declared in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#mem-almost-prime-index-set-cons).

## Dusart's bounds for the $n$th prime

For $n \ge 1$ let $p_n$ denote the $n$th prime, so
that $p_1 = 2$, and let $\log$ be the natural logarithm. For every natural number $n \ge 2$,

$$
p_n \ge n (\log n + \log \log n - 1)
$$

and

$$
p_n \ge n \left( \log n + \log \log n - 1 + \frac{\log \log n - 2.25}{\log n} \right),
$$

and for every natural number $n \ge 39017$,

$$
p_n \le n (\log n + \log \log n - 0.9484).
$$

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Lemma 4 (quoting Dusart).

Stated but not proved: `MetaMathlibExt.nth_prime_dusart_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#nth-prime-dusart-bounds).

## Convergence of reciprocal sums over almost primes of almost prime index

A $k$-almost
prime is a positive integer with exactly $k$ prime factors counted with multiplicity. For positive
integers $k_1, \dots, k_m$ let $N_{k_1}$ be the set of $k_1$-almost primes and, for $m \ge 2$, let
$N_{k_1 k_2 \cdots k_m}$ be the set of $k_1$-almost primes whose index in the increasing
enumeration of the $k_1$-almost primes (starting at $1$) lies in $N_{k_2 \cdots k_m}$. Then for
every $m \ge 2$ and all positive integers $k_1, \dots, k_m$ the series
$\sum_{n \in N_{k_1 k_2 \cdots k_m}} 1/n$ converges.

In particular (the case $m = 2$), for all positive integers $j$ and $k$ the sum of the reciprocals
of the $j$-almost primes of $k$-almost prime index converges.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 5.

Stated but not proved: `MetaMathlibExt.summable_inv_almostPrimeIndexSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#summable-inv-almost-prime-index-set).

## Reciprocal sum of the primes of semiprime index

Let $N_{1,2}$ be the set of primes $p_i$
(indexed from $p_1 = 2$) whose index $i$ is a semiprime, that is, a product of two not
necessarily distinct primes. Then $0.9910 < \sum_{n \in N_{1,2}} 1/n < 0.9915$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 6.

Stated but not proved: `MetaMathlibExt.tsum_inv_primes_of_semiprime_index_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#tsum-inv-primes-of-semiprime-index-bound).

## Crişan–Erban expansion of the semiprime counting function

A semiprime is a product of
exactly two primes counted with multiplicity; for real $x$ let $N_2(x)$ be the number of semiprimes
at most $x$. Let $\beta$ be the Meissel–Mertens constant, $\gamma$ the Euler–Mascheroni constant
and $\log$ the natural logarithm. There are real constants $c_0, c_1, c_2, \dots$ with
$c_0 = \beta$ and

$$
c_1 = \beta - 1 - \gamma - \sum_{p} \frac{\log p}{p (p - 1)},
$$

the sum running over all primes $p$, such that for every natural number $N$, as $x \to \infty$,

$$
N_2(x) = \frac{x}{\log x} \sum_{n=0}^{N-1} \frac{n! \, (\log \log x + c_n)}{\log^n x} +
O_N\left( \frac{x \log \log x}{\log^{N+1} x} \right).
$$

The paper calls the $c_n$ explicit but displays only $c_0$ and $c_1$; the remaining constants are
only asserted to exist.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Lemma 1 (quoting Crişan and Erban).

Stated but not proved: `MetaMathlibExt.semiprime_count_asymptotic_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#semiprime-count-asymptotic-expansion).

## Explicit estimate for the reciprocal sum of the semiprimes

A semiprime is a product of
exactly two primes counted with multiplicity; for real $x$ let $S(x)$ be the sum of $1/n$ over the
semiprimes $n \le x$. Let $\beta$ be the Meissel–Mertens constant, $\gamma$ the Euler–Mascheroni
constant and $\log$ the natural logarithm, and put

$$
P(2) = \sum_{p} \frac{1}{p^2}, \qquad \zeta(2) = \frac{\pi^2}{6}, \qquad
\alpha_1 = \gamma + \sum_{p} \frac{\log p}{p (p - 1)},
$$

the sums running over all primes $p$. Then for every real $x > 1$ the error

$$
E(x) = S(x) - \frac{(\log \log x + \beta)^2}{2} - \frac{P(2) - \zeta(2)}{2} -
\frac{\alpha_1}{\log x}
$$

satisfies $|E(x)| < (\log x)^{-3/2}$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Lemma 2 (quoting Bayless et al.).

Stated but not proved: `MetaMathlibExt.semiprime_reciprocal_sum_explicit_estimate` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#semiprime-reciprocal-sum-explicit-estima).

## Erdős–Sárközy bound for almost primes

There is a real constant $C$ such that for every
integer $k \ge 1$ and every real $t \ge 1$, the number $\pi_{k+1}(t)$ of integers $n$ with
$1 \le n \le t$ that have exactly $k + 1$ prime factors, counted with multiplicity, satisfies
$\pi_{k+1}(t) \le C \cdot \frac{k^4}{2^k} \, t \log t$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Lemma 3 (quoting Erdős and Sárközy).

Stated but not proved: `MetaMathlibExt.almostPrime_count_le_erdos_sarkozy` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#almost-prime-count-le-erdos-sarkozy).

## Logarithmic expansions of the prime counting function

Let $\pi(x)$ be the number of
primes $p \le x$. As $x \to \infty$,

$$
\log \pi(x) = \log x - \log \log x + \frac{1}{\log x} + \frac{3}{2 (\log x)^2} +
O\left(\frac{1}{(\log x)^3}\right),
$$



$$
\log \log \pi(x) = \log \log x - \frac{\log \log x}{\log x} -
\frac{(\log \log x)^2}{2 (\log x)^2} + \frac{1}{(\log x)^2} +
O\left(\frac{(\log \log x)^3}{(\log x)^3}\right),
$$

and

$$
\frac{1}{\log \pi(x)} - \frac{1}{\log x}\left(1 + \frac{\log \log x}{\log x} +
\frac{(\log \log x)^2 - 1}{(\log x)^2} + \frac{(\log \log x)^3}{(\log x)^3}\right) =
O\left(\frac{\log \log x}{(\log x)^4}\right).
$$

The last expansion is the paper's form, whose error term $O(\log \log x / (\log x)^3)$ sits
inside the parentheses, multiplied out by the factor $1/\log x$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Lemma 5.

Stated but not proved: `MetaMathlibExt.log_primeCounting_asymptotics` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#log-prime-counting-asymptotics).

## Expansion of the reciprocal logarithm of the semiprime count

Let $\pi_2(x)$ be the
number of integers $n$ with $1 \le n \le x$ that have exactly two prime factors counted with
multiplicity, and let $\beta$ be the Meissel–Mertens constant. Then, as $x \to \infty$,

$$
\frac{1}{\log \pi_2(x)} - \frac{1}{\log x}\left(1 + \frac{\log \log x}{\log x} -
\frac{\log \log \log x}{\log x} - \frac{\beta}{\log x \, \log \log x}\right) =
O\left(\frac{1}{(\log x)^2 (\log \log x)^2}\right).
$$

This is the paper's expansion, whose error term $O(1/(\log x \, (\log \log x)^2))$ sits inside
the parentheses, multiplied out by the factor $1/\log x$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Lemma 6.

Stated but not proved: `MetaMathlibExt.inv_log_semiprime_count_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#inv-log-semiprime-count-asymptotic).

## Counting primes of semiprime index

A semiprime is a product of exactly two primes counted
with multiplicity. Let $p_i$ denote the $i$th prime ($p_1 = 2$), and for real $x$ let $N_{1,2}(x)$
be the number of primes $p_i \le x$ whose index $i$ is a semiprime. Let $\beta$ be the
Meissel–Mertens constant, $\gamma$ the Euler–Mascheroni constant, $\log$ the natural logarithm, and

$$
c_1 = \beta - 1 - \gamma - \sum_{p} \frac{\log p}{p (p - 1)},
$$

the sum running over all primes $p$. Then, as $x \to \infty$,

$$
N_{1,2}(x) = \frac{x}{\log^2 x} \left( \log \log x + \beta +
\frac{(\log \log x + \beta)(\log \log x + 1) + c_1}{\log x} \right) +
O\left( \frac{x (\log \log x)^3}{\log^4 x} \right).
$$

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 1.

Stated but not proved: `MetaMathlibExt.primes_of_semiprime_index_count_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#primes-of-semiprime-index-count-asymptot).

## Counting semiprimes of prime index

A semiprime is a product of exactly two primes counted
with multiplicity. Let $s_i$ denote the $i$th semiprime ($s_1 = 4$), and for real $x$ let
$N_{2,1}(x)$ be the number of semiprimes $s_i \le x$ whose index $i$ is prime. Let $\beta$ be the
Meissel–Mertens constant and $\log$ the natural logarithm. Then, as $x \to \infty$,

$$
N_{2,1}(x) = \frac{x}{\log^2 x} \left( \log \log x + \beta +
\frac{\log \log x \, (\log \log x - \log \log \log x)}{\log x} \right) +
O\left( \frac{x \log \log x}{\log^3 x} \right).
$$

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 2.

Stated but not proved: `MetaMathlibExt.semiprimes_of_prime_index_count_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#semiprimes-of-prime-index-count-asymptot).

## Primes of semiprime index eventually outnumber semiprimes of prime index

A semiprime is
a product of exactly two primes counted with multiplicity. Let $p_i$ denote the $i$th prime
($p_1 = 2$) and $s_i$ the $i$th semiprime ($s_1 = 4$). For real $x$ let $N_{1,2}(x)$ be the number
of primes $p_i \le x$ whose index $i$ is a semiprime, and $N_{2,1}(x)$ the number of semiprimes
$s_i \le x$ whose index $i$ is prime. Then $N_{2,1}(x) < N_{1,2}(x)$ for all sufficiently large
$x$, and, with $\log$ the natural logarithm, as $x \to \infty$

$$
N_{1,2}(x) - N_{2,1}(x) = \frac{x \log \log x \, \log \log \log x}{\log^3 x} +
O\left( \frac{x \log \log x}{\log^3 x} \right).
$$

This is the form
$\frac{x \log \log x \, \log \log \log x}{\log^3 x} (1 + O(1 / \log \log \log x))$ with the main
factor multiplied out.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Corollary 1.

Stated but not proved: `MetaMathlibExt.primes_of_semiprime_index_count_sub_semiprimes_of_prime_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#primes-of-semiprime-index-count-sub-semi).

## Counting almost primes of almost prime index

Let $j, k \ge 1$ be integers and, for real
$x$, let $N_{jk}(x)$ be the number of $j$-almost primes $n \le x$ whose index in the increasing
enumeration of the $j$-almost primes, counted from $1$, is a $k$-almost prime. Writing
$M(x) = \frac{x \, (\log \log x)^{j+k-2}}{(\log x)^2 \, (j-1)! \, (k-1)!}$, we have
$N_{jk}(x) - M(x) = O(M(x) / \log \log x)$ as $x \to \infty$.

The paper's clause "the same estimate holds for $N_{kj}$" is the instance with $j$ and $k$
swapped, since the main term is symmetric.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 3.

Stated but not proved: `MetaMathlibExt.almostPrimeIndexSet_pair_count_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#almost-prime-index-set-pair-count-asympt).

## Counting almost primes of iterated almost prime index

Let $m \ge 1$, let
$k_1, \dots, k_m$ be positive integers, let $N_{k_1 \cdots k_m}$ be the almost prime index set
(for $m = 1$ the $k_1$-almost primes, and for $m \ge 2$ the $k_1$-almost primes whose index in
increasing order, counted from $1$, lies in $N_{k_2 \cdots k_m}$), and for real $x$ let
$N_{k_1 \cdots k_m}(x)$ be the number of its elements $n \le x$. Writing
$M(x) = \frac{x}{(\log x)^m} \prod_{i=1}^m \frac{(\log \log x)^{k_i - 1}}{(k_i - 1)!}$, we have
$N_{k_1 \cdots k_m}(x) - M(x) = O(M(x) / \log \log x)$ as $x \to \infty$.

The paper's displayed exponent $k_1 + \cdots + k_{m-1} k_m - m$ is a typo for
$k_1 + \cdots + k_{m-1} + k_m - m$, as its equivalent product form shows.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 4.

Stated but not proved: `MetaMathlibExt.almostPrimeIndexSet_count_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#almost-prime-index-set-count-asymptotic).

## Size of the nth almost prime of almost prime index

Let $j, k \ge 1$ be integers and, for
$n \ge 1$, let $p_{j,k,n}$ be the $n$th element, in increasing order, of the set $N_{jk}$ of
$j$-almost primes whose index in the increasing enumeration of the $j$-almost primes, counted
from $1$, is a $k$-almost prime. Writing
$P(n) = \frac{n (\log n)^2 \, (j-1)! \, (k-1)!}{(\log \log n)^{j+k-2}}$, we have
$p_{j,k,n} - P(n) = O(P(n) / \log \log n)$ as $n \to \infty$ through the integers.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Corollary 2.

Stated but not proved: `MetaMathlibExt.nth_almostPrimeIndexSet_pair_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#nth-almost-prime-index-set-pair-asymptot).

## Size of the nth element of an iterated almost prime index set

Let $m \ge 1$, let
$k_1, \dots, k_m$ be positive integers, and for $n \ge 1$ let $p_{k_1, \dots, k_m, n}$ be the
$n$th element, in increasing order, of the almost prime index set $N_{k_1 \cdots k_m}$. Writing
$P(n) = n (\log n)^m \prod_{i=1}^m \frac{(k_i - 1)!}{(\log \log n)^{k_i - 1}}$, we have
$p_{k_1, \dots, k_m, n} - P(n) = O(P(n) / \log \log n)$ as $n \to \infty$ through the integers.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Corollary 3.

Stated but not proved: `MetaMathlibExt.nth_almostPrimeIndexSet_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#nth-almost-prime-index-set-asymptotic).

## Reciprocal sum of the primes of $k$-almost prime index

For $k \ge 0$ let $N_{1k}$ be
the set of primes $p_i$ (indexed from $p_1 = 2$) whose index $i$ is a $k$-almost prime, that is,
has exactly $k$ prime factors counted with multiplicity. Then
$\sum_{n \in N_{1k}} 1/n = 1 + O(e^{-k/2})$ as $k \to \infty$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 7.

Stated but not proved: `MetaMathlibExt.tsum_inv_primes_of_almostPrime_index_sub_one_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#tsum-inv-primes-of-almost-prime-index-su).

## Lower bound for reciprocal sums over almost primes of almost prime index

A $k$-almost
prime is a positive integer with exactly $k$ prime factors counted with multiplicity. For positive
integers $j$ and $k$ let $N_{jk}$ be the set of $j$-almost primes whose index in the increasing
enumeration of the $j$-almost primes (starting at $1$) is a $k$-almost prime. Fix an integer
$j \ge 1$. There is a real constant $c > 0$ such that

$$
\sum_{n \in N_{jk}} \frac{1}{n} \ge c \, k^{j-1}
$$

for all sufficiently large $k$. Moreover, if $j \ge 2$, then $\sum_{n \in N_{jk}} 1/n \to \infty$
as $k \to \infty$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 8.

Stated but not proved: `MetaMathlibExt.tsum_inv_almostPrimeIndexSet_pair_lower_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#tsum-inv-almost-prime-index-set-pair-low).

## Exponential decay of reciprocal sums over triple almost prime index sets

A $k$-almost
prime is a positive integer with exactly $k$ prime factors counted with multiplicity. For positive
integers $a$ and $b$ let $N_{ab}$ be the set of $a$-almost primes whose index in the increasing
enumeration of the $a$-almost primes (starting at $1$) is a $b$-almost prime, and for positive
integers $k_1, k_2, k$ let $N_{k_1 k_2 k}$ be the set of $k_1$-almost primes whose index in the
increasing enumeration of the $k_1$-almost primes lies in $N_{k_2 k}$. Fix positive integers $k_1$
and $k_2$. Then, as $k \to \infty$,

$$
\sum_{n \in N_{k_1 k_2 k}} \frac{1}{n} = O\left( e^{-k/2} \right).
$$

This is the case $m = 2$ of the paper's bound $\ll (e^{k/2})^{-(m-1)}$ for the reciprocal sum of
$N_{k_1 \cdots k_m k}$, the only case its proof supports. For $m = 3$ and $k_1 = k_2 = k_3 = 1$,
with $p_n$ the $n$th prime, the single term $1/p_{p_{p_{2^k}}}$ is $\gg 2^{-k} k^{-3}$ because
$p_n < n (\log n + \log \log n)$ for $n \ge 6$, and $e^{k} 2^{-k} k^{-3} \to \infty$, so the
printed bound fails for $m = 3$.

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 9, case `m = 2`.

Stated but not proved: `MetaMathlibExt.tsum_inv_almostPrimeIndexSet_triple_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#tsum-inv-almost-prime-index-set-triple-i).

## Reciprocal sums over iterated almost prime index sets tend to zero

A $k$-almost prime is
a positive integer with exactly $k$ prime factors counted with multiplicity. For positive integers
$k_1, \dots, k_m$ let $N_{k_1}$ be the set of $k_1$-almost primes and, for $m \ge 2$, let
$N_{k_1 k_2 \cdots k_m}$ be the set of $k_1$-almost primes whose index in the increasing
enumeration of the $k_1$-almost primes (starting at $1$) lies in $N_{k_2 \cdots k_m}$. Fix
$m \ge 2$ and positive integers $k_1, \dots, k_m$. Then

$$
\lim_{k \to \infty} \sum_{n \in N_{k_1 \cdots k_m k}} \frac{1}{n} = 0.
$$

## Sources

- Paul Kinlaw, Megan Triplett, and William Tripp, *Almost Primes of Almost Prime Index*, INTEGERS 24 (2024), Article A99, Theorem 9, "in particular" clause.

Stated but not proved: `MetaMathlibExt.tendsto_tsum_inv_almostPrimeIndexSet_append_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlmostPrimeIndexWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html#tendsto-tsum-inv-almost-prime-index-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost primes of almost prime index](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/almost-primes-of-almost-prime-index)
