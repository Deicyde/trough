---
declaration: section
origin: cited
lean: MetaMathlibExt.takagiBit, MetaMathlibExt.takagiEll, MetaMathlibExt.takagiNewdef, MetaMathlibExt.takagiBit_eq, MetaMathlibExt.takagiEll_zero, MetaMathlibExt.takagiEll_succ, MetaMathlibExt.takagiNewdef_eq, MetaMathlibExt.takagiBit_neg
statement: formalized
---

# Takagi function

50 results, 25 proved and 25 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html).

## Binary digits of a natural number

For a natural number $n$ and an integer $i$, the binary
digit $n_i \in \{0, 1\}$ of $n$ is the coefficient of $2^i$ in the binary expansion of $n$ when
$i \ge 0$, and $n_i = 0$ when $i < 0$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7.

Formalized by `MetaMathlibExt.takagiBit`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-bit).

## Takagi coefficients

Let $n$ be a natural number and $k$ an integer, and write $n_j$ for
the binary digit of $n$ at position $j$ (so $n_j = 0$ for $j < 0$). The Takagi coefficients
$\ell_i(n, k)$, for natural numbers $i$, are the natural numbers given by $\ell_0(n, k) = 0$ and,
for every natural number $i$, with $s_i = \sum_{j=0}^{i-1} n_{k-j}$, by $\ell_{i+1}(n, k) = s_i$
if $n_{k-i} = 0$ and $\ell_{i+1}(n, k) = i - s_i$ otherwise.

In particular $\ell_1(n, k) = 0$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7.

Formalized by `MetaMathlibExt.takagiEll`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-ell).

## Takagi function on dyadic presentations

For a natural number $n$ and an integer $k$, the
Takagi value $\tau(n, k)$ of the dyadic presentation $n / 2^{k+1}$ is the sum of the real series
$\sum_{i=0}^{\infty} \ell_{i+1}(n, k) / 2^{i+1}$, where $\ell_i(n, k)$ denotes the $i$-th Takagi
coefficient of $n$ and $k$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiNewdef`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-newdef).

## Formula for the binary digits

For every natural number $n$ and every integer $i$, the
binary digit $n_i$ of $n$ equals $1$ if $i \ge 0$ and the coefficient of $2^i$ in the binary
expansion of $n$ is $1$, and equals $0$ otherwise.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiBit_eq`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-bit-eq).

## The Takagi coefficient at index zero

For every natural number $n$ and every integer $k$,
the Takagi coefficient $\ell_0(n, k)$ is $0$.

The index $0$ is only an auxiliary base value: the Takagi series starts at $\ell_1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiEll_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-ell-zero).

## Formula for the Takagi coefficients

For every natural number $n$, every integer $k$ and
every natural number $i$, let $s_i = \sum_{j=0}^{i-1} n_{k-j}$, where $n_j$ denotes the binary
digit of $n$ at position $j$. Then the Takagi coefficient $\ell_{i+1}(n, k)$ equals $s_i$ if
$n_{k-i} = 0$, and equals $i - s_i$ otherwise.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiEll_succ`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-ell-succ).

## Series for the Takagi value

For every natural number $n$ and every integer $k$, the
Takagi value $\tau(n, k)$ of the dyadic presentation $n / 2^{k+1}$ satisfies
$\tau(n, k) = \sum_{i=0}^{\infty} \ell_{i+1}(n, k) / 2^{i+1}$, where $\ell_i(n, k)$ denotes the
$i$-th Takagi coefficient of $n$ and $k$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiNewdef_eq`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-newdef-eq).

## Binary digits at negative positions vanish

