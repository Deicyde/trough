---
declaration: section
origin: cited
lean: MetaMathlibExt.acceptableSeed_of_jacobi, MetaMathlibExt.mersenne_prime_iff_lucasLehmer_six_div_five, MetaMathlibExt.lehmerV, MetaMathlibExt.lehmerV_add_four, MetaMathlibExt.lehmerV_two_neg_one, MetaMathlibExt.mersenne_prime_of_dvd_lehmerV, MetaMathlibExt.mersenne_dvd_lehmerV_of_jacobi, MetaMathlibExt.mersenne_dvd_lehmerV_of_diophantine
statement: formalized
---

# Lucas–Lehmer test

22 results, 10 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html).

## Lucas–Lehmer test with a general seed

Let $n \ge 3$ be an odd natural number, let
$M_n = 2^n - 1$, and let $s_1$ be an integer. Define $s_{k+1} = s_k^2 - 2$ for $k \ge 1$. If the
Jacobi symbols satisfy $\left(\frac{s_1 + 2}{M_n}\right) = -1$ and
$\left(\frac{s_1 - 2}{M_n}\right) = 1$, then $M_n$ is prime if and only if $M_n$ divides
$s_{n-1}$.

In the terminology of Roettger and Williams, such a seed $s_1$ is acceptable: the Lucas–Lehmer
test started at $s_1$ decides the primality of $M_n$ (their Assertion A).

Proof: Following Mathlib's Lucas-Lehmer order argument, sufficiency uses a quadratic extension
and the least prime factor; necessity uses the Jacobi conditions and Frobenius conjugation as in
Lehmer (1930) and Roettger-Williams (2025).

## Sources

- E. L. Roettger and H. C. Williams, "Some Remarks Concerning the Lucas-Lehmer Primality Test," Journal of Integer Sequences 28 (2025), Article 25.2.5, Theorem, lines 814–819; Assertion A at lines 187–190, https://cs.uwaterloo.ca/journals/JIS/VOL28/Roettger/roettger15.tex

