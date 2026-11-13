---
declaration: section
origin: cited
lean: MetaMathlibExt.trinomialCoefficient, MetaMathlibExt.trinomialTransformSequence, MetaMathlibExt.trinomialTransformSequence_zero, MetaMathlibExt.trinomialTransformSequence_zero_apply, MetaMathlibExt.riordan_array_sum_eq_coeff_subst, MetaMathlibExt.trinomialCoefficient_eq_coeff, MetaMathlibExt.sum_trinomialCoefficient_arith_prog, MetaMathlibExt.trinomialCoefficient_alternating_sums_mod_three_five
statement: formalized
---

# Trinomial coefficients and the 2-Pascal triangle

35 results, 4 proved and 31 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html).

## Trinomial coefficient

For natural numbers $n$ and $k$, the trinomial coefficient in row
$n$ and column $k$ is the coefficient of $X^k$ in the polynomial $(1 + X + X^2)^n$.

Formalized by `MetaMathlibExt.trinomialCoefficient`, a definition declared in [MathlibExt/NumberTheory/TrinomialCoefficient.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/TrinomialCoefficient.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-coefficient).

## Trinomial transform

Let $R$ be a semiring and $a \colon \mathbb{N} \to R$ a sequence. The
trinomial transform of $a$ is the sequence $b \colon \mathbb{N} \to R$ given by

$$b_n = \sum_{i=0}^{2n} T(n, i)\, a_i,$$

where $T(n, i)$ is the trinomial coefficient, the coefficient of $X^i$ in $(1 + X + X^2)^n$,
regarded as an element of $R$.

## Sources

- László Németh, *The Trinomial Transform Triangle*, Journal of Integer Sequences 21 (2018), Article 18.7.3.

Formalized by `MetaMathlibExt.trinomialTransformSequence`, a definition declared in [MathlibExt/NumberTheory/TrinomialTransformSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/TrinomialTransformSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-transform-sequence).

## Zeroth term of the trinomial transform

For every semiring $R$ and every sequence
$a \colon \mathbb{N} \to R$, the zeroth term of the trinomial transform of $a$ equals $a_0$.

Formalized by `MetaMathlibExt.trinomialTransformSequence_zero`, a theorem declared in [MathlibExt/NumberTheory/TrinomialTransformSequence.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/TrinomialTransformSequence.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-transform-sequence-zero).

## Trinomial transform of the zero sequence

For every semiring $R$ and every
$n \in \mathbb{N}$, the $n$th term of the trinomial transform of the zero sequence
$\mathbb{N} \to R$ is $0$.

Formalized by `MetaMathlibExt.trinomialTransformSequence_zero_apply`, a theorem declared in [MathlibExt/NumberTheory/TrinomialTransformSequence.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/TrinomialTransformSequence.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-transform-sequence-zero-apply).

## Fundamental theorem of Riordan arrays

Write $[t^m]F$ for the coefficient of $t^m$ in a
power series $F$. Let $R$ be a commutative ring and let $d$, $h$, $f$ be power series over
$R$ with $h(0) = 0$. Then for every $n \in \mathbb{N}$,

$$\sum_{k=0}^{n} \left([t^n]\,d(t)\,h(t)^k\right) [t^k]\,f = [t^n]\,d(t)\,f(h(t)).$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 1 (`jis-2025-25.3.5-thm-1`).

Stated but not proved: `MetaMathlibExt.riordan_array_sum_eq_coeff_subst` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#riordan-array-sum-eq-coeff-subst).

## Trinomial coefficients as coefficients of a rational series

Write $\binom{n}{k}_2$ for
the trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$, and $[t^m]\,F$ for the
coefficient of $t^m$ in a formal power series $F$ over $\mathbb{Q}$. For all natural numbers
$n$ and $k$, $\binom{n}{k}_2 = [t^{2n}]\,(1 - t + t^2)^n (1 - t)^{-1} \left(t/(1-t)\right)^k$.

The paper also allows negative integers $k$; that case is not included here.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 3 (`jis-2025-25.3.5-thm-3`).