For every natural number $n$ and every
integer $i < 0$, the binary digit $n_i$ of $n$ is $0$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiBit_neg`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-bit-neg).

## The first Takagi coefficient vanishes

For every natural number $n$ and every integer $k$,
the Takagi coefficient $\ell_1(n, k)$ is $0$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition.

Formalized by `MetaMathlibExt.takagiEll_one`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/TakagiFunction.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-ell-one).

## Number of D-nodes of the divide-and-conquer tree

The number $\delta(n)$ of D-nodes in the
divide-and-conquer tree on $n$ leaves (OEIS A296062) is defined by the recurrence the paper
quotes from Coronado et al.: $\delta(1) = 0$, and for every natural number $m \ge 1$,
$\delta(2m) = 2\,\delta(m)$ and $\delta(2m+1) = \delta(m) + \delta(m+1) + 1$. The value at $0$
is the junk value $\delta(0) = 0$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 9 (`exp_D_recursive`).

Formalized by `MetaMathlibExt.dcDNodes`, a definition declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes).

## The divide-and-conquer D-node count at one leaf

The divide-and-conquer D-node count
$\delta$ satisfies $\delta(1) = 0$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 9 (`exp_D_recursive`).

Formalized by `MetaMathlibExt.dcDNodes_one`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-one).

## Doubling recurrence for the divide-and-conquer D-node count

For every integer $m > 0$,
the divide-and-conquer D-node count $\delta$ satisfies $\delta(2m) = 2\delta(m)$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 9 (`exp_D_recursive`).

Formalized by `MetaMathlibExt.dcDNodes_two_mul`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-two-mul).

## Odd-argument recurrence for the divide-and-conquer D-node count

For every integer
$m > 0$, the divide-and-conquer D-node count $\delta$ satisfies
$\delta(2m+1) = \delta(m) + \delta(m+1) + 1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 9 (`exp_D_recursive`).

Formalized by `MetaMathlibExt.dcDNodes_two_mul_add_one`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-two-mul-add-one).

## Small values of the divide-and-conquer D-node count

The divide-and-conquer D-node count
$\delta$ satisfies $\delta(2) = 0$, $\delta(3) = 1$, $\delta(4) = 0$, $\delta(5) = 2$,
$\delta(6) = 2$ and $\delta(7) = 2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 9 (`exp_D_recursive`).

Formalized by `MetaMathlibExt.dcDNodes_small`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-small).

## Level counts of D-nodes

For natural numbers $n$ and $i$, let $n_i$ be the binary digit
of $n$ at position $i$ (the coefficient of $2^i$ in the binary expansion of $n$). The level count
$\lambda_i(n)$ is $n \bmod 2^i$ if $n_i = 0$, and $2^i - (n \bmod 2^i)$ if $n_i = 1$.

This is the paper's closed form for the number of D-nodes on level $i$ of the
divide-and-conquer tree on $n$ leaves.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 11 (`exp_D_closed`).

Formalized by `MetaMathlibExt.dcLevelDNodes`, a definition declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-level-dnodes).

## Level count of D-nodes when the binary digit is zero

Let $n$ and $i$ be natural numbers
such that the binary digit $n_i$ of $n$ (the coefficient of $2^i$ in the binary expansion of
$n$) equals $0$. Then the level count of D-nodes is $\lambda_i(n) = n \bmod 2^i$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 11 (`exp_D_closed`).

Formalized by `MetaMathlibExt.dcLevelDNodes_of_digit_eq_zero`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-level-dnodes-of-digit-eq-zero).

## Level count of D-nodes when the binary digit is one

Let $n$ and $i$ be natural numbers
such that the binary digit $n_i$ of $n$ (the coefficient of $2^i$ in the binary expansion of
$n$) equals $1$. Then the level count of D-nodes is $\lambda_i(n) = 2^i - (n \bmod 2^i)$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 11 (`exp_D_closed`).

Formalized by `MetaMathlibExt.dcLevelDNodes_of_digit_eq_one`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-level-dnodes-of-digit-eq-one).

## Level count of D-nodes on level zero

For every natural number $n$, the level count of
D-nodes on level $0$ is $\lambda_0(n) = n \bmod 2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 11 (`exp_D_closed`).

Formalized by `MetaMathlibExt.dcLevelDNodes_zero`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-level-dnodes-zero).

## Number of $D$-nodes of a full binary tree

A $D$-node of a full binary tree is an
interior node whose two subtrees have different numbers of leaves. The number of $D$-nodes of a
full binary tree is the number of its interior nodes that are $D$-nodes.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition (`S`-nodes and `D`-nodes).

Formalized by `MetaMathlibExt.treeDNodes`, a definition declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-dnodes).

## Number of $S$-nodes of a full binary tree

An $S$-node of a full binary tree is an
interior node whose two subtrees have the same number of leaves. The number of $S$-nodes of a
full binary tree is the number of its interior nodes that are $S$-nodes.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition (`S`-nodes and `D`-nodes).

Formalized by `MetaMathlibExt.treeSNodes`, a definition declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-snodes).

## Divide-and-conquer trees

A divide-and-conquer tree is a full binary tree in which, at
every interior node, the numbers of leaves of the two subtrees differ by at most $1$. In
particular a single leaf is a divide-and-conquer tree.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition (Divide-and-conquer tree).

Formalized by `MetaMathlibExt.IsDivideConquerTree`, a definition declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#is-divide-conquer-tree).

## Recursion for the number of $D$-nodes

Write $D(t)$ for the number of $D$-nodes of a
full binary tree $t$. If the root of $t$ has left subtree $l$ and right subtree $r$, then
$D(t) = \varepsilon + D(l) + D(r)$, where $\varepsilon = 0$ if $l$ and $r$ have the same number
of leaves and $\varepsilon = 1$ otherwise.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition (`S`-nodes and `D`-nodes).

Formalized by `MetaMathlibExt.treeDNodes_node`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-dnodes-node).

## Recursion for the number of $S$-nodes

Write $S(t)$ for the number of $S$-nodes of a
full binary tree $t$. If the root of $t$ has left subtree $l$ and right subtree $r$, then
$S(t) = \varepsilon + S(l) + S(r)$, where $\varepsilon = 1$ if $l$ and $r$ have the same number
of leaves and $\varepsilon = 0$ otherwise.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition (`S`-nodes and `D`-nodes).

Formalized by `MetaMathlibExt.treeSNodes_node`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-snodes-node).

## The single-leaf tree

The full binary tree consisting of a single leaf has no $D$-nodes
and no $S$-nodes, and it is a divide-and-conquer tree.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definitions (`S`-nodes and `D`-nodes; Divide-and-conquer tree).

Formalized by `MetaMathlibExt.treeNodes_nil`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-nodes-nil).

## The divide-and-conquer condition at the root

A full binary tree whose root has left
subtree $L$ and right subtree $R$ is a divide-and-conquer tree if and only if the numbers of
leaves of $L$ and $R$ differ by at most $1$ and both $L$ and $R$ are divide-and-conquer trees.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Definition (Divide-and-conquer tree).

Formalized by `MetaMathlibExt.isDivideConquerTree_node`, a theorem declared in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#is-divide-conquer-tree-node).

## Normalized form of $n = 2^k + r$

Let $n$, $k$ and $r$ be natural numbers with $r < 2^k$
and $n = 2^k + r$, and let $x$ be a rational number with $n = 2^k (1 + x)$. Then $x = r / 2^k$
and $1 + x = n / 2^k$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 2 (`jis-2024-24.2.7-lem-2`).

Stated but not proved: `MetaMathlibExt.dyadic_mantissa_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dyadic-mantissa-eq).

