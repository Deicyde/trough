---
declaration: section
origin: cited
lean: MetaMathlibExt.coloredCompositionCount, MetaMathlibExt.coloredCompositionCount_one_three_two, MetaMathlibExt.coloredDyckPathCount, MetaMathlibExt.coloredDyckPathCount_one_three_two, MetaMathlibExt.polygonDiagonals, MetaMathlibExt.IsNoncrossingDiagonalSet, MetaMathlibExt.dissectionFaceSize, MetaMathlibExt.coloredPolygonDissectionCount
statement: formalized
---

# Colored compositions, Dyck paths and polygon dissections

16 results, 10 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html).

## Number of colored compositions

Let $\gamma = (\gamma_1, \gamma_2, \dots)$ be a sequence
of natural numbers and let $n, k$ be natural numbers. The number $c_{n,k}(\gamma)$ of
$\gamma$-colored compositions of $n$ with $k$ parts counts the compositions of $n$ with exactly $k$
parts in which each part equal to $j$ carries one of $\gamma_j$ colors: it is the sum, over all
compositions $(a_1, \dots, a_k)$ of $n$ into $k$ positive parts, of
$\gamma_{a_1} \cdots \gamma_{a_k}$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Compositions).

Formalized by `MetaMathlibExt.coloredCompositionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-composition-count).

## Compositions of 3 into two parts

With one color for every part ($\gamma_j = 1$ for all
$j$), the number of colored compositions of $3$ with $2$ parts is $c_{3,2}(\gamma) = 2$: the
compositions $(1,2)$ and $(2,1)$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2.

Formalized by `MetaMathlibExt.coloredCompositionCount_one_three_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-composition-count-one-three-two).

## Number of colored Dyck paths

Let $\gamma = (\gamma_1, \gamma_2, \dots)$ be a sequence of
natural numbers and let $n, k$ be natural numbers. In a Dyck path, each peak $UD$ together with the
maximal run of $D$ steps starting at its $D$ forms a primitive block $UD^j$. The number
$d_{n,k}(\gamma)$ counts the Dyck paths of semilength $n$ with exactly $k$ peaks in which each
primitive block $UD^j$ carries one of $\gamma_j$ colors: it is the sum, over all Dyck paths of
semilength $n$ with $k$ peaks, of the product of $\gamma_j$ over their primitive blocks $UD^j$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Dyck paths).

Formalized by `MetaMathlibExt.coloredDyckPathCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-dyck-path-count).

## Dyck paths of semilength 3 with two peaks

With one color for every block ($\gamma_j = 1$
for all $j$), the number of colored Dyck paths of semilength $3$ with $2$ peaks is
$d_{3,2}(\gamma) = 3$, a Narayana number.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2.

Formalized by `MetaMathlibExt.coloredDyckPathCount_one_three_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-dyck-path-count-one-three-two).

## Diagonals of a convex polygon

For $n \in \mathbb{N}$, label the vertices of the convex
$(n+2)$-gon $0, 1, \dots, n+1$ in cyclic order. Its diagonals are the pairs $(a, b)$ of natural
numbers with $a + 2 \le b \le n + 1$ and $(a, b) \ne (0, n+1)$; the excluded pair is the side
joining the vertices $0$ and $n+1$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Polygon partitions).

Formalized by `MetaMathlibExt.polygonDiagonals`, a definition declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#polygon-diagonals).

## Noncrossing sets of diagonals

A finite set $D$ of pairs of natural numbers is
noncrossing when there are no $(a, b) \in D$ and $(c, d) \in D$ with $a < c < b < d$. For
diagonals $(a, b)$ with $a < b$ of a convex polygon whose vertices are labelled by natural numbers
in cyclic order, this says that no two diagonals of $D$ cross in the interior of the polygon.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Polygon partitions).

Formalized by `MetaMathlibExt.IsNoncrossingDiagonalSet`, a definition declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#is-noncrossing-diagonal-set).

## Size of the polygon under a chord

Let $D$ be a finite set of pairs of natural numbers
and let $e = (a, b)$ be a pair of natural numbers. The face size of $e$ in $D$ is $2$ plus the
number of natural numbers $v$ with $a < v < b$ for which there is no pair $(c, d) \in D$ other
than $e$ with $a \le c < v < d \le b$. When $D$ is a noncrossing set of diagonals of the convex
$(n+2)$-gon with vertices $0, \dots, n+1$ in cyclic order and $e$ is a diagonal in $D$ or the root
side $(0, n+1)$, this is the number of vertices of the polygon of the dissection that lies
directly under $e$, on the side of the vertices $a, \dots, b$: the endpoints $a$ and $b$ and the
vertices between them that no other chord of $D$ under $e$ cuts off. Every polygon of the
dissection lies directly under exactly one such chord.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Polygon partitions).

