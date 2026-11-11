---
declaration: section
origin: cited
lean: MetaMathlibExt.remainderSet, MetaMathlibExt.remainderCount, MetaMathlibExt.remainderCount_eleven, MetaMathlibExt.remainderCount_twelve, MetaMathlibExt.remainderConstant, MetaMathlibExt.remainderCount_asymptotic, MetaMathlibExt.remainderCount_drops_unbounded, MetaMathlibExt.remainderCount_consecutive_differences
statement: formalized
---

# Sets of remainders

15 results, 8 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html).

## Remainder set

For a natural number $n$, the remainder set is
$S(n) = \{\, n \bmod k : 1 \le k \le \lfloor n/2 \rfloor \,\}$, the set of remainders of $n$
modulo the integers from $1$ to $\lfloor n/2 \rfloor$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Section 1 (definition of `S(n)`).

Formalized by `MetaMathlibExt.remainderSet`, a definition declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-set).

## Remainder count

For a natural number $n$, $s(n)$ is the number of elements of the
remainder set $S(n)$, that is, the number of distinct values of $n \bmod k$ for
$1 \le k \le \lfloor n/2 \rfloor$ (OEIS A283190).

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Section 1 (definition of `s(n)`).

Formalized by `MetaMathlibExt.remainderCount`, a definition declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-count).

## The remainder count of 11

The number $s(11)$ of distinct remainders $11 \bmod k$ for
$1 \le k \le 5$ equals $4$.

These remainders form the set $S(11) = \{0, 1, 2, 3\}$ (Table 1 of the paper).

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Table 1.

Formalized by `MetaMathlibExt.remainderCount_eleven`, a theorem declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-count-eleven).

## The remainder count of 12

The number $s(12)$ of distinct remainders $12 \bmod k$ for
$1 \le k \le 6$ equals $2$.

This is a drop from $s(11) = 4$, the number of distinct remainders $11 \bmod k$ for
$1 \le k \le 5$ (Table 1 of the paper).

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Table 1.

Formalized by `MetaMathlibExt.remainderCount_twelve`, a theorem declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-count-twelve).

## The remainder-set constant

The remainder-set constant is
$c = \sum_{p} \frac{1}{p(p+1)} \prod_{q < p} \left(1 - \frac{1}{q}\right)$, where $p$ runs
over all primes and, for each $p$, $q$ runs over the primes less than $p$.

Numerically, $c \approx 0.2296$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, equation `eq:asymp`.

Formalized by `MetaMathlibExt.remainderConstant`, a definition declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-constant).

## Asymptotic formula for the number of remainders

Let $s(n)$ be the number of distinct
remainders $n \bmod k$ with $1 \le k \le \lfloor n/2 \rfloor$ and let $c$ be the remainder-set
constant. Then, as $n \to \infty$ over the natural numbers,
$s(n) - cn = O\bigl(n / (\log n \cdot \log \log n)\bigr)$, and $s(n)/n \to c$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Theorem 1 (`thm:asymp`).

Stated but not proved: `MetaMathlibExt.remainderCount_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-count-asymptotic).

## Unbounded drops in the number of remainders

Let $s(n)$ be the number of distinct
remainders $n \bmod k$ with $1 \le k \le \lfloor n/2 \rfloor$. For every natural number $M$
there are infinitely many $n$ with $s(n+1) + M \le s(n)$; equivalently,
$\liminf_{n \to \infty} (s(n+1) - s(n)) = -\infty$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Proposition 17 (`prop:diffs_unbounded`).

Stated but not proved: `MetaMathlibExt.remainderCount_drops_unbounded` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-count-drops-unbounded).

## Consecutive differences of the number of remainders

Let $s(n)$ be the number of
distinct remainders $n \bmod k$ with $1 \le k \le \lfloor n/2 \rfloor$. Then
$s(n+1) \le s(n) + 1$ for every $n \ge 1$; there is a real constant $C$ with
$s(n) - C \log \log n \le s(n+1)$ for all sufficiently large $n$; and for every natural number
$M$ there are infinitely many $n$ with $s(n+1) + M \le s(n)$, that is,
$\liminf_{n \to \infty} (s(n+1) - s(n)) = -\infty$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Theorem 2 (`thm:diffs`).

Stated but not proved: `MetaMathlibExt.remainderCount_consecutive_differences` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#remainder-count-consecutive-differences).

## Counting integers with a given least prime factor in an interval

Let $a$ and $t$ be
positive integers and let $p$ be a prime. Let $N$ be the number of integers $m$ with
$a + 1 \le m \le a + t$ that are divisible by $p$ and by no prime $q < p$. Then

$$\left| N - \frac{t}{p} \prod_{q < p,\ q \text{ prime}} \left(1 - \frac{1}{q}\right) \right|
\le 2^{\pi(p-1)}$$

where $\pi$ is the prime-counting function.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Lemma 6 (`lem:Dp`).

Stated but not proved: `MetaMathlibExt.card_leastPrimeFactor_interval_error` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#card-least-prime-factor-interval-error).

## Upper bound $1.3\, n / \log n$ for the prime-counting function

For every natural
number $n \ge 2$, the number $\pi(n)$ of primes at most $n$ satisfies
$\pi(n) \le 1.3\, n / \log n$, where $\log$ is the natural logarithm.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Lemma 7 (`lem:primecounting_ub`).

Stated but not proved: `MetaMathlibExt.primeCounting_le_thirteen_tenths` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#prime-counting-le-thirteen-tenths).

## Tail of the sum of inverse prime squares

As the natural number $n$ tends to infinity,
the sum $\sum_{p > n,\ p \text{ prime}} 1/p^2$ of the inverse squares of the primes greater
than $n$ is $O(1/(n \log n))$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Lemma 8 (`lem:psquared_sum_est`).

Stated but not proved: `MetaMathlibExt.tsum_inv_sq_primes_gt_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#tsum-inv-sq-primes-gt-is-big-o).

