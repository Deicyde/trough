---
declaration: section
origin: cited
lean: MetaMathlibExt.tsum_twoAdic_parametric_multisection, MetaMathlibExt.tsum_threeAdic_parametric_multisection, MetaMathlibExt.tsum_threeAdic_multiples_regroup, MetaMathlibExt.tsum_baseAdic_parametric_multisection, MetaMathlibExt.tsum_baseAdic_multiples_regroup, MetaMathlibExt.tsum_baseAdic_weighted_multisection, MetaMathlibExt.tsum_twoAdic_truncated_regroup, MetaMathlibExt.tsum_twoAdic_high_regroup
statement: formalized
---

# Multisection of series by index factorization

23 results, 2 proved and 21 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html).

## Parametric two-adic multisection

Let $q \in \mathbb{C}$ and let $b : \mathbb{N} \to
\mathbb{C}$ be a sequence (its value at $0$ is not used). Suppose that the families
$(q^j b_{(2n-1) 2^j})$ and $(q^j (q - 1) b_{2n \cdot 2^j})$, indexed by the pairs $(j, n)$ of
natural numbers with $n \ge 1$, are summable. Then

$$\sum_{j \ge 0,\ n \ge 1} \left(q^j b_{(2n-1) 2^j} - q^j (q - 1) b_{2n \cdot 2^j}\right)
= \sum_{m \ge 1} b_m.$$

The two summability hypotheses imply that $(b_m)_{m \ge 1}$ is summable.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 1, series version (`jis-2024-24.5.5-prop-1`).

Stated but not proved: `MetaMathlibExt.tsum_twoAdic_parametric_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-two-adic-parametric-multisection).

## Parametric 3-adic multisection of a series

Let $q$ be a complex number and let
$(b_m)_{m \ge 1}$ be a sequence of complex numbers such that the three families
$q^j b_{(3n-1) 3^j}$, $q^j b_{(3n-2) 3^j}$ and $q^j (q - 1) b_{3n \cdot 3^j}$, each indexed by
the pairs $(j, n)$ with $j \ge 0$ and $n \ge 1$, are summable. Then

$$\sum_{j \ge 0,\, n \ge 1} \Bigl( q^j \bigl( b_{(3n-1) 3^j} + b_{(3n-2) 3^j} \bigr) -
q^j (q - 1) b_{3n \cdot 3^j} \Bigr) = \sum_{m \ge 1} b_m.$$

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Corollary 6, first display in sum form (`jis-2024-24.5.5-cor-6`).

Stated but not proved: `MetaMathlibExt.tsum_threeAdic_parametric_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-three-adic-parametric-multisection).

## Regrouping the multiples of 3 by their 3-adic factorization

Let $(b_m)_{m \ge 1}$ be a
sequence of complex numbers such that the family $(b_{3m})_{m \ge 1}$ is summable. Then

$$\sum_{j \ge 1,\, n \ge 1} \bigl( b_{(3n-1) 3^j} + b_{(3n-2) 3^j} \bigr) =
\sum_{m \ge 1} b_{3m},$$

where the sum on the left is an unconditional sum over the pairs $(j, n)$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Corollary 6, deduced identity in sum form (`jis-2024-24.5.5-cor-6`).

Stated but not proved: `MetaMathlibExt.tsum_threeAdic_multiples_regroup` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-three-adic-multiples-regroup).

## Parametric base-B multisection of a series

Let $B \ge 2$ be a natural number, let $q$
be a complex number and let $(c_m)_{m \ge 1}$ be a sequence of complex numbers. Suppose that the
family $q^j c_{(Bn-k) B^j}$ indexed by the triples $(j, n, k)$ with $j \ge 0$, $n \ge 1$ and
$1 \le k \le B - 1$ is summable, and that the family $q^j (q - 1) c_{Bn \cdot B^j}$ indexed by
the pairs $(j, n)$ with $j \ge 0$ and $n \ge 1$ is summable. Then

$$\sum_{j \ge 0,\, n \ge 1} \Bigl( q^j \sum_{k=1}^{B-1} c_{(Bn-k) B^j} -
q^j (q - 1) c_{Bn \cdot B^j} \Bigr) = \sum_{m \ge 1} c_m.$$

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 7, first display in sum form (`jis-2024-24.5.5-prop-7`).

