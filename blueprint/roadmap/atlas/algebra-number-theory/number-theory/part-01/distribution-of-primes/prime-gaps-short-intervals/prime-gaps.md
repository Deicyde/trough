---
declaration: section
origin: cited
lean: MetaMathlibExt.AreConsecutivePrimes, MetaMathlibExt.IsConsecutivePrimeBlock, MetaMathlibExt.IsRestrictedConsecutivePrimeBlock, primeGap, MathlibExt.NumberTheory.primeGapLiminf, MathlibExt.NumberTheory.consecutive_nth_prime, MathlibExt.NumberTheory.primeGap_pos, MathlibExt.NumberTheory.two_le_primeGap
statement: formalized
---

# Prime gaps

20 results, 18 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html).

## Consecutive primes

Natural numbers $p$ and $q$ are consecutive primes when $p$ and $q$
are prime, $p < q$, and every prime $r$ satisfies $r \le p$ or $q \le r$; that is, no prime
lies strictly between $p$ and $q$.

This is the usual meaning of successive primes $p_k, p_{k+1}$ used in the source papers.

## Sources

- * <https://cs.uwaterloo.ca/journals/JIS/VOL25/Krizek/krizek3.tex> * <https://cs.uwaterloo.ca/journals/JIS/VOL14/Noe/noe12.tex> * <https://cs.uwaterloo.ca/journals/JIS/VOL15/Shevelev/shevelev19.tex>

Formalized by `MetaMathlibExt.AreConsecutivePrimes`, a definition declared in [MathlibExt/NumberTheory/ConsecutivePrime.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ConsecutivePrime.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#are-consecutive-primes).

## Block of consecutive primes

A list $l$ of natural numbers is a block of consecutive
primes when $l$ is nonempty, every entry of $l$ is prime, $l$ is strictly increasing, and every
two adjacent entries of $l$ are consecutive primes.

## Sources

- see the sources cited on `AreConsecutivePrimes` for occurrences of blocks `pₖ, pₖ₊₁, …, pₘ` of consecutive primes.

Formalized by `MetaMathlibExt.IsConsecutivePrimeBlock`, a definition declared in [MathlibExt/NumberTheory/ConsecutivePrime.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ConsecutivePrime.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#is-consecutive-prime-block).

## Restricted block of consecutive primes

Let $P$ be a predicate on natural numbers. A list
$l$ of natural numbers is a block of consecutive primes restricted by $P$ when $l$ is a block of
consecutive primes and every entry of $l$ satisfies $P$.

This covers, for example, the factorial- and primorial-bounded blocks in the source papers by
choosing the corresponding predicate $P$.

Formalized by `MetaMathlibExt.IsRestrictedConsecutivePrimeBlock`, a definition declared in [MathlibExt/NumberTheory/ConsecutivePrime.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ConsecutivePrime.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#is-restricted-consecutive-prime-block).

## Prime gap

Let $p_0 = 2$, $p_1 = 3$, $p_2 = 5, \dots$ be the primes in increasing order,
indexed from $0$. For a natural number $n$, the prime gap at $n$ is $p_{n+1} - p_n$.

Formalized by `primeGap`, a definition declared in [MathlibExt/NumberTheory/PrimeGap.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGap.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap).

## Liminf of prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in increasing order
and let $g_n = p_{n+1} - p_n$ be the $n$-th prime gap. The liminf of prime gaps is
$\liminf_{n \to \infty} g_n$, taken in $\mathbb{N} \cup \{\infty\}$; the value $\infty$ is
allowed.

Formalized by `MathlibExt.NumberTheory.primeGapLiminf`, a definition declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap-liminf).

## Successive primes in the enumeration are consecutive

Let $p_0 < p_1 < p_2 < \cdots$ be
the primes in increasing order. For every $n \in \mathbb{N}$, $p_n$ and $p_{n+1}$ are consecutive
primes: both are prime, $p_n < p_{n+1}$, and no prime lies strictly between them.

Formalized by `MathlibExt.NumberTheory.consecutive_nth_prime`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#consecutive-nth-prime).

## Prime gaps are positive

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in increasing
order and let $g_n = p_{n+1} - p_n$ be the $n$-th prime gap. Then $g_n > 0$ for every
$n \in \mathbb{N}$, including $n = 0$.

Formalized by `MathlibExt.NumberTheory.primeGap_pos`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap-pos).

## Prime gaps after the first are at least two

Let $p_0 < p_1 < p_2 < \cdots$ be the primes
in increasing order and let $g_n = p_{n+1} - p_n$ be the $n$-th prime gap. For every $n \ge 1$,
$g_n \ge 2$.

Formalized by `MathlibExt.NumberTheory.two_le_primeGap`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#two-le-prime-gap).

## The liminf of prime gaps is at least two

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order and let $g_n = p_{n+1} - p_n$ be the $n$-th prime gap. Then
$\liminf_{n \to \infty} g_n \ge 2$, where the liminf is taken in $\mathbb{N} \cup \{\infty\}$.

Formalized by `MathlibExt.NumberTheory.two_le_primeGapLiminf`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#two-le-prime-gap-liminf).

## When the liminf of prime gaps is at most a given bound

Let $p_0 < p_1 < p_2 < \cdots$
be the primes in increasing order, let $g_n = p_{n+1} - p_n$ be the $n$-th prime gap, and let
$L = \liminf_{n \to \infty} g_n$, taken in $\mathbb{N} \cup \{\infty\}$. For every natural number
$B$, $L \le B$ if and only if $g_n \le B$ for infinitely many $n$.

Formalized by `MathlibExt.NumberTheory.primeGapLiminf_le_iff_infinite`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap-liminf-le-iff-infinite).

