---
declaration: section
origin: cited
lean: MetaMathlibExt.dyckValleyHeights, MetaMathlibExt.dyckValleyHeights_UUDUDDUD, MetaMathlibExt.dyckValleyHeights_UDUUDUDD, MetaMathlibExt.IsNondecreasingDyckPath, MetaMathlibExt.nondecreasingDyckWords, MetaMathlibExt.card_nondecreasingDyckWords_three, MetaMathlibExt.card_nondecreasingDyckWords_four, MetaMathlibExt.dyckSubwordCount
statement: formalized
---

# Subwords in non-decreasing Dyck paths

33 results, 18 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html).

## Valley heights

For a finite sequence $l$ of up steps $U$ and down steps $D$, the valley
heights of $l$ form the list with one entry for each factor $DU$ of $l$, from left to right:
the number of $U$ steps minus the number of $D$ steps in $l$ up to and including the $D$ of
that factor, taken to be $0$ when negative.

## Sources

- Flórez and Ramírez, *Restricted Dyck paths on valleys sequence*, arXiv:2108.08299, Section 1, the definition of non-decreasing Dyck paths used by Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6.

Formalized by `MetaMathlibExt.dyckValleyHeights`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-valley-heights).

## Valley heights of UUDUDDUD

The Dyck path $UUDUDDUD$ has exactly two valleys, of heights
$1$ and $0$ from left to right.

In particular this path is not non-decreasing.

## Sources

- Flórez and Ramírez, *Restricted Dyck paths on valleys sequence*, arXiv:2108.08299, Section 1.

Formalized by `MetaMathlibExt.dyckValleyHeights_UUDUDDUD`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-valley-heights-uududdud).

## Valley heights of UDUUDUDD

The Dyck path $UDUUDUDD$ has exactly two valleys, of heights
$0$ and $1$ from left to right.

## Sources

- Flórez and Ramírez, *Restricted Dyck paths on valleys sequence*, arXiv:2108.08299, Section 1.

Formalized by `MetaMathlibExt.dyckValleyHeights_UDUUDUDD`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-valley-heights-uduududd).

## Non-decreasing Dyck paths

A Dyck path is non-decreasing when its valley heights (the
heights reached after the $D$ of each factor $DU$), read from left to right, form a
non-decreasing sequence.

## Sources

- Flórez and Ramírez, *Restricted Dyck paths on valleys sequence*, arXiv:2108.08299, Section 1 (the `0`-Dyck paths), as used by Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6.

Formalized by `MetaMathlibExt.IsNondecreasingDyckPath`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#is-nondecreasing-dyck-path).

## Non-decreasing Dyck paths of semilength $n$

For a natural number $n$, $D_n$ is the finite
set of Dyck paths of semilength $n$ that are non-decreasing: the heights of their valleys (the
height reached after the $D$ of each factor $DU$), read from left to right, form a non-decreasing
sequence.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.nondecreasingDyckWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-words).

## Five non-decreasing Dyck paths of semilength 3

There are exactly $5$ non-decreasing
Dyck paths of semilength $3$.

These are all five Dyck paths of semilength $3$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.card_nondecreasingDyckWords_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#card-nondecreasing-dyck-words-three).

## Thirteen non-decreasing Dyck paths of semilength 4

There are exactly $13$
non-decreasing Dyck paths of semilength $4$.

They are all $14$ Dyck paths of semilength $4$ except $UUDUDDUD$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.card_nondecreasingDyckWords_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#card-nondecreasing-dyck-words-four).

## Number of occurrences of a subword

For finite words $w$ and $l$ in the up step $U$ and
the down step $D$, the number of occurrences of $w$ in $l$ is the number of suffixes of $l$,
including $l$ itself and the empty suffix, that begin with $w$. Thus every occurrence of $w$ as a
contiguous subword of $l$ is counted, overlapping occurrences separately.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.dyckSubwordCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-subword-count).

## Occurrences of UU in UUUDDD

The contiguous subword $UU$ occurs exactly $2$ times in
$UUUDDD$; the two occurrences overlap.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.dyckSubwordCount_UU_UUUDDD`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-subword-count-uu-uuuddd).

## Occurrences of UDU in UDUDUD

The contiguous subword $UDU$ occurs exactly $2$ times in
$UDUDUD$; the two occurrences overlap.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.dyckSubwordCount_UDU_UDUDUD`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-subword-count-udu-ududud).

## Total occurrences of a subword in non-decreasing Dyck paths

