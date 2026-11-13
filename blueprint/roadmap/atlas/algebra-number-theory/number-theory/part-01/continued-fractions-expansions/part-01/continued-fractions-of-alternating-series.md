---
declaration: section
origin: cited
lean: MetaMathlibExt.alternatingSeries_contFract_twoStepPattern, MetaMathlibExt.alternatingSeries_contFract_threeStepPattern, MetaMathlibExt.twoStepPatternDen, MetaMathlibExt.twoStepPatternDen_one_one, MetaMathlibExt.threeStepPatternDen, MetaMathlibExt.threeStepPatternDen_one_one, MetaMathlibExt.twoStepPattern_alternatingSeries_contFract, MetaMathlibExt.twoStepPattern_irrationalityExponent
statement: formalized
---

# Continued fractions of alternating series

10 results, 4 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html).

## Alternating series with a two-step continued fraction pattern

Let $(u_i)_{i \ge 0}$ be
positive integers with $u_0 = 1$, and let $x$ be an irrational real number with
$\sum_{i \ge 0} (-1)^i / u_i = x$. Write $x = [a_0; a_1, a_2, \dots]$ for its continued fraction
expansion and $p_n / q_n = [a_0; a_1, \dots, a_n]$ for its convergents, with $q_0 = 1$ and
$q_1 = a_1$. Suppose that for every $n \ge 0$ we have
$\sum_{i=0}^{n} (-1)^i / u_i = p_{n+1} / q_{n+1}$, $u_{2n+1} \mid u_{2n+2}$ and
$u_{2n+3} = \bigl(\prod_{j=0}^{n} u_{2j+2} / u_{2j+1}\bigr)^2 + u_{2n+2}$. Then
(i) $u_n = q_n q_{n+1}$ for every $n \ge 0$, (ii) for every $n \ge 0$ there is a natural number
$m$ with $a_{2n+3} = m \, q_{2n+1}$, and (iii) $a_{2n+2} = 1$ for every $n \ge 1$.

Part (iii) is stated only for $n \ge 1$, because it can fail at $n = 0$: the continued fraction
$[0; 1, 2, 1, 1, 4, 1, 32, 1, 1280, \dots]$, continued by $a_{2n+4} = 1$ and
$a_{2n+3} = q_{2n+1}$, with $u_n = q_n q_{n+1}$ (here $q = 1, 1, 3, 4, 7, 32, 39, 1280, \dots$)
satisfies every hypothesis and has $a_2 = 2$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Theorem 4 (`jis-2025-25.1.4-thm-4`).

Stated but not proved: `MetaMathlibExt.alternatingSeries_contFract_twoStepPattern` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#alternating-series-cont-fract-two-step-p).

## Alternating series with a three-step continued fraction pattern

Let $(u_i)_{i \ge 0}$
be positive integers with $u_0 = 1$, and let $x$ be an irrational real number with
$\sum_{i \ge 0} (-1)^i / u_i = x$. Write $x = [a_0; a_1, a_2, \dots]$ for its continued fraction
expansion and $p_n / q_n = [a_0; a_1, \dots, a_n]$ for its convergents, with $q_0 = 1$ and
$q_1 = a_1$. Suppose that for every $n \ge 0$ we have
$\sum_{i=0}^{n} (-1)^i / u_i = p_{n+1} / q_{n+1}$, $u_{3n+2} \mid u_{3n+3}$,
$u_{3n+2} - u_{3n+1} = \bigl(\prod_{j=0}^{\lfloor 3n/2 \rfloor} u_{3n-2j+1} / u_{3n-2j}\bigr)^2$
and $u_{3n+4} - u_{3n+3} = (u_{3n+3} / u_{3n+2})^2 (u_{3n+2} - u_{3n+1})$. Then
(i) $u_n = q_n q_{n+1}$ for every $n \ge 0$, (ii) for every $n \ge 0$ there is a natural number
$m$ with $a_{3n+4} = m \, q_{3n+2}$, and (iii) $a_{3n+3} = 1$ for every $n \ge 0$ and
$a_{3n+2} = 1$ for every $n \ge 1$.

