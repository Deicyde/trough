---
declaration: section
origin: cited
lean: MetaMathlibExt.decreasingParts, MetaMathlibExt.litCellsIncreasing, MetaMathlibExt.litNodesIncreasing, MetaMathlibExt.litCellsDecreasing, MetaMathlibExt.triangularQBinomial, MetaMathlibExt.trianglePartitionSeries, MetaMathlibExt.litCellsIncreasing_indiscrete, MetaMathlibExt.litNodesIncreasing_indiscrete
statement: formalized
---

# Lit cells in integer partitions

18 results, 11 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html).

## Parts of a partition in decreasing order

For a partition $p$ of $n$ with $\ell$ parts,
this is the list $x_1 \ge x_2 \ge \cdots \ge x_\ell$ of the parts of $p$, each repeated according
to its multiplicity, sorted in weakly decreasing order.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 1 (weakly decreasing bargraphs).

Formalized by `MetaMathlibExt.decreasingParts`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#decreasing-parts).

## Lit cells of a weakly increasing bargraph

For a partition $p$ of $n$, the number of lit
cells of $p$, drawn as a weakly increasing bargraph, is defined as the largest part of $p$ plus the
number of parts of $p$ minus the number of distinct parts of $p$ (the largest part of the empty
partition is $0$).

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 3, proof of Proposition 1.

Formalized by `MetaMathlibExt.litCellsIncreasing`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-increasing).

## Lit nodes of a partition

The number of lit nodes of a partition $p$, drawn as a weakly
increasing Ferrers diagram of nodes, is defined as the largest part of $p$ plus the number of
parts of $p$ minus one; for the empty partition it is $0$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 3, proof of Proposition 2.

Formalized by `MetaMathlibExt.litNodesIncreasing`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-nodes-increasing).

## Lit cells of a weakly decreasing bargraph

Let $p$ be a partition of $n$ with $\ell$
parts $x_1 \ge x_2 \ge \cdots \ge x_\ell$. The number of lit cells of $p$, drawn as a weakly
decreasing bargraph, is defined as $\max_{1 \le i \le \ell} (x_i + i - 1)$, and as $0$ when $p$
has no parts. It is the largest part of the image of $p$ under Prodinger's bijection
$x_i \mapsto x_i + i - 1$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 5.

Formalized by `MetaMathlibExt.litCellsDecreasing`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-decreasing).

## Triangular $q$-binomial coefficient

For natural numbers $r$ and $s$, the triangular
$q$-binomial coefficient $t[r, s] \in \mathbb{Z}[[q]]$ is the power series whose coefficient of
$q^n$ is the number of partitions of $n$ with exactly $s$ parts $x_1 \ge \dots \ge x_s$ that fit
in the staircase with column heights $r, r - 1, \dots, r - s + 1$, that is, with
$x_i + (i - 1) \le r$ for $1 \le i \le s$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 4.

Formalized by `MetaMathlibExt.triangularQBinomial`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#triangular-qbinomial).

## Triangle partition series

For a natural number $r$, the triangle partition series is the
power series $T_q(r) = \sum_{s=0}^{r} t[r, s] \in \mathbb{Z}[[q]]$, where $t[r, s]$ is the
triangular $q$-binomial coefficient. It is the generating function of partitions contained in the
triangle with column heights $r, r - 1, \dots, 1$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Definition 1.

