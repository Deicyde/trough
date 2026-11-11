---
declaration: section
origin: cited
lean: MetaMathlibExt.nonIntersectingWordPairs_card_eq_coeff, MetaMathlibExt.nonIntersectingWordPairs_sameLength_generatingFunction, MetaMathlibExt.nonIntersectingWordPairs_sameLength_card, MetaMathlibExt.wordPairs_overlap_sum_eq_coeff, MetaMathlibExt.wordPairs_sameLength_overlap_sum, MetaMathlibExt.weaklyDecreasingNonIntersectingPairs_card_eq_coeff, MetaMathlibExt.weaklyDecreasingNonIntersectingPairs_generatingFunction, MetaMathlibExt.weaklyDecreasingNonIntersectingPairs_sameLength_card
statement: formalized
---

# Intersections in pairs of words

9 results, 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html).

## Non-intersecting pairs of words

Fix natural numbers $k$, $n \ge 1$ and $r \ge 1$, and call
a pair of words over an alphabet of $k$ letters non-intersecting when no letter occurs in both.
Write $[x^m] F$ for the coefficient of $x^m$ in a formal power series $F$ over $\mathbb{Q}$ and
$S(m, j)$ for the Stirling numbers of the second kind. Let $N$ be the number of non-intersecting
pairs $(u, v)$ with $u$ of length $n$ and $v$ of length $r$. Then
$N = \sum_{j=1}^{k-1} \binom{k}{j} \,
[x^n]\Bigl(j! \, x^j \bigl(\prod_{i=1}^{j} (1 - i x)\bigr)^{-1}\Bigr) \,
[x^r]\bigl((k-j) x \, (1 - (k-j) x)^{-1}\bigr)$
and
$N = \sum_{j=1}^{k-1} \binom{k}{j} \, j! \, S(n, j) \,
[x^r]\bigl((k-j) x \, (1 - (k-j) x)^{-1}\bigr)$.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Theorem 1.

Stated but not proved: `MetaMathlibExt.nonIntersectingWordPairs_card_eq_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#non-intersecting-word-pairs-card-eq-coef).

## Generating function of non-intersecting pairs of words of equal length

Let $k$ be a
natural number, let $S(n, j)$ denote the Stirling numbers of the second kind, and for $n \ge 1$ let
$h(n)$ be the number of pairs $(u, v)$ of words of length $n$ over an alphabet of $k$ letters such
that no letter occurs in both. Then, as formal power series over $\mathbb{Q}$,
$\sum_{n \ge 1} h(n) x^n = \sum_{n \ge 0} \sum_{j=1}^{k-1} \binom{k}{j} \, j! \, S(n, j) \,
(k-j)^n x^n$.

The constant term on the right is $0$ because $S(0, j) = 0$ for $j \ge 1$: the empty pair is not
counted.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Corollary 1.

Stated but not proved: `MetaMathlibExt.nonIntersectingWordPairs_sameLength_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#non-intersecting-word-pairs-same-length).

## Non-intersecting pairs of words of equal length

Let $S(n, j)$ denote the Stirling numbers
of the second kind. For natural numbers $k$ and $n \ge 1$, the number of pairs $(u, v)$ of words
of length $n$ over an alphabet of $k$ letters such that no letter occurs in both $u$ and $v$ is
$\sum_{j=1}^{k-1} \binom{k}{j} \, j! \, S(n, j) \, (k-j)^n$.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Corollary 2.

Stated but not proved: `MetaMathlibExt.nonIntersectingWordPairs_sameLength_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#non-intersecting-word-pairs-same-length-2).

## Overlap statistic on pairs of words

Fix natural numbers $k$, $n \ge 1$, $r \ge 1$ and a
rational number $q$. For words $u$ and $v$ over an alphabet of $k$ letters, the overlap of
$(u, v)$ is the number of positions of $v$ whose letter occurs in $u$. Write $[x^m] F$ for the
coefficient of $x^m$ in a formal power series $F$ over $\mathbb{Q}$, $S(m, j)$ for the Stirling
numbers of the second kind, and $c_j = qj + k - j$. Then the sum of $q^{\text{overlap}}$ over all
pairs $(u, v)$ with $u$ of length $n$ and $v$ of length $r$ equals
$\sum_{j=1}^{k} \binom{k}{j} \, [x^r]\bigl(c_j x \, (1 - c_j x)^{-1}\bigr) \, j! \, S(n, j)$.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Theorem 2.

Stated but not proved: `MetaMathlibExt.wordPairs_overlap_sum_eq_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#word-pairs-overlap-sum-eq-coeff).

## Overlap statistic on pairs of words of equal length

