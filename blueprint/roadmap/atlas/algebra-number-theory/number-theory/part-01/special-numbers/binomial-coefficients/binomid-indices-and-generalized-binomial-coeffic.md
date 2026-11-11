---
declaration: section
origin: cited
lean: MetaMathlibExt.IsBinomidIndex, MetaMathlibExt.isBinomidIndex_const, MetaMathlibExt.IsLexMinimalExtensionOf, MetaMathlibExt.IsLexMinimalExtension, MetaMathlibExt.isLexMinimalExtensionOf_zero, MetaMathlibExt.binomidShift, MetaMathlibExt.binomidShift_zero, MetaMathlibExt.isBinomidIndex_of_monotone
statement: formalized
---

# Binomid indices and generalized binomial coefficients

52 results, 21 proved and 31 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html).

## Binomid index

An infinite binomid index is a sequence $(e_1, e_2, \dots)$ of
nonnegative integers such that $\sum_{i=n-k+1}^{n} e_i \ge \sum_{i=1}^{k} e_i$ for all
$1 \le k \le n$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53; definition as restated in arXiv:2505.20018, Section 1.

Formalized by `MetaMathlibExt.IsBinomidIndex`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-binomid-index).

## Constant sequences are binomid indices

For every natural number $c$, the constant
sequence $(c, c, c, \dots)$ is a binomid index.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53.

Formalized by `MetaMathlibExt.isBinomidIndex_const`, a theorem declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-binomid-index-const).

## Lex-minimal extension

Let $e = (e_1, e_2, \dots)$ be a sequence of nonnegative integers
and $m \ge 0$. Then $e$ is the lex-minimal extension of $(e_1, \dots, e_m)$ when $e$ is an
infinite binomid index and, for every infinite binomid index $g$ with $g_i = e_i$ for all
$i \le m$, either $g = e$ or $e$ is lexicographically smaller than $g$: there is a $j$ with
$e_i = g_i$ for all $i < j$ and $e_j < g_j$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53; definition as restated in arXiv:2505.20018, Section 1.

Formalized by `MetaMathlibExt.IsLexMinimalExtensionOf`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-of).

## Lex-minimal extensions

A sequence $e = (e_1, e_2, \dots)$ of nonnegative integers is a
lex-minimal extension when, for some $m \ge 0$, it is the lex-minimal extension of
$(e_1, \dots, e_m)$. The set of all lex-minimal extensions is denoted $L$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53.

Formalized by `MetaMathlibExt.IsLexMinimalExtension`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension).

## The zero sequence is lex-minimal

For every $m \ge 0$, the zero sequence
$(0, 0, \dots)$ is the lex-minimal extension of its first $m$ entries.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53.

Formalized by `MetaMathlibExt.isLexMinimalExtensionOf_zero`, a theorem declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-of-zero).

## Right shift of a sequence

For a natural number $l$, the right shift $\sigma^l$ sends a
sequence $\eta = (e_1, e_2, \dots)$ of nonnegative integers to the sequence
$(0, \dots, 0, e_1, e_2, \dots)$ obtained by prepending $l$ zeros: its first $l$ entries are $0$
and its $(l + i)$-th entry is $e_i$ for every $i \ge 1$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53; definition as restated in arXiv:2505.20018, Section 1.

Formalized by `MetaMathlibExt.binomidShift`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-shift).

## Shifting by zero places is the identity

For every sequence $\eta$ of nonnegative
integers, $\sigma^0(\eta) = \eta$, where $\sigma^l$ is the right shift that prepends $l$ zeros.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53.

Formalized by `MetaMathlibExt.binomidShift_zero`, a theorem declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-shift-zero).

## Monotone sequences are binomid indices

Every non-decreasing sequence
$e_1 \le e_2 \le \cdots$ of nonnegative integers is an infinite binomid index.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Proposition 1.