Stated but not proved: `MetaMathlibExt.trinomialCoefficient_eq_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-coefficient-eq-coeff).

## Roots-of-unity filter for trinomial coefficients

Write $\binom{n}{k}_2$ for the trinomial
coefficient, the coefficient of $t^k$ in $(1 + t + t^2)^n$. Let $n$, $x$, $b$ be natural
numbers with $x < b$, let $z \ne 0$ be a complex number, and let $w = e^{2\pi i/b}$. Then

$$\sum_{k=0}^{\lfloor (2n - x)/b \rfloor} \binom{n}{x + bk}_2 z^{x + bk} =
\frac{z^n}{b} \sum_{j=1}^{b} w^{j(n - x)} \left(1 + z w^j + \frac{1}{z w^j}\right)^n,$$

where for $x > 2n$ the left side is $0$. The hypothesis $z \ne 0$ is implicit in the
paper's $(z w^j)^{-1}$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 9 (`jis-2025-25.3.5-thm-9`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_arith_prog` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-arith-prog).

## Alternating trinomial sums over residue classes modulo 3 and 5

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$, and
$L_m$ for the Lucas numbers ($L_0 = 2$, $L_1 = 1$, $L_{m+2} = L_{m+1} + L_m$). Let $n$ and $x$ be
natural numbers.

If $x < 3$, then $3 \sum_{k=0}^{2n} (-1)^{k+x} \binom{n}{3k+x}_2$ equals $(-1)^n 2^{n+1} + 1$
when $n \equiv x \pmod 3$, and $(-1)^{n+1} 2^n + 1$ otherwise.

If $x < 5$, let $S = 5 \sum_{k=0}^{2n} (-1)^{k+x} \binom{n}{5k+x}_2$. Then
$S = 2 (-1)^n L_{2n} + 1$ when $n \equiv x \pmod 5$, $S = (-1)^{n+1} L_{2n+1} + 1$ when
$n \equiv x \pm 1 \pmod 5$, and $S = (-1)^n L_{2n-1} + 1$ when $n \ge 1$ and
$n \equiv x \pm 2 \pmod 5$.

The paper does not bound $x$; the last case excludes $n = 0$, where it would need $L_{-1}$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 10 (`jis-2025-25.3.5-cor-10`).

Stated but not proved: `MetaMathlibExt.trinomialCoefficient_alternating_sums_mod_three_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-coefficient-alternating-sums-m).

## Alternating sums of trinomial coefficients in an arithmetic progression

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in $(1 + t + t^2)^n$.
For natural numbers $n$, $x$, $b$ with $b$ even and $x < b$,

$$\sum_{k=0}^{2n} (-1)^k \binom{n}{x + bk}_2 = \frac{1}{b} \sum_{j=1}^{b}
\cos\frac{\pi(n - x)(1 + 2j)}{b} \left(1 + 2\cos\frac{\pi(2j + 1)}{b}\right)^n.$$

The paper sums over all $k \ge 0$ (the terms with $k > 2n$ vanish) and does not state
$x < b$; without it the identity fails: for $n = 3$ and $b = x = 2$ the left side is $1$ and
the right side is $0$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 11 (`jis-2025-25.3.5-cor-11`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_arith_prog_alternating` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-arith-prog-alt).

## Generating polynomial of trinomial coefficients with even index

Write $\binom{n}{k}_2$
for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. For every
$n \in \mathbb{N}$ and all complex numbers $z$ and $s$ with $s^2 = z$

$$\sum_{k=0}^{n} \binom{n}{2k}_2 z^k = \frac{(1 + s + z)^n + (1 - s + z)^n}{2}.$$

The paper states this for an indeterminate $z$, with $\sqrt{z}$ in place of $s$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 13 (`jis-2025-25.3.5-cor-13`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-even).

## Generating polynomial of trinomial coefficients with odd index

Write $\binom{n}{k}_2$
for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. For every
$n \in \mathbb{N}$ and all complex numbers $z$ and $s$ with $s^2 = z$ and $s \ne 0$

$$\sum_{k=0}^{n} \binom{n}{2k+1}_2 z^k = \frac{(1 + s + z)^n - (1 - s + z)^n}{2s}.$$

The paper states this for an indeterminate $z$, with $\sqrt{z}$ in place of $s$, and calls the
left side $q_n(z)$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 15 (`jis-2025-25.3.5-cor-15`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-odd).

## Alternating binomial transform of a row of trinomial coefficients

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. For all
$n, m \in \mathbb{N}$

