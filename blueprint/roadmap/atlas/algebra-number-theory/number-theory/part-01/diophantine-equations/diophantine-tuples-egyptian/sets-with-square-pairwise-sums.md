---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.PairwiseSumsSquares, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.IsSemiMagicRoots, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_int_pairwiseSumsSquares_scale_translate, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_triple_of_isSemiMagicRoots, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_isSemiMagicRoots_of_pairwiseSumsSquares_triple, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quintuple_of_isSemiMagicRoots, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_isSemiMagicRoots_f_of_pairwiseSumsSquares_quintuple, MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quadruple_of_isSemiMagicRoots
statement: formalized
---

# Sets with square pairwise sums

16 results, 2 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html).

## Families whose pairwise sums are squares

Let $\alpha$ be a type with an addition and a
multiplication, and let $(a_i)_{i \in I}$ and $(b_j)_{j \in J}$ be families in $\alpha$ indexed by
arbitrary types $I$ and $J$. They have all pairwise sums square when, for every $i \in I$ and
$j \in J$, the sum $a_i + b_j$ is a square in $\alpha$, that is, $a_i + b_j = c \cdot c$ for some
$c \in \alpha$.

Formalized by `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.PairwiseSumsSquares`, a definition declared in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares).

## Semi-magic matrix of squares

A $3 \times 3$ integer matrix $E = (e_{ij})$ has semi-magic
squares when the matrix $(e_{ij}^2)$ of its squared entries is semi-magic: there is an integer
$S$ such that $\sum_{j=1}^{3} e_{ij}^2 = S$ for every row $i$ and $\sum_{i=1}^{3} e_{ij}^2 = S$ for
every column $j$.

Formalized by `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.IsSemiMagicRoots`, a definition declared in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#is-semi-magic-roots).

## Scaling rational families with square pairwise sums to integers

Let $a_1, \dots, a_m$
and $b_1, \dots, b_n$ be rational numbers such that every sum $a_i + b_j$ is the square of a
rational number, and let $t$ be an integer and $k$ a rational number such that $k^2 a_i - t$ is an
integer for every $i$ and $k^2 b_j + t$ is an integer for every $j$. Then the integers
$a_i' = k^2 a_i - t$ and $b_j' = k^2 b_j + t$ are such that every sum $a_i' + b_j'$ is the square
of an integer.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_int_pairwiseSumsSquares_scale_translate` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#exists-int-pairwise-sums-squares-scale-t).

## Triples with square pairwise sums from a semi-magic square of squares

Let $e_{ij}$,
$1 \le i, j \le 3$, be integers such that the matrix of squares $(e_{ij}^2)$ is semi-magic, that
is, all its row sums and all its column sums are equal. Put $a_1 = e_{13}^2$, $a_2 = e_{31}^2$,
$a_3 = e_{22}^2$ and $b_1 = 0$, $b_2 = e_{21}^2 - e_{13}^2$, $b_3 = e_{11}^2 - e_{22}^2$. Then
$a_i + b_j$ is a perfect square for all $i, j \in \{1, 2, 3\}$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_triple_of_isSemiMagicRoots` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-triple-of-is-semi).

## Triples with square pairwise sums come from semi-magic squares

