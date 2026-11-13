---
declaration: section
origin: cited
lean: MetaMathlibExt.IsArithmeticalStructure, MetaMathlibExt.isArithmeticalStructure_top_fin_two, MetaMathlibExt.coconutTree, MetaMathlibExt.coconutTree_adj_inl_inl, MetaMathlibExt.coconutTree_adj_inl_inr, MetaMathlibExt.coconutTree_not_adj_inr_inr, MetaMathlibExt.IsSmoothCoconut, MetaMathlibExt.IsSmoothCoconut.two_le_leaf
statement: formalized
---

# Arithmetical structures on graphs

44 results, 24 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html).

## Arithmetical structure

An arithmetical structure on a graph $G$ with vertex set $V$ is a
pair of labelings $d, r : V \to \mathbb{N}$ such that $d(v) > 0$ and $r(v) > 0$ for every vertex
$v$, $d(v)\, r(v) = \sum_{w \sim v} r(w)$ for every vertex $v$, where the sum runs over the
neighbours $w$ of $v$, and the only natural number dividing every $r(v)$ is $1$. For a finite graph
with adjacency matrix $A$ the middle condition reads $(\operatorname{diag}(d) - A)\, r = 0$.

The neighbour sum is taken to be $0$ when $v$ has infinitely many neighbours, so no arithmetical
structure exists on a graph with a vertex of infinite degree.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.1 (arXiv numbering).

Formalized by `MetaMathlibExt.IsArithmeticalStructure`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#is-arithmetical-structure).

## The all-ones structure on a single edge

On the graph with two vertices joined by an edge,
the labelings $d = (1, 1)$ and $r = (1, 1)$ form an arithmetical structure.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.1 (arXiv numbering).

Formalized by `MetaMathlibExt.isArithmeticalStructure_top_fin_two`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#is-arithmetical-structure-top-fin-two).

## Coconut tree

For natural numbers $p$ and $s$, the coconut tree $\mathrm{CT}(p, s)$ is the
graph whose vertices are the path vertices $v_1, \dots, v_p$ and the leaves
$v_{\ell_1}, \dots, v_{\ell_s}$, in which $v_i$ and $v_{i+1}$ are adjacent for $1 \le i < p$, every
leaf is adjacent to $v_p$, and there are no other edges. For $p = 0$ it consists of $s$ isolated
vertices.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.2 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutTree`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-tree).

## Adjacent path vertices of a coconut tree

Let the coconut tree $CT(p, s)$ have path
vertices $v_1, \dots, v_p$. Two path vertices $v_a$ and $v_b$ are adjacent if and only if
$|a - b| = 1$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.2 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutTree_adj_inl_inl`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-tree-adj-inl-inl).

## Adjacency of leaves and path vertices in a coconut tree

Let the coconut tree
$CT(p, s)$ have path vertices $v_1, \dots, v_p$, with central vertex $v_p$. A leaf of $CT(p, s)$
is adjacent to a path vertex $v_k$ if and only if $k = p$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.2 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutTree_adj_inl_inr`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-tree-adj-inl-inr).

## Leaves of a coconut tree are pairwise nonadjacent

No leaf of the coconut tree $CT(p, s)$
is adjacent to a leaf.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.2 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutTree_not_adj_inr_inr`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-tree-not-adj-inr-inr).

## Smooth arithmetical structure on a coconut tree

Let $CT(p, s)$ be the coconut tree with
path vertices $v_1, \dots, v_p$ and leaves $\ell_1, \dots, \ell_s$ adjacent to $v_p$. An
arithmetical structure $(d, r)$ on $CT(p, s)$ is smooth if $d(v_i) \ge 2$ for $1 \le i \le p - 1$
and $d(\ell_j) \ge 2$ for $1 \le j \le s$; there is no condition on $d(v_p)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.3 (arXiv numbering).

Formalized by `MetaMathlibExt.IsSmoothCoconut`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#is-smooth-coconut).

## Leaves of a smooth coconut structure have label at least 2