Formalized by `MetaMathlibExt.trianglePartitionSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#triangle-partition-series).

## Lit cells of a one-part increasing bargraph

For every natural number $n \ge 1$, the
partition $(n)$ of $n$ with a single part has $n$ lit cells as a weakly increasing bargraph.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 3 (definition of lit cells).

Formalized by `MetaMathlibExt.litCellsIncreasing_indiscrete`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-increasing-indiscrete).

## Lit nodes of a one-part partition

For every natural number $n \ge 1$, the one-part
partition $(n)$ of $n$ has exactly $n$ lit nodes.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 3 (definition of lit nodes).

Formalized by `MetaMathlibExt.litNodesIncreasing_indiscrete`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-nodes-increasing-indiscrete).

## Lit cells of a one-part decreasing bargraph

For every natural number $n \ge 1$, the
partition $(n)$ of $n$ with a single part has $n$ lit cells as a weakly decreasing bargraph.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 5 (lit cells of decreasing partitions).

Formalized by `MetaMathlibExt.litCellsDecreasing_indiscrete`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-decreasing-indiscrete).

## Triangular $q$-binomial coefficients with no parts

For every natural number $r$, the
triangular $q$-binomial coefficient satisfies $t[r, 0] = 1$: only the empty partition has no
parts.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Section 4, initial conditions (10).

Formalized by `MetaMathlibExt.triangularQBinomial_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#triangular-qbinomial-zero-right).

## Triangle partition series at zero

The triangle partition series $T_q(r)$ at $r = 0$
equals $1$, that is, $T_q(0) = 1$ in $\mathbb{Z}[[q]]$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Definition 1.

Formalized by `MetaMathlibExt.trianglePartitionSeries_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#triangle-partition-series-zero).

## Generating function for lit cells of weakly increasing bargraphs

Let
$P(q) = \sum_{n \ge 0} p(n) q^n$ be the partition generating function, and let
$L(q) \in \mathbb{Z}[[q]]$ be the power series whose coefficient of $q^n$ is the total number of
lit cells over all partitions of $n$ drawn as weakly increasing bargraphs. Then

$$L(q) = 2P(q) \sum_{i \ge 1} \frac{q^i}{1 - q^i} - P(q) \frac{q}{1 - q}$$

and

$$L(q) = P(q) \sum_{i \ge 1} \frac{q^i (1 + q^i)}{1 - q^i},$$

where the sums converge coefficientwise.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Proposition 1, eq. (5).

Stated but not proved: `MetaMathlibExt.litCellsIncreasing_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-increasing-generating-function).

## Generating function for lit nodes of weakly increasing diagrams

Let
$P(q) = \sum_{n \ge 0} p(n) q^n$ be the partition generating function, and let
$N(q) \in \mathbb{Z}[[q]]$ be the power series whose coefficient of $q^n$ is the total number of
lit nodes over all partitions of $n$ drawn as weakly increasing Ferrers diagrams of nodes. Then

$$N(q) = 1 + P(q) \Bigl(\sum_{i \ge 1} \frac{2q^i}{1 - q^i} - 1\Bigr),$$

where the sum converges coefficientwise.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Proposition 2, eq. (7).

Stated but not proved: `MetaMathlibExt.litNodesIncreasing_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-nodes-increasing-generating-function).

## Recursion for triangular $q$-binomial coefficients

The triangular $q$-binomial
coefficients $t[r, s] \in \mathbb{Z}[[q]]$ satisfy the recursion
$t[r, s] = q^s \sum_{i=0}^{s} t[r - 1, i]$ for all natural numbers $r \ge 1$ and $s \le r$,
together with the initial conditions $t[1, 1] = q$, $t[2, 1] = q(1 + q)$, $t[r, 0] = 1$ for
every $r$, and $t[r, s] = 0$ whenever $r < s$.

The recursion is stated for $s \le r$ only: for $s > r$ the left side is $0$, while the right
side is $q^s \sum_{i=0}^{r-1} t[r - 1, i] \ne 0$; for example $t[1, 2] = 0$ but
$q^2 (t[0, 0] + t[0, 1] + t[0, 2]) = q^2$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Proposition 3, eqs. (9), (10).

Stated but not proved: `MetaMathlibExt.triangularQBinomial_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#triangular-qbinomial-recursion).

## Triangular $q$-binomial coefficients via Gaussian binomials

For natural numbers $r$ and
$s$ with $1 \le r$ and $s \le r$, the triangular $q$-binomial coefficient $t[r, s]$ satisfies

$$
t[r, s] = q^s \binom{r + s - 1}{s}_q - q^{s+1} \sum_{i=2}^{s} t[i - 1, i - 1] \,
q^{i(r - i)} \binom{r + 1 + s - 2i}{s - i}_q
$$

