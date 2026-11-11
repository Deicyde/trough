---
declaration: section
origin: cited
lean: MetaMathlibExt.DelannoyConstructions.delannoy_eq_sum_choose_mul_choose_two_pow, MetaMathlibExt.DelannoyConstructions.choose_add_choose_succ_modEq_two, MetaMathlibExt.DelannoyConstructions.genDelannoyUpper, MetaMathlibExt.DelannoyConstructions.genDelannoyLower, MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_zero_two_two, MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_one_three_two, MetaMathlibExt.DelannoyConstructions.genDelannoyLower_one_two_two, MetaMathlibExt.DelannoyConstructions.genDelannoyLower_zero
statement: formalized
---

# Generalized Delannoy numbers

21 results, 6 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html).

## Delannoy numbers as a sum of powers of two

For all natural numbers $m$ and $n$, the
Delannoy number $D(m, n)$, that is, the Delannoy triangle entry $T(m + n, m; 1)$, satisfies
$D(m, n) = \sum_{j=0}^{\min(m, n)} \binom{m}{j} \binom{n}{j} 2^j$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 8 (`jis-2024-24.1.8-thm-8`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.delannoy_eq_sum_choose_mul_choose_two_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#delannoy-eq-sum-choose-mul-choose-two-po).

## Parity of a sum of adjacent binomial coefficients

For all natural numbers $n$ and $k$
with $k \ge 1$, $\binom{n}{k} + \binom{n+1}{k} \equiv \binom{n}{k-1} \pmod 2$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Lemma 15 (`jis-2024-24.1.8-lem-15`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.choose_add_choose_succ_modEq_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#choose-add-choose-succ-mod-eq-two).

## Generalized Delannoy number with upper index

For natural numbers $k$, $m$ and $n$, the
generalized Delannoy number $D^k(m, n)$ is the natural number

$$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}.$$

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Section 1 (definition of `D^k(m, n)`).

Formalized by `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper`, a definition declared in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper).

## Lower generalized Delannoy number

For natural numbers $k$, $m$ and $n$, the generalized
Delannoy number $D_k(m, n)$ is

$$D_k(m, n) = \sum_{j=0}^{n} \binom{m + n - k - j}{n - k} \binom{n}{j},$$

where each subtraction is truncated at $0$. The definition is intended for $m, n \ge k$, where
no truncation occurs.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Section 1 (definition of `D_k(m, n)`).

Formalized by `MetaMathlibExt.DelannoyConstructions.genDelannoyLower`, a definition declared in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-lower).

## An upper generalized Delannoy number equal to $13$

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. Then $D^0(2, 2) = 13$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Table 1.

Formalized by `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_zero_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-zero-two-two).

## An upper generalized Delannoy number equal to $44$

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. Then $D^1(3, 2) = 44$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Table 1.

Formalized by `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_one_three_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-one-three-two).

## A value of the lower generalized Delannoy number

The lower generalized Delannoy number
$D_1(2, 2)$ equals $8$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Section 1 (central theorem `D_k(m, n) = 2^k D^k(n - k, m - k)`).

Formalized by `MetaMathlibExt.DelannoyConstructions.genDelannoyLower_one_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-lower-one-two-two).

## The lower and upper generalized Delannoy numbers agree at index zero

For natural
numbers $k$, $m$ and $n$, let
$D_k(m, n) = \sum_{j=0}^{n} \binom{m + n - k - j}{n - k} \binom{n}{j}$ (with subtraction
truncated at $0$) and
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ be the lower
and upper generalized Delannoy numbers. Then $D_0(m, n) = D^0(m, n)$ for all natural numbers
$m$ and $n$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Section 1.

Formalized by `MetaMathlibExt.DelannoyConstructions.genDelannoyLower_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-lower-zero).