If $(d, r)$ is a smooth
arithmetical structure on the coconut tree $\mathrm{CT}(p, s)$, then $d_{\ell_j} \ge 2$ for every
leaf $\ell_j$, $1 \le j \le s$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 2.3 (arXiv numbering).

Formalized by `MetaMathlibExt.IsSmoothCoconut.two_le_leaf`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#two-le-leaf).

## Ballot numbers

For natural numbers $n$ and $k$, the ballot number $B(n, k)$ is the
integer part of $\max(n + 1 - k, 0) \binom{n+k}{n} / (n + 1)$. For $k \le n + 1$ the division
is exact, so $B(n, k) = \frac{n - k + 1}{n + 1} \binom{n+k}{n}$ (OEIS A009766), and
$B(n, k) = 0$ for $k > n + 1$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Section 1.

Formalized by `MetaMathlibExt.ballotNumber`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ballot-number).

## Ballot numbers with second index zero

For every natural number $n$, the ballot number
$B(n, 0)$ equals $1$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Section 1.

Formalized by `MetaMathlibExt.ballotNumber_zero_right`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ballot-number-zero-right).

## Diagonal ballot numbers are Catalan numbers

For every natural number $n$, the ballot
number $B(n, n)$ equals the $n$-th Catalan number $C_n$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Section 1.

Formalized by `MetaMathlibExt.ballotNumber_self`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ballot-number-self).

## Terms of the coconut tree count

For natural numbers $x$ and $y$, the term $A(x, y)$ is
defined by $A(x, 0) = C_{x-1}$, $A(x, 1) = C_{x-1} - C_{x-2}$ and, for $y \ge 2$,

$$A(x, y) = \sum_{i=y+1}^{x} B(x - y - 1, x - i) \, |\mathrm{SArith}(CT(i - y, y))|,$$

where $C_n$ is the $n$-th Catalan number (a negative index is read as $0$), $B$ is the ballot
number, and $|\mathrm{SArith}(CT(m, y))|$ is the number of smooth arithmetical structures
$(d, r)$ on the coconut tree $CT(m, y)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Theorem 1.

Formalized by `MetaMathlibExt.coconutCountTerm`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-count-term).

## The coconut count term with second argument zero

For every natural number $x$, the
term $A(x, 0)$ of the coconut tree count equals the Catalan number $C_{x-1}$, read as $C_0$
when $x = 0$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Theorem 1.

Formalized by `MetaMathlibExt.coconutCountTerm_zero`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-count-term-zero).

## Euclidean chain function

For natural numbers $x_1$ and $x_2$, the Euclidean chain
$x_1, x_2, x_3, \dots$ is given by $x_{i+1} = (-x_{i-1}) \bmod x_i$ (the least nonnegative
residue) while $x_i \ne 0$, and by $x_{i+1} = 0$ once $x_i = 0$. The Euclidean chain function is
defined by the recursion $F(x, 0) = 1$ and $F(x, y) = 1 + F(y, (-x) \bmod y)$ for $y \ne 0$. For
$x_1 > 0$, $F(x_1, x_2)$ is the number of positive terms of the Euclidean chain.

For $x_1 = 0$ the recursion also counts the first term $0$: $F(0, 0) = 1$ and $F(0, 1) = 2$,
although the chains $0, 0$ and $0, 1, 0$ have $0$ and $1$ positive terms.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 4.12 (arXiv numbering).

Formalized by `MetaMathlibExt.euclideanChainLength`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length).

## Euclidean chain function with second argument zero

For every natural number $x$, the
Euclidean chain function $F$ satisfies $F(x, 0) = 1$.

For $x = 0$ this is the value given by the recursive definition of $F$, not a count of positive
terms.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 4.12 (arXiv numbering).

Formalized by `MetaMathlibExt.euclideanChainLength_zero`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length-zero).

## Recursion for the Euclidean chain function