in $\mathbb{Z}[[q]]$, where $\binom{M}{k}_q$ denotes the Gaussian binomial coefficient.

In the range $s \le r$ every exponent and binomial index above is a natural number; for $s > r$
one has $t[r, s] = 0$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Proposition 4, eq. (12).

Stated but not proved: `MetaMathlibExt.triangularQBinomial_eq_gaussBinom_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#triangular-qbinomial-eq-gauss-binom-sub).

## Lit cells of weakly decreasing partitions with few parts

Let $k$ and $s$ be natural
numbers with $s \le k$. Write $\binom{M}{m}_q$ for the Gaussian binomial coefficient, and $t[s, i]$
for the triangular $q$-binomial coefficient: the generating function of partitions with exactly
$i$ parts $x_1 \ge \cdots \ge x_i$ such that $x_j + j - 1 \le s$ for $1 \le j \le i$. Let
$\mathrm{lit}[k, s] \in \mathbb{Z}[[q]]$ be the power series whose coefficient of $q^n$ is the
number of partitions of $n$ with at most $s + 1$ parts and at most $k$ lit cells as weakly
decreasing bargraphs. Then

$$\mathrm{lit}[k, s] = \sum_{i=0}^{s} t[s, i] \, q^{i(k-s)} \binom{k + 1 - i}{k - s}_q.$$

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Proposition 5, eq. (13).

Stated but not proved: `MetaMathlibExt.litCellsDecreasing_le_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-decreasing-le-generating-funct).

## Generating function for lit cells of weakly decreasing bargraphs

Let
$P(q) = \sum_{n \ge 0} p(n) q^n$ be the partition generating function, for $k \ge 0$ let $T_q(k)$
be the generating function of partitions contained in the triangle with column heights
$k, k - 1, \ldots, 1$ (so $T_q(0) = 1$), and let $L(q) \in \mathbb{Z}[[q]]$ be the power series
whose coefficient of $q^n$ is the total number of lit cells over all partitions of $n$ drawn as
weakly decreasing bargraphs. Then

$$L(q) = \sum_{k \ge 0} \bigl(P(q) - T_q(k)\bigr),$$

where the sum converges coefficientwise.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Theorem 1, eq. (16).

Stated but not proved: `MetaMathlibExt.litCellsDecreasing_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-decreasing-generating-function).

## Lit cells when only the first column is lit

For a partition $p$ of $n$ with $\ell \ge 1$
parts $x_1 \ge x_2 \ge \cdots \ge x_\ell$, say that only the first column of its weakly
decreasing bargraph is lit when the number of lit cells of $p$ equals its largest part $x_1$,
that is, when $x_i + i - 1 \le x_1$ for $1 \le i \le \ell$. Let $F(q) \in \mathbb{Z}[[q]]$ be
the power series whose coefficient of $q^n$ is the sum of $x_1$ over the partitions of $n$ in
which only the first column is lit and $x_1 \ge 2$. For $r \ge 0$ let $T_q(r)$ be the
generating function of partitions contained in the triangle with column heights
$r, r - 1, \ldots, 1$. Then

$$F(q) = \sum_{r \ge 1} (r + 1) q^{r+1} T_q(r),$$

where the sum converges coefficientwise.

The condition $x_1 \ge 2$ is the range $r \ge 1$ of the paper's
$T(u, q) = \sum_{r \ge 1} u^{r+1} q^{r+1} T_q(r)$; among the partitions in which only the first
column is lit it excludes only $(1)$.

## Sources

- Aubrey Blecher, Arnold Knopfmacher, and Michael Mays, *Casting Light on Integer Partitions*, INTEGERS 24 (2024), Article A56, Proposition 6.

Stated but not proved: `MetaMathlibExt.litCellsDecreasing_firstColumn_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/Partition/LitCellsPartitionsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html#lit-cells-decreasing-first-column-genera).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lit cells in integer partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/lit-cells-in-integer-partitions)
