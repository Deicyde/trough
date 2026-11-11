---
declaration: section
origin: cited
lean: Nat.eq_zero_of_three_pow_succ_add_one_eq_sq, MathlibExt.NumberTheory.ExponentialDiophantineWanted.pow_add_pow_eq_sq, MathlibExt.NumberTheory.ExponentialDiophantineWanted.pow19_add_pow151_ne_sq, MathlibExt.NumberTheory.PowAddPowEqSqWanted.two_pow_add_one_eq_sq, MathlibExt.NumberTheory.PowAddPowEqSqWanted.pow_add_one_eq_sq, MathlibExt.NumberTheory.PowAddPowEqSqWanted.one_add_pow_eq_sq, MathlibExt.NumberTheory.PowAddPowEqSqWanted.even_of_pos_exp, MathlibExt.NumberTheory.PowAddPowEqSqWanted.opposite_parity
statement: formalized
---

# Squares as sums or differences of powers

28 results, 1 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html).

## Powers of three plus one that are perfect squares

For natural numbers $y$ and $z$, if
$3^{y+1} + 1 = z^2$, then $y = 0$.

## Sources

- M. Buosi, G. S. Ferreira, and A. L. P. Porto, arXiv:2308.10043v1, Lemma 2.1 (`main.tex`, lines 128–131). The paper uses natural numbers including zero.