Stated but not proved: `MetaMathlibExt.isBinomidIndex_of_monotone` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-binomid-index-of-monotone).

## Partial-sum characterization of binomid indices

Let $\eta = (e_1, e_2, \dots)$ be a
sequence of nonnegative integers with partial sums $s_n = e_1 + \dots + e_n$ (so $s_0 = 0$).
Then $\eta$ is a binomid index if and only if $s_{n-k} + s_k \le s_n$ for all $k$ and $n$ with
$1 \le k < n$. Moreover, for every $m$, if $\eta$ is the lex-minimal extension of its first $m$
entries, then for every $n > m$

$$s_n = \max_{1 \le k < n} (s_{n-k} + s_k),$$

where the maximum over the empty range (for $n = 1$) is taken to be $0$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Lemma 1.

Stated but not proved: `MetaMathlibExt.isBinomidIndex_iff_partialSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-binomid-index-iff-partial-sum).

## Monotone finite binomid indices extend periodically

Let $m \ge 1$ and let
$e_1 \le e_2 \le \cdots \le e_m$ be nonnegative integers. Then the periodic sequence
$(e_1, \dots, e_m, e_1, \dots, e_m, \dots)$ is the lex-minimal extension of $(e_1, \dots, e_m)$.

A non-decreasing finite sequence is automatically a finite binomid index.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Proposition 3.

Stated but not proved: `MetaMathlibExt.isLexMinimalExtensionOf_periodic_of_monotoneOn` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-of-periodic-of).

## A lex-minimal extension periodic from its second entry is periodic

Let
$\eta = (e_1, e_2, \dots)$ be a lex-minimal extension and let $p \ge 1$. If $e_{i+p} = e_i$
for every $i \ge 2$, then $e_{1+p} = e_1$, so the whole sequence $\eta$ is periodic with
period $p$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Proposition 4.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtension.apply_period_eq_apply_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#apply-period-eq-apply-zero).

## Periodic binomid indices are lex-minimal extensions

If an infinite binomid index
$e = (e_1, e_2, \dots)$ is periodic, that is, there is $p \ge 1$ with $e_{i+p} = e_i$ for all
$i$, then $e$ is a lex-minimal extension: it is the lex-minimal extension of
$(e_1, \dots, e_m)$ for some $m \ge 0$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Proposition 5.

Stated but not proved: `MetaMathlibExt.isLexMinimalExtension_of_periodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-of-periodic).

## Lex-minimal extensions are closed under addition

If $\eta_1$ and $\eta_2$ are
lex-minimal extensions, then their componentwise sum $\eta_1 + \eta_2$ is a lex-minimal
extension.

Since the zero sequence is also a lex-minimal extension, the set $L$ of lex-minimal extensions
is a monoid under componentwise addition.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Corollary 1.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtension.add` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#add).

## Distinct shifts of lex-minimal extensions meet only in zero

Let $L$ be the set of
lex-minimal extensions, and for a natural number $l$ let $\sigma^l$ be the right shift that
prepends $l$ zeros to a sequence. For natural numbers $l \neq m$,
$\sigma^l(L) \cap \sigma^m(L) = \{(0, 0, 0, \dots)\}$: the only sequence in both images is
the zero sequence.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Proposition 6.

Stated but not proved: `MetaMathlibExt.binomidShift_image_inter_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-shift-image-inter-eq-zero).

## Primes divide all inner binomial coefficients of infinitely many rows

For every prime
$p$ there are infinitely many natural numbers $n$ such that $p$ divides the binomial coefficient
$\binom{n}{k}$ for every $k$ with $1 \le k < n$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Corollary 3.