Stated but not proved: `MetaMathlibExt.tsum_baseAdic_parametric_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-base-adic-parametric-multisection).

## Regrouping the multiples of B by their B-adic factorization

Let $B \ge 2$ be a natural
number and let $(c_m)_{m \ge 1}$ be a sequence of complex numbers such that the family
$(c_{Bm})_{m \ge 1}$ is summable. Then

$$\sum_{j \ge 1,\, n \ge 1} \sum_{k=1}^{B-1} c_{(Bn-k) B^j} = \sum_{m \ge 1} c_{Bm},$$

where the outer sum on the left is an unconditional sum over the pairs $(j, n)$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 7, deduced identity in sum form (`jis-2024-24.5.5-prop-7`).

Stated but not proved: `MetaMathlibExt.tsum_baseAdic_multiples_regroup` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-base-adic-multiples-regroup).

## Weighted base-B multisection of a series

Let $B \ge 2$ be a natural number, let
$\varphi, \chi : \mathbb{N} \to \mathbb{C}$ be weights and let $(c_m)_{m \ge 1}$ be a sequence
of complex numbers, and for $m \ge 1$ let $\nu_B(m)$ be the largest $k$ with $B^k \mid m$.
Suppose that the family $\varphi(j) c_{(Bn-k) B^j}$ indexed by the triples $(j, n, k)$ with
$j \ge 0$, $n \ge 1$ and $1 \le k \le B - 1$ is summable, and that the family
$\chi(j) c_{Bn \cdot B^j}$ indexed by the pairs $(j, n)$ with $j \ge 0$ and $n \ge 1$ is
summable. Then

$$\sum_{j \ge 0,\, n \ge 1} \Bigl( \sum_{k=1}^{B-1} \varphi(j) c_{(Bn-k) B^j} +
\chi(j) c_{Bn \cdot B^j} \Bigr) = \sum_{m \ge 1} \Bigl( \varphi(\nu_B(m)) +
\sum_{k < \nu_B(m)} \chi(k) \Bigr) c_m.$$

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 8, base-`b` sum form (`jis-2024-24.5.5-prop-8`).

Stated but not proved: `MetaMathlibExt.tsum_baseAdic_weighted_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-base-adic-weighted-multisection).

## Truncated two-adic regrouping

For every natural number $J$ and all sequences
$\varphi, c : \mathbb{N} \to \mathbb{C}$,

$$\sum_{j \ge J,\ n \ge 1} \varphi(j) c_{(2n-1) 2^j}
= \sum_{p \ge 1} \varphi(J + \nu_2(p)) c_{p 2^J},$$

where $\nu_2(p)$ is the exponent of the largest power of $2$ dividing $p$, the left side runs over
the pairs $(j, n)$ of natural numbers with $j \ge J$ and $n \ge 1$, the right side runs over the
positive integers $p$, and each side is an unconditional sum, taken to be $0$ when its family is
not summable.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 13, in sum form (`jis-2024-24.5.5-prop-13`).

Stated but not proved: `MetaMathlibExt.tsum_twoAdic_truncated_regroup` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-two-adic-truncated-regroup).

## Regrouping the multiples of a power of 2 by their 2-adic factorization

For every
natural number $J$ and every sequence $(c_m)_{m \ge 1}$ of complex numbers,

$$\sum_{j \ge J,\, n \ge 1} c_{(2n-1) 2^j} = \sum_{p \ge 1} c_{p 2^J},$$

where the left side is an unconditional sum over the pairs $(j, n)$. No summability is assumed:
$(j, n) \mapsto (2n-1) 2^{j-J}$ is a bijection onto the positive integers, so the two families
are summable together or not at all, and a non-summable family has sum $0$ by convention.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Corollary 14, first display in sum form (`jis-2024-24.5.5-cor-14`).

Stated but not proved: `MetaMathlibExt.tsum_twoAdic_high_regroup` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-two-adic-high-regroup).

## Two-adic regrouping of the non-multiples of a power of two

For every natural number $J$
and every sequence $c : \mathbb{N} \to \mathbb{C}$,

$$\sum_{0 \le j < J,\ n \ge 1} c_{(2n-1) 2^j} = \sum_{p \ge 1,\ 2^J \nmid p} c_p,$$

where the left side runs over the pairs $(j, n)$ of natural numbers with $j < J$ and $n \ge 1$,
the right side runs over the positive integers $p$ not divisible by $2^J$, and each side is an
unconditional sum, taken to be $0$ when its family is not summable.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Corollary 14, second display in sum form (`jis-2024-24.5.5-cor-14`).