$$\sum_{k=m}^{2n} \binom{n}{k}_2 \binom{k}{m} (-1)^k = \binom{n}{m}_2.$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 16 (`jis-2025-25.3.5-thm-16`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_mul_choose_alternating` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-mul-choose-alt).

## Two binomial transforms of a row of trinomial coefficients agree

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. For all
$n, m \in \mathbb{N}$

$$\sum_{k=0}^{m} \binom{n}{k}_2 \binom{m}{k} =
\sum_{k=0}^{2n} \binom{n}{k}_2 \binom{m+k}{k} (-1)^k.$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 17 (`jis-2025-25.3.5-thm-17`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_mul_choose_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-mul-choose-eq).

## Alternating binomial sum down a trinomial column

Write $\binom{n}{k}_2$ for the
trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$. For natural numbers $n \le m$,
$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{n-k}{m}_2 = \binom{n}{m-n}$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 18 (`jis-2025-25.3.5-thm-18`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_sub_mul_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-sub-mul-choose).

## Alternating binomial sum of trinomial coefficients over even rows

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$. For
every natural number $n$, $\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{2n-2k}{n}_2 = 2^n$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 19 (`jis-2025-25.3.5-thm-19`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_two_mul_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-two-mul-sub).

## Vandermonde convolution for trinomial coefficients

Write $\binom{n}{k}_2$ for the
trinomial coefficient, the coefficient of $t^k$ in $(1 + t + t^2)^n$, and put $\binom{n}{k}_2 = 0$
for negative integers $k$. Then for all natural numbers $n$, $m$ and every integer $l$,

$$\sum_{k=0}^{2m} \binom{n}{l + k}_2 \binom{m}{k}_2 = \binom{n + m}{2m + l}_2.$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 20 (`jis-2025-25.3.5-thm-20`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_convolution` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-convolution).

## Alternating sum of squared trinomial coefficients

Write $\binom{n}{k}_2$ for the
trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$. For every natural number $n$,
$\sum_{k=0}^{2n} (-1)^k \binom{n}{k}_2^2 = \binom{n}{n}_2$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 24 (`jis-2025-25.3.5-thm-24`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_sq_alternating` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-sq-alternating).

## Sums of squares and products of trinomial coefficients with even index

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. For
every $n \in \mathbb{N}$ let $c_n = \binom{n}{n/2}_2$ if $n$ is even and $c_n = 0$ if $n$ is odd.
Then

$$\sum_{k=0}^{n} \binom{n}{2k}_2^2 = \frac{1}{2}\binom{2n}{2n}_2 + \frac{1}{2}\binom{n}{n}_2$$

and

$$\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{n-2k}_2 \binom{n}{2k}_2 =
\frac{1}{2}\binom{2n}{n}_2 + \frac{1}{2} c_n.$$

For odd $n$ the paper's $\binom{n}{n/2}_2$ is read as $0$: the floor reading fails, e.g. at
$n = 1$ the left side is $1$ while $\frac{1}{2}\binom{2}{1}_2 + \frac{1}{2}\binom{1}{0}_2 = 3/2$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 26 (`jis-2025-25.3.5-thm-26`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_even_sq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-even-sq).

## Absorption identity for trinomial coefficients

Write $\binom{n}{k}_2$ for the
trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$. For natural numbers $n \ge 1$
and $k$, $\frac{k}{n} \binom{n}{k}_2 = \binom{n-1}{k-1}_2 + 2 \binom{n-1}{k-2}_2$, where a term
whose lower index is negative is read as $0$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Lemma 31 (`jis-2025-25.3.5-lem-31`).

Stated but not proved: `MetaMathlibExt.trinomialCoefficient_absorption` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-coefficient-absorption).

## Weighted diagonal sums of trinomial coefficients by coefficient extraction

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$,
$[t^m]\,g$ for the coefficient of $t^m$ in a power series $g$, and $f_k = [t^k]\,f$. For every
integer $n > 0$ and every formal power series $f \in \mathbb{Q}[[t]]$

$$\sum_{k=0}^{\lfloor 2n/3 \rfloor} \binom{n-k}{k}_2 \frac{n}{n-k} f_k =
[t^{2n}]\, \frac{(1-t+t^2)^{n-1}(3-4t+2t^2)}{1-t}\,
f\!\left(\frac{t^3}{(1-t+t^2)(1-t)}\right).$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 32 (`jis-2025-25.3.5-thm-32`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_diagonal_weighted` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-diagonal-weigh).

## Alternating weighted diagonal sum of trinomial coefficients

