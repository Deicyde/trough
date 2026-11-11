---
declaration: section
origin: cited
lean: MetaMathlibExt.restrictedSumset_two_zero_one_two, MetaMathlibExt.atLeastDistinctSumset, MetaMathlibExt.atLeastDistinctSumset_three_two_zero_one_two, MetaMathlibExt.cauchy_davenport_nsmul, MetaMathlibExt.dias_da_silva_hamidoune, MetaMathlibExt.vosper_nsmul, MetaMathlibExt.nathanson_restrictedSumset_inverse, MetaMathlibExt.freiman_three_k_sub_four
statement: formalized
---

# Sumsets with at least r distinct terms

15 results, 3 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html).

## Restricted twofold sumset of \{0, 1, 2}

In the integers, the restricted sumset
$2^{\wedge}\{0, 1, 2\}$, the set of sums of two distinct elements of $\{0, 1, 2\}$, equals
$\{1, 2, 3\}$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Section 1 (definition of `h^A`).

Formalized by `MetaMathlibExt.restrictedSumset_two_zero_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#restricted-sumset-two-zero-one-two).

## Sums with at least $r$ distinct terms

Let $G$ be an additive commutative monoid, $A$ a
finite subset of $G$ and $h, r$ natural numbers. The sumset $h^{(\ge r)}A$ is the set of all sums
of $h$ elements of $A$, repetitions allowed, in which at least $r$ distinct elements occur, that
is, the elements $\sum_{a \in B} x_a a$ with $B \subseteq A$, $|B| \ge r$, positive integers
$x_a$ and $\sum_{a \in B} x_a = h$.

For $r = 1$ and $h \ge 1$ it is the $h$-fold sumset $hA$; for $r = h$ it is the restricted
sumset $h^{\wedge}A$ of sums of $h$ distinct elements of $A$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Section 1, Definition 1.

Formalized by `MetaMathlibExt.atLeastDistinctSumset`, a definition declared in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#at-least-distinct-sumset).

## Example of a sumset with at least two distinct terms

In the integers, the set of sums of
three elements of $\{0, 1, 2\}$, repetitions allowed, in which at least two distinct elements
occur is $3^{(\ge 2)}\{0, 1, 2\} = \{1, 2, 3, 4, 5\}$; the sums $0$ and $6$ need a single
repeated term.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Section 1, Definition 1.

Formalized by `MetaMathlibExt.atLeastDistinctSumset_three_two_zero_one_two`, a theorem declared in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#at-least-distinct-sumset-three-two-zero).

## Cauchy–Davenport theorem for $h$-fold sumsets

Let $p$ be a prime, $A$ a nonempty subset
of $\mathbb{Z}/p\mathbb{Z}$ with $|A| = k$, and $h \ge 1$ a natural number. Then the $h$-fold
sumset $hA = \{a_1 + \dots + a_h : a_1, \dots, a_h \in A\}$ satisfies
$|hA| \ge \min(p,\ hk - h + 1)$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 1 (Cauchy–Davenport theorem).

Stated but not proved: `MetaMathlibExt.cauchy_davenport_nsmul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#cauchy-davenport-nsmul).

## Dias da Silva–Hamidoune theorem

Let $p$ be a prime, $A$ a nonempty subset of
$\mathbb{Z}/p\mathbb{Z}$ with $|A| = k$, and $h$ a natural number with $1 \le h \le k$. Then the
restricted sumset $h^{\wedge}A$ of sums of $h$ distinct elements of $A$ satisfies
$|h^{\wedge}A| \ge \min(p,\ hk - h^2 + 1)$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 2 (Dias da Silva–Hamidoune theorem).

Stated but not proved: `MetaMathlibExt.dias_da_silva_hamidoune` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#dias-da-silva-hamidoune).

## Vosper's theorem for iterated sumsets