Let $a_1, a_2, a_3$ and
$b_1, b_2, b_3$ be integers such that every sum $a_i + b_j$ is the square of an integer. Then
there is a $3 \times 3$ integer matrix $E = (e_{ij})$ whose squared entries $e_{ij}^2$ have all
three row sums and all three column sums equal to one common integer, and such that
$e_{11}^2 = a_3 + b_3$, $e_{12}^2 = a_2 + b_2$, $e_{13}^2 = a_1 + b_1$, $e_{21}^2 = a_1 + b_2$,
$e_{22}^2 = a_3 + b_1$, $e_{23}^2 = a_2 + b_3$, $e_{31}^2 = a_2 + b_1$, $e_{32}^2 = a_1 + b_3$ and
$e_{33}^2 = a_3 + b_2$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_isSemiMagicRoots_of_pairwiseSumsSquares_triple` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#exists-is-semi-magic-roots-of-pairwise-s).

## Five integers with square sums from two semi-magic squares of squares

Let $e_{ij}$ and
$f_{ij}$, $1 \le i, j \le 3$, be integers such that the matrices of squares $(e_{ij}^2)$ and
$(f_{ij}^2)$ are both semi-magic (in each matrix all row sums and all column sums are equal) and
have the same diagonal, $e_{ii}^2 = f_{ii}^2$ for $i = 1, 2, 3$. Put $a_1 = e_{13}^2$,
$a_2 = e_{31}^2$, $a_3 = e_{22}^2$, $a_4 = f_{13}^2$, $a_5 = f_{31}^2$ and $b_1 = 0$,
$b_2 = e_{21}^2 - e_{13}^2$, $b_3 = e_{11}^2 - e_{22}^2$. Then $a_i + b_j$ is a perfect square for
all $1 \le i \le 5$ and $1 \le j \le 3$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quintuple_of_isSemiMagicRoots` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-quintuple-of-is-se).

## Quintuple extensions come from a second semi-magic square

Let $E = (e_{ij})$ be a
$3 \times 3$ integer matrix whose squared entries $e_{ij}^2$ have all three row sums and all three
column sums equal to one common integer. Put $(a_1, a_2, a_3) = (e_{13}^2, e_{31}^2, e_{22}^2)$ and
$(b_1, b_2, b_3) = (0, e_{21}^2 - e_{13}^2, e_{11}^2 - e_{22}^2)$, and let $a_4, a_5$ be integers
such that every sum $a_i + b_j$ with $1 \le i \le 5$ and $1 \le j \le 3$ is the square of an
integer. Then there is a $3 \times 3$ integer matrix $F = (f_{ij})$ whose squared entries also
have all row sums and all column sums equal to one common integer, with $f_{11}^2 = e_{11}^2$,
$f_{22}^2 = e_{22}^2$, $f_{33}^2 = e_{33}^2$, $a_4 = f_{13}^2$ and $a_5 = f_{31}^2$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_isSemiMagicRoots_f_of_pairwiseSumsSquares_quintuple` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#exists-is-semi-magic-roots-f-of-pairwise).

## Extending the triples to quadruples with square pairwise sums

Let $E = (e_{ij})$,
$G = (g_{ij})$ and $H = (h_{ij})$ be $3 \times 3$ integer matrices, each of whose squared entries
have all three row sums and all three column sums equal to one common integer, such that
$e_{12}^2 = g_{12}^2$, $e_{13}^2 = g_{13}^2$, $e_{21}^2 = g_{21}^2$, $e_{31}^2 = g_{31}^2$,
$e_{11}^2 = h_{11}^2$, $e_{22}^2 = h_{22}^2$, $g_{11}^2 = h_{12}^2$ and $g_{22}^2 = h_{31}^2$. Put
$(a_1, a_2, a_3, a_4) = (e_{13}^2, e_{31}^2, e_{22}^2, g_{22}^2)$ and
$(b_1, b_2, b_3, b_4) = (0, e_{21}^2 - e_{13}^2, e_{11}^2 - e_{22}^2, g_{11}^2 - g_{22}^2)$. Then
$a_i + b_j$ is the square of an integer for all $1 \le i, j \le 4$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quadruple_of_isSemiMagicRoots` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-quadruple-of-is-se).

## Quadruple extensions come from two further semi-magic squares

