---
declaration: section
origin: cited
lean: MetaMathlibExt.dixon_alternating_cubic_binomial_sum, MetaMathlibExt.extFact, MetaMathlibExt.extFact_of_neg, MetaMathlibExt.extFact_natCast, MetaMathlibExt.invFact, MetaMathlibExt.invFact_of_neg, MetaMathlibExt.invFact_natCast, MetaMathlibExt.invFact_shift
statement: formalized
proof: formalized
---

# Dixon's identity

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html).

## Dixon's alternating cubic binomial sum

For every natural number $n$,
$\sum_{k=0}^{2n} (-1)^k \binom{2n}{k}^3 = (-1)^n \binom{2n}{n} \binom{3n}{2n}$.

Mikić attributes the identity to A. C. Dixon, "On the sum of the cubes of the
coefficients in a certain expansion by the binomial theorem", Messenger of
Mathematics 20 (1891), 79--80. This is the specialization of Dixon's three-parameter
identity in which all three parameters equal $n$; the three-parameter identity is not stated.

## Sources

- Jovan Mikić, "A Method For Examining Divisibility Properties Of Some Binomial Sums", Journal of Integer Sequences 21 (2018), Article 18.8.7, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Mikic/mikic25.tex>, equation (2.0.1), lines 119--124.