For natural numbers $x$ and $y$ with $y \ne 0$,
the Euclidean chain function $F$ satisfies $F(x, y) = 1 + F(y, (-x) \bmod y)$, where
$(-x) \bmod y$ is the least nonnegative residue of $-x$ modulo $y$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 4.12 (arXiv numbering).

Formalized by `MetaMathlibExt.euclideanChainLength_of_ne_zero`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length-of-ne-zero).

## Euclidean chain function of 13 and 60

The Euclidean chain function $F$ satisfies
$F(13, 60) = 8$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Example 4.13 (arXiv numbering).

Formalized by `MetaMathlibExt.euclideanChainLength_thirteen_sixty`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length-thirteen-sixty).

## Monotonicity criteria for arithmetical structures on coconut trees

Let $(d, r)$ be an
arithmetical structure on the coconut tree $CT(p, s)$ with path vertices $v_1, \dots, v_p$, and
write $d_k = d(v_k)$ and $r_k = r(v_k)$. The following are equivalent: (1) $d_k \ge 2$ for
$1 \le k \le p - 1$; (2) $0 < r_2 - r_1 \le r_3 - r_2 \le \cdots \le r_p - r_{p-1}$; (3)
$r_1 < r_2 < \cdots < r_p$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Lemma 1.

Stated but not proved: `MetaMathlibExt.IsArithmeticalStructure.coconut_tfae` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-tfae).

## Characterization of smooth coconut structures

Let $p \ge 1$ and let $(d, r)$ be an
arithmetical structure on the coconut tree $CT(p, s)$ with path vertices $v_1, \dots, v_p$ and
leaves $\ell_1, \dots, \ell_s$ adjacent to $v_p$. Then $(d, r)$ is smooth if and only if
$r(\ell_j) < r(v_p)$ for every $j$ and $r(v_1) < r(v_2) < \dots < r(v_p)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Lemma 2.

Stated but not proved: `MetaMathlibExt.IsArithmeticalStructure.isSmoothCoconut_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#is-smooth-coconut-iff).

## The leaf labels of a smooth arithmetical structure on a coconut tree are coprime

Let
$(d, r)$ be a smooth arithmetical structure on the coconut tree $\mathrm{CT}(p, s)$ with leaves
$v_{\ell_1}, \dots, v_{\ell_s}$. If a natural number $g$ divides $r(v_{\ell_j})$ for every
$j = 1, \dots, s$, then $g = 1$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Lemma 3.

Stated but not proved: `MetaMathlibExt.IsSmoothCoconut.eq_one_of_dvd_leaves` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#eq-one-of-dvd-leaves).

## Arithmetical structures on a one-leaf coconut tree with a non-smoothable leaf

For every
integer $p \ge 1$, the number of arithmetical structures $(d, r)$ on the coconut tree
$\mathrm{CT}(p, 1)$, which is the path on $p + 1$ vertices, whose leaf $\ell_1$ has
$d_{\ell_1} \ne 1$ (so that the leaf cannot be smoothed) is $C_p - C_{p-1}$, where $C_n$
denotes the $n$-th Catalan number.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 5.

Stated but not proved: `MetaMathlibExt.ncard_arithmeticalStructure_coconutTree_one_leaf_ne_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ncard-arithmetical-structure-coconut-tre).

## Number of arithmetical structures on coconut trees

For $p \ge 1$ and $s \ge 2$, the number
of arithmetical structures on the coconut tree $CT(p, s)$ is

$$\sum_{j=0}^{s} \binom{s}{j} A(p + s - j, s - j),$$

where $A(x, y)$ is the coconut count term.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Theorem 1.

Stated but not proved: `MetaMathlibExt.ncard_arithmeticalStructure_coconutTree` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ncard-arithmetical-structure-coconut-tre-2).

## Number of arithmetical structures on coconut trees with two leaves

For $p \ge 2$, the
number of arithmetical structures on the coconut tree $CT(p, 2)$ is

$$2 C_p - C_{p-1} + \sum_{i=3}^{p+2} B(p - 1, p + 2 - i)\, N(i - 2),$$

