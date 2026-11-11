---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPosetMatrix, MetaMathlibExt.IsPosetMatrix.Rel, MetaMathlibExt.IsPosetMatrix.upper, MetaMathlibExt.IsPosetMatrix.diagonal, MetaMathlibExt.IsPosetMatrix.transitive, MetaMathlibExt.IsPosetMatrix.rel_refl, MetaMathlibExt.IsPosetMatrix.rel_trans, MetaMathlibExt.isPosetMatrix_block_iff_directSum_ordinalSum
statement: formalized
---

# Poset matrices and quasi-full rooted trees

12 results, 7 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html).

## Poset matrix

An $n \times n$ Boolean matrix $M$, with rows and columns indexed by
$\{0, \dots, n-1\}$, is an upper-triangular $(0, 1)$-poset matrix when its entries strictly
below the main diagonal are false ($M_{ij}$ is false whenever $j < i$), its diagonal entries
$M_{ii}$ are true, and its true entries are transitive: if $M_{ij}$ and $M_{jk}$ are true,
then $M_{ik}$ is true.

## Sources

- JIS `mohammad3.tex`, lines 171–176.

Formalized by `MetaMathlibExt.IsPosetMatrix`, a definition declared in [MathlibExt/Order/PosetMatrix.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#is-poset-matrix).

## Relation represented by a Boolean matrix

Let $M$ be an $n \times n$ Boolean matrix
with rows and columns indexed by $\{0, \dots, n-1\}$. The relation represented by $M$
relates index $i$ to index $j$ exactly when the entry $M_{ij}$ is true.

The matrix $M$ is arbitrary; it need not be a poset matrix.

Formalized by `MetaMathlibExt.IsPosetMatrix.Rel`, a definition declared in [MathlibExt/Order/PosetMatrix.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#rel).

## Poset matrices are upper triangular

If $M$ is an $n \times n$ poset matrix, then
$M_{ij}$ is false for all indices $i, j < n$ with $j < i$.

Formalized by `MetaMathlibExt.IsPosetMatrix.upper`, a theorem declared in [MathlibExt/Order/PosetMatrix.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#upper).

## Diagonal entries of a poset matrix

If $M$ is an $n \times n$ poset matrix, then
$M_{ii}$ is true for every index $i < n$.

Formalized by `MetaMathlibExt.IsPosetMatrix.diagonal`, a theorem declared in [MathlibExt/Order/PosetMatrix.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#diagonal).

## Transitivity of the true entries of a poset matrix

If $M$ is an $n \times n$ poset
matrix, then for all indices $i, j, k < n$, if $M_{ij}$ and $M_{jk}$ are true, then $M_{ik}$
is true.

Formalized by `MetaMathlibExt.IsPosetMatrix.transitive`, a theorem declared in [MathlibExt/Order/PosetMatrix.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#transitive).

## The relation of a poset matrix is reflexive

If $M$ is an $n \times n$ poset matrix,
then the relation represented by $M$ relates every index $i < n$ to itself.

Formalized by `MetaMathlibExt.IsPosetMatrix.rel_refl`, a theorem declared in [MathlibExt/Order/PosetMatrix.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#rel-refl).

## The relation of a poset matrix is transitive

If $M$ is an $n \times n$ poset matrix
and $i, j, k < n$ are indices such that the relation represented by $M$ relates $i$ to $j$
and $j$ to $k$, then it relates $i$ to $k$.

Formalized by `MetaMathlibExt.IsPosetMatrix.rel_trans`, a theorem declared in [MathlibExt/Order/PosetMatrix.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/PosetMatrix.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#rel-trans).

## Block decomposition of a poset matrix

Let $m, k \ge 1$ and let $M$ be a poset matrix of
order $m + k$, a Boolean matrix with rows and columns indexed by $0, \dots, m + k - 1$. Then
$M_{ij}$ is false for all $i < m \le j$ if and only if there are poset matrices $A$ of order $m$
and $B$ of order $k$ such that $M$ is their direct sum: $M_{ij} = A_{ij}$ for $i, j < m$,
$M_{m+i, m+j} = B_{ij}$ for $i, j < k$, and every other entry of $M$ is false. Likewise $M_{ij}$
is true for all $i < m \le j$ if and only if there are poset matrices $A$ of order $m$ and $B$ of
order $k$ such that $M$ is their ordinal sum: the same diagonal blocks, $M_{ij}$ true for all
$i < m \le j$, and $M_{ij}$ false for all $j < m \le i$.

Only one block length is stated; the version with several lengths $n_1 < \dots < n_r$ follows by
iterating it.

## Sources

- Salah Uddin Mohammad, Md. Shah Noor, and Md. Rashed Talukder, *Recognition and Enumeration of the Quasi-Full Rooted Trees*, Journal of Integer Sequences 28 (2025), Article 25.6.3, Theorem 3 (`jis-2025-25.6.3-thm-3`).

Stated but not proved: `MetaMathlibExt.isPosetMatrix_block_iff_directSum_ordinalSum` is written with `theorem_wanted` in [WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#is-poset-matrix-block-iff-direct-sum-ord).

## Direct and ordinal sums of poset matrices represent sums of posets

A poset matrix $M$ of
order $n$, a Boolean matrix with rows and columns indexed by $0, \dots, n - 1$, represents a
partial order $P$ when there is a bijection $e$ from $\{0, \dots, n - 1\}$ to $P$ such that
$e(i) \le e(j)$ if and only if $M_{ij}$ is true. Let $A$ and $B$ be poset matrices of orders $m$
and $k$ representing partial orders $P$ and $Q$. Let $A \oplus B$ and $A \boxplus B$ be the
matrices $N$ of order $m + k$ with $N_{ij} = A_{ij}$ for $i, j < m$, $N_{m+i, m+j} = B_{ij}$ for
$i, j < k$, and $N_{ij}$ false for all $j < m \le i$, where $N_{ij}$ for $i < m \le j$ is false
in $A \oplus B$ and true in $A \boxplus B$. Then $A \oplus B$ is a poset matrix representing the
disjoint sum $P + Q$, in which no element of $P$ is comparable with an element of $Q$, and
$A \boxplus B$ is a poset matrix representing the ordinal sum $P \oplus Q$, in which every
element of $P$ lies below every element of $Q$.

Only sums of two terms are stated; sums of $r$ terms follow by iterating.

## Sources

- Salah Uddin Mohammad, Md. Shah Noor, and Md. Rashed Talukder, *Recognition and Enumeration of the Quasi-Full Rooted Trees*, Journal of Integer Sequences 28 (2025), Article 25.6.3, Theorem 4 (`jis-2025-25.6.3-thm-4`).

Stated but not proved: `MetaMathlibExt.directSum_ordinalSum_represents` is written with `theorem_wanted` in [WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#direct-sum-ordinal-sum-represents).

## Block properties decide connectedness of the represented poset

Let $M$ be a poset matrix
of order $n$, a Boolean matrix with rows and columns indexed by $0, \dots, n - 1$, that
represents a partial order $P$: there is a bijection $e$ from $\{0, \dots, n - 1\}$ to $P$ such
that $e(i) \le e(j)$ if and only if $M_{ij}$ is true. Let $1 \le r < n$. If $M_{ij}$ is true for
all $i < r \le j$ (the block of $1$s property of length $r$), then $P$ is connected: every subset
$S$ of $P$ such that $x \in S \iff y \in S$ whenever $x \le y$ is empty or all of $P$. If
$M_{ij}$ is false for all $i < r \le j$ (the block of $0$s property of length $r$), then $P$ is
disconnected: some nonempty subset $S$ of $P$ with nonempty complement satisfies
$x \in S \iff y \in S$ whenever $x \le y$.

Since a relabeling of $M$ represents the same poset, this also covers matrices that satisfy a
block property after relabeling.

## Sources

- Salah Uddin Mohammad, Md. Shah Noor, and Md. Rashed Talukder, *Recognition and Enumeration of the Quasi-Full Rooted Trees*, Journal of Integer Sequences 28 (2025), Article 25.6.3, Theorem 5 (`jis-2025-25.6.3-thm-5`).

Stated but not proved: `MetaMathlibExt.connected_or_disconnected_of_block_property` is written with `theorem_wanted` in [WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#connected-or-disconnected-of-block-prope).

## Arity of quasi-full rooted trees

Let $P$ be a finite partial order with $n \ge 3$
elements that is a rooted tree: $P$ has a least element and, for every $x \in P$, the elements
below $x$ form a chain. For a natural number $t$, call $P$ quasi-full $t$-ary when every $x \in P$
is covered by exactly $\min(|U_x| - 1, t)$ elements of $P$, where $U_x = \{y \in P : x \le y\}$.
Then (i) if $P$ is quasi-full $(n - 1)$-ary, it is quasi-full $t$-ary for every $t \ge n$; and
(ii) if $P$ is quasi-full $t$-ary for some $t \le n - 2$, it is not quasi-full $t'$-ary for any
$t' \ge n$.

The source states this for poset matrices representing quasi-full $t$-ary rooted trees; both
parts depend only on the represented poset.

## Sources

- Salah Uddin Mohammad, Md. Shah Noor, and Md. Rashed Talukder, *Recognition and Enumeration of the Quasi-Full Rooted Trees*, Journal of Integer Sequences 28 (2025), Article 25.6.3, Theorem 10 (`jis-2025-25.6.3-thm-10`).

Stated but not proved: `MetaMathlibExt.quasiFullTree_arity` is written with `theorem_wanted` in [WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#quasi-full-tree-arity).

## Direct sum criterion for relabeling inequivalence

Let $n, t \ge 2$ and let
$M$ and $M'$ be poset matrices of order $n$, Boolean matrices with rows and columns indexed by
$0, \dots, n - 1$. Let $0 = l_0 < l_1 < \dots < l_t = n$ be such that the gaps $l_{k+1} - l_k$ are
nondecreasing in $k$. Suppose that for every $k \le t$, $M_{ij}$ is false for all $i < l_k \le j$,
and that for every $k < t$ there is $s \ge 1$ with $l_k + s < l_{k+1}$ such that $M_{ij}$ is true
for all $i, j$ with $l_k \le i < l_k + s \le j < l_{k+1}$. Suppose the same of $M'$ with a sequence
$0 = l'_0 < l'_1 < \dots < l'_t = n$ whose gaps are nondecreasing. If $l_k \ne l'_k$ for some $k$,
then $M$ and $M'$ are not relabeling equivalent: there is no permutation $\sigma$ of
$\{0, \dots, n - 1\}$ with $M'_{ij} = M_{\sigma(i) \sigma(j)}$ for all $i, j$.

The source assumes in addition that $M$ and $M'$ represent quasi-full $t$-ary rooted forests; the
statement holds without that assumption.

## Sources

- Salah Uddin Mohammad, Md. Shah Noor, and Md. Rashed Talukder, *Recognition and Enumeration of the Quasi-Full Rooted Trees*, Journal of Integer Sequences 28 (2025), Article 25.6.3, Theorem 11 (`jis-2025-25.6.3-thm-11`).

Stated but not proved: `MetaMathlibExt.not_relabel_equiv_of_blockLengths_ne` is written with `theorem_wanted` in [WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/QuasiFullRootedTreeWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html#not-relabel-equiv-of-block-lengths-ne).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poset matrices and quasi-full rooted trees](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/partially-ordered-sets/poset-matrices-and-quasi-full-rooted-trees)