Formalized by `MetaMathlibExt.dixon_alternating_cubic_binomial_sum`, a theorem declared in [MathlibExt/Combinatorics/DixonCubicBinomial.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonCubicBinomial.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#dixon-alternating-cubic-binomial-sum).

## Extended factorial

For an integer $n$, the extended factorial of $n$ is the rational
number $n!$ when $n \ge 0$ and $0$ when $n < 0$.

Formalized by `MetaMathlibExt.extFact`, a definition declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#ext-fact).

## The extended factorial vanishes at negative integers

For every integer $n < 0$, the
extended factorial of $n$ is $0$.

Formalized by `MetaMathlibExt.extFact_of_neg`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#ext-fact-of-neg).

## The extended factorial of a natural number

For every natural number $n$, the extended
factorial of $n$ equals the ordinary factorial $n!$.

Formalized by `MetaMathlibExt.extFact_natCast`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#ext-fact-nat-cast).

## Inverse factorial on the integers

For an integer $n$, the inverse factorial of $n$ is
the rational number $1/n!$ when $n \ge 0$ and $0$ when $n < 0$.

Formalized by `MetaMathlibExt.invFact`, a definition declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#inv-fact).

## The inverse factorial vanishes at negative integers

For every integer $n < 0$, the
inverse factorial of $n$ is $0$.

Formalized by `MetaMathlibExt.invFact_of_neg`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#inv-fact-of-neg).

## The inverse factorial at natural numbers

For every natural number $n$, the inverse
factorial of $n$, viewed as an integer, equals $(n!)^{-1}$ in $\mathbb{Q}$.

Formalized by `MetaMathlibExt.invFact_natCast`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#inv-fact-nat-cast).

## Shift identity for the inverse factorial

For every integer $n$, the inverse
factorial of $n$ equals $n + 1$ times the inverse factorial of $n + 1$, as rational numbers.

For $n \ge 0$ this is $1/n! = (n+1)/(n+1)!$. For $n < 0$ both sides are $0$: the inverse
factorial vanishes at negative integers, and the factor $n + 1$ is $0$ at $n = -1$.

Formalized by `MetaMathlibExt.invFact_shift`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#inv-fact-shift).

## Integer binomial coefficient

For an integer $m$ write $m!$ for the extended factorial
and $\frac{1}{m!}$ for the inverse factorial; both are $0$ when $m < 0$. For integers $n$ and
$k$, the integer binomial coefficient is the rational number
$\binom{n}{k} = n! \cdot \frac{1}{k!} \cdot \frac{1}{(n - k)!}$.

These are the source's zero conventions: $\binom{n}{k} = 0$ unless $0 \le k \le n$.

Formalized by `MetaMathlibExt.intBinom`, a definition declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#int-binom).

## Integer binomial coefficients of natural numbers

For natural numbers $k \le n$, the
integer binomial coefficient of $n$ and $k$ equals the ordinary binomial coefficient
$\binom{n}{k}$.

Formalized by `MetaMathlibExt.intBinom_natCast`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#int-binom-nat-cast).

## Integer binomial coefficients vanish at negative lower index

For integers $n$ and
$k$ with $k < 0$, the integer binomial coefficient $\binom{n}{k}$ is $0$.

Formalized by `MetaMathlibExt.intBinom_of_neg_right`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#int-binom-of-neg-right).

## Integer binomial coefficients vanish when the lower index exceeds the upper

For
integers $n < k$, the integer binomial coefficient $\binom{n}{k}$ is $0$.

Formalized by `MetaMathlibExt.intBinom_of_lt`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#int-binom-of-lt).

## Term of Dixon's alternating sum

Write $\binom{n}{m}$ for the integer binomial coefficient
of integers $n$ and $m$. For integers $a_1, a_2, a_3$ and $k$, the Dixon summand is the rational
number $(-1)^k \binom{2a_1}{a_1 + k} \binom{2a_2}{a_2 + k} \binom{2a_3}{a_3 + k}$.

Formalized by `MetaMathlibExt.dixonSummand`, a definition declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#dixon-summand).

## Bound of the Dixon summation window

For integers $a_1, a_2, a_3$, the Dixon bound is
$\max(|a_1|, |a_2|, |a_3|)$.

Every integer $k$ whose term in Dixon's alternating sum is nonzero satisfies $|k|$ at most this
bound, so summing over $k$ from minus the bound to the bound covers the whole sum.

Formalized by `MetaMathlibExt.dixonBound`, a definition declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#dixon-bound).

## The Dixon sum $\upsilon_3$

For integers $a_1, a_2, a_3$, let
$B = \max(|a_1|, |a_2|, |a_3|)$. Then $\upsilon_3(a_1, a_2, a_3)$ is the rational number

$$\upsilon_3(a_1, a_2, a_3) = \sum_{k=-B}^{B} (-1)^k \prod_{i=1}^{3} \binom{2a_i}{a_i + k},$$

where for integers $n$ and $k$ the binomial coefficient $\binom{n}{k}$ is the ordinary one when
$0 \le k \le n$ and is $0$ otherwise.

Every summand with $|k| > B$ is zero, so this is the alternating sum over all integers $k$.

Formalized by `MetaMathlibExt.upsilon₃`, a definition declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#upsilon).

## Dixon's summation theorem

For an integer $m$ write $m!$ for the extended factorial
and $\frac{1}{m!}$ for the inverse factorial; both are $0$ when $m < 0$. For all integers
$a_1, a_2, a_3$, the Dixon sum $\Upsilon_3(a_1, a_2, a_3)$ equals

$$
(2a_1)!\,(2a_2)!\,(2a_3)!\,(a_1 + a_2 + a_3)! \cdot
\frac{1}{(a_1 + a_2)!} \cdot \frac{1}{(a_1 + a_3)!} \cdot \frac{1}{(a_2 + a_3)!} \cdot
\frac{1}{a_1!} \cdot \frac{1}{a_2!} \cdot \frac{1}{a_3!}.
$$

Proof: a Wilf–Zeilberger pair. For $a = a_1 \ge 0$ and $b = a_2 \ge 0$ the normalized summand
in $c = a_3$ has the certificate ratio
$R(c, k) = -\frac{(a + k)(b + k)}{2(c - k + 1)(a + b + c + 1)}$; induction on $c$ telescopes
over the fixed window $[-a, a]$. Negative arguments make both sides zero.

## Sources

- Abdesselam, arXiv:1903.11147v2, Proposition (Dixon), TeX lines 502-512.

Formalized by `MetaMathlibExt.dixon_summation`, a theorem declared in [MathlibExt/Combinatorics/DixonSummation.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/DixonSummation.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html#dixon-summation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dixon's identity](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/dixon-s-identity)