where $C_n$ is the $n$-th Catalan number, $B(n, k)$ is the ballot number and $N(q)$ is the number
of smooth arithmetical structures on $CT(q, 2)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 2.

Stated but not proved: `MetaMathlibExt.ncard_arithmeticalStructure_coconutTree_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ncard-arithmetical-structure-coconut-tre-3).

## Number of arithmetical structures on stars

For $s \ge 2$, the number of arithmetical
structures on the star $CT(1, s)$, a centre joined to $s$ leaves, is

$$1 + \sum_{j=0}^{s-2} \binom{s}{j} N(s - j),$$

where $N(t)$ is the number of smooth arithmetical structures on the star $CT(1, t)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 3.

Stated but not proved: `MetaMathlibExt.ncard_arithmeticalStructure_coconutTree_star` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ncard-arithmetical-structure-coconut-tre-4).

## Euclidean chain function under adding multiples

For natural numbers $x \ge 1$, $y$ and
$k$, the Euclidean chain function $F$ satisfies $F(x + k y, y) = F(x, y)$ and
$F(x, k x + y) = F(x, y) + k$.

The source quotes this result from Archer et al.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 6.

Stated but not proved: `MetaMathlibExt.euclideanChainLength_add_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length-add-mul).

## Euclidean chain function when the first argument divides the second

For natural numbers
$x, y \ge 1$ with $x \mid y$, the Euclidean chain function $F$ satisfies $F(x, y) = 1 + y / x$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 4.

Stated but not proved: `MetaMathlibExt.euclideanChainLength_of_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length-of-dvd).

## Euclidean chain function at one

For every natural number $y$, the Euclidean chain
function $F$ satisfies $F(1, y) = y + 1$, and for every natural number $x \ge 1$ it satisfies
$F(x, 1) = 2$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 5.

Stated but not proved: `MetaMathlibExt.euclideanChainLength_one_left_and_one_right` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#euclidean-chain-length-one-left-and-one).

## Smooth coconut structures with prescribed labels

Let $s \ge 1$ and let $c$ and
$a_1, \dots, a_s$ be natural numbers with $a_i > 0$, $a_i \mid c$ and $a_i < c$ for every $i$, such
that the only natural number dividing $c$ and all of $a_1, \dots, a_s$ is $1$. Write $CT(p, s)$ for
the coconut tree with path vertices $v_1, \dots, v_p$ and leaves $\ell_1, \dots, \ell_s$ adjacent
to $v_p$. Then there is exactly one $p \ge 1$ such that $CT(p, s)$ carries a smooth arithmetical
structure $(d, r)$ with $r(\ell_i) = a_i$ for every $i$ and $r(v_p) = c$. Moreover, for every
$p \ge 1$, any two smooth arithmetical structures $(d, r)$ and $(d', r')$ on $CT(p, s)$ with
$r(\ell_i) = r'(\ell_i) = a_i$ for every $i$ and $r(v_p) = r'(v_p) = c$ are equal.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 7.

Stated but not proved: `MetaMathlibExt.existsUnique_isSmoothCoconut` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#exists-unique-is-smooth-coconut).

## Path length of a smooth arithmetical structure on a coconut tree

Let $F$ be the
Euclidean chain function, let $p \ge 1$, and let $(d, r)$ be a smooth arithmetical structure on
the coconut tree $\mathrm{CT}(p, s)$, with path vertices $v_1, \dots, v_p$ and leaves
$v_{\ell_1}, \dots, v_{\ell_s}$. Then $p = F(r(v_{\ell_1}) + \dots + r(v_{\ell_s}), r(v_p)) - 1$.

The source states this for the smooth arithmetical structure that Proposition 7 constructs from
labels $a_1, \dots, a_s$ and $c$; every smooth arithmetical structure is the one constructed from
its own labels $a_j = r(v_{\ell_j})$ and $c = r(v_p)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 6.

Stated but not proved: `MetaMathlibExt.IsSmoothCoconut.eq_euclideanChainLength_sub_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#eq-euclidean-chain-length-sub-one).

