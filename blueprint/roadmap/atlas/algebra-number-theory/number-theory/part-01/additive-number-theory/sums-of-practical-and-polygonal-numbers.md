---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_practical_add_triangular, MetaMathlibExt.eventually_practical_add_two_polygonal, MetaMathlibExt.exists_sq_modEq_eight_mul_add_one, MetaMathlibExt.isPracticalNumber_mul_of_le_sigma_add_one, MetaMathlibExt.sq_sub_one_div_eight_eq_triangular, MetaMathlibExt.exists_polygonal_add_polygonal_modEq_prime, MetaMathlibExt.exists_polygonal_add_polygonal_modEq_two, MetaMathlibExt.exists_sq_add_sq_modEq_prime_pow
statement: formalized
---

# Sums of practical and polygonal numbers

12 results, 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html).

## Every positive integer is a practical number plus a triangular number

For every natural
number $n > 0$ there are a practical number $q$ and a natural number $k$ with
$n = q + k(k+1)/2$; the case $k = 0$, where the triangular number is $0$, is allowed.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Theorem 1 (`jis-2024-24.5.1-thm-1`).

Stated but not proved: `MetaMathlibExt.exists_practical_add_triangular` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-practical-add-triangular).

## Large integers as a practical number plus two polygonal numbers

Let $s > 3$ be a natural
number and, for a natural number $x$, let $P_s(x) = (s-2)\binom{x}{2} + x$ be the $x$-th
$s$-gonal number, so that $P_s(0) = 0$. There is a natural number $N$ such that every natural
number $n > N$ can be written as $n = q + P_s(x) + P_s(y)$ with $q$ a practical number and
$x, y$ natural numbers.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Theorem 2 (`jis-2024-24.5.1-thm-2`).

Stated but not proved: `MetaMathlibExt.eventually_practical_add_two_polygonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#eventually-practical-add-two-polygonal).

## Square roots modulo powers of two

For all natural numbers $m > 0$ and $n > 0$ there is
a natural number $x$ with $1 \le x \le 2^m - 1$ and $x^2 \equiv 8n + 1 \pmod{2^{m+2}}$.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 3 (arXiv Lemma 3.1; `jis-2024-24.5.1-lem-3`).

Stated but not proved: `MetaMathlibExt.exists_sq_modEq_eight_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-sq-mod-eq-eight-mul-add-one).

## Products of a practical number with small factors

Let $m$ be a practical number and let
$\sigma(m)$ denote the sum of the positive divisors of $m$. Then for every natural number $n$
with $1 \le n \le \sigma(m) + 1$, the product $mn$ is a practical number.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 4 (arXiv Lemma 3.2; `jis-2024-24.5.1-lem-4`), quoting Margenstern.

Stated but not proved: `MetaMathlibExt.isPracticalNumber_mul_of_le_sigma_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#is-practical-number-mul-of-le-sigma-add).

## Odd squares and triangular numbers

For every odd natural number $x$, the number
$(x^2 - 1)/8$ is a triangular number: there is a natural number $k$ with
$(x^2 - 1)/8 = p_3(k)$, where $p_3(k) = k(k+1)/2$ is the $k$-th $3$-gonal number.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 5 (arXiv Lemma 3.3; `jis-2024-24.5.1-lem-5`).

Stated but not proved: `MetaMathlibExt.sq_sub_one_div_eight_eq_triangular` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#sq-sub-one-div-eight-eq-triangular).

## Sums of two polygonal numbers modulo an odd prime

For a natural number $s > 3$ and a
natural number $x$, let $P_s(x) = (s-2)\binom{x}{2} + x$ be the $x$-th $s$-gonal number. For
every odd prime $p$ and every natural number $n > 0$ there are natural numbers $x, y > 0$ with
$P_s(x) + P_s(y) \equiv n \pmod{p}$.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 6 (arXiv Lemma 4.1; `jis-2024-24.5.1-lem-6`).

Stated but not proved: `MetaMathlibExt.exists_polygonal_add_polygonal_modEq_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-polygonal-add-polygonal-mod-eq-pr).

## Parity of sums of two polygonal numbers

For a natural number $s > 3$ and a natural
number $x$, let $P_s(x) = (s-2)\binom{x}{2} + x$ be the $x$-th $s$-gonal number. For every
natural number $n > 0$ there are natural numbers $x, y > 0$ such that
$P_s(x_1) + P_s(y_1) \equiv n \pmod{2}$ for all natural numbers $x_1, y_1 > 0$ with
$x_1 \equiv x \pmod{4}$ and $y_1 \equiv y \pmod{4}$.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 7 (arXiv Lemma 4.2; `jis-2024-24.5.1-lem-7`).

