---
declaration: section
origin: cited
lean: MetaMathlibExt.arndtCompositionCount, MetaMathlibExt.arndtCompositionCount_six_two, MetaMathlibExt.arndtCompositionCount_six_three, MetaMathlibExt.arndtCompositionCount_six_four, MetaMathlibExt.arndtGF, MetaMathlibExt.coeff_arndtGF, MetaMathlibExt.arndtGF_mul_one_sub_pairs, MetaMathlibExt.arndtGF_univ_mul
statement: formalized
---

# Arndt compositions

85 results, 43 proved and 42 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html).

## Number of Arndt compositions with parts in a set

For a set $S$ of natural numbers and
natural numbers $n$ and $k$, $a_S(n, k)$ is the number of $k$-tuples $(c_1, \dots, c_k)$ of
positive integers such that $c_1 + \dots + c_k = n$, every $c_i$ lies in $S$, and
$c_{2i-1} > c_{2i}$ for every $i$ with $2i \le k$. These tuples are the Arndt compositions of
$n$ with $k$ parts in $S$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 1 (definition of Arndt compositions, after D. F. Checa and J. L. Ramírez, arXiv:2311.15388, Section 1).

Formalized by `MetaMathlibExt.arndtCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count).

## Arndt compositions of 6 with two parts

There are exactly $2$ Arndt compositions of $6$
with two parts.

They are $(5, 1)$ and $(4, 2)$.

## Sources

- D. F. Checa and J. L. Ramírez, *Arndt compositions: a generating functions approach*, arXiv:2311.15388, Section 1 (list of the Arndt compositions of `6`).

Formalized by `MetaMathlibExt.arndtCompositionCount_six_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-six-two).

## Arndt compositions of 6 with three parts

There are exactly $4$ Arndt compositions of $6$
with three parts.

They are $(4, 1, 1)$, $(3, 2, 1)$, $(3, 1, 2)$ and $(2, 1, 3)$.

## Sources

- D. F. Checa and J. L. Ramírez, *Arndt compositions: a generating functions approach*, arXiv:2311.15388, Section 1 (list of the Arndt compositions of `6`).

Formalized by `MetaMathlibExt.arndtCompositionCount_six_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-six-three).

## Arndt compositions of 6 with four parts

There is exactly one Arndt composition of $6$
with four parts.

It is $(2, 1, 2, 1)$.

## Sources

- D. F. Checa and J. L. Ramírez, *Arndt compositions: a generating functions approach*, arXiv:2311.15388, Section 1 (list of the Arndt compositions of `6`).

Formalized by `MetaMathlibExt.arndtCompositionCount_six_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-six-four).

## Generating function of Arndt compositions with parts in a set

An Arndt composition is a
finite sequence $(\sigma_1, \dots, \sigma_k)$ of positive integers such that
$\sigma_{2i-1} > \sigma_{2i}$ for every $i$ with $2i \le k$. For a set $S$ of natural numbers, let
$a_S(n, k)$ be the number of Arndt compositions of $n$ with $k$ parts, all in $S$. The bivariate
generating function of these compositions, by weight ($x$) and number of parts ($y$), is the power
series $A_S(x, y) = \sum_{n \ge 0} \left(\sum_{k=0}^{n} a_S(n, k)\, y^k\right) x^n$ in
$\mathbb{Z}[y][[x]]$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 2.

Formalized by `MetaMathlibExt.arndtGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf).

## Coefficients of the generating function of Arndt compositions

For a set $S$ of natural
numbers and every $n \ge 0$, the coefficient of $x^n$ in the generating function $A_S(x, y)$ of
Arndt compositions with parts in $S$ is the polynomial $\sum_{k=0}^{n} a_S(n, k)\, y^k$ in
$\mathbb{Z}[y]$, where $a_S(n, k)$ is the number of Arndt compositions of $n$ with $k$ parts, all
in $S$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 2.

Formalized by `MetaMathlibExt.coeff_arndtGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#coeff-arndt-gf).

## Pair decomposition of the Arndt generating function

Let $S$ be a set of positive
integers and let $A_S(x, y)$ be the generating function of Arndt compositions with parts in $S$:
the formal power series in $x$ over $\mathbb{Z}[y]$ whose coefficient of $x^n y^k$ is the number
of Arndt compositions of $n$ with $k$ parts, all in $S$. Put $P_S(x) = \sum_{i \in S} x^i$ and
$Q_S(x) = \sum_{i, j \in S,\ j < i} x^{i+j}$. Then

$$A_S(x, y) \, (1 - y^2 Q_S(x)) = 1 + y P_S(x).$$

Equivalently, $A_S(x, y) = (1 + y P_S(x)) \sum_{m \ge 0} Q_S(x)^m y^{2m}$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 1 (`jis-2025-25.3.6-thm-1`).

Stated but not proved: `MetaMathlibExt.arndtGF_mul_one_sub_pairs` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf-mul-one-sub-pairs).

## Generating function of all Arndt compositions

Let $A(x, y)$ be the formal power series
in $x$ over $\mathbb{Z}[y]$ whose coefficient of $x^n y^k$ is the number of Arndt compositions of
$n$ with $k$ parts. Then

$$A(x, y) \left((1 - x)(1 - x^2) - y^2 x^3\right) = (1 - x + xy)(1 - x^2).$$

Equivalently, $A(x, y) = (1 + xy/(1 - x)) \sum_{m \ge 0} y^{2m} x^{3m} / (x; x)_2^m$ with
$(x; x)_2 = (1 - x)(1 - x^2)$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 9 (`jis-2025-25.3.6-thm-9`).

Stated but not proved: `MetaMathlibExt.arndtGF_univ_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf-univ-mul).

## Arndt compositions with a given number of parts as a sum of products

For all natural
numbers $n$ and $\ell$, the number of Arndt compositions of $n$ with $2\ell$ parts is

$$\sum_{(a_1, \dots, a_\ell)} \prod_{i=1}^{\ell} \left\lfloor \frac{a_i - 1}{2} \right\rfloor,$$

the sum running over the $\ell$-tuples of natural numbers with $a_1 + \dots + a_\ell = n$ and
every $a_i \ge 3$; and the number of Arndt compositions of $n$ with $2\ell + 1$ parts is the same
sum of products $\prod_{i=1}^{\ell} \lfloor (a_i - 1)/2 \rfloor$, now running over the
$(\ell + 1)$-tuples $(a_1, \dots, a_{\ell+1})$ of natural numbers with
$a_1 + \dots + a_{\ell+1} = n$, $a_1, \dots, a_\ell \ge 3$ and $a_{\ell+1} \ge 1$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 10 (`jis-2025-25.3.6-thm-10`).

Stated but not proved: `MetaMathlibExt.arndtCompositionCount_eq_sum_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-eq-sum-prod).

## Arndt compositions with parts at most 3 and the Padovan numbers

For every $n \ge 0$, the
number of Arndt compositions of $n$ (compositions $(\sigma_1, \dots, \sigma_k)$ with
$\sigma_{2i-1} > \sigma_{2i}$ whenever $2i \le k$) with all parts in $\{1, 2, 3\}$, counting the
empty composition when $n = 0$, equals the shifted Padovan number $s_{n+2}$, where $s_0 = 1$,
$s_1 = 0$, $s_2 = 1$ and $s_{m+3} = s_{m+1} + s_m$. Equivalently, it is the Padovan number $P(n)$
given by $P(0) = P(1) = P(2) = 1$ and $P(n) = P(n-2) + P(n-3)$ for $n \ge 3$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 2 (`jis-2025-25.3.6-thm-2`).

