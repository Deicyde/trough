---
declaration: section
origin: cited
lean: MetaMathlibExt.pseudoGreedyRemainder, MetaMathlibExt.pseudoGreedyExpansion, MetaMathlibExt.pseudoGreedyGap, MetaMathlibExt.pseudoGreedyRemainder_succ, MetaMathlibExt.pseudoGreedyExpansion_one_zero, MetaMathlibExt.pseudoGreedyExpansion_one_one, MetaMathlibExt.pseudoGreedyGap_one_zero, MetaMathlibExt.eq_round_inv_remainder_add
statement: formalized
---

# Reciprocal sums of doubly exponential sequences

19 results, 7 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html).

## Pseudo-greedy remainder sequence

For a real number $r$, the remainder sequence
$(x_n)_{n \ge 0}$ of the pseudo-greedy expansion of $r$ is defined by $x_0 = r$ and
$x_{n+1} = x_n - 1/a_n$, where $a_n = \lfloor x_n^{-1} + 1 + 1/2 \rfloor$ is the integer
nearest to $x_n^{-1} + 1$, with halves rounded up.

Here $0^{-1}$ and $1/0$ are read as $0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Section 2 (definitions of the pseudo-greedy expansion and its remainder sequence).

Formalized by `MetaMathlibExt.pseudoGreedyRemainder`, a definition declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-remainder).

## Pseudo-greedy expansion

Let $r$ be a real number with pseudo-greedy remainder sequence
$(x_n)_{n \ge 0}$. The pseudo-greedy expansion of $r$ is the integer sequence
$a_n = \lfloor x_n^{-1} + 1 + 1/2 \rfloor$ for $n \ge 0$; that is, $a_n$ is the integer nearest
to $x_n^{-1} + 1$, with halves rounded up.

Here $0^{-1}$ is read as $0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Section 2 (definition of the pseudo-greedy expansion).

Formalized by `MetaMathlibExt.pseudoGreedyExpansion`, a definition declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-expansion).

## Gap sequence of the pseudo-greedy expansion

Let $r$ be a real number, and let $(x_n)$
be the remainder sequence and $(a_n)$ the pseudo-greedy expansion of $r$. The gap sequence of
$r$ is the real sequence $\varepsilon_n = x_n^{-1} + 1 - a_n$ for $n \ge 0$.

Here $0^{-1}$ is read as $0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Section 2 (definition of the gap sequence).

Formalized by `MetaMathlibExt.pseudoGreedyGap`, a definition declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-gap).

## Remainder recursion

For every real number $r$ and every $n \ge 0$, the remainder
sequence $(x_n)$ and the pseudo-greedy expansion $(a_n)$ of $r$ satisfy $x_{n+1} = x_n - 1/a_n$.

Here $1/0$ is read as $0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Section 2 (definition of the remainder sequence).

Formalized by `MetaMathlibExt.pseudoGreedyRemainder_succ`, a theorem declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-remainder-succ).

## The pseudo-greedy expansion of 1 starts with 2

The first term $a_0$ of the
pseudo-greedy expansion of $1$ equals $2$, the first Sylvester number.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Example 1 (the expansion of `1` is the Sylvester sequence).

Formalized by `MetaMathlibExt.pseudoGreedyExpansion_one_zero`, a theorem declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-expansion-one-zero).

## Second term of the pseudo-greedy expansion of $1$

The pseudo-greedy expansion
$(a_n)_{n \ge 0}$ of $1$ satisfies $a_1 = 3$.

The remainder after the first term $a_0 = 2$ is $1 - 1/2 = 1/2$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Example 1 (the expansion of `1` is the Sylvester sequence).

Formalized by `MetaMathlibExt.pseudoGreedyExpansion_one_one`, a theorem declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-expansion-one-one).

## The first gap of the expansion of 1 vanishes

The first term $\varepsilon_0$ of the gap
sequence of the pseudo-greedy expansion of $1$ is $0$: the first remainder is $x_0 = 1$ and the
first term of the expansion is $a_0 = 2$, so $\varepsilon_0 = x_0^{-1} + 1 - a_0 = 1 + 1 - 2 = 0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Example 1 (`ε_n = 0` for the expansion of `1`).

Formalized by `MetaMathlibExt.pseudoGreedyGap_one_zero`, a theorem declared in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-gap-one-zero).

## Recovering a doubly exponential sequence from its reciprocal sum