Stated but not proved: `MetaMathlibExt.infinite_setOf_prime_dvd_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#infinite-set-of-prime-dvd-choose).

## Primes divide all inner Fibonomial coefficients of infinitely many rows

Let $F_n$ be
the Fibonacci numbers and $F_n! = F_1 F_2 \cdots F_n$ the Fibonacci factorial. For every prime
$p$ there are infinitely many natural numbers $n$ such that for every $k$ with $1 \le k < n$ the
Fibonomial coefficient $F_n! / (F_k! \, F_{n-k}!)$ is an integer multiple of $p$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Corollary 4.

Stated but not proved: `MetaMathlibExt.infinite_setOf_prime_dvd_fibonomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#infinite-set-of-prime-dvd-fibonomial).

## The lex-minimal extension is computed greedily

Let $m \ge 1$ and let
$f = (f_1, f_2, \dots)$ be a sequence of nonnegative integers whose first $m$ entries form a
finite binomid index, that is, $\sum_{i=n-k+1}^{n} f_i \ge \sum_{i=1}^{k} f_i$ for all
$1 \le k \le n \le m$. Suppose that for every $n > m$ the entry $f_n$ equals the maximum,
over $1 \le k < n$, of the integers $\sum_{i=1}^{k} f_i - \sum_{i=n-k+1}^{n-1} f_i$. Then $f$
is the lex-minimal extension of $(f_1, \dots, f_m)$.

The differences are taken in the integers and may be negative; the condition says that
$f_n + \sum_{i=n-k+1}^{n-1} f_i \ge \sum_{i=1}^{k} f_i$ for every $1 \le k < n$, with equality
for some such $k$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Proposition 2.

Stated but not proved: `MetaMathlibExt.isLexMinimalExtensionOf_of_greedy` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-of-of-greedy).

## Lex-minimal extensions have a nomid coefficient equal to one

Let $m \ge 1$, let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $m$ entries, and let $p$ be a
prime. Write $f_i = p^{e_i}$ for $i \ge 1$ and, for $1 \le k \le n$, let
$[n, k]_f = \frac{f_n f_{n-1} \cdots f_{n-k+1}}{f_k f_{k-1} \cdots f_1}$ be the $f$-nomid
coefficient, the generalized binomial coefficient of $f$. Then for every $n > m$ there is some $k$
with $1 \le k < n$ and $[n, k]_f = 1$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Corollary 2.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.exists_nomid_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#exists-nomid-eq-one).

## Nomid coefficients of binomid indices that are not lex-minimal extensions

Let
$\mu = (e_1, e_2, \dots)$ be a binomid index such that for no $m$ is $\mu$ the lex-minimal
extension of its first $m$ entries, and let $p$ be a prime. Write $f_i = p^{e_i}$ for $i \ge 1$
and let $[n, k]_f = \frac{f_n f_{n-1} \cdots f_{n-k+1}}{f_k f_{k-1} \cdots f_1}$ be the
$f$-nomid coefficient. Then there are infinitely many natural numbers $n$ such that for every $k$
with $1 \le k < n$ the coefficient $[n, k]_f$ is an integer multiple of $p$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Corollary 2.

Stated but not proved: `MetaMathlibExt.infinite_setOf_prime_dvd_nomid_of_not_isLexMinimalExtension` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#infinite-set-of-prime-dvd-nomid-of-not-i).

## Initial averages of a sequence

For a sequence $\eta = (e_1, e_2, \dots)$ of
nonnegative integers and $i \ge 1$, the average $A_{i,0}(\eta)$ is the rational number
$s_i / i$, where $s_i = e_1 + \dots + e_i$ is the sum of the first $i$ entries; for $i = 0$
the value is $A_{0,0}(\eta) = 0$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Section 3; the same average is the sequence `Ave(η)` of Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 2.

Formalized by `MetaMathlibExt.binomidAverage`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average).

## Averages of a constant sequence

For every natural number $c$ and every $i \ge 1$,
the average $A_{i,0}$ of the first $i$ entries of the constant sequence $(c, c, c, \dots)$
equals $c$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Section 3.

Formalized by `MetaMathlibExt.binomidAverage_const`, a theorem declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-const).

## Upper average of a sequence