Write $\binom{n}{k}_2$ for
the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. For every integer $n > 0$
let $S_n = \sum_{k=0}^{\lfloor 2n/3 \rfloor} \binom{n-k}{k}_2 \frac{n}{n-k} (-1)^k$, a rational
number. Then $S_n = 1$ if $n \equiv 1$ or $n \equiv 3 \pmod 4$, $S_n = -1$ if
$n \equiv 2 \pmod 4$, and $S_n = 3$ if $n \equiv 0 \pmod 4$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 35 (`jis-2025-25.3.5-cor-35`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_diagonal_alternating` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-diagonal-alter).

## Generating sum of the upper half of a trinomial row

Write $\binom{n}{k}_2$ for the
trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$. For every natural number $n$
and every complex number $w$,

$$\sum_{k=0}^{n} \binom{n}{n-k}_2 w^{n+k} = \frac{(1+w+w^2)^n}{2} + \frac{\binom{n}{n}_2 w^n}{2} +
\frac{w^2-1}{2} \sum_{k=0}^{n-1} \binom{k}{k}_2 (1+w+w^2)^{n-1-k} w^k.$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 40 (`jis-2025-25.3.5-cor-40`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_upper_half` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-upper-half).

## Trinomial coefficients along lines from a square-root series

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$, and
$[t^m]\,F$ for the coefficient of $t^m$ in a formal power series $F$ over $\mathbb{Q}$. Let $S$
be a power series over $\mathbb{Q}$ with $S^2 = 1 - 2t - 3t^2$ and $S(0) = 1$. For natural
numbers $n, a, b, k$ with $2a \le b$,
$2^{(b-a)k} \binom{n+ak}{n+bk}_2 = [t^{n+bk}]\, S^{-1} (1 - t - S)^{(b-a)k}$.

Equivalently $\binom{n+ak}{n+bk}_2 = [t^n]\, S^{-1}
\left((1 - t - S)^{b-a} / (2^{b-a} t^b)\right)^k$, the paper's form, which allows integers
$a$ and $b$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 38 (`jis-2025-25.3.5-thm-38`).

Stated but not proved: `MetaMathlibExt.trinomialCoefficient_eq_coeff_sqrt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-coefficient-eq-coeff-sqrt).

## Inversion of an implicit Riordan array sum

Write $[t^m]F$ for the coefficient of $t^m$
in a power series $F$ and $F'$ for its formal derivative. Let $K$ be a field and let $f$,
$\psi$, $g$, $b$ be power series over $K$ with $f(0) \ne 0$, $\psi(0) \ne 0$ and $g(0) \ne 0$.
Put $h(t) = t\,g(t)$ and, for $m \in \mathbb{N}$, $a_m = [t^m]\,f(t)\,\psi(t)^m\,b(h(t))$. Then
for every $n \in \mathbb{N}$,

$$[t^n]\,b = \sum_{k=0}^{n} \left([t^{n-k}]\,
\frac{(\psi - t\psi')\,h'}{f\,\psi^{k+1}\,g^{n+1}}\right) a_k.$$

The paper writes the factor $1/g^{n+1}$ as $t^{n+1}/h(t)^{n+1}$ and does not state the
hypothesis $f(0) \ne 0$, which $1/f$ needs.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 47 (`jis-2025-25.3.5-thm-47`).

Stated but not proved: `MetaMathlibExt.implicit_riordan_sum_inverse` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#implicit-riordan-sum-inverse).

## Sprugnoli's binomial sum theorem

Write $[t^j]F$ for the coefficient of $t^j$ in a power
series $F$ over $\mathbb{C}$, $\binom{u}{j}$ for the generalized binomial coefficient, and
$(1 + t)^u = \sum_{j \ge 0} \binom{u}{j} t^j$ for the binomial series of a complex number $u$.
Let $f$ be a power series over $\mathbb{C}$. For natural numbers $n$, $x$, $a$, $b$ with
$a < b$,

$$\sum_{k=0}^{n} \binom{n + ak}{x + bk} [t^k]\,f =
[t^n]\,\frac{t^x}{(1 - t)^{x+1}}\, f\!\left(\frac{t^{b-a}}{(1 - t)^b}\right),$$

and for natural numbers $m$, $c$ with $c > 0$, every complex $y$ and every integer $a'$,

$$\sum_{k=0}^{\lfloor m/c \rfloor} \binom{y + a'k}{m - ck} [t^k]\,f =
[t^m]\,(1 + t)^y f\!\left(t^c (1 + t)^{a'}\right).$$

In the first sum the terms with $k > n$ would vanish, and the second stops where the lower
index $m - ck$ would become negative. The paper allows integer $x$ and $a$ in the first
identity and writes the second with $b = -c < 0$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 2 (`jis-2025-25.3.5-thm-2`).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_coeff_eq_coeff_subst` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-choose-mul-coeff-eq-coeff-subst).