Formalized by `MetaMathlibExt.acceptableSeed_of_jacobi`, a theorem declared in [MathlibExt/NumberTheory/LucasLehmerAcceptableSeed.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LucasLehmerAcceptableSeed.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#acceptable-seed-of-jacobi).

## Lucas–Lehmer test with the rational seed $6/5$

Let $n \ge 3$, let $M_n = 2^n - 1$, and
define $s_1 = 6 \cdot 5^{-1}$ and $s_{k+1} = s_k^2 - 2$ in $\mathbb{Z}/M_n\mathbb{Z}$. If
$n \equiv 3 \pmod 4$, then $M_n$ is prime if and only if $s_{n-1} = 0$. If $n \equiv 1 \pmod 4$,
then $M_n$ is prime if and only if $s_{n-2} = 0$.

In both cases $n$ is odd, so $5$ does not divide $M_n$ and $5^{-1}$ is the inverse of $5$
modulo $M_n$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Theorem 17.

Stated but not proved: `MetaMathlibExt.mersenne_prime_iff_lucasLehmer_six_div_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-prime-iff-lucas-lehmer-six-div).

## Lehmer's companion sequence

For integers $R$ and $Q$, Lehmer's companion sequence
$\bar V_k(R, Q)$, $k = 0, 1, 2, \ldots$, is the integer sequence with $\bar V_0 = 2$,
$\bar V_1 = 1$, $\bar V_2 = R - 2Q$, $\bar V_3 = R - 3Q$ and
$\bar V_{k+4} = (R - 2Q)\,\bar V_{k+2} - Q^2\,\bar V_k$ for every $k \ge 0$.

With $P = \sqrt R$ and the Lucas sequence $V_k(P, Q)$ given by $V_0 = 2$, $V_1 = P$ and
$V_{k+2} = P V_{k+1} - Q V_k$, for $R \ne 0$ the term $\bar V_k(R, Q)$ equals $V_k(\sqrt R, Q)$
for even $k$ and $V_k(\sqrt R, Q)/\sqrt R$ for odd $k$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 2 (definition of `V̄_n` and recurrence (4thLehmer)).

Formalized by `MetaMathlibExt.lehmerV`, a definition declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#lehmer-v).

## Fourth-order recurrence of Lehmer's companion sequence

For all integers $R$ and $Q$ and
every natural number $k$, Lehmer's companion sequence satisfies
$\bar V_{k+4}(R, Q) = (R - 2Q)\,\bar V_{k+2}(R, Q) - Q^2\,\bar V_k(R, Q)$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 2, recurrence (4thLehmer).

Formalized by `MetaMathlibExt.lehmerV_add_four`, a theorem declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#lehmer-v-add-four).

## Lehmer's companion sequence for $R = 2$ and $Q = -1$

For $R = 2$ and $Q = -1$, Lehmer's
companion sequence has $\bar V_2(2, -1) = 4$, $\bar V_4(2, -1) = 14$ and
$\bar V_8(2, -1) = 194$.

These are the parameters giving the seed $4$, and $14 = 4^2 - 2$ and $194 = 14^2 - 2$, as the
doubling formula (LehmerV2n) predicts.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 2 (formula (LehmerV2n) and the case `R = 2`, `Q = -1` after Theorem 6).

Formalized by `MetaMathlibExt.lehmerV_two_neg_one`, a theorem declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#lehmer-v-two-neg-one).

## Lehmer-sequence primality criterion for Mersenne numbers

Let $n \ge 3$ be odd, let
$M_n = 2^n - 1$, and let $R$ and $Q$ be integers with $\gcd(M_n, Q) = 1$. If $M_n$ divides
Lehmer's companion term $\bar V_{2^{n-1}}(R, Q)$, then $M_n$ is prime.

Here $2^{n-1} = (M_n + 1)/2$. No coprimality of $R$ and $Q$ and no condition on $D = R - 4Q$
is assumed.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Lemma 4.

Stated but not proved: `MetaMathlibExt.mersenne_prime_of_dvd_lehmerV` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-prime-of-dvd-lehmer-v).

## Divisibility of Lehmer's companion sequence by a Mersenne prime

Let $n \ge 3$ be an odd
natural number such that $M_n = 2^n - 1$ is prime, let $R$ and $Q$ be integers, let
$\bar V_k(R, Q)$ denote Lehmer's companion sequence, and put $D = R - 4Q$. If the Jacobi symbols
$\left(\frac{DR}{M_n}\right)$ and $\left(\frac{QR}{M_n}\right)$ are both $-1$, then $M_n$
divides $\bar V_{(M_n+1)/2}(R, Q) = \bar V_{2^{n-1}}(R, Q)$.

Since $M_n$ is prime, these Jacobi symbols are Legendre symbols.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Lemma 5.

Stated but not proved: `MetaMathlibExt.mersenne_dvd_lehmerV_of_jacobi` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-dvd-lehmer-v-of-jacobi).

## Divisibility of Lehmer's companion sequence by a Mersenne prime, Diophantine form

Let
$n \ge 3$ be an odd natural number such that $M_n = 2^n - 1$ is prime, and let $r$, $d$, $q$,
$X$, $Y$, $Z$ be integers with $\gcd(M_n, Y) = 1$ and $4qY^2 = rX^2 - dZ^2$. Put $R = rX^2$ and
$Q = qY^2$, and let $\bar V_k(R, Q)$ denote Lehmer's companion sequence. If the Jacobi symbols
$\left(\frac{rd}{M_n}\right)$ and $\left(\frac{qr}{M_n}\right)$ are both $-1$, then $M_n$ divides
$\bar V_{(M_n+1)/2}(R, Q) = \bar V_{2^{n-1}}(R, Q)$.

Here $D = R - 4Q = dZ^2$, and since $M_n$ is prime the Jacobi symbols are Legendre symbols.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Lemma 7.

Stated but not proved: `MetaMathlibExt.mersenne_dvd_lehmerV_of_diophantine` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-dvd-lehmer-v-of-diophantine).

## Euler's family of solutions of $aT^2 - bU^2 = c$

Let $a$, $b$, $c$ be integers
with $ab > 1$, $ab$ not a perfect square and $c \ne 0$, and let $T_1$, $U_1$ be integers with
$aT_1^2 - bU_1^2 = c$. Let $\varepsilon = x_1 + y_1\sqrt{ab}$ be the fundamental solution of
$x^2 - ab\,y^2 = 1$ and, for every natural number $j$, write
$\varepsilon^j = x_j + y_j\sqrt{ab}$. Then for every $j \ge 0$ the integers
$T = T_1 x_j + b U_1 y_j$ and $U = a T_1 y_j + U_1 x_j$ satisfy $aT^2 - bU^2 = c$, and different
$j$ give different pairs $(T, U)$.

The hypothesis $c \ne 0$ is added to the source statement: for $c = 0$ the only integer solution
is $(0, 0)$, since $ab$ is not a square.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Theorem 8.

Stated but not proved: `MetaMathlibExt.pell_euler_solutions` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#pell-euler-solutions).

## Odd squarefree part

For an integer $N$ and a natural number $k$, $k$ is an odd
squarefree part of $N$, written $N^* = k$, when $k$ is odd and squarefree and $N = 2^a m^2 k$
for some natural number $a$ and some integer $m$.

For positive $N$ such a $k$ is unique: it is the squarefree part of $N$ when that is odd, and
half of it otherwise.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 7 (definition of `N^*`).

Formalized by `MetaMathlibExt.IsOddSquarefreePart`, a definition declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#is-odd-squarefree-part).

## The odd squarefree part of $360$

The number $5$ is the odd squarefree part of $360$:
$5$ is odd and squarefree, and $360 = 2^a m^2 \cdot 5$ for some natural number $a$ and some
integer $m$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 7 (example `10 = sqf(360)`).

Formalized by `MetaMathlibExt.isOddSquarefreePart_360`, a theorem declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#is-odd-squarefree-part-360).

## The order $\Omega(m)$ of $2$, doubled when odd

For a natural number $m$, let $\omega(m)$
be the multiplicative order of $2$ modulo $m$, taken to be $0$ when no positive power of $2$ is
congruent to $1$ modulo $m$ (that is, when $m$ is even). Then $\Omega(m) = 2\omega(m)$ if
$\omega(m)$ is odd, and $\Omega(m) = \omega(m)$ otherwise.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 7 (definitions of `ω(m)` and `Ω(m)`).

Formalized by `MetaMathlibExt.mersenneOmega`, a definition declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-omega).

## $\Omega$ for the seed $37$

We have $\Omega(1365) = 12$, where $\Omega(m)$ is the
multiplicative order of $2$ modulo $m$, doubled when that order is odd. Here $1365 = 35 \cdot 39$
is the product of the odd squarefree parts $35$ of $37 - 2$ and $39$ of $37 + 2$, the parts
$s_1^-$ and $s_1^+$ for the seed $s_1 = 37$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 7 (example `s_1 = 37`).

Formalized by `MetaMathlibExt.mersenneOmega_1365`, a theorem declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-omega-1365).

## Condition (etar) on Jacobi symbols of $M_n$

Let $s^-$, $s^+$ and $n$ be natural
numbers and let $M_n = 2^n - 1$. For a natural number $s$ write $\left(\frac{M_n}{s}\right)$ for
the Jacobi symbol, the product of the Legendre symbols $\left(\frac{M_n}{p}\right)$ over the
prime factors $p$ of $s$ counted with multiplicity (so it is $1$ for $s = 0$ and $s = 1$).
Condition (etar) holds for $s^-$, $s^+$ and $n$ when $s^- = 1$ or
$\left(\frac{M_n}{s^-}\right) = (-1)^{(s^- - 1)/2}$, and moreover
$\left(\frac{M_n}{s^+}\right) = (-1)^{(s^+ + 1)/2}$. Here the exponents are rounded down, and
$s^- - 1$ is read as $0$ when $s^- = 0$.

In the source, $s^-$ and $s^+$ are the odd squarefree parts $s_1^-$ and $s_1^+$ of $s_1 - 2$
and $s_1 + 2$ for a seed $s_1$. For squarefree $s$ the Jacobi symbol $\left(\frac{M_n}{s}\right)$
is the product of $\eta_n(p) = \left(\frac{M_n}{p}\right)$ over the primes $p$ dividing $s$,
which is how the source states the condition.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 7, condition (etar).

Formalized by `MetaMathlibExt.MersenneEtaCondition`, a definition declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-eta-condition).

## Condition (etar) for the seed $37$

For the seed $s_1 = 37$, the odd squarefree parts of
$s_1 - 2 = 35$ and $s_1 + 2 = 39$ are $s_1^- = 35$ and $s_1^+ = 39$. Condition (etar) for
$s_1^- = 35$ and $s_1^+ = 39$ holds for $n = 7$ and fails for $n = 1$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Section 7 (example `s_1 = 37`, `𝒜(37) = {7}`).

Formalized by `MetaMathlibExt.mersenneEtaCondition_37`, a theorem declared in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-eta-condition-37).

## Infinitely many acceptable seeds with the same odd squarefree parts

Let $n \ge 3$ be a
natural number and $M_n = 2^n - 1$. For an integer $S$ put $S_1 = S$ and $S_{k+1} = S_k^2 - 2$,
and call $S$ an acceptable seed for $M_n$ if $M_n$ is prime exactly when $M_n$ divides
$S_{n-1}$. Let $s_1 \ge 3$ be an integer that is an acceptable seed for $M_n$, and let $s_1^-$
and $s_1^+$ be the odd squarefree parts of $s_1 - 2$ and $s_1 + 2$. Then there are infinitely
many integers $S \ge 3$ that are acceptable seeds for $M_n$ and for which $s_1^-$ and $s_1^+$
are the odd squarefree parts of $S - 2$ and $S + 2$.

Seeds are taken $\ge 3$ (the paper's seeds are nonnegative, and the odd squarefree part of
$S - 2$ needs $S - 2 > 0$).

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Theorem 10.

Stated but not proved: `MetaMathlibExt.infinite_acceptableSeeds_same_parts` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#infinite-acceptable-seeds-same-parts).

## Order of $2$ modulo a product of coprime odd numbers

Let $m_1$ and $m_2$ be coprime odd
natural numbers, and write $\omega(m)$ for the multiplicative order of $2$ modulo $m$. Then
$\omega(m_1 m_2) = \operatorname{lcm}(\omega(m_1), \omega(m_2))$.

The printed $\operatorname{lcm}(\omega(m_1)\omega(m_2))$ is read as
$\operatorname{lcm}(\omega(m_1), \omega(m_2))$; the product reading fails, since $\omega(15) = 4$
while $\omega(3)\omega(5) = 8$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Proposition 11.

Stated but not proved: `MetaMathlibExt.orderOf_two_mul_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#order-of-two-mul-coprime).

## A zero Legendre symbol forces $\gcd(n, \Omega) > 1$

Let $s_1 \ge 3$ be an integer, let
$s_1^-$ and $s_1^+$ be the odd squarefree parts of $s_1 - 2$ and $s_1 + 2$, and let
$\Omega = \Omega(s_1^- s_1^+)$. Let $p$ be a prime dividing $s_1^- s_1^+$, let $n$ be a natural
number and let $M_n = 2^n - 1$. If the Legendre symbol $\left(\frac{M_n}{p}\right)$ is $0$, then
$\gcd(n, \Omega) > 1$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Proposition 12.

Stated but not proved: `MetaMathlibExt.one_lt_gcd_mersenneOmega_of_legendreSym_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#one-lt-gcd-mersenne-omega-of-legendre-sy).

## Condition (etar) fails for some reduced residue when $s_1^- \equiv 3 \pmod 4$

Let
$s_1 \ge 3$ be an integer, let $s_1^-$ and $s_1^+$ be the odd squarefree parts of $s_1 - 2$ and
$s_1 + 2$, and let $\Omega = \Omega(s_1^- s_1^+)$ be the order of $2$ modulo $s_1^- s_1^+$,
doubled when it is odd. If $s_1^- \equiv 3 \pmod 4$, then there is a natural number $n$ with
$1 \le n < \Omega$ and $\gcd(n, \Omega) = 1$ for which condition (etar) for $s_1^-$, $s_1^+$
and $n$ fails.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Lemma 13.

Stated but not proved: `MetaMathlibExt.exists_not_mersenneEtaCondition_of_minus` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#exists-not-mersenne-eta-condition-of-min).

## Condition (etar) fails for some reduced residue when $s_1^+ \equiv 1 \pmod 4$

Let
$s_1 \ge 3$ be an integer, let $s_1^-$ and $s_1^+$ be the odd squarefree parts of $s_1 - 2$ and
$s_1 + 2$, and let $\Omega = \Omega(s_1^- s_1^+)$ be the order of $2$ modulo $s_1^- s_1^+$,
doubled when it is odd. If $s_1^+ \equiv 1 \pmod 4$, then there is a natural number $n$ with
$1 \le n < \Omega$ and $\gcd(n, \Omega) = 1$ for which condition (etar) for $s_1^-$, $s_1^+$
and $n$ fails.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Lemma 14.

Stated but not proved: `MetaMathlibExt.exists_not_mersenneEtaCondition_of_plus` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#exists-not-mersenne-eta-condition-of-plu).

## Residues mod $4$ of $s_1^-$ and $s_1^+$ when (etar) always holds

Let $s_1 \ge 3$ be an
integer, let $s_1^-$ and $s_1^+$ be the odd squarefree parts of $s_1 - 2$ and $s_1 + 2$, and let
$\Omega = \Omega(s_1^- s_1^+)$. If the number of integers $n$ with $1 \le n < \Omega$ and
$\gcd(n, \Omega) = 1$ for which condition (etar) holds for $s_1^-$, $s_1^+$ and $n$ equals
$\varphi(\Omega)$, then $s_1^- \equiv 1 \pmod 4$ and $s_1^+ \equiv 3 \pmod 4$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Theorem 15.

Stated but not proved: `MetaMathlibExt.minus_mod_four_of_mersenneEtaCondition_all` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#minus-mod-four-of-mersenne-eta-condition).

## Condition (etar) fails for some reduced residue when the seed is odd

Let $s_1 \ge 3$ be
an odd integer, let $s_1^-$ and $s_1^+$ be the odd squarefree parts of $s_1 - 2$ and $s_1 + 2$,
and let $\Omega = \Omega(s_1^- s_1^+)$. Then the number of integers $n$ with $1 \le n < \Omega$
and $\gcd(n, \Omega) = 1$ for which condition (etar) holds for $s_1^-$, $s_1^+$ and $n$ is not
equal to $\varphi(\Omega)$.

## Sources

- E. L. Roettger and H. C. Williams, *Some Remarks Concerning the Lucas-Lehmer Primality Test*, Journal of Integer Sequences 28 (2025), Article 25.2.5, Corollary 16.

Stated but not proved: `MetaMathlibExt.mersenneEtaCondition_not_all_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LucasLehmerRationalSeedWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html#mersenne-eta-condition-not-all-of-odd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucas–Lehmer test](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/lucas-lehmer-test)
