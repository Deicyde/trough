---
declaration: section
origin: cited
lean: MetaMathlibExt.lucasU_two_mul_eq_lucasU_mul_lucasV, MetaMathlibExt.lucasU_dvd_and_lucasV_dvd_of_dvd, MetaMathlibExt.p_dvd_lucasU_two_mul_and_lucasV_of_odd, MetaMathlibExt.lucasU_lucasV_neg_p, MetaMathlibExt.lucas_recurrence_add_modEq_of_dvd_lucasU, MetaMathlibExt.prime_pow_succ_dvd_lucasU_two_mul_iff, MetaMathlibExt.gcd_lucasU_two_mul_div_p_eq_one, MetaMathlibExt.lucasU_mod_two
statement: formalized
---

# Divisibility properties of Lucas sequences

60 results, 20 proved and 40 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html).

## Doubling formula $U_{2n} = U_n V_n$ for Lucas sequences

Let $P$ and $Q$ be integers with
$Q \ne 0$, and let $U$ and $V$ be the Lucas sequences $U(P, Q)$ and $V(P, Q)$. Then
$U_{2n} = U_n V_n$ for every natural number $n$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Proposition 2.3 (i).

Stated but not proved: `MetaMathlibExt.lucasU_two_mul_eq_lucasU_mul_lucasV` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-two-mul-eq-lucas-u-mul-lucas-v).

## Divisibility of Lucas sequences at divisible indices

Let $U = U(P, Q)$ and
$V = V(P, Q)$ be the Lucas sequences with integer parameters $P$ and $Q \ne 0$, and let $m$ and
$n$ be natural numbers with $m \mid n$. Then $U_m \mid U_n$, and if moreover $n/m$ is odd, then
$V_m \mid V_n$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Proposition 2.3 (iii), (iv).

Stated but not proved: `MetaMathlibExt.lucasU_dvd_and_lucasV_dvd_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-dvd-and-lucas-v-dvd-of-dvd).

## $P$ divides $U_{2n}$, and $V_n$ for odd $n$

Let $P$ and $Q$ be integers with $Q \ne 0$,
and let $U$ and $V$ be the Lucas sequences $U(P, Q)$ and $V(P, Q)$. Then $P \mid U_{2n}$ for every
natural number $n$, and $P \mid V_n$ for every odd natural number $n$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Proposition 2.3 (v), (vi).

Stated but not proved: `MetaMathlibExt.p_dvd_lucasU_two_mul_and_lucasV_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#p-dvd-lucas-u-two-mul-and-lucas-v-of-odd).

## Lucas sequences under negation of the first parameter

For integers $P$ and $Q \ne 0$ and
every natural number $n$, the Lucas sequences $U$ and $V$ satisfy
$U_n(-P, Q) = (-1)^{n+1} U_n(P, Q)$ and $V_n(-P, Q) = (-1)^n V_n(P, Q)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Proposition 2.3 (vii), (viii).

Stated but not proved: `MetaMathlibExt.lucasU_lucasV_neg_p` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-lucas-v-neg-p).

## Shift congruence for the Lucas recurrence

Let $U = U(P, Q)$ be the Lucas sequence with
integer parameters $P$ and $Q \ne 0$, and let $(W_n)_{n \ge 0}$ be a sequence of integers with
$W_{n+2} = P W_{n+1} - Q W_n$ for every $n \ge 0$. If $t \ge 0$ and $m$ are integers with
$m \mid U_t$ and $\gcd(m, Q) = 1$, then $W_{n+t} \equiv U_{t+1} W_n \pmod{m}$ for every $n \ge 0$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 2.5.

Stated but not proved: `MetaMathlibExt.lucas_recurrence_add_modEq_of_dvd_lucasU` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-recurrence-add-mod-eq-of-dvd-lucas).

## When $p^{i+1}$ divides $U_{2n}$, for a prime power $p^i$ exactly dividing $P$

Let $P$ and
$Q$ be coprime integers with $Q \ne 0$, and let $U_n$ be the Lucas sequence $U(P, Q)$. Let $p$ be
a prime and $i \ge 1$ such that $p^i \mid P$ and $p^{i+1} \nmid P$. Then for every positive
integer $n$, $p^{i+1} \mid U_{2n}$ if and only if $p \mid n$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 2.6, first claim.

Stated but not proved: `MetaMathlibExt.prime_pow_succ_dvd_lucasU_two_mul_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#prime-pow-succ-dvd-lucas-u-two-mul-iff).

## Coprimality of $U_{2n}/P$ and $P$

Let $P$ and $Q$ be integers with $Q \ne 0$, $P \ne 0$
and $\gcd(P, Q) = 1$, and let $(U_n)$ be the Lucas sequence $U(P, Q)$. If $n$ is a positive
integer with $\gcd(n, P) = 1$, then $\gcd(U_{2n}/P, P) = 1$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 2.6, "in particular" claim.

Stated but not proved: `MetaMathlibExt.gcd_lucasU_two_mul_div_p_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#gcd-lucas-u-two-mul-div-p-eq-one).

## Lucas sequences modulo 2

Let $U = U(P, Q)$ be the Lucas sequence with integer parameters
$P$ and $Q \ne 0$, let $D = P^2 - 4Q$, and suppose $2 \nmid \gcd(P, Q)$. Then $U$ is periodic
modulo $2$ from index $1$ on: there is $k > 0$ with $U_{n+k} \equiv U_n \pmod 2$ for every
$n \ge 1$. If $P$ is odd and $Q$ is even, then $U_n$ is odd for every $n \ge 1$. If $P$ is even
and $Q$ is odd, then for every $n \ge 0$, $2 \mid U_n$ if and only if $2 \mid n$; moreover
$2 \mid D$. If $P$ and $Q$ are both odd, then for every $n \ge 0$, $2 \mid U_n$ if and only if
$3 \mid n$.

The periodicity need not start at $n = 0$: for $P = 1$ and $Q = 2$, $U$ is $0, 1, 1, 1, \dots$
modulo $2$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 2.7.