## $D$-nodes and $S$-nodes of a full binary tree

Let $t$ be a full binary tree with $n$
leaves and let $a$ be the number of $S$-nodes of $t$. Then the number of $D$-nodes of $t$ is
$n - 1 - a$ (subtraction of natural numbers, truncated at $0$).

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 5 (`jis-2024-24.2.7-lem-5`).

Stated but not proved: `MetaMathlibExt.treeDNodes_eq_numLeaves_sub_one_sub_treeSNodes` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-dnodes-eq-num-leaves-sub-one-sub-tr).

## The Takagi function at dyadic rationals counts D-nodes (Coronado et al.)

Let $k$ and $r$
be natural numbers with $r \le 2^k$. Write $\tau(r / 2^k)$ for the Takagi value of the dyadic
presentation $r / 2^k$, and $\delta(n)$ for the number of $D$-nodes of the divide-and-conquer
tree on $n$ leaves, given by $\delta(1) = 0$, $\delta(2m) = 2 \delta(m)$ and
$\delta(2m + 1) = \delta(m) + \delta(m + 1) + 1$ for $m \ge 1$. Then
$\tau(r / 2^k) = \delta(2^k + r) / 2^k$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 8 (`jis-2024-24.2.7-thm-8`).

Stated but not proved: `MetaMathlibExt.takagi_dyadic_eq_dcDNodes_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-dyadic-eq-dc-dnodes-div).

## Coronado et al.'s count of $D$-nodes in divide-and-conquer trees

Every
divide-and-conquer tree with $n$ leaves has exactly $\delta(n)$ $D$-nodes, where $\delta$ is the
function on positive integers given by $\delta(1) = 0$, $\delta(2m) = 2\delta(m)$ and
$\delta(2m+1) = \delta(m) + \delta(m+1) + 1$ for $m \ge 1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 9 (`jis-2024-24.2.7-thm-9`).

Stated but not proved: `MetaMathlibExt.treeDNodes_eq_dcDNodes_of_isDivideConquerTree` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#tree-dnodes-eq-dc-dnodes-of-is-divide-co).

## Midpoint identity for the divide-and-conquer D-node count

Let $\delta$ be the
divide-and-conquer D-node count. Let $k$ and $r$ be natural numbers with $0 < r < 2^k$, put
$n = 2^k + r$, and let $\nu_2(r)$ be the position of the lowest nonzero binary digit of $r$,
counted from $0$ (the exponent of the largest power of $2$ dividing $r$). Then
$\delta(n) = \frac{\delta(n-1) + \delta(n+1)}{2} + 1 - \nu_2(r)$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Corollary 10 (`jis-2024-24.2.7-cor-10`).

Stated but not proved: `MetaMathlibExt.dcDNodes_eq_midpoint_add_one_sub_lowestBit` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-eq-midpoint-add-one-sub-lowest).

## Level-sum formula for the divide-and-conquer D-node count

Let $\delta$ be the
divide-and-conquer D-node count. For every integer $n > 0$, let $k = \lfloor \log_2 n \rfloor$,
let $\lambda_i(n)$ be the level-$i$ D-node count, and let $n_i$ be the binary digit of $n$ at
$2^i$. Then

$$\delta(n) = \sum_{i=0}^{k-1} \lambda_i(n),$$

and explicitly

$$\delta(n) = \sum_{i=0}^{k-1} \left(n_i 2^i + (-1)^{n_i} (n \bmod 2^i)\right).$$

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 11 (`jis-2024-24.2.7-thm-11`).

Stated but not proved: `MetaMathlibExt.dcDNodes_eq_sum_dcLevelDNodes` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-eq-sum-dc-level-dnodes).

## Adding a larger power of two raises the Hamming weight by one

For a natural number $m$,
write $s_1(m)$ for the sum of the binary digits of $m$ (the number of ones in its binary
expansion). For all natural numbers $k$ and $r$ with $r < 2^k$, $s_1(2^k + r) = s_1(r) + 1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 13 (`jis-2024-24.2.7-lem-13`).

Stated but not proved: `MetaMathlibExt.hammingWeight_two_pow_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#hamming-weight-two-pow-add).