Formalized by `Nat.eq_zero_of_three_pow_succ_add_one_eq_sq`, a theorem declared in [MathlibExt/NumberTheory/Diophantine/PowerSquare.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Diophantine/PowerSquare.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#eq-zero-of-three-pow-succ-add-one-eq-sq).

## Solutions of $p^x + (p + a)^y = z^2$ for odd primes $p$ and $p + a$

Let $p$ be a
prime with $p \ne 2$ and $p \ne 3$, and let $a$ be a natural number such that $p + a$ is
prime, $a \equiv 0 \pmod 4$ and $p$ divides $a + 1$. If natural numbers $x$, $y$ and $z$
satisfy $p^x + (p + a)^y = z^2$, then $x = 0$, $y = 1$ and $z^2 = p + a + 1$.

## Sources

- Shalini Choudhury and Naba Kanta Sarma, "On the Diophantine Equations `(p+a)^x + p^y = z^2` and `(p+a)^x - p^y = z^2` where `p` and `p+a` Are Odd Primes", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.ExponentialDiophantineWanted.pow_add_pow_eq_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExponentialDiophantineWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ExponentialDiophantineWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#pow-add-pow-eq-sq).

## $19^x + 151^y$ is never a perfect square

For all natural numbers $x$, $y$ and $z$,
$19^x + 151^y \ne z^2$.

## Sources

- Shalini Choudhury and Naba Kanta Sarma, "On the Diophantine Equations `(p+a)^x + p^y = z^2` and `(p+a)^x - p^y = z^2` where `p` and `p+a` Are Odd Primes", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.ExponentialDiophantineWanted.pow19_add_pow151_ne_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExponentialDiophantineWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ExponentialDiophantineWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#pow19-add-pow151-ne-sq).

## Solutions of $2^x + 1 = z^2$

For natural numbers $x$ and $z$, $2^x + 1 = z^2$ holds if
and only if $x = 3$ and $z = 3$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.two_pow_add_one_eq_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#two-pow-add-one-eq-sq).

## Solutions of $n^x + 1 = z^2$ for $n \ne 2$

Let $n \ge 1$ be a natural number with
$n \ne 2$. For natural numbers $x$ and $z$, $n^x + 1 = z^2$ holds if and only if $x = 1$ and
$z^2 = n + 1$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.pow_add_one_eq_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#pow-add-one-eq-sq).

## The case $x = 0$ of $n^x + (5p)^y = z^2$

Let $p$ be a prime with $p \ne 2$. For natural
numbers $y$ and $z$, $1 + (5p)^y = z^2$ holds if and only if $y = 1$ and $z^2 = 5p + 1$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.one_add_pow_eq_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#one-add-pow-eq-sq).

## Evenness of $x$ in $n^x + (5p)^y = z^2$ when $n \equiv 2, 3 \pmod 5$

Let $p$ be a prime
and $n$ a natural number with $n \equiv 2 \pmod 5$ or $n \equiv 3 \pmod 5$. If natural numbers
$x$, $y$, $z$ with $y > 0$ satisfy $n^x + (5p)^y = z^2$, then $x$ is even.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.even_of_pos_exp` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#even-of-pos-exp).

## Opposite parity of the exponents in $n^x + (5p)^y = z^2$ when $n \equiv p \equiv 3 \pmod 4$

Let $p$ be a prime and $n$ a natural number with $n \equiv 3 \pmod 4$ and $p \equiv 3 \pmod 4$.
If natural numbers $x$, $y$, $z$ satisfy $n^x + (5p)^y = z^2$, then $x$ and $y$ have opposite
parity.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.opposite_parity` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#opposite-parity).

## No solutions of $n^x + (5p)^y = z^2$ when $n \equiv p \equiv 1 \pmod 4$

Let $p$ be a
prime and $n$ a natural number with $n \equiv 1 \pmod 4$ and $p \equiv 1 \pmod 4$. Then there
are no natural numbers $x$, $y$, $z$ with $n^x + (5p)^y = z^2$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.no_solution_mod_four_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#no-solution-mod-four-one).

## Solutions of $2^x + (5p)^y = z^2$ for $p \equiv 3 \pmod 4$

Let $p$ be a prime with
$p \equiv 3 \pmod 4$. For natural numbers $x$, $y$, $z$, $2^x + (5p)^y = z^2$ holds if and
only if $(x, y, z) = (3, 0, 3)$, or $p = 3$ and $(x, y, z) = (6, 2, 17)$, or $x = 0$, $y = 1$
and $z^2 = 5p + 1$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.two_pow_solutions` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#two-pow-solutions).

## Solutions of $n^x + (5p)^y = z^2$ for $n \equiv 3, 27 \pmod{60}$ and $p \equiv 7 \pmod{12}$

Let $p$ be a prime with $p \equiv 7 \pmod{12}$, and let $n$ be a natural number with
$n \equiv 3 \pmod{60}$ or $n \equiv 27 \pmod{60}$ such that $\gcd(n, p) = 1$ and
$\gcd(n, 5p - 1) = 1$. For natural numbers $x$, $y$, $z$, $n^x + (5p)^y = z^2$ holds if and
only if either $x = 0$, $y = 1$ and $z^2 = 5p + 1$, or $x = 1$, $y = 0$ and $z^2 = n + 1$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.solutions_mod_sixty` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#solutions-mod-sixty).

## Solutions of $2^x + 15^y = z^2$

The natural numbers $x$, $y$, $z$ with
$2^x + 15^y = z^2$ are exactly $(x, y, z) = (3, 0, 3)$, $(0, 1, 4)$ and $(6, 2, 17)$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Corollary 3.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.two_pow_add_fifteen_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#two-pow-add-fifteen-pow).

## Solutions of $3^x + 35^y = z^2$

The natural numbers $x$, $y$, $z$ with
$3^x + 35^y = z^2$ are exactly $(x, y, z) = (1, 0, 2)$ and $(x, y, z) = (0, 1, 6)$.

## Sources

- Suton Tadee, "On the Diophantine Equation `n^x + (5p)^y = z^2`", Corollary 4.

Stated but not proved: `MathlibExt.NumberTheory.PowAddPowEqSqWanted.three_pow_add_thirtyfive_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowAddPowEqSqWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowAddPowEqSqWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#three-pow-add-thirtyfive-pow).

## Prime powers one less than a square

Let $p$ be a prime. Then non-negative integers $x$
and $y$ satisfy $p^x + 1 = y^2$ if and only if $(p, x, y) = (2, 3, 3)$ or $(p, x, y) = (3, 1, 2)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Lemma 2.

Stated but not proved: `MetaMathlibExt.prime_pow_add_one_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pow-add-one-eq-sq-iff).

## Squares of the form $1 + (2^k(2p - 1))^y$ for prime pairs

Let $p$ be an odd prime such
that $2p - 1$ is prime, and let $k \ge 1$ be an integer. Then non-negative integers $y$ and $z$
satisfy $1 + (2^k(2p - 1))^y = z^2$ if and only if $k = 4$, $p = 3$, $y = 1$ and $z = 9$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Lemma 4.