Stated but not proved: `MetaMathlibExt.sum_arndtCompositionCount_le_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#sum-arndt-composition-count-le-three).

## Arndt compositions with parts at most 4 and Narayana's cows sequence

For every
$n \ge 0$, the number of Arndt compositions of $n$ (compositions $(\sigma_1, \dots, \sigma_k)$
with $\sigma_{2i-1} > \sigma_{2i}$ whenever $2i \le k$) with all parts in $\{1, 2, 3, 4\}$,
counting the empty composition when $n = 0$, equals $N_{n+1}$, where $(N_m)$ is Narayana's cows
sequence: $N_0 = 0$, $N_1 = N_2 = 1$ and $N_m = N_{m-1} + N_{m-3}$ for $m \ge 3$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 4 (`jis-2025-25.3.6-thm-4`).

Stated but not proved: `MetaMathlibExt.sum_arndtCompositionCount_le_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#sum-arndt-composition-count-le-four).

## Generating function of Arndt compositions with bounded largest part

For a natural number
$\ell$, let $A(x, y; \ell)$ be the formal power series in $x$ over $\mathbb{Z}[y]$ whose
coefficient of $x^n y^k$ is the number of Arndt compositions of $n$ with $k$ parts, all at most
$\ell$, and let

$$D_\ell(x, y) = 1 - x^{2+2\ell} y^2 + x^{2+\ell} (1 + x) y^2 - x (1 + x + x^2 (y^2 - 1)).$$

Then

$$A(x, y; \ell) \, D_\ell(x, y) = (1 - x^2)\left(1 - x + x (1 - x^\ell) y\right).$$

The paper assumes $\ell \ge 2$; the identity also holds for $\ell = 0, 1$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Corollary 5 (`jis-2025-25.3.6-cor-5`).

Stated but not proved: `MetaMathlibExt.arndtGF_le_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf-le-mul).

## Generating function of Arndt compositions with bounded smallest part

For a natural
number $\ell \ge 1$, let $B(x, y; \ell)$ be the formal power series in $x$ over $\mathbb{Z}[y]$
whose coefficient of $x^n y^k$ is the number of Arndt compositions of $n$ with $k$ parts, all at
least $\ell$. Then

$$B(x, y; \ell) \left(1 - x - x^2 + x^3 - x^{2\ell+1} y^2\right) = (1 - x^2)(1 - x + x^\ell y).$$

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Corollary 6 (`jis-2025-25.3.6-cor-6`).

Stated but not proved: `MetaMathlibExt.arndtGF_ge_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf-ge-mul).

## Generating functions of Arndt compositions with even parts and with odd parts

Let
$A_E(x, y)$ and $A_O(x, y)$ be the formal power series in $x$ over $\mathbb{Z}[y]$ whose
coefficient of $x^n y^k$ is the number of Arndt compositions of $n$ with $k$ parts, all even,
respectively all odd. Then

$$A_E(x, y) \left(1 - x^2 - x^4 + x^6 (1 - y^2)\right) = (1 - x^4)\left(1 - x^2 (1 - y)\right)$$

and

$$A_O(x, y) \left(1 - x^2 + x^6 - x^4 (1 + y^2)\right) = (1 - x^4)(1 - x^2 + x y).$$

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Corollary 7 (`jis-2025-25.3.6-cor-7`).

Stated but not proved: `MetaMathlibExt.arndtGF_even_odd_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf-even-odd-mul).

## Down/up compositions

A down/up (descending wiggly) composition of $n$ with $k$ parts is a
sequence $(\sigma_1, \dots, \sigma_k)$ of positive integers with sum $n$ such that
$\sigma_1 > \sigma_2 < \sigma_3 > \sigma_4 < \cdots$, that is, $\sigma_i > \sigma_{i+1}$ for odd
$i$ and $\sigma_i < \sigma_{i+1}$ for even $i$. For $n, k, j \ge 0$, $w(n, k, j)$ is the number of
down/up compositions of $n$ with $k$ parts whose last part $\sigma_k$ equals $j$, where the empty
composition ($k = 0$) is taken to have last part $0$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3 (the set `W`, OEIS A025049).

Formalized by `MetaMathlibExt.downUpCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-composition-count).

## Down/up compositions of 5 with two parts

Among the down/up compositions of $5$ with two
parts (pairs $(\sigma_1, \sigma_2)$ of positive integers with $\sigma_1 + \sigma_2 = 5$ and
$\sigma_1 > \sigma_2$), exactly one has last part $1$, exactly one has last part $2$, and none has
last part $3$.

The compositions counted are $(4, 1)$ and $(3, 2)$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3 (the set `W`).

Formalized by `MetaMathlibExt.downUpCompositionCount_five_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-composition-count-five-two).

## Down/up compositions of 6 with three parts

Among the down/up compositions of $6$ with
three parts (triples $(\sigma_1, \sigma_2, \sigma_3)$ of positive integers with sum $6$ and
$\sigma_1 > \sigma_2 < \sigma_3$), exactly one has last part $3$, exactly one has last part $2$,
and none has last part $1$.

The compositions counted are $(2, 1, 3)$ and $(3, 1, 2)$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3 (the set `W`).

Formalized by `MetaMathlibExt.downUpCompositionCount_six_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-composition-count-six-three).

## Generating function of down/up compositions with an even number of parts

$F(x, y, z)$ is
the formal power series in $\mathbb{Q}[[x, y, z]]$ whose coefficient of $x^n y^k z^j$ is the
number of down/up compositions of $n$ with $k$ parts and last part $j$ when $k$ is even, and $0$
when $k$ is odd. The empty composition, with last part $0$, contributes the constant term $1$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3.1 (definition of `F`).

Formalized by `MetaMathlibExt.downUpEvenGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-even-gf).

## Generating function of down/up compositions with an odd number of parts

$G(x, y, z)$ is
the formal power series in $\mathbb{Q}[[x, y, z]]$ whose coefficient of $x^n y^k z^j$ is the
number of down/up compositions of $n$ with $k$ parts and last part $j$ when $k$ is odd, and $0$
when $k$ is even.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3.1 (definition of `G`).

Formalized by `MetaMathlibExt.downUpOddGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-odd-gf).

## The auxiliary series $\alpha$ for down/up compositions

In $\mathbb{Q}[[x, y, z]]$ write
$(a; x)_m = \prod_{j=0}^{m-1} (1 - a x^j)$. For a power series $w$ in $\mathbb{Q}[[x, y, z]]$, the
series $\alpha(x, y, w)$ is the coefficientwise convergent sum
$\alpha(x, y, w) = \sum_{n \ge 0} \frac{(-1)^n x^{n^2+n} y^{2n} w^n}{(xw; x)_{2n}}$.

The paper uses it with $w = z$ and with $w = x$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 12, equation (5).

Formalized by `MetaMathlibExt.arndtPalAlpha`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-pal-alpha).

## The auxiliary series $\beta$ for down/up compositions

In $\mathbb{Q}[[x, y, z]]$ write
$(a; x)_m = \prod_{j=0}^{m-1} (1 - a x^j)$. For a power series $w$ in $\mathbb{Q}[[x, y, z]]$, the
series $\beta(x, y, w)$ is the coefficientwise convergent sum
$\beta(x, y, w) = \sum_{n \ge 1} \frac{(-1)^{n+1} x^{n^2+n} y^{2n} w^n}{(1 - x)(xw; x)_{2n-1}}$.

The paper uses it with $w = z$ and with $w = x$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 12, equation (5).

Formalized by `MetaMathlibExt.arndtPalBeta`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-pal-beta).

## Formula for the generating function of even-length down/up compositions