For a word $w$ in the steps
$U$ and $D$ and for $n \ge 0$, $d_w(n)$ is the total number of occurrences of $w$ as a contiguous
subword (overlapping occurrences counted separately), summed over all non-decreasing Dyck paths
of semilength $n$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.nondecreasingDyckSubwordTotal`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-total).

## Peaks in the non-decreasing Dyck paths of semilength three

Let $d_w(n)$ be the total
number of occurrences of the subword $w$ over all non-decreasing Dyck paths of semilength $n$.
Then $d_{UD}(3) = 10$; that is, the non-decreasing Dyck paths of semilength $3$ have $10$ peaks
$UD$ in total.

All five Dyck paths of semilength $3$ are non-decreasing.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.nondecreasingDyckSubwordTotal_UD_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-total-ud-thre).

## Bivariate generating function of a subword in non-decreasing Dyck paths

For a word $w$
in the steps $U$ and $D$, let $D_n$ be the set of non-decreasing Dyck paths of semilength $n$,
and let $\#w(P)$ be the number of occurrences of $w$ as a contiguous subword of a path $P$,
overlapping occurrences counted separately. The bivariate generating function $F_w(x, y)$ is
the power series in $x$ with coefficients in $\mathbb{Z}[y]$ given by

$$F_w(x, y) = \sum_{n \ge 1} \sum_{P \in D_n} y^{\#w(P)} x^n,$$

so its constant coefficient is $0$: the empty path is not counted.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.nondecreasingDyckSubwordBivariateGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-bivariate-gf).

## Generating function of the total subword count in non-decreasing Dyck paths

For a word
$w$ in the steps $U$ and $D$, let $d_w(n)$ be the total number of occurrences of $w$ as a
contiguous subword (overlapping occurrences counted separately) over all non-decreasing Dyck
paths of semilength $n$. The univariate generating function of $w$ is the integer power series

$$D_w(x) = \sum_{n \ge 0} d_w(n) x^n.$$

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Section 1.

Formalized by `MetaMathlibExt.nondecreasingDyckSubwordTotalGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-total-gf).

## Height of the last peak

For a finite sequence $l$ of up steps $U$ and down steps $D$,
the last peak height of $l$ is undefined when $l$ has no factor $UD$. Otherwise it is the
height of the peak of the rightmost factor $UD$: the number of $U$ steps minus the number of
$D$ steps in $l$ up to and including the $U$ of that factor, taken to be $0$ when negative.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 16.

Formalized by `MetaMathlibExt.dyckLastPeakHeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-last-peak-height).

## Last peak height of UDUUDD

The last peak of the Dyck path $UDUUDD$ has height $2$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 16.

Formalized by `MetaMathlibExt.dyckLastPeakHeight_UDUUDD`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#dyck-last-peak-height-uduudd).

## Non-decreasing Dyck paths by height of the last peak

For natural numbers $n$ and $k$,
$l_{n,k}$ is the number of non-decreasing Dyck paths of semilength $n$ whose last peak (the last
factor $UD$) has height $k$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 16.

Formalized by `MetaMathlibExt.nondecreasingDyckLastPeakCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-last-peak-count).

## Non-decreasing Dyck paths of semilength four with last peak at height one

Exactly four
non-decreasing Dyck paths of semilength $4$ have their last peak at height $1$; that is,
$l_{4,1} = 4$, where $l_{n,k}$ is the number of non-decreasing Dyck paths of semilength $n$
whose last peak has height $k$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 16.