## Smooth coconut structures with central label above one

Let $p \ge 1$ and let $(d, r)$ be
a smooth arithmetical structure on the coconut tree $\mathrm{CT}(p, s)$, with central vertex $v_p$
and leaves $\ell_1, \ldots, \ell_s$. Then $d_{v_p} > 1$ if and only if
$r_{v_p} < \sum_{j=1}^{s} r_{\ell_j}$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 8.

Stated but not proved: `MetaMathlibExt.IsSmoothCoconut.one_lt_center_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#one-lt-center-iff).

## Smooth structures on coconut trees with two leaves

Let $p \ge 1$ and let $(d, r)$ be a
smooth arithmetical structure on the coconut tree $CT(p, 2)$, whose path is
$v_1, \dots, v_p$ and whose two leaves are attached to the central vertex $v_p$. Then
$d(v_p) \le 1$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 7.

Stated but not proved: `MetaMathlibExt.IsSmoothCoconut.center_le_one_of_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#center-le-one-of-two).

## Smoothing at a path vertex of a coconut tree

Let the coconut tree $CT(p + 1, s)$ have
path vertices $v_1, \dots, v_{p+1}$, central vertex $v_{p+1}$ and leaves $\ell_1, \dots, \ell_s$,
let $d$ and $r$ be labelings of its vertices by natural numbers, and let $1 \le k \le p + 1$.
Smoothing $(d, r)$ at $v_k$ gives the labelings $(d', r')$ of $CT(p, s)$ obtained by deleting
$v_k$ and renumbering the remaining path vertices $v_1, \dots, v_{k-1}, v_{k+1}, \dots, v_{p+1}$
in order as $v_1, \dots, v_p$. Every remaining vertex keeps its value of $r$ and its value of $d$,
except that $d$ drops by $1$ (truncated at $0$) at the path neighbours $v_{k-1}$ and $v_{k+1}$
of $v_k$, where they exist.

The paper applies it only at a non-central vertex ($k \le p$) with $d(v_k) = 1$: for $k \ge 2$
this is the degree-2 smoothing of Definition 3.1 and for $k = 1$ the smoothing at $v_1$ of
Definition 3.4.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definitions 3.1 and 3.4 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutSmoothPath`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-smooth-path).

## Smoothing at a leaf of a coconut tree

Let the coconut tree $CT(p, s + 1)$ have path
vertices $v_1, \dots, v_p$, central vertex $v_p$ and leaves $\ell_1, \dots, \ell_{s+1}$, let $d$
and $r$ be labelings of its vertices by natural numbers, and let $1 \le k \le s + 1$. Smoothing
$(d, r)$ at the leaf $\ell_k$ gives the labelings $(d', r')$ of $CT(p, s)$ obtained by deleting
$\ell_k$ and renumbering the remaining leaves $\ell_1, \dots, \ell_{k-1}, \ell_{k+1}, \dots,
\ell_{s+1}$ in order as $\ell_1, \dots, \ell_s$. Every remaining vertex keeps its value of $r$
and its value of $d$, except that $d$ drops by $1$ (truncated at $0$) at the central vertex $v_p$
when $p \ge 1$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 3.4 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutSmoothLeaf`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-smooth-leaf).

## Subdivision at a path vertex of a coconut tree

