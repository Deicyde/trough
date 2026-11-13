---
declaration: section
origin: cited
lean: MetaMathlibExt.gcdTermSeq, MetaMathlibExt.gcdTermSeq_zero, MetaMathlibExt.mul_mk_gcdTermSeq, MetaMathlibExt.gcdTermSeq_natural_and_eq_gcd_add_one, MetaMathlibExt.gcdTermSeq_le_gcdTermSeq_one_one, MetaMathlibExt.gcd_add_one_eq_floor_div_mod_five, MetaMathlibExt.gcd_eq_neg_emod_emod_five_sub_two, MetaMathlibExt.gcd_arithmetic_terms_small_bases
statement: formalized
---

# Arithmetic terms for the greatest common divisor

8 results, 3 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html).

## The gcd-term sequence

For natural numbers $a$, $b$ and $n$, $s_{a,b}(n)$ is the rational
number that is the coefficient of $z^n$ in the inverse of the formal power series
$(z^a - 1)(z^b - 1)$ over $\mathbb{Q}$. For $a, b \ge 1$ this series has constant coefficient $1$,
so $s_{a,b}$ is the coefficient sequence of $f_{a,b}(z) = 1 / ((z^a - 1)(z^b - 1))$. If $a = 0$
or $b = 0$ the series is $0$, whose inverse is taken to be $0$, so $s_{a,b}(n) = 0$.

## Sources

- Mihai Prunescu and Joseph M. Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Section 2 (definition of `s_{a,b}`).

Formalized by `MetaMathlibExt.gcdTermSeq`, a definition declared in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-term-seq).

## Initial value of the gcd-term sequence

For natural numbers $a, b \ge 1$, the gcd-term
sequence satisfies $s_{a,b}(0) = 1$.

## Sources

- Prunescu and Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Section 2.

Formalized by `MetaMathlibExt.gcdTermSeq_zero`, a theorem declared in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-term-seq-zero).

## Generating function of the gcd-term sequence

For natural numbers $a, b \ge 1$, in the
ring $\mathbb{Q}[[z]]$ of formal power series, the gcd-term sequence $s_{a,b}$ satisfies

$$
(z^a - 1)(z^b - 1) \sum_{n \ge 0} s_{a,b}(n) z^n = 1.
$$

## Sources

- Prunescu and Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Section 2.

Formalized by `MetaMathlibExt.mul_mk_gcdTermSeq`, a theorem declared in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#mul-mk-gcd-term-seq).

## The gcd-term sequence is integral and recovers the gcd

Let $a, b \ge 1$ be natural
numbers and let $s_{a,b}$ be the gcd-term sequence. Every value $s_{a,b}(n)$ is a natural number,
and $s_{a,b}(ab) = \gcd(a, b) + 1$.

## Sources

- Mihai Prunescu and Joseph M. Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Lemma 4.

Stated but not proved: `MetaMathlibExt.gcdTermSeq_natural_and_eq_gcd_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-term-seq-natural-and-eq-gcd-add-one).

## The gcd-term sequence is bounded by $n + 1$

Let $a, b \ge 1$ be natural numbers, at least
one of them greater than $1$, and let $s_{a,b}$ be the gcd-term sequence. For every natural
number $n$, $s_{a,b}(n) \le s_{1,1}(n) = n + 1$, and $s_{a,b}(n) = s_{1,1}(n)$ only if $n = 0$.

## Sources

- Mihai Prunescu and Joseph M. Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Lemma 5.

Stated but not proved: `MetaMathlibExt.gcdTermSeq_le_gcdTermSeq_one_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-term-seq-le-gcd-term-seq-one-one).

## Arithmetic term for the gcd in base $5$

For all natural numbers $a, b \ge 1$,

$$
\gcd(a, b) + 1 = \left\lfloor \frac{5^{ab(ab+a+b)}}{(5^{a^2 b} - 1)(5^{a b^2} - 1)} \right\rfloor
\bmod 5^{ab},
$$

that is, $\gcd(a, b)$ is one less than the remainder of this floor modulo $5^{ab}$.

## Sources

- Mihai Prunescu and Joseph M. Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Theorem 1.

Stated but not proved: `MetaMathlibExt.gcd_add_one_eq_floor_div_mod_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-add-one-eq-floor-div-mod-five).

## Second arithmetic term for the gcd in base $5$

For all natural numbers $a, b \ge 1$,

$$
\gcd(a, b) = \Big( \big( (-5^{ab(ab+a+b)}) \bmod \big( (5^{a^2 b} - 1)(5^{a b^2} - 1) \big) \big)
\bmod 5^{ab} \Big) - 2
$$

in the integers, where $x \bmod m$ is the remainder of $x$ in $\{0, \dots, m - 1\}$ for $m > 0$,
also when $x < 0$.

## Sources

- Mihai Prunescu and Joseph M. Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Corollary 1.

Stated but not proved: `MetaMathlibExt.gcd_eq_neg_emod_emod_five_sub_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-eq-neg-emod-emod-five-sub-two).

## The gcd terms in bases $2$, $3$ and $4$

Let $c \in \{2, 3, 4\}$, let $a, b \ge 1$ be
natural numbers, and put $E = ab(ab + a + b)$ and $D = (c^{a^2 b} - 1)(c^{a b^2} - 1)$. Then the
identity

$$
\gcd(a, b) = \left( \lfloor c^E / D \rfloor \bmod c^{ab} \right) - 1
$$

holds if and only if $(a, b) \ne (1, 1)$, and the identity

$$
\gcd(a, b) = \big( ((-c^E) \bmod D) \bmod c^{ab} \big) - 2
$$

holds if and only if $(a, b) \ne (1, 1)$. Both identities are read in the integers, where
$x \bmod m$ is the remainder of $x$ in $\{0, \dots, m - 1\}$ for $m > 0$, also when $x < 0$.

## Sources

- Mihai Prunescu and Joseph M. Shunia, *Arithmetic-Term Representations for the Greatest Common Divisor*, INTEGERS 26 (2026), Article A96, Corollary 2.

Stated but not proved: `MetaMathlibExt.gcd_arithmetic_terms_small_bases` is written with `theorem_wanted` in [WantedExt/NumberTheory/GcdArithmeticTermWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GcdArithmeticTermWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html#gcd-arithmetic-terms-small-bases).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic terms for the greatest common divisor](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/arithmetic-terms-for-the-greatest-common-divisor)