Let $\beta \ge 0$ and
$r$ be real numbers, and let $(a_n)_{n \ge 0}$ be a sequence of positive integers with
$|a_n^2 / a_{n+1} - \beta| \le 1/3$ for all $n$ and $\sum_n 1 / a_n = r$. Write
$x_n = r - \sum_{k\lt n} 1 / a_k$. Then for every $n$ with $a_n \ge 8 (\beta + 1/3)^2$ we have
$a_n = \lfloor x_n^{-1} + \beta + 1/2 \rfloor$, that is, $a_n$ is the integer nearest to
$x_n^{-1} + \beta$, with halves rounded up. Moreover, if $a_n^2 / a_{n+1} \to \beta$, then
$|x_n^{-1} + \beta - a_n| \to 0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Theorem 1.

Stated but not proved: `MetaMathlibExt.eq_round_inv_remainder_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#eq-round-inv-remainder-add).

## Characterization of the Sylvester sequence

Let $(a_n)_{n \ge 0}$ be a sequence of
positive integers with $2/3 \le a_n^2 / a_{n+1} \le 4/3$ for all $n$ and $\sum_n 1 / a_n = 1$.
Then $a_n = s_n(1)$ for all $n \ge 0$, where $(s_n(1))_{n \ge 0}$ is the generalized Sylvester
sequence with parameter $1$, that is, the Sylvester sequence $2, 3, 7, 43, \ldots$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Corollary 1.

Stated but not proved: `MetaMathlibExt.eq_sylvester_of_ratio_mem_of_hasSum_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#eq-sylvester-of-ratio-mem-of-has-sum-one).

## Characterization of the denominators of the Millin series

Let $(a_n)_{n \ge 0}$ be a
sequence of positive integers with $a_n^2 / a_{n+1} \le 2/3$ for all $n$ and
$\sum_n 1 / a_n = (5 - \sqrt 5) / 2$. Then $a_n = F_{2^{n+1}}$ for all $n \ge 0$, where $F_k$
is the $k$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$); that is, $a$ is the sequence
$F_2, F_4, F_8, \ldots$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Corollary 2.

Stated but not proved: `MetaMathlibExt.eq_fib_two_pow_of_ratio_le_of_hasSum_millin` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#eq-fib-two-pow-of-ratio-le-of-has-sum-mi).

## Doubly exponential floors are Type 2 irrationality sequences for all but countably many bases

**Doubly exponential floors are Type 2 irrationality sequences for all but countably many
bases.** For all real numbers $\alpha > 1$ outside a countable set, the sequence
$(\lfloor \alpha^{2^{n+1}} \rfloor)_{n \ge 0}$ is a Type 2 irrationality sequence: for every
sequence $(b_n)_{n \ge 0}$ of positive integers with $b_n / \lfloor \alpha^{2^{n+1}} \rfloor \to 1$,
the series $\sum_n 1 / b_n$ does not converge to a rational number.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Theorem 2 and the definition of Type 2 irrationality sequences preceding it.

Stated but not proved: `MetaMathlibExt.countable_not_type2IrrationalitySequence_floor_pow_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#countable-not-type2-irrationality-sequen).

## Convergence of the pseudo-greedy expansion

For every real number $r > 0$, the
pseudo-greedy expansion $(a_n)_{n \ge 0}$ of $r$ satisfies $\sum_n 1 / a_n = r$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Lemma 1.

Stated but not proved: `MetaMathlibExt.hasSum_one_div_pseudoGreedyExpansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#has-sum-one-div-pseudo-greedy-expansion).

## Recursion for the pseudo-greedy expansion

Let $r > 0$ be a real number, and let
$(a_n)$ be its pseudo-greedy expansion and $(\varepsilon_n)$ its gap sequence. Then for every
$n \ge 0$,

$$a_{n+1} = \frac{a_n^2}{1 - \varepsilon_n} - a_n + (1 - \varepsilon_{n+1}).$$

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Lemma 2.

Stated but not proved: `MetaMathlibExt.pseudoGreedyExpansion_succ_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-expansion-succ-eq).

## A vanishing gap stays zero

Let $r > 0$ be a real number and let $(\varepsilon_n)$ be
the gap sequence of its pseudo-greedy expansion. For every $n \ge 0$, if $\varepsilon_n = 0$,
then $\varepsilon_{n+1} = 0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Lemma 3.

Stated but not proved: `MetaMathlibExt.pseudoGreedyGap_succ_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-gap-succ-eq-zero).

## Structure of the pseudo-greedy expansion of a rational

