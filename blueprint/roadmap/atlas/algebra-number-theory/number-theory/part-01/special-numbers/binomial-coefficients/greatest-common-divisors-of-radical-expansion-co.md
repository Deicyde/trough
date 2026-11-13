---
declaration: section
origin: cited
lean: MetaMathlibExt.existsUnique_radical_expansion_coeffs, MetaMathlibExt.gcd_radical_expansion_coeffs_eq_one, MetaMathlibExt.gcd_pow_add_neg_one_pow_mul_eq_one, MetaMathlibExt.prime_dvd_choose_pow_mul_pow_mul, MetaMathlibExt.choose_pow_mul_modEq, MetaMathlibExt.gcd_sqrt_expansion_coeffs, MetaMathlibExt.gcd_prime_root_expansion_coeffs, MetaMathlibExt.gcd_radical_expansion_coeffs_dvd_succ
statement: formalized
---

# Greatest common divisors of radical-expansion coefficients

12 results, 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html).

## Unique integer coordinates of powers of $u + v^{1/N}$

Let $N$ be a natural number with
at least two distinct prime divisors, let $u, v$ be coprime positive integers such that
$x^N - v$ is irreducible over $\mathbb{Q}$, and let $\theta = v^{1/N}$ be the positive real
$N$-th root of $v$. Then for every natural number $n$ there is exactly one tuple of integers
$(a_0, \dots, a_{N-1})$ with $(u + \theta)^n = \sum_{i=0}^{N-1} a_i \theta^i$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Lemma 3 (`jis-2025-25.2.2-lem-3`).

Stated but not proved: `MetaMathlibExt.existsUnique_radical_expansion_coeffs` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#exists-unique-radical-expansion-coeffs).

## Coprime coefficients of $(u + v^{1/N})^n$ when $N$ has two distinct prime factors

Let
$N$ be a natural number with at least two distinct prime divisors, let $u, v$ be coprime positive
integers such that $x^N - v$ is irreducible over $\mathbb{Q}$, let $\theta = v^{1/N}$ be the
positive real $N$-th root of $v$, and let $a_{n,i}$ (for natural $n$ and $0 \le i \le N - 1$) be
integers with $(u + \theta)^n = \sum_{i=0}^{N-1} a_{n,i} \theta^i$ for every $n \ge 1$. Then for
every $n \ge 1$ the greatest common divisor of $a_{n,0}, \dots, a_{n,N-1}$ is $1$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Theorem 16 (`jis-2025-25.2.2-thm-16`) and its unnumbered restatement in the introduction (`jis-2025-25.2.2-thm-unnumbered-1`).

Stated but not proved: `MetaMathlibExt.gcd_radical_expansion_coeffs_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#gcd-radical-expansion-coeffs-eq-one).

## $u^N + (-1)^{N+1} v$ is coprime to $u$ and to $v$

Let $u, v$ be coprime positive integers
and let $N \ge 1$. Then $\gcd(u^N + (-1)^{N+1} v, u) = 1$ and $\gcd(u^N + (-1)^{N+1} v, v) = 1$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Lemma 5 (`jis-2025-25.2.2-lem-5`).

Stated but not proved: `MetaMathlibExt.gcd_pow_add_neg_one_pow_mul_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#gcd-pow-add-neg-one-pow-mul-eq-one).

## $p$ divides $\binom{p^r a}{p^s b}$ when $r > s$

Let $p$ be a prime, let $r > s$ be
natural numbers, and let $a, b$ be natural numbers not divisible by $p$. Then
$p \mid \binom{p^r a}{p^s b}$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Corollary 14 (`jis-2025-25.2.2-cor-14`).

Stated but not proved: `MetaMathlibExt.prime_dvd_choose_pow_mul_pow_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#prime-dvd-choose-pow-mul-pow-mul).

## Binomial coefficients $\binom{p^r a}{p^r b}$ modulo $p$

Let $p$ be a prime, let $r \ge 1$,
and let $a, b$ be natural numbers not divisible by $p$. Then
$\binom{p^r a}{p^r b} \equiv \binom{a}{b} \pmod{p}$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Corollary 15 (`jis-2025-25.2.2-cor-15`).

Stated but not proved: `MetaMathlibExt.choose_pow_mul_modEq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#choose-pow-mul-mod-eq).