The product runs over the quotients $u_{k+1} / u_k$ for $k = 3n, 3n - 2, 3n - 4, \dots$, ending
at $k = 1$ when $n$ is odd and at $k = 0$ when $n$ is even. The condition $a_{3n+2} = 1$ is
stated only for $n \ge 1$, because it can fail at $n = 0$: the continued fraction
$[0; 1, 2, 1, 3, 1, 1, 19, 1, 1, 699, \dots]$ with $u_n = q_n q_{n+1}$ satisfies every hypothesis
and has $a_2 = 2$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Theorem 10 (`jis-2025-25.1.4-thm-10`).

Stated but not proved: `MetaMathlibExt.alternatingSeries_contFract_threeStepPattern` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#alternating-series-cont-fract-three-step).

## Convergent denominators of the two-step pattern

For a natural number $\beta$ and a
sequence $(\omega_n)_{n \ge 0}$ of natural numbers, define natural numbers $q_n$ by $q_0 = 1$,
$q_1 = \omega_0$, and for every $n \ge 0$, $q_{2n+2} = q_{2n+1} + q_{2n}$ and
$q_{2n+3} = \omega_{n+1} q_{2n+1}^\beta q_{2n+2} + q_{2n+1}$.

When the $\omega_n$ are positive, these are the convergent denominators of the continued fraction
$[0; \omega_0, 1, \omega_1 q_1^\beta, 1, \omega_2 q_3^\beta, 1, \dots]$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Section 2.1, displays (e2) and (e22).

Formalized by `MetaMathlibExt.twoStepPatternDen`, a definition declared in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#two-step-pattern-den).

## Small values of the two-step pattern denominators