Fix natural numbers $k$ and $n \ge 1$
and a rational number $q$. For words $u$ and $v$ over an alphabet of $k$ letters, the overlap of
$(u, v)$ is the number of positions of $v$ whose letter occurs in $u$. Let $S(n, j)$ denote the
Stirling numbers of the second kind. Then the sum of $q^{\text{overlap}}$ over all pairs $(u, v)$
of words of length $n$ equals $\sum_{j=1}^{k} \binom{k}{j} \, j! \, S(n, j) \, (qj + k - j)^n$.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Corollary 3.

Stated but not proved: `MetaMathlibExt.wordPairs_sameLength_overlap_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#word-pairs-same-length-overlap-sum).

## Non-intersecting pairs of weakly decreasing words

Fix natural numbers $k$, $n \ge 1$ and
$r \ge 1$, and order an alphabet of $k$ letters. Write $[x^m] F$ for the coefficient of $x^m$ in a
formal power series $F$ over $\mathbb{Q}$. The number of pairs $(u, v)$ of weakly decreasing words
over this alphabet, $u$ of length $n$ and $v$ of length $r$, such that no letter occurs in both is
$\sum_{j=1}^{k-1} \binom{k}{j} \, [x^n]\bigl(x^j (1-x)^{-j}\bigr) \,
[x^r]\bigl((1-x)^{-(k-j)} - 1\bigr)$.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Theorem 3.

Stated but not proved: `MetaMathlibExt.weaklyDecreasingNonIntersectingPairs_card_eq_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#weakly-decreasing-non-intersecting-pairs).

## Generating function of non-intersecting pairs of weakly decreasing words

Let $k$ be a
natural number and order an alphabet of $k$ letters. In the ring of formal power series in $x$
and $y$ over $\mathbb{Q}$ let
$f(x, y) = \bigl(x (1-x)^{-1} + (1-y)^{-1}\bigr)^k - (1-x)^{-k} - (1-y)^{-k} + 1$.
Then for all natural numbers $n$ and $r$, the coefficient of $x^n y^r$ in $f$ is $0$ if $n = 0$
or $r = 0$, and otherwise equals the number of pairs $(u, v)$ of weakly decreasing words over this
alphabet, $u$ of length $n$ and $v$ of length $r$, such that no letter occurs in both.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Corollary 4.

Stated but not proved: `MetaMathlibExt.weaklyDecreasingNonIntersectingPairs_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#weakly-decreasing-non-intersecting-pairs-2).

## Non-intersecting pairs of weakly decreasing words of equal length

For natural numbers $k$
and $n \ge 1$, the number of pairs $(u, v)$ of weakly decreasing words of length $n$ over an
ordered alphabet of $k$ letters such that no letter occurs in both is
$\sum_{j=1}^{k-1} \binom{k}{j} \binom{n-1}{j-1} \binom{n+k-j-1}{n}$.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Corollary 5.

Stated but not proved: `MetaMathlibExt.weaklyDecreasingNonIntersectingPairs_sameLength_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#weakly-decreasing-non-intersecting-pairs-3).

## Overlap statistic on pairs of weakly decreasing words

Fix natural numbers $k$, $n \ge 1$,
$r \ge 1$ and a rational number $q$, and order an alphabet of $k$ letters. For words $u$ and $v$
over this alphabet, the overlap of $(u, v)$ is the number of positions of $v$ whose letter occurs
in $u$. Write $[x^m] F$ for the coefficient of $x^m$ in a formal power series $F$ over
$\mathbb{Q}$. Let $T$ be the sum of $q^{\text{overlap}}$ over all pairs $(u, v)$ of weakly
decreasing words, $u$ of length $n$ and $v$ of length $r$. Then
$T = \sum_{j=1}^{k} \binom{k}{j} \, [x^n]\bigl(x^j (1-x)^{-j}\bigr) \,
[x^r]\Bigl((1-x)^{-(k-j)} - 1 + (1-x)^{-(k-j)} \sum_{m \ge 1} \binom{m+j-1}{m} q^m x^m\Bigr)$
and
$T = \sum_{j=1}^{k} \binom{k}{j} \, [x^n]\bigl(x^j (1-x)^{-j}\bigr) \,
[x^r]\bigl(-1 + (1-x)^{-(k-j)} (1 - qx)^{-j}\bigr)$.

The paper prints these sums over $j$ with upper limit $k - 1$, which omits the pairs whose first
word uses all $k$ letters ($j = k$, which Theorem 2 includes): for $k = 1$ and $n = r = 1$ the
only pair contributes $q$, while the printed sum is empty.

## Sources

- Aubrey Blecher and Arnold Knopfmacher, *Intersections in Pairs of Words*, INTEGERS 24 (2024), Article A107, Theorem 4.

Stated but not proved: `MetaMathlibExt.weaklyDecreasingPairs_overlap_sum_eq_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WordPairIntersectionsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html#weakly-decreasing-pairs-overlap-sum-eq-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intersections in pairs of words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/intersections-in-pairs-of-words)