Stated but not proved: `MetaMathlibExt.lucasU_mod_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-mod-two).

## Lucas sequences modulo 3

Let $U = U(P, Q)$ be the Lucas sequence with integer parameters
$P$ and $Q \ne 0$, let $D = P^2 - 4Q$, and suppose $3 \nmid \gcd(P, Q)$. Then $U$ is periodic
modulo $3$ from index $1$ on: there is $k > 0$ with $U_{n+k} \equiv U_n \pmod 3$ for every
$n \ge 1$. If $3 \mid Q$, then $3 \nmid U_n$ for every $n \ge 1$. If $3 \mid P$, then for every
$n \ge 0$, $3 \mid U_n$ if and only if $2 \mid n$. If $3 \nmid P$ and $Q \equiv -1 \pmod 3$,
then for every $n \ge 0$, $3 \mid U_n$ if and only if $4 \mid n$. If $3 \nmid P$ and
$Q \equiv 1 \pmod 3$, then for every $n \ge 0$, $3 \mid U_n$ if and only if $3 \mid n$; moreover
$3 \mid D$.

The periodicity need not start at $n = 0$: for $P = 1$ and $Q = 3$, $U$ is $0, 1, 1, 1, \dots$
modulo $3$. The source's values $\rho(3) = 2, 4, 3$ of the rank of apparition are the least
positive indices these equivalences give.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 2.8.

Stated but not proved: `MetaMathlibExt.lucasU_mod_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-mod-three).

## Growth and positivity of Lucas sequences with positive discriminant

Let $P, Q$ be
integers with $P \neq 0$, $Q \neq 0$ and $D = P^2 - 4Q > 0$, and let $U = U(P, Q)$ and
$V = V(P, Q)$ be the Lucas sequences. Then $|U_n| < |U_{n+1}|$ for every $n \ge 2$ and
$|V_n| < |V_{n+1}|$ for every $n \ge 1$; if $P > 0$, then $U_n > 0$ for every $n \ge 1$ and
$V_n > 0$ for every $n \ge 0$; and $|U_3| \ge 3$ unless $|P| = 1$ and $Q = -1$.

When $Q \neq 0$ and $D > 0$, the condition $P \neq 0$ is equivalent to the pair $(P, Q)$ being
nondegenerate (Theorem 2.1 of the source).

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 2.9.

Stated but not proved: `MetaMathlibExt.lucas_abs_strictMono_of_discr_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-abs-strict-mono-of-discr-pos).

## $U_n$ divides none of $U_1, \dots, U_{n-1}$

Let $P$ and $Q$ be integers with $P \ne 0$,
$Q \ne 0$ and $D = P^2 - 4Q > 0$, and let $U_n$ be the Lucas sequence $U(P, Q)$. Then for every
$n \ge 3$ and every $k$ with $0 < k < n$, $U_n$ does not divide $U_k$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Corollary 2.10.

Stated but not proved: `MetaMathlibExt.not_lucasU_dvd_lucasU_of_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#not-lucas-u-dvd-lucas-u-of-lt).

## Common divisors of $P$ and the discriminant

Let $P$ and $Q$ be coprime integers and let
$D = P^2 - 4Q$. Then $\gcd(P, D)$ divides $4$, and $\gcd(P, D') = 1$ for every odd integer $D'$
dividing $D$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 4.9.

Stated but not proved: `MetaMathlibExt.gcd_p_discr_dvd_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#gcd-p-discr-dvd-four).

## Parity of $U_m$ and $U_{2m}/P$ and their coprimality to $D$

Let $P$ and $Q$ be coprime
integers with $P \ne 0$ and $Q \ne 0$, let $U_n$ be the Lucas sequence $U(P, Q)$, and let
$D = P^2 - 4Q$. Let $m$ be an odd natural number with $\gcd(m, PQD) = 1$, and with $3 \nmid m$ if
$P$ and $Q$ are both odd. Then $U_m$ and $U_{2m}/P$ are odd, and each of them is coprime to $D$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 4.10.

Stated but not proved: `MetaMathlibExt.odd_lucasU_coprime_discr` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#odd-lucas-u-coprime-discr).

## Composite terms of Lucas sequences with positive discriminant

Let $U = U(P, Q)$ be the
Lucas sequence with integer parameters $P \ne 0$ and $Q \ne 0$ such that $\gcd(P, Q) = 1$ and
$D = P^2 - 4Q > 0$, and let $m \ge 5$ be an odd integer. If $m$ is not prime, then $U_m$ is
composite; and $U_{2m}/P$ is always composite. Here an integer $N$ is composite when $|N| > 1$
and $|N|$ is not prime.

Since $D > 0$, the conditions $P \ne 0$ and $Q \ne 0$ say that $U$ is nondegenerate. The quotient
$U_{2m}/P$ is an integer because $P \mid U_{2m}$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Corollary 4.2.

Stated but not proved: `MetaMathlibExt.lucasU_composite_of_discr_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-composite-of-discr-pos).

## Pseudoprime candidates from a Lucas sequence

Let $U = U(P, Q)$ be the Lucas sequence with
integer parameters $P \ne 0$ and $Q \ne 0$ such that $\gcd(P, Q) = 1$ and $D = P^2 - 4Q > 0$.
Let $m > 1$ be an odd integer with $\gcd(m, PQD) = 1$, and assume $3 \nmid m$ when $P$ and $Q$
are both odd. Put $N_1 = U_m$ and $N_2 = U_{2m}/P$. Then $N_1$ and $N_2$ are positive and odd,
and $\gcd(N_1 N_2, PQD) = 1$. If $m$ is not prime, then $N_1$ and $N_2$ are composite, that is,
$|N_i| > 1$ and $|N_i|$ is not prime for $i = 1, 2$. If $P$ is odd, or $P \equiv 0 \pmod 4$ and
$Q \equiv -1 \pmod 4$, or $P \equiv 2 \pmod 4$ and $Q \equiv -1 \pmod 8$, then the Jacobi
symbols satisfy $(D/m) = (D/|N_1|) = (D/|N_2|)$.

Since $D > 0$, the conditions $P \ne 0$ and $Q \ne 0$ say that $U$ is nondegenerate. The quotient
$U_{2m}/P$ is an integer because $P \mid U_{2m}$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Lemma 6.1.

Stated but not proved: `MetaMathlibExt.lucasU_pseudoprime_candidates_jacobiSym` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-pseudoprime-candidates-jacobi-sy).

## Classification of degenerate Lucas sequences

Let $P, Q$ be integers, let
$\alpha, \beta \in \mathbb{C}$ satisfy $\alpha + \beta = P$ and $\alpha\beta = Q$ (so they are the
roots of $x^2 - Px + Q$), and let $D = P^2 - 4Q$. Let $(u_n)$ be the Lucas sequence of the first
kind with parameters $P, Q$, and let $(v_n)$ be the integer sequence with $v_0 = 2$, $v_1 = P$ and
$v_{n+2} = P v_{n+1} - Q v_n$ for all $n$. Suppose that $Q = 0$ or that $\alpha/\beta$ is a root
of unity. Then either (i) $Q = 0$, $D = P^2$, and $u_n = P^{n-1}$ and $v_n = P^n$ for every
$n \ge 1$; or there is a nonzero integer $M$ such that one of the following holds:
(ii) $\alpha/\beta = 1$, $P = 2M$, $Q = M^2$ and $D = 0$;
(iii) $\alpha/\beta = -1$, $P = 0$, $Q = M$ and $D = -4M$;
(iv) $\alpha/\beta$ is a primitive cube root of unity, $P = M$, $Q = M^2$ and $D = -3M^2$;
(v) $\alpha/\beta$ is a primitive fourth root of unity, $P = 2M$, $Q = 2M^2$ and $D = -4M^2$;
(vi) $\alpha/\beta$ is a primitive sixth root of unity, $P = 3M$, $Q = 3M^2$ and $D = -3M^2$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.lucas_degenerate_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-degenerate-cases).

