---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSumOfTwoPrimePowers, MetaMathlibExt.isSumOfTwoPrimePowers_two, MetaMathlibExt.not_isSumOfTwoPrimePowers_of_lt_two, MetaMathlibExt.tribonacci_infinite_not_isSumOfTwoPrimePowers, MetaMathlibExt.shiftedPadovan_infinite_not_isSumOfTwoPrimePowers, MetaMathlibExt.perrin_infinite_not_isSumOfTwoPrimePowers, MetaMathlibExt.leonardo_infinite_not_isSumOfTwoPrimePowers, MetaMathlibExt.infinite_thirdOrderRecurrence_with_infinite_not_isSum
statement: formalized
---

# Recurrence terms that are not sums of two prime powers

8 results, 3 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html).

## Sums of two prime powers

An integer $n$ is a sum of two prime powers if
$n = p^a + q^b$ for some primes $p$ and $q$ and some natural numbers $a$ and $b$. Since the
exponents may be $0$, the number $1 = p^0$ counts as a prime power here.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3.

Formalized by `MetaMathlibExt.IsSumOfTwoPrimePowers`, a definition declared in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#is-sum-of-two-prime-powers).

## $2$ is a sum of two prime powers

The integer $2$ is a sum of two prime powers, since
$2 = 2^0 + 2^0$.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3.

Formalized by `MetaMathlibExt.isSumOfTwoPrimePowers_two`, a theorem declared in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#is-sum-of-two-prime-powers-two).

## Integers below $2$ are not sums of two prime powers

If $n$ is an integer with $n < 2$,
then $n$ is not a sum of two prime powers, since every prime power $p^a$ is at least $1$.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3.

Formalized by `MetaMathlibExt.not_isSumOfTwoPrimePowers_of_lt_two`, a theorem declared in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#not-is-sum-of-two-prime-powers-of-lt-two).

## Infinitely many Tribonacci numbers are not sums of two prime powers

Let $(T_n)_{n \ge 0}$
be the Tribonacci sequence, given by $T_0 = 0$, $T_1 = 0$, $T_2 = 1$ and
$T_{n+3} = T_{n+2} + T_{n+1} + T_n$. There are infinitely many natural numbers $k$ such that
$T_k$ is not a sum of two prime powers.

The paper proves the stronger statement that this holds for every sufficiently large
$k \equiv 3817 \pmod{163843680}$. That form is not stated here, since the residue class depends
on how the sequence is indexed.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3, Theorem 2 (`jis-2026-26.2.3-thm-2`).

Stated but not proved: `MetaMathlibExt.tribonacci_infinite_not_isSumOfTwoPrimePowers` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#tribonacci-infinite-not-is-sum-of-two-pr).

## Infinitely many Padovan numbers are not sums of two prime powers

Let $(a_n)_{n \ge 0}$ be
the shifted Padovan sequence, given by $a_0 = 1$, $a_1 = 0$, $a_2 = 1$ and
$a_{n+3} = a_{n+1} + a_n$, so that $a_{n+2} = P_n$ is the $n$-th Padovan number, where
$P_0 = P_1 = P_2 = 1$ and $P_{n+3} = P_{n+1} + P_n$. There are infinitely many natural numbers
$k$ such that $a_k$ is not a sum of two prime powers.

The paper proves the stronger statement that this holds for every sufficiently large
$k \equiv 45750 \pmod{967206240}$. That form is not stated here, since the residue class depends
on how the sequence is indexed.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3, Theorem 3 (`jis-2026-26.2.3-thm-3`).

Stated but not proved: `MetaMathlibExt.shiftedPadovan_infinite_not_isSumOfTwoPrimePowers` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#shifted-padovan-infinite-not-is-sum-of-t).

## Infinitely many Perrin numbers are not sums of two prime powers

Let $(E_n)_{n \ge 0}$ be
the Perrin sequence, given by $E_0 = 3$, $E_1 = 0$, $E_2 = 2$ and $E_{n+3} = E_{n+1} + E_n$.
There are infinitely many natural numbers $k$ such that $E_k$ is not a sum of two prime powers.

The paper proves the stronger statement that this holds for every sufficiently large
$k \equiv 472190 \pmod{967206240}$. That form is not stated here, since the residue class
depends on how the sequence is indexed.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3, Theorem 5 (`jis-2026-26.2.3-thm-5`).

Stated but not proved: `MetaMathlibExt.perrin_infinite_not_isSumOfTwoPrimePowers` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#perrin-infinite-not-is-sum-of-two-prime).

## Infinitely many Leonardo numbers are not sums of two prime powers

Let $(L_n)_{n \ge 0}$
be the Leonardo numbers, the generalized Leonardo numbers $L_{1,n}$ with parameter $1$, given
by $L_0 = L_1 = 1$ and $L_{n+2} = L_{n+1} + L_n + 1$. There are infinitely many natural numbers
$k$ such that $L_k$ is not a sum of two prime powers.

The paper proves the stronger statement that this holds for every sufficiently large
$k \equiv 539073 \pmod{3543120}$. That form is not stated here, since the residue class depends
on how the sequence is indexed.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3, Theorem 6 (`jis-2026-26.2.3-thm-6`).

Stated but not proved: `MetaMathlibExt.leonardo_infinite_not_isSumOfTwoPrimePowers` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#leonardo-infinite-not-is-sum-of-two-prim).

## Third-order recurrences with infinitely many terms not sums of two prime powers

There
are infinitely many sequences $(s_n)_{n \ge 0}$ of positive integers with all of the following
properties: each value is taken by $s_n$ for only finitely many $n$; there are integers
$c_0, c_1, c_2$ with $c_0 \ne 0$ and $s_{n+3} = c_0 s_n + c_1 s_{n+1} + c_2 s_{n+2}$ for all
$n \ge 0$; there are no integers $d_0, d_1$ with $s_{n+2} = d_0 s_n + d_1 s_{n+1}$ for all
$n \ge 0$; and $s_k$ is not a sum of two prime powers for infinitely many $k$.

The condition that each value is taken only finitely often excludes trivial examples such as
periodic sequences taking the value $1$ infinitely often: no integer below $2$ is a sum of two
prime powers.

## Sources

- Baczkowski and Keener, *Third-Order Recurrence Sequences with Infinitely Many Terms not Equal to the Sum of Two Prime Powers*, Journal of Integer Sequences 29 (2026), Article 26.2.3, Corollary 1 (`jis-2026-26.2.3-cor-1`).

Stated but not proved: `MetaMathlibExt.infinite_thirdOrderRecurrence_with_infinite_not_isSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ThirdOrderPrimePowersWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html#infinite-third-order-recurrence-with-inf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Recurrence terms that are not sums of two prime powers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/recurrence-terms-that-are-not-sums-of-two-prime)
