---
declaration: section
origin: cited
lean: MetaMathlibExt.lucasU_three_neg_four_composite, MetaMathlibExt.lucasU_q_one_shifts_eventually_composite, MetaMathlibExt.exists_shift_lucasU_q_neg_one_composite, MetaMathlibExt.lucasU_square_q_finite_primes, MetaMathlibExt.lucasU_power_params_finite_primes, MetaMathlibExt.fib_add_14475_not_prime
statement: formalized
---

# Composite terms of shifted Lucas sequences

6 results, 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html).

## Composite terms of the Lucas sequence $U_n(3, -4)$

Let $U_n = U_n(3, -4)$ be the
Lucas sequence with $U_0 = 0$, $U_1 = 1$ and $U_{n+2} = 3U_{n+1} + 4U_n$, so that
$U_n = 0, 1, 3, 13, 51, 205, 819, \ldots$. For every natural number $n \ge 4$, $U_n$ is
composite: $U_n > 1$ and $U_n$ is not prime.

## Sources

- Dan Ismailescu, Daniel Hyunwoo Jeon, Aaron Kim, Joonbeom Kwon and Austin Lee, *Shifting Lucas Sequences Away from Primes*, INTEGERS 25 (2025), Article A42, Theorem 1.

Stated but not proved: `MetaMathlibExt.lucasU_three_neg_four_composite` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html#lucas-u-three-neg-four-composite).

## Unit shifts of $U_n(P, 1)$ are eventually composite

Let $P \ge 3$ be an integer and
let $U_n = U_n(P, 1)$ be the Lucas sequence with $U_0 = 0$, $U_1 = 1$ and
$U_{n+2} = PU_{n+1} - U_n$. Then there is a natural number $N$ such that for every $n \ge N$
the three integers $U_n - 1$, $U_n$ and $U_n + 1$ are all composite, that is, each is
greater than $1$ and not prime.

## Sources

- Dan Ismailescu, Daniel Hyunwoo Jeon, Aaron Kim, Joonbeom Kwon and Austin Lee, *Shifting Lucas Sequences Away from Primes*, INTEGERS 25 (2025), Article A42, Theorem 2.

Stated but not proved: `MetaMathlibExt.lucasU_q_one_shifts_eventually_composite` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html#lucas-u-q-one-shifts-eventually-composit).

## A shift of $U_n(P, -1)$ away from primes

Let $P \ge 1$ be an integer and let
$U_n = U_n(P, -1)$ be the Lucas sequence with $U_0 = 0$, $U_1 = 1$ and
$U_{n+2} = PU_{n+1} + U_n$. Then there is an integer $K > 0$ such that for every natural
number $n$ the three integers $U_n + K - 1$, $U_n + K$ and $U_n + K + 1$ are all composite,
that is, each is greater than $1$ and not prime.

## Sources

- Dan Ismailescu, Daniel Hyunwoo Jeon, Aaron Kim, Joonbeom Kwon and Austin Lee, *Shifting Lucas Sequences Away from Primes*, INTEGERS 25 (2025), Article A42, Theorem 3.

Stated but not proved: `MetaMathlibExt.exists_shift_lucasU_q_neg_one_composite` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html#exists-shift-lucas-u-q-neg-one-composite).

## Lucas sequences with square $Q$ have finitely many prime terms

Let $P$ and $Q$ be
integers with $P \ge 1$ and $P^2 - 4Q > 0$, where $Q \ne 0$ is a perfect square, and let
$U_n = U_n(P, Q)$ be the Lucas sequence with $U_0 = 0$, $U_1 = 1$ and
$U_{n+2} = PU_{n+1} - QU_n$. Then $|U_n|$ is prime for only finitely many natural
numbers $n$.

## Sources

- Dan Ismailescu, Daniel Hyunwoo Jeon, Aaron Kim, Joonbeom Kwon and Austin Lee, *Shifting Lucas Sequences Away from Primes*, INTEGERS 25 (2025), Article A42, Theorem 4(a) (quoted from their reference [2]).

Stated but not proved: `MetaMathlibExt.lucasU_square_q_finite_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html#lucas-u-square-q-finite-primes).

## Lucas sequences with power parameters have finitely many prime terms

Let $x \ne y$
be real numbers such that $x + y$ and $xy$ are integers, and let $r > 1$ be a natural
number. Let $P$ and $Q$ be integers with $P = x^r + y^r$ and $Q = x^r y^r$, and suppose
$Q \ne 0$, $P \ge 1$ and $P^2 - 4Q > 0$. Let $U_n = U_n(P, Q)$ be the Lucas sequence with
$U_0 = 0$, $U_1 = 1$ and $U_{n+2} = PU_{n+1} - QU_n$. Then $|U_n|$ is prime for only
finitely many natural numbers $n$.

## Sources

- Dan Ismailescu, Daniel Hyunwoo Jeon, Aaron Kim, Joonbeom Kwon and Austin Lee, *Shifting Lucas Sequences Away from Primes*, INTEGERS 25 (2025), Article A42, Theorem 4(b) (quoted from their reference [2]).

Stated but not proved: `MetaMathlibExt.lucasU_power_params_finite_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html#lucas-u-power-params-finite-primes).

## Fibonacci numbers shifted by $14475$ are never prime

Let $F_n$ be the $n$-th
Fibonacci number, with $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$. For every
natural number $n$, the number $F_n + 14475$ is not prime.

## Sources

- Dan Ismailescu, Daniel Hyunwoo Jeon, Aaron Kim, Joonbeom Kwon and Austin Lee, *Shifting Lucas Sequences Away from Primes*, INTEGERS 25 (2025), Article A42, Theorem 5.

Stated but not proved: `MetaMathlibExt.fib_add_14475_not_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ShiftedLucasCompositeWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html#fib-add-14475-not-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Composite terms of shifted Lucas sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/composite-terms-of-shifted-lucas-sequences)
