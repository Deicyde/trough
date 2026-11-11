---
declaration: section
origin: cited
lean: MetaMathlibExt.cube_split_of_mul_eq_prime_sq_mul_cube_of_gcd_eq_one, MetaMathlibExt.cube_split_of_mul_eq_prime_sq_mul_cube_of_gcd_prime, MetaMathlibExt.sq_add_add_one_eq_three_mul_cube_iff, MetaMathlibExt.sq_add_add_one_eq_cube_iff, MetaMathlibExt.gcd_sub_one_sq_add_add_one, MetaMathlibExt.cube_sub_cube_eq_two_or_one_iff, MetaMathlibExt.cube_sub_two_mul_cube_eq_one_iff, MetaMathlibExt.cube_sub_mul_cube_eq_one_iff_of_mem
statement: formalized
---

# Consecutive powerful numbers

18 results, 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html).

## Splitting $RS = p^2 C^3$ when $R$ and $S$ are coprime

Let $p$ be a prime and let $R$,
$S$, $C$ be integers with $RS = p^2 C^3$ and $\gcd(R, S) = 1$. Then there are integers $C_1$,
$C_2$ such that either $R = C_1^3$ and $S = p^2 C_2^3$, or $R = p^2 C_1^3$ and $S = C_2^3$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 1.

Stated but not proved: `MetaMathlibExt.cube_split_of_mul_eq_prime_sq_mul_cube_of_gcd_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#cube-split-of-mul-eq-prime-sq-mul-cube-o).

## Splitting $RS = p^2 C^3$ when $\gcd(R, S)$ is prime

Let $p$ be a prime and let $R$, $S$,
$C$ be integers with $RS = p^2 C^3$ such that $g = \gcd(R, S)$ is prime. Then there are
integers $C_1$, $C_2$ such that one of the following holds: $R = g C_1^3$ and $S = g C_2^3$;
or $R = g C_1^3$ and $S = g^2 p^2 C_2^3$; or $S = g C_1^3$ and $R = g^2 p^2 C_2^3$; or
$R = g p^2 C_1^3$ and $S = g^2 C_2^3$; or $S = g p^2 C_1^3$ and $R = g^2 C_2^3$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 1.

Stated but not proved: `MetaMathlibExt.cube_split_of_mul_eq_prime_sq_mul_cube_of_gcd_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#cube-split-of-mul-eq-prime-sq-mul-cube-o-2).

## Integer solutions of $u^2 \pm u + 1 = 3v^3$

For all integers $u$ and $v$,
$u^2 + u + 1 = 3v^3$ if and only if $(u, v) = (-2, 1)$ or $(u, v) = (1, 1)$, and
$u^2 - u + 1 = 3v^3$ if and only if $(u, v) = (2, 1)$ or $(u, v) = (-1, 1)$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 2.

Stated but not proved: `MetaMathlibExt.sq_add_add_one_eq_three_mul_cube_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#sq-add-add-one-eq-three-mul-cube-iff).

## When $u^2 \pm u + 1$ is a cube

For every integer $u$, $u^2 + u + 1$ is the cube of an
integer if and only if $u \in \{-19, -1, 0, 18\}$, and $u^2 - u + 1$ is the cube of an integer
if and only if $u \in \{-18, 0, 1, 19\}$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 3.

Stated but not proved: `MetaMathlibExt.sq_add_add_one_eq_cube_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#sq-add-add-one-eq-cube-iff).

## The gcd of $x \mp 1$ and $x^2 \pm x + 1$

For every integer $x$,
$\gcd(x - 1, x^2 + x + 1) = \gcd(x - 1, 3)$ and $\gcd(x + 1, x^2 - x + 1) = \gcd(x + 1, 3)$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 4.

Stated but not proved: `MetaMathlibExt.gcd_sub_one_sq_add_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#gcd-sub-one-sq-add-add-one).

## Integer solutions of $u^3 - v^3 = 2$ and $u^3 - v^3 = 1$

For all integers $u$ and $v$,
$u^3 - v^3 = 2$ if and only if $(u, v) = (1, -1)$, and $u^3 - v^3 = 1$ if and only if
$(u, v) = (1, 0)$ or $(u, v) = (0, -1)$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 5.

Stated but not proved: `MetaMathlibExt.cube_sub_cube_eq_two_or_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#cube-sub-cube-eq-two-or-one-iff).

## Integer solutions of $u^3 - 2v^3 = 1$

For all integers $u$ and $v$, $u^3 - 2v^3 = 1$ if
and only if $(u, v) = (1, 0)$ or $(u, v) = (-1, -1)$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 7.

Stated but not proved: `MetaMathlibExt.cube_sub_two_mul_cube_eq_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#cube-sub-two-mul-cube-eq-one-iff).

## Integer solutions of $u^3 - d v^3 = 1$ for $d \in \{4, 18, 36\}$

Let $d$ be one of the
integers $4$, $18$, $36$. For all integers $u$ and $v$, $u^3 - d v^3 = 1$ if and only if
$(u, v) = (1, 0)$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Lemma 8.

Stated but not proved: `MetaMathlibExt.cube_sub_mul_cube_eq_one_iff_of_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#cube-sub-mul-cube-eq-one-iff-of-mem).