Let $E = (e_{ij})$ be a
$3 \times 3$ integer matrix whose squared entries $e_{ij}^2$ have all three row sums and all three
column sums equal to one common integer. Put $(a_1, a_2, a_3) = (e_{13}^2, e_{31}^2, e_{22}^2)$ and
$(b_1, b_2, b_3) = (0, e_{21}^2 - e_{13}^2, e_{11}^2 - e_{22}^2)$, and let $a_4, b_4$ be integers
such that every sum $a_i + b_j$ with $1 \le i, j \le 4$ is the square of an integer. Then there
are $3 \times 3$ integer matrices $G = (g_{ij})$ and $H = (h_{ij})$, each of whose squared entries
have all row sums and all column sums equal to one common integer, such that
$g_{12}^2 = e_{12}^2$, $g_{13}^2 = e_{13}^2$, $g_{21}^2 = e_{21}^2$, $g_{31}^2 = e_{31}^2$,
$h_{11}^2 = e_{11}^2$, $h_{22}^2 = e_{22}^2$, $h_{12}^2 = g_{11}^2$, $h_{31}^2 = g_{22}^2$,
$a_4 = g_{22}^2$ and $b_4 = g_{11}^2 - g_{22}^2$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.exists_isSemiMagicRoots_gh_of_pairwiseSumsSquares_quadruple` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#exists-is-semi-magic-roots-gh-of-pairwis).

## Four-parameter triples with square pairwise sums, family (3.1)

For all integers
$p, q, r, s$, put $a_1 = 0$, $a_2 = 16pqrs$, $a_3 = (p+q+r+s)(p+q-r-s)(p-q+r-s)(p-q-r+s)$ and
$b_1 = 4(pr - qs)^2$, $b_2 = 4(ps - qr)^2$, $b_3 = 4(pq - rs)^2$. Then $a_i + b_j$ is a perfect
square for all $i, j \in \{1, 2, 3\}$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_triple_family31` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-triple-family31).

## Four-parameter triples with square pairwise sums, family (3.2)

For all integers
$p, q, r, s$, put $a_1 = -(p+q+r+s)(p+q-r-s)(p-q+r-s)(p-q-r+s)$,
$a_2 = -(p-q+r+s)(p-q-r-s)(p+q+r-s)(p+q-r+s)$, $a_3 = 0$ and
$b_1 = (p^2 - q^2 + r^2 - s^2)^2$, $b_2 = (p^2 - q^2 - r^2 + s^2)^2$,
$b_3 = (p^2 + q^2 - r^2 - s^2)^2$. Then $a_i + b_j$ is a perfect square for all
$i, j \in \{1, 2, 3\}$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_triple_family32` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-triple-family32).

## Four-parameter triples with square pairwise sums, family (3.3)

For all integers
$p, q, r, s$, put $a_1 = 4(ps - qr)^2$, $a_2 = 4(ps + qr)^2$, $a_3 = (p^2 - q^2 - r^2 + s^2)^2$
and $b_1 = 4(p^2 - q^2)(r^2 - s^2)$, $b_2 = 0$, $b_3 = 4(p^2 - r^2)(q^2 - s^2)$. Then $a_i + b_j$
is a perfect square for all $i, j \in \{1, 2, 3\}$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_triple_family33` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-triple-family33).

## A seven-parameter family of five and three rationals with square pairwise sums