Let $p$ be a prime, let $A$ be a subset of the
cyclic group $\mathbb{Z}/p\mathbb{Z}$ with $k = |A| \ge 2$ elements, let $h \ge 2$ be an integer,
and let $hA = \{a_1 + \dots + a_h : a_1, \dots, a_h \in A\}$ be the $h$-fold sumset of $A$. If
$|hA| = hk - h + 1$ and $hk - h + 1 \le p - 2$, then $A$ is an arithmetic progression of
length $k$ in $\mathbb{Z}/p\mathbb{Z}$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 3 (Vosper's theorem).

Stated but not proved: `MetaMathlibExt.vosper_nsmul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#vosper-nsmul).

## Nathanson's inverse theorem for restricted sumsets

Let $A$ be a finite set of integers
with $k = |A| \ge 5$ elements and let $h$ be an integer with $2 \le h \le k - 2$. Write
$h^{\wedge} A$ for the restricted sumset of $A$, the set of sums of $h$ distinct elements of
$A$. If $|h^{\wedge} A| = hk - h^2 + 1$, then $A$ is an arithmetic progression of length $k$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 4 (Nathanson).

Stated but not proved: `MetaMathlibExt.nathanson_restrictedSumset_inverse` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#nathanson-restricted-sumset-inverse).

## Freiman's $3k - 4$ theorem

Let $A$ be a finite set of integers with $|A| = k \ge 3$,
$\min A = 0$ and $\gcd(A) = 1$, and let $b$ be a natural number. If
$|2A| = 2k - 1 + b \le 3k - 4$, where $2A = \{a + a' : a, a' \in A\}$, then $A$ is contained in
an arithmetic progression of length at most $k + b$.

Since $|2A| \ge 2k - 1$ always, taking $b$ to be a natural number loses nothing.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 5 (Freiman's `3k - 4` theorem).

Stated but not proved: `MetaMathlibExt.freiman_three_k_sub_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#freiman-three-k-sub-four).

## Plagne's theorem on the smallest iterated sumsets in cyclic groups

Let $m$, $k$ and $h$
be natural numbers with $1 \le k \le m$ and $h \ge 1$. For a subset $A$ of
$\mathbb{Z}_m = \mathbb{Z}/m\mathbb{Z}$ let $hA = \{a_1 + \dots + a_h : a_1, \dots, a_h \in A\}$
be its $h$-fold sumset. Then the minimum of $|hA|$ over all $k$-element subsets
$A \subseteq \mathbb{Z}_m$ is

$$\min\{(h \lceil k/d \rceil - h + 1)\, d : d \text{ a positive divisor of } m\}.$$

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 6 (Plagne).

Stated but not proved: `MetaMathlibExt.plagne_min_nsmul_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#plagne-min-nsmul-card).

## Bajnok's lemma on subset sums in $\mathbb{Z}/d\mathbb{Z}$

Let $d$ and $t$ be natural
numbers with $1 \le t \le d - 1$. Then every $\ell \in \mathbb{Z}/d\mathbb{Z}$ is the sum of the
elements of some $t$-element subset $L \subseteq \mathbb{Z}/d\mathbb{Z}$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Lemma 1 (Bajnok).

Stated but not proved: `MetaMathlibExt.exists_card_eq_sum_eq_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#exists-card-eq-sum-eq-zmod).

## Decomposition of sums with at least $r$ distinct terms

Let $G$ be an abelian group, $A$
a nonempty finite subset of $G$, and $r, h$ natural numbers with $1 \le r \le |A|$ and $r \le h$.
Write $h^{(\ge r)}A$ for the set of sums of $h$ elements of $A$, repetitions allowed, in which at
least $r$ distinct elements occur, $(h - r)A$ for the set of sums of $h - r$ elements of $A$,
repetitions allowed (so $0A = \{0\}$), and $r^{\wedge}A$ for the restricted sumset of sums of
$r$ distinct elements of $A$. Then $h^{(\ge r)}A = (h - r)A + r^{\wedge}A$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Lemma 2, equation (5).

Stated but not proved: `MetaMathlibExt.atLeastDistinctSumset_eq_nsmul_add_restrictedSumset` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#at-least-distinct-sumset-eq-nsmul-add-re).

## Sharp lower bound for sums with at least $r$ distinct terms modulo a prime

Let $p$ be a
prime, and for natural numbers $h, r$ and a finite set $A \subseteq \mathbb{Z}/p\mathbb{Z}$ write
$h^{(\ge r)}A$ for the set of sums of $h$ elements of $A$, repetitions allowed, in which at least
$r$ distinct elements occur. If $A$ is nonempty with $|A| = k$, $1 \le r \le k$ and $r \le h$,
then $|h^{(\ge r)}A| \ge \min\{p,\ h(k - 1) - r(r - 1) + 1\}$. The bound is sharp: for all
natural numbers $k, r, h$ with $1 \le r \le k \le p$, $r \le h$ and
$h(k - 1) - r(r - 1) + 1 \le p$ there is a set $A \subseteq \mathbb{Z}/p\mathbb{Z}$ with
$|A| = k$ and $|h^{(\ge r)}A| = h(k - 1) - r(r - 1) + 1$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 9, equation (6).

Stated but not proved: `MetaMathlibExt.atLeastDistinctSumset_card_ge_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#at-least-distinct-sumset-card-ge-zmod).

## Inverse theorem for sums with at least $r$ distinct terms modulo a prime

Let $p$ be a
prime, let $A \subseteq \mathbb{Z}/p\mathbb{Z}$ be a set with $|A| = k \ge 2$, and let $r, h$ be
natural numbers with $1 \le r \le k$ and $h \ge r + 2$. Write $h^{(\ge r)}A$ for the set of sums
of $h$ elements of $A$, repetitions allowed, in which at least $r$ distinct elements occur. If
$|h^{(\ge r)}A| = h(k - 1) - r(r - 1) + 1$ and $h(k - 1) - r(r - 1) + 1 \le p - 2$, then $A$ is
an arithmetic progression of length $k$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 11.

Stated but not proved: `MetaMathlibExt.atLeastDistinctSumset_inverse_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#at-least-distinct-sumset-inverse-zmod).

## Lower bound and inverse theorem for sums with at least $r$ distinct terms in $\mathbb{Z}$

Let $A$ be a nonempty finite set of integers with $|A| = k$, and let $r, h$ be natural numbers
with $1 \le r \le k$, $r \le h$ and $h \ge 2$. Write $h^{(\ge r)}A$ for the set of sums of $h$
elements of $A$, repetitions allowed, in which at least $r$ distinct elements occur. Then
$|h^{(\ge r)}A| \ge h(k - 1) - r(r - 1) + 1$. If equality holds and either $k \ge 2$ and
$h \ge r + 2$, or $k \ge 5$, $2 \le r \le k - 2$ and $h \in \{r, r + 1\}$, then $A$ is an
arithmetic progression of length $k$.

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 12, equation (7).

Stated but not proved: `MetaMathlibExt.atLeastDistinctSumset_card_ge_int` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#at-least-distinct-sumset-card-ge-int).

## Lev's lower bound for iterated sumsets

Let $A$ be a finite set of integers with
$k = |A| \ge 3$ elements, smallest element $\min A = 0$ and $\gcd(A) = 1$. For $n \ge 1$ let
$nA = \{a_1 + \dots + a_n : a_1, \dots, a_n \in A\}$ be the $n$-fold sumset of $A$. Then for
every integer $h \ge 2$,

$$|hA| \ge |(h - 1)A| + \min\{\max A,\ h(k - 2) + 1\}.$$

## Sources

- Jagannath Bhanja, *Sumsets with a Minimum Number of Distinct Terms*, INTEGERS 25 (2025), Article A12, Theorem 13 (Lev).

Stated but not proved: `MetaMathlibExt.lev_nsmul_card_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumsetsMinimumDistinctTermsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html#lev-nsmul-card-ge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sumsets with at least r distinct terms](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sumsets-with-at-least-r-distinct-terms)