Let
$F(x, y, z) \in \mathbb{Q}[[x, y, z]]$ be the generating function of down/up compositions with an
even number of parts (including the empty composition, with last part $0$) by weight ($x$),
number of parts ($y$) and last part ($z$). For a power series $w$, write
$(xw; x)_m = \prod_{i=1}^{m} (1 - x^i w)$ and let

$$\alpha(x, y, w) = \sum_{n \ge 0} \frac{(-1)^n x^{n^2+n} y^{2n} w^n}{(xw; x)_{2n}}$$

and

$$\beta(x, y, w) = \sum_{n \ge 1} \frac{(-1)^{n+1} x^{n^2+n} y^{2n} w^n}{(1 - x)(xw; x)_{2n-1}},$$

with the sums taken coefficientwise. Then

$$F(x, y, z) = \alpha(x, y, z) + \frac{\alpha(x, y, x)\, \beta(x, y, z)}{1 - \beta(x, y, x)}.$$

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 12 (`jis-2025-25.3.6-thm-12`).

Stated but not proved: `MetaMathlibExt.downUpEvenGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-even-gf-eq).

## Odd-length down/up compositions from even-length ones

Let $F(x, y, z)$ and $G(x, y, z)$
in $\mathbb{Q}[[x, y, z]]$ be the generating functions of down/up compositions with an even,
respectively odd, number of parts by weight ($x$), number of parts ($y$) and last part ($z$).
Then

$$G(x, y, z) = \frac{xyz}{1 - xz}\, F(x, y, xz).$$

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 13 (`jis-2025-25.3.6-thm-13`).

Stated but not proved: `MetaMathlibExt.downUpOddGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#down-up-odd-gf-eq).

## Palindromic Arndt compositions

An Arndt composition of $n$ with $k$ parts is a sequence
$(\sigma_1, \dots, \sigma_k)$ of positive integers with sum $n$ such that
$\sigma_{2i-1} > \sigma_{2i}$ whenever $2i \le k$; it is palindromic when
$\sigma_i = \sigma_{k+1-i}$ for all $i$. For $n, k, m \ge 0$, $p(n, k, m)$ is the number of
palindromic Arndt compositions of $n$ with $k \ge 1$ parts whose middle summand
$\sigma_{\lfloor k/2 \rfloor + 1}$ equals $m$; in particular $p(n, 0, m) = 0$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3 (the set `PA`).

Formalized by `MetaMathlibExt.palindromicArndtCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#palindromic-arndt-count).

## Palindromic Arndt compositions of 5

There is exactly one palindromic Arndt composition of
$5$ with one part and middle summand $5$, exactly one with three parts and middle summand $1$,
and none with three parts and middle summand $2$.

The compositions counted are $(5)$ and $(2, 1, 2)$; the paper reads them off the coefficient of
$x^5$ in the series expansion of the generating function of palindromic Arndt compositions.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3.2 (series expansion of `PA(x, y, 1)`).

Formalized by `MetaMathlibExt.palindromicArndtCount_five`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#palindromic-arndt-count-five).

## Palindromic Arndt generating function

A palindromic Arndt composition of $n$ with
$k \ge 1$ parts is a tuple $(\sigma_1, \dots, \sigma_k)$ of positive integers with sum $n$ such
that $\sigma_{2i-1} > \sigma_{2i}$ whenever $2i \le k$, and $\sigma_i = \sigma_{k+1-i}$ for all
$i$; its middle summand is $\sigma_{\lfloor k/2 \rfloor + 1}$. The generating function
$PA(x, y, z)$ is the formal power series in $x, y, z$ with rational coefficients whose coefficient
of $x^n y^k z^m$ is the number of palindromic Arndt compositions of $n$ with $k$ parts and middle
summand $m$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 3.2 (definition of `PA`).

Formalized by `MetaMathlibExt.palindromicArndtGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#palindromic-arndt-gf).

## Generating function of palindromic Arndt compositions

Let $PA(x, y, z)$ be the
generating function of nonempty palindromic Arndt compositions by weight ($x$), number of parts
($y$) and middle summand ($z$), and let $F(x, y, z)$ be the generating function of down/up
compositions $\sigma_1 > \sigma_2 < \sigma_3 > \cdots$ with an even number of parts by weight
($x$), number of parts ($y$) and last part ($z$). Then, as formal power series over $\mathbb{Q}$,

$$
PA(x, y, z) = \frac{xyz}{1 - xz} F(x^2, y^2, xz) +
\frac{x^3 y^3 z}{(1 - x^2)(1 - xz)} F(x^2, y^2, x^2) -
\frac{x^3 y^3 z}{(1 - xz)(1 - x^3 z)} F(x^2, y^2, x^3 z).
$$

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 14 (`jis-2025-25.3.6-thm-14`).

Stated but not proved: `MetaMathlibExt.palindromicArndtGF_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#palindromic-arndt-gf-eq).

## Colored Arndt compositions

An Arndt composition of $n$ with $k$ parts is a sequence
$(\sigma_1, \dots, \sigma_k)$ of positive integers with sum $n$ such that
$\sigma_{2i-1} > \sigma_{2i}$ for every $i$ with $2i \le k$. In a colored Arndt composition, each
part of size $m$ carries one of $m$ colors. The number $c(n, k)$ of colored Arndt compositions of
$n$ with $k$ parts is therefore the sum of $\sigma_1 \sigma_2 \cdots \sigma_k$ over all Arndt
compositions $(\sigma_1, \dots, \sigma_k)$ of $n$ with $k$ parts.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 4 (definition of colored Arndt compositions).

Formalized by `MetaMathlibExt.coloredArndtCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-count).

## Colored Arndt compositions of 4

Write $m_a$ for a part of size $m$ with color
$a \in \{1, \dots, m\}$. The colored Arndt compositions of $4$ are $(4_1)$, $(4_2)$, $(4_3)$,
$(4_4)$, $(3_a, 1_1)$ for $a \le 3$, and $(2_a, 1_1, 1_1)$ for $a \le 2$. Hence the numbers of
colored Arndt compositions of $4$ with $1$, $2$ and $3$ parts are $c(4, 1) = 4$, $c(4, 2) = 3$
and $c(4, 3) = 2$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 4, list (6).

Formalized by `MetaMathlibExt.coloredArndtCount_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-count-four).

## Generating function of colored Arndt compositions

The bivariate generating function of
colored Arndt compositions, by weight ($x$) and number of parts ($y$), is the power series
$C(x, y) = \sum_{n \ge 0} \left(\sum_{k=0}^{n} c(n, k)\, y^k\right) x^n$ in $\mathbb{Z}[y][[x]]$,
where $c(n, k)$ is the number of colored Arndt compositions of $n$ with $k$ parts.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Section 4 (definition of `C(x, y)`).

Formalized by `MetaMathlibExt.coloredArndtGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-gf).

## Closed form of the generating function of colored Arndt compositions

Let
$C(x, y) = \sum_{n, k} c(n, k)\, x^n y^k$ in $\mathbb{Z}[y][[x]]$, where $c(n, k)$ is the number
of colored Arndt compositions of $n$ with $k$ parts. Then
$C(x, y) \cdot (1 - x - 3x^2 - x^3(2y^2 - 3) - x^4(y^2 - 3) - x^5(3 + y^2) - x^6 + x^7) =
(1 - x)^2 (1 + x)^3 (1 + x^2 + x(y - 2))$.

Since the second factor on the left has constant term $1$, this says that
$C(x, y) = \frac{(1 - x)^2 (1 + x)^3 (1 + x^2 + x(y - 2))}{1 - x - 3x^2 - x^3(2y^2 - 3) -
x^4(y^2 - 3) - x^5(3 + y^2) - x^6 + x^7}$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 17 (`jis-2025-25.3.6-thm-17`).

