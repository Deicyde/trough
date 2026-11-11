---
declaration: section
origin: cited
lean: MetaMathlibExt.fried_alternating_binomial_identity, MetaMathlibExt.bala_somos_partition_parity, MetaMathlibExt.coeff_diag_trinomial_product_eq_franel, MetaMathlibExt.exists_sq_near_triangular_beatty_sqrt_two, MetaMathlibExt.ncard_arithProg_eq_sum_divisorSummatory, MetaMathlibExt.card_digitInsertion_le_ten_mul_eq_digitSum, MetaMathlibExt.bala_binomial_sum_odd_imp_mod_four, MetaMathlibExt.ceil_cot_pi_div_two_mul_steps
statement: formalized
---

# Binomial sum parities and cotangent floor sequences

17 results, 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html).

## Fried's alternating binomial identity

For integers $a$ and $b$ let $\binom{a}{b}$ be the
binomial coefficient when $a, b \ge 0$ (so $0$ when $b > a$), and $0$ when $a < 0$ or $b < 0$.
For natural numbers $n$, $r$, $s$ with $r \le n$ and $s \le 2r$, with all arguments computed in
the integers,

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{2n-2r}{n-k} \binom{n-k}{n-2r+s}
\binom{2r-k-s}{n-s} = (-1)^n \binom{n}{2r-n} \binom{2n-2r}{n-s}.$$

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Lemma 1 (`jis-2026-26.1.8-lem-1`).

Stated but not proved: `MetaMathlibExt.fried_alternating_binomial_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#fried-alternating-binomial-identity).

## The Bala–Somos parity conjectures

For a natural number $k$ let $p(k)$ be the number of
partitions of $k$. For natural numbers $m$ and $N$ let
$b_m(N) = \sum_{k=1}^{N} k^{2m+1} p(k) p(N-k)$ and $a(N) = \sum_{j=0}^{N} c(j)\, p(N-j)$, where
$c(0) = 0$ and $c(j) = \sum_{d \mid j,\ d \text{ odd}} (-1)^{j/d - 1}$ for $j \ge 1$. Then for all
$m \ge 1$ and $n \ge 1$: (a) if $n$ is odd, then $n$ divides $b_m(n)$; (b) $n$ divides $b_m(2n)$,
and $b_m(2n)/n$ is odd if and only if $n$ and $p(n)$ are both odd; (c) $a(n)$ is odd if and only
if $n$ and $p(n)$ are both odd; (d) twice the fractional part of the rational number $b_1(n)/n$
equals $1$ if and only if $n$ is even and $n/2$ and $p(n/2)$ are both odd.

Here $c(j)$ is the coefficient of $x^j$ in $\sum_{k \ge 1} x^{2k-1}/(1 + x^{2k-1})$, so $a(N)$ is
the coefficient of $x^N$ in $\bigl(\sum_{k \ge 1} x^{2k-1}/(1 + x^{2k-1})\bigr)
\prod_{k \ge 1} 1/(1 - x^k)$ (A305123). The paper calls the left side of (d) $c(n)$, a different
sequence from the coefficients $c(j)$ above.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 8 (`jis-2026-26.1.8-thm-8`).

Stated but not proved: `MetaMathlibExt.bala_somos_partition_parity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#bala-somos-partition-parity).

## A diagonal coefficient equal to a signed Franel number

For every $n \ge 0$, the
coefficient of $x^n y^n z^n$ in the integer polynomial
$(1 + x + y - z)^n (1 + x - y + z)^n (1 - x + y + z)^n$ equals
$(-1)^n \sum_{k=0}^{n} \binom{n}{k}^3$ (A000172).

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 2 (`jis-2026-26.1.8-thm-2`).

Stated but not proved: `MetaMathlibExt.coeff_diag_trinomial_product_eq_franel` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#coeff-diag-trinomial-product-eq-franel).

## Triangular numbers near squares along $\lfloor n\sqrt{2} \rfloor$