Formalized by `MetaMathlibExt.nondecreasingDyckLastPeakCount_four_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-last-peak-count-four).

## Generating functions and closed form for the subword $UD$ in non-decreasing Dyck paths

For $n \ge 0$ let $\mathcal{D}_n$ be the set of non-decreasing Dyck paths of semilength $n$, let
$\#_{UD}(P)$ be the number of occurrences of the subword $UD$ in a path $P$, and let
$d_{UD}(n) = \sum_{P \in \mathcal{D}_n} \#_{UD}(P)$. Let
$F_{UD}(x, y) = \sum_{n \ge 1} \sum_{P \in \mathcal{D}_n} y^{\#_{UD}(P)} x^n$, a power series in
$x$ with coefficients in $\mathbb{Z}[y]$, and $D_{UD}(x) = \sum_{n \ge 0} d_{UD}(n) x^n$ in
$\mathbb{Z}[[x]]$. Then $(1 - 2x + x^2 - xy) F_{UD}(x, y) = (1 - x) x y$ and
$(1 - 3x + x^2)^2 D_{UD}(x) = x (1 - x)^3$, and for every $n \ge 1$,

$$10\, d_{UD}(n) = (5n - 7) F_{2n} - (n - 5) L_{2n},$$

where $F_k$ and $L_k$ are the Fibonacci and Lucas numbers ($F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = 1$).

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 1 (`jis-2025-25.1.6-thm-1`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-ud).

## The subword $DU$ in non-decreasing Dyck paths

Let $F_{DU}(x, y)$ and $D_{DU}(x)$ be the
bivariate and univariate generating functions of the subword $DU$ in non-decreasing Dyck paths,
let $d_{DU}(n)$ be the total number of occurrences of $DU$ over all non-decreasing Dyck paths of
semilength $n$, and let $F_n$ and $L_n$ denote the Fibonacci and Lucas numbers. Then

$$(1 - 2x + x^2 - xy) F_{DU}(x, y) = (1 - x) x$$

in $\mathbb{Z}[y][[x]]$,

$$(1 - 3x + x^2)^2 D_{DU}(x) = (1 - x) x^2$$

in $\mathbb{Z}[[x]]$, and for every $n \ge 1$,

$$10 d_{DU}(n) = (5n - 2) F_{2n} - n L_{2n}.$$

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 2 (`jis-2025-25.1.6-thm-2`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_DU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-du).

## Generating functions and closed form for the subwords $UU$ and $DD$ in non-decreasing Dyck paths

**Generating functions and closed form for the subwords $UU$ and $DD$ in non-decreasing Dyck
paths.** Let $w$ be $UU$ or $DD$. For $n \ge 0$ let $\mathcal{D}_n$ be the set of non-decreasing
Dyck paths of semilength $n$, let $\#_w(P)$ be the number of occurrences of the subword $w$ in a
path $P$, and let $d_w(n) = \sum_{P \in \mathcal{D}_n} \#_w(P)$. Let
$F_w(x, y) = \sum_{n \ge 1} \sum_{P \in \mathcal{D}_n} y^{\#_w(P)} x^n$, a power series in $x$
with coefficients in $\mathbb{Z}[y]$, and $D_w(x) = \sum_{n \ge 0} d_w(n) x^n$ in
$\mathbb{Z}[[x]]$. Then $(1 - x - 2xy + x^2 y^2) F_w(x, y) = x (1 - xy)$ and
$(1 - 3x + x^2)^2 D_w(x) = x^2 (1 - x + x^2)$, and for every $n \ge 1$,

$$10\, d_w(n) = (7 - 10n) F_{2n} + (6n - 5) L_{2n},$$

where $F_k$ and $L_k$ are the Fibonacci and Lucas numbers ($F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = 1$).

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 3 (`jis-2025-25.1.6-thm-3`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UU_DD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-uu-dd).

## Subword $UUU$ in non-decreasing Dyck paths

Let $F_{UUU}(x, y) \in \mathbb{Z}[y][[x]]$ be
the bivariate generating function with constant term $0$ in which, for $n \ge 1$, the coefficient
of $x^n$ is the sum of $y^{k(P)}$ over the non-decreasing Dyck paths $P$ of semilength $n$, where
$k(P)$ is the number of occurrences of the subword $UUU$ in $P$ (overlapping occurrences counted
separately). Let $d_{UUU}(n)$ be the total number of occurrences of $UUU$ over all non-decreasing
Dyck paths of semilength $n$, let $D_{UUU}(x) = \sum_{n \ge 0} d_{UUU}(n) x^n \in \mathbb{Z}[[x]]$,
and let $F_n$ and $L_n$ denote the Fibonacci and Lucas numbers. Then
$(1 - x(2 + y) + x^2 y) F_{UUU}(x, y) = (1 - xy) x$, $(1 - 3x + x^2)^2 D_{UUU}(x) = x^3$, and
for every $n \ge 1$, $10\, d_{UUU}(n) = -(5n + 4) F_{2n} + 3n L_{2n}$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 4 (`jis-2025-25.1.6-thm-4`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UUU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-uuu).

## Generating functions and closed form for the subword $UDU$ in non-decreasing Dyck paths

For $n \ge 0$ let $\mathcal{D}_n$ be the set of non-decreasing Dyck paths of semilength $n$, let
$\#_{UDU}(P)$ be the number of occurrences of the subword $UDU$ in a path $P$, and let
$d_{UDU}(n) = \sum_{P \in \mathcal{D}_n} \#_{UDU}(P)$. Let
$F_{UDU}(x, y) = \sum_{n \ge 1} \sum_{P \in \mathcal{D}_n} y^{\#_{UDU}(P)} x^n$, a power series
in $x$ with coefficients in $\mathbb{Z}[y]$, and $D_{UDU}(x) = \sum_{n \ge 0} d_{UDU}(n) x^n$ in
$\mathbb{Z}[[x]]$. Then $(1 - x(2 + y) + x^2 y) F_{UDU}(x, y) = (1 - x) x$ and
$(1 - 3x + x^2)^2 D_{UDU}(x) = x^2 (1 - x)^2$, and for every $n \ge 1$,

$$10\, d_{UDU}(n) = (11 - 5n) F_{2n} + (3n - 5) L_{2n},$$

where $F_k$ and $L_k$ are the Fibonacci and Lucas numbers ($F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = 1$).

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 5 (`jis-2025-25.1.6-thm-5`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UDU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-udu).

## Generating functions and closed form for the subword $UDD$ in non-decreasing Dyck paths

For $n \ge 0$ let $\mathcal{D}_n$ be the set of non-decreasing Dyck paths of semilength $n$, let
$\#_{UDD}(P)$ be the number of occurrences of the subword $UDD$ in a path $P$, and let
$d_{UDD}(n) = \sum_{P \in \mathcal{D}_n} \#_{UDD}(P)$. Let
$F_{UDD}(x, y) = \sum_{n \ge 1} \sum_{P \in \mathcal{D}_n} y^{\#_{UDD}(P)} x^n$, a power series
in $x$ with coefficients in $\mathbb{Z}[y]$, and $D_{UDD}(x) = \sum_{n \ge 0} d_{UDD}(n) x^n$ in
$\mathbb{Z}[[x]]$. Then

$$(1 - 3x + x^2 (2 - y)) (1 - 2x + x^2 (1 - y)) F_{UDD}(x, y) = (1 - x)(1 - 2x)(1 - x(1 - y)) x$$

and

$$(1 - 2x)(1 - 3x + x^2)^2 D_{UDD}(x) = (1 - x)(1 - 3x + 2x^2 - x^3) x^2,$$

and for every $n \ge 2$,

$$5\, d_{UDD}(n) = (5n - 9) F_{2n} + (5 - 2n) L_{2n} - 5 \cdot 2^{n-2},$$

where $F_k$ and $L_k$ are the Fibonacci and Lucas numbers ($F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = 1$).

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 6 (`jis-2025-25.1.6-thm-6`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UDD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-udd).

## The subword $DUU$ in non-decreasing Dyck paths

Let $F_{DUU}(x, y)$ and $D_{DUU}(x)$ be
the bivariate and univariate generating functions of the subword $DUU$ in non-decreasing Dyck
paths, let $d_{DUU}(n)$ be the total number of occurrences of $DUU$ over all non-decreasing Dyck
paths of semilength $n$, and let $F_n$ and $L_n$ denote the Fibonacci and Lucas numbers. Then

$$(1 - 3x + x^2(3 - 2y) - x^3(1 - y)) F_{DUU}(x, y) = x - x^2 + x^3(1 - y)$$

in $\mathbb{Z}[y][[x]]$,

$$(1 - 3x + x^2)^2 D_{DUU}(x) = x^3$$

in $\mathbb{Z}[[x]]$, and for every $n \ge 3$,

$$10 d_{DUU}(n) = -(5n + 4) F_{2n} + 3n L_{2n}.$$

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 7 (`jis-2025-25.1.6-thm-7`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_DUU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-duu).

## The subword $DUD$ in non-decreasing Dyck paths

Let $F_{DUD}(x, y)$ and $D_{DUD}(x)$ be
the bivariate and univariate generating functions of the subword $DUD$ in non-decreasing Dyck
paths, let $d_{DUD}(n)$ be the total number of occurrences of $DUD$ over all non-decreasing Dyck
paths of semilength $n$, and let $F_n$ and $L_n$ denote the Fibonacci and Lucas numbers. Then

$$(1 - x^2(1 - 2y) + x^3(1 - y) - x(2 + y)) F_{DUD}(x, y) = x (1 - x - x^2(1 - y))$$

in $\mathbb{Z}[y][[x]]$,

$$(1 - 3x + x^2)^2 D_{DUD}(x) = x^2 - 2x^3$$

in $\mathbb{Z}[[x]]$, and for every $n \ge 3$,

$$5 d_{DUD}(n) = (5n + 1) F_{2n} - 2n L_{2n}.$$

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 8 (`jis-2025-25.1.6-thm-8`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_DUD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-dud).

## The subword $DDU$ in non-decreasing Dyck paths

Let $F_{DDU}(x, y)$ and $D_{DDU}(x)$ be
the bivariate and univariate generating functions of the subword $DDU$ in non-decreasing Dyck
paths, let $d_{DDU}(n)$ be the total number of occurrences of $DDU$ over all non-decreasing Dyck
paths of semilength $n$, and let $F_n$ and $L_n$ denote the Fibonacci and Lucas numbers. Then

$$(1 - 3x + x^2(2 - y)) F_{DDU}(x, y) = (1 - x) x$$

in $\mathbb{Z}[y][[x]]$,

$$(1 - 3x + x^2)^2 D_{DDU}(x) = (1 - x) x^3$$

in $\mathbb{Z}[[x]]$, and for every $n \ge 3$,

$$10 d_{DDU}(n) = (10n - 13) F_{2n} + (-4n + 5) L_{2n}.$$

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 9 (`jis-2025-25.1.6-thm-9`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_DDU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-ddu).

## The subword $DDD$ in non-decreasing Dyck paths

Let $F_{DDD}(x, y)$ and $D_{DDD}(x)$ be
the bivariate and univariate generating functions of the subword $DDD$ in non-decreasing Dyck
paths, let $d_{DDD}(n)$ be the total number of occurrences of $DDD$ over all non-decreasing Dyck
paths of semilength $n$, and let $F_n$ and $L_n$ denote the Fibonacci and Lucas numbers. Then

$$(1 - x(1 + y) - x^2(1 - y)) (1 - x(1 + 2y) - x^2(1 - y - y^2)) F_{DDD}(x, y) =
x (1 - xy) (1 - 2xy - x^2(1 - y^2))$$

in $\mathbb{Z}[y][[x]]$,

$$(1 - 2x) (1 - 3x + x^2)^2 D_{DDD}(x) = x^3 (1 - 2x + x^2 - x^3)$$

in $\mathbb{Z}[[x]]$, and for every $n \ge 3$,

$$4 d_{DDD}(n) = (-8n + 10) F_{2n} + (4n - 6) L_{2n} + 2^n.$$

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 10 (`jis-2025-25.1.6-thm-10`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_DDD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-ddd).

## Generating functions and closed form for the subword $UUD$ in non-decreasing Dyck paths

For $n \ge 0$ let $\mathcal{D}_n$ be the set of non-decreasing Dyck paths of semilength $n$, let
$\#_{UUD}(P)$ be the number of occurrences of the subword $UUD$ in a path $P$, and let
$d_{UUD}(n) = \sum_{P \in \mathcal{D}_n} \#_{UUD}(P)$. Let
$F_{UUD}(x, y) = \sum_{n \ge 1} \sum_{P \in \mathcal{D}_n} y^{\#_{UUD}(P)} x^n$, a power series
in $x$ with coefficients in $\mathbb{Z}[y]$, and $D_{UUD}(x) = \sum_{n \ge 0} d_{UUD}(n) x^n$ in
$\mathbb{Z}[[x]]$. Then

$$(1 - 3x + x^2 (3 - 2y) - x^3 (1 - y)) F_{UUD}(x, y) = (1 - x) x (1 - x(1 - y))$$

and $(1 - 3x + x^2)^2 D_{UUD}(x) = (1 - x)^2 x^2$, and for every $n \ge 3$,

$$10\, d_{UUD}(n) = (11 - 5n) F_{2n} + (3n - 5) L_{2n},$$

where $F_k$ and $L_k$ are the Fibonacci and Lucas numbers ($F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = 1$).

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 11 (`jis-2025-25.1.6-thm-11`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UUD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-uud).

## Subword $UUUD$ in non-decreasing Dyck paths

Let $F_{UUUD}(x, y) \in \mathbb{Z}[y][[x]]$ be
the bivariate generating function with constant term $0$ in which, for $n \ge 1$, the coefficient
of $x^n$ is the sum of $y^{k(P)}$ over the non-decreasing Dyck paths $P$ of semilength $n$, where
$k(P)$ is the number of occurrences of the subword $UUUD$ in $P$. Let $d_{UUUD}(n)$ be the total
number of occurrences of $UUUD$ over all non-decreasing Dyck paths of semilength $n$, let
$D_{UUUD}(x) = \sum_{n \ge 0} d_{UUUD}(n) x^n \in \mathbb{Z}[[x]]$, and let $F_n$ and $L_n$ denote
the Fibonacci and Lucas numbers. Then
$(1 - 3x + x^2 + (3 - 3y) x^3 - 2(1 - y) x^4) F_{UUUD}(x, y) = (1 - x)(x + x^3 (y - 1))$,
$(1 + x(x - 3))^2 D_{UUUD}(x) = (x - 1)^2 x^3 (x + 1)$, and for every $n \ge 3$,
$d_{UUUD}(n) = n F_{2n-5} - L_{2n-6}$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 12 (`jis-2025-25.1.6-thm-12`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_UUUD` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-uuud).

