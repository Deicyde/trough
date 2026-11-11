---
declaration: section
origin: cited
lean: MetaMathlibExt.primitive_nondeficient_prime_power_bound, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.IsNondeficient, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.IsPrimitiveNondeficient, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.abundancyIndex, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.abundancySup, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.isPrimitiveNondeficient_two_pow_mul_prime_iff, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.deficient_of_odd_card_primeFactors_eq_two, MathlibExt.NumberTheory.PrimitiveNondeficientWanted.exists_pow_factorization_add_one_lt_two_mul_radical
statement: formalized
---

# Primitive non-deficient numbers

14 results, 5 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html).

## Prime-power bound for primitive non-deficient numbers

Let $\sigma(m)$ denote the sum of the
divisors of $m$. Let $n$ be a positive integer that is non-deficient, $\sigma(n) \ge 2n$, and
primitive, meaning that every divisor $m$ of $n$ with $m < n$ is deficient, $\sigma(m) < 2m$.
Let $k$ be the number of distinct prime factors of $n$ and $R$ their product. Then $n$ has a
prime factor $p$ with $p^{v_p(n) + 1} < 2kR$, where $v_p(n)$ is the exponent of $p$ in $n$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?," Journal of Integer Sequences 29 (2026), Article 26.4.3, Theorem, equation, lines 107–109, https://cs.uwaterloo.ca/journals/JIS/VOL29/Zelinsky/zel14.tex

Formalized by `MetaMathlibExt.primitive_nondeficient_prime_power_bound`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/PrimitiveNondeficientBound.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/PrimitiveNondeficientBound.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#primitive-nondeficient-prime-power-bound).

## Non-deficient number

A natural number $n$ is non-deficient when $n \ne 0$ and
$\sigma(n) \ge 2n$, where $\sigma(n)$ is the sum of the positive divisors of $n$.

Positivity is part of the notion: $0$ has no divisors in this convention, so the inequality
alone would make $0$ non-deficient.

Formalized by `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.IsNondeficient`, a definition declared in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#is-nondeficient).

## Primitive non-deficient number

A natural number $n$ is primitive non-deficient when it
is non-deficient and every proper divisor $m$ of $n$ (a divisor with $m < n$) is deficient, that
is, $\sigma(m) < 2m$, where $\sigma(m)$ is the sum of the positive divisors of $m$.

Formalized by `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.IsPrimitiveNondeficient`, a definition declared in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#is-primitive-nondeficient).

## Abundancy index

For a natural number $n$, the abundancy index is the rational number
$h(n) = \sigma(n)/n$, where $\sigma(n)$ is the sum of the positive divisors of $n$.

At $n = 0$ this gives $h(0) = 0$, since division by zero is $0$ in $\mathbb{Q}$; the abundancy
index is only meaningful for positive $n$.

Formalized by `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.abundancyIndex`, a definition declared in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#abundancy-index).

## Product of $p/(p-1)$ over the prime factors

For a natural number $n$, let
$H(n) = \prod_p p/(p-1)$ in $\mathbb{Q}$, the product over the distinct primes $p$ dividing $n$.
For $n = 0$ the product is empty ($0$ is taken to have no prime factors), so $H(0) = 1$.

Formalized by `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.abundancySup`, a definition declared in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#abundancy-sup).

## Even primitive non-deficient numbers with two prime factors

Let $p$ be an odd prime and
$a$ a natural number. Then $2^a p$ is primitive non-deficient if and only if
$2^a < p \le 2^{a+1} - 1$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma, first part.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.isPrimitiveNondeficient_two_pow_mul_prime_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#is-primitive-nondeficient-two-pow-mul-pr).

## Odd numbers with two prime factors are deficient

If $n$ is an odd natural number with
exactly two distinct prime divisors, then $\sigma(n) < 2n$, where $\sigma(n)$ is the sum of the
positive divisors of $n$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma, second part.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.deficient_of_odd_card_primeFactors_eq_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#deficient-of-odd-card-prime-factors-eq-t).

## Small component for odd primitive non-deficient numbers with three or four prime factors