## Horizontal sum identity for the upper generalized Delannoy numbers

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. For all natural numbers $k$, $m$ and $n$,
$D^k(m, n) + D^k(m, n + 1) = 2 D^{k+1}(m, n)$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 3 (`jis-2024-24.1.8-thm-3`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_add_succ_right` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-add-succ-right).

## Vertical sum identity for the upper generalized Delannoy numbers

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. For all natural numbers $k$, $m$ and $n$ with $k \ge 1$,
$D^k(m, n) + D^k(m + 1, n) = D^{k-1}(m + 1, n + 1)$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 4 (`jis-2024-24.1.8-thm-4`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_add_succ_left` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-add-succ-left).

## Horizontal difference identity for the upper generalized Delannoy numbers

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. For all natural numbers $k$, $m$ and $n$ with $m \ge 1$,
$D^k(m, n + 1) - D^k(m, n) = 2 D^{k+1}(m - 1, n)$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Corollary 5 (`jis-2024-24.1.8-cor-5`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_succ_right_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-succ-right-sub).

## Vertical difference identity for the upper generalized Delannoy numbers

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. For all natural numbers $k$, $m$ and $n$ with $k \ge 1$,
$D^k(m + 1, n) - D^k(m, n) = D^{k-1}(m + 1, n)$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Corollary 6 (`jis-2024-24.1.8-cor-6`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_succ_left_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-succ-left-sub).

## Relationship identities for generalized Delannoy numbers

The four relationship identities for `D_k` (`k ≥ 1`, `m, n ≥ k`):
`D_k(m, n) + D_k(m, n + 1) = 2 D_(k-1)(m, n)`, `D_k(m, n) + D_k(m + 1, n) = D_(k+1)(m + 1, n + 1)`,
`D_k(m, n + 1) - D_k(m, n) = 2 D_(k-1)(m - 1, n)`, `D_k(m + 1, n) - D_k(m, n) = D_(k+1)(m + 1, n)`.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 7 (`jis-2024-24.1.8-thm-7`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyLower_relations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-lower-relations).

## Lower generalized Delannoy numbers as a sum of powers of two

For natural numbers $k$, $m$,
$n$ with $m \ge k$ and $n \ge k$, the lower generalized Delannoy number $D_k(m, n)$ satisfies
$D_k(m, n) = \sum_{j=0}^{\min(m-k, n-k)} \binom{m-k}{j} \binom{n}{j+k} 2^{j+k}$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 9 (`jis-2024-24.1.8-thm-9`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyLower_eq_sum_two_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-lower-eq-sum-two-pow).

## Powers-of-two formula for the upper generalized Delannoy numbers

For natural numbers $k$, $m$ and $n$, write
$D^k(m, n) = \sum_{j=0}^{n} \binom{m + n + k - j}{n + k} \binom{n}{j}$ for the upper
generalized Delannoy numbers. For all natural numbers $k$, $m$ and $n$,

$$D^k(m, n) = \sum_{j=0}^{\min(m, n)} \binom{m + k}{j + k} \binom{n}{j} 2^j.$$

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 10 (`jis-2024-24.1.8-thm-10`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoyUpper_eq_sum_two_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-upper-eq-sum-two-pow).

## Unified power-of-two sums for generalized Delannoy numbers

For natural numbers $k$, $m$,
$n$, write $D_k(m, n)$ and $D^k(m, n)$ for the lower and upper generalized Delannoy numbers. If
$m \ge k$ and $n \ge k$, then
$D_k(m, n) = \sum_{j=k}^{\min(m, n)} \binom{m-k}{j-k} \binom{n}{j} 2^j$; and, for all $k$, $m$, $n$,
$D^k(m, n) = \sum_{j=0}^{\min(m, n)} \binom{m+k}{j+k} \binom{n}{j} 2^j$.

