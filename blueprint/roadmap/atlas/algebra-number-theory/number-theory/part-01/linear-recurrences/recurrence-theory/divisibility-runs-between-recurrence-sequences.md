---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDivRunUpTo, MetaMathlibExt.isDivRunUpTo_zero, MetaMathlibExt.int_gcd_gibonacciNumber_sub_two, MetaMathlibExt.gibonacciNumber_backward, MetaMathlibExt.gibonacciNumber_eq_fib, MetaMathlibExt.exists_generalizedTribonacci_basis, MetaMathlibExt.isDivRunUpTo_small, MetaMathlibExt.generalizedTribonacci_eq_zero_of_dvd
statement: formalized
---

# Divisibility runs between recurrence sequences

18 results, 4 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html).

## Divisibility runs

For integers $x, y, a, b, c$ and a natural number $L$, let
$(P_n)_{n \ge 0}$ be the Gibonacci sequence with $P_0 = x$ and $P_1 = y$, and let $(Q_n)_{n \ge 0}$
be the generalized Tribonacci sequence with $Q_0 = a$, $Q_1 = b$ and $Q_2 = c$. The configuration
$(x, y; a, b, c)$ has a divisibility run of length at least $L$ when $P_i \ne 0$ and
$P_i \mid Q_i$ for every $i < L$.

This is the statement that the run length $L(x, y; a, b, c)$ of the paper's Equation (1) is at
least $L$; the paper indexes the sequences from $1$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Equation (1) and Proposition 3.

Formalized by `MetaMathlibExt.IsDivRunUpTo`, a definition declared in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#is-div-run-up-to).

## Divisibility runs of length zero

For integers $x, y, a, b, c$, let $(P_n)_{n \ge 0}$ be
the Gibonacci sequence with $P_0 = x$ and $P_1 = y$, let $(Q_n)_{n \ge 0}$ be the generalized
Tribonacci sequence with $Q_0 = a$, $Q_1 = b$ and $Q_2 = c$, and say $(x, y; a, b, c)$ has a
divisibility run of length at least $L$ when $P_i \ne 0$ and $P_i \mid Q_i$ for every natural
number $i < L$. Then $(x, y; a, b, c)$ always has a divisibility run of length at least $0$, since
no natural number $i$ satisfies $i < 0$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Equation (1).

Formalized by `MetaMathlibExt.isDivRunUpTo_zero`, a theorem declared in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#is-div-run-up-to-zero).

## Gibonacci terms two apart have the gcd of the initial values

Let $x, y$ be integers and
let $(P_n)_{n \ge 0}$ be the Gibonacci sequence with $P_0 = x$ and $P_1 = y$. For every $n \ge 2$,
the nonnegative greatest common divisor of $P_n$ and $P_{n-2}$ equals that of $x$ and $y$:
$\gcd(P_n, P_{n-2}) = \gcd(x, y)$.

The paper indexes the sequence from $1$ and states this for $n \ge 3$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Lemma 2.

Stated but not proved: `MetaMathlibExt.int_gcd_gibonacciNumber_sub_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#int-gcd-gibonacci-number-sub-two).

## Backward recurrence for Gibonacci numbers

Let $x, y$ be integers and let
$(P_n)_{n \ge 0}$ be the Gibonacci sequence with $P_0 = x$ and $P_1 = y$. For every $n \ge 3$,
$P_{n-1} = P_n - P_{n-2}$ and $P_{n-3} = P_n - 2 P_{n-2}$.

The paper indexes the sequence from $1$ and states these identities for $n \ge 4$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Lemma 3.

Stated but not proved: `MetaMathlibExt.gibonacciNumber_backward` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#gibonacci-number-backward).

## Gibonacci numbers in terms of Fibonacci numbers

Let $x, y$ be integers, let
$(P_n)_{n \ge 0}$ be the Gibonacci sequence with $P_0 = x$ and $P_1 = y$, and let $(F_n)_{n \ge 0}$
be the Fibonacci sequence with $F_0 = 0$ and $F_1 = 1$. For every $n \ge 1$,
$P_n = F_{n-1}\,x + F_n\,y$.

The paper indexes $P$ from $1$ and states this as $P_n = F_{n-2}\,x + F_{n-1}\,y$ for $n \ge 2$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 1.

Stated but not proved: `MetaMathlibExt.gibonacciNumber_eq_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#gibonacci-number-eq-fib).