## Hamming weight of the successor of an even number

For a natural number $m$, write
$s_1(m)$ for the sum of the binary digits of $m$ (the number of ones in its binary expansion).
If $n$ is an even natural number (including $n = 0$), then $s_1(n + 1) = s_1(n) + 1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 14 (`jis-2024-24.2.7-lem-14`).

Stated but not proved: `MetaMathlibExt.hammingWeight_succ_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#hamming-weight-succ-of-even).

## Hamming weight of the predecessor of an odd number

For a natural number $m$, write
$s_1(m)$ for the sum of the binary digits of $m$ (the number of ones in its binary expansion).
If $n$ is an odd natural number, then $s_1(n - 1) = s_1(n) - 1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 15 (`jis-2024-24.2.7-lem-15`).

Stated but not proved: `MetaMathlibExt.hammingWeight_pred_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#hamming-weight-pred-of-odd).

## Hamming weight of a power of two minus an odd number

For a natural number $m$, write
$s_1(m)$ for the sum of the binary digits of $m$ (the number of ones in its binary expansion).
Let $k$ and $r$ be natural numbers with $r$ odd and $2r < 2^k$, that is, $r < 2^{k-1}$. Then
$s_1(2^k - r) = 1 + k - s_1(r)$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 16 (`jis-2024-24.2.7-lem-16`).