Formalized by `MetaMathlibExt.dissectionFaceSize`, a definition declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#dissection-face-size).

## Colored polygon dissection count

Let $\gamma : \mathbb{N} \to \mathbb{N}$ and
$n, k \in \mathbb{N}$. For $n \ge 1$, label the vertices of the convex $(n+2)$-gon $0, \dots, n+1$
in cyclic order, with root side $(0, n+1)$. Then $p_{n,k}(\gamma)$ is the sum, over all sets $D$ of
$k - 1$ pairwise noncrossing diagonals of this polygon, of the product, over the root side and
the diagonals $e$ of $D$, of $\gamma(j_e)$, where $j_e + 2$ is the number of vertices of the
polygon of the dissection lying directly under $e$. Every polygon of the dissection lies directly
under exactly one of these chords, so $p_{n,k}(\gamma)$ counts the partitions of the rooted
$(n+2)$-gon into $k$ polygons by $k - 1$ noncrossing diagonals in which each $(j+2)$-gon is
colored in one of $\gamma(j)$ ways. For $k = 0$ the sum is empty, so $p_{n,0}(\gamma) = 0$.
For $n = 0$ (a degenerate $2$-gon) the count is set to $p_{0,k}(\gamma) = 0$, so $\gamma(0)$
never enters.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Polygon partitions).

Formalized by `MetaMathlibExt.coloredPolygonDissectionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-polygon-dissection-count).

## Dissections of a pentagon into two polygons

With one color for every polygon, that is
$\gamma(j) = 1$ for all $j$, the colored polygon dissection count satisfies $p_{3,2}(\gamma) = 5$:
a convex pentagon has five diagonals, and each one cuts it into two polygons.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2.

Formalized by `MetaMathlibExt.coloredPolygonDissectionCount_one_three_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-polygon-dissection-count-one-thr).

## Colored dissections of a hexagon by one diagonal

Let $\gamma_1 = 2$, $\gamma_2 = 3$,
$\gamma_3 = 5$ and $\gamma_j = 0$ for every other $j$. The number of partitions of a rooted convex
hexagon by one diagonal into $2$ polygons in which each $(j+2)$-gon carries one of $\gamma_j$
colors is $p_{4,2}(\gamma) = 87$: three diagonals cut the hexagon into two quadrilaterals and six
cut it into a triangle and a pentagon, giving $3 \cdot 3^2 + 6 \cdot 2 \cdot 5 = 87$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2.