For a sequence $\eta = (e_1, e_2, \dots)$ of nonnegative
integers with partial sums $s_i = e_1 + \dots + e_i$ and averages $A_{i,0}(\eta) = s_i / i$,
the upper average of $\eta$ is $A_0(\eta) = \limsup_{i \to \infty} A_{i,0}(\eta)$, taken in
the extended real numbers; it is $+\infty$ when $s_i / i$ is unbounded.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Section 3.

Formalized by `MetaMathlibExt.binomidUpperAverage`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-upper-average).

## Upper average of a constant sequence

For every natural number $c$, the upper average
$A_0$ of the constant sequence $(c, c, c, \dots)$ equals $c$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Section 3.

Formalized by `MetaMathlibExt.binomidUpperAverage_const`, a theorem declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-upper-average-const).

## The Average Condition

A sequence $\eta = (e_1, e_2, \dots)$ of nonnegative integers
satisfies the Average Condition when its upper average $A_0(\eta)$, the limit superior as
$n \to \infty$ of the averages $A_{n,0}(\eta) = (e_1 + \dots + e_n)/n$ taken in the extended
real line, equals $A_{i,0}(\eta)$ for some $i \ge 1$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Lemma 3.

Formalized by `MetaMathlibExt.BinomidAverageCondition`, a definition declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-condition).

## Constant sequences satisfy the Average Condition

For every natural number $c$, the
constant sequence $(c, c, c, \dots)$ satisfies the Average Condition.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Lemma 3.

Formalized by `MetaMathlibExt.binomidAverageCondition_const`, a theorem declared in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-condition-const).

## Averages of a binomid index

Let $\eta = (e_1, e_2, \dots)$ be a binomid index, write
$s_n = e_1 + \dots + e_n$, and for $i \ge 1$ and $l \ge 0$ let $A_{i,l} = (s_{i+l} - s_l)/i$
be the average of $e_{l+1}, \dots, e_{l+i}$. Then for all $i, l \ge 1$: $A_{i,l} \ge A_{i,0}$;
$A_{ki,0} \ge A_{i,0}$ for every $k \ge 1$; and
$A_{i+l,0} = \frac{i}{i+l} A_{i,l} + \frac{l}{l+i} A_{l,0}$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Lemma 2.

Stated but not proved: `MetaMathlibExt.IsBinomidIndex.binomidAverage_props` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-props).

## The upper average of a binomid index is the supremum of its averages

Let $\eta$ be a
binomid index, let $s_i$ be the sum of its first $i$ entries, let $A_{i,0}(\eta) = s_i / i$ for
$i \ge 1$, and let $A_0(\eta) = \limsup_{i \to \infty} A_{i,0}(\eta)$ be its upper average.
Then, in the extended real numbers, $A_0(\eta) = \sup_{i \ge 1} A_{i,0}(\eta)$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Lemma 2.

Stated but not proved: `MetaMathlibExt.IsBinomidIndex.binomidUpperAverage_eq_iSup` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-upper-average-eq-i-sup).

## Lex-minimal extensions satisfy the Average Condition

Every lex-minimal extension
satisfies the Average Condition.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Lemma 3.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtension.binomidAverageCondition` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-condition-2).

## The Average Condition gives eventually periodic lex-minimal extensions

If an
infinite binomid index $e = (e_1, e_2, \dots)$ satisfies the Average Condition, then $e$ is
a lex-minimal extension, that is, the lex-minimal extension of $(e_1, \dots, e_m)$ for some
$m \ge 0$, and $e$ is eventually periodic: there are $N$ and $p \ge 1$ such that
$e_{n+p} = e_n$ for all $n \ge N$.

## Sources

- Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), Article A53, Theorem 1.

Stated but not proved: `MetaMathlibExt.IsBinomidIndex.isLexMinimalExtension_and_eventually_periodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/BinomidIndexWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BinomidIndexWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-and-eventually).

