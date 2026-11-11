---
declaration: section
origin: cited
lean: MetaMathlibExt.compositionShade, MetaMathlibExt.totalCompositionShade, MetaMathlibExt.compositionShade_four, MetaMathlibExt.compositionShade_one_three, MetaMathlibExt.compositionShade_le_totalCompositionShade, MetaMathlibExt.totalCompositionShade_zero, MetaMathlibExt.totalCompositionShade_generatingFunction
statement: formalized
---

# Shade of integer compositions

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html).

## Shade of a composition

Let $x = (x_0, x_1, \ldots, x_{k-1})$ be a finite list of
natural numbers (the parts of a composition), drawn as a bargraph whose column $c$ has height
$x_c$, with $x_c = 0$ for $c \ge k$. A cell $(c, h)$ with column $c \ge 0$ and height $h \ge 1$
is shaded when $h > x_c$ and $x_j \ge h + (c - j)$ for some column $j < c$. The shade of $x$
is the number of shaded cells.

Every shaded cell satisfies $c < k + s$ and $h \le s$, where $s = x_0 + \cdots + x_{k-1}$,
so the number of shaded cells is finite.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Section 1.

Formalized by `MetaMathlibExt.compositionShade`, a definition declared in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#composition-shade).

## Total shade of compositions

For a natural number $n$, the total shade $c(n)$ is the
sum of the shades of all compositions of $n$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Section 2.

Formalized by `MetaMathlibExt.totalCompositionShade`, a definition declared in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#total-composition-shade).

## Shade of the composition 4

The one-part composition $4$ has shade $6$: its
bargraph has $6$ shaded cells.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Figure 5.

Formalized by `MetaMathlibExt.compositionShade_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#composition-shade-four).

## Shade of the composition 1 + 3

The composition $1 + 3$ has shade $3$: its bargraph
has $3$ shaded cells.

All three shaded cells lie to the right of the bargraph.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Figure 5.

Formalized by `MetaMathlibExt.compositionShade_one_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#composition-shade-one-three).

## The total shade bounds the shade of each composition

For every natural number $n$
and every composition $x$ of $n$, the shade of $x$ is at most the total shade $c(n)$ of the
compositions of $n$.

For example, since the composition $4$ has shade $6$, this gives $c(4) \ge 6$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Section 2.

Formalized by `MetaMathlibExt.compositionShade_le_totalCompositionShade`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#composition-shade-le-total-composition-s).

## Total shade of the compositions of zero

The total shade $c(0)$ of the compositions
of $0$ is zero: $c(0) = 0$.

The only composition of $0$ is the empty one, whose bargraph has no shaded cells.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Section 2.

Formalized by `MetaMathlibExt.totalCompositionShade_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#total-composition-shade-zero).

## Generating function for the total shade of compositions

Let $c(n)$ be the total
shade of the compositions of $n$, and let $q$ be a real number with $0 < q < 1/4$. For natural
numbers $i_2, i_3, s_1, s_3$ put

$$A_{i_2, i_3, s_1, s_3} = (s_1 - s_3) \prod_{i_3 < i < i_2} (1 - q^{s_1 - i + 1}) +
\sum_{i_3 < j < i_2} \Big( \prod_{i_3 < i < i_2, i \ne j} (1 - q^{s_1 - i + 1}) \Big)
\frac{j(q - 1) + q^{s_1 + 1 - j} + s_1 - q(1 + s_1)}{1 - q},$$



$$B_{i_2} = 1 + \sum_{m \ge 1} q^{-i_2 m - m(m - 1)/2} (1 - q)^{-m} q^{m(1 + 2 i_2 + m)/2},$$

and for natural numbers $i, j, s$ put

$$E_{i, j, s} = -1 - q^{1 - i - j + s} (-2 + i + j - s) + q^{2 - i - j + s} (-1 + i + j - s).$$

Let

$$D_L(q) = \sum_{i_1 \ge 1} \sum_{s_1 \ge i_1 + 2} \Big( \frac{1}{1 - q} \Big)^{i_1 - 2}
\Big( \prod_{r=1}^{i_1 - 1} (1 - q^{s_1 - r}) \Big) q^{i_1 (i_1 - 1)/2 - i_1 s_1}
\sum_{i_2 = i_1 + 2}^{s_1 + 1} \sum_{s_2 \ge s_1 + 1} \sum_{i_3 = i_1 + 1}^{i_2 - 1}
\sum_{s_3 = i_3}^{s_1 - 1} q^{i_3 s_1 + s_2 + s_3 - (i_3 + i_3^2)/2}
\Big( \frac{1}{1 - q} \Big)^{i_2 - i_3} A_{i_2, i_3, s_1, s_3} B_{i_2},$$



$$D_R(q) = \sum_{i \ge 1} \sum_{s \ge i} \Big( \prod_{r=1}^{i-1} (1 - q^{s - r}) \Big)
\frac{q^s}{(1 - q)^{i-1}} \Big( \binom{s - i + 1}{2} \sum_{m=0}^{s-1} \frac{q^m}{(1 - q)^m}
\prod_{r=1}^{m} (1 - q^{s + 1 - i - r}) +
\frac{1}{(1 - q)^2} \sum_{m=1}^{s-1} \sum_{j=1}^{m} \frac{q^m}{(1 - q)^{m-1}}
\Big( \prod_{1 \le r \le m, r \ne j} (1 - q^{s + 1 - i - r}) \Big) E_{i, j, s} \Big).$$

Then

$$\sum_{n \ge 0} c(n) q^n = D_L(q) + D_R(q).$$

Empty sums are $0$ and empty products are $1$; all exponents are integers and may be
negative. For $0 < q < 1/4$ all these series converge absolutely.

This is Theorem 1 of the paper with two corrected readings. In the paper's display for
$D_L(q)$ the outer double sum over $i_1, s_1$ (and the left-hand side $L(x, q, u)$) is
duplicated, a typesetting slip; reading it once reproduces the printed expansion
$2q^6 + 6q^7 + 24q^8 + \cdots$. In the display for $D_R(q)$ the product in the double sum
over $m, j$ runs over $r \ne j$, as in the paper's display (R) from which it is obtained by
setting $x = 1$; with the product over all $r$ as printed, the coefficient of $q^4$ in
$D_R(q)$ is $14$ instead of the printed $13$, and $D_L + D_R$ no longer matches the total
shade.

## Sources

- Aubrey Blecher, Arnold Knopfmacher and Michael Mays, *Shade in Compositions of Integers*, Journal of Integer Sequences 27 (2024), Article 24.5.6, Theorem 1 (`jis-2024-24.5.6-thm-1`).

Stated but not proved: `MetaMathlibExt.totalCompositionShade_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CompositionShadeWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html#total-composition-shade-generating-funct).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shade of integer compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/shade-of-integer-compositions)