Stated but not proved: `MetaMathlibExt.coloredArndtGF_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-gf-mul).

## Generating function for the total number of colored Arndt compositions

For $n \ge 0$ let
$c(n, k)$ be the number of colored Arndt compositions of $n$ with $k$ parts, and let
$c(n) = \sum_{k=0}^{n} c(n, k)$ be the total number of colored Arndt compositions of $n$ (so
$c(0) = 1$, counting the empty composition). Then, in the ring $\mathbb{Z}[[x]]$ of formal power
series,

$$\Big(\sum_{n \ge 0} c(n) x^n\Big) (1 - x - 3x^2 + x^3 + 2x^4 - 4x^5 - x^6 + x^7) =
(1 - x)^2 (1 + x)^3 (1 - x + x^2).$$

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Corollary 18 (`jis-2025-25.3.6-cor-18`).

Stated but not proved: `MetaMathlibExt.coloredArndt_total_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-total-mul).

## Generating function of colored Arndt compositions with $k$ parts

For every $k \ge 0$,
let $C_k(x) = \sum_{n \ge 0} c(n, k)\, x^n$ in $\mathbb{Z}[[x]]$, where $c(n, k)$ is the number of
colored Arndt compositions of $n$ with $k$ parts. Then
$C_k(x)\, (1 - x)^{2k} (1 + x)^{3\lfloor k/2 \rfloor} =
x^{k + \lfloor k/2 \rfloor} (x^2 + x + 2)^{\lfloor k/2 \rfloor}$.

Equivalently, since $(1 - x)^{2k} (1 + x)^{3\lfloor k/2 \rfloor}$ has constant term $1$,
$C_k(x) = \frac{x^{k + \lfloor k/2 \rfloor} (x^2 + x + 2)^{\lfloor k/2 \rfloor}}
{(1 - x)^{2k} (1 + x)^{3\lfloor k/2 \rfloor}}$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Theorem 19 (`jis-2025-25.3.6-thm-19`).

Stated but not proved: `MetaMathlibExt.coloredArndt_parts_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-parts-mul).

## Asymptotics of colored Arndt compositions with $k$ parts

For every fixed $k \ge 1$, the
number $c(n, k)$ of colored Arndt compositions of $n$ with $k$ parts satisfies
$c(n, k) \sim \frac{n^{2k-1}}{2^{\lfloor k/2 \rfloor} (2k - 1)!}$ as $n \to \infty$.

## Sources

- Mohammed L. Nadji, Moussa Ahmia, Daniel F. Checa, and José L. Ramírez, *Arndt Compositions with Restricted Parts, Palindromes, and Colored Variants*, Journal of Integer Sequences 28 (2025), Article 25.3.6, Corollary 20 (`jis-2025-25.3.6-cor-20`).

Stated but not proved: `MetaMathlibExt.coloredArndtCount_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsWanted.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#colored-arndt-count-is-equivalent).

## Bivariate generating function of a two-index count

For a function $a$ assigning a natural
number $a(n, m)$ to every pair of natural numbers $n, m$, its bivariate generating function is the
power series $\sum_{n \ge 0} \bigl(\sum_{m = 0}^{n} a(n, m)\, y^m\bigr) x^n$ in
$\mathbb{Z}[y][[x]]$, where $x$ marks the first index (the weight) and $y$ the second. Only the
terms with $m \le n$ enter; for counts with $a(n, m) = 0$ whenever $m > n$ it equals
$\sum_{n, m} a(n, m)\, x^n y^m$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2 (the series `A(x, y)`, `Ap(x, y)`, `Bp(x, y)`, `B(x, y)`, `A_k(x, y)` and `A^{(k)}(x, y)`).

Formalized by `MetaMathlibExt.bivariateCountGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf).

## Coefficients of a bivariate generating function

For every function $a$ assigning a natural
number $a(n, m)$ to each pair of natural numbers and every $n \ge 0$, the coefficient of $x^n$ in
the bivariate generating function of $a$ is the polynomial
$\sum_{m = 0}^{n} a(n, m)\, y^m \in \mathbb{Z}[y]$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2.

Formalized by `MetaMathlibExt.coeff_bivariateCountGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#coeff-bivariate-count-gf).

## The Arndt generating function as a bivariate count series

For a set $S$ of natural
numbers, let $a_S(n, m)$ be the number of Arndt compositions of $n$ with $m$ parts, all parts in
$S$. Then the Arndt generating function $A_S(x, y)$ equals the bivariate generating function
$\sum_{n \ge 0} \sum_{m=0}^{n} a_S(n, m) x^n y^m$ in $\mathbb{Z}[y][[x]]$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2 (definition of `A(x, y)`).

Formalized by `MetaMathlibExt.arndtGF_eq_bivariateCountGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-gf-eq-bivariate-count-gf).

## Anti-palindromic compositions

For natural numbers $n$ and $m$, the number of
anti-palindromic compositions of $n$ with $m$ parts: sequences $(c_1, \dots, c_m)$ of positive
integers with $c_1 + \dots + c_m = n$ and $c_i \ne c_{m+1-i}$ for every $i$ with
$2i \ne m + 1$. That is, each part differs from the part in the mirror position, except the
middle part when $m$ is odd.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2.1 (definition of anti-palindromic compositions, after Andrews, Just, and Simay).

Formalized by `MetaMathlibExt.antiPalindromicCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#anti-palindromic-composition-count).

## Reduced anti-palindromic compositions

For natural numbers $n$ and $m$, this is the number
of compositions $(\sigma_1, \ldots, \sigma_m)$ of $n$ into $m$ positive parts such that
$\sigma_i > \sigma_{m+1-i}$ for every $i$ with $2i < m + 1$.

A composition $(\sigma_1, \ldots, \sigma_m)$ is anti-palindromic when
$\sigma_i \ne \sigma_{m+1-i}$ for every $i$ with $2i \ne m + 1$. Two anti-palindromic compositions
are equivalent when one arises from the other by swapping the entries $\sigma_i$ and
$\sigma_{m+1-i}$ of some of the pairs; each class contains exactly one composition of the form
above, so this is also the number of classes, the reduced anti-palindromic compositions of $n$
with $m$ parts.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2.1 (reduced anti-palindromic compositions and the choice of representative after Theorem 7).

Formalized by `MetaMathlibExt.reducedAntiPalindromicCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#reduced-anti-palindromic-composition-cou).

## Anti-palindromic compositions of 6 with three parts

There are exactly eight
anti-palindromic compositions of $6$ with three parts.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2.1 (each class has `2^{⌊ℓ/2⌋}` members).

Formalized by `MetaMathlibExt.antiPalindromicCompositionCount_six_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#anti-palindromic-composition-count-six-t).

## Reduced anti-palindromic compositions of 6 with three parts

There are exactly four reduced
anti-palindromic compositions of $6$ with three parts.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2.1 (each class has `2^{⌊ℓ/2⌋}` members).

Formalized by `MetaMathlibExt.reducedAntiPalindromicCompositionCount_six_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#reduced-anti-palindromic-composition-cou-2).

## Anti-palindromic compositions of 6 with four parts

There are exactly four
anti-palindromic compositions of $6$ with four parts, and exactly one reduced anti-palindromic
composition of $6$ with four parts.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 2.1 (each class has `2^{⌊ℓ/2⌋}` members).

Formalized by `MetaMathlibExt.antiPalindromicCompositionCount_six_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#anti-palindromic-composition-count-six-f).

## Arndt compositions by last part