Stated but not proved: `MetaMathlibExt.tsum_twoAdic_low_regroup` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-two-adic-low-regroup).

## Double 2-adic multisection of a double series

Let $(b_{p,q})_{p, q \ge 1}$ be a double
sequence of complex numbers such that each of the four families
$2^{j+k} b_{(2n-1) 2^j, (2m-1) 2^k}$, $2^{j+k} b_{(2n) 2^j, (2m) 2^k}$,
$2^{j+k} b_{(2n) 2^j, (2m-1) 2^k}$ and $2^{j+k} b_{(2n-1) 2^j, (2m) 2^k}$, indexed by the
quadruples $(j, k, n, m)$ with $j, k \ge 0$ and $n, m \ge 1$, is summable. Then

$$\sum_{p, q \ge 1} b_{p,q} = \sum_{j, k \ge 0,\ n, m \ge 1} 2^{j+k} \bigl(
b_{(2n-1) 2^j, (2m-1) 2^k} + b_{(2n) 2^j, (2m) 2^k} -
b_{(2n) 2^j, (2m-1) 2^k} - b_{(2n-1) 2^j, (2m) 2^k} \bigr),$$

where both sides are unconditional sums, over the pairs $(p, q)$ and the quadruples
$(j, k, n, m)$ respectively.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 15, sum version (`jis-2024-24.5.5-prop-15`).

Stated but not proved: `MetaMathlibExt.tsum_twoAdic_double_multisection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tsum-two-adic-double-multisection).

## $2$-adic expansion of the weighted Lambert series $f$

For every complex number $q$ with
$|q| < 1$, the weighted Lambert series $f(q) = \sum_{n \ge 1} n q^n / (1 - q^n)$ and
$g(q) = \sum_{n \ge 1} n q^n / (1 + q^n)$ satisfy
$f(q) = \sum_{j, k \ge 0} 2^{2j+k} \bigl(g(q^{2^{j+k}}) - 4 g(q^{2^{j+k+1}})\bigr)$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Corollary 16 (`jis-2024-24.5.5-cor-16`).

Stated but not proved: `MetaMathlibExt.lambert_sigma_eq_tsum_twoAdic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#lambert-sigma-eq-tsum-two-adic).

## 2-adic dissection of the Euler function

For every complex number $q$ with $|q| < 1$,
with the infinite q-Pochhammer symbol $(a; r)_\infty = \prod_{k \ge 0} (1 - a r^k)$, the
unconditional infinite product over $j \ge 0$ satisfies

$$\prod_{j \ge 0} \left( \frac{(q^{2^j}; q^{2^{j+1}})_\infty}
{(q^{2^{j+1}}; q^{2^{j+1}})_\infty} \right)^{2^j} = (q; q)_\infty.$$

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 19, first display (`jis-2024-24.5.5-prop-19`).