## Basis sequences for generalized Tribonacci sequences

There are integer sequences
$(u_n)_{n \ge 0}$, $(v_n)_{n \ge 0}$ and $(w_n)_{n \ge 0}$, each satisfying the Tribonacci
recurrence $s_{n+3} = s_{n+2} + s_{n+1} + s_n$ for all $n \ge 0$, with initial values
$(u_0, u_1, u_2) = (1, 0, 0)$, $(v_0, v_1, v_2) = (0, 1, 0)$ and $(w_0, w_1, w_2) = (0, 0, 1)$,
such that for all integers $a, b, c$ and every $n \ge 0$ the $n$-th term of the generalized
Tribonacci sequence with initial values $a, b, c$ equals $u_n a + v_n b + w_n c$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 2.

Stated but not proved: `MetaMathlibExt.exists_generalizedTribonacci_basis` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#exists-generalized-tribonacci-basis).

## Divisibility runs of length one, two and three

For integers $x, y, a, b, c$, let $(P_n)$
be the Gibonacci sequence with $P_0 = x$, $P_1 = y$ and $(Q_n)$ the generalized Tribonacci sequence
with $Q_0 = a$, $Q_1 = b$, $Q_2 = c$, and say $(x, y; a, b, c)$ has a divisibility run of length at
least $L$ when $P_i \ne 0$ and $P_i \mid Q_i$ for every $i < L$. Then there is a run of length at
least $1$ if and only if $x \ne 0$ and $x \mid a$; a run of length at least $2$ if and only if
$x \ne 0$, $x \mid a$, $y \ne 0$ and $y \mid b$; and a run of length at least $3$ if and only if
$x \ne 0$, $x \mid a$, $y \ne 0$, $y \mid b$, $x + y \ne 0$ and $x + y \mid c$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 3.

Stated but not proved: `MetaMathlibExt.isDivRunUpTo_small` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#is-div-run-up-to-small).

## Divisibility by a Gibonacci sequence forces a Tribonacci sequence to vanish

Let
$x, y, a, b, c$ be integers, let $(P_n)_{n \ge 0}$ be the Gibonacci sequence with $P_0 = x$ and
$P_1 = y$, and let $(Q_n)_{n \ge 0}$ be the generalized Tribonacci sequence with $Q_0 = a$,
$Q_1 = b$ and $Q_2 = c$. If $P_n \ne 0$ and $P_n \mid Q_n$ for every $n \ge 0$, then $Q_n = 0$
for every $n \ge 0$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Theorem 1.

Stated but not proved: `MetaMathlibExt.generalizedTribonacci_eq_zero_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#generalized-tribonacci-eq-zero-of-dvd).

## Growth bounds for Gibonacci and generalized Tribonacci sequences

Let $\varphi$ be the
golden ratio. For integers $x, y$ let $(P_n)_{n \ge 0}$ be the Gibonacci sequence with $P_0 = x$
and $P_1 = y$, and for integers $a, b, c$ let $(Q_n)_{n \ge 0}$ be the generalized Tribonacci
sequence with $Q_0 = a$, $Q_1 = b$ and $Q_2 = c$. Then (i) for all integers $x, y$ and every
$n \ge 0$, $|P_n| \le (|x| + |y|)\,\varphi^n$; (ii) there are real constants $c_0 > 0$ and
$c_1 > 0$ such that for all integers $x, y$ with $(x, y) \ne (0, 0)$ and every $n \ge 0$ with
$c_1 (\log(|x| + |y|) + 1) \le n$, one has $c_0\,\varphi^{n+1} / (|x| + |y|) \le |P_n|$; and
(iii) for every real $\tau$ with $\tau^3 = \tau^2 + \tau + 1$, all integers $a, b, c$ and every
$n \ge 0$, $|Q_n| \le (|a| + |b| + |c|)\,\tau^n$.

The paper indexes both sequences from $1$, so its $n$-th terms are $P_{n-1}$ and $Q_{n-1}$ here.
It prints (ii) with the threshold "n large enough depending on $|x| + |y|$"; the logarithmic
threshold is the one the paper uses in its proof of Theorem 2.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Lemma 1, with the threshold as used in the proof of Theorem 2.

Stated but not proved: `MetaMathlibExt.gibonacci_generalizedTribonacci_growth_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#gibonacci-generalized-tribonacci-growth).