For a natural number
$n$ let $a = \lfloor n\sqrt{2} \rfloor$ (A001951) and $T_a = a(a+1)/2$. Then some integer $k$
satisfies $|T_a - k^2| \le \lfloor a/2 \rfloor$; that is, the distance from $T_a$ to the nearest
perfect square is at most $\lfloor a/2 \rfloor$.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 3 (`jis-2026-26.1.8-thm-3`).

Stated but not proved: `MetaMathlibExt.exists_sq_near_triangular_beatty_sqrt_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#exists-sq-near-triangular-beatty-sqrt-tw).

## Counting arithmetic progressions in $\{1, \dots, n\}$

For every integer $n \ge 1$, the
number of subsets $S \subseteq \{1, \dots, n\}$ with $|S| \ge 2$ that are arithmetic progressions,
that is, $S = \{a, a + d, \dots, a + (|S| - 1)d\}$ for some natural numbers $a$ and $d \ge 1$,
equals $\sum_{m=0}^{n-1} D(m)$, where $D(m) = \sum_{k=1}^{m} \lfloor m/k \rfloor$ (A078567,
A006218).

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 5 (`jis-2026-26.1.8-thm-5`).

Stated but not proved: `MetaMathlibExt.ncard_arithProg_eq_sum_divisorSummatory` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#ncard-arith-prog-eq-sum-divisor-summator).

## Inserting a digit and the digit sum

Let $n \ge 1$ have the $\ell$ decimal digits
$d_{\ell-1} \dots d_1 d_0$, so that $n = \sum_{j\lt \ell} d_j 10^j$. Let $S(n)$ be the set of the
numbers $\sum_{j\lt i} d_j 10^j + x \cdot 10^i + \sum_{i \le j < \ell} d_j 10^{j+1}$ with
$0 \le i \le \ell$ and $x \in \{0, \dots, 9\}$, excluding $i = \ell$ with $x = 0$: these are the
numbers obtained by inserting one decimal digit $x$ anywhere in the decimal expansion of $n$,
without creating a leading zero. Then the number of elements of $S(n)$ that are at most $10n$,
that is, the position of $10n$ when $S(n)$ is listed in increasing order, equals the digit sum
$d_0 + d_1 + \dots + d_{\ell-1}$ of $n$ (A007953).

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 6 (`jis-2026-26.1.8-thm-6`).

Stated but not proved: `MetaMathlibExt.card_digitInsertion_le_ten_mul_eq_digitSum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#card-digit-insertion-le-ten-mul-eq-digit).

## Odd values of Bala's binomial sum are $1$ modulo $4$

For a natural number $n$, let
$a(n) = \sum_{k=0}^{n} \binom{2n+1}{n+k+1} (-2)^k$. If $a(n)$ is odd, then $a(n) \equiv 1 \pmod 4$.