Stated but not proved: `MetaMathlibExt.hammingWeight_two_pow_sub_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#hamming-weight-two-pow-sub-of-odd).

## Level counts of D-nodes at consecutive integers

Let $k$, $r$ and $i$ be natural numbers
with $r$ odd, $r < 2^k$ and $0 < i < k$, and let $n = 2^k + r$. Then the level counts of
D-nodes satisfy $\lambda_i(n) - \lambda_i(n-1) = 1$ if the binary digit $n_i$ of $n$ is $0$,
and $\lambda_i(n) - \lambda_i(n-1) = -1$ if $n_i = 1$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 17 (`jis-2024-24.2.7-lem-17`).

Stated but not proved: `MetaMathlibExt.dcLevelDNodes_sub_pred` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-level-dnodes-sub-pred).

## Symmetry of the D-node counts

For all natural numbers $k$ and $r$ with $r \le 2^k$,
$\delta(2^{k+1} - r) = \delta(2^k + r)$, where $\delta(n)$ denotes the number of D-nodes in the
divide-and-conquer tree on $n$ leaves.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 18 (`jis-2024-24.2.7-lem-18`).

Stated but not proved: `MetaMathlibExt.dcDNodes_two_pow_succ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-two-pow-succ-sub).

## Successor formula for the D-node count at even arguments

Let $\delta$ be the
divide-and-conquer D-node count and $s_1(n)$ the number of ones in the binary expansion of $n$.
For every even integer $n > 0$, $\delta(n+1) = \delta(n) + \lfloor \log_2 n \rfloor - 2 s_1(n) + 2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 19 (`jis-2024-24.2.7-lem-19`).

Stated but not proved: `MetaMathlibExt.dcDNodes_succ_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-succ-of-even).

## Successor formula for the D-node count at odd arguments

Let $\delta$ be the
divide-and-conquer D-node count and $s_1(n)$ the number of ones in the binary expansion of $n$.
For every odd natural number $n$,
$\delta(n+1) = \delta(n) + \lfloor \log_2 n \rfloor - 2 s_1(n) + 2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 20 (`jis-2024-24.2.7-lem-20`).

Stated but not proved: `MetaMathlibExt.dcDNodes_succ_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-succ-of-odd).

## Successor formula for the divide-and-conquer D-node count

Let $\delta$ be the
divide-and-conquer D-node count and $s_1(n)$ the number of ones in the binary expansion of $n$.
For every integer $n > 0$,
$\delta(n+1) = \delta(n) + \lfloor \log_2 n \rfloor - 2 s_1(n) + 2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 21 (`jis-2024-24.2.7-thm-21`).