Stated but not proved: `MetaMathlibExt.exists_polygonal_add_polygonal_modEq_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-polygonal-add-polygonal-mod-eq-tw).

## Sums of two squares modulo prime powers

Let $p$ be a prime with $p \equiv 1 \pmod{4}$.
For all natural numbers $n > 0$ and $k > 0$ there are natural numbers $x, y > 0$ with
$x^2 + y^2 \equiv n \pmod{p^k}$ and $p \nmid y$.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 8 (arXiv Lemma 4.3; `jis-2024-24.5.1-lem-8`).

Stated but not proved: `MetaMathlibExt.exists_sq_add_sq_modEq_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-sq-add-sq-mod-eq-prime-pow).

## Sums of two polygonal numbers modulo prime powers

For a natural number $s > 3$ and a
natural number $x$, let $P_s(x) = (s-2)\binom{x}{2} + x$ be the $x$-th $s$-gonal number. There
is a prime $p$ with $p \equiv 1 \pmod{4}$ and $p \nmid s - 2$ such that for all natural numbers
$k > 0$ and $n > 0$ there are natural numbers $x, y > 0$ with
$P_s(x) + P_s(y) \equiv n \pmod{p^k}$.

The paper's statement asks only for an odd prime; the condition $p \equiv 1 \pmod{4}$ is the
choice made in its proof via Lemma 8 (arXiv Lemma 4.3).

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 9 (arXiv Lemma 4.4; `jis-2024-24.5.1-lem-9`).

Stated but not proved: `MetaMathlibExt.exists_prime_polygonal_add_polygonal_modEq_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-prime-polygonal-add-polygonal-mod).

## Quadratic upper bound for polygonal numbers

For a natural number $s > 3$ and a natural
number $x$, let $P_s(x) = (s-2)\binom{x}{2} + x$ be the $x$-th $s$-gonal number. For every natural
number $c$ there is a natural number $A$ such that $2 P_s(2cx) \le A x^2$ for every natural
number $x \ge 1$.

The paper states this only for one specific prime $c$, the prime chosen in Lemma 9 (arXiv
Lemma 4.4), and for real $x$; here $c$ is an arbitrary natural number and $x$ is a natural number.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 10 (arXiv Lemma 4.5; `jis-2024-24.5.1-lem-10`).

Stated but not proved: `MetaMathlibExt.exists_two_polygonal_two_mul_le_mul_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#exists-two-polygonal-two-mul-le-mul-sq).

## Practical numbers divisible by neither 3 nor 4

If $q$ is a practical number that is
divisible by neither $3$ nor $4$, then $q = 1$ or $q = 2$.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Lemma 11 (arXiv Lemma 4.6; `jis-2024-24.5.1-lem-11`).

Stated but not proved: `MetaMathlibExt.isPracticalNumber_eq_one_or_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#is-practical-number-eq-one-or-two).

## Exceptions to sums of a practical number and polygonal numbers

(a) Let $s \ge 3$ with
$s \equiv 0$ or $s \equiv 4 \pmod{12}$. Then there are infinitely many positive integers $n$ that
cannot be written as $n = q + p_s(m)$ with $q$ a practical number and $m \ge 0$ an integer, where
$p_s(m)$ is the $m$-th $s$-gonal number. (b) For every natural number $M$ there is a natural
number $S$ such that for every $t \ge S$ there are at least $M$ positive integers $n$ that cannot
be written as $n = q + p_t(x) + p_t(y)$ with $q$ a practical number and integers $x, y \ge 0$.

## Sources

- Sai Teja Somu and Duc Van Khanh Tran, *On Sums of Practical Numbers and Polygonal Numbers*, Journal of Integer Sequences 27 (2024), Article 24.5.1, Proposition 12 (arXiv Proposition 4.7; `jis-2024-24.5.1-prop-12`).

Stated but not proved: `MetaMathlibExt.practical_add_polygonal_exceptions` is written with `theorem_wanted` in [WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PracticalPolygonalSumsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html#practical-add-polygonal-exceptions).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of practical and polygonal numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/additive-number-theory/sums-of-practical-and-polygonal-numbers)