Let $n$ be an odd primitive non-deficient number with exactly $3$ or exactly $4$ distinct prime
factors, and let $R$ be the product of the distinct prime factors of $n$. Then some prime factor
$p$ of $n$ satisfies $p^{a+1} < 2R$, where $a$ is the exponent of $p$ in $n$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.exists_pow_factorization_add_one_lt_two_mul_radical` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#exists-pow-factorization-add-one-lt-two).

## Grün's bound for non-deficient numbers

Let $n$ be a non-deficient number with $k$
distinct prime factors, the least of which is $p_1$. Then $\tfrac{3}{2} p_1 - 2 < k$, and if
$p_1 \ge 5$ then $p_1 + 2 \le k$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.grun_bounds_of_isNondeficient` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#grun-bounds-of-is-nondeficient).

## The power of 2 in an even primitive non-deficient number is below its radical

Let $n$
be an even primitive non-deficient number, that is, a positive integer with $\sigma(n) \ge 2n$
all of whose proper divisors $m$ satisfy $\sigma(m) < 2m$, where $\sigma$ is the sum of divisors.
If $2^a$ is the largest power of $2$ dividing $n$ and $R$ is the product of the distinct primes
dividing $n$, then $2^{a+1} < R$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Proposition.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.two_pow_factorization_add_one_lt_radical` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#two-pow-factorization-add-one-lt-radical).

## Zelinsky's reciprocal bound

For real numbers $k$ and $m$ with $k \ge 2$ and
$0 < m < 1/(k(k+1))$, we have $1/(1 - km) < 1 + (k+1)m$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.one_div_one_sub_mul_lt_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#one-div-one-sub-mul-lt-add).

## Abundancy ratio at an exactly dividing prime power

Let $n$ be a positive integer, $p$ a
prime and $a \ge 1$ an integer such that $p^a$ exactly divides $n$ (that is, $p^a \mid n$ and
$p^{a+1} \nmid n$). Then $h(n)/h(n/p) \le 1 + 1/p^a$, where $h(m) = \sigma(m)/m$ is the abundancy
index and $\sigma(m)$ is the sum of the positive divisors of $m$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.abundancyIndex_div_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#abundancy-index-div-le).

## Generalized Puchta lemma

Let $n$ be a primitive non-deficient number with $k$ distinct
prime factors, the least of which is $p_1$, and suppose that $(p_1, k) \ne (3, 3)$. Let $\alpha$
be a rational number with $0 < \alpha < 1$ such that $H(n) \ge 2 + \alpha$, where
$H(n) = \prod_p p/(p-1)$ is the product over the distinct primes $p$ dividing $n$. Then some
prime factor $p$ of $n$ satisfies $p^{a+1} < \max\bigl(2(k + 2 + p_1)/\alpha,\ k(k+1)\bigr)$,
where $a$ is the exponent of $p$ in $n$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Lemma.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.exists_pow_factorization_add_one_lt_max` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#exists-pow-factorization-add-one-lt-max).

## Dichotomy for odd primitive non-deficient numbers

Let $n$ be an odd primitive
non-deficient number, that is, a positive integer with $\sigma(n) \ge 2n$ all of whose proper
divisors $m$ satisfy $\sigma(m) < 2m$, where $\sigma$ is the sum of divisors. Let $k$ be the
number of distinct prime factors of $n$, let $p_1$ and $p_k$ be its least and greatest prime
factors, and let $R$ be the product of the distinct primes dividing $n$. Then either
$p_k < \sqrt{R}$, or some prime $p$ dividing $n$ satisfies $p^{a+1} < (k + 2 + p_1)(p_k - 1)$,
where $a$ is the exponent of $p$ in $n$.

## Sources

- Joshua Zelinsky, "Must a Primitive Non-Deficient Number Always Have a Small Component?", Proposition.

Stated but not proved: `MathlibExt.NumberTheory.PrimitiveNondeficientWanted.max_primeFactor_lt_sqrt_radical_or_exists_pow_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimitiveNondeficientWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html#max-prime-factor-lt-sqrt-radical-or-exis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive non-deficient numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/primitive-non-deficient-numbers)