An Arndt composition of $n$ is a composition
$(\sigma_1, \ldots, \sigma_\ell)$ of $n$ into positive parts such that $\sigma_{2i-1} > \sigma_{2i}$
for every $i$ with $2i \le \ell$. For natural numbers $n$ and $j$, $b(n, j)$ is the number of
Arndt compositions of $n$, with any number of parts, whose last part is $j$. The empty
composition of $0$ counts as having last part $0$, so $b(0, 0) = 1$ and $b(0, j) = 0$ for
$j \ge 1$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 3 (definition of `b(n, m)` and Table 2).

Formalized by `MetaMathlibExt.arndtLastPartCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-last-part-count).

## Arndt compositions of 6 by last part

Let $b(n, j)$ be the number of Arndt compositions
of $n$ with last part $j$. Then $b(6, 1) = 4$, $b(6, 2) = 2$, $b(6, 3) = 1$ and $b(6, 6) = 1$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 3, Table 2.

Formalized by `MetaMathlibExt.arndtLastPartCount_six`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-last-part-count-six).

## Number of $k$-Arndt compositions

For an integer $k$ and $n, m \ge 0$, $a_k(n, m)$ is the
number of $k$-Arndt compositions of $n$ with $m$ parts: sequences $(c_0, \ldots, c_{m-1})$ of
positive integers with $c_0 + \cdots + c_{m-1} = n$ such that $c_{2i} > c_{2i+1} + k$ for every
$i \ge 0$ with $2i + 1 < m$. For $k = 0$ these are the Arndt compositions.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 4 (definition of `k`-Arndt compositions, after Hopkins and Tangboonduangjit; Theorem 11 treats `k ≥ 0` and `k < 0`).

Formalized by `MetaMathlibExt.kArndtCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-composition-count).

## Sample values of the $k$-Arndt composition counts

Writing $a_k(n, m)$ for the number of
$k$-Arndt compositions of $n$ with $m$ parts, $a_3(7, 2) = 1$, $a_3(7, 3) = 1$ and
$a_{-3}(4, 2) = 3$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 4 (series expansions after Theorem 11).

Formalized by `MetaMathlibExt.kArndtCompositionCount_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-composition-count-examples).

## Number of $k$-block Arndt compositions

For $k \ge 1$ and $n, m \ge 0$, $a^{(k)}(n, m)$ is
the number of $k$-block Arndt compositions of $n$ with $m$ parts: sequences
$(c_0, \ldots, c_{m-1})$ of positive integers with $c_0 + \cdots + c_{m-1} = n$ that strictly
decrease inside each block of $k$ consecutive positions $ki, ki + 1, \ldots, ki + k - 1$ (the last
block may be shorter), that is, $c_i > c_{i+1}$ for every $i$ with $i + 1 < m$ and
$i \not\equiv k - 1 \pmod{k}$. For $k = 2$ these are the Arndt compositions.

The definition is meant for $k \ge 1$; its value at $k = 0$ has no combinatorial meaning.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 5 (definition of `k`-block Arndt compositions).

Formalized by `MetaMathlibExt.blockArndtCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#block-arndt-composition-count).

## Four-part 3-block Arndt compositions of 10

There are exactly $7$ three-block Arndt
compositions of $10$ with $4$ parts, that is, $a^{(3)}(10, 4) = 7$.

They are $(6,2,1,1)$, $(5,3,1,1)$, $(5,2,1,2)$, $(4,3,2,1)$, $(4,3,1,2)$, $(4,2,1,3)$ and
$(3,2,1,4)$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Section 5 (list of the compositions counted by `a^{(3)}(10) = 18`).

Formalized by `MetaMathlibExt.blockArndtCompositionCount_three_ten_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#block-arndt-composition-count-three-ten).

## Alternating sum and recurrence for Arndt compositions

Let $a(n, m)$ be the number of
Arndt compositions of $n$ with $m$ parts, and write $K = n - m - \lfloor m/2 \rfloor$. For all
$n, m \ge 0$: if $m + \lfloor m/2 \rfloor \le n$, then

$$a(n, m) = \sum_{\ell=0}^{K} \binom{m+\ell-1}{\ell} \binom{n-m-\ell-1}{K-\ell} (-1)^{K-\ell},$$

and otherwise $a(n, m) = 0$. Moreover, for all $n \ge 3$ and $m \ge 2$,
$a(n, m) = a(n-1, m) + a(n-2, m) - a(n-3, m) + a(n-3, m-2)$. The binomial coefficients are the
generalized ones, $\binom{r}{k} = r(r-1)\cdots(r-k+1)/k!$ for an integer $r$, so the upper
index $-1$ is allowed and $\binom{-1}{k} = (-1)^k$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 2.

Stated but not proved: `MetaMathlibExt.arndtCompositionCount_eq_alternating_sum_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-eq-alternating-s).

## Positive sum for Arndt compositions

Let $a(n, m)$ be the number of Arndt compositions of
$n$ with $m$ parts, and write $h = \lfloor m/2 \rfloor$. For all $n \ge 0$ and $m \ge 1$: if
$m + h \le n$, then

$$a(n, m) = \sum_{\ell=0}^{\lfloor (n-m-h)/2 \rfloor} \binom{h+\ell-1}{\ell}
\binom{n-2h-2\ell-1}{\lfloor (m-1)/2 \rfloor},$$

and otherwise $a(n, m) = 0$. Here $\binom{-1}{0} = 1$ (this term occurs for $m = 1$).

The paper states it for all $n, m \ge 0$; at $n = m = 0$ it fails ($a(0, 0) = 1$, while the only
term has lower index $\lfloor -1/2 \rfloor = -1$ and vanishes), so the case $m = 0$ is omitted.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 3.

Stated but not proved: `MetaMathlibExt.arndtCompositionCount_eq_positive_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-eq-positive-sum).

## Holonomic recurrence for Arndt compositions

Let $a(n, m)$ be the number of Arndt
compositions of $n$ with $m$ parts. For all $n, m \ge 0$,

$$(m - n - 2 + \lfloor m/2 \rfloor)\, a(n+2, m) + (m - \lfloor m/2 \rfloor)\, a(n+1, m) +
n\, a(n, m) = 0.$$

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 4.

Stated but not proved: `MetaMathlibExt.arndtCompositionCount_holonomic_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-holonomic-recurr).

## Asymptotics of Arndt compositions with a fixed number of parts

Let $a(n, m)$ be the
number of Arndt compositions of $n$ with $m$ parts. For every fixed integer $m \ge 1$,

$$a(n, m) \sim \frac{n^{m-1}}{2^{\lfloor m/2 \rfloor} (m-1)!} \quad (n \to \infty).$$

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Corollary 1.

Stated but not proved: `MetaMathlibExt.arndtCompositionCount_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-count-is-equivalent).

## Arndt compositions are counted by Fibonacci numbers

Let $a(n, m)$ be the number of Arndt
compositions of $n$ with $m$ parts, let $a(n) = \sum_{m=0}^{n} a(n, m)$ be the number of all
Arndt compositions of $n$, and let $F_n$ be the $n$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$).
Then, in $\mathbb{Z}[[x]]$,

$$\Big(\sum_{n \ge 0} a(n) x^n\Big)(1 - x - x^2) = 1 - x^2,$$

and $a(n) = F_n$ for every $n \ge 1$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Corollary 2.

Stated but not proved: `MetaMathlibExt.arndtComposition_total_eq_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-total-eq-fib).

## Expected number of parts of an Arndt composition

Let $a(n, m)$ be the number of Arndt
compositions of $n$ with $m$ parts, and $F_n$ the $n$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$).
Then

$$\frac{1}{F_n} \sum_{m=0}^{n} m\, a(n, m) \sim \left(\frac{3}{\sqrt 5} - 1\right) n
\quad (n \to \infty).$$