## Rank of appearance in a Lucas sequence

Let $U = U(P, Q)$ be the Lucas sequence with
integer parameters $P$ and $Q \ne 0$. The rank of appearance $\rho(m)$ of a natural number $m$ in
$U$ is the least positive integer $r$ with $m \mid U_r$; when no positive $r$ has $m \mid U_r$,
$\rho(m) = 0$.

When $m \ge 1$ and $\gcd(m, Q) = 1$, such an $r$ always exists (the source defines $\rho(m)$ only
in this case); it can also exist when $\gcd(m, Q) \ne 1$. For $m = 0$ it need not exist even when
$\gcd(0, Q) = |Q| = 1$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Section 2.

Formalized by `MetaMathlibExt.lucasRankOfAppearance`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-rank-of-appearance).

## Rank of appearance is at most any positive index of divisibility

Let $P, Q$ be integers
with $Q \neq 0$, let $U = U(P, Q)$ be the Lucas sequence, and write $\rho(m)$ for the rank of
appearance of a natural number $m$ in $U$. If $r > 0$ and $m \mid U_r$, then $\rho(m) \le r$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Section 2 (definition of `ρ` as a least index).

Formalized by `MetaMathlibExt.lucasRankOfAppearance_le_of_dvd`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-rank-of-appearance-le-of-dvd).

## The rank of appearance in a Lucas sequence is attained

Let $U = U(P, Q)$ be a Lucas
sequence and $m$ a natural number. If $m \mid U_r$ for some positive integer $r$, then the rank of
appearance $\rho(m)$ of $m$ in $U$ is positive and $m \mid U_{\rho(m)}$.

Together with the bound $\rho(m) \le r$ for every positive $r$ with $m \mid U_r$, this makes
$\rho(m)$ the least such index.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Section 2 (definition of `ρ` as a least index).

Formalized by `MetaMathlibExt.lucasRankOfAppearance_spec`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-rank-of-appearance-spec).

## Rank of appearance of $1$

For all integers $P, Q$ with $Q \neq 0$, the rank of
appearance of $1$ in the Lucas sequence $U(P, Q)$ is $1$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Section 2 (definition of `ρ`).

Formalized by `MetaMathlibExt.lucasRankOfAppearance_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-rank-of-appearance-one).

## Index of the Lucas pseudoprime congruences

Let $P, Q$ be integers with $Q \neq 0$ and
$D = P^2 - 4Q$. For a natural number $N$, the index is $N - (D/N)$, where $(D/N)$ is the Jacobi
symbol, replaced by $0$ when this difference is negative. For $N > 1$ the difference is positive.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, congruences (3.1), (3.4).

Formalized by `MetaMathlibExt.lucasPseudoprimeIndex`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-pseudoprime-index).

## Lucas pseudoprimes

Let $P, Q$ be integers with $Q \neq 0$, let $U_n$ be the Lucas
sequence of $(P, Q)$ and let $D = P^2 - 4Q$. A natural number $N$ is a Lucas pseudoprime with
parameters $P, Q$ if $N$ is odd and composite, $\gcd(N, QD) = 1$ and $N$ divides
$U_{N - (D/N)}$, where $(D/N)$ is the Jacobi symbol.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.1.

Formalized by `MetaMathlibExt.IsLucasPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-pseudoprime).

## Lucas pseudoprimes of the second kind

Let $P, Q$ be integers with $Q \neq 0$, let $U_n$
be the Lucas sequence of $(P, Q)$ and let $D = P^2 - 4Q$. A natural number $N$ is a Lucas
pseudoprime of the second kind with parameters $P, Q$ if $N$ is odd and composite,
$\gcd(N, QD) = 1$ and $U_N \equiv (D/N) \pmod{N}$, where $(D/N)$ is the Jacobi symbol.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.2.

Formalized by `MetaMathlibExt.IsLucasPseudoprimeSecondKind`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-pseudoprime-second-kind).

## Dickson pseudoprimes

Let $P$ and $Q \ne 0$ be integers with discriminant
$D = P^2 - 4Q$, and let $(V_n)$ be the companion Lucas sequence $V(P, Q)$. A natural number $N$
is a Dickson pseudoprime with parameters $P$ and $Q$ if $N$ is odd, $N > 1$, $N$ is not prime,
$\gcd(N, QD) = 1$, and $V_N \equiv P \pmod N$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.3.

Formalized by `MetaMathlibExt.IsDicksonPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-dickson-pseudoprime).

## Dickson pseudoprimes of the second kind

Let $P$ and $Q \ne 0$ be integers with
discriminant $D = P^2 - 4Q$, and let $(V_n)$ be the companion Lucas sequence $V(P, Q)$. A
natural number $N$ is a Dickson pseudoprime of the second kind with parameters $P$ and $Q$ if
$N$ is odd, $N > 1$, $N$ is not prime, $\gcd(N, QD) = 1$, and
$V_{N - (D/N)} \equiv 2Q^{(1 - (D/N))/2} \pmod N$, where $(D/N)$ is the Jacobi symbol.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.4.

Formalized by `MetaMathlibExt.IsDicksonPseudoprimeSecondKind`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-dickson-pseudoprime-second-kind).

## Frobenius pseudoprime for Lucas parameters

Let $U$ and $V$ be the Lucas sequences with
integer parameters $P$ and $Q \neq 0$, and let $D = P^2 - 4Q$. A natural number $N$ is a
Frobenius pseudoprime with parameters $P, Q$ when $\gcd(N, PQD) = 1$ and $N$ is a Lucas
pseudoprime, a Lucas pseudoprime of the second kind, a Dickson pseudoprime and a Dickson
pseudoprime of the second kind with parameters $P, Q$. Equivalently, $\gcd(N, PQD) = 1$, $N$ is
odd and composite, and, writing $\varepsilon = (D/N)$ for the Jacobi symbol, $N$ satisfies the
congruences $U_{N-\varepsilon} \equiv 0$, $U_N \equiv \varepsilon$, $V_N \equiv P$ and
$V_{N-\varepsilon} \equiv 2Q^{(1-\varepsilon)/2}$ modulo $N$.

This is the notion of the source, not Grantham's Frobenius pseudoprime defined through quotient
rings of polynomials.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.5.

Formalized by `MetaMathlibExt.IsLucasFrobeniusPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-frobenius-pseudoprime).