Let the coconut tree $CT(p, s)$ have path
vertices $v_1, \dots, v_p$ and leaves $\ell_1, \dots, \ell_s$, let $d$ and $r$ be labelings of
its vertices by natural numbers, and let $1 \le k \le p$. Subdividing $(d, r)$ at position $k$
gives the labelings $(d', r')$ of $CT(p + 1, s)$ obtained by inserting a new path vertex $w$
just before $v_k$, so that the path becomes $v_1, \dots, v_{k-1}, w, v_k, \dots, v_p$, with
$d'(w) = 1$ and $r'(w) = r(v_{k-1}) + r(v_k)$, where $r(v_0) = 0$ (so $r'(w) = r(v_1)$ when
$k = 1$). The path neighbours of $w$, namely $v_{k-1}$ (when $k \ge 2$) and $v_k$, get
$d' = d + 1$; every other vertex keeps its value of $d$, and every vertex other than $w$ keeps
its value of $r$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 3.9 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutSubdivide`, a definition declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-subdivide).

## Example of smoothing a coconut tree at a path vertex

List a labeling of a coconut tree as
its values on the path vertices $v_1, v_2, \dots$, then $\mid$, then its values on the leaves.
Smoothing the labelings $d = (3, 1, 3, 2, 2 \mid 2, 2, 4)$ and $r = (1, 3, 2, 3, 4 \mid 2, 2, 1)$
of $CT(5, 3)$ at $v_2$ gives the labelings $d' = (2, 2, 2, 2 \mid 2, 2, 4)$ and
$r' = (1, 2, 3, 4 \mid 2, 2, 1)$ of $CT(4, 3)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Example 3.2 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutSmoothPath_example`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-smooth-path-example).

## An example of smoothing at a path vertex and at a leaf

On the coconut tree $CT(4, 4)$,
write a labeling as (values at $v_1, \dots, v_4$ | values at the leaves $\ell_1, \dots, \ell_4$).
Take $d = (1, 3, 2, 3 \mid 2, 2, 3, 1)$ and $r = (2, 2, 4, 6 \mid 3, 3, 2, 6)$. Smoothing at the
path vertex $v_1$ and then at the leaf $\ell_4$ gives the labelings $d' = (2, 2, 2 \mid 2, 2, 3)$
and $r' = (2, 4, 6 \mid 3, 3, 2)$ on $CT(3, 3)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Example 3.5 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutSmoothLeaf_example`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-smooth-leaf-example).

## Example of subdividing a coconut tree

List a labeling of a coconut tree as its values on
the path vertices $v_1, v_2, \dots$, then $\mid$, then its values on the leaves. Subdividing the
labelings $d = (2, 2, 2, 2 \mid 2, 2, 4)$ and $r = (1, 2, 3, 4 \mid 2, 2, 1)$ of $CT(4, 3)$ at
position $2$ gives the labelings $d' = (3, 1, 3, 2, 2 \mid 2, 2, 4)$ and
$r' = (1, 3, 2, 3, 4 \mid 2, 2, 1)$ of $CT(5, 3)$. These are the labelings of Example 3.2, whose
smoothing at $v_2$ is $(d, r)$, so here subdivision undoes that smoothing.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 3.9 and Example 3.2 (arXiv numbering).

Formalized by `MetaMathlibExt.coconutSubdivide_example`, a theorem declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-subdivide-example).

## Ancestors of labelings of coconut trees

Let $x$ be a pair of vertex labelings $(d, r)$
of the coconut tree $CT(p, s)$ and $y$ a pair of vertex labelings of $CT(q, t)$. Then $y$ is an
ancestor of $x$, and $x$ a descendant of $y$, when $y$ is obtained from $x$ by a finite,
possibly empty, sequence of smoothings, each performed at a vertex where the current
$d$-label equals $1$: either at a path vertex other than the central vertex, or at a leaf.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Definition 3.7 (ancestors and descendants; arXiv numbering).

Formalized by `MetaMathlibExt.CoconutAncestor`, an inductive type declared in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-ancestor).

## Path smoothing preserves arithmetical structures on coconut trees

Let $s \ge 1$ and let
$(d, r)$ be an arithmetical structure on the coconut tree $CT(p + 1, s)$, whose path vertices are
$v_1, \dots, v_{p+1}$ with central vertex $v_{p+1}$. If $d(v_k) = 1$ for some non-central path
vertex $v_k$ (that is, $1 \le k \le p$), then smoothing $(d, r)$ at $v_k$ gives an arithmetical
structure on $CT(p, s)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 3.3 and Proposition 3.6 for `i = 1`.