## Counting configurations with long divisibility runs

For natural numbers $B$ and $r$,
$A_B(r)$ is the number of integer tuples $(x, y, a, b, c)$ with all five entries in $[-B, B]$,
$(x, y) \ne (0, 0)$ and $(a, b, c) \ne (0, 0, 0)$ that have a divisibility run of length at
least $r$: for every $i < r$, the Gibonacci number $P_i$ with initial values $P_0 = x$, $P_1 = y$
is nonzero and divides the generalized Tribonacci number $Q_i$ with initial values $Q_0 = a$,
$Q_1 = b$, $Q_2 = c$ (indices start at $0$).

The tuples satisfying the size and nonvanishing conditions form the paper's set
$\mathcal{C}_B$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Equation (2).

Formalized by `MetaMathlibExt.divRunCount`, a definition declared in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count).

## Run count at bound 1 and length 1

Exactly $156$ integer tuples $(x, y, a, b, c)$ with
all entries in $\{-1, 0, 1\}$, $(x, y) \ne (0, 0)$ and $(a, b, c) \ne (0, 0, 0)$ have a
divisibility run of length at least $1$; that is, $A_1(1) = 156$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 4.

Formalized by `MetaMathlibExt.divRunCount_one_one`, a theorem declared in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-one-one).

## Divisibility runs have logarithmic length

There is a real constant $C > 0$ such that for
every natural number $B \ge 2$, all integers $x, y, a, b, c \in [-B, B]$ with $(x, y) \ne (0, 0)$
and $(a, b, c) \ne (0, 0, 0)$, and every natural number $L$ such that $(x, y, a, b, c)$ has a
divisibility run of length at least $L$, we have $L \le C \log B$. Here a divisibility run of
length at least $L$ means that for every $i < L$ the Gibonacci number $P_i$ with $P_0 = x$,
$P_1 = y$ is nonzero and divides the generalized Tribonacci number $Q_i$ with $Q_0 = a$,
$Q_1 = b$, $Q_2 = c$.

In the paper's notation this is $E(B) \le C \log B$, where $E(B)$ is the maximal run length
over these configurations.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Theorem 2.

Stated but not proved: `MetaMathlibExt.divRun_length_le_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-length-le-log).

## Exact formula for the length-one run count

For every natural number $B$, let
$D(B) = \sum_{m=1}^{B} \lfloor B/m \rfloor$ and let $A_B(1)$ be the number of integer tuples
$(x, y, a, b, c) \in [-B, B]^5$ with $(x, y) \ne (0, 0)$ and $(a, b, c) \ne (0, 0, 0)$ that have
a divisibility run of length at least $1$. Then

$$A_B(1) = 4(2B+1)^3 D(B) + 2B(2B+1)\left((2B+1)^2 - 1\right).$$

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 4.

Stated but not proved: `MetaMathlibExt.divRunCount_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-one).

## Asymptotics of the length-one run count

There is a real constant $K$ such that for every
natural number $B \ge 2$ the number $A_B(1)$ of integer tuples $(x, y, a, b, c) \in [-B, B]^5$
with $(x, y) \ne (0, 0)$ and $(a, b, c) \ne (0, 0, 0)$ that have a divisibility run of length at
least $1$ satisfies $|A_B(1) - 32 B^4 \log B| \le K B^4$; that is,
$A_B(1) = 32 B^4 \log B + O(B^4)$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 4.