## Trinomial coefficients from an algebraic Riordan array

Write $\binom{n}{k}_2$ for the
trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$, and $[t^m]\,F$ for the
coefficient of $t^m$ in a formal power series $F$ over $\mathbb{Q}$. Let $S$ and $Q$ be power
series over $\mathbb{Q}$ with $S^2 = 4 - 3t^2$, $S(0) = 2$, $2Q^2 = 2 - t^2 - tS$ and $Q(0) = 1$,
and put

$$\alpha = \frac{-2\,(2Q + t^2 S - t)}{Q\,(3t^4 + 2tS - t^2 - 4)}, \qquad
\beta = \frac{t\,(t + S)}{2\,(1 - t^2)}.$$

Then $\binom{n}{k}_2 = [t^{2n}]\,\alpha\,\beta^k$ for all natural numbers $n$ and $k$.

In the paper $S = \sqrt{4 - 3t^2}$ and $\sqrt{2}\,Q = \sqrt{2 - t^2 - t\sqrt{4 - 3t^2}}$; since
$\sqrt{8 - 6t^2} = \sqrt{2}\,S$, the factors $\sqrt{2}$ in its formula for $\alpha$ cancel.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 6 (`jis-2025-25.3.5-thm-6`).

Stated but not proved: `MetaMathlibExt.trinomialCoefficient_eq_coeff_alpha_mul_beta_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#trinomial-coefficient-eq-coeff-alpha-mul).

## Sums of trinomial coefficients along lines by coefficient extraction

Write $[t^j]\,g$
for the coefficient of $t^j$ in a power series $g$, and $f_k = [t^k]\,f$. For $n \in \mathbb{N}$
let $\binom{n}{j}_2 = [t^j]\,(1+t+t^2)^n$ be the trinomial coefficient. For complex $u$ and $z$
let $(1 + zt + z^2t^2)^u$ be the binomial series $\sum_{i \ge 0} \binom{u}{i} (zt + z^2t^2)^i$,
and for complex $u$ let $\binom{u}{j}_2 = [t^j]\,(1+t+t^2)^u$. Let $n, x, a, b, m, c$ be natural
numbers with $2a < b$ and $c > 0$, let $y, z \in \mathbb{C}$, let $a'$ be an integer and let
$f \in \mathbb{C}[[t]]$. Then

$$\sum_{k=0}^{2n} \binom{n+ak}{x+bk}_2 z^{2(n+ak)-(x+bk)} f_k =
[t^{2n}]\, (1-zt+z^2t^2)^n \frac{t^x}{(1-zt)^{x+1}}\,
f\!\left(\frac{t^{b-2a} (1-zt+z^2t^2)^a}{(1-zt)^b}\right),$$

where a term with $x + bk > 2(n+ak)$ is $0$ because its trinomial coefficient is, and

$$\sum_{k=0}^{\lfloor m/c \rfloor} \binom{y+a'k}{m-ck}_2 z^{m-ck} f_k =
[t^m]\, (1+zt+z^2t^2)^y\, f\big(t^c (1+zt+z^2t^2)^{a'}\big).$$

The paper allows integers $x$ and $a$ in the first identity and obtains the second as the case
$b = -c < 0$; $\binom{u}{j}_2$ for complex $u$ is Comtet's extension (the paper's Eq. (8)).

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 7 (`jis-2025-25.3.5-thm-7`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_mul_coeff_eq_coeff_subst` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-mul-coeff-eq-c).

## Gould-type identities for binomial and extended trinomial coefficients

