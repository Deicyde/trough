---
declaration: section
origin: cited
lean: MetaMathlibExt.IsComplementaryPair, MetaMathlibExt.SatisfiesParametrizedSumEquation, MetaMathlibExt.SatisfiesBaseSumEquation, MetaMathlibExt.SatisfiesShiftedSumEquation, MetaMathlibExt.IsComplementaryDeterminedByParametrizedSumEquation, MetaMathlibExt.IsComplementaryDeterminedByBaseSumEquation, MetaMathlibExt.IsComplementaryDeterminedByShiftedSumEquation, MetaMathlibExt.nthNonValue
statement: formalized
---

# Complementary sequences

32 results, 10 proved and 22 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html).

## Complementary pair of sequences

Two sequences $a, b : \mathbb{N} \to \mathbb{N}$, indexed
from $0$, form a complementary pair when all their terms are positive, both are strictly
increasing, no term of $a$ equals a term of $b$, and every positive integer is a term of $a$ or
a term of $b$. In particular, the ranges of $a$ and $b$ partition the positive integers.

Formalized by `MetaMathlibExt.IsComplementaryPair`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#is-complementary-pair).

## The subsequence-sum equation $a_n = b_{hn} + b_{khn}$

Sequences
$a, b : \mathbb{N} \to \mathbb{N}$ and natural numbers $h$ and $k$ satisfy the parametrized
subsequence-sum equation when $h \ge 2$, $k \ge 2$, $b_0 = 1$, and $a_n = b_{hn} + b_{khn}$ for
every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.SatisfiesParametrizedSumEquation`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#satisfies-parametrized-sum-equation).

## The subsequence-sum equation $a_n = b_{2n} + b_{4n}$

Sequences
$a, b : \mathbb{N} \to \mathbb{N}$ satisfy this equation when $b_0 = 1$ and
$a_n = b_{2n} + b_{4n}$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.SatisfiesBaseSumEquation`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#satisfies-base-sum-equation).

## The subsequence-sum equation $a_n = b_{2n} + b_{4n} + 1$

Sequences
$a, b : \mathbb{N} \to \mathbb{N}$ satisfy this equation when $b_0 = 1$ and
$a_n = b_{2n} + b_{4n} + 1$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.SatisfiesShiftedSumEquation`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#satisfies-shifted-sum-equation).

## Complementary pair determined by $a_n = b_{hn} + b_{khn}$

Sequences
$a, b : \mathbb{N} \to \mathbb{N}$ form a complementary pair determined by this equation with
natural-number parameters $h$ and $k$ when they form a complementary pair (both strictly
increasing with positive terms, and every positive integer is a term of exactly one of them),
$h \ge 2$, $k \ge 2$, $b_0 = 1$, and $a_n = b_{hn} + b_{khn}$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsComplementaryDeterminedByParametrizedSumEquation`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#is-complementary-determined-by-parametri).

## Complementary pair determined by $a_n = b_{2n} + b_{4n}$

Sequences
$a, b : \mathbb{N} \to \mathbb{N}$ form a complementary pair determined by this equation when they
form a complementary pair (both strictly increasing with positive terms, and every positive
integer is a term of exactly one of them) and they satisfy $b_0 = 1$ and $a_n = b_{2n} + b_{4n}$
for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsComplementaryDeterminedByBaseSumEquation`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#is-complementary-determined-by-base-sum).

## Complementary pair determined by $a_n = b_{2n} + b_{4n} + 1$

Sequences
$a, b : \mathbb{N} \to \mathbb{N}$ form a complementary pair determined by this equation when they
form a complementary pair (both strictly increasing with positive terms, and every positive
integer is a term of exactly one of them) and they satisfy $b_0 = 1$ and
$a_n = b_{2n} + b_{4n} + 1$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsComplementaryDeterminedByShiftedSumEquation`, a definition declared in [MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ComplementarySequenceDeterminedBySubsequenceSumEquation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#is-complementary-determined-by-shifted-s).

## The $n$-th non-value of a sequence

For $f : \mathbb{N} \to \mathbb{N}$ and $n \ge 1$, the
$n$-th non-value of $f$ is the $n$-th smallest positive integer that is not of the form $f(m)$
with $m \ge 1$, or $0$ if fewer than $n$ such integers exist. At $n = 0$ it takes the same value
as at $n = 1$.

In the paper's notation, where $f = f_{\neg P}$ lists the positive integers without a property
$P$, the $n$-th non-value of $f$ is $f_P(n)$, the $n$-th term of the complementary sequence.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Section 1 (definition of `f_P`).

Formalized by `MetaMathlibExt.nthNonValue`, a definition declared in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value).