Stated but not proved: `MetaMathlibExt.divRunCount_one_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-one-asymptotic).

## Exact formula for the length-two run count

For every natural number $B$, let
$S(B) = \sum_{m=1}^{B} \left(2\lfloor B/m \rfloor + 1\right)$ and let $A_B(2)$ be the number of
integer tuples $(x, y, a, b, c) \in [-B, B]^5$ with $(x, y) \ne (0, 0)$ and
$(a, b, c) \ne (0, 0, 0)$ that have a divisibility run of length at least $2$. Then
$S(B) = 2 \sum_{m=1}^{B} \lfloor B/m \rfloor + B$ and $A_B(2) = 4(2B+1) S(B)^2 - 4B^2$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 5.

Stated but not proved: `MetaMathlibExt.divRunCount_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-two).

## Asymptotics of the length-two run count

There is a real constant $K$ such that for every
natural number $B \ge 2$ the number $A_B(2)$ of integer tuples $(x, y, a, b, c) \in [-B, B]^5$
with $(x, y) \ne (0, 0)$ and $(a, b, c) \ne (0, 0, 0)$ that have a divisibility run of length at
least $2$ satisfies $|A_B(2) - 32 B^3 (\log B)^2| \le K B^3 \log B$; that is,
$A_B(2) = 32 B^3 (\log B)^2 + O(B^3 \log B)$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 5.

Stated but not proved: `MetaMathlibExt.divRunCount_two_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-two-asymptotic).

## Exact formula for the length-three run count

For a natural number $B$, let $A_B(3)$ be
the number of integer tuples $(x, y, a, b, c) \in [-B, B]^5$ with $(x, y) \ne (0, 0)$ and
$(a, b, c) \ne (0, 0, 0)$ that have a divisibility run of length at least $3$, and for integers
$m \ge 1$ let $d_B(m) = 2\lfloor B/m \rfloor + 1$. Then

$$A_B(3) = \sum_{x, y} \left(d_B(|x|)\, d_B(|y|)\, d_B(|x+y|) - 1\right),$$

where the sum runs over the integers $x, y \in [-B, B]$ with $x \ne 0$, $y \ne 0$ and
$x + y \ne 0$, and also

$$
A_B(3) = 2 \sum_{m=1}^{B} \sum_{n=1}^{B} d_B(m)\, d_B(n)\, d_B(m+n) +
4 \sum_{1 \le n < m \le B} d_B(m)\, d_B(n)\, d_B(m-n) - (4B^2 - 2B).
$$

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 6.

Stated but not proved: `MetaMathlibExt.divRunCount_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-three).

## Divisor-sum formula for the length-four run count

For a natural number $B$, let $A_B(4)$
be the number of integer tuples $(x, y, a, b, c) \in [-B, B]^5$ with $(x, y) \ne (0, 0)$ and
$(a, b, c) \ne (0, 0, 0)$ that have a divisibility run of length at least $4$. For integers $x, y$
let $T_B(x, y)$ be the number of integer triples $(a, b, c) \in [-B, B]^3$ with $x \mid a$,
$y \mid b$, $x + y \mid c$ and $x + 2y \mid a + b + c$, and let $T'_B(x, y)$ be the number of
integer triples $(\alpha, \beta, \gamma)$ with $|\alpha| \le \lfloor B/|x| \rfloor$,
$|\beta| \le \lfloor B/|y| \rfloor$, $|\gamma| \le \lfloor B/|x+y| \rfloor$ and
$x + 2y \mid x\alpha + y\beta + (x+y)\gamma$. Then

$$A_B(4) = \sum_{x, y} \left(T_B(x, y) - 1\right) = \sum_{x, y} \left(T'_B(x, y) - 1\right),$$

where both sums run over the integers $x, y \in [-B, B]$ with $x \ne 0$, $y \ne 0$, $x + y \ne 0$
and $x + 2y \ne 0$.

The second form comes from writing $a = x\alpha$, $b = y\beta$, $c = (x+y)\gamma$; it is the
paper's $\sum \chi_{x,y}(\alpha, \beta, \gamma)$.

## Sources

- Smirnov, *Finite Divisibility Runs Between Generalized Fibonacci and Tribonacci Sequences*, INTEGERS 26 (2026), Article A122, Proposition 7.

Stated but not proved: `MetaMathlibExt.divRunCount_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/DivisibilityRunsWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DivisibilityRunsWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html#div-run-count-four).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisibility runs between recurrence sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrence-theory/divisibility-runs-between-recurrence-sequences)
