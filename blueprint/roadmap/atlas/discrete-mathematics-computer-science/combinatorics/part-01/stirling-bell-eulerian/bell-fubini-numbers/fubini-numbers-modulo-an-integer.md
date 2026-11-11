---
declaration: section
origin: cited
lean: MetaMathlibExt.descPochhammer_eq_sum_signedStirlingFirst, MetaMathlibExt.pow_add_carmichael_modEq_of_lt, MetaMathlibExt.fubiniNumber_add_carmichael_modEq, MetaMathlibExt.fubiniNumber_eventuallyPeriodic_iff_carmichael_dvd, MetaMathlibExt.rFubini_add_carmichael_modEq
statement: formalized
---

# Fubini numbers modulo an integer

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html).

## Falling factorial in terms of signed Stirling numbers

For every natural number $n$, the
identity of polynomials with integer coefficients

$$x (x - 1) \cdots (x - n + 1) = \sum_{k=0}^{n} s(n, k)\, x^k$$

holds, where $s(n, k)$ is the signed Stirling number of the first kind.

## Sources

- Benjamin Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, Journal of Integer Sequences 28 (2025), Article 25.4.1, Proposition 2 (`jis-2025-25.4.1-prop-2`).

Stated but not proved: `MetaMathlibExt.descPochhammer_eq_sum_signedStirlingFirst` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html#desc-pochhammer-eq-sum-signed-stirling-f).

## A Carmichael congruence for all residues modulo $K$

Let $K$ be a natural number, let
$\lambda(K)$ be the value of the Carmichael function at $K$, and let $R$ be the largest exponent
in the prime factorization of $K$ ($R = 0$ for $K \le 1$). Then
$a^R \equiv a^{\lambda(K) + R} \pmod K$ for every natural number $a < K$.

## Sources

- Benjamin Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, Journal of Integer Sequences 28 (2025), Article 25.4.1, Proposition 4 (`jis-2025-25.4.1-prop-4`).

Stated but not proved: `MetaMathlibExt.pow_add_carmichael_modEq_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html#pow-add-carmichael-mod-eq-of-lt).

## Eventual periodicity of the Fubini numbers modulo $K$

Let $K$ be a natural number, let
$\lambda(K)$ be the value of the Carmichael function at $K$, and let $R$ be the largest exponent
in the prime factorization of $K$ ($R = 0$ for $K \le 1$). Then the Fubini numbers $F(n)$
satisfy $F(n + \lambda(K)) \equiv F(n) \pmod K$ for every natural number $n \ge R$.

## Sources

- Benjamin Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, Journal of Integer Sequences 28 (2025), Article 25.4.1, Corollary 10 (`jis-2025-25.4.1-cor-10`).

Stated but not proved: `MetaMathlibExt.fubiniNumber_add_carmichael_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html#fubini-number-add-carmichael-mod-eq).

## Eventual periods of the Fubini numbers modulo an odd number

Let $K$ be an odd natural
number and let $\lambda(K)$ be the value of the Carmichael function at $K$. Then a natural number
$p$ is divisible by $\lambda(K)$ if and only if there is a natural number $N$ such that the Fubini
numbers $F(n)$ satisfy $F(n + p) \equiv F(n) \pmod K$ for all $n \ge N$. In particular, the
eventual period of the Fubini numbers modulo $K$ is exactly $\lambda(K)$.

## Sources

- Benjamin Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, Journal of Integer Sequences 28 (2025), Article 25.4.1, Corollary 11 (`jis-2025-25.4.1-cor-11`).

Stated but not proved: `MetaMathlibExt.fubiniNumber_eventuallyPeriodic_iff_carmichael_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html#fubini-number-eventually-periodic-iff-ca).

## Eventual periodicity of the $r$-Fubini numbers modulo $K$

For a natural number $r \ge 1$
and a natural number $m$, let $F_r(m)$ be the number of pairs $(k, f)$ of a natural number
$k \le m$ and a surjection $f : \{0, \dots, m - 1\} \to \{0, \dots, k - 1\}$ that is injective on
the elements less than $r$; equivalently, $F_r(m)$ counts the weak orderings of $m$ elements in
which the elements less than $r$ are pairwise untied. Let $K$ be a natural number, let
$\lambda(K)$ be the value of the Carmichael function at $K$, and let $R$ be the largest exponent
in the prime factorization of $K$ ($R = 0$ for $K \le 1$). Then
$F_r(n + \lambda(K)) \equiv F_r(n) \pmod K$ for every natural number $n \ge r - 1 + R$.

## Sources

- Benjamin Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, Journal of Integer Sequences 28 (2025), Article 25.4.1, Corollary 12 (`jis-2025-25.4.1-cor-12`).

Stated but not proved: `MetaMathlibExt.rFubini_add_carmichael_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RiggedHorseNumbersWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html#r-fubini-add-carmichael-mod-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fubini numbers modulo an integer](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/fubini-numbers-modulo-an-integer)