## The first average is the first entry

For every sequence $\eta = (e_1, e_2, \dots)$ of
nonnegative integers, the initial average $A_{1,0}(\eta)$ of its first entry equals $e_1$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 2.

Formalized by `MetaMathlibExt.binomidAverage_one`, a theorem declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-one).

## Indices of maximal average

For a sequence $\eta = (e_1, e_2, \dots)$ of nonnegative
integers and $m \ge 0$, let $A_i = (e_1 + \dots + e_i)/i$ be the average of the first $i$
entries of $\eta$. The set of maximal-average indices of $\eta$ up to $m$ is the set of all $i$
with $1 \le i \le m$ such that $A_j \le A_i$ for every $j$ with $1 \le j \le m$; for
$m \ge 1$ these are the $i$ with $1 \le i \le m$ and $A_i = A_{\max}$, where
$A_{\max} = \max \{A_i \mid 1 \le i \le m\}$, and for $m = 0$ the set is empty.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 3 (the set `{i ≤ m | A_max = A_i}`).

Formalized by `MetaMathlibExt.maxAverageIndices`, a definition declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#max-average-indices).

## Maximal-average indices for $m = 1$

Let $\eta = (e_1, e_2, \dots)$ be a sequence of
nonnegative integers and $A_i = (e_1 + \dots + e_i)/i$. For $m = 1$, the set of indices
$1 \le i \le m$ at which $A_i$ is maximal among $A_1, \dots, A_m$ is $\{1\}$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 3.

Formalized by `MetaMathlibExt.maxAverageIndices_one`, a theorem declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#max-average-indices-one).

## Basis of a submonoid

Let $M$ and $B$ be subsets of an additive commutative monoid.
Then $B$ is a basis of $M$ when $M$ is the submonoid $\langle B \rangle$ generated by $B$ and
no element of $B$ is a nonnegative integer combination of elements of $B$ in which its own
coefficient is $0$: for all pairwise distinct $\beta_1, \dots, \beta_n \in B$, all nonnegative
integers $c_1, \dots, c_n$ and every $j$, if $\beta_j = \sum_{i=1}^n c_i \beta_i$ then
$c_j \ge 1$.

The elements $\beta_i$ are required to be distinct: the paper's wording allows repeated
entries, under which $\beta = (b, b)$ and $b = 0 \cdot b + 1 \cdot b$ would rule out every
nonempty $B$; its uniqueness proof uses distinct entries.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 4 (definition of a basis).

Formalized by `MetaMathlibExt.IsAddMonoidBasis`, a definition declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-add-monoid-basis).

## A monoid basis does not contain zero

Let $\alpha$ be an additive commutative monoid and
let $M$ and $B$ be subsets of $\alpha$. If $B$ is a basis of $M$, then $0 \notin B$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 4.

Formalized by `MetaMathlibExt.IsAddMonoidBasis.zero_notMem`, a theorem declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#zero-not-mem).

## The empty set is a basis of the zero submonoid

In every additive commutative monoid,
the empty set is a basis of the subset $\{0\}$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 4.

Formalized by `MetaMathlibExt.isAddMonoidBasis_empty`, a theorem declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-add-monoid-basis-empty).

## Atomic binomid index

A sequence $\eta$ of nonnegative integers is a nonzero atomic
binomid index (an element of the paper's set $\mathrm{Atom}$) when $\eta$ is a nonzero binomid
index that is not the sum of two nonzero binomid indices: whenever $\eta = \eta_1 + \eta_2$
termwise with $\eta_1$ and $\eta_2$ binomid indices, $\eta_1 = 0$ or $\eta_2 = 0$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 4 (definition of atomic).

Formalized by `MetaMathlibExt.IsAtomicBinomidIndex`, a definition declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-atomic-binomid-index).

## The constant sequence $1$ is atomic