The paper's $a(n)$ is A026641 (the number of even-outdegree nodes in all ordered trees with $n$
edges); its proof works with this binomial sum (Bala's formula, display (13)), which is taken as
the definition here.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 7 (`jis-2026-26.1.8-thm-7`).

Stated but not proved: `MetaMathlibExt.bala_binomial_sum_odd_imp_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#bala-binomial-sum-odd-imp-mod-four).

## The ceiling of $\cot(\pi/(2m))$ rises in steps of $0$ or $1$

For $m \ge 1$ let
$g(m) = \lceil \cot(\pi/(2m)) \rceil$. Then for every $m \ge 1$, $g(m) \le g(m+1)$ and
$g(m+1) - g(m) \in \{0, 1\}$; and for every integer $n \ge 1$, the number of $m \ge 1$ with
$g(m) = n$ is $1$ or $2$.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Lemma 9 (`jis-2026-26.1.8-lem-9`).

Stated but not proved: `MetaMathlibExt.ceil_cot_pi_div_two_mul_steps` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#ceil-cot-pi-div-two-mul-steps).

## Counting $m$ with $\lceil \cot(\pi/(2m)) \rceil \le r$

Let
$g(m) = \lceil \cot(\pi / (2m)) \rceil$ for integers $m \ge 1$, and call an integer $j$ a
singleton if exactly one integer $m \ge 1$ satisfies $g(m) = j$. For an integer $r \ge 1$, let
$s(r)$ be the number of singletons in $\{1, \dots, r\}$. Then the number of integers $m \ge 2$
with $g(m) \le r$ equals $2r - s(r)$.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Lemma 10 (`jis-2026-26.1.8-lem-10`).

Stated but not proved: `MetaMathlibExt.ncard_ceil_cot_le_eq_two_mul_sub_singletons` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#ncard-ceil-cot-le-eq-two-mul-sub-singlet).

## Values taken once by the ceiling of $\cot(\pi/(2m))$

For $m \ge 1$ let
$g(m) = \lceil \cot(\pi/(2m)) \rceil$. Let $r \ge 1$ and $m \ge 2$ be integers. Then $m$ is the
only integer $m' \ge 1$ with $g(m') = r$ if and only if $g(m-1) = r - 1$, $g(m) = r$ and
$g(m+1) = r + 1$.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Lemma 11 (`jis-2026-26.1.8-lem-11`).

Stated but not proved: `MetaMathlibExt.ceil_cot_singleton_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#ceil-cot-singleton-iff).

## Jeffery's conjecture on singletons of $\lfloor \cot(\pi/(2m)) \rfloor$

Let
$f(m) = \lfloor \cot(\pi / (2m)) \rfloor$ for nonzero integers $m$. Let $a_1 < a_2 < \cdots$ list
the integers $k \ge 1$ for which exactly one integer $m \ge 2$ satisfies $f(-m) = -k$, and let
$b_1 < b_2 < \cdots$ list the integers $k \ge 2$ with $f(-k-1) < f(-k) < f(-k+1)$. Then for every
integer $n \ge 1$, $2a_n = b_n + n - 1$ (A223577, A223578).

If either list has fewer than $n$ terms, its $n$-th term is taken to be $0$.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 12 (`jis-2026-26.1.8-thm-12`).

Stated but not proved: `MetaMathlibExt.jeffery_floor_cot_singletons` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#jeffery-floor-cot-singletons).

## Counting solutions of a repeating-decimal ratio equation

For every natural number
$n \ge 1$, the number of natural numbers $x$ with $10^n \le x < 10^{n+1}$ for which there is a
natural number $k$ with $x \le k < 2x$ and $k / x = 1 + (x - 10^n) / (10^n - 1)$, computed in the
rationals, (OEIS A285273) equals $2^{\omega(10^n - 1)}$, where $\omega(m)$ is the number of
distinct prime factors of $m$.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 13 (`jis-2026-26.1.8-thm-13`).

Stated but not proved: `MetaMathlibExt.ncard_repeating_decimal_ratio_eq_two_pow_omega` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#ncard-repeating-decimal-ratio-eq-two-pow).

## Zakharov's conjecture on regions cut by cevians

Let $A$, $B$, $C$ be affinely independent
points of $\mathbb{R}^2$ and $T$ the triangle they span; a cevian is a segment joining a vertex
of $T$ to a point of the open side opposite it. The regions cut out by cevians
$c_1, \dots, c_n$ are the connected components of the interior of $T$ minus
$c_1 \cup \dots \cup c_n$. Then for every $n \ge 0$, the maximum number of regions cut out by
$n$ cevians (not necessarily distinct) is $\lceil (n+1)(n+2)/3 \rceil$ (A007980).

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 14 (`jis-2026-26.1.8-thm-14`).

Stated but not proved: `MetaMathlibExt.cevian_max_regions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#cevian-max-regions).

## Zakharov's conjecture on intersection points of cevians

Let $A$, $B$, $C$ be affinely
independent points of $\mathbb{R}^2$ and $T$ the triangle they span; a cevian is a segment
joining a vertex of $T$ to a point of the open side opposite it. Let $n \ge 0$ and let
$c_1, \dots, c_n$ be cevians such that the interior of $T$ minus $c_1 \cup \dots \cup c_n$ has
exactly $\lceil (n+1)(n+2)/3 \rceil$ connected components. Then the number of points of the
interior of $T$ that lie on $c_i$ and on $c_j$ for some $i \ne j$ is $\lfloor n^2/3 \rfloor$
(A000212).

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Corollary 15 (`jis-2026-26.1.8-cor-15`).

Stated but not proved: `MetaMathlibExt.cevian_max_regions_intersection_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#cevian-max-regions-intersection-count).

## Intersection points of two fans of rays

Let $m, n \ge 1$, $P = (-1, 0)$ and
$Q = (1, 0)$. From $P$ draw the $m$ closed rays at angles $\pi - 2\pi s/m$ for $0 \le s < m$, and
from $Q$ the $n$ closed rays at angles $2\pi t/n$ for $0 \le t < n$. Let
$h = \lfloor (m - 1)/2 \rfloor$. Then the number of points that are $P$, $Q$, or a point off the
$x$-axis lying on a ray from $P$ and on a ray from $Q$ is
$2 \sum_{s=1}^{h} \lceil ns/m - 1/2 \rceil + 2$ for odd $n$ and
$2 \sum_{s=1}^{h} \lceil ns/m \rceil - 2h + 2$ for even $n$.

Off the $x$-axis these are exactly the points where two rays meet; on the axis, rays meet only at
$P$, $Q$ or along overlapping segments, which the paper does not count.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Theorem 16 (`jis-2026-26.1.8-thm-16`).

Stated but not proved: `MetaMathlibExt.two_fan_ray_intersection_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#two-fan-ray-intersection-count).

## Blomberg's conjecture on intersection points of two equal fans

Let $n \ge 1$,
$P = (-1, 0)$ and $Q = (1, 0)$. From $P$ draw the $n$ closed rays at angles $\pi - 2\pi s/n$ for
$0 \le s < n$, and from $Q$ the $n$ closed rays at angles $2\pi t/n$ for $0 \le t < n$. Then the
number of points that are $P$, $Q$, or a point off the $x$-axis lying on a ray from $P$ and on a
ray from $Q$ is $(n^2 + 7)/4$ for odd $n$ and $(n^2 - 6n + 16)/4$ for even $n$ (A338042).

Off the $x$-axis these are exactly the points where two rays meet; on the axis, rays meet only at
$P$, $Q$ or along overlapping segments, which are not counted.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Corollary 17 (`jis-2026-26.1.8-cor-17`).

Stated but not proved: `MetaMathlibExt.two_fan_ray_intersection_count_diag` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#two-fan-ray-intersection-count-diag).

## Blomberg's conjecture on regions cut out by two equal fans

Let $n \ge 3$, $P = (-1, 0)$
and $Q = (1, 0)$. From $P$ draw the $n$ closed rays at angles $\pi - 2\pi s/n$ for $0 \le s < n$,
and from $Q$ the $n$ closed rays at angles $2\pi t/n$ for $0 \le t < n$, and let $U$ be the union
of these rays. Then there is a real $R_0$ such that for every real $R \ge R_0$, if $K_R$ is the
convex hull of the points of $U$ on the circle $x^2 + y^2 = R^2$, the interior of $K_R$ minus $U$
has $(n^2 + 8n - 5)/4$ connected components for odd $n$ and $(n^2 + 2n)/4$ for even $n$
(A338041).

The points lie on the circle, so $K_R$ is the polygon joining consecutive points, and the
connected components are the regions into which the rays cut it.

## Sources

- Sela Fried, *Proofs of Ten Conjectures From the OEIS*, Journal of Integer Sequences 29 (2026), Article 26.1.8, Corollary 21 (`jis-2026-26.1.8-cor-21`).

Stated but not proved: `MetaMathlibExt.two_fan_region_count_diag` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/TenOeisConjecturesWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html#two-fan-region-count-diag).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial sum parities and cotangent floor sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/binomial-sum-parities-and-cotangent-floor-sequen)