For complex $u$
and $j \in \mathbb{N}$ write $\binom{u}{j}$ for the generalized binomial coefficient and
$\binom{u}{j}_2$ for the coefficient of $t^j$ in
$(1 + t + t^2)^u = \sum_{i \ge 0} \binom{u}{i}(t + t^2)^i$ (Comtet's extension). Then for all
complex $x$, $y$ and every $n \in \mathbb{N}$,

$$\sum_{k=0}^{\lfloor n/3 \rfloor} \binom{x}{k}\binom{y - 3x}{n - 3k} =
\sum_{k=0}^{n} \binom{x}{k}\binom{y - 2k}{n - k}(-3)^k$$

and

$$\sum_{k=0}^{\lfloor n/3 \rfloor} \binom{-x}{n - 3k}_2 \binom{x}{k}(-1)^k = (-1)^n \binom{x}{n}.$$

The paper's Eq. (25) also equates the first two sums with
$\sum_k \binom{2x}{n-k}_2 \binom{y-2x}{k}(-1)^{n-k}$; that expression is left out because it is
false as printed: at $x = 2$, $y = 1/3$, $n = 1$ it equals $-23/3$, while both sides of the
first identity equal $-17/3$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 21 (`jis-2025-25.3.5-thm-21`).

Stated but not proved: `MetaMathlibExt.sum_choose_gould_and_extended_trinomial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-choose-gould-and-extended-trinomial).

## An alternating convolution of extended trinomial coefficients

For complex $u$ and
$j \in \mathbb{N}$ write $\binom{u}{j}_2$ for the coefficient of $t^j$ in
$(1 + t + t^2)^u = \sum_{i \ge 0} \binom{u}{i}(t + t^2)^i$ (Comtet's extension), where
$\binom{u}{i}$ is the generalized binomial coefficient. Then for every complex $x$ and every
$n \in \mathbb{N}$,

$$\sum_{k=0}^{n} \binom{2n - x}{n - k}_2 \binom{x}{k}_2 (-1)^k =
\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{2n - 2x}{n - 2k}_2 \binom{x}{k}_2.$$

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 23 (`jis-2025-25.3.5-thm-23`).

Stated but not proved: `MetaMathlibExt.sum_extended_trinomial_alternating_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-extended-trinomial-alternating-eq).

## Tribonacci numbers from every third term of A077943

Let $T_n$ be the Tribonacci
numbers, $T_0 = T_1 = 0$, $T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$. Let
$(y_n)_{n \ge 0}$ be a sequence of integers with $y_0 = y_1 = 0$, $y_2 = 1$ and
$y_{n+3} = 2y_{n+2} - 2y_{n+1} + 2y_n$ for all $n \ge 0$ (the sequence A077943). Then for
every $n \ge 0$, $2^{n+1} T_{n+2} = y_{3(n+1)}$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 27 (`jis-2025-25.3.5-thm-27`).

