---
declaration: section
origin: cited
lean: MetaMathlibExt.two_pow_half_modEq_one_fermatNumber, MetaMathlibExt.sq_dvd_fermatNumber_iff, MetaMathlibExt.sq_dvd_fermatNumber_iff_wieferich_orderOf, MetaMathlibExt.gcd_pow_pow_add_one, MetaMathlibExt.monotone_cardFactors_pow_pow_add_one, MetaMathlibExt.not_pow_pow_modEq_one_of_lt, MetaMathlibExt.sq_dvd_pow_pow_add_one_wieferich, MetaMathlibExt.sq_dvd_pow_two_pow_add_one_iff_wieferich
statement: formalized
---

# Square prime factors of Fermat numbers

11 results, 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html).

## Warren–Bray congruence for prime divisors of Fermat numbers

Let $F_n = 2^{2^n} + 1$ be
the $n$-th Fermat number. For every $n \ge 2$ and every odd prime $p$ dividing $F_n$, we have
$2^{(p-1)/2} \equiv 1 \pmod{F_n}$. This result is due to Warren and Bray (1967).

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Theorem 2, citing Warren and Bray.

Stated but not proved: `MetaMathlibExt.two_pow_half_modEq_one_fermatNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#two-pow-half-mod-eq-one-fermat-number).

## Squared prime factors of Fermat numbers

Let $F_n = 2^{2^n} + 1$ be the $n$-th Fermat
number, and let $p$ be a prime dividing $F_n$. Then $p^2$ divides $F_n$ if and only if
$2^{p-1} \equiv 1 \pmod{p^2}$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Theorem 3, citing Křížek, Luca, and Somer.

Stated but not proved: `MetaMathlibExt.sq_dvd_fermatNumber_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#sq-dvd-fermat-number-iff).

## Squared prime factors of Fermat numbers via Wieferich primes and orders

Let
$F_n = 2^{2^n} + 1$ be the $n$-th Fermat number. For every natural number $n$ and every odd prime
$p$, $p^2$ divides $F_n$ if and only if $p$ is a Wieferich prime (to base $2$) and the
multiplicative order of $2$ modulo $p$ is $2^{n+1}$.

This follows from the criterion that a prime $p$ dividing $F_n$ satisfies $p^2 \mid F_n$ exactly
when $2^{p-1} \equiv 1 \pmod{p^2}$, since an odd prime $p$ divides $F_n$ exactly when the order
of $2$ modulo $p$ is $2^{n+1}$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Theorem 5, Equation (11).

Stated but not proved: `MetaMathlibExt.sq_dvd_fermatNumber_iff_wieferich_orderOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#sq-dvd-fermat-number-iff-wieferich-order).

## Greatest common divisors of generalized Fermat numbers

For natural numbers $a$, $b$ and
$k$ write $F_k(a, b) = a^{b^k} + 1$, and let $a, b \ge 2$ and $m$, $n$ be natural numbers. If
$n < m$ and $a$ and $b$ are both even, then $\gcd(F_m(a, b), F_n(a, b)) = 1$. If $n < m$, $a$ is
odd and $b$ is even, then $\gcd(F_m(a, b), F_n(a, b)) = 2$. If $n \le m$ and $b$ is odd, then
$\gcd(F_m(a, b), F_n(a, b)) = F_n(a, b)$.

The source assumes $a, b > 2$ and $0 \le n \le m$; its proof uses only $a, b \ge 2$ and treats
$m > n$ ("Since $m > n$"), and the first two cases fail for $m = n$: for $a = b = 4$ and
$m = n = 0$ the gcd is $\gcd(5, 5) = 5$, and for $a = 3$, $b = 4$ and $m = n = 0$ it is
$\gcd(4, 4) = 4$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Proposition 1.

Stated but not proved: `MetaMathlibExt.gcd_pow_pow_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#gcd-pow-pow-add-one).

## Monotonicity of the number of prime factors of generalized Fermat numbers

For natural
numbers $a$, $b$ and $n$ write $F_n(a, b) = a^{b^n} + 1$, and let $\Omega(N)$ be the number of
prime factors of $N$ counted with multiplicity. If $a, b \ge 2$ and $b$ is odd, then
$\Omega(F_n(a, b)) \le \Omega(F_m(a, b))$ for all natural numbers $n \le m$.

The source writes $\varphi_n(a, b)$ for $\Omega(F_n(a, b))$. Its open question on
$\varphi_n(2, 2)$ and its list of values of $\varphi_n(2, 2)$ are not stated here.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Corollary 1.

Stated but not proved: `MetaMathlibExt.monotone_cardFactors_pow_pow_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#monotone-card-factors-pow-pow-add-one).

## Smaller iterated powers are not congruent to one

Let $a, b, m \ge 2$ and $n \ge 1$ be
natural numbers with $a^{b^n} \not\equiv 1 \pmod m$. Then $a^{b^t} \not\equiv 1 \pmod m$ for every
natural number $t < n$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Lemma 2.

Stated but not proved: `MetaMathlibExt.not_pow_pow_modEq_one_of_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#not-pow-pow-mod-eq-one-of-lt).