## Iterated remainder sets

For a natural number $n$, the iterated remainder sets
$S_j(n)$, $j \ge 0$, are defined by $S_0(n) = \{1, \dots, \lfloor n/2 \rfloor\}$ and, for
$j \ge 0$, $S_{j+1}(n) = \{n \bmod k : k \in S_j(n),\ k \ne 0\}$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Section 2 (definition of `S_j(n)`).

Formalized by `MetaMathlibExt.iteratedRemainderSet`, a definition declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#iterated-remainder-set).

## The first iterated remainder set is the remainder set

For every natural number $n$, the
iterated remainder set $S_1(n)$ equals the remainder set
$S(n) = \{n \bmod k : 1 \le k \le \lfloor n/2 \rfloor\}$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Section 2 (`S(n) = S_1(n)`).

Formalized by `MetaMathlibExt.iteratedRemainderSet_one`, a theorem declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#iterated-remainder-set-one).

## Iterated remainder sets of 35

The iterated remainder sets of $35$ satisfy
$S_6(35) = \{0\}$ and $S_7(35) = \emptyset$.

## Sources

- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Section 2 (definition of `S_j(n)`).

Formalized by `MetaMathlibExt.iteratedRemainderSet_thirtyFive`, a theorem declared in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#iterated-remainder-set-thirty-five).

## Maximal Pierce length via iterated remainder sets

Let $n \ge 3$ and $t$ be natural
numbers, let $P(n)$ be the maximal Pierce length of $n$ and let $S_j(n)$ be the iterated
remainder sets of $n$. Then the following are equivalent: $P(n) = t + 1$; $S_t(n) = \{0\}$;
$S_t(n)$ has exactly one element and $S_{t+j}(n) = \emptyset$ for every $j \ge 1$.

This corrects the index of the printed lemma, $P(n) = t \iff S_{t+1}(n) = \{0\}$, which fails
for every $n \ge 3$: for example $P(5) = 3$, $S_2(5) = \{0\}$ and $S_4(5) = \emptyset$. The
paper derives the lemma from its Lemma 18 ($r \in S_j(n)$ if and only if $a_{j+1} = r$ for some
$\lfloor n/2 \rfloor + 1 \le a \le n$, where $a_0 = a$ and $a_{i+1} = n \bmod a_i$), which
gives the index $P(n) - 1$. Lemma 18, and hence this lemma, needs $n \ge 3$: $P(2) = 1$ but
$S_0(2) = \{1\}$.

## Sources

- the forward direction of the first equivalence (for `t ≥ 1`) is proved as `S_eq_singleton_zero_of_maxLength_eq` in `FormalizedPapers/NumberTheory/BaraskarGokhaleJainKiezun2026`.
- Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, Journal of Integer Sequences 29 (2026), Article 26.1.4, Lemma 19.

Stated but not proved: `MetaMathlibExt.pierce_maxLength_eq_succ_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/RemainderSetBoundsWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RemainderSetBoundsWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html#pierce-max-length-eq-succ-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sets of remainders](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/sets-of-remainders)