## $x^3 - 1$ and $x^3 + 1$ are not both a prime square times a cube

There are no primes
$p$, $q$ and integers $x$, $a$, $b$ with $x^3 - 1 = p^2 a^3$ and $x^3 + 1 = q^2 b^3$.

As in the paper, $x$, $a$, $b$ range over all integers, with no positivity assumption.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Theorem 1.

Stated but not proved: `MetaMathlibExt.not_cube_sub_one_eq_prime_sq_mul_cube_and_cube_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#not-cube-sub-one-eq-prime-sq-mul-cube-an).

## $x^6 - 1$ is not $p^2 q^2$ times a nonzero cube

For all primes $p$, $q$ and all integers
$x$ and $a$ with $a \ne 0$, $x^6 - 1 \ne p^2 q^2 a^3$.

## Sources

- Jialai She, *Nonexistence of Consecutive Powerful Triplets Around Cubes with Prime-Square Factors*, INTEGERS 25 (2025), Article A103, Corollary 1.

Stated but not proved: `MetaMathlibExt.pow_six_sub_one_ne_prime_sq_mul_prime_sq_mul_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutivePowerfulTripletsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#pow-six-sub-one-ne-prime-sq-mul-prime-sq).

## Two is not a difference of two squares

For all integers $a$ and $b$,
$a^2 - b^2 \neq 2$.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.int_sq_sub_int_sq_ne_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#int-sq-sub-int-sq-ne-two).

## Exact divisibility of $x^2 + x + 1$ by $3$

If $x$ is an integer with
$x \equiv 1 \pmod 3$, then $3$ divides $x^2 + x + 1$ but $9$ does not.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.three_exact_dvd_sq_add_self_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#three-exact-dvd-sq-add-self-add-one).

## Exact divisibility of $x^2 - x + 1$ by $3$

If $x$ is an integer with
$x \equiv 2 \pmod 3$, then $3$ divides $x^2 - x + 1$ but $9$ does not.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.three_exact_dvd_sq_sub_self_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#three-exact-dvd-sq-sub-self-add-one).

## Integer points on a quartic give integer points on a cubic

Let $a$, $c$ and $e$ be
integers with $a \neq 0$. If there are integers $x \neq 0$ and $y$ with
$y^2 = a x^4 + c x^2 + e$, then there are integers $X \neq 0$ and $Y$ with
$Y^2 = X^3 + c X^2 + a e X$.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.exists_int_point_elliptic_of_exists_int_point_quartic` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#exists-int-point-elliptic-of-exists-int).

## Positive solutions of $x^2 - 3y^2 = 1$

For integers $x$ and $y$, we have $x > 0$,
$y > 0$ and $x^2 - 3y^2 = 1$ if and only if $x + y\sqrt{3} = (2 + \sqrt{3})^k$ in
$\mathbb{Z}[\sqrt{3}]$ for some natural number $k \ge 1$. Writing
$(2 + \sqrt{3})^k = u_k + v_k \sqrt{3}$ for $k \ge 0$, we have $(u_1, v_1) = (2, 1)$,
$(u_2, v_2) = (7, 4)$, and $u_{k+2} = 4u_{k+1} - u_k$ and $v_{k+2} = 4v_{k+1} - v_k$ for
every $k \ge 0$.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.pell_three_eq_one_positive_solutions_iff_and_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#pell-three-eq-one-positive-solutions-iff).

## Positive solutions of $x^2 - 3y^2 = -2$

For integers $x$ and $y$, we have $x > 0$,
$y > 0$ and $x^2 - 3y^2 = -2$ if and only if $x + y\sqrt{3} = (1 + \sqrt{3})(2 + \sqrt{3})^k$
in $\mathbb{Z}[\sqrt{3}]$ for some integer $k \ge 0$. Writing
$(1 + \sqrt{3})(2 + \sqrt{3})^k = u_k + v_k \sqrt{3}$ for $k \ge 0$, we have
$(u_0, v_0) = (1, 1)$, $(u_1, v_1) = (5, 3)$, and $u_{k+2} = 4u_{k+1} - u_k$ and
$v_{k+2} = 4v_{k+1} - v_k$ for every $k \ge 0$.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.pell_three_eq_neg_two_positive_solutions_iff_and_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#pell-three-eq-neg-two-positive-solutions).

## No cube whose neighbours are prime cubes times squares

There are no primes $p$, $q$
and positive integers $x$, $y$, $z$ with $x^3 - 1 = p^3 y^2$ and $x^3 + 1 = q^3 z^2$.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.not_exists_prime_cube_square_neighbors_of_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#not-exists-prime-cube-square-neighbors-o).

## No integer solutions of $64x^6 - 1 = p^3 q^3 y^2$ with $p$, $q$ prime

There are no
integers $x$, $y$ and primes $p$, $q$ with $64 x^6 - 1 = p^3 q^3 y^2$.

## Sources

- Tsz Ho Chan, "A Note on Three Consecutive Powerful Numbers", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.PowerfulNumbersWanted.not_exists_sixty_four_mul_pow_six_sub_one_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PowerfulNumbersWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PowerfulNumbersWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html#not-exists-sixty-four-mul-pow-six-sub-on).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Consecutive powerful numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/consecutive-powerful-numbers)