## Euler pseudoprime

Let $a$ be an integer. A natural number $N$ is an Euler pseudoprime to
the base $a$ when $N$ is odd and composite, $\gcd(a, N) = 1$, and
$a^{(N-1)/2} \equiv (a/N) \pmod N$, where $(a/N)$ is the Jacobi symbol.

The source states the definition for positive odd $a$ and applies it to the base $Q$ (for
example $Q = -1$ in Remark 3.8); here $a$ is any integer.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.7.

Formalized by `MetaMathlibExt.IsEulerPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-euler-pseudoprime).

## Euler–Lucas pseudoprime

Let $U$ and $V$ be the Lucas sequences with integer parameters
$P$ and $Q \neq 0$, and let $D = P^2 - 4Q$. A natural number $N$ is an Euler–Lucas pseudoprime
with parameters $P, Q$ when $N$ is odd and composite, $\gcd(N, QD) = 1$, and, writing
$\varepsilon = (D/N)$ for the Jacobi symbol, $N \mid U_{(N-\varepsilon)/2}$ if the Jacobi symbol
$(Q/N)$ equals $1$, and $N \mid V_{(N-\varepsilon)/2}$ if $(Q/N) = -1$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.9.

Formalized by `MetaMathlibExt.IsEulerLucasPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-euler-lucas-pseudoprime).

## Strong Lucas pseudoprimes

Let $P, Q$ be integers with $Q \neq 0$, let $U_n$ and $V_n$ be
the Lucas sequences of $(P, Q)$ and let $D = P^2 - 4Q$. A natural number $N$ is a strong Lucas
pseudoprime with parameters $P, Q$ if $N$ is odd and composite, $\gcd(N, QD) = 1$, and, writing
$N - (D/N) = 2^s d$ with $d$ odd, where $(D/N)$ is the Jacobi symbol, either $N \mid U_d$ or
$N \mid V_{2^r d}$ for some $r$ with $0 \le r < s$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.10.

Formalized by `MetaMathlibExt.IsStrongLucasPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-strong-lucas-pseudoprime).

## Super pseudoprime

Let $P, Q$ be integers with $Q \neq 0$, let $D = P^2 - 4Q$, and let $S$
be a property of natural numbers. A natural number $N$ is a super pseudoprime of type $S$ with
parameters $(P, Q)$ when $N$ is odd, $N > 1$, $N$ is not prime, $\gcd(N, QD) = 1$, and every
divisor $d > 1$ of $N$ is prime or has property $S$.

Taking for $S$ the property of being a Lucas, strong Lucas or Frobenius pseudoprime with
parameters $(P, Q)$ gives the super Lucas, super strong Lucas and super Frobenius pseudoprimes.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.13.

Formalized by `MetaMathlibExt.IsSuperPseudoprime`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-super-pseudoprime).

## $9$ is a Lucas pseudoprime for $(P, Q) = (1, 5)$

The number $9$ is a Lucas pseudoprime
with parameters $P = 1$ and $Q = 5$.

Here the discriminant is $D = P^2 - 4Q = -19$, the Jacobi symbol $(D/9)$ is $1$, and $9$
divides $U_8 = -279$, where $U_n$ is the Lucas sequence of $(1, 5)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.1 (example).

Formalized by `MetaMathlibExt.isLucasPseudoprime_one_five_nine`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-pseudoprime-one-five-nine).

## $9$ is a strong Lucas pseudoprime for $(P, Q) = (1, 5)$

The number $9$ is a strong
Lucas pseudoprime with parameters $P = 1$ and $Q = 5$.

Here $D = P^2 - 4Q = -19$, the Jacobi symbol $(D/9)$ is $1$, $9 - (D/9) = 8 = 2^3 \cdot 1$, and
$9$ divides $V_2 = -9$, where $V_n$ is the companion Lucas sequence of $(1, 5)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.10 (example).

Formalized by `MetaMathlibExt.isStrongLucasPseudoprime_one_five_nine`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-strong-lucas-pseudoprime-one-five-nin).

## 9 is an Euler–Lucas pseudoprime for P = 1, Q = 5

For the Lucas sequences $U$ and $V$
with parameters $P = 1$ and $Q = 5$, the number $9$ is an Euler–Lucas pseudoprime.

Here $D = P^2 - 4Q = -19$, the Jacobi symbols $(D/9)$ and $(5/9)$ both equal $1$, and $U_4 = -9$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.9 (example).

Formalized by `MetaMathlibExt.isEulerLucasPseudoprime_one_five_nine`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-euler-lucas-pseudoprime-one-five-nine).

## 9 is a Frobenius pseudoprime for P = 4, Q = -1

For the Lucas sequences with parameters
$P = 4$ and $Q = -1$, so that $D = P^2 - 4Q = 20$, the number $9$ is a Frobenius pseudoprime.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.5 (example).

Formalized by `MetaMathlibExt.isLucasFrobeniusPseudoprime_four_neg_one_nine`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-frobenius-pseudoprime-four-neg).

## 561 is an Euler pseudoprime to the base 2

The composite number $561 = 3 \cdot 11 \cdot 17$
is an Euler pseudoprime to the base $2$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.7 (example).

Formalized by `MetaMathlibExt.isEulerPseudoprime_two_561`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-euler-pseudoprime-two-561).

## $9$ is a super Lucas pseudoprime for $(P, Q) = (1, 5)$

The number $9$ is a super Lucas
pseudoprime with parameters $P = 1$, $Q = 5$: its divisors greater than $1$ are $3$, a prime, and
$9$, a Lucas pseudoprime with these parameters.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Definition 3.13 (example).

Formalized by `MetaMathlibExt.isSuperPseudoprime_one_five_nine`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-super-pseudoprime-one-five-nine).

## Properties of the rank of appearance in a Lucas sequence

Let $U = U(P, Q)$ be the Lucas
sequence with integer parameters $P$ and $Q \ne 0$, let $D = P^2 - 4Q$, let $\rho(m)$ be the rank
of appearance of $m$ in $U$, and write $(a/n)$ for the Jacobi symbol. Let $r$ and $s$ range over
positive integers and $p$ over primes. Then:
(i) if $\gcd(r, Q) = 1$, then $r \mid U_s$ if and only if $\rho(r) \mid s$;
(ii) if $p$ is odd and $p \nmid Q$, then $p \mid U_{p - (D/p)}$;
(iii) if $p \mid D$ and $p \nmid Q$, then $\rho(p) = p$;
(iv) if $p \nmid 2QD$, then $p \mid U_{(p - (D/p))/2}$ if and only if $(Q/p) = 1$;
(v) if $p$ is odd, $p \nmid Q$, and $k \ge 0$ satisfies $\rho(p^k) = \rho(p)$ and
$\rho(p^{k+1}) \ne \rho(p)$, then $\rho(p^j) = p^{\max(j - k, 0)} \rho(p)$ for every $j \ge 1$;
(vi) if $\gcd(rs, Q) = 1$ and $r \mid s$, then $\rho(r) \mid \rho(s)$;
(vii) if $\gcd(P, Q) = 1$, then $\gcd(U_r, U_s) = |U_{\gcd(r, s)}|$;
(viii) if $\gcd(r, s) = 1$ and $\gcd(rs, Q) = 1$, then
$\rho(rs) = \operatorname{lcm}(\rho(r), \rho(s))$;
(ix) if $\gcd(P, Q) = 1$ and $p \mid Q$, then $p \nmid U_n$ for every $n \ge 1$;
(x) if $\gcd(P, Q) = 1$, $p$ is odd and $p \nmid Q$, then $p \equiv (D/p) \pmod{\rho(p)}$.

Part (v) fails for $p = 2$: for $(P, Q) = (1, -1)$ one has $\rho(2) = 3$, $\rho(4) = 6$ and
$\rho(8) = 6 \ne 12$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 2.4.

Stated but not proved: `MetaMathlibExt.lucasRankOfAppearance_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-rank-of-appearance-properties).