Stated but not proved: `MetaMathlibExt.one_add_two_pow_mul_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#one-add-two-pow-mul-pow-eq-sq-iff).

## Terai's conjecture when $c$ is prime and $b \equiv \pm 5 \pmod 8$

Let $a, b, c$ be
natural numbers with $a^2 + b^2 = c^2$, $\gcd(a, b, c) = 1$, $b \equiv \pm 5 \pmod 8$ (that is,
$b$ is $3$ or $5$ modulo $8$) and $c$ prime. Then for all positive integers $x, y, z$, the
equation $x^2 + b^y = c^z$ holds if and only if $(x, y, z) = (a, 2, 2)$.

This case of the conjecture is due to Yuan and Wang. Terai's conjecture (the paper's Conjecture 1)
also assumes $a$ even, which follows here since $b$ is odd.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Lemma 6 and Conjecture 1.

Stated but not proved: `MetaMathlibExt.terai_pythagorean_of_prime_of_mod_eight` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#terai-pythagorean-of-prime-of-mod-eight).

## Integer points on three Mordell curves

The integer solutions of $y^2 = x^3 - 2$ are
exactly $(x, y) = (3, 5)$ and $(3, -5)$, the integer solutions of $y^2 = x^3 - 18$ are exactly
$(x, y) = (3, 3)$ and $(3, -3)$, and $y^2 = x^3 - 162$ has no integer solutions.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Lemma 7 (quoted from the LMFDB).

Stated but not proved: `MetaMathlibExt.mordell_curves_two_eighteen_one_six_two_integer_points` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#mordell-curves-two-eighteen-one-six-two).

## Solutions of $3^x = y^2 + 2$

For natural numbers $x, y$, we have $3^x = y^2 + 2$ if and
only if $(x, y)$ is $(1, 1)$ or $(3, 5)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Lemma 8.

Stated but not proved: `MetaMathlibExt.three_pow_eq_sq_add_two_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#three-pow-eq-sq-add-two-iff).

## Solutions of $2x^2 + 1 = 3^y$

For natural numbers $x, y$, we have $2x^2 + 1 = 3^y$ if and
only if $(x, y)$ is $(0, 0)$, $(1, 1)$, $(2, 2)$ or $(11, 5)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Lemma 9.

Stated but not proved: `MetaMathlibExt.two_mul_sq_add_one_eq_three_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#two-mul-sq-add-one-eq-three-pow-iff).

## Squares of the form $p^x + (2p - 1)^y$ for prime pairs

Let $p$ be an odd prime such that
$2p - 1$ is prime. Then non-negative integers $x$, $y$ and $z$ satisfy $p^x + (2p - 1)^y = z^2$
if and only if $p = 3$ and $(x, y, z) = (1, 0, 2)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 1.

Stated but not proved: `MetaMathlibExt.prime_pair_pow_add_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-pow-add-pow-eq-sq-iff).

## No squares of the form $p^x + (2^{2k+1}(2p - 1))^y$ for prime pairs with $p \equiv 5, 7 \pmod 8$

**No squares of the form $p^x + (2^{2k+1}(2p - 1))^y$ for prime pairs with
$p \equiv 5, 7 \pmod 8$.** Let $p$ be a prime with $p \equiv 5 \pmod 8$ or $p \equiv 7 \pmod 8$
such that $2p - 1$ is prime. Then for all non-negative integers $k$, $x$, $y$ and $z$,
$p^x + (2^{2k+1}(2p - 1))^y \ne z^2$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 2.

Stated but not proved: `MetaMathlibExt.prime_pair_pow_add_two_pow_odd_mul_pow_ne_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-pow-add-two-pow-odd-mul-pow-n).

## Squares of the form $p^x + (2^{2k}(2p - 1))^y$ for prime pairs

Let $p$ be a prime with
$p \equiv 3 \pmod 4$ such that $2p - 1$ is prime, and let $k \ge 1$ be an integer. Then
non-negative integers $x$, $y$ and $z$ satisfy $p^x + (2^{2k}(2p - 1))^y = z^2$ if and only if
either $p = 3$ and $(x, y, z) = (1, 0, 2)$, or $p = 3$, $k = 2$ and $(x, y, z) = (0, 1, 9)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 3.

Stated but not proved: `MetaMathlibExt.prime_pair_pow_add_two_pow_even_mul_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-pow-add-two-pow-even-mul-pow).

## Squares of the form $(2p - 1)^x - p^y$ for prime pairs

Let $p$ be a prime with
$p \equiv 3 \pmod 4$ such that $2p - 1$ is prime. Then non-negative integers $x$, $y$ and $z$
satisfy $(2p - 1)^x - p^y = z^2$ if and only if $(x, y, z) = (0, 0, 0)$, or $p = 3$ and
$(x, y, z) = (2, 2, 4)$, or $p = 2t^2 + 1$ for some non-negative integer $t$ and
$(x, y, z) = (1, 0, 2t)$.

In the last family the two primes are $p = 2t^2 + 1$ and $2p - 1 = 4t^2 + 1$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 4.