## Recurrence for the subword $U^m$ in non-decreasing Dyck paths

Let $m \ge 1$. Let
$d_w(n)$ be the total number of occurrences of the subword $w$ over all non-decreasing Dyck paths
of semilength $n$, and let $F_k$ be the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$). Then for every
$n > m$,

$$d_{U^m}(n) = 3\,d_{U^m}(n-1) - d_{U^m}(n-2) + F_{2(n-m)} + F_{2(n-2)} -
\sum_{k=1}^{m-2} k\,F_{2(n-k-2)}$$

(the sum is empty when $m \le 2$); moreover $d_{U^m}(n) = 0$ for every $n < m$, and
$d_{U^m}(m) = 1$.

The source writes $n \le m$ for the vanishing case, which contradicts $d_{U^m}(m) = 1$; the
vanishing case is stated for $n < m$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 13 (`jis-2025-25.1.6-thm-13`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_U_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-u-pow).

## Recurrence for the subword $U^mD$ in non-decreasing Dyck paths

Let $m \ge 1$. Let
$d_w(n)$ be the total number of occurrences of the subword $w$ over all non-decreasing Dyck paths
of semilength $n$, and let $F_k$ be the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$). Then for every
$n \ge m + 2$,

$$d_{U^mD}(n) = 3\,d_{U^mD}(n-1) - d_{U^mD}(n-2) + F_{2(n-m)-3} + m\,F_{2(n-m-1)};$$

