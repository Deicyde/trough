---
declaration: section
origin: cited
lean: MetaMathlibExt.compositionOddMinusEven, MetaMathlibExt.compositionOddMinusEven_zero_true, MetaMathlibExt.IsHuangSmallPartPlacement, MetaMathlibExt.isHuangSmallPartPlacement_of_forall_le, MetaMathlibExt.sum_distincts_neg_one_pow_card, MetaMathlibExt.compositionOddMinusEven_parts_gt_one, MetaMathlibExt.compositionOddMinusEven_parts_ge, MetaMathlibExt.sum_distincts_mod_four_mul_neg_one_pow_card
statement: formalized
---

# Even and odd compositions

17 results, 4 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html).

## Signed count of compositions

For a natural number $N$ and a property $P$ of compositions
of $N$, the signed count of the compositions of $N$ satisfying $P$ is the number of them with an
odd number of parts minus the number with an even number of parts. Equivalently, it is the sum
of $(-1)^{\ell(c) + 1}$ over all compositions $c$ of $N$ satisfying $P$, where $\ell(c)$ is the
number of parts of $c$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Section 1.

Formalized by `MetaMathlibExt.compositionOddMinusEven`, a definition declared in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even).

## Signed count of the compositions of zero

The only composition of $0$ is the empty one,
which has no parts and so is even. Hence the signed count of all compositions of $0$, the number
of odd compositions minus the number of even ones, is $-1$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Section 1.

Formalized by `MetaMathlibExt.compositionOddMinusEven_zero_true`, a theorem declared in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-zero-true).

## Huang's placement condition for small parts

Let $k$ be a natural number. A finite
sequence $(a_0, \dots, a_{\ell - 1})$ of natural numbers satisfies the placement condition for $k$
when every entry $a_i < k$ has a preceding entry and a following entry, the preceding entry
satisfies $a_{i-1} \ge k$, and the following entry $a_{i+1}$ is either the last entry (that is,
$i + 2 = \ell$) or satisfies $a_{i+1} > k$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 15.

Formalized by `MetaMathlibExt.IsHuangSmallPartPlacement`, a definition declared in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#is-huang-small-part-placement).

## Sequences without small parts satisfy Huang's placement condition

If every entry of a
finite sequence of natural numbers is at least $k$, then the sequence satisfies Huang's placement
condition for $k$, vacuously.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 15.

Formalized by `MetaMathlibExt.isHuangSmallPartPlacement_of_forall_le`, a theorem declared in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#is-huang-small-part-placement-of-forall).

## Legendre's identity for partitions into distinct parts

For a natural number $n$, let
$E(n)$ and $O(n)$ be the numbers of partitions of $n$ into distinct parts with an even and an
odd number of parts, respectively. If $2n = j(3j + 1)$ or $2n = j(3j - 1)$ for some integer
$j \ge 0$, then $E(n) - O(n) = (-1)^j$; otherwise $E(n) - O(n) = 0$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 1 (Legendre) (`jis-2024-24.6.5-thm-1`).

Stated but not proved: `MetaMathlibExt.sum_distincts_neg_one_pow_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#sum-distincts-neg-one-pow-card).

## Signed count of compositions with parts greater than one

For every $n \ge 0$, among the
compositions of $n + 1$ whose parts are all greater than $1$, the number with an odd number of
parts minus the number with an even number of parts is $(-1)^j$ if $n = 3j + 1$ or $n = 3j + 2$
for some $j \ge 0$, and $0$ otherwise.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 5 (`jis-2024-24.6.5-thm-5`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_parts_gt_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-parts-gt-one).

## Signed count of compositions with parts at least $k$

Let $k, n \ge 1$. Among the
compositions of $n + k - 1$ whose parts are all at least $k$, the number with an odd number of
parts minus the number with an even number of parts equals
$\sum_{j=0}^{\lfloor (n-1)/k \rfloor} (-1)^j \binom{n-1-j(k-1)}{j}$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 8 (`jis-2024-24.6.5-thm-8`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_parts_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-parts-ge).

## Nyirenda's identity for distinct parts modulo a multiple of four

Let $r \ge 1$ and $n$
be natural numbers, and let $E(n)$ and $O(n)$ be the numbers of partitions of $n$ into distinct
parts, each congruent to $0$, $2r + 1$ or $2r - 1$ modulo $4r$, with an even and an odd number
of parts, respectively. If $n = j(2rj + 1)$ or $n = j(2rj - 1)$ for some integer $j \ge 0$, then
$E(n) - O(n) = (-1)^j$; otherwise $E(n) - O(n) = 0$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 9 (Nyirenda) (`jis-2024-24.6.5-thm-9`).

Stated but not proved: `MetaMathlibExt.sum_distincts_mod_four_mul_neg_one_pow_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#sum-distincts-mod-four-mul-neg-one-pow-c).