Stated but not proved: `MetaMathlibExt.dcDNodes_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-succ).

## Binary-digit formula for the divide-and-conquer D-node count

Let $\delta$ be the
divide-and-conquer D-node count and let $s_1(m)$ be the number of ones in the binary expansion
of $m$. For every integer $n > 0$, let $k = \lfloor \log_2 n \rfloor$ and let $n_j$ be the binary
digit of $n$ at $2^j$. Then

$$\delta(n) = \sum_{i=0}^{k-1} 2^i n_i \Big(k - i - 2 \sum_{j=i}^{k} n_j + 4\Big),$$

and also

$$\delta(n) = \sum_{i=0}^{k-1} 2^i n_i \Big(k - i - 2\, s_1(\lfloor n / 2^i \rfloor) + 4\Big).$$

The printed inner sum $\sum_{j=i}^k n_i$ is read as $\sum_{j=i}^k n_j$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 22 (`jis-2024-24.2.7-thm-22`).

Stated but not proved: `MetaMathlibExt.dcDNodes_eq_sum_digit_weight` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#dc-dnodes-eq-sum-digit-weight).

## Binary digit sum from consecutive D-node counts

For every natural number $n > 0$, the
sum $s_1(n)$ of the binary digits of $n$ satisfies
$s_1(n) = (\delta(n) - \delta(n+1) + \lfloor \log_2 n \rfloor)/2 + 1$ in $\mathbb{Q}$, where
$\delta(m)$ denotes the number of D-nodes in the divide-and-conquer tree on $m$ leaves.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Corollary 23 (`jis-2024-24.2.7-cor-23`).

Stated but not proved: `MetaMathlibExt.hammingWeight_eq_dcDNodes_diff` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#hamming-weight-eq-dc-dnodes-diff).

## Midpoint recurrence for the Takagi function at dyadic rationals

Let $k$ and $r$ be
natural numbers with $1 \le r < 2^k$. For a natural number $m$, write $\tau(m / 2^k)$ for the
Takagi value of the dyadic presentation $m / 2^k$, and let $\rho_1$ be the $2$-adic valuation of
$r$, the position (counted from $0$) of the lowest nonzero binary digit of $r$. Then
$\tau(r / 2^k) = (\tau((r - 1) / 2^k) + \tau((r + 1) / 2^k))/2 + (1 - \rho_1)/2^k$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 24 (`jis-2024-24.2.7-thm-24`).

Stated but not proved: `MetaMathlibExt.takagi_dyadic_eq_midpoint_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-dyadic-eq-midpoint-add).

## Takagi values at dyadic rationals from level $D$-node counts

Let $k$ and $r$ be
natural numbers with $r < 2^k$ and put $n = 2^k + r$. Write $\tau(r, k-1)$ for the Takagi value
of the dyadic presentation $r/2^k$, write $n_i = \lfloor n/2^i \rfloor \bmod 2$ for the binary
digit of $n$ at position $i$, and let $\lambda_i(n)$ be the level-$i$ $D$-node count, which
equals $n \bmod 2^i$ if $n_i = 0$ and $2^i - (n \bmod 2^i)$ if $n_i = 1$. Then

$$\tau(r, k-1) = 2^{-k} \sum_{i=0}^{k-1} \lambda_i(n)$$

and

$$\tau(r, k-1) = 2^{-k} \sum_{i=0}^{k-1} (n_i 2^i + (-1)^{n_i} (n \bmod 2^i)).$$

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 25 (`jis-2024-24.2.7-thm-25`).

Stated but not proved: `MetaMathlibExt.takagi_dyadic_eq_sum_dcLevelDNodes` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-dyadic-eq-sum-dc-level-dnodes).

## Consecutive Takagi values at dyadic rationals

Let $k$ and $r$ be natural numbers with
$r < 2^k$ and put $n = 2^k + r$. Write $\tau(m, k-1)$ for the Takagi value of the dyadic
presentation $m/2^k$, and $s_1(n)$ for the number of ones in the binary expansion of $n$. Then
$\tau(r+1, k-1) = \tau(r, k-1) + (k - 2 s_1(n) + 2)/2^k$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 26 (`jis-2024-24.2.7-thm-26`).