## Gcd of the coefficients of $(u + \sqrt{v})^n$

Let $u, v$ be coprime positive integers
with $\sqrt{v}$ irrational, let $a_n, b_n$ (for natural $n$) be integers with
$(u + \sqrt{v})^n = a_n + b_n \sqrt{v}$ for every $n \ge 1$, and let $D_n \ge 0$ be the greatest
common divisor of $a_n$ and $b_n$. Then for every $n \ge 1$:
(a) if $u^2 - v$ is odd, then $D_n = 1$;
(b) if $u^2 - v \equiv 2 \pmod 4$, then $D_{2n-1} = 2^{n-1}$ and $D_{2n} = 2^n$;
(c) if $u^2 - v \equiv 4 \pmod 8$, then $D_{3n-2} = 2^{3n-3}$, $D_{3n-1} = 2^{3n-2}$ and
$D_{3n} = 2^{3n}$;
(d) if $u^2 - v \equiv 0 \pmod 8$, then $D_n = 2^{n-1}$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Theorem 17 (`jis-2025-25.2.2-thm-17`).

Stated but not proved: `MetaMathlibExt.gcd_sqrt_expansion_coeffs` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#gcd-sqrt-expansion-coeffs).

## Gcd of the coefficients of $(u + v^{1/p})^n$ for an odd prime $p$

Let $p$ be an odd
prime, let $u, v$ be coprime positive integers such that $\theta = v^{1/p}$, the positive real
$p$-th root of $v$, is irrational, and let $a_{n,i}$ (for natural $n$ and $0 \le i \le p - 1$) be
integers with $(u + \theta)^n = \sum_{i=0}^{p-1} a_{n,i} \theta^i$ for every $n \ge 1$. Write
$D_n$ for the nonnegative greatest common divisor of $a_{n,0}, \dots, a_{n,p-1}$. Then:
(a) if $p \nmid u^p + v$, then $D_n = 1$ for every $n \ge 1$;
(b) if $u^p + v = mp$ for a natural number $m$ with $p \nmid m$, then $D_{np+i} = p^n$ for all
natural numbers $n, i$ with $i \le p - 1$ and $np + i \ge 1$;
(c) if $p^2 \mid u^p + v$, then $D_{n(p-1)+i} = p^n$ for all natural numbers $n, i$ with
$1 \le i \le p - 1$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Theorem 18 (`jis-2025-25.2.2-thm-18`).

Stated but not proved: `MetaMathlibExt.gcd_prime_root_expansion_coeffs` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#gcd-prime-root-expansion-coeffs).

## The coefficient gcd of $(u + v^{1/N})^n$ divides that of $(u + v^{1/N})^{n+1}$

Let
$N, u, v$ be natural numbers such that $x^N - v$ is irreducible over $\mathbb{Q}$, let
$\theta = v^{1/N}$ be the nonnegative real $N$-th root of $v$, and let $a_{n,i}$ (for natural $n$
and $0 \le i \le N - 1$) be integers with $(u + \theta)^n = \sum_{i=0}^{N-1} a_{n,i} \theta^i$
for every $n \ge 1$. Write $D_n$ for the nonnegative greatest common divisor of
$a_{n,0}, \dots, a_{n,N-1}$. Then $D_n \mid D_{n+1}$ for every $n \ge 1$.

This holds without the paper's standing assumptions $N \ge 4$ and $\gcd(u, v) = 1$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Lemma 4 (`jis-2025-25.2.2-lem-4`).

