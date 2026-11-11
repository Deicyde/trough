---
declaration: section
origin: cited
lean: MetaMathlibExt.fulton_morris_pisano_fixed_point, MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.pisanoPeriod, MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.pisanoPeriod_fib_dvd_two_mul, MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.tendsto_iInf_pisanoPeriod_div_atTop, MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.sum_fib_mod_prime_eq_and_not_dvd, MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.fib_two_mul_prime_odd_and_fib_fib_add_two_mod, MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.infinite_setOf_odd_dvd_sum_fib
statement: formalized
---

# Pisano periods

7 results, 2 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html).

## Fulton–Morris theorem on Pisano periods equal to the modulus

Write $F_t$ for the $t$-th
Fibonacci number. Let $m > 1$ be a natural number and let $\pi$ be a positive integer with
$F_\pi \equiv 0 \pmod{m}$ and $F_{\pi+1} \equiv 1 \pmod{m}$ such that $\pi \le t$ for every
positive integer $t$ with $F_t \equiv 0 \pmod{m}$ and $F_{t+1} \equiv 1 \pmod{m}$; that is, $\pi$
is the Pisano period of $m$. Then $\pi = m$ if and only if $m = 24 \cdot 5^{\lambda - 1}$ for some
integer $\lambda \ge 1$.

## Sources

- Amirali Fatehizadeh and Daniel Yaqubi, "Average of the Fibonacci Numbers," Journal of Integer Sequences 25 (2022), Article 22.2.6, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Yaqubi/yaq6.tex>, lines 177–189. The theorem is attributed there to John Fulton and William Morris, "On arithmetical functions related to the Fibonacci numbers," Acta Arithmetica 16 (1969), 105–110, DOI 10.4064/aa-16-2-105-110.

Formalized by `MetaMathlibExt.fulton_morris_pisano_fixed_point`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/FultonMorrisPisanoFixedPoint.lean, line 1282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/FultonMorrisPisanoFixedPoint.lean#L1282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#fulton-morris-pisano-fixed-point).

## Pisano period

For a natural number $n$, the Pisano period $\pi(n)$ is the minimal period
of the pair $(0, 1)$ under the Fibonacci step $(a, b) \mapsto (b, a + b)$ on
$\mathbb{Z}/n\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$: the least $k \ge 1$ such that $k$
applications of the step map $(0, 1)$ back to $(0, 1)$, or $0$ if there is no such $k$ (as for
$n = 0$, where $\mathbb{Z}/0\mathbb{Z} = \mathbb{Z}$).

Formalized by `MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.pisanoPeriod`, a definition declared in [WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#pisano-period).

## The Pisano period of $F_n$ divides $2n$ for even $n$

Let $F_n$ denote the $n$-th Fibonacci
number and $\pi(m)$ the Pisano period of $m$. For every even natural number $n > 1$, $\pi(F_n)$
divides $2n$.

## Sources

- Oisín Flynn-Connolly, "On the Divisibility of Sums of Fibonacci Numbers", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.pisanoPeriod_fib_dvd_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#pisano-period-fib-dvd-two-mul).

## The minimum of $\pi(n)/n$ over $1 \le n < N$ tends to zero

Let $\pi(n)$ denote the Pisano
period of $n$. As $N \to \infty$, the minimum of the real numbers $\pi(n)/n$ over the integers
$1 \le n \le N - 1$ (defined for $N \ge 2$) tends to $0$.

## Sources

- Oisín Flynn-Connolly, "On the Divisibility of Sums of Fibonacci Numbers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.tendsto_iInf_pisanoPeriod_div_atTop` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#tendsto-i-inf-pisano-period-div-at-top).

## Sum of the first $p$ Fibonacci numbers modulo a prime $p$

Let $p > 5$ be a prime, let
$F_i$ denote the $i$-th Fibonacci number, with $F_1 = F_2 = 1$, and let
$S = F_1 + F_2 + \dots + F_p$. If $p \equiv 1$ or $4 \pmod 5$, then $S$ leaves remainder $1$ on
division by $p$; if $p \equiv 2$ or $3 \pmod 5$, then $S$ leaves remainder $p - 2$ on division
by $p$; and in every case $p$ does not divide $S$.

## Sources

- Oisín Flynn-Connolly, "On the Divisibility of Sums of Fibonacci Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.sum_fib_mod_prime_eq_and_not_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#sum-fib-mod-prime-eq-and-not-dvd).

## Odd Fibonacci numbers $F_n$ with $F_{F_n + 2} \equiv 1 \pmod{F_n}$

Let $F_m$ denote the
$m$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$. If $p$ is an odd prime with
$p \equiv 2 \pmod 3$ and $p \equiv 2$ or $3 \pmod 5$, and $n = 2p$ or $n = 4p$, then $F_n$ is odd
and $F_{F_n + 2}$ leaves remainder $1$ on division by $F_n$.

## Sources

- Oisín Flynn-Connolly, "On the Divisibility of Sums of Fibonacci Numbers", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.fib_two_mul_prime_odd_and_fib_fib_add_two_mod` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#fib-two-mul-prime-odd-and-fib-fib-add-tw).

## Infinitely many odd $k$ divide the sum of the first $k$ Fibonacci numbers

Let $F_i$ denote
the $i$-th Fibonacci number, with $F_1 = F_2 = 1$. There are infinitely many odd positive integers
$k$ such that $k$ divides $F_1 + F_2 + \dots + F_k$.

## Sources

- Oisín Flynn-Connolly, "On the Divisibility of Sums of Fibonacci Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.FibonacciSumDivisibilityWanted.infinite_setOf_odd_dvd_sum_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/FibonacciSumDivisibilityWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html#infinite-set-of-odd-dvd-sum-fib).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pisano periods](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/pisano-periods)