Stated but not proved: `MetaMathlibExt.takagi_dyadic_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-dyadic-succ).

## Takagi values at dyadic rationals from binary digits

Let $k$ and $r$ be natural
numbers with $r < 2^k$ and put $n = 2^k + r$. Write $\tau(r, k-1)$ for the Takagi value of the
dyadic presentation $r/2^k$, write $n_j = \lfloor n/2^j \rfloor \bmod 2$ for the binary digit of
$n$ at position $j$, and write $s_1(m)$ for the number of ones in the binary expansion of $m$.
Then

$$\tau(r, k-1) = 2^{-k} \sum_{i=0}^{k-1} 2^i n_i (k - i - 2 \sum_{j=i}^{k} n_j + 4)$$

and

$$\tau(r, k-1) = 2^{-k} \sum_{i=0}^{k-1} 2^i n_i (k - i - 2 s_1(\lfloor n/2^i \rfloor) + 4).$$

The paper prints the inner sum as $\sum_{j=i}^{k} n_i$; it is read here as $\sum_{j=i}^{k} n_j$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 27 (`jis-2024-24.2.7-thm-27`).

Stated but not proved: `MetaMathlibExt.takagi_dyadic_eq_sum_digit_weight` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#takagi-dyadic-eq-sum-digit-weight).

## Binary digit sum from consecutive Takagi values

Let $k$ and $r$ be natural numbers
with $r < 2^k$, let $n = 2^k + r$, and let $s_1(n)$ be the sum of the binary digits of $n$.
Writing $\tau(m, k - 1)$ for the Takagi value of the dyadic presentation $m / 2^k$, one has
$s_1(n) = 2^{k-1} \bigl(\tau(r, k - 1) - \tau(r + 1, k - 1)\bigr) + (k + 2)/2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Theorem 28 (`jis-2024-24.2.7-thm-28`).

Stated but not proved: `MetaMathlibExt.hammingWeight_eq_takagi_diff` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#hamming-weight-eq-takagi-diff).

## Sum of binary digit sums below a power of two

For a natural number $i$, let $s_1(i)$
denote the sum of the binary digits of $i$. Then for every natural number $m$,
$2 \sum_{i < 2^m} s_1(i) = 2^m m$; that is, the binary expansions of $0, 1, \dots, 2^m - 1$
contain $2^m m / 2$ ones in total.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Lemma 29 (`jis-2024-24.2.7-lem-29`).

Stated but not proved: `MetaMathlibExt.two_mul_sum_hammingWeight_range_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#two-mul-sum-hamming-weight-range-two-pow).

## Trollope's formula via the Takagi function

For a natural number $m$, write $s_1(m)$ for
the sum of the binary digits of $m$ and $S_1(m) = \sum_{i=0}^{m-1} s_1(i)$. Let $k$ and $r$ be
natural numbers with $r < 2^k$, and put $n = 2^k + r$ and $x = r / 2^k$. Write $\tau(x)$ for
the Takagi value of the dyadic presentation $r / 2^k$. Then

$$S_1(n) = \frac{n \log_2 n}{2} + 2^{k-1} \left(2x - \tau(x) - (1 + x) \log_2 (1 + x)\right).$$

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Corollary 30 (`jis-2024-24.2.7-cor-30`).

Stated but not proved: `MetaMathlibExt.sum_hammingWeight_range_eq_trollope` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#sum-hamming-weight-range-eq-trollope).

## Cumulative binary digit sums via the Takagi function

For a natural number $m$, write
$s_1(m)$ for the sum of the binary digits of $m$ and $S_1(m) = \sum_{i=0}^{m-1} s_1(i)$. Let
$k$ and $r$ be natural numbers with $r < 2^k$, and put $n = 2^k + r$ and $x = r / 2^k$. Write
$\tau(x)$ for the Takagi value of the dyadic presentation $r / 2^k$, and $\delta(n)$ for the
number of $D$-nodes of the divide-and-conquer tree on $n$ leaves, given by $\delta(1) = 0$,
$\delta(2m) = 2 \delta(m)$ and $\delta(2m + 1) = \delta(m) + \delta(m + 1) + 1$ for $m \ge 1$.
Then $S_1(n) = (nk + 2^k (2x - \tau(x)))/2$, $S_1(n) = (nk + 2r - 2^k \tau(x))/2$ and
$S_1(n) = (nk + 2r - \delta(n))/2$.

## Sources

- Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, Journal of Integer Sequences 27 (2024), Article 24.2.7, Corollary 31 (`jis-2024-24.2.7-cor-31`).

Stated but not proved: `MetaMathlibExt.sum_hammingWeight_range_eq_takagi_dcDNodes` is written with `theorem_wanted` in [WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/TakagiDyadicIdentitiesWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html#sum-hamming-weight-range-eq-takagi-dc-dn).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Takagi function](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/takagi-function)