## Squared prime factors of generalized Fermat numbers

For natural numbers $a$, $b$ and $n$
write $F_n(a, b) = a^{b^n} + 1$. Let $a, b \ge 2$, let $n$ be a natural number, let $p$ be an odd
prime coprime to $ab$, and write $\operatorname{ord}_p(a)$ for the multiplicative order of $a$
modulo $p$. If $p^2$ divides $F_n(a, b)$, then $a^{p-1} \equiv 1 \pmod{p^2}$ (that is, $p$ is a
Wieferich prime to base $a$) and $\operatorname{ord}_p(a)$ divides $2b^n$. Conversely, if
$a^{p-1} \equiv 1 \pmod{p^2}$ and $\operatorname{ord}_p(a) = 2b^n$, then $p^2$ divides $F_n(a, b)$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Theorem 4.

Stated but not proved: `MetaMathlibExt.sq_dvd_pow_pow_add_one_wieferich` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#sq-dvd-pow-pow-add-one-wieferich).

## Squared prime factors of $a^{2^n} + 1$

Let $p$ be an odd prime, let $a$ be a natural
number not divisible by $p$, and let $n$ be a natural number. Then $p^2$ divides $a^{2^n} + 1$ if
and only if $a^{p-1} \equiv 1 \pmod{p^2}$ (that is, $p$ is a Wieferich prime to base $a$) and the
multiplicative order of $a$ modulo $p$ is $2^{n+1}$.

The congruence $a^{p-1} \equiv 1 \pmod{p^2}$ is the source's equation (8) defining $p \in W(a)$.
The source assumes $a \ge 2$; for $a = 1$ both sides are false.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Theorem 5.

Stated but not proved: `MetaMathlibExt.sq_dvd_pow_two_pow_add_one_iff_wieferich` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#sq-dvd-pow-two-pow-add-one-iff-wieferich).

## Wieferich primes to base $a$ via multiplicative orders

Let $p$ be a prime and $a$ a
natural number not divisible by $p$. Then $a^{p-1} \equiv 1 \pmod{p^2}$, that is, $p$ is a
Wieferich prime to base $a$, if and only if the multiplicative order of $a$ modulo $p^2$ equals
the multiplicative order of $a$ modulo $p$.

The congruence $a^{p-1} \equiv 1 \pmod{p^2}$ is the source's equation (8) defining $p \in W(a)$.
The source assumes $a \ge 2$; both sides also hold for $a = 1$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Lemma 1 (iii).

Stated but not proved: `MetaMathlibExt.pow_sub_one_modEq_one_sq_iff_orderOf_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#pow-sub-one-mod-eq-one-sq-iff-order-of-e).

## Divisibility of later generalized Fermat numbers

For natural numbers $a$, $b$ and $m$
write $F_m(a, b) = a^{b^m} + 1$. Let $a, b, D \ge 2$ and $n$ be natural numbers such that $D$
divides $F_n(a, b)$. If $b$ is odd, then $D$ divides $F_{n+k}(a, b)$ for every $k \ge 1$. If $b$
is even and $D \ge 3$, then $D$ does not divide $F_{n+k}(a, b)$ for any $k \ge 1$.

The source states the even case for $D \ge 2$; its proof gives $F_{n+k}(a, b) \equiv 2 \pmod D$,
which excludes only $D = 2$, and the even case is false there: for $a = 3$, $b = 2$, $n = 0$ and
$k = 1$, $2$ divides both $F_0(3, 2) = 4$ and $F_1(3, 2) = 10$.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Theorem 7.

Stated but not proved: `MetaMathlibExt.dvd_pow_pow_add_one_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#dvd-pow-pow-add-one-shift).

## Start of the period of generalized Fermat numbers modulo the square of a prime

For
natural numbers $a$, $b$ and $k$ write $F_k(a, b) = a^{b^k} + 1$. Let $a, b \ge 2$, let $p$ be a
prime, and let $n_0$ be the least natural number with $p^2 \mid F_{n_0}(a, b)$. Say that the
sequence $(F_k(a, b))_k$ is periodic modulo $p^2$ from index $m$ if there is a $T > 0$ with
$F_{m+k+T}(a, b) \equiv F_{m+k}(a, b) \pmod{p^2}$ for every $k \ge 0$. If $b$ is odd, then $n_0$
is the least index from which the sequence is periodic modulo $p^2$; if $b$ is even, this least
index is $n_0 + 1$.

In the source's terms, $n_0$ is the index of the first term of the period when $b$ is odd, and
the index of the last term of the pre-period when $b$ is even.

## Sources

- Klaška, *Several Notes on Jakóbczyk's Hypothesis on Fermat Numbers*, INTEGERS 26 (2026), Article A77, Corollary 2.

Stated but not proved: `MetaMathlibExt.isLeast_periodic_start_pow_pow_add_one_mod_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/JakobczykFermatWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JakobczykFermatWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html#is-least-periodic-start-pow-pow-add-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square prime factors of Fermat numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/special-primes/square-prime-factors-of-fermat-numbers)