For $\beta = 1$ and $\omega_n = 1$ for
all $n$, the convergent denominators $q_0, \dots, q_7$ of the two-step pattern are
$1, 1, 2, 3, 5, 18, 23, 432$ (the paper's first example).

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Section 2.1, first example.

Formalized by `MetaMathlibExt.twoStepPatternDen_one_one`, a theorem declared in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#two-step-pattern-den-one-one).

## Convergent denominators of the three-step pattern

For a natural number $\beta$ and a
sequence $(\omega_n)_{n \ge 0}$ of natural numbers, define natural numbers $q_n$ by $q_0 = 1$,
$q_1 = \omega_0$, and for every $n \ge 0$, $q_{3n+2} = q_{3n+1} + q_{3n}$,
$q_{3n+3} = q_{3n+2} + q_{3n+1}$ and $q_{3n+4} = \omega_{n+1} q_{3n+3} q_{3n+2}^\beta + q_{3n+2}$.

When the $\omega_n$ are positive, these are the convergent denominators of the continued fraction
$[0; \omega_0, 1, 1, \omega_1 q_2^\beta, 1, 1, \omega_2 q_5^\beta, \dots]$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Section 2.2, displays (e3) and (e33).

Formalized by `MetaMathlibExt.threeStepPatternDen`, a definition declared in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#three-step-pattern-den).

## Small values of the three-step pattern denominators

For $\beta = 1$ and $\omega_n = 1$
for all $n$, the convergent denominators $q_0, \dots, q_7$ of the three-step pattern are
$1, 1, 2, 3, 8, 11, 19, 220$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Section 2.2, display (e33).

Formalized by `MetaMathlibExt.threeStepPatternDen_one_one`, a theorem declared in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#three-step-pattern-den-one-one).

## Two-step pattern as an alternating series

Let $\beta$ be a natural number, let
$(\omega_n)_{n \ge 0}$ be positive integers, and let $(q_n)_{n \ge 0}$ be the convergent
denominators of the two-step pattern for $\beta$ and $(\omega_n)$. Then the series
$\sum_{i \ge 0} (-1)^i / (q_i q_{i+1})$ converges absolutely, and its sum $x$ has continued
fraction expansion $[a_0; a_1, a_2, \dots]$ with $a_0 = 0$, $a_1 = \omega_0$, and
$a_{2n+2} = 1$ and $a_{2n+3} = \omega_{n+1} q_{2n+1}^\beta$ for every $n \ge 0$; that is,
$x = [0; \omega_0, 1, \omega_1 q_1^\beta, 1, \omega_2 q_3^\beta, 1, \dots]$.

The paper assumes $\beta \ge 1$; the statement here also allows $\beta = 0$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Proposition 2, under the hypotheses (e2) of Section 2.1.

Stated but not proved: `MetaMathlibExt.twoStepPattern_alternatingSeries_contFract` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#two-step-pattern-alternating-series-cont).

## Irrationality exponent of the two-step pattern

Let $\beta \ge 1$ be a natural number,
let $(\omega_n)_{n \ge 0}$ be positive integers, let $(q_n)_{n \ge 0}$ be the convergent
denominators of the two-step pattern for $\beta$ and $(\omega_n)$, and let
$x = \sum_{i \ge 0} (-1)^i / (q_i q_{i+1})$. Let $L$ be the limit superior, in the extended real
numbers, of $\ln \omega_n / \ln q_{2n}$ as $n \to \infty$. Then $x$ is Liouville with exponent $p$
for every real $p < 2 + \beta + L$, that is, for each such $p$ there is a constant $C$ such that
$0 < |x - m/k| < C / k^p$ for infinitely many positive integers $k$, each with some integer $m$.
Moreover $2 + \beta \le 2 + \beta + L$, and $x$ is transcendental.

In other words, the irrationality exponent of $x$ satisfies $\mu(x) \ge 2 + \beta + L$, where $L$
may be $+\infty$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Theorem 3.

Stated but not proved: `MetaMathlibExt.twoStepPattern_irrationalityExponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#two-step-pattern-irrationality-exponent).

## Three-step pattern as an alternating series

Let $\beta$ be a natural number, let
$(\omega_n)_{n \ge 0}$ be positive integers, and let $(q_n)_{n \ge 0}$ be the convergent
denominators of the three-step pattern for $\beta$ and $(\omega_n)$. Then the series
$\sum_{i \ge 0} (-1)^i / (q_i q_{i+1})$ converges absolutely, and its sum $x$ has continued
fraction expansion $[a_0; a_1, a_2, \dots]$ with $a_0 = 0$, $a_1 = \omega_0$, and
$a_{3n+2} = a_{3n+3} = 1$ and $a_{3n+4} = \omega_{n+1} q_{3n+2}^\beta$ for every $n \ge 0$; that is,
$x = [0; \omega_0, 1, 1, \omega_1 q_2^\beta, 1, 1, \omega_2 q_5^\beta, \dots]$.

The paper assumes $\beta \ge 1$; the statement here also allows $\beta = 0$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Proposition 8, under the hypotheses (e3) of Section 2.2.

Stated but not proved: `MetaMathlibExt.threeStepPattern_alternatingSeries_contFract` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#three-step-pattern-alternating-series-co).

## Irrationality exponent of the three-step pattern

Let $\beta \ge 1$ be a natural number,
let $(\omega_n)_{n \ge 0}$ be positive integers, let $(q_n)_{n \ge 0}$ be the convergent
denominators of the three-step pattern for $\beta$ and $(\omega_n)$, and let
$x = \sum_{i \ge 0} (-1)^i / (q_i q_{i+1})$. Let $L$ be the limit superior, in the extended real
numbers, of $\ln \omega_n / \ln q_{3n}$ as $n \to \infty$. Then $x$ is Liouville with exponent $p$
for every real $p < 2 + \beta + L$, that is, for each such $p$ there is a constant $C$ such that
$0 < |x - m/k| < C / k^p$ for infinitely many positive integers $k$, each with some integer $m$.
Moreover $2 + \beta \le 2 + \beta + L$, and $x$ is transcendental.

In other words, the irrationality exponent of $x$ satisfies $\mu(x) \ge 2 + \beta + L$, where $L$
may be $+\infty$.

## Sources

- Khalil Ayadi, Chiheb Ben Bechir, and Maher Saadaoui, *Continued Fractions with Predictable Patterns and Transcendental Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.4, Theorem 9.

Stated but not proved: `MetaMathlibExt.threeStepPattern_irrationalityExponent` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingSeriesContinuedFractionWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html#three-step-pattern-irrationality-exponen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continued fractions of alternating series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-alternating-series)