Stated but not proved: `MetaMathlibExt.two_pow_mul_tribonacci_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#two-pow-mul-tribonacci-eq).

## Binet-type formula for diagonal sums of trinomial coefficients

Write $\binom{n}{k}_2$
for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. Let $z, w \in \mathbb{C}$
and let $r_1, r_2, r_3 \in \mathbb{C}$ be pairwise distinct with $r_1 + r_2 + r_3 = 2w$,
$r_1 r_2 + r_1 r_3 + r_2 r_3 = 2w^2$ and $r_1 r_2 r_3 = z + w^3$, that is, let $r_1, r_2, r_3$
be the three distinct zeros of $t^3 - 2wt^2 + 2w^2 t - (z + w^3)$. Then for every
$n \in \mathbb{N}$

$$\sum_{k=0}^{\lfloor 2n/3 \rfloor} \binom{n-k}{k}_2 w^{2n-3k} z^k =
\sum_{i=1}^{3} \frac{(w^2 - w r_i + r_i^2)^{n+1}}{\prod_{j \ne i} (r_i - r_j)}.$$

The paper names the zeros $\alpha_{z,w}, \beta_{z,w}, \bar\beta_{z,w}$ by Cardano's formulas; the
right side is symmetric, so they are given here by Vieta's relations.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Theorem 28 (`jis-2025-25.3.5-thm-28`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_diagonal_binet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-diagonal-binet).

## Weighted diagonal sums of trinomial coefficients and the sequence A075115

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $x^k$ in $(1+x+x^2)^n$. Let
$(\lambda_m)$ be the integer sequence with $\lambda_0 = 3$, $\lambda_1 = 2$, $\lambda_2 = 0$ and
$\lambda_{m+3} = 2\lambda_{m+2} - 2\lambda_{m+1} + 2\lambda_m$ (OEIS A075115). For every natural
number $n \ge 1$,
$2^n \sum_{k=0}^{\lfloor 2n/3 \rfloor} \binom{n-k}{k}_2 \frac{n}{n-k} = \lambda_{3n}$.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 33 (`jis-2025-25.3.5-cor-33`).

Stated but not proved: `MetaMathlibExt.two_pow_mul_sum_trinomialCoefficient_diagonal_weighted` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#two-pow-mul-sum-trinomial-coefficient-di).

## Power-sum formula for weighted diagonal sums of trinomial coefficients

Write
$\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in $(1+t+t^2)^n$. Let
$z, w \in \mathbb{C}$ and let $r_1, r_2, r_3 \in \mathbb{C}$ satisfy $r_1 + r_2 + r_3 = 2w$,
$r_1 r_2 + r_1 r_3 + r_2 r_3 = 2w^2$ and $r_1 r_2 r_3 = z + w^3$, that is, let $r_1, r_2, r_3$
be the zeros, with multiplicity, of $t^3 - 2wt^2 + 2w^2 t - (z + w^3)$. Then for every integer
$n > 0$

$$\sum_{k=0}^{\lfloor 2n/3 \rfloor} \binom{n-k}{k}_2 \frac{n}{n-k} w^{2n-3k} z^k =
(w^2 - w r_1 + r_1^2)^n + (w^2 - w r_2 + r_2^2)^n + (w^2 - w r_3 + r_3^2)^n.$$

The zeros (Cardano's $\alpha_{z,w}, \beta_{z,w}, \bar\beta_{z,w}$ in the paper) are given by
Vieta's relations.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 36 (`jis-2025-25.3.5-cor-36`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_diagonal_weighted_power_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-diagonal-weigh-2).

## Tribonacci formula for a diagonal sum of trinomial coefficients

Write $\binom{n}{k}_2$ for the trinomial coefficient, the coefficient of $t^k$ in
$(1 + t + t^2)^n$, and $T_n$ for the Tribonacci numbers, $T_0 = T_1 = 0$, $T_2 = 1$ and
$T_{n+3} = T_{n+2} + T_{n+1} + T_n$. Then for every $n \in \mathbb{N}$,

$$\sum_{k=0}^{n} \binom{n + k}{n - k}_2 = \frac{T_{2(n+1)}}{2} + \frac{1}{2}\binom{n}{n}_2 +
\frac{1}{2} \sum_{k=0}^{n-1} \binom{k}{k}_2 \left(T_{2(n-k)} + T_{2(n-1-k)}\right).$$

The sequence $(T_{2n})$ is the bisection A099463.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 42 (`jis-2025-25.3.5-cor-42`).

Stated but not proved: `MetaMathlibExt.sum_trinomialCoefficient_add_sub_eq_tribonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#sum-trinomial-coefficient-add-sub-eq-tri).

## Recovering even coefficients from the 2-Pascal transform

Write $[t^m]F$ for the
coefficient of $t^m$ in a power series $F$. Let $S$, $Q$, $R$ be power series over $\mathbb{Q}$
with $S^2 = 4 - 3t^2$, $S(0) = 2$, $2Q^2 = 2 - t^2 - tS$, $Q(0) = 1$, $R^2 = 1 - t + t^2$ and
$R(0) = 1$, and put

$$\alpha = \frac{-2(2Q + t^2 S - t)}{Q(3t^4 + 2tS - t^2 - 4)}, \qquad
\beta = \frac{t(t + S)}{2(1 - t^2)}.$$

For a power series $f$ over $\mathbb{Q}$ let $g(t) = \alpha(t)\,f(\beta(t))$. Then for every
$n \in \mathbb{N}$,

$$[t^{2n}]\,f = [t^{2n}]\,\frac{(2 - t)(1 - t)^{2n}}{2(1 - t + t^2)}\,g\!\left(\frac{t}{R}\right).$$

Here $S$, $Q$, $R$ are the square roots $\sqrt{4 - 3t^2}$, $\sqrt{(2 - t^2 - tS)/2}$ and
$\sqrt{1 - t + t^2}$, and $\alpha$, $\beta$ are the series of the paper's Theorem 6.

## Sources

- Yassine Otmani, *The 2-Pascal Triangle and a Related Riordan Array*, Journal of Integer Sequences 28 (2025), Article 25.3.5, Corollary 49 (`jis-2025-25.3.5-cor-49`).

Stated but not proved: `MetaMathlibExt.coeff_two_mul_eq_inverse_trinomial_transform` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPascalTriangleWanted.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html#coeff-two-mul-eq-inverse-trinomial-trans).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trinomial coefficients and the 2-Pascal triangle](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/trinomial-coefficients-and-the-2-pascal-triangle)