## Strong Lucas pseudoprimes are Euler–Lucas pseudoprimes

Let $P$ and $Q \ne 0$ be
integers. Every strong Lucas pseudoprime with parameters $P$ and $Q$ is an Euler–Lucas
pseudoprime with parameters $P$ and $Q$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 3.12.

Stated but not proved: `MetaMathlibExt.isEulerLucasPseudoprime_of_isStrongLucasPseudoprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-euler-lucas-pseudoprime-of-is-strong).

## Strong Lucas pseudoprimes via the $2$-adic valuation of ranks

Let $P, Q$ be integers
such that the Lucas pair $(P, Q)$ is nondegenerate, let $D = P^2 - 4Q$, and let $\rho(m)$ be the
rank of appearance of $m$ in the Lucas sequence $U(P, Q)$. Let $N$ be a Lucas pseudoprime with
parameters $P, Q$ such that $\gcd(N, PQD) = 1$. Then $\rho(p^k) = \rho(p)$ for every prime $p$
dividing $N$, where $p^k$ is the exact power of $p$ dividing $N$; and $N$ is a strong Lucas
pseudoprime with parameters $P, Q$ if and only if the $2$-adic valuations $\nu_2(\rho(p))$ are
equal for all primes $p$ dividing $N$.

The source prints $\rho(p_i^{k_i}) = p_i$, which is false: for $(P, Q) = (1, -1)$ and
$N = 323 = 17 \cdot 19$ one has $\rho(17) = 9$ and $\rho(19) = 18$. The statement uses
$\rho(p_i)$, as in Theorems 3.16 and 3.17.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 3.14.

Stated but not proved: `MetaMathlibExt.isStrongLucasPseudoprime_iff_padicValNat_two_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-strong-lucas-pseudoprime-iff-padic-va).

## Lucas pseudoprimes of odd rank are strong

Let $P, Q$ be integers such that the Lucas
pair $(P, Q)$ is nondegenerate, and let $\rho(N)$ be the rank of appearance of $N$ in the Lucas
sequence $U(P, Q)$. If $N$ is a Lucas pseudoprime with parameters $P, Q$ and $\rho(N)$ is odd,
then $N$ is a strong Lucas pseudoprime with parameters $P, Q$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Corollary 3.15.

Stated but not proved: `MetaMathlibExt.isStrongLucasPseudoprime_of_odd_lucasRankOfAppearance` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-strong-lucas-pseudoprime-of-odd-lucas).

## Rank of appearance and super Lucas pseudoprimes

Let $P, Q$ be integers with $Q \neq 0$
such that the pair $(P, Q)$ is nondegenerate, let $D = P^2 - 4Q$, and write $\rho(m)$ for the rank
of appearance of $m$ in the Lucas sequence $U(P, Q)$. Let $N > 1$ be an odd number that is not
prime, with $\gcd(N, QD) = 1$, and for each prime $p \mid N$ let $k_p$ be the exponent of $p$ in
$N$ and let $m_p \ge k_p$ satisfy $\rho(p^{m_p}) = \rho(p)$ and $\rho(p^{m_p + 1}) \neq \rho(p)$.
Let $h$ be the least common multiple of the $\rho(p)$ over the primes $p \mid N$. Then
$\rho(N) = h$, and $N$ is a super Lucas pseudoprime with parameters $(P, Q)$ if and only if
$p \equiv (D/p) \pmod h$ for every prime $p \mid N$, where $(D/p)$ is the Jacobi symbol.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 3.16.

Stated but not proved: `MetaMathlibExt.lucasRankOfAppearance_eq_lcm_and_isSuperPseudoprime_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-rank-of-appearance-eq-lcm-and-is-s).

## Super strong Lucas pseudoprimes from equal ranks of appearance

Let $P, Q$ be integers
with $Q \neq 0$ such that the pair $(P, Q)$ is nondegenerate, let $D = P^2 - 4Q$, and write
$\rho(m)$ for the rank of appearance of $m$ in the Lucas sequence $U(P, Q)$. Let $N > 1$ be an
odd number that is not prime, with $\gcd(N, PQD) = 1$, such that for every prime $p \mid N$,
with $p^{k}$ the exact power of $p$ dividing $N$, $\rho(p^{k}) = \rho(p)$, and $\rho(p) = \rho(q)$
for all primes $p, q \mid N$. Then $N$ is a super strong Lucas pseudoprime with parameters
$(P, Q)$, and if $Q = \pm 1$ it is also a super Frobenius pseudoprime with parameters $(P, Q)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 3.17.

Stated but not proved: `MetaMathlibExt.isSuperPseudoprime_of_lucasRankOfAppearance_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-super-pseudoprime-of-lucas-rank-of-ap).

## From Euler–Lucas to Frobenius pseudoprimes

Let $P$ and $Q \neq 0$ be integers forming a
nondegenerate Lucas pair, and let $D = P^2 - 4Q$. If $N$ is an Euler–Lucas pseudoprime with
parameters $P, Q$ and an Euler pseudoprime to the base $Q$, and $\gcd(N, PQD) = 1$, then $N$ is a
Frobenius pseudoprime with parameters $P, Q$.