Stated but not proved: `MetaMathlibExt.IsArithmeticalStructure.coconutSmoothPath` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-smooth-path-2).

## Smoothing a leaf preserves arithmetical structures

Let $p$ and $s$ be natural numbers
with $p + s \ge 2$, let $(d, r)$ be an arithmetical structure on the coconut tree
$CT(p, s + 1)$, and let $\ell$ be a leaf with $d(\ell) = 1$. Then the labelings $(d', r')$
obtained by smoothing $(d, r)$ at $\ell$ form an arithmetical structure on $CT(p, s)$.

The hypothesis $p + s \ge 2$ excludes the single-edge tree $CT(1, 1)$: there $d = r = (1, 1)$,
and smoothing the leaf gives $d' = 0$ at the remaining vertex, which is not an arithmetical
structure.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 3.6.

Stated but not proved: `MetaMathlibExt.IsArithmeticalStructure.coconutSmoothLeaf` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-smooth-leaf-2).

## Subdivision preserves arithmetical structures on coconut trees

If $(d, r)$ is an
arithmetical structure on the coconut tree $CT(p, s)$, whose path vertices are $v_1, \dots, v_p$,
then for every $1 \le k \le p$, subdividing $(d, r)$ at position $k$ (inserting a new path vertex
just before $v_k$) gives an arithmetical structure on $CT(p + 1, s)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 3.11.

Stated but not proved: `MetaMathlibExt.IsArithmeticalStructure.coconutSubdivide` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#coconut-subdivide-2).

## Unique smooth ancestor

Let $s \ge 1$ and let $(d, r)$ be an arithmetical structure on the
coconut tree $CT(p, s)$ with $d(\ell_j) \ge 2$ at every leaf $\ell_j$. Then there is exactly one
pair consisting of a number $q$ with $1 \le q \le p$ and a smooth arithmetical structure on
$CT(q, s)$ that is a coconut ancestor of $(d, r)$, that is, one obtained from $(d, r)$ by a
possibly empty sequence of smoothings, each performed at a vertex whose current $d$-label is $1$
and which is either a leaf or a path vertex other than the last path vertex (the one adjacent to
the leaves).

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Lemma 3.8.

Stated but not proved: `MetaMathlibExt.IsArithmeticalStructure.existsUnique_smooth_coconutAncestor` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#exists-unique-smooth-coconut-ancestor).

## Number of descendants of a smooth coconut structure

Let $s \ge 2$ and $1 \le i \le p$,
and let $(d, r)$ be a smooth arithmetical structure on the coconut tree $\mathrm{CT}(i, s)$. Then
exactly $B(p - 1, p - i)$ arithmetical structures on $\mathrm{CT}(p, s)$ are descendants of
$(d, r)$, where $B(n, k)$ is the ballot number.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Proposition 4.5.

Stated but not proved: `MetaMathlibExt.ncard_coconutDescendants` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ncard-coconut-descendants).

## Counting coconut structures whose leaves cannot be smoothed

For $p \ge 1$ and $s \ge 2$,
the number of arithmetical structures $(d, r)$ on the coconut tree $CT(p, s)$ with $d(\ell_j) \ge 2$
at every leaf $\ell_j$ is

$$\sum_{i=1}^{p} B(p - 1, p - i)\, N(i),$$

where $B(n, k)$ is the ballot number and $N(i)$ is the number of smooth arithmetical structures on
$CT(i, s)$.

## Sources

- Diaz-Lopez, Ha, Harris, Rogers, Koss and Smith, *Arithmetical Structures on Coconut Trees*, INTEGERS 25 (2025), Article A82, Corollary 4.6.

Stated but not proved: `MetaMathlibExt.ncard_arithmeticalStructure_coconutTree_leaves_ge_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ArithmeticalStructureCoconutTreeWanted.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html#ncard-arithmetical-structure-coconut-tre-5).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetical structures on graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/algebraic-graph-theory/part-01/arithmetical-structures-on-graphs)