The constant sequence $(1, 1, 1, \dots)$ is a
nonzero atomic binomid index: it is a nonzero binomid index that is not the sum of two nonzero
binomid indices.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Section 4 (example of `(E_m)^∞` with `m = 1`).

Formalized by `MetaMathlibExt.isAtomicBinomidIndex_one`, a theorem declared in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-atomic-binomid-index-one).

## Partial-sum criterion for lex-minimal extensions

Let $k \ge 1$, let
$\eta = (e_1, e_2, \dots)$ be a sequence of nonnegative integers and write
$S_i = e_1 + \dots + e_i$. Suppose $S_i + S_j \le S_{i+j}$ for all $i, j \ge 1$ with
$i + j \le k$. Then $\eta$ is the lex-minimal extension of $(e_1, \dots, e_k)$ if and only if,
for every $r > k$, $S_i + S_j \le S_r$ for all $i, j \ge 1$ with $i + j = r$, with equality for
at least one such pair $(i, j)$.

In the paper's notation, the condition says that $\Delta_\eta(r) = 0$ for every $r > k$, where
$\Delta_\eta(r) = \min \{S_r - S_i - S_j : i + j = r,\ i, j \ge 1\}$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Proposition 1.

Stated but not proved: `MetaMathlibExt.isLexMinimalExtensionOf_iff_forall_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-lex-minimal-extension-of-iff-forall-l).

## Partial sums of a lex-minimal extension solve a knapsack problem

Let $m \ge 1$, let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $m$ entries, and write
$S_i = e_1 + \dots + e_i$. Then for every $c \ge 1$ there are nonnegative integers
$n_1, \dots, n_m$ with $\sum_{i=1}^m n_i i = c$ and $S_c = \sum_{i=1}^m n_i S_i$ that solve the
unbounded knapsack problem with values $S_i$, weights $i$ and capacity $c$: all nonnegative
integers $n'_1, \dots, n'_m$ with $\sum_{i=1}^m n'_i i \le c$ satisfy
$\sum_{i=1}^m n'_i S_i \le \sum_{i=1}^m n_i S_i$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Proposition 2.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.exists_knapsack` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#exists-knapsack).

## The largest of the first $m$ averages is the largest average

Let $m \ge 0$ and let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $m$ entries, with averages
$A_i = (e_1 + \dots + e_i)/i$ for $i \ge 1$. If $1 \le j \le m$ and
$A_j = \max \{A_i \mid 1 \le i \le m\}$, then $A_i \le A_j$ for every $i \ge 1$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Lemma 1.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.binomidAverage_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#binomid-average-le).

## Every index with maximal average is a multiple of the gcd of those up to $m$

Let
$m \ge 0$, let $\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $m$ entries,
with averages $A_i = (e_1 + \dots + e_i)/i$, let $J$ be the set of indices $1 \le j \le m$ with
$A_j = \max \{A_{j'} \mid 1 \le j' \le m\}$, and let $g = \gcd J$. Then $g$ divides every
$i \ge 1$ such that $A_i = A_j$ for some $j \in J$.

Since every element of $J$ is such an index, $g$ is also the greatest common divisor of all
$i \ge 1$ with $A_i = A_j$ for some $j \in J$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Lemma 2.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.gcd_maxAverageIndices_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#gcd-max-average-indices-dvd).

## The gcd of the maximizing indices divides the minimal period

Let $m \ge 1$, let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $m$ entries, with averages
$A_i = (e_1 + \dots + e_i)/i$, and let $g$ be the greatest common divisor of the indices
$1 \le i \le m$ with $A_i = \max \{A_j \mid 1 \le j \le m\}$. If $p$ is the least $q \ge 1$
such that $e_{i+q} = e_i$ for all sufficiently large $i$, then $g$ divides $p$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Lemma 3.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.gcd_maxAverageIndices_dvd_minimalPeriod` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#gcd-max-average-indices-dvd-minimal-peri).

## Minimal period of a lex-minimal extension

Let $m \ge 1$ and let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of $(e_1, \dots, e_m)$. For
$1 \le i \le m$ let $A_i = (e_1 + \dots + e_i)/i$, and let $A_{\max}$ be the largest of
$A_1, \dots, A_m$. Let $g$ be the greatest common divisor of the indices $1 \le i \le m$ with
$A_i = A_{\max}$. Then $g$ is the minimal eventual period of $\eta$: $g \ge 1$,
$e_{i+g} = e_i$ for all sufficiently large $i$, and every $q \ge 1$ with $e_{i+q} = e_i$ for
all sufficiently large $i$ satisfies $g \le q$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Theorem 1.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.isLeast_period_gcd_maxAverageIndices` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-least-period-gcd-max-average-indices).