The base $Q$ is any nonzero integer; the source's Definition 3.7 is stated for positive odd bases.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 3.18.

Stated but not proved: `MetaMathlibExt.isLucasFrobeniusPseudoprime_of_isEulerLucasPseudoprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 593](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L593). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-frobenius-pseudoprime-of-is-eul).

## From strong Lucas to Frobenius pseudoprimes when Q = ±1

Let $P$ and $Q$ be integers
forming a nondegenerate Lucas pair with $Q = 1$ or $Q = -1$, and let $D = P^2 - 4Q$. If $N$ is a
strong Lucas pseudoprime with parameters $P, Q$ and $\gcd(N, PD) = 1$, then $N$ is a Frobenius
pseudoprime with parameters $P, Q$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 3.19.

Stated but not proved: `MetaMathlibExt.isLucasFrobeniusPseudoprime_of_isStrongLucasPseudoprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-frobenius-pseudoprime-of-is-str).

## Carmichael's primitive divisor theorem

Let $P$ and $Q$ be coprime integers forming a
nondegenerate Lucas pair with discriminant $D = P^2 - 4Q > 0$, and let $(U_n)$ be the Lucas
sequence $U(P, Q)$. Then for every $n \ge 1$ with $n \notin \{1, 2, 6, 12\}$, the term $U_n$ has
a primitive prime divisor: a prime $p$ that divides $U_n$ but divides no $U_s$ with $1 \le s < n$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.exists_isPrimitivePrimeDivisor_lucasU_of_discr_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#exists-is-primitive-prime-divisor-lucas).

## Bilu–Hanrot–Voutier theorem for Lucas sequences

Let $P$ and $Q$ be coprime integers
forming a nondegenerate Lucas pair, and let $(U_n)$ be the Lucas sequence $U(P, Q)$. Then for
every $n \ge 1$ with $n \notin \{1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 18, 30\}$, the term $U_n$
has a primitive prime divisor: a prime $p$ that divides $U_n$ but divides no $U_s$ with
$1 \le s < n$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 4.3.

Stated but not proved: `MetaMathlibExt.exists_isPrimitivePrimeDivisor_lucasU` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 625](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L625). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#exists-is-primitive-prime-divisor-lucas-2).

## Rotkiewicz: strong Lucas and Frobenius pseudoprimes with two prime factors

Let $P$ and
$Q$ be integers forming a nondegenerate Lucas pair with $Q = \pm 1$. Then infinitely many
products $N = p_1 p_2$ of two distinct odd primes $p_1$ and $p_2$ are both strong Lucas
pseudoprimes and Frobenius pseudoprimes with parameters $P$ and $Q$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 4.5.

Stated but not proved: `MetaMathlibExt.infinite_strong_frobenius_pseudoprimes_two_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#infinite-strong-frobenius-pseudoprimes-t).

## Rotkiewicz: Frobenius pseudoprimes in arithmetic progressions

Let $P$ and $Q$ be
integers forming a nondegenerate Lucas pair with $Q = \pm 1$, and let $a$ and $b$ be coprime
positive integers. Then infinitely many natural numbers $N \equiv b \pmod a$ are Frobenius
pseudoprimes with parameters $P$ and $Q$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 4.6.

Stated but not proved: `MetaMathlibExt.infinite_frobenius_pseudoprimes_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#infinite-frobenius-pseudoprimes-mod-eq).

## Lucas-type pseudoprime properties are unchanged by $P \mapsto -P$

Let $P$ and $Q$ be
integers such that the Lucas pair $(P, Q)$ is nondegenerate, let $D = P^2 - 4Q$, and let $N > 1$
be an odd natural number with $\gcd(N, QD) = 1$. Then $N$ is a Lucas pseudoprime for $(P, Q)$ if
and only if it is one for $(-P, Q)$, and the same holds for Lucas pseudoprimes of the second
kind, Dickson pseudoprimes, Dickson pseudoprimes of the second kind, and Frobenius pseudoprimes.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 4.7.

Stated but not proved: `MetaMathlibExt.pseudoprime_iff_neg_p` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#pseudoprime-iff-neg-p).

## Composite terms $|U_p|$ are super strong Lucas pseudoprimes

Let $P, Q$ be integers with
$\gcd(P, Q) = 1$ such that the Lucas pair $(P, Q)$ is nondegenerate, let $U_n$ be the Lucas
sequence of $(P, Q)$ and let $D = P^2 - 4Q$. Let $p \ge 5$ be a prime with $\gcd(p, PQD) = 1$
such that $|U_p|$ is composite. Then $|U_p|$ is a super strong Lucas pseudoprime with parameters
$P, Q$, and if $Q = \pm 1$ it is also a super Frobenius pseudoprime with parameters $P, Q$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 5.1, first two sentences.