## Nyirenda's identity for distinct parts modulo an odd number

Let $r \ge 1$ and $n$ be
natural numbers, and let $E(n)$ and $O(n)$ be the numbers of partitions of $n$ into distinct
parts, each congruent to $0$, $r$ or $r + 1$ modulo $2r + 1$, with an even and an odd number of
parts, respectively. If $2n = j((2r + 1)j + 1)$ or $2n = j((2r + 1)j - 1)$ for some integer
$j \ge 0$, then $E(n) - O(n) = (-1)^j$; otherwise $E(n) - O(n) = 0$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 9 (Nyirenda) (`jis-2024-24.6.5-thm-9`).

Stated but not proved: `MetaMathlibExt.sum_distincts_mod_two_mul_add_one_neg_one_pow_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#sum-distincts-mod-two-mul-add-one-neg-on).

## Signed count of compositions with parts at least $k$ in a residue class

Let $k, n \ge 1$
and $r > s \ge 0$. Among the compositions of $n + k - 1$ whose parts are all at least $k$ and
congruent to $k + s$ modulo $r$, the number with an odd number of parts minus the number with an
even number of parts is the sum of $(-1)^j \binom{i+j}{i}$ over all $i, j \ge 0$ with
$ri + j(k+s) + s + 1 = n$ (an empty sum when $n \le s$).

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 10 (`jis-2024-24.6.5-thm-10`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_parts_ge_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-parts-ge-mod).

## Signed count of residue-class compositions with parts at least $r - s$

Let $r > s \ge 0$,
let $k = r - s$ and let $n \ge 1$. Among the compositions of $n + k - 1$ whose parts are all at
least $k$ and congruent to $k + s$ modulo $r$, the number with an odd number of parts minus the
number with an even number of parts is $1$ if $n = s + 1$ and $0$ otherwise.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Corollary 12 (`jis-2024-24.6.5-cor-12`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_parts_ge_modEq_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-parts-ge-mod-2).

## Signed count of residue-class compositions with parts at least $2r - s$

Let $r > s \ge 0$,
let $k = 2r - s$ and let $n \ge 1$. Among the compositions of $n + k - 1$ whose parts are all at
least $k$ and congruent to $k + s$ modulo $r$, let $b^{r,s}_{k,n}$ be the number with an odd
number of parts minus the number with an even number of parts. Then $b^{r,s}_{k,n} = (-1)^j$ if
$n = 3rj + s + 1$ or $n = 3rj + r + s + 1$ for some $j \ge 0$, and $b^{r,s}_{k,n} = 0$ otherwise.

The source record writes this quantity as $d^{r,s}_{k,n}$; the paper's proof computes
$b^{r,s}_{k,n}$, the quantity stated here.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Corollary 13 (`jis-2024-24.6.5-cor-13`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_parts_ge_modEq_two_mul_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-parts-ge-mod-3).

## Franklin's partition identity

Let $k \ge 1$ and let $m$ and $n$ be natural numbers. The
number of partitions of $n$ in which exactly $m$ distinct part sizes occur at least $k$ times
equals the number of partitions of $n$ in which exactly $m$ distinct part sizes are divisible by
$k$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 14 (Franklin) (`jis-2024-24.6.5-thm-14`).

Stated but not proved: `MetaMathlibExt.card_partition_franklin` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#card-partition-franklin).

## Huang's Franklin-type identity for compositions

Let $k \ge 1$, $m \ge 0$ and $n \ge 1$.
The number of compositions of $n$ with exactly $m$ parts not congruent to $1$ modulo $k$, all of
which are greater than $k$, equals the number of compositions of $n + k - 1$ with exactly $m$
parts less than $k$ in which every part less than $k$ is preceded by a part at least $k$ and is
followed by a part that is either the last part or greater than $k$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 15 (Huang) (`jis-2024-24.6.5-thm-15`).

Stated but not proved: `MetaMathlibExt.card_composition_huang_franklin` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#card-composition-huang-franklin).

## Signed count of Huang's compositions, binomial form

Let $k, n \ge 1$ and $m \ge 0$.
Among the compositions of $n + k - 1$ with exactly $m$ parts less than $k$ in which every part
less than $k$ is preceded by a part at least $k$ and followed by a part that is either the last
part or greater than $k$, let $b^{(m)}_{k,n}$ be the number with an odd number of parts minus the
number with an even number of parts. Then $b^{(m)}_{k,n}$ is the sum of
$(-1)^{\ell+j} \binom{i}{m} \binom{i+j-1}{j} \binom{m}{\ell} \binom{m+h-1}{h}$ over all
$i, j, \ell, h \ge 0$ with $i + (k+1)m + jk + \ell(k-1) + h = n$, where $\binom{-1}{0} = 1$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 16 (`jis-2024-24.6.5-thm-16`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_huang_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-huang-eq-sum).

## Signed count of Huang's compositions, monomial form

Let $k \ge 2$, $m \ge 0$ and
$n \ge 1$. Among the compositions of $n + k - 1$ with exactly $m$ parts less than $k$ in which
every part less than $k$ is preceded by a part at least $k$ and followed by a part that is either
the last part or greater than $k$, let $b^{(m)}_{k,n}$ be the number with an odd number of parts
minus the number with an even number of parts. Then $b^{(m)}_{k,n}$ is the sum of
$(-1)^j \binom{i}{m} \binom{i+j-1}{j}$ over all $i, j \ge 0$ and all functions
$g \colon \{1, \dots, m\} \to \{0, 1, \dots, k-2\}$ with
$i + (k+1)m + jk + g(1) + \dots + g(m) = n$, where $\binom{-1}{0} = 1$.

Grouping the functions $g$ by the partition $\lambda$ formed by their nonzero values gives the
paper's form of the sum: over partitions $\lambda$ with at most $m$ parts, each at most $k-2$
(written $\lambda \subseteq (k-2)^m$), of size $|\lambda| = n - i - (k+1)m - jk$, each weighted
by $m_\lambda(1^m)$, the monomial symmetric function $m_\lambda$ in $m$ variables evaluated at
$x_1 = \dots = x_m = 1$, which is the number of functions $g$ in the group.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 16 (`jis-2024-24.6.5-thm-16`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_huang_eq_sum_monomial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-huang-eq-sum-2).

## Signed count of compositions with exactly $m$ parts less than $k$

Let $k, n \ge 1$ and
$m \ge 0$. Among the compositions of $n + k - 1$ with exactly $m$ parts less than $k$, the number
with an odd number of parts minus the number with an even number of parts is the sum of
$(-1)^{i+\ell+1} \binom{i+j-1}{j} \binom{i}{m} \binom{m}{\ell}$ over all $i, j, \ell \ge 0$ with
$i + j + (k-1)(\ell + i - m - 1) = n$, where $\binom{-1}{0} = 1$.

Only finitely many terms are nonzero: a nonzero term has $\ell \le m$ and
$i, j \le n + (k-1)(m+1)$.

## Sources

- Jia Huang, *Even and Odd Compositions with Restricted Parts*, Journal of Integer Sequences 27 (2024), Article 24.6.5, Theorem 17 (`jis-2024-24.6.5-thm-17`).

Stated but not proved: `MetaMathlibExt.compositionOddMinusEven_parts_lt_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/EvenOddCompositionsWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html#composition-odd-minus-even-parts-lt-eq-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Even and odd compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/even-and-odd-compositions)