For
rational numbers $f, g, m, u_1, u_2, v_1, v_2$, put
$\alpha = m u_1 u_2 (u_1 v_1 - u_2 v_2)$, $\beta = (u_1 v_2 - u_2 v_1)(m^2 u_1 u_2 v_1 v_2 - 1)$,
$\gamma = m v_1 v_2 (u_1 v_1 - u_2 v_2)$, $\alpha' = m u_1 u_2 (u_1 v_1 + u_2 v_2)$,
$\beta' = (u_1 v_2 + u_2 v_1)(m^2 u_1 u_2 v_1 v_2 + 1)$ and
$\gamma' = m v_1 v_2 (u_1 v_1 + u_2 v_2)$, and let
$a_1 = 4(\alpha f^2 - \beta f g - \gamma g^2)^2$,
$a_2 = 4(\alpha' f^2 + \beta' f g + \gamma' g^2)^2$,
$a_3 = \bigl((u_1^2 u_2^2 (v_1^2 - v_2^2) m^2 + u_1^2 - u_2^2) f^2 -
(v_1^2 v_2^2 (u_1^2 - u_2^2) m^2 + v_1^2 - v_2^2) g^2\bigr)^2$,
$a_4 = 4(\alpha f^2 + \beta f g - \gamma g^2)^2$,
$a_5 = 4(\alpha' f^2 - \beta' f g + \gamma' g^2)^2$,
$b_1 = 0$,
$b_2 = -4 (u_1^2 - u_2^2)(v_1^2 - v_2^2)(m^2 u_1^2 u_2^2 f^2 - g^2)(f^2 - m^2 v_1^2 v_2^2 g^2)$
and
$b_3 = 4 (m^2 u_1^2 v_1^2 - 1)(m^2 u_2^2 v_2^2 - 1)(f^2 u_1^2 - g^2 v_1^2)(f^2 u_2^2 - g^2 v_2^2)$.
Then $a_i + b_j$ is the square of a rational number for all $1 \le i \le 5$ and $1 \le j \le 3$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quintuple_family41` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-quintuple-family41).

## A four-parameter family of integer quadruples with square pairwise sums

For integers
$u_1, u_2, v_1, v_2$, put $w = v_1^4 - 6 v_1^2 v_2^2 + v_2^4$, $s = v_1^2 + v_2^2$ and
$d = v_1^2 - v_2^2$, and let
$a_1 = w^2 d^2 (u_1^2 + u_2^2)^2$, $a_2 = w^2 s^2 (u_1^2 - u_2^2)^2$,
$a_3 = d^2 (s^2 u_1^2 - 16 u_1 u_2 v_1^2 v_2^2 - s^2 u_2^2)^2$,
$a_4 = d^2 (s^2 u_1^2 + 16 u_1 u_2 v_1^2 v_2^2 - s^2 u_2^2)^2$, $b_1 = 0$,
$b_2 = w^2 \bigl((v_2 - v_1) u_1 + (v_1 + v_2) u_2\bigr)
\bigl((v_1 + v_2) u_1 + (v_1 - v_2) u_2\bigr)\bigl((v_1 - v_2) u_1 + (v_1 + v_2) u_2\bigr)
\bigl((v_1 + v_2) u_1 - (v_1 - v_2) u_2\bigr)$,
$b_3 = -d^2 (s u_1 + 4 u_1 v_1 v_2 - s u_2)(s u_1 - 4 u_1 v_1 v_2 - s u_2)
(s u_1 + 4 u_2 v_1 v_2 + s u_2)(s u_1 - 4 u_2 v_1 v_2 + s u_2)$ and
$b_4 = -d^2 (s u_1 + 4 u_1 v_1 v_2 + s u_2)(s u_1 - 4 u_1 v_1 v_2 + s u_2)
(s u_1 + 4 u_2 v_1 v_2 - s u_2)(s u_1 - 4 u_2 v_1 v_2 - s u_2)$.
Then $a_i + b_j$ is the square of an integer for all $1 \le i, j \le 4$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quadruple_family51` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-quadruple-family51).

## First three-parameter family of rational quadruples with square pairwise sums

For
rational numbers $m, q, r$, let
$a_1 = 16 m^2 (m^4 - 1)^2 \bigl((5m^4 - 2m^2 + 1) q^2 - 2(m^4 - 6m^2 + 1) q r +
(m^4 - 2m^2 + 5) r^2\bigr)^2$,
$a_2 = 16 m^2 (m^4 - 1)^2 \bigl((5m^4 - 2m^2 + 1) q^2 - (m^4 - 2m^2 + 5) r^2\bigr)^2$,
$a_3 = 16 m^2 (m^4 - 1)^2 \bigl((7m^4 - 2m^2 - 1) q^2 - (2m^4 - 12m^2 + 2) q r -
(m^4 + 2m^2 - 7) r^2\bigr)^2$,
$a_4 = (m^2 - 1)^2 \bigl((3m^8 + 40m^6 - 26m^4 - 1) q^2 + 2(m^4 - 6m^2 + 1)^2 q r -
(m^8 + 26m^4 - 40m^2 - 3) r^2\bigr)^2$,
$b_1 = 0$,
$b_2 = -4 m^2 \bigl((m^4 + 6m^2 - 3) q + (m^4 - 2m^2 + 5) r\bigr)
\bigl((3m^4 - 6m^2 - 1) q - (m^4 - 2m^2 + 5) r\bigr)
\bigl((5m^4 - 2m^2 + 1) q - (3m^4 - 6m^2 - 1) r\bigr)
\bigl((5m^4 - 2m^2 + 1) q + (m^4 + 6m^2 - 3) r\bigr)$,
$b_3 = -128 m^2 (m^4 - 1)^3 (q^2 - r^2)(3m^2 q - m^2 r - q + 3r)(m^2 q + r)$ and
$b_4 = 16 (m^2 + 1)^2 (m^2 - 1)^3 (m^2 q^2 - r^2)
\bigl((m^4 + 6m^3 - 2m - 1) q - (m^4 + 2m^3 - 6m - 1) r\bigr)
\bigl((m^4 - 6m^3 + 2m - 1) q - (m^4 - 2m^3 + 6m - 1) r\bigr)$.
Then $a_i + b_j$ is the square of a rational number for all $1 \le i, j \le 4$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quadruple_family58` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-quadruple-family58).

## Second three-parameter family of rational quadruples with square pairwise sums

For
rational numbers $m, q, r$, let
$a_1 = 16 m^2 (m^4 - 1)^2 \bigl((m^6 - 2m^4 + 5m^2) q^2 + (2m^5 - 12m^3 + 2m) q r +
(5m^4 - 2m^2 + 1) r^2\bigr)^2$,
$a_2 = 16 m^2 (m^4 - 1)^2 \bigl((m^6 - 2m^4 + 5m^2) q^2 - (5m^4 - 2m^2 + 1) r^2\bigr)^2$,
$a_3 = (m^2 - 1)^2 \bigl((m^{10} + 26m^6 - 40m^4 - 3m^2) q^2 +
(2m^9 - 24m^7 + 76m^5 - 24m^3 + 2m) q r - (3m^8 + 40m^6 - 26m^4 - 1) r^2\bigr)^2$,
$a_4 = 16 m^2 (m^4 - 1)^2 \bigl((m^6 + 2m^4 - 7m^2) q^2 - (2m^5 - 12m^3 + 2m) q r -
(7m^4 - 2m^2 - 1) r^2\bigr)^2$,
$b_1 = 0$,
$b_2 = -4 m^2 \bigl((m^5 + 6m^3 - 3m) q - (5m^4 - 2m^2 + 1) r\bigr)
\bigl((3m^5 - 6m^3 - m) q + (5m^4 - 2m^2 + 1) r\bigr)
\bigl((m^5 - 2m^3 + 5m) q + (3m^4 - 6m^2 - 1) r\bigr)
\bigl((m^5 - 2m^3 + 5m) q - (m^4 + 6m^2 - 3) r\bigr)$,
$b_3 = -16 m^2 (m^2 + 1)^2 (m^2 - 1)^3 (q^2 - r^2)
\bigl((m^5 - 2m^4 + 6m^2 - m) q + (m^4 - 6m^3 + 2m - 1) r\bigr)
\bigl((m^5 + 2m^4 - 6m^2 - m) q + (m^4 + 6m^3 - 2m - 1) r\bigr)$ and
$b_4 = 128 m^3 (m^4 - 1)^3 (m r - q)(m^2 q^2 - r^2)\bigl((m^3 - 3m) q + (3m^2 - 1) r\bigr)$.
Then $a_i + b_j$ is the square of a rational number for all $1 \le i, j \le 4$.

## Sources

- Ajai Choudhry, "Two Sets of Integers Such That All Elements of the Sumset of the Two Sets Are Perfect Squares", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.TwoSetsSumsetSquaresWanted.pairwiseSumsSquares_quadruple_family59` is written with `theorem_wanted` in [WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/TwoSetsSumsetSquaresWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html#pairwise-sums-squares-quadruple-family59).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sets with square pairwise sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/sets-with-square-pairwise-sums)