Stated but not proved: `MetaMathlibExt.gcd_radical_expansion_coeffs_dvd_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#gcd-radical-expansion-coeffs-dvd-succ).

## Common prime factors of $u^N + (-1)^{N+1} v$ and the coefficient gcd divide $N$

Let
$N \ge 2$, let $u, v$ be coprime natural numbers such that $x^N - v$ is irreducible over
$\mathbb{Q}$, let $\theta = v^{1/N}$ be the nonnegative real $N$-th root of $v$, and let $a_{n,i}$
(for natural $n$ and $0 \le i \le N - 1$) be integers with
$(u + \theta)^n = \sum_{i=0}^{N-1} a_{n,i} \theta^i$ for every $n \ge 1$. Write $D_n$ for the
nonnegative greatest common divisor of $a_{n,0}, \dots, a_{n,N-1}$. Then for every $n \ge 1$,
every prime $p$ dividing $\gcd(u^N + (-1)^{N+1} v, D_n)$ divides $N$.

The paper assumes $N \ge 4$; the cases $N = 2, 3$ also hold, while $N = 1$ fails, since then
$D_n = (u + v)^n$.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Lemma 6 (`jis-2025-25.2.2-lem-6`).

Stated but not proved: `MetaMathlibExt.prime_dvd_gcd_pow_add_radical_coeffs` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#prime-dvd-gcd-pow-add-radical-coeffs).

## Primes dividing the coefficient gcd of $(u + v^{1/N})^n$ divide the norm

Let $u, v, N$
be natural numbers such that $x^N - v$ is irreducible over $\mathbb{Q}$. Write $\theta = v^{1/N}$
for the nonnegative real $N$-th root of $v$, and let $a_{n,i}$ be integers ($n \ge 1$,
$0 \le i < N$) with $(u + \theta)^n = \sum_{i=0}^{N-1} a_{n,i} \theta^i$ for every $n \ge 1$. If
$n \ge 1$ and $p$ is a prime dividing $D_n = \gcd(a_{n,0}, \dots, a_{n,N-1})$, then $p$ divides
$u^N + (-1)^{N+1} v$, the norm of $u + \theta$.

The paper's section assumes $N \ge 4$ and $u, v$ coprime; neither is needed here.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Lemma 7 (`jis-2025-25.2.2-lem-7`).

Stated but not proved: `MetaMathlibExt.prime_dvd_pow_add_of_dvd_radical_coeffs_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#prime-dvd-pow-add-of-dvd-radical-coeffs).

## Primes dividing the coefficient gcd of $(u + v^{1/N})^n$ divide $N$

Let $N \ge 2$ and
let $u, v$ be coprime natural numbers such that $x^N - v$ is irreducible over $\mathbb{Q}$. Write
$\theta = v^{1/N}$ for the nonnegative real $N$-th root of $v$, and let $a_{n,i}$ be integers
($n \ge 1$, $0 \le i < N$) with $(u + \theta)^n = \sum_{i=0}^{N-1} a_{n,i} \theta^i$ for every
$n \ge 1$. If $n \ge 1$ and $p$ is a prime dividing $D_n = \gcd(a_{n,0}, \dots, a_{n,N-1})$,
then $p$ divides $N$.

The paper's section assumes $N \ge 4$; the cases $N = 2, 3$ also hold, while $N = 1$ fails
(there $D_n = (u + v)^n$).

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Lemma 8 (`jis-2025-25.2.2-lem-8`).

Stated but not proved: `MetaMathlibExt.prime_dvd_of_dvd_radical_coeffs_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#prime-dvd-of-dvd-radical-coeffs-gcd).

## Coprime coefficients when $u^N + (-1)^{N+1} v$ is coprime to $N$

Let $N \ge 2$, let
$u, v$ be coprime natural numbers such that $x^N - v$ is irreducible over $\mathbb{Q}$, let
$\theta = v^{1/N}$ be the nonnegative real $N$-th root of $v$, and let $a_{n,i}$ (for natural $n$
and $0 \le i \le N - 1$) be integers with $(u + \theta)^n = \sum_{i=0}^{N-1} a_{n,i} \theta^i$
for every $n \ge 1$. If $u^N + (-1)^{N+1} v$ and $N$ are coprime integers, then for every
$n \ge 1$ the greatest common divisor of $a_{n,0}, \dots, a_{n,N-1}$ is $1$.

The paper assumes $N \ge 4$; the cases $N = 2, 3$ also hold, while $N = 1$ fails.

## Sources

- John Ferdinands and Timothy Ferdinands, *Greatest Common Divisors and Lucas's Theorem*, Journal of Integer Sequences 28 (2025), Article 25.2.2, Corollary 9 (`jis-2025-25.2.2-cor-9`).

Stated but not proved: `MetaMathlibExt.gcd_radical_expansion_coeffs_eq_one_of_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdLucasTheoremWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdLucasTheoremWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html#gcd-radical-expansion-coeffs-eq-one-of-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Greatest common divisors of radical-expansion coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/greatest-common-divisors-of-radical-expansion-co)