## Finite liminf of prime gaps and bounded gaps between primes

Let
$p_0 < p_1 < p_2 < \cdots$ be the primes in increasing order, let $g_n = p_{n+1} - p_n$ be the
$n$-th prime gap, and let $L = \liminf_{n \to \infty} g_n$, taken in $\mathbb{N} \cup \{\infty\}$.
Then $L \ne \infty$ if and only if there is a natural number $B > 0$ such that infinitely many
primes $p$ admit a prime $q$ with $p < q$ and $q - p \le B$.

Formalized by `MathlibExt.NumberTheory.primeGapLiminf_ne_top_iff_bounded_pairs`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap-liminf-ne-top-iff-bounded-pair).

## A prime gap equals two exactly at a twin prime

Let $p_0 < p_1 < p_2 < \cdots$ be the
primes in increasing order and let $g_n = p_{n+1} - p_n$ be the $n$-th prime gap. For every
$n \in \mathbb{N}$, $g_n = 2$ if and only if $p_n + 2$ is prime.

Formalized by `MathlibExt.NumberTheory.primeGap_eq_two_iff`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap-eq-two-iff).

## The liminf of prime gaps is two exactly when there are infinitely many twin primes

Let
$p_0 < p_1 < p_2 < \cdots$ be the primes in increasing order and let $g_n = p_{n+1} - p_n$ be the
$n$-th prime gap. Then $\liminf_{n \to \infty} g_n = 2$, taken in $\mathbb{N} \cup \{\infty\}$, if
and only if there are infinitely many primes $p$ such that $p + 2$ is also prime.

Formalized by `MathlibExt.NumberTheory.primeGapLiminf_eq_two_iff`, a theorem declared in [MathlibExt/NumberTheory/PrimeGapLiminf.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeGapLiminf.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-gap-liminf-eq-two-iff).

## Largest prime gap below $x$