moreover $d_{U^mD}(n) = 0$ for every $n < m$, $d_{U^mD}(m) = 1$, and $d_{U^mD}(m+1) = m + 2$.

The source states the recurrence for $n \ge m$, where $n = m$ and $n = m + 1$ give negative
Fibonacci indices; those two values are the separately stated initial values, and the recurrence
is stated for $n \ge m + 2$.

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 15 (`jis-2025-25.1.6-thm-15`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_U_pow_D` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-u-pow-d).

## Recurrence for the subword $UD^m$ in non-decreasing Dyck paths

Let $m \ge 1$. Let
$d_w(n)$ be the total number of occurrences of the subword $w$ over all non-decreasing Dyck paths
of semilength $n$, let $l_{n,k}$ be the number of non-decreasing Dyck paths of semilength $n$
whose last peak has height $k$, and let $F_k$ be the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$).
Then for every $n$ with $n > m$ and $n \ge 3$,

$$d_{UD^m}(n) = 3\,d_{UD^m}(n-1) - d_{UD^m}(n-2) + F_{2(n-m)-1} + l_{n-1,m-1} - l_{n-2,m-1};$$

moreover $d_{UD^m}(n) = 0$ for every $n < m$, and $d_{UD^m}(m) = 1$.

The source states the recurrence for $n \ge m$; $n = m$ is the separately stated initial value,
and the added condition $n \ge 3$ excludes only $(m, n) = (1, 2)$, where $d_{UD}(2) = 3$ but the
right side is $3 \cdot 1 - 0 + F_1 + l_{1,0} - l_{0,0} = 4$ (the empty path has no peak).

## Sources

- Flórez, Junes, Montoya, and Ramírez, *Counting Subwords in Non-Decreasing Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.1.6, Theorem 16 (`jis-2025-25.1.6-thm-16`).

Stated but not proved: `MetaMathlibExt.nondecreasingDyck_subword_U_D_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/NondecreasingDyckSubwordsWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html#nondecreasing-dyck-subword-u-d-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subwords in non-decreasing Dyck paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/subwords-in-non-decreasing-dyck-paths)