Since there are $F_n$ Arndt compositions of $n$ for $n \ge 1$, the left side is the expected
number of parts of a uniformly random Arndt composition of $n$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 5.

Stated but not proved: `MetaMathlibExt.arndtComposition_expected_parts_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-composition-expected-parts-is-equi).

## Generating function of anti-palindromic compositions

Let $ap(n, m)$ be the number of
anti-palindromic compositions of $n$ with $m$ parts, and let
$Ap(x, y) = \sum_{n \ge 0} \sum_{m=0}^{n} ap(n, m)\, x^n y^m \in \mathbb{Z}[y][[x]]$. Then
$Ap(x, y)\,(1 - x - x^2 + x^3 - 2x^3y^2) = 1 - x - x^2 + x^3 + xy - x^3y$, that is,
$Ap(x, y) = (1 - x - x^2 + x^3 + xy - x^3y)/(1 - x - x^2 + x^3 - 2x^3y^2)$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 6.

Stated but not proved: `MetaMathlibExt.bivariateCountGF_antiPalindromic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf-anti-palindromic).

## Generating function of reduced anti-palindromic compositions

Let $b(n, m)$ be the number
of reduced anti-palindromic compositions of $n$ with $m$ parts, and let
$B_p(x, y) = \sum_{n \ge 0} \sum_{m = 0}^{n} b(n, m)\, x^n y^m$ in $\mathbb{Z}[y][[x]]$, where
$x$ marks the weight and $y$ the number of parts. Then

$$B_p(x, y)\,(1 - x - x^2 + x^3 - x^3 y^2) = 1 - x - x^2 + x^3 + xy - x^3 y,$$

that is, $B_p(x, y) = (1 - x - x^2 + x^3 + xy - x^3 y)/(1 - x - x^2 + x^3 - x^3 y^2)$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Corollary 3.

Stated but not proved: `MetaMathlibExt.bivariateCountGF_reducedAntiPalindromic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf-reduced-anti-palindro).

## Arndt compositions and reduced anti-palindromic compositions are equinumerous

For all
natural numbers $n$ and $m$, the number of reduced anti-palindromic compositions of $n$ with $m$
parts equals the number of Arndt compositions of $n$ with $m$ parts, all positive integers being
allowed as parts.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 7.

Stated but not proved: `MetaMathlibExt.reducedAntiPalindromicCompositionCount_eq_arndtCompositionCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#reduced-anti-palindromic-composition-cou-3).

## Generating function of Arndt compositions by last part

Let $b(n, m)$ be the number of
Arndt compositions of $n$ with last part $m$, where the empty composition of $0$ counts as
having last part $0$ (so $b(0, 0) = 1$), and let
$B(x, y) = \sum_{n \ge 0} \sum_{m=0}^{n} b(n, m)\, x^n y^m \in \mathbb{Z}[y][[x]]$. Then
$B(x, y)\,(1 - x - x^2)(1 - xy)(1 - x^2y) =
1 - x - x^2 - x^2y + 2x^3y + 2x^4y - x^5y - x^4y^2$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 8.

Stated but not proved: `MetaMathlibExt.bivariateCountGF_arndtLastPart` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf-arndt-last-part).

## Closed formula for Arndt compositions by last part

Let $F_r$ be the $r$-th Fibonacci
number ($F_0 = 0$, $F_1 = 1$) and $b(n, m)$ the number of Arndt compositions of $n$ with last
part $m$. Define $t_1, t_2 : \mathbb{N} \to \mathbb{N}$ by $t_1(0) = 1$, $t_1(1) = 0$,
$t_1(r) = F_{r-2}$ and $t_2(0) = 0$, $t_2(1) = 1$, $t_2(r) = F_{r-1}$ for $r \ge 2$. Then for all
integers $n \ge 1$ and $m \ge 1$: $b(n, m) = 0$ if $n < m$, $b(n, m) = t_1(n - m)$ if
$m \le n < 2m$, and $b(n, m) = t_1(n - m) + t_2(n - 2m)$ if $n \ge 2m$.

The paper leaves the range of $m$ implicit; at $m = 0$ the printed formula fails ($b(1, 0) = 0$,
while the formula gives $t_1(1) + t_2(1) = 1$), so $m \ge 1$ is assumed.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 9.

Stated but not proved: `MetaMathlibExt.arndtLastPartCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-last-part-count-eq).

## Asymptotics of Arndt compositions with a fixed last part

Let $b(n, m)$ be the number of
Arndt compositions of $n$ with last part $m$, and let $\varphi$ be the golden ratio. For every
fixed integer $m \ge 1$,
$b(n, m) \sim \frac{\varphi^{n-m-2}}{\sqrt{5}} \left(1 + \frac{1}{\varphi^{m-1}}\right)$ as
$n \to \infty$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 10.

Stated but not proved: `MetaMathlibExt.arndtLastPartCount_isEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-last-part-count-is-equivalent).

## Arndt compositions with last part at most or at least $k$

Let $F_n$ be the $n$-th
Fibonacci number ($F_0 = 0$, $F_1 = 1$) and $b(n, j)$ the number of Arndt compositions of $n$
with last part $j$. For all integers $k \ge 1$ and $n \ge 2k + 2$, the number of Arndt
compositions of $n$ with last part at most $k$ is
$\sum_{j=1}^{k} b(n, j) = F_n - F_{n-k-1} - F_{n-2k-2}$, and the number with last part at least
$k$ is $\sum_{j=k}^{n} b(n, j) = F_{n-k} + F_{n-2k}$.

The paper prints the second count as $F_{n-k} - F_{n-2k}$, which is false: for $k = 1$ and
$n = 4$ all $F_4 = 3$ Arndt compositions of $4$ have last part at least $1$, while
$F_3 - F_2 = 1$. The sign $+$ is the one the paper's own consequence uses ($F_{n-2} + F_{n-4}$
compositions with last part greater than $1$), and it is what subtracting the number with last
part at most $k - 1$ from $F_n$ gives.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Corollary 4.

Stated but not proved: `MetaMathlibExt.arndtLastPart_atMost_atLeast` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-last-part-at-most-at-least).

## Generating function of $k$-Arndt compositions for $k \ge 0$

Let $k \ge 0$ be an
integer, let $a_k(n, m)$ be the number of $k$-Arndt compositions of $n$ with $m$ parts, and let
$A_k(x, y) = \sum_{n \ge 0} \sum_{m=0}^{n} a_k(n, m)\, x^n y^m \in \mathbb{Z}[y][[x]]$. Then
$A_k(x, y)\,(1 - x - x^2 + x^3 - x^{3+k}y^2) = (1 - x^2)(1 - x(1 - y))$, that is,
$A_k(x, y) = (1 - x^2)(1 - x(1 - y))/(1 - x - x^2 + x^3 - x^{3+k}y^2)$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 11, case `k ≥ 0`.

Stated but not proved: `MetaMathlibExt.bivariateCountGF_kArndt_nonneg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf-k-arndt-nonneg).

## Generating function of $k$-Arndt compositions for negative $k$

Let $k' \ge 1$ and
$k = -k'$, let $a_k(n, m)$ be the number of $k$-Arndt compositions of $n$ with $m$ parts, and
let $A_k(x, y) = \sum_{n \ge 0} \sum_{m=0}^{n} a_k(n, m)\, x^n y^m \in \mathbb{Z}[y][[x]]$. Then
$A_k(x, y)\,(1 - x - x^2(1 + y^2) + x^3(1 - y^2) + y^2x^{2+k'}) = (1 - x^2)(1 - x(1 - y))$,
that is,
$A_k(x, y) = (1 - x^2)(1 - x(1 - y))/(1 - x - x^2(1 + y^2) + x^3(1 - y^2) + y^2x^{2-k})$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 11, case `k < 0`.

Stated but not proved: `MetaMathlibExt.bivariateCountGF_kArndt_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf-k-arndt-neg).