## A preperiod bound for lex-minimal extensions

Let $m \ge 0$, let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $m$ entries, with averages
$A_i = (e_1 + \dots + e_i)/i$, and let $1 \le k \le m$ with
$A_k = \max \{A_i \mid 1 \le i \le m\}$. Then $\eta$ is periodic after position
$N = k m (m + 1)/2$: there is $p \ge 1$ with $e_{i+p} = e_i$ for all $i > N$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Theorem 2.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.exists_period_from_preperiod_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#exists-period-from-preperiod-bound).

## Summands of a lex-minimal extension are lex-minimal

Let $\eta_1$ and $\eta_2$ be
infinite binomid indices and let $k \ge 0$. If the termwise sum $\eta_1 + \eta_2$ is the
lex-minimal extension of its first $k$ entries, then $\eta_1$ is the lex-minimal extension of
its first $k$ entries and $\eta_2$ is the lex-minimal extension of its first $k$ entries.

Since every lex-minimal extension is the lex-minimal extension of its first $k$ entries for some
$k$, this contains the first claim of the source: if $\eta_1 + \eta_2$ is a lex-minimal
extension, then so are $\eta_1$ and $\eta_2$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Proposition 3.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.of_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#of-add).

## Atoms are the unique basis of an atom-generated submonoid

Let $\iota$ be a type and
let $M$ be a submonoid of $\mathbb{N}^\iota$ under componentwise addition. Let $A$ be the set
of atoms of $M$: the elements $a \in M$ with $a \ne 0$ such that $y = 0$ or $z = 0$ whenever
$a = y + z$ with $y, z \in M$. If every element of $M$ is a finite sum of elements of $A$, then
a set $B \subseteq \mathbb{N}^\iota$ is a basis of $M$ if and only if $B = A$; that is, $A$ is
the unique basis of $M$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Proposition 4.

Stated but not proved: `MetaMathlibExt.isAddMonoidBasis_iff_eq_atoms` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-add-monoid-basis-iff-eq-atoms).

## Basis of the monoid of lex-minimal extensions

Let $L$ be the set of lex-minimal
extensions, viewed inside the sequences of nonnegative integers under componentwise addition.
A set $B$ of sequences of nonnegative integers is a basis of $L$ if and only if $B$ is the set
of nonzero atomic binomid indices that belong to $L$. Hence that set is the unique basis of $L$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Proposition 5.

Stated but not proved: `MetaMathlibExt.isAddMonoidBasis_lexMinimalExtensions_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-add-monoid-basis-lex-minimal-extensio).

## Basis of the span of the lex-minimal extensions of length $k$

Let $k \ge 0$ and let
$L_k$ be the set of sequences $\eta = (e_1, e_2, \dots)$ of nonnegative integers that are the
lex-minimal extension of $(e_1, \dots, e_k)$. A set $B$ of sequences of nonnegative integers is
a basis of the submonoid generated by $L_k$ under componentwise addition if and only if $B$ is
the set of nonzero atomic binomid indices that belong to $L_k$. Hence that set is the unique
basis of this submonoid.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Proposition 5.

Stated but not proved: `MetaMathlibExt.isAddMonoidBasis_closure_lexMinimalExtensionsOf_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#is-add-monoid-basis-closure-lex-minimal).