Stated but not proved: `MetaMathlibExt.tprod_qPochhammer_twoAdic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tprod-q-pochhammer-two-adic).

## Parametric 2-adic dissection of the Euler function for real q

Let $q$ and $p$ be real
numbers with $0 < q < 1$, and write $(a; r)_\infty = \prod_{k \ge 0} (1 - a r^k)$ for real $a$
and $r$ (an unconditional infinite product). Then, with real exponents $p - 1$ and $p^j$,

$$\prod_{j \ge 0} \left( \frac{(q^{2^j}; q^{2^{j+1}})_\infty}
{(q^{2^{j+1}}; q^{2^{j+1}})_\infty^{\,p-1}} \right)^{p^j} = (q; q)_\infty.$$

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 19, second display, real case (`jis-2024-24.5.5-prop-19`).

Stated but not proved: `MetaMathlibExt.tprod_qPochhammer_twoAdic_parametric` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tprod-q-pochhammer-two-adic-parametric).

## Parametric $3$-adic dissection of the Euler function

For real numbers $x$ and $y$ with
$0 < y < 1$ write $(x; y)_\infty = \prod_{k \ge 0} (1 - x y^k)$. For all real numbers $q$ and $p$
with $0 < q < 1$,
$\prod_{j \ge 0} \bigl((q^{3^j}; q^{3^{j+1}})_\infty\, (q^{2 \cdot 3^j}; q^{3^{j+1}})_\infty /
(q^{3^{j+1}}; q^{3^{j+1}})_\infty^{\,p - 1}\bigr)^{p^j} = (q; q)_\infty$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 19, third display, real case (`jis-2024-24.5.5-prop-19`).

Stated but not proved: `MetaMathlibExt.tprod_qPochhammer_threeAdic_parametric` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tprod-q-pochhammer-three-adic-parametric).

## 2-adic product factorization of the Euler function

For every complex number $q$ with
$|q| < 1$, with the infinite q-Pochhammer symbol $(a; r)_\infty = \prod_{k \ge 0} (1 - a r^k)$,
the unconditional infinite product over $j \ge 0$ satisfies
$\prod_{j \ge 0} (q^{2^j}; q^{2^{j+1}})_\infty = (q; q)_\infty$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 19, case `p = 1`, base 2 (`jis-2024-24.5.5-prop-19`).

Stated but not proved: `MetaMathlibExt.tprod_qPochhammer_twoAdic_factorization` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tprod-q-pochhammer-two-adic-factorizatio).

## $3$-adic factorization of the Euler function

Write
$(x; y)_\infty = \prod_{k \ge 0} (1 - x y^k)$ for the infinite $q$-Pochhammer symbol, where $x$
and $y$ are complex and $|y| < 1$. For every complex number $q$ with $|q| < 1$,
$\prod_{j \ge 0} (q^{3^j}; q^{3^{j+1}})_\infty\, (q^{2 \cdot 3^j}; q^{3^{j+1}})_\infty =
(q; q)_\infty$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 19, case `p = 1`, base 3 (`jis-2024-24.5.5-prop-19`).

Stated but not proved: `MetaMathlibExt.tprod_qPochhammer_threeAdic_factorization` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tprod-q-pochhammer-three-adic-factorizat).

## $2$-adic multisection of the infinite $q$-Pochhammer symbol

Write
$(x; y)_\infty = \prod_{k \ge 0} (1 - x y^k)$ for the infinite $q$-Pochhammer symbol, where $x$
and $y$ are complex and $|y| < 1$. For complex numbers $a$ and $q$ with $|q| < 1$,
$\prod_{j \ge 0} \bigl((a q^{2^j - 1}; q^{2^{j+1}})_\infty /
(a q^{2^{j+1} - 1}; q^{2^{j+1}})_\infty\bigr)^{2^j} = (a; q)_\infty$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 20 (`jis-2024-24.5.5-prop-20`).

Stated but not proved: `MetaMathlibExt.tprod_qPochhammer_shifted_twoAdic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#tprod-q-pochhammer-shifted-two-adic).

## $2$-adic dissection of a ratio of Gamma functions

For complex numbers $a$ and $z$ write
$f(a, z) = \Gamma(a + 1)^2 / \bigl(\Gamma(a + 1 - iz)\, \Gamma(a + 1 + iz)\bigr)$. If $a$ is not a
negative integer, then for every complex number $z$,
$f(a, z) = \prod_{j \ge 0} f(a / 2^{j+1} - 1/2,\ z / 2^{j+1})$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 22 (`jis-2024-24.5.5-prop-22`).

Stated but not proved: `MetaMathlibExt.gamma_ratio_eq_tprod_twoAdic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#gamma-ratio-eq-tprod-two-adic).

## Two-adic multisection of the power-weighted Lambert series

For every integer $\mu \ge 1$
and every complex number $q$ with $|q| < 1$, the power-weighted Lambert series
$f_\mu(q) = \sum_{n \ge 1} n^\mu q^n / (1 - q^n)$ and
$g_\mu(q) = \sum_{n \ge 1} n^\mu q^n / (1 + q^n)$ satisfy

$$
f_\mu(q) = \sum_{j, k \ge 0} 2^{(\mu+1)j+k}
\left(g_\mu\left(q^{2^{j+k}}\right) - 2^{\mu+1} g_\mu\left(q^{2^{j+k+1}}\right)\right),
$$

the sum running over all pairs $(j, k)$ of natural numbers.

The paper prints the weight $2^{2j+k}$, its value for $\mu = 1$ (Corollary 16), which is false
for $\mu \ge 2$: for $\mu = 2$ the coefficient of $q^2$ is $\sigma_2(2) = 1^2 + 2^2 = 5$ on the
left and $1$ on the right. The weight $2^{(\mu+1)j+k}$ is what the paper's proof of Corollary 16
gives with $n^\mu$ in place of $n$: there $2^{2j+k} = 2^{j+k} \cdot 2^j$, where $2^j$ is the
factor of the index $(2n-1) 2^j$ in the summand $n$, which becomes $2^{\mu j}$ for $n^\mu$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Corollary 17 (`jis-2024-24.5.5-cor-17`).

Stated but not proved: `MetaMathlibExt.lambertMu_sigma_eq_tsum_twoAdic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#lambert-mu-sigma-eq-tsum-two-adic).