## The first non-square

The smallest positive integer that is not the square of a positive
integer is $2$; that is, the first non-value of $m \mapsto m^2$ is $2$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Section 1 (the non-squares).

Formalized by `MetaMathlibExt.nthNonValue_sq_one`, a theorem declared in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-sq-one).

## The second non-square

The second smallest positive integer that is not the square of a
positive integer is $3$; that is, the second non-value of $m \mapsto m^2$ is $3$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Section 1 (the non-squares).

Formalized by `MetaMathlibExt.nthNonValue_sq_two`, a theorem declared in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-sq-two).

## Complementary sequences in two Lambek–Moser steps

Let $f : \mathbb{N} \to \mathbb{N}$
satisfy $f(1) \ge 1$ and $f(m + 1) \ge f(m) + m$ for all $m \ge 1$, let $C(x)$ be the number of
$m$ with $1 \le m \le x$ and $f(m) \le x$, and for $n \ge 1$ let $f_P(n)$ be the $n$-th positive
integer that is not a value $f(m)$ with $m \ge 1$. Then $f_P(n) = n + C(n + C(n))$ for every
$n \ge 1$.

Under the hypotheses, $f(m) \ge m$ for all $m \ge 1$, so $C(x)$ is the number of all $m \ge 1$
with $f(m) \le x$, the counting function of the values of $f$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 1.

Stated but not proved: `MetaMathlibExt.nthNonValue_eq_two_step` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-eq-two-step).

## Complementary sequences from one evaluation of the counting function

Let
$f : \mathbb{N} \to \mathbb{N}$ satisfy $f(1) \ge 1$ and $f(m + 1) \ge f(m) + m$ for all
$m \ge 1$, let $C(x)$ be the number of $m$ with $1 \le m \le x$ and $f(m) \le x$, and for
$n \ge 1$ let $f_P(n)$ be the $n$-th positive integer that is not a value $f(m)$ with $m \ge 1$.
Then for every $n \ge 1$, $f_P(n) = n + C(n) + 1$ if $f(C(n) + 1) \le n + C(n)$, and
$f_P(n) = n + C(n)$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 2.

Stated but not proved: `MetaMathlibExt.nthNonValue_eq_one_step` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-eq-one-step).

## Complementary sequences from an interleaving function

Let
$f : \mathbb{N} \to \mathbb{N}$ satisfy $f(1) \ge 1$ and $f(m + 1) \ge f(m) + m$ for all $m \ge 1$,
and for $n \ge 1$ let $f_P(n)$ be the $n$-th positive integer that is not a value $f(m)$ with
$m \ge 1$. Let $\alpha : \mathbb{N} \to \mathbb{R}$ satisfy $f(m - 1) \le \alpha(m) \le f(m)$ for
all $m \ge 2$, and let $h : \mathbb{N} \to \mathbb{N}$ satisfy $h(n) \ge 1$ and
$\alpha(h(n)) \le n < \alpha(h(n) + 1)$ for all $n \ge 1$.
Then for every $n \ge 1$, $f_P(n) = n + h(n) + 1$ if $f(h(n) + 1) \le n + h(n)$; otherwise
$f_P(n) = n + h(n) - 1$ if $n + h(n) \le f(h(n))$, and $f_P(n) = n + h(n)$ if not.

For increasing $\alpha$ with $\alpha(1) = 1$, the paper's choice of $h(n)$ as the largest
$m \ge 1$ with $\alpha(m) \le n$ satisfies the hypothesis on $h$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 3.

Stated but not proved: `MetaMathlibExt.nthNonValue_eq_interleave` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-eq-interleave).

## Interleaving formula when $f(m) - \alpha(m) < m$

Let
$f : \mathbb{N} \to \mathbb{N}$ satisfy $f(1) \ge 1$ and $f(m + 1) \ge f(m) + m$ for all $m \ge 1$,
and for $n \ge 1$ let $f_P(n)$ be the $n$-th positive integer that is not a value $f(m)$ with
$m \ge 1$. Let $\alpha : \mathbb{N} \to \mathbb{R}$ satisfy $f(m - 1) \le \alpha(m) \le f(m)$ for
all $m \ge 2$, and let $h : \mathbb{N} \to \mathbb{N}$ satisfy $h(n) \ge 1$ and
$\alpha(h(n)) \le n < \alpha(h(n) + 1)$ for all $n \ge 1$.
Suppose moreover that $f(m) - \alpha(m) < m$ for all $m \ge 1$. Then for every $n \ge 1$,
$f_P(n) = n + h(n) + 1$ if $f(h(n) + 1) \le n + h(n)$, and $f_P(n) = n + h(n)$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Corollary 1.