Stated but not proved: `MetaMathlibExt.prime_pair_pow_sub_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-pow-sub-pow-eq-sq-iff).

## Squares of the form $(2^{2k}(2p - 1))^x - p^y$ for prime pairs

Let $p$ be a prime with
$p \equiv 3 \pmod 4$ such that $2p - 1$ is prime, and let $k \ge 1$ be an integer. Then
non-negative integers $x$, $y$ and $z$ satisfy $(2^{2k}(2p - 1))^x - p^y = z^2$ if and only if
$(x, y, z) = (0, 0, 0)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 6.

Stated but not proved: `MetaMathlibExt.prime_pair_two_pow_even_mul_pow_sub_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-two-pow-even-mul-pow-sub-pow).

## Squares of the form $(2^{2k+1}(2p - 1))^x - p^y$ for prime pairs

Let $p$ be a prime with
$p \equiv 5 \pmod 8$ such that $2p - 1$ is prime, and let $k$ be a non-negative integer. Then
non-negative integers $x$, $y$ and $z$ satisfy $(2^{2k+1}(2p - 1))^x - p^y = z^2$ if and only if
$(x, y, z) = (0, 0, 0)$, or $k = 0$, $x = 1$, $y = 0$ and $4p = z^2 + 3$.

In the last case the two primes are $p = (z^2 + 3)/4$ and $2p - 1 = (z^2 + 1)/2$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 7.

Stated but not proved: `MetaMathlibExt.prime_pair_two_pow_odd_mul_pow_sub_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-two-pow-odd-mul-pow-sub-pow-e).

## Squares of the form $p^x - (2^{2k+1}(2p - 1))^y$ for prime pairs

Let $p$ be a prime with
$p \equiv 3 \pmod 8$ such that $2p - 1$ is prime, and let $k$ be a non-negative integer. Then
non-negative integers $x$, $y$ and $z$ satisfy $p^x - (2^{2k+1}(2p - 1))^y = z^2$ if and only if
$(x, y, z) = (0, 0, 0)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 9.

Stated but not proved: `MetaMathlibExt.prime_pair_pow_sub_two_pow_odd_mul_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#prime-pair-pow-sub-two-pow-odd-mul-pow-e).

## The exponential equations for the prime pair (2, 3)

The six equations
$(-1)^\alpha 2^x + (-1)^\beta (2^k \cdot 3)^y = z^2$ with $\alpha, \beta, k \in \{0, 1\}$ and
$\alpha\beta = 0$ have exactly the following solutions in natural numbers $x, y, z$, where the
equations are read in the integers. The equation $2^x + 3^y = z^2$ holds if and only if
$(x, y, z)$ is $(0, 1, 2)$, $(3, 0, 3)$ or $(4, 2, 5)$. The equation $2^x - 3^y = z^2$ holds if
and only if $(x, y, z)$ is $(0, 0, 0)$, $(1, 0, 1)$ or $(2, 1, 1)$. The equation
$-2^x + 3^y = z^2$ holds if and only if $(x, y, z)$ is $(0, 0, 0)$, $(1, 1, 1)$, $(1, 3, 5)$,
$(3, 2, 1)$ or $(5, 4, 7)$. The equation $2^x + 6^y = z^2$ holds if and only if $(x, y, z)$ is
$(3, 0, 3)$ or $(6, 2, 10)$. The equation $2^x - 6^y = z^2$ holds if and only if $(x, y, z)$ is
$(0, 0, 0)$ or $(1, 0, 1)$. The equation $-2^x + 6^y = z^2$ holds if and only if $(x, y, z)$ is
$(0, 0, 0)$, $(1, 1, 2)$, $(5, 2, 2)$, $(9, 4, 28)$ or $(5, 5, 88)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 10.

Stated but not proved: `MetaMathlibExt.two_pow_three_pow_six_pow_eq_sq_solutions` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#two-pow-three-pow-six-pow-eq-sq-solution).

## Solutions of $2 + 7^y = z^2$

For natural numbers $y, z$, we have $2 + 7^y = z^2$ if and
only if $(y, z) = (1, 3)$.

## Sources

- Jing Zhang and Yuan Li, *On the Equation (-1)^α p^x + (-1)^β (2^k(2p - 1))^y = z^2 for Prime Pairs (p, 2p - 1)*, INTEGERS 24 (2024), Article A64, Theorem 11.

Stated but not proved: `MetaMathlibExt.two_add_seven_pow_eq_sq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimePairExponentialDiophantineWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html#two-add-seven-pow-eq-sq-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Squares as sums or differences of powers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/squares-as-sums-or-differences-of-powers)