Formalized by `MetaMathlibExt.coloredPolygonDissectionCount_hexagon_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-polygon-dissection-count-hexagon).

## Hoggatt–Lind formula for colored compositions

Let $\gamma = (\gamma_1, \gamma_2, \dots)$
be a sequence of natural numbers and let $c_{n,k}(\gamma)$ be the number of compositions of $n$
with $k$ parts in which each part $j$ carries one of $\gamma_j$ colors. For every natural number
$n \ge 1$ and every natural number $k$, as rational numbers,

$$c_{n,k}(\gamma) = \frac{k!}{n!} B_{n,k}(1! \, \gamma_1, 2! \, \gamma_2, \dots),$$

where $B_{n,k}$ is the partial Bell polynomial.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Proposition 1 (`jis-2024-24.5.2-prop-1`), citing Hoggatt and Lind.

Stated but not proved: `MetaMathlibExt.coloredCompositionCount_eq_partialBell` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-composition-count-eq-partial-bel).

## Mansour–Sun formula for colored Dyck paths

Let $\gamma = (\gamma_1, \gamma_2, \dots)$ be
a sequence of natural numbers and let $d_{n,k}(\gamma)$ be the number of Dyck paths of semilength
$n$ with $k$ peaks in which each block $UD^j$, formed by a peak and the maximal run of $D$ steps
starting at its $D$, carries one of $\gamma_j$ colors. For every natural number $n \ge 1$ and
every natural number $k$, as rational numbers,

$$d_{n,k}(\gamma) = \frac{1}{(n+1-k)!} B_{n,k}(1! \, \gamma_1, 2! \, \gamma_2, \dots),$$

where $B_{n,k}$ is the partial Bell polynomial and $n + 1 - k$ is truncated subtraction, which is
$0$ when $k > n + 1$.

For $k \le n + 1$ the factor is $1/(n-k+1)!$; for every $k > n$ both sides vanish because
$B_{n,k} = 0$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Proposition 2 (`jis-2024-24.5.2-prop-2`), citing Mansour and Sun.

Stated but not proved: `MetaMathlibExt.coloredDyckPathCount_eq_partialBell` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-dyck-path-count-eq-partial-bell).

## Birmajer–Gil–Weiner formula for colored polygon partitions

Let
$\gamma = (\gamma_1, \gamma_2, \dots)$ be a sequence of natural numbers and let $p_{n,k}(\gamma)$
be the number of partitions of a rooted convex $(n+2)$-gon by $k - 1$ noncrossing diagonals into
$k$ polygons in which each $(j+2)$-gon carries one of $\gamma_j$ colors. For all natural numbers
$n \ge 1$ and $k \ge 1$, as rational numbers,

$$p_{n,k}(\gamma) = \frac{1}{n+1}\binom{n+k}{k}\frac{k!}{n!}B_{n,k}(1!\gamma_1, 2!\gamma_2, \dots)$$

where $B_{n,k}$ is the partial Bell polynomial.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Proposition 3 (`jis-2024-24.5.2-prop-3`), citing Birmajer, Gil, and Weiner.

Stated but not proved: `MetaMathlibExt.coloredPolygonDissectionCount_eq_partialBell` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#colored-polygon-dissection-count-eq-part).

## Colored compositions and colored Dyck paths

Let $\gamma = (\gamma_1, \gamma_2, \dots)$
be a sequence of natural numbers. Let $c_{n,k}(\gamma)$ be the number of compositions of $n$ with
$k$ parts in which each part $j$ carries one of $\gamma_j$ colors, and let $d_{n,k}(\gamma)$ be the
number of Dyck paths of semilength $n$ with $k$ peaks in which each block $UD^j$, formed by a peak
and the maximal run of $D$ steps starting at its $D$, carries one of $\gamma_j$ colors. For all
natural numbers $n$ and $k$ with $1 \le k \le n$,

$$\binom{n}{k-1} c_{n,k}(\gamma) = k \, d_{n,k}(\gamma).$$

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Theorem 4 (`jis-2024-24.5.2-thm-4`).

Stated but not proved: `MetaMathlibExt.choose_mul_coloredCompositionCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#choose-mul-colored-composition-count-eq).

## Colored Dyck paths and colored polygon partitions

Let
$\gamma = (\gamma_1, \gamma_2, \dots)$ be a sequence of natural numbers. Let $d_{n,k}(\gamma)$ be
the number of Dyck paths of semilength $n$ with $k$ peaks in which each block $UD^j$, formed by a
peak and the maximal run of $D$ steps starting at its $D$, carries one of $\gamma_j$ colors, and
let $p_{n,k}(\gamma)$ be the number of partitions of a rooted convex $(n+2)$-gon by $k - 1$
noncrossing diagonals into $k$ polygons in which each $(j+2)$-gon carries one of $\gamma_j$
colors. For all natural numbers $n$ and $k$ with $1 \le k \le n$,

$$\binom{n+k}{k} d_{n,k}(\gamma) = \binom{n+1}{k} p_{n,k}(\gamma).$$

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Theorem 6 (`jis-2024-24.5.2-thm-6`).

Stated but not proved: `MetaMathlibExt.choose_mul_coloredDyckPathCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#choose-mul-colored-dyck-path-count-eq).

## Polygon partitions and colored compositions

For every coloring sequence
$\gamma : \mathbb{N} \to \mathbb{N}$ and all natural numbers $n$ and $k$ with $1 \le k \le n$, the
colored polygon dissection count $p_{n,k}(\gamma)$ and the colored composition count
$c_{n,k}(\gamma)$ satisfy

$$(n+1)\, p_{n,k}(\gamma) = \binom{n+k}{k}\, c_{n,k}(\gamma).$$

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Theorem 8 (`jis-2024-24.5.2-thm-8`).

Stated but not proved: `MetaMathlibExt.succ_mul_coloredPolygonDissectionCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/ColoredCompositionsDyckPolygonsWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html#succ-mul-colored-polygon-dissection-coun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Colored compositions, Dyck paths and polygon dissections](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/colored-compositions-dyck-paths-and-polygon-diss)