Stated but not proved: `MetaMathlibExt.nthNonValue_eq_interleave_of_sub_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-eq-interleave-of-sub-lt).

## Interleaving formula when $f(m) - \alpha(m) \ge m$

Let
$f : \mathbb{N} \to \mathbb{N}$ satisfy $f(1) \ge 1$ and $f(m + 1) \ge f(m) + m$ for all $m \ge 1$,
and for $n \ge 1$ let $f_P(n)$ be the $n$-th positive integer that is not a value $f(m)$ with
$m \ge 1$. Let $\alpha : \mathbb{N} \to \mathbb{R}$ satisfy $f(m - 1) \le \alpha(m) \le f(m)$ for
all $m \ge 2$, and let $h : \mathbb{N} \to \mathbb{N}$ satisfy $h(n) \ge 1$ and
$\alpha(h(n)) \le n < \alpha(h(n) + 1)$ for all $n \ge 1$.
Suppose moreover that $f(m) - \alpha(m) \ge m$ for all $m \ge 2$. Then for every $n \ge 1$,
$f_P(n) = n + h(n)$ if $f(h(n)) < n + h(n)$, and $f_P(n) = n + h(n) - 1$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Corollary 2.

Stated but not proved: `MetaMathlibExt.nthNonValue_eq_interleave_of_le_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-eq-interleave-of-le-sub).

## Formula for the $n$-th non-triangular number

For every integer $n \ge 1$, the $n$-th
smallest positive integer that is not a triangular number $j(j+1)/2$ with $j \ge 1$ is
$n + \lfloor \sqrt{2n} + 1/2 \rfloor$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Corollary 3.

Stated but not proved: `MetaMathlibExt.nthNonValue_triangular_eq_round` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-triangular-eq-round).

## Formula for the non-square numbers

For every integer $n \ge 1$, the $n$-th positive
integer that is not a perfect square is $n + \lfloor \sqrt{n} + 1/2 \rfloor$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Corollary 3.

Stated but not proved: `MetaMathlibExt.nthNonValue_sq_eq_round` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-sq-eq-round).

## Formula for the non-polygonal numbers

Let $k \ge 3$, and for $j \ge 1$ let
$T(k, j) = (k - 2) j (j - 1)/2 + j$ be the $k$-gonal numbers. For every integer $n \ge 1$, put
$s = \lfloor \sqrt{2n/(k - 2)} \rfloor$. Then the $n$-th positive integer that is not of the form
$T(k, j)$ with $j \ge 1$ equals $n + s + 1$ if $(k - 2) s (s + 1) < 2n$, and $n + s$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 4, Equation (3).

Stated but not proved: `MetaMathlibExt.nthNonValue_polygonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-polygonal).

## Rounding formula for the non-$k$-gonal numbers, $3 \le k \le 10$

Let $3 \le k \le 10$;
the $k$-gonal numbers are $(k - 2) j (j - 1)/2 + j$ for $j \ge 1$. For every $n \ge 1$, the $n$-th
positive integer that is not a $k$-gonal number equals
$n + \lfloor \sqrt{2n/(k - 2)} + 1/2 \rfloor$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 4 (last sentence).

Stated but not proved: `MetaMathlibExt.nthNonValue_polygonal_eq_round` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-polygonal-eq-round).

## Shifted formula for the non-polygonal numbers

Let $k \ge 3$, let $r$ be a real number
with $-1 \le r \le k - 4$, and for $j \ge 1$ let $T(k, j) = (k - 2) j (j - 1)/2 + j$ be the
$k$-gonal numbers. For every integer $n \ge 1$, put $s = \lfloor \sqrt{(2n + r)/(k - 2)} \rfloor$.
Then the $n$-th positive integer that is not of the form $T(k, j)$ with $j \ge 1$ equals
$n + s + 1$ if $(k - 2) s (s + 1) < 2n$, and $n + s$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 5, Equation (4).

Stated but not proved: `MetaMathlibExt.nthNonValue_polygonal_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-polygonal-shift).

## Rounding formula for the non-$k$-gonal numbers, every $k \ge 3$