With the convention $D_{-k} = D^k$, the second formula is the first with $k$ replaced by $-k$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 11 (`jis-2024-24.1.8-thm-11`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.genDelannoy_eq_sum_two_pow_unified` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#gen-delannoy-eq-sum-two-pow-unified).

## Parity of adjacent rows of a Delannoy array

Let $R(m, n)$, for $m, n \in \mathbb{N}$, be
integers with $R(m+1, n+1) = R(m, n+1) + R(m+1, n) + R(m, n)$ for all $m, n$, and let
$m \in \mathbb{N}$. If $R(m, 0) \equiv R(m+1, 0) \pmod 2$, then $R(m, i) \equiv R(m+1, i) \pmod 2$
for all $i$; if $R(m, 0) \not\equiv R(m+1, 0) \pmod 2$, then
$R(m, i) \not\equiv R(m+1, i) \pmod 2$ for all $i$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 13 (`jis-2024-24.1.8-thm-13`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.delannoyArray_rows_parity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#delannoy-array-rows-parity).

## Rows of iterated horizontal sums of a Delannoy array agree mod 2

Let $R(m, n)$, for
$m, n \in \mathbb{N}$, be integers with $R(m+1, n+1) = R(m, n+1) + R(m+1, n) + R(m, n)$ for all
$m, n$. For an array $S$ let $(HS)(m, n) = S(m, n) + S(m, n+1)$, and write $R^i = H^i R$ for the
$i$-fold horizontal sum. Then for every $i \ge 1$ and all $m, m', n \in \mathbb{N}$,
$R^i(m, n) \equiv R^i(m', n) \pmod 2$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Corollary 14 (`jis-2024-24.1.8-cor-14`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.delannoyArray_horizontalSum_rows_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#delannoy-array-horizontal-sum-rows-mod-e).

## Parity of iterated horizontal sums of a Delannoy array with binomial seeds

Let $R(m, n)$,
for $m, n \in \mathbb{N}$, be integers with $R(m+1, n+1) = R(m, n+1) + R(m+1, n) + R(m, n)$ for
all $m, n$. For an array $S$ let $(HS)(m, n) = S(m, n) + S(m, n+1)$, and write $R^i = H^i R$ for
the $i$-fold horizontal sum, so $R^0 = R$. Let $k \in \mathbb{N}$ and suppose
$R(0, n) = \binom{k+n}{k}$ for all $n$; the values $R(m, 0)$ for $m \ge 1$ are arbitrary. Then
every entry of $R^{k+1}$ is even, and for every $j \le k$ some entry of $R^j$ is odd.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Lemma 16 (`jis-2024-24.1.8-lem-16`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.delannoyArray_binomial_seeds_parity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#delannoy-array-binomial-seeds-parity).

## First horizontal sums of a Delannoy array with binomial seeds

Let $R(m, n)$, for
$m, n \in \mathbb{N}$, be integers with $R(m+1, n+1) = R(m, n+1) + R(m+1, n) + R(m, n)$ for all
$m, n$. Let $k \ge 1$ and suppose $R(0, n) = \binom{k+n}{k}$ for all $n$. Then for all $m$ and
$n$, $R(m, n) + R(m, n+1) \equiv \binom{k+n}{k-1} \pmod 2$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 17 (`jis-2024-24.1.8-thm-17`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.delannoyArray_binomial_seeds_horizontalSum_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#delannoy-array-binomial-seeds-horizontal).

## Powers of two dividing iterated horizontal sums of a Delannoy array

Let $R(m, n)$, for
$m, n \in \mathbb{N}$, be integers with $R(m+1, n+1) = R(m, n+1) + R(m+1, n) + R(m, n)$ for all
$m, n$. For an array $S$ let $(HS)(m, n) = S(m, n) + S(m, n+1)$, and write $R^i = H^i R$ for the
$i$-fold horizontal sum. Let $k, i \in \mathbb{N}$ with $i \ge 1$, and suppose
$R(0, n) = \binom{k+n}{k}$ for all $n$. Then every entry of $R^{k+i}$ is divisible by $2^i$, and
some entry of $R^{k+i}$ is not divisible by $2^{i+1}$.

## Sources

- Steven Edwards and William Griffiths, *Delannoy Constructions*, Journal of Integer Sequences 27 (2024), Article 24.1.8, Theorem 18 (`jis-2024-24.1.8-thm-18`).

Stated but not proved: `MetaMathlibExt.DelannoyConstructions.delannoyArray_binomial_seeds_two_pow_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DelannoyConstructionsWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html#delannoy-array-binomial-seeds-two-pow-dv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Delannoy numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/generalized-delannoy-numbers)