Let $p$ and $q$ be positive
integers, let $r = p/q$, and let $(x_n)$, $(a_n)$ and $(\varepsilon_n)$ be the remainder
sequence, the pseudo-greedy expansion and the gap sequence of $r$. Put
$d_n = q a_0 a_1 \cdots a_{n-1}$ (so $d_0 = q$). Then there are positive integers $c_n$ and
integers $e_n$ ($n \ge 0$) such that for every $n$ we have $x_n = c_n / d_n$,
$\varepsilon_n = e_n / c_n$, $e_n \equiv d_n \pmod{c_n}$, $-c_n/2 \le e_n < c_n/2$,
$a_n = (d_n - e_n)/c_n + 1$, $c_{n+1} = c_n - e_n$ and $d_{n+1} = d_n a_n$. Moreover, as
$n \to \infty$, $c_n = O(a_0 \cdots a_{n-1} / a_n)$ and $c_n = O(1.5^n)$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Lemma 4.

Stated but not proved: `MetaMathlibExt.pseudoGreedyExpansion_rational_structure` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-expansion-rational-structu).

## Eventual vanishing of the pseudo-greedy gaps of a rational number

Let $r$ be a positive
rational number and let $(\varepsilon_n)_{n \ge 0}$ be the gap sequence of the pseudo-greedy
expansion of $r$. Suppose that $\liminf_n \varepsilon_n \prod_{k\lt n} (1 - \varepsilon_k) \ge 0$,
that is, for every $\delta > 0$ we have $\varepsilon_n \prod_{k\lt n} (1 - \varepsilon_k) \ge -\delta$
for all sufficiently large $n$; or that $\varepsilon_n \ge 0$ for all sufficiently large $n$.
Then $\varepsilon_n = 0$ for all sufficiently large $n$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Proposition 1.

Stated but not proved: `MetaMathlibExt.eventually_pseudoGreedyGap_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#eventually-pseudo-greedy-gap-eq-zero).

## Tails that are pseudo-greedy expansions

Let $(a_n)_{n \ge 0}$ be a sequence of positive
integers with $a_n^2 / a_{n+1} \to 1$ such that $\sum_n 1 / a_n$ converges. Then there is a
natural number $N$ such that, with $r = \sum_{k \ge 0} 1 / a_{N+k}$, the tail
$(a_{N+n})_{n \ge 0}$ is the pseudo-greedy expansion of $r$, and the gap sequence of this
expansion tends to $0$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Corollary 3.

Stated but not proved: `MetaMathlibExt.exists_tail_eq_pseudoGreedyExpansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#exists-tail-eq-pseudo-greedy-expansion).

## Erdős–Straus and Badea criterion for the Sylvester recurrence

Let $(a_n)_{n \ge 0}$ be a
sequence of positive integers with $a_n^2 / a_{n+1} \to 1$ such that $\sum_n 1 / a_n$ converges
to a rational number. Suppose that
$\liminf_n (a_0 \cdots a_{n-1} / a_n)(1 - a_n^2 / a_{n+1}) \ge 0$, that is, for every
$\delta > 0$ this quantity is at least $-\delta$ for all sufficiently large $n$; or that
$a_{n+1} \ge a_n^2 - a_n + 1$ for all sufficiently large $n$. Then
$a_{n+1} = a_n^2 - a_n + 1$ for all sufficiently large $n$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Corollary 4.

Stated but not proved: `MetaMathlibExt.eventually_sylvester_recurrence_of_rational_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#eventually-sylvester-recurrence-of-ratio).

## Koizumi's conjecture is equivalent to the Erdős–Graham question

The following are
equivalent. (1) For every positive rational number $r$ whose pseudo-greedy gap sequence
$(\varepsilon_n)_{n \ge 0}$ tends to $0$, we have $\varepsilon_n = 0$ for all sufficiently large
$n$. (2) Every sequence $(a_n)_{n \ge 0}$ of positive integers with $a_n^2 / a_{n+1} \to 1$ such
that $\sum_n 1 / a_n$ converges to a rational number satisfies $a_{n+1} = a_n^2 - a_n + 1$ for
all sufficiently large $n$.

## Sources

- Junnosuke Koizumi, *Irrationality of the Reciprocal Sum of Doubly Exponential Sequences*, INTEGERS 26 (2026), Article A28, Theorem 3, with Conjecture 1 and Question 1.

Stated but not proved: `MetaMathlibExt.pseudoGreedy_conjecture_iff_erdos_graham_question` is written with `theorem_wanted` in [WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DoublyExponentialReciprocalSumWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html#pseudo-greedy-conjecture-iff-erdos-graha).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reciprocal sums of doubly exponential sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/reciprocal-sums-of-doubly-exponential-sequences)