## Counting $k$-Arndt compositions for nonnegative $k$

Let $k \ge 0$ be an integer and let
$a_k(n) = \sum_{m = 0}^{n} a_k(n, m)$ be the number of $k$-Arndt compositions of $n$. Then, in
$\mathbb{Z}[[x]]$,

$$\Bigl(\sum_{n \ge 0} a_k(n)\, x^n\Bigr)(1 - x - x^2 + x^3 - x^{k+3}) = 1 - x^2,$$

that is, $\sum_{n \ge 0} a_k(n)\, x^n = (1 - x^2)/(1 - x - x^2 + x^3 - x^{k+3})$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Corollary 6, case `k ≥ 0`.

Stated but not proved: `MetaMathlibExt.kArndtComposition_total_gf_nonneg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-composition-total-gf-nonneg).

## Counting $k$-Arndt compositions for negative $k$

Let $k = -k'$ with $k' \ge 1$ an integer,
and let $a_k(n) = \sum_{m = 0}^{n} a_k(n, m)$ be the number of $k$-Arndt compositions of $n$. Then,
in $\mathbb{Z}[[x]]$,

$$\Bigl(\sum_{n \ge 0} a_k(n)\, x^n\Bigr)(1 - x - 2x^2 + x^{2-k}) = 1 - x^2,$$

that is, $\sum_{n \ge 0} a_k(n)\, x^n = (1 - x^2)/(1 - x - 2x^2 + x^{2-k})$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Corollary 6, case `k < 0`.

Stated but not proved: `MetaMathlibExt.kArndtComposition_total_gf_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-composition-total-gf-neg).

## Generating function of block Arndt compositions

Let $k \ge 1$, let $a^{(k)}(n, m)$ be
the number of $k$-block Arndt compositions of $n$ with $m$ parts, and let
$A^{(k)}(x, y) = \sum_{n \ge 0} \sum_{m=0}^{n} a^{(k)}(n, m)\, x^n y^m \in \mathbb{Z}[y][[x]]$.
Then
$A^{(k)}(x, y) \bigl(\prod_{\ell=1}^{k} (1 - x^\ell) - x^{\binom{k+1}{2}} y^k\bigr) =
\sum_{j=0}^{k-1} x^{\binom{j+1}{2}} y^j \prod_{\ell=j+1}^{k} (1 - x^\ell)$.
Equivalently, with $J_j(x, y) = x^{\binom{j+1}{2}} y^j \prod_{\ell=1}^{j} (1 - x^\ell)^{-1}$,
$A^{(k)}(x, y) = \bigl(\sum_{j=0}^{k-1} J_j(x, y)\bigr) / (1 - J_k(x, y))$.

## Sources

- Daniel F. Checa and José L. Ramírez, *Arndt Compositions: A Generating Functions Approach*, INTEGERS 24 (2024), Article A35, Theorem 12.

Stated but not proved: `MetaMathlibExt.bivariateCountGF_blockArndt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtCompositionsGeneratingFunctionsWanted.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#bivariate-count-gf-block-arndt).

## Generalized Arndt compositions

For an integer $k$ and a natural number $n$, $a(n, k)$ is
the number of compositions $(c_1, \dots, c_m)$ of $n$, with any number $m \ge 0$ of parts, such
that $c_{2i-1} > c_{2i} + k$ for every $i$ with $2i \le m$; a final unpaired part is
unconstrained. The empty composition gives $a(0, k) = 1$, and $k = 0$ gives Arndt compositions.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Definition 4.

Formalized by `MetaMathlibExt.kArndtTotalCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-total-count).

## Generalized Arndt counts for compositions of five

The numbers $a(5, k)$ of generalized
Arndt compositions of $5$ (compositions $(c_1, \dots, c_m)$ of $5$ with $c_{2i-1} > c_{2i} + k$
whenever $2i \le m$) are $a(5, 0) = 5$, $a(5, -1) = 10$, $a(5, -2) = 14$ and $a(5, 1) = 3$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Table 9.

Formalized by `MetaMathlibExt.kArndtTotalCount_five`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-total-count-five).

## Compositions into odd or small even parts

For natural numbers $k$ and $n$, $c^{2k}_o(n)$
is the number of compositions of $n$, with any number of parts, in which every part is odd or at
most $2k$. For $k = 0$ these are De Morgan's compositions of $n$ into odd parts.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Definitions 2 and 5.

Formalized by `MetaMathlibExt.oddOrSmallEvenCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#odd-or-small-even-composition-count).

## Compositions of five into odd or small even parts

Let $c^{2k}_o(n)$ be the number of
compositions of $n$ in which every part is odd or at most $2k$. Then $c^0_o(5) = 5$ and
$c^2_o(5) = 14$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Table 3 and the discussion after Theorem 5.

Formalized by `MetaMathlibExt.oddOrSmallEvenCompositionCount_five`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#odd-or-small-even-composition-count-five).

## Compositions into even or small odd parts

For natural numbers $k$ and $n$,
$c^{2k+1}_e(n)$ is the number of compositions of $n$ (sequences of positive integers of any
length, including the empty one, that sum to $n$) in which every part is even or at most
$2k + 1$. In particular $c^{2k+1}_e(0) = 1$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Definition 5.

Formalized by `MetaMathlibExt.evenOrSmallOddCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#even-or-small-odd-composition-count).

## Compositions of $5$ into even or small odd parts

$c^1_e(5) = 10$ and $c^3_e(5) = 15$,
where $c^{2k+1}_e(n)$ is the number of compositions of $n$ in which every part is even or at
most $2k + 1$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Table 6 and the discussion after Theorem 6.

Formalized by `MetaMathlibExt.evenOrSmallOddCompositionCount_five`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#even-or-small-odd-composition-count-five).

## The map $U$ on lists

The map $U$ sends a list $(c_1, c_2, \dots)$ of natural
numbers to the concatenation of the images of its consecutive pairs $(c_1, c_2)$, $(c_3, c_4)$,
and so on, where $1^j$ denotes $j$ parts equal to $1$: a pair $(a, b)$ with $b < a$ goes to
$(1^{a - b - 1}, 2b + 1)$; a pair $(a, b)$ with $b \ge a$ goes to $(1^{a + b - 2k}, 2k)$, where
$k = \lfloor (b - a)/2 \rfloor + 1$ is the integer $k \ge 1$ with $2k - 2 \le b - a < 2k$; and a
final unpaired entry $a$ goes to $1^a$. The empty list goes to itself. The exponent
$a + b - 2k$ is read as $0$ when it is negative, which happens only when $a = 0$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 2 and its proof.

Formalized by `MetaMathlibExt.arndtU`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-u).

## Values of the map $U$

The map $U$ sends $(2, 3)$ to $(1, 1, 1, 2)$, $(1, 4)$ to
$(1, 4)$, $(3, 2)$ to $(5)$, $(1, 1, 1, 2)$ to $(2, 1, 2)$ and $(1, 3, 1)$ to $(4, 1)$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Table 3.