Stated but not proved: `MetaMathlibExt.isSuperPseudoprime_natAbs_lucasU_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-super-pseudoprime-nat-abs-lucas-u-pri).

## Compositeness criteria for $|U_p|$

Let $P$ and $Q$ be coprime integers such that the
Lucas pair $(P, Q)$ is nondegenerate, let $U_n$ be the Lucas sequence $U(P, Q)$, let
$D = P^2 - 4Q$, and write $\left(\frac{a}{b}\right)$ for the Jacobi symbol. Call a prime $p$
admissible if $p \ge 5$ and $\gcd(p, PQD) = 1$. Then the following hold.

First, if $Q$ is the square of an integer and $D > 0$, then for every admissible prime $p$, $|U_p|$
is greater than $1$, is not prime, and has at least two distinct prime factors.

Second, let $p$ be an admissible prime such that $2p + 1$ is prime and
$\left(\frac{D}{2p+1}\right) = \left(\frac{Q}{2p+1}\right) = 1$. Then $2p + 1 \mid |U_p|$ if
$|U_p| > 2p + 1$; and if $D > 0$, then $|U_p| > 2p + 1$ unless $p = 5$, $|P| = 1$ and $Q = -2$.

Third, if $D < 0$, there is a constant $C$ such that $|U_p| > 2p + 1$ for every prime $p \ge C$.

Fourth, let $p$ be an admissible prime such that $2p - 1$ is prime,
$\left(\frac{D}{2p-1}\right) = -1$ and $\left(\frac{Q}{2p-1}\right) = 1$. Then $2p - 1 \mid |U_p|$
if $|U_p| > 2p - 1$; and if $D > 0$, then $|U_p| > 2p - 1$ unless $p = 7$, $|P| = 1$ and $Q = -1$.

The source states the bound for $D < 0$ in both parts (ii) and (iii) of Theorem 5.1, as printed
with $2p + 1$ in each; the third claim above is that bound.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 5.1 (i)–(iii).

Stated but not proved: `MetaMathlibExt.natAbs_lucasU_prime_composite_criteria` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#nat-abs-lucas-u-prime-composite-criteria).

## Super strong Lucas pseudoprimes from composed Lucas pairs

Let $P_1, Q_1$ be integers
with $\gcd(P_1, Q_1) = 1$ such that the Lucas pair $(P_1, Q_1)$ is nondegenerate, with Lucas
sequences $U_n(P_1, Q_1)$, $V_n(P_1, Q_1)$ and discriminant $D_1 = P_1^2 - 4Q_1$. Let $k \ge 2$
with $\gcd(D_1, k) = 1$, let $\varepsilon = \pm 1$, and let $P = \varepsilon V_k(P_1, Q_1)$,
$Q = Q_1^k$ and $D = P^2 - 4Q$. Let $p$ be a prime with $p \nmid k D_1$ and $\gcd(p, PQD) = 1$,
such that $p \ge 5$ if $D > 0$, $p \ge 11$ if $D < 0$, and $p \ne 13$ if $|P_1| = 1$ and
$Q_1 = 2$. Then $\gcd(P, Q) = 1$, the Lucas pair $(P, Q)$ is nondegenerate,
$D = D_1 U_k(P_1, Q_1)^2$, and $|U_p(P, Q)|$ is a super strong Lucas pseudoprime with parameters
$P, Q$; if moreover $Q_1 = \pm 1$, it is also a super Frobenius pseudoprime with parameters
$P, Q$. Finally, $2^{\omega(k)} \le \tau(k) \le \tau(|U_p(P, Q)|)$, where $\omega(k)$ is the
number of distinct prime factors of $k$ and $\tau(n)$ is the number of positive divisors of $n$.

The source writes the exclusion as "$p \ne 13$ if $P = \pm 1$, $Q = 2$", which is vacuous for
$Q = Q_1^k$ with $k \ge 2$; read for $(P, Q)$ it fails: $(P_1, Q_1, k) = (1, 2, 2)$ gives
$(P, Q) = (\mp 3, 4)$ and $|U_{13}(3, 4)| = 181$, a prime. Without $\gcd(p, PQD) = 1$, the
standing hypothesis of Theorem 5.1, it fails as well: $(P_1, Q_1, k, p) = (-3, -1, 3, 5)$ gives
$D = 1300$ and $5 \mid U_5(\pm 36, -1)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 5.1 (iv).

Stated but not proved: `MetaMathlibExt.isSuperPseudoprime_natAbs_lucasU_prime_of_lucasV` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-super-pseudoprime-nat-abs-lucas-u-pri-2).

## Super Lucas pseudoprimes of the form $|U_{2p}/P|$

Let $P, Q$ be integers with $Q \neq 0$
such that the pair $(P, Q)$ is nondegenerate and $\gcd(P, Q) = 1$, let $D = P^2 - 4Q$, and let
$U = U(P, Q)$ be the Lucas sequence. Let $p \ge 5$ be a prime with $\gcd(p, PQD) = 1$ such that
$(p, |P|, Q)$ is none of $(5, 1, 2)$, $(5, 1, 3)$, $(5, 2, 3)$, $(5, 12, 55)$ and $(13, 1, 2)$.
Then $|U_{2p}/P|$, with $U_{2p}/P$ the integer quotient, is a super Lucas pseudoprime with
parameters $(P, Q)$. Moreover, for $\varepsilon = \pm 1$ the Lucas sequences of the excluded
parameters satisfy $|U_{10}(\varepsilon, 2)| = 11$, $|U_{10}(\varepsilon, 3)| = 31$,
$|U_{10}(2\varepsilon, 3)/(2\varepsilon)| = 11$,
$|U_{10}(12\varepsilon, 55)/(12\varepsilon)| = 3739$ and $|U_{26}(\varepsilon, 2)| = 181$, and
$11$, $31$, $3739$ and $181$ are prime.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 5.3.

Stated but not proved: `MetaMathlibExt.isSuperPseudoprime_natAbs_lucasU_two_mul_prime_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-super-pseudoprime-nat-abs-lucas-u-two).

## Strong Lucas pseudoprimes among the terms $|U_m|$

Let $P, Q$ be integers with
$\gcd(P, Q) = 1$ such that the Lucas pair $(P, Q)$ is nondegenerate and $D = P^2 - 4Q > 0$, and
let $U_n$ be the Lucas sequence of $(P, Q)$. Suppose that $P$ is odd, or $P \equiv 0 \pmod 4$ and
$Q \equiv -1 \pmod 4$, or $P \equiv 2 \pmod 4$ and $Q \equiv -1 \pmod 8$. Let $m \ge 5$ be an
odd prime or a Lucas pseudoprime of the second kind with parameters $P, Q$, such that
$\gcd(m, PQD) = 1$, such that $3 \nmid m$ if $P$ and $Q$ are both odd, and such that $|U_m|$ is
not prime if $m$ is prime. Then $|U_m|$ is a strong Lucas pseudoprime with parameters $P, Q$.

The source states the result for $N_1 = U_m$, which is positive by its Lemma 6.1.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.2.

Stated but not proved: `MetaMathlibExt.isStrongLucasPseudoprime_natAbs_lucasU` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 778](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L778). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-strong-lucas-pseudoprime-nat-abs-luca).

## $|U_m|$ is a strong Lucas and Frobenius pseudoprime when $Q = \pm 1$

Let $P$ and $Q$ be
integers with $Q = 1$ or $Q = -1$ such that the Lucas pair $(P, Q)$ is nondegenerate, let $U_n$
be the Lucas sequence $U(P, Q)$, and let $D = P^2 - 4Q$. Let $m \ge 5$ be either an odd prime or
a Lucas pseudoprime of the second kind for $(P, Q)$, with $\gcd(m, PD) = 1$ and with $3 \nmid m$
if $P$ is odd. Then $D > 0$, $\gcd(U_m, PD) = 1$, and $3 \nmid U_m$ if $P$ is odd. Suppose
moreover that $|U_m|$ is not prime whenever $m$ is prime and $Q = -1$, and that $P$ is odd, or
$P$ is even and $Q = -1$. Then $|U_m|$ is both a strong Lucas pseudoprime and a Frobenius
pseudoprime for $(P, Q)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.3.