Let $k \ge 3$; the
$k$-gonal numbers are $(k - 2) j (j - 1)/2 + j$ for $j \ge 1$. For every $n \ge 1$, the $n$-th
positive integer that is not a $k$-gonal number equals
$n + \lfloor \sqrt{(2n - 2 + \lfloor (k + 1)/4 \rfloor)/(k - 2)} + 1/2 \rfloor$.

This corresponds to the shift $r = \lfloor (k + 1)/4 \rfloor - 2$ in the source.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 5 (last sentence).

Stated but not proved: `MetaMathlibExt.nthNonValue_polygonal_eq_round_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-polygonal-eq-round-shift).

## Formula for the non-second-pentagonal numbers

For every integer $n \ge 1$, put
$s = \lfloor \sqrt{2n/3} \rfloor$. Then the $n$-th positive integer that is not a second
pentagonal number $(3j^2 + j)/2$ with $j \ge 1$ equals $n + s + 1$ if $s (3s + 5) + 4 \le 2n$, and
$n + s$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 6.

Stated but not proved: `MetaMathlibExt.nthNonValue_secondPentagonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-second-pentagonal).

## Formula for the non-second-polygonal numbers

Let $k > 5$, and for $j \ge 1$ let
$S(k, j) = ((k - 2) j^2 + (k - 4) j)/2$ be the second $k$-gonal numbers. For every integer
$n \ge 1$, put $s = \lfloor \sqrt{2n/(k - 2)} \rfloor$. Then the $n$-th positive integer that is
not of the form $S(k, j)$ with $j \ge 1$ equals $n + s$ if $(k - 2) s (s + 1) < 2n + 4s$, and
$n + s - 1$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 7, Equation (5).

Stated but not proved: `MetaMathlibExt.nthNonValue_secondPolygonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-second-polygonal).

## Non-centered polygonal numbers

Let $k \ge 3$; the centered $k$-gonal numbers are
$k j (j + 1)/2 + 1$ for $j \ge 0$. For $n \ge 1$ let $a(n)$ be the $n$-th nonnegative integer that
is not a centered $k$-gonal number (so $a(1) = 0$), and let $s = \lfloor \sqrt{2n/k} \rfloor$.
Then $a(n) = n + s$ if $k s (s + 1) < 2(n + s - 1)$, and $a(n) = n + s - 1$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 8.

Stated but not proved: `MetaMathlibExt.nth_nonCenteredPolygonal` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-centered-polygonal).

## Formula for the non-pyramidal numbers

Let $3 \le k \le 8$, and for $j \ge 1$ let
$P(k, j) = j (j + 1) ((k - 2) j - (k - 5))/6$ be the $k$-gonal pyramidal numbers. For every
integer $n \ge 1$, put $s = \lfloor \sqrt[3]{6n/(k - 2)} \rfloor$. Then the $n$-th positive
integer that is not of the form $P(k, j)$ with $j \ge 1$ equals $n + s + 1$ if
$6n \ge s^3 (k - 2) + 3 s^2 (k - 1) + s (2k - 1) + 6$; otherwise it equals $n + s - 1$ if
$6n \le s (s - 1) (s (k - 2) + k + 1)$, and $n + s$ if not.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 9, Equation (6).

Stated but not proved: `MetaMathlibExt.nthNonValue_pyramidal` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-pyramidal).

## Two-case formula for the non-pyramidal numbers when $k \le 5$

Let $3 \le k \le 5$, and
for $j \ge 1$ let $P(k, j) = j (j + 1) ((k - 2) j - (k - 5))/6$ be the $k$-gonal pyramidal
numbers. For every integer $n \ge 1$, put $s = \lfloor \sqrt[3]{6n/(k - 2)} \rfloor$. Then the
$n$-th positive integer that is not of the form $P(k, j)$ with $j \ge 1$ equals $n + s - 1$ if
$6n \le s (s - 1) (s (k - 2) + k + 1)$, and $n + s$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Corollary 4, Equation (7).

Stated but not proved: `MetaMathlibExt.nthNonValue_pyramidal_two_case` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-pyramidal-two-case).

## Two-case formula for the non-pyramidal numbers when $k \le 8$

Let $3 \le k \le 8$, and
for $j \ge 1$ let $P(k, j) = j (j + 1) ((k - 2) j - (k - 5))/6$ be the $k$-gonal pyramidal
numbers. For every integer $n \ge 1$, put $s = \lfloor \sqrt[3]{6n/(k - 2)} \rfloor$. Then the
$n$-th positive integer that is not of the form $P(k, j)$ with $j \ge 1$ equals $n + s - 1$ if
$6n \le s (s - 1) (s (k - 2) + k + 1)$, and $n + s$ otherwise.

This extends Equation (7) of Corollary 4 from $k \le 5$ to $k \le 8$; the paper reports it after
checking small values of $n$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, remark after Corollary 4.

Stated but not proved: `MetaMathlibExt.nthNonValue_pyramidal_two_case_le_eight` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-pyramidal-two-case-le-eigh).

## Integers missed by the sums $1^k + \dots + j^k$

Let $k > 1$ and $n \ge 1$ be integers,
and let $h = \lfloor ((k+1)n)^{1/(k+1)} \rfloor$. Then the $n$-th smallest positive integer that
is not of the form $\sum_{i=1}^{j} i^k$ with $j \ge 1$ is $n + h - 1$ if
$n \le \sum_{i=1}^{h} (i^k - 1)$, and $n + h$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 10 (third equivalent form).

Stated but not proved: `MetaMathlibExt.nthNonValue_sumPow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-sum-pow).