## Borwein's eta–Lambert correspondence

Let $(a_n)$ and $(b_n)$ be sequences of complex
numbers and let $C$ and $K$ be real numbers with $|a_n| \le C n^K$ and $|b_n| \le C n^K$ for every
$n \ge 1$. Let $\eta(s) = \sum_{n \ge 1} (-1)^{n-1} n^{-s}$ be the Dirichlet eta function. Then
$\eta(s) \sum_{n \ge 1} a_n n^{-s} = \sum_{n \ge 1} b_n n^{-s}$ for every real number
$s > \max(K + 2, 1)$ if and only if $\sum_{n \ge 1} a_n x^n / (1 + x^n) = \sum_{n \ge 1} b_n x^n$
for every real number $x$ with $0 < x < 1$.

The source quotes the correspondence from Borwein and Borwein without growth hypotheses or
ranges for $s$ and $x$; the growth bound and the ranges above make all the series involved converge
absolutely.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 18 (`jis-2024-24.5.5-prop-18`).

Stated but not proved: `MetaMathlibExt.eta_mul_LSeries_iff_lambert` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#eta-mul-lseries-iff-lambert).

## The Gamma quadratic ratio

For complex numbers $a$, $b$ and $z$, the Gamma quadratic ratio
is $g(a, b, z) = \dfrac{b}{b - z} \cdot
\dfrac{\Gamma(a - \sqrt{a^2 - b})\, \Gamma(a + \sqrt{a^2 - b})}
{\Gamma(a - \sqrt{a^2 - b + z})\, \Gamma(a + \sqrt{a^2 - b + z})}$, where $\sqrt{\cdot}$ is the
principal complex square root (the value does not depend on the choice of root).

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 23.

Formalized by `MetaMathlibExt.gammaQuadraticRatio`, a definition declared in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#gamma-quadratic-ratio).

## The Gamma quadratic ratio at $z = 0$

Let $a$ and $b$ be complex numbers with $b \ne 0$
and $\Gamma(a - \sqrt{a^2 - b})\, \Gamma(a + \sqrt{a^2 - b}) \ne 0$, where $\sqrt{\cdot}$ denotes
the principal complex square root. Then the Gamma quadratic ratio $g$ satisfies $g(a, b, 0) = 1$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 23.

Formalized by `MetaMathlibExt.gammaQuadraticRatio_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#gamma-quadratic-ratio-zero-right).

## $2$-adic dissection of the Gamma quadratic ratio

Let $a, b, z$ be complex numbers such
that $m^2 + 2am + b \ne 0$ and $m^2 + 2am + b - z \ne 0$ for every integer $m$ that is nonnegative
or of the form $m = -2^j$ with $j \ge 0$ an integer. For $j \ge 0$ put $a_j = a / 2^{j+1} - 1/2$
and $b_j = 1/4 - a / 2^{j+1} + b / 2^{2j+2}$. Then the Gamma quadratic ratio $g$ satisfies
$g(a, b, z) = \prod_{j \ge 0} g(a_j, b_j, z / 2^{2j+2})$.

The source prints the parameters $a / 2^j - 1$ and $1 - a / 2^{j+1} + b / 2^{2j+2}$, which make
the identity false: for $a = 3/10$, $b = -2$, $z = 7/10$ the left side is about $1.6283$ and the
printed product about $6.18 \cdot 10^4$, while the product above matches. The parameters $a_j$,
$b_j$ come from the penultimate line of the source's proof, which writes
$m^2 + 2am + b = 2^{2j+2}(n^2 + 2 a_j n + b_j)$ for $m = (2n - 1) 2^j$. The hypotheses, absent
from the source, exclude the poles of every Gamma factor on both sides and the vanishing of $b$
and $b - z$.

## Sources

- Christophe Vignat and Michael Milgram, *Curious Multisection Identities by Index Factorization*, Journal of Integer Sequences 27 (2024), Article 24.5.5, Proposition 23 (`jis-2024-24.5.5-prop-23`).

Stated but not proved: `MetaMathlibExt.gammaQuadraticRatio_eq_tprod_twoAdic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IndexFactorizationMultisectionWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html#gamma-quadratic-ratio-eq-tprod-two-adic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multisection of series by index factorization](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/multisection-of-series-by-index-factorization)