Stated but not proved: `MetaMathlibExt.lucasU_strong_frobenius_of_q_eq_one_or_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 796](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L796). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-strong-frobenius-of-q-eq-one-or).

## Lucas pseudoprimes from even-index Lucas terms divided by P

Let $U$ be the Lucas sequence
with parameters $P$ and $Q$ forming a nondegenerate Lucas pair, with $\gcd(P, Q) = 1$ and
$D = P^2 - 4Q > 0$. Let $m \ge 5$ be either an odd prime or a Frobenius pseudoprime with
parameters $P, Q$, such that $\gcd(m, PQD) = 1$, and $3 \nmid m$ if $P$ and $Q$ are both odd.
Suppose that $P$ is odd, or $P \equiv 0 \pmod 4$ and $Q \equiv -1 \pmod 4$, or
$P \equiv 2 \pmod 4$ and $Q \equiv -1 \pmod 8$. Then $N_2 = |U_{2m}/P|$ is a Lucas pseudoprime
with parameters $P, Q$.

Here $U_{2m}/P$ is the integer quotient, exact because $P \mid U_{2m}$; by Lemma 6.1 it is
positive, so $N_2 = U_{2m}/P$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.5.

Stated but not proved: `MetaMathlibExt.isLucasPseudoprime_natAbs_lucasU_two_mul_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-pseudoprime-nat-abs-lucas-u-two).

## $|U_{2m}/P|$ is a Lucas pseudoprime when $Q = \pm 1$

Let $P$ and $Q$ be integers with
$Q = 1$ or $Q = -1$ such that the Lucas pair $(P, Q)$ is nondegenerate, let $U_n$ be the Lucas
sequence $U(P, Q)$, and let $D = P^2 - 4Q$. Let $m \ge 5$ be either an odd prime or a Lucas
pseudoprime for $(P, Q)$, with $\gcd(m, PD) = 1$ and with $3 \nmid m$ if $P$ is odd, and put
$N_2 = U_{2m}/P$. Then $D > 0$, $\gcd(N_2, PD) = 1$, and $3 \nmid N_2$ if $P$ is odd; and if $P$
is odd, or $P$ is even and $Q = -1$, then $|N_2|$ is a Lucas pseudoprime for $(P, Q)$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.6.

Stated but not proved: `MetaMathlibExt.lucasU_two_mul_div_isLucasPseudoprime_of_q_eq_one_or_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 832](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L832). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-two-mul-div-is-lucas-pseudoprime).

## Frobenius criterion for Lucas pseudoprimes that are not strong

Let $U$ be the Lucas
sequence with parameters $P$ and $Q$, where $Q = 1$ or $Q = -1$, and let $D = P^2 - 4Q$. Let $N$
be a Lucas pseudoprime with parameters $P, Q$ such that $\gcd(N, D) = 1$ and $N$ is not a strong
Lucas pseudoprime, let $\rho(N)$ be the rank of appearance of $N$ in $U$, and let $k$ be a natural
number with $2^k \mid \rho(N)$ and $2^{k+1} \nmid \rho(N)$. Write $(D/N)$ for the Jacobi symbol.
If $Q = -1$, then $N$ is a Frobenius pseudoprime with parameters $P, Q$ if and only if
$N \equiv (D/N) \pmod{2^{k+1}}$ and $(D/N) = 1$. If $Q = 1$, then $N$ is a Frobenius pseudoprime
with parameters $P, Q$ if and only if $N \equiv (D/N) \pmod{2^{k+1}}$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.9.

Stated but not proved: `MetaMathlibExt.isLucasFrobeniusPseudoprime_iff_of_not_isStrongLucasPseudoprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 849](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L849). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#is-lucas-frobenius-pseudoprime-iff-of-no).

## When $|U_{2m}/P|$ is a Frobenius pseudoprime, for $Q = \pm 1$

Let $P$ and $Q$ be integers
with $Q = 1$ or $Q = -1$ such that the Lucas pair $(P, Q)$ is nondegenerate, let $U_n$ be the
Lucas sequence $U(P, Q)$, and let $D = P^2 - 4Q$. Let $m \ge 5$ be either an odd prime or a Lucas
pseudoprime for $(P, Q)$, with $\gcd(m, PD) = 1$ and with $3 \nmid m$ if $P$ is odd, and write
$\left(\frac{D}{m}\right)$ for the Jacobi symbol. Suppose that $P$ is odd, or $P$ is even and
$Q = -1$, and put $N_2 = |U_{2m}/P|$. Then $D > 0$ and $N_2$ is a Lucas pseudoprime for $(P, Q)$.
Moreover, $N_2$ is a Frobenius pseudoprime for $(P, Q)$ if and only if:
$m \equiv \left(\frac{D}{m}\right) \pmod 6$ and $\left(\frac{D}{m}\right) = 1$, when $P$ is odd
and $Q = -1$; $m \equiv \left(\frac{D}{m}\right) \pmod 6$, when $P$ is odd and $Q = 1$; and
$m \equiv \left(\frac{D}{m}\right) \pmod 4$ and $\left(\frac{D}{m}\right) = 1$, when $P$ is even
and $Q = -1$.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.10.

Stated but not proved: `MetaMathlibExt.lucasU_two_mul_div_isLucasFrobeniusPseudoprime_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 867](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L867). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#lucas-u-two-mul-div-is-lucas-frobenius-p).

## Frobenius and non-Frobenius pseudoprimes of the form $U_{2m}/P$

Let $P$ and $Q$ be
integers forming a nondegenerate Lucas pair with $Q = \pm 1$, with $P$ odd if $Q = 1$, and let
$(U_n)$ be the Lucas sequence $U(P, Q)$. Call $m$ admissible if it is an odd prime or a Lucas
pseudoprime with parameters $P$ and $Q$. Then infinitely many natural numbers $N = |U_{2m}/P|$
with $m$ admissible are both Lucas pseudoprimes and Frobenius pseudoprimes with parameters $P$
and $Q$, and infinitely many such $N$ are Lucas pseudoprimes but not Frobenius pseudoprimes.

Nondegeneracy is assumed explicitly, and the statement fails without it: for $(P, Q) = (1, 1)$
the sequence $U$ runs $0, 1, 1, 0, -1, -1, \dots$, so $U_{2m}/P \in \{0, \pm 1\}$ is never a
pseudoprime.

## Sources

- Lawrence Somer and Michal Křížek, *On Lucas and Frobenius Pseudoprimes*, INTEGERS 25 (2025), Article A107, Theorem 6.11.

Stated but not proved: `MetaMathlibExt.infinite_lucasU_two_mul_div_frobenius_and_not` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean, line 894](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/LucasSequenceDivisibilityWanted.lean#L894). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html#infinite-lucas-u-two-mul-div-frobenius-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisibility properties of Lucas sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/divisibility-properties-of-lucas-sequences)