## Integers not of the form $m + 1^k + \cdots + m^k$

Let $k > 1$. For $n \ge 1$ let $a(n)$
be the $n$-th positive integer that is not of the form $m + \sum_{i=1}^m i^k$ with $m \ge 1$, and
let $h = \lfloor ((k + 1) n)^{1/(k+1)} \rfloor$. Then $a(n) = n + h - 1$ if
$n \le \sum_{i=1}^h i^k$, and $a(n) = n + h$ otherwise.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 11 (third equivalent form).

Stated but not proved: `MetaMathlibExt.nthNonValue_add_sumPow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-add-sum-pow).

## Rising factorial between consecutive $k$-th powers

Let $k$ and $n$ be natural numbers,
write $n^{\overline{k}} = n (n + 1) \cdots (n + k - 1)$ for the rising factorial, and let
$r = \lfloor (k^2 - 4k + 6)/4 \rfloor$ if $k$ is even and $r = \lfloor (k^2 - 6k + 11)/4 \rfloor$
if $k$ is odd. If $n \ge r$, then
$(n + \lfloor k/2 \rfloor - 1)^k \le n^{\overline{k}} \le (n + \lfloor k/2 \rfloor)^k$.

Both numerators are positive: $k^2 - 4k + 6 = (k - 2)^2 + 2$ and $k^2 - 6k + 11 = (k - 3)^2 + 2$.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Lemma 1, Equation (8).

Stated but not proved: `MetaMathlibExt.ascFactorial_bounds_half` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#asc-factorial-bounds-half).

## Formula for the non-simplex numbers

Let $k$ satisfy $1 < k \le 5$, $k = 7$ or $k = 9$.
For every integer $n \ge 1$, put $R = \lfloor (k!\, n)^{1/k} \rfloor$ and let
$t = n + R - \lfloor k/2 \rfloor$, an integer. Then the $n$-th positive integer that is not a
$k$-simplex number $\binom{j + k - 1}{k}$ with $j \ge 1$ equals $t + 2$ if
$\binom{R + \lceil k/2 \rceil + 1}{k} \le t + 1$; otherwise it equals $t$ if
$t < \binom{R + \lceil k/2 \rceil}{k}$, and $t + 1$ if not.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Theorem 12, Equation (9).

Stated but not proved: `MetaMathlibExt.nthNonValue_simplex` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-simplex).

## Formula for the non-simplex numbers when $k \le 15$

Let $1 < k \le 15$. For every
integer $n \ge 1$, put $R = \lfloor (k!\, n)^{1/k} \rfloor$ and let
$t = n + R - \lfloor k/2 \rfloor$, an integer. Then the $n$-th positive integer that is not a
$k$-simplex number $\binom{j + k - 1}{k}$ with $j \ge 1$ equals $t + 2$ if
$\binom{R + \lceil k/2 \rceil + 1}{k} \le t + 1$; otherwise it equals $t$ if
$t < \binom{R + \lceil k/2 \rceil}{k}$, and $t + 1$ if not.

## Sources

- Chai Wah Wu, *Algorithms for Complementary Sequences*, INTEGERS 25 (2025), Article A95, Corollary 5.

Stated but not proved: `MetaMathlibExt.nthNonValue_simplex_le_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/ComplementarySequencesWanted.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ComplementarySequencesWanted.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html#nth-non-value-simplex-le-fifteen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complementary sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/complementary-sequences)