## Late partial sums of a lex-minimal extension split

Let $k \ge 1$, let
$\eta = (e_1, e_2, \dots)$ be the lex-minimal extension of its first $k$ entries, and write
$S_i = e_1 + \dots + e_i$. Then for every $l$ there is a map $\pi \colon \mathbb{N} \to \mathbb{N}$
such that $1 \le \pi(i) < i$ and $S_i = S_{\pi(i)} + S_{i - \pi(i)}$ for every $i$ with
$k < i \le l$.

The paper takes the specific bound $l = l(k)$ from its proof of the preceding lemma; the
statement here holds for every $l$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Lemma 4.

Stated but not proved: `MetaMathlibExt.IsLexMinimalExtensionOf.exists_path` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#exists-path).

## Spans of lex-minimal extensions of a fixed length are finitely generated

For $k \ge 0$
let $L_k$ be the set of sequences of nonnegative integers that are the lex-minimal extension of
their first $k$ entries. Then the submonoid of $\mathbb{N}^{\mathbb{N}}$ (under componentwise
addition) generated by $L_k$ is finitely generated, and only finitely many elements of $L_k$
are atomic binomid indices, that is, nonzero binomid indices that are not the sum of two
nonzero binomid indices.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Lemma 5.

Stated but not proved: `MetaMathlibExt.fg_closure_lexMinimalExtensionsOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#fg-closure-lex-minimal-extensions-of).

## Spans of lex-minimal extensions of a fixed length are finitely presented

For $k \ge 0$
let $L_k$ be the set of sequences of nonnegative integers that are the lex-minimal extension of
their first $k$ entries, and let $\langle L_k \rangle$ be the submonoid of $\mathbb{N}^{\mathbb{N}}$
(under componentwise addition) generated by $L_k$. Then there are $n \ge 0$, a surjective
monoid homomorphism $f \colon \mathbb{N}^n \to \langle L_k \rangle$ and a finite set $R$ of
pairs of elements of $\mathbb{N}^n$ such that the congruence on $\mathbb{N}^n$ generated by $R$
is the kernel congruence of $f$, which relates $x$ and $y$ exactly when $f(x) = f(y)$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Lemma 6.

Stated but not proved: `MetaMathlibExt.exists_finitePresentation_closure_lexMinimalExtensionsOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#exists-finite-presentation-closure-lex-m).

## The monoid of lex-minimal extensions is a directed union

For $k \ge 0$ let $L_k$ be the
set of sequences of nonnegative integers that are the lex-minimal extension of their first $k$
entries, let $\langle L_k \rangle$ be the submonoid of $\mathbb{N}^{\mathbb{N}}$ (under
componentwise addition) generated by $L_k$, and let $\mathcal{A}_k$ be the set of elements of
$L_k$ that are atomic binomid indices, that is, nonzero binomid indices that are not the sum of
two nonzero binomid indices. Then $\langle L_k \rangle \subseteq \langle L_{k'} \rangle$ and
$\mathcal{A}_k \subseteq \mathcal{A}_{k'}$ whenever $k \le k'$; the union of the sets
$\langle L_k \rangle$ over all $k$ is the set $L$ of all lex-minimal extensions; and for every
$k$ the submonoid generated by $\mathcal{A}_k$ is $\langle L_k \rangle$.

## Sources

- Caalim and Tanaka, *Generalized Binomial Coefficients and the Monoid of Lexicographically Minimal Extensions*, INTEGERS 26 (2026), Article A113, Theorem 3.

Stated but not proved: `MetaMathlibExt.iUnion_closure_lexMinimalExtensionsOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LexMinimalExtensionMonoidWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html#i-union-closure-lex-minimal-extensions-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomid indices and generalized binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/binomid-indices-and-generalized-binomial-coeffic)