Let $p_0 = 2 < p_1 = 3 < p_2 = 5 < \dots$ be the primes in
increasing order. For a real number $x$, $d(x)$ is the largest prime gap $p_{n+1} - p_n$ over all
$n$ with $p_n < x$ (the next prime $p_{n+1}$ may exceed $x$), and $d(x) = 0$ when no prime is
less than $x$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1138Wanted.supPrimeGap`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1138Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1138Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#sup-prime-gap).

## The regime $x \to \infty$ with $x/2 < y < x$

The filter on pairs $(x, y)$ of real
numbers along which $x \to \infty$ while $x/2 < y < x$: a set of pairs belongs to it exactly
when it contains every pair $(x, y)$ with $x/2 < y < x$ and $x$ sufficiently large.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1138Wanted.sndGtHalfFst`, an abbreviation declared in [WantedExt/NumberTheory/ErdosProblem1138Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1138Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#snd-gt-half-fst).

## Primes in a window of $C$ maximal prime gaps

Let $p_0 = 2 < p_1 = 3 < p_2 = 5 < \dots$
be the primes in increasing order, let $\pi$ be the prime-counting function, and for real $x$
let $d(x)$ be the largest prime gap $p_{n+1} - p_n$ over all $n$ with $p_n < x$, with
$d(x) = 0$ when no prime is less than $x$. For a real number $C$, this is the function on pairs
$(x, y)$ of real numbers given by $\pi(\lfloor y + C\,d(x) \rfloor) - \pi(\lfloor y \rfloor)$,
where the floors are taken in $\mathbb{N}$ (so negative numbers have floor $0$) and the
difference is taken in $\mathbb{R}$.

When $C \ge 0$ this is the number of primes in the interval $(y, y + C\,d(x)]$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1138Wanted.primeCountIocMulConst`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1138Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1138Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#prime-count-ioc-mul-const).

## Vardi's prime-gap asymptotic

Let $\pi$ be the prime-counting function and, for real $x$,
let $d(x)$ be the largest prime gap $p_{n+1} - p_n$ over the primes $p_n < x$. The proposition
states that for every real $C > 1$,

$$
\pi(\lfloor y + C\,d(x) \rfloor) - \pi(\lfloor y \rfloor) \sim \frac{C\,d(x)}{\log y}
$$

as $x \to \infty$ over pairs $(x, y)$ of reals with $x/2 < y < x$, where $\sim$ means that the
difference of the two sides is $o$ of the right-hand side.

This proposition is false (Erdős Problem 1138 was resolved in the negative).

Formalized by `MathlibExt.NumberTheory.ErdosProblem1138Wanted.vardiAsymptotic`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1138Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1138Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#vardi-asymptotic).

## Negation of Vardi's prime-gap asymptotic

The proposition that Vardi's prime-gap
asymptotic does not hold.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1138Wanted.disprovedVardi`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1138Wanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1138Wanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#disproved-vardi).

## Vardi's prime-gap asymptotic is false

Let $\pi$ be the prime-counting function and, for
real $x$, let $d(x)$ be the largest prime gap $p_{n+1} - p_n$ over the primes $p_n < x$. It is
not true that for every real $C > 1$,
$\pi(\lfloor y + C\,d(x) \rfloor) - \pi(\lfloor y \rfloor)$ is asymptotically equivalent to
$C\,d(x) / \log y$ as $x \to \infty$ over pairs $(x, y)$ with $x/2 < y < x$.

This resolves Erdős Problem 1138 in the negative (Sunder, Kumrawat and Cheri, with GPT 5.5;
the disproof is Lean-verified).

## Sources

- Sunder, Kumrawat, Cheri, and GPT 5.5 (Lean-verified disproof), per erdosproblems.com/1138, https://www.erdosproblems.com/1138; Hrishi Sunder, Sourish Kumrawat, and Kireet Cheri, An Elementary Obstruction to a Uniform Prime-Gap Asymptotic (2026), https://github.com/sourish-kumrawat/sourish-kumrawat.github.io/blob/adcbf7ea4e6f57b84001c372a7f8093c95fe7b10/papers/Erdos_1138.pdf; Lean disproof of Erdos Problem 1138, YanYablonovskiy/formal-conjectures, https://github.com/YanYablonovskiy/formal-conjectures/blob/7c134317104d3b98ecc751afbb79ec0adddf8e7c/FormalConjectures/ErdosProblems/1138a.lean#L497.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem1138Wanted.vardiAsymptotic_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem1138Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1138Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#vardi-asymptotic-refuted).

## Erdős Problem 6 (increasing prime gaps)

Let $p_0 = 2$, $p_1 = 3$, $p_2 = 5, \dots$ be the
primes in increasing order and let $d_n = p_{n+1} - p_n$ be the prime gap at $n$. There are
infinitely many natural numbers $n$ with $d_n < d_{n+1} < d_{n+2}$.

This was proved by Banks, Freiberg and Turnage-Butterbaugh using the Maynard–Tao machinery.

## Sources

- William D. Banks, Tristan Freiberg, and Caroline L. Turnage-Butterbaugh, Consecutive primes in tuples, Acta Arith. 167 (2015), 261-266; arXiv:1311.7003, https://arxiv.org/abs/1311.7003.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem6Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem6Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem6Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime gaps](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/prime-gaps)