Formalized by `MetaMathlibExt.arndtU_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-u-examples).

## The map $V$ on lists

The map $V$ sends a list $(c_1, c_2, \dots)$ of natural
numbers to the concatenation of the images of its consecutive pairs $(c_1, c_2)$, $(c_3, c_4)$,
and so on, where $1^j$ denotes $j$ parts equal to $1$: a pair $(a, b)$ with $b \le a$ goes to
$(1^{a - b}, 2b)$; a pair $(a, b)$ with $b > a$ goes to $(1^{a + b - 2k - 1}, 2k + 1)$, where
$k = \lfloor (b - a + 1)/2 \rfloor$ is the integer $k \ge 1$ with $2k - 1 \le b - a < 2k + 1$;
and a final unpaired entry $a$ goes to $1^a$. The empty list goes to itself. The exponent
$a + b - 2k - 1$ is read as $0$ when it is negative, which happens only when $a = 0$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 3 and its proof.

Formalized by `MetaMathlibExt.arndtV`, a definition declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-v).

## Values of the map $V$

The map $V$ sends $(2, 3)$ to $(1, 1, 3)$, $(1, 4)$ to $(5)$,
$(4, 1)$ to $(1, 1, 1, 2)$, $(1, 3, 1)$ to $(1, 3, 1)$ and $(2, 2, 1)$ to $(4, 1)$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Table 6.

Formalized by `MetaMathlibExt.arndtV_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-v-examples).

## Arndt compositions and compositions into odd parts are equinumerous

For every natural
number $n$, the number $a(n, 0)$ of Arndt compositions of $n$ (compositions $(c_1, \dots, c_m)$
of $n$ with $c_{2i-1} > c_{2i}$ whenever $2i \le m$) equals the number $c^0_o(n)$ of compositions
of $n$ into odd parts. This includes $n = 0$, where both counts are $1$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 1.

Stated but not proved: `MetaMathlibExt.kArndtTotalCount_zero_eq_odd_compositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-total-count-zero-eq-odd-composit).

## The pairwise map U permutes compositions

For every natural number $n$ there is a
permutation $\sigma$ of the compositions of $n$ such that, for every composition $c$ of $n$, the
list of parts of $\sigma(c)$ is $U(c)$, the result of applying the pairwise map $U$ to the list
of parts of $c$. In particular, $U$ sends compositions of $n$ to compositions of $n$ and permutes
them.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_perm_composition_blocks_eq_arndtU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#exists-perm-composition-blocks-eq-arndt).

## The map $V$ permutes compositions

For every natural number $n$, the map $V$ sends
compositions of $n$ to compositions of $n$, and it is a permutation of the set of compositions
of $n$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 3.

Stated but not proved: `MetaMathlibExt.exists_perm_composition_blocks_eq_arndtV` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#exists-perm-composition-blocks-eq-arndt-2).

## Compositions fixed by $U$ and their Padovan count

A composition $(c_1, \dots, c_m)$ of
$n$ is fixed by the map $U$ if and only if $c_i = 1$ for every odd $i$ and $c_i$ is even for
every even $i$. Let $c_U(n)$ be the number of compositions of $n$ fixed by $U$. Then
$c_U(n) = c_U(n - 2) + c_U(n - 3)$ for every $n \ge 4$, $c_U(1) = 1$, $c_U(2) = 0$,
$c_U(3) = 1$, and $c_U(n) = P_{n-1}$ for every $n \ge 1$, where $P$ is the shifted Padovan
sequence, given by $P_0 = 1$, $P_1 = 0$, $P_2 = 1$ and $P_{j+3} = P_{j+1} + P_j$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Proposition 1.

Stated but not proved: `MetaMathlibExt.arndtU_fixed_iff_and_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-u-fixed-iff-and-count).

## Compositions fixed by $V$ and their Fibonacci count

A composition $(c_1, \dots, c_m)$
of $n$ is fixed by the map $V$ if and only if $c_i = 1$ for every odd $i$ and $c_i$ is odd and
at least $3$ for every even $i$. Let $c_V(n)$ be the number of compositions of $n$ fixed by $V$.
Then $c_V(n) = c_V(n - 2) + c_V(n - 4)$ for every $n \ge 5$, $c_V(1) = c_V(4) = 1$,
$c_V(2) = c_V(3) = 0$, and $c_V(2j) = c_V(2j + 1) = F_{j-1}$ for every $j \ge 1$, where $F$ is
the Fibonacci sequence with $F_0 = 0$ and $F_1 = 1$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Proposition 2.

Stated but not proved: `MetaMathlibExt.arndtV_fixed_iff_and_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#arndt-v-fixed-iff-and-count).

## Recurrences for generalized Arndt counts

Let $a(n, k)$ be the number of generalized
Arndt compositions of $n$ with shift $k$, set $a(m, k) = 0$ for $m < 0$, and note that
$a(0, k) = 1$ counts the empty composition. For every natural number $j$ and every $n \ge 3$,

$$a(n, -j) = a(n - 1, -j) + 2a(n - 2, -j) - a(n - 2 - j, -j),$$

and for every natural number $k$ and every $n \ge 3$,

$$a(n, k) = a(n - 1, k) + a(n - 2, k) - a(n - 3, k) + a(n - 3 - k, k).$$

The paper sets $a(n - 2 - j, -j) = 0$ whenever $n - 2 - j \le 0$; at $n - 2 - j = 0$ that is
false ($j = 1$, $n = 3$: $a(3, -1) = 3$, while $a(2, -1) + 2a(1, -1) - 0 = 4$), and its own
bijection uses the empty composition there. At $n = 2$ the recurrences fail for every shift
(for instance $a(2, k) \ne a(1, k) + 2a(0, k)$), so $n \ge 3$ is assumed.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 4.

Stated but not proved: `MetaMathlibExt.kArndtTotalCount_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-total-count-recurrence).

## Generalized Arndt compositions with negative even shift

For every natural number
$j \ge 1$ and every natural number $n$, the number $a(n, -2j)$ of compositions
$(c_1, \dots, c_m)$ of $n$ with $c_{2i-1} > c_{2i} - 2j$ whenever $2i \le m$ equals the number
$c^{2j}_o(n)$ of compositions of $n$ in which every part is odd or at most $2j$. This includes
$n = 0$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 5.

Stated but not proved: `MetaMathlibExt.kArndtTotalCount_neg_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-total-count-neg-even).

## Generalized Arndt compositions with negative odd shift

For all natural numbers $j$ and
$n$, the number $a(n, -2j - 1)$ of compositions $(c_1, \dots, c_m)$ of $n$ with
$c_{2i-1} > c_{2i} - 2j - 1$ whenever $2i \le m$ equals the number $c^{2j+1}_e(n)$ of
compositions of $n$ in which every part is even or at most $2j + 1$. This includes $n = 0$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Theorem 6.

Stated but not proved: `MetaMathlibExt.kArndtTotalCount_neg_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#k-arndt-total-count-neg-odd).

## Recurrences for even-or-small-odd and odd-or-small-even compositions

For natural
numbers $k$ and $n$, let $c^{2k+1}_e(n)$ be the number of compositions of $n$ in which every part
is even or at most $2k + 1$, and $c^{2k}_o(n)$ the number in which every part is odd or at most
$2k$. If $k \ge 1$ and $n \ge 3$, then

$$c^{2k+1}_e(n) = c^{2k+1}_e(n - 1) + 2c^{2k+1}_e(n - 2) - c^{2k+1}_e(n - 3 - 2k)$$

and

$$c^{2k}_o(n) = c^{2k}_o(n - 1) + 2c^{2k}_o(n - 2) - c^{2k}_o(n - 2 - 2k),$$

where the last term is read as $0$ when its argument is negative.

Both recurrences fail at $n = 2$.

## Sources

- Brian Hopkins and Aram Tangboonduangjit, *Arndt and De Morgan Compositions*, INTEGERS 26 (2026), Article A64, Corollary 1.

Stated but not proved: `MetaMathlibExt.evenOrSmallOdd_oddOrSmallEven_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ArndtDeMorganCompositionsWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html#even-or-small-odd-odd-or-small-even-recu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arndt compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/arndt-compositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/arndt-compositions)
