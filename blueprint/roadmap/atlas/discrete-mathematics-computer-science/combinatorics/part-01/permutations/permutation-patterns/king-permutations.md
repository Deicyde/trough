---
declaration: section
origin: cited
lean: MetaMathlibExt.king_permutation_not_separable, MetaMathlibExt.king_permutation_hasPattern_classical, MetaMathlibExt.IsKingPerm, MetaMathlibExt.permAscentCount, MetaMathlibExt.permDescentCount, MetaMathlibExt.permStats_one_fin_three, MetaMathlibExt.permStats_revPerm_fin_three, MetaMathlibExt.ContainsFlatPOPBelow
statement: formalized
---

# King permutations

23 results, 13 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html).

## No king permutation of length at least $2$ is separable

For every $n \ge 2$, every
permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$ in which adjacent entries never differ by exactly
$1$, that is, $|\sigma(i + 1) - \sigma(i)| \ne 1$ whenever $i + 1 < n$, contains the classical
pattern $2413$ or the classical pattern $3142$. Since the separable permutations are those
avoiding both $2413$ and $3142$, no such permutation is separable.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Theorem 2.

Stated but not proved: `MetaMathlibExt.king_permutation_not_separable` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-permutation-not-separable).

## King permutations of length at least $2$ contain $12$, $21$, $132$, $213$, $231$ and $312$

For every $n \ge 2$, every permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$ in which adjacent
entries never differ by exactly $1$, that is, $|\sigma(i + 1) - \sigma(i)| \ne 1$ whenever
$i + 1 < n$, contains each of the classical patterns $12$, $21$, $132$, $213$, $231$ and $312$.

Theorem 1 also lists nine partially ordered patterns that no such permutation avoids; they are
not part of this statement.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Theorem 1.

Stated but not proved: `MetaMathlibExt.king_permutation_hasPattern_classical` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-permutation-has-pattern-classical).

## King permutations

A permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$ is a king permutation
if adjacent entries never differ by exactly $1$: for every position $i$ with $i + 1 < n$, neither
$\sigma(i + 1) = \sigma(i) + 1$ nor $\sigma(i) = \sigma(i + 1) + 1$. Equivalently,
$|\sigma(i + 1) - \sigma(i)| > 1$ for all adjacent positions $i$ and $i + 1$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.3.

Formalized by `MetaMathlibExt.IsKingPerm`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#is-king-perm).

## Number of ascents of a permutation

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$
written in one-line notation, $\operatorname{asc}(\sigma)$ is the number of positions $i$ with
$i + 1 < n$ and $\sigma(i) < \sigma(i + 1)$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permAscentCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#perm-ascent-count).

## Number of descents of a permutation

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$
written in one-line notation, $\operatorname{des}(\sigma)$ is the number of positions $i$ with
$i + 1 < n$ and $\sigma(i + 1) < \sigma(i)$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permDescentCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#perm-descent-count).

## Statistics of the permutation $123$

The identity permutation of $\{0, 1, 2\}$, written
$012$ in one-line notation and $123$ after shifting every value up by one, has two ascents, no
descents, three left-to-right maxima, one right-to-left maximum, one left-to-right minimum and
three right-to-left minima.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permStats_one_fin_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#perm-stats-one-fin-three).

## Statistics of the permutation $321$

The reversal permutation $i \mapsto 2 - i$ of
$\{0, 1, 2\}$, written $210$ in one-line notation and $321$ after shifting every value up by
one, has no ascents, two descents, one left-to-right maximum, three right-to-left maxima, three
left-to-right minima and one right-to-left minimum.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1 (statistics).

Formalized by `MetaMathlibExt.permStats_revPerm_fin_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#perm-stats-rev-perm-fin-three).

## Containing a flat pattern with one bottom label

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n - 1\}$ and let $j \in \{0, 1, 2, 3\}$. Then $\sigma$ contains the flat partially
ordered pattern $P_{j+1}$ of size $4$, in which label $j + 1$ lies below the other three labels
(which are mutually incomparable), if there are positions $i_0 < i_1 < i_2 < i_3$ such that
$\sigma(i_j) < \sigma(i_m)$ for every $m \in \{0, 1, 2, 3\}$ with $m \neq j$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.1 and Table 1.

Formalized by `MetaMathlibExt.ContainsFlatPOPBelow`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#contains-flat-popbelow).

## Containing a flat pattern with one top label

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n - 1\}$ and let $j \in \{0, 1, 2, 3\}$. Then $\sigma$ contains the flat partially
ordered pattern $Q_{j+1}$ of size $4$, in which label $j + 1$ lies above the other three labels,
if there are positions $i_0 < i_1 < i_2 < i_3$ such that $\sigma(i_m) < \sigma(i_j)$ for every
$m \in \{0, 1, 2, 3\}$ with $m \neq j$.

The pattern $Q_k$ is the complement of the pattern $P_k$ of Table 1, in which label $k$ lies
below the other three labels.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.1 and Table 1.

Formalized by `MetaMathlibExt.ContainsFlatPOPAbove`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#contains-flat-popabove).

## Containing $P_{j+1}$ forces length at least $4$

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n - 1\}$ and let $j \in \{0, 1, 2, 3\}$. If $\sigma$ contains the flat partially
ordered pattern $P_{j+1}$ of size $4$, in which label $j + 1$ lies below the other three labels,
then $n \ge 4$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.1.

Formalized by `MetaMathlibExt.four_le_of_containsFlatPOPBelow`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#four-le-of-contains-flat-popbelow).

## Containing $Q_{j+1}$ forces length at least $4$

Let $\sigma$ be a permutation of
$\{0, 1, \dots, n - 1\}$ and let $j \in \{0, 1, 2, 3\}$. If $\sigma$ contains the flat partially
ordered pattern $Q_{j+1}$ of size $4$, in which label $j + 1$ lies above the other three labels,
then $n \ge 4$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.1.

Formalized by `MetaMathlibExt.four_le_of_containsFlatPOPAbove`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#four-le-of-contains-flat-popabove).

## Generating function of king permutations avoiding $P_{j+1}$

For $j \in \{0, 1, 2, 3\}$
let $P_{j+1}$ be the flat partially ordered pattern of length $4$ whose element number $j + 1$
lies below each of the other three: a permutation $\sigma$ contains $P_{j+1}$ if there are
positions $i_0 < i_1 < i_2 < i_3$ with $\sigma(i_j) < \sigma(i_m)$ for every $m \ne j$. A king
permutation is one in which adjacent entries never differ by exactly $1$; let $K_n(P_{j+1})$ be
the set of king permutations of length $n$ that do not contain $P_{j+1}$. The generating function
$A_{P_{j+1}}$ is the formal power series in $x$ with coefficients in $\mathbb{Z}[p, q, u, v]$

$$
A_{P_{j+1}}(x; p, q, u, v) = \sum_{n \ge 0} \sum_{\sigma \in K_n(P_{j+1})}
x^n p^{\operatorname{asc}(\sigma)} q^{\operatorname{des}(\sigma)}
u^{\operatorname{lmax}(\sigma)} v^{\operatorname{rmax}(\sigma)},
$$

where $\operatorname{asc}$, $\operatorname{des}$, $\operatorname{lmax}$ and $\operatorname{rmax}$
count ascents, descents, left-to-right maxima and right-to-left maxima.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.4.

Formalized by `MetaMathlibExt.kingFlatPOPBelowGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popbelow-gf).

## Generating function of king permutations avoiding $Q_{j+1}$

For $j \in \{0, 1, 2, 3\}$
let $Q_{j+1}$ be the flat partially ordered pattern of length $4$ whose element number $j + 1$
lies above each of the other three: a permutation $\sigma$ contains $Q_{j+1}$ if there are
positions $i_0 < i_1 < i_2 < i_3$ with $\sigma(i_m) < \sigma(i_j)$ for every $m \ne j$. A king
permutation is one in which adjacent entries never differ by exactly $1$; let $K_n(Q_{j+1})$ be
the set of king permutations of length $n$ that do not contain $Q_{j+1}$. The generating function
$\bar A_{Q_{j+1}}$ is the formal power series in $x$ with coefficients in $\mathbb{Z}[p, q, s, t]$

$$
\bar A_{Q_{j+1}}(x; p, q, s, t) = \sum_{n \ge 0} \sum_{\sigma \in K_n(Q_{j+1})}
x^n p^{\operatorname{asc}(\sigma)} q^{\operatorname{des}(\sigma)}
s^{\operatorname{lmin}(\sigma)} t^{\operatorname{rmin}(\sigma)},
$$

where $\operatorname{asc}$, $\operatorname{des}$, $\operatorname{lmin}$ and $\operatorname{rmin}$
count ascents, descents, left-to-right minima and right-to-left minima.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.4.

Formalized by `MetaMathlibExt.kingFlatPOPAboveGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popabove-gf).

## Constant term of $A_{P_{j+1}}$

For every $j \in \{0, 1, 2, 3\}$, the coefficient of $x^0$
in the generating function $A_{P_{j+1}}(x; p, q, u, v)$ of king permutations avoiding the flat
partially ordered pattern $P_{j+1}$ is the constant polynomial $1$.

The empty permutation is the only permutation of length $0$; it is a king permutation, it avoids
$P_{j+1}$, and it has no ascents, descents, left-to-right maxima or right-to-left maxima.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.4 and proof of Theorem 3.

Formalized by `MetaMathlibExt.constantCoeff_kingFlatPOPBelowGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#constant-coeff-king-flat-popbelow-gf).

## Constant term of $\bar A_{Q_{j+1}}$

For every $j \in \{0, 1, 2, 3\}$, the coefficient of
$x^0$ in the generating function $\bar A_{Q_{j+1}}(x; p, q, s, t)$ of king permutations avoiding
the flat partially ordered pattern $Q_{j+1}$ is the constant polynomial $1$.

The empty permutation is the only permutation of length $0$; it is a king permutation, it avoids
$Q_{j+1}$, and it has no ascents, descents, left-to-right minima or right-to-left minima.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Section 1.4 and proof of Theorem 3.

Formalized by `MetaMathlibExt.constantCoeff_kingFlatPOPAboveGF`, a theorem declared in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#constant-coeff-king-flat-popabove-gf).

## Rational generating function for king permutations avoiding $P_1$

Let $P_1$ be the flat
partially ordered pattern of length $4$ whose first element lies below each of the other three,
and let $A_{P_1}(x; p, q, u, v)$ be the generating function of king permutations avoiding $P_1$,
in which $x$ marks length and $p$, $q$, $u$, $v$ mark ascents, descents, left-to-right maxima and
right-to-left maxima. Then $B \cdot A_{P_1} = A$ in $\mathbb{Z}[p, q, u, v][[x]]$, where
$A = \sum_{k=0}^{7} a_k x^k$ and $B = \sum_{k=0}^{7} b_k x^k$ with $a_0 = b_0 = -1$, $a_1 = -uv$,
$b_1 = 0$, $a_2 = b_2 = pqv$, $a_3 = pq^2v + pquv^2$, $b_3 = pq^2v$,
$a_4 = p^2q^2v^2 + pq^3v^2 + pq^2uv^2 - p^2qu^2v^2 - pq^2u^2v^2$, $b_4 = p^2q^2v^2 + pq^3v^2$,
$a_5 = p^2q^3v^2 - p^2q^2u^2v^2 + 2p^2q^3v^3 + pq^4v^3 - 2p^2q^2u^2v^3 - pq^3u^2v^3$,
$b_5 = p^2q^3v^2 + 2p^2q^3v^3 + pq^4v^3$,
$a_6 = 2p^2q^4v^3 - 2p^2q^3u^2v^3 + p^2q^4v^4 - p^2q^3u^2v^4$, $b_6 = 2p^2q^4v^3 + p^2q^4v^4$,
$a_7 = p^2q^5v^4 - p^2q^4u^2v^4$ and $b_7 = p^2q^5v^4$. Since $B$ has constant term $-1$, this
determines $A_{P_1} = A / B$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Theorem 3.

Stated but not proved: `MetaMathlibExt.kingFlatPOPBelowGF_zero_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popbelow-gf-zero-eq).

## Rational generating function for king permutations avoiding $P_2$

Let $P_2$ be the flat
partially ordered pattern of length $4$ whose second element lies below each of the other three,
and let $A_{P_2}(x; p, q, u, v)$ be the generating function of king permutations avoiding $P_2$,
in which $x$ marks length and $p$, $q$, $u$, $v$ mark ascents, descents, left-to-right maxima and
right-to-left maxima. Then $B \cdot A_{P_2} = A$ in $\mathbb{Z}[p, q, u, v][[x]]$, where
$A = \sum_{k=0}^{6} a_k x^k$ and $B = \sum_{k=0}^{6} b_k x^k$ with $a_0 = b_0 = -1$, $a_1 = -uv$,
$b_1 = 0$, $a_2 = b_2 = pqu + pquv$, $a_3 = p^2quv + pqu^2v + pqu^2v^2$, $b_3 = p^2quv$,
$a_4 = b_4 = p^2q^2uv + p^3qu^2v - p^2q^2u^2v + p^2q^2uv^2$,
$a_5 = p^3q^2u^2v + p^2q^3uv^2 + p^3q^2u^2v^2 - p^2q^2u^3v^2$,
$b_5 = p^3q^2u^2v + p^2q^3uv^2 + p^3q^2u^2v^2$ and $a_6 = b_6 = p^3q^3u^2v^2$. Since $B$ has
constant term $-1$, this determines $A_{P_2} = A / B$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Theorem 4.

Stated but not proved: `MetaMathlibExt.kingFlatPOPBelowGF_one_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popbelow-gf-one-eq).

## The generating functions for $P_4$ and $P_1$ differ by a change of variables

For $k = 1$
and $k = 4$ let $P_k$ be the flat partially ordered pattern of length $4$ whose $k$-th element lies
below each of the other three, and let $A_{P_k}(x; p, q, u, v)$ be the generating function of king
permutations avoiding $P_k$, in which $x$ marks length and $p$, $q$, $u$, $v$ mark ascents,
descents, left-to-right maxima and right-to-left maxima. Then
$A_{P_4}(x; p, q, u, v) = A_{P_1}(x; q, p, v, u)$: the series $A_{P_4}$ is obtained from
$A_{P_1}$ by exchanging $p$ with $q$ and $u$ with $v$ in every coefficient.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Corollary 1.

Stated but not proved: `MetaMathlibExt.kingFlatPOPBelowGF_three_eq_rename` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popbelow-gf-three-eq-rename).

## The generating functions for $Q_1$ and $P_1$ differ by a change of variables

Let $P_1$
(respectively $Q_1$) be the flat partially ordered pattern of length $4$ whose first element lies
below (respectively above) each of the other three. Let $A_{P_1}(x; p, q, u, v)$ be the
generating function of king permutations avoiding $P_1$, in which $x$ marks length and $p$, $q$,
$u$, $v$ mark ascents, descents, left-to-right maxima and right-to-left maxima, and let
$\bar A_{Q_1}(x; p, q, s, t)$ be the generating function of king permutations avoiding $Q_1$, in
which $s$ and $t$ mark left-to-right minima and right-to-left minima instead. Then
$\bar A_{Q_1}(x; p, q, s, t) = A_{P_1}(x; q, p, s, t)$: the series $\bar A_{Q_1}$ is obtained
from $A_{P_1}$ by exchanging $p$ with $q$ in every coefficient and writing $s$, $t$ for $u$, $v$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Corollary 2.

Stated but not proved: `MetaMathlibExt.kingFlatPOPAboveGF_zero_eq_rename` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popabove-gf-zero-eq-rename).

## The king generating function avoiding $Q_4$

Let $A_{P_1}(x, p, q, u, v)$ be the
generating function of king permutations avoiding the flat pattern $P_1$ (label $1$ below labels
$2, 3, 4$), where $x, p, q, u, v$ mark length, ascents, descents, left-to-right maxima and
right-to-left maxima, and let $\bar A_{Q_4}(x, p, q, s, t)$ be the generating function of king
permutations avoiding the flat pattern $Q_4$ (label $4$ above labels $1, 2, 3$), where
$x, p, q, s, t$ mark length, ascents, descents, left-to-right minima and right-to-left minima.
Then $\bar A_{Q_4}(x, p, q, s, t) = A_{P_1}(x, p, q, t, s)$: the coefficient of each power of $x$
in $\bar A_{Q_4}$ is obtained from the corresponding coefficient of $A_{P_1}$ by exchanging the
last two variables.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Corollary 3.

Stated but not proved: `MetaMathlibExt.kingFlatPOPAboveGF_three_eq_rename` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popabove-gf-three-eq-rename).

## The generating functions for $P_3$ and $P_2$ differ by a change of variables

For $k = 2$
and $k = 3$ let $P_k$ be the flat partially ordered pattern of length $4$ whose $k$-th element lies
below each of the other three, and let $A_{P_k}(x; p, q, u, v)$ be the generating function of king
permutations avoiding $P_k$, in which $x$ marks length and $p$, $q$, $u$, $v$ mark ascents,
descents, left-to-right maxima and right-to-left maxima. Then
$A_{P_3}(x; p, q, u, v) = A_{P_2}(x; q, p, v, u)$: the series $A_{P_3}$ is obtained from
$A_{P_2}$ by exchanging $p$ with $q$ and $u$ with $v$ in every coefficient.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Corollary 4.

Stated but not proved: `MetaMathlibExt.kingFlatPOPBelowGF_two_eq_rename` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popbelow-gf-two-eq-rename).

## The king generating function avoiding $Q_2$

Let $A_{P_2}(x, p, q, u, v)$ be the
generating function of king permutations avoiding the flat pattern $P_2$ (label $2$ below labels
$1, 3, 4$), where $x, p, q, u, v$ mark length, ascents, descents, left-to-right maxima and
right-to-left maxima, and let $\bar A_{Q_2}(x, p, q, s, t)$ be the generating function of king
permutations avoiding the flat pattern $Q_2$ (label $2$ above labels $1, 3, 4$), where
$x, p, q, s, t$ mark length, ascents, descents, left-to-right minima and right-to-left minima.
Then $\bar A_{Q_2}(x, p, q, s, t) = A_{P_2}(x, q, p, s, t)$: the coefficient of each power of $x$
in $\bar A_{Q_2}$ is obtained from the corresponding coefficient of $A_{P_2}$ by exchanging $p$
and $q$.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Corollary 5.

Stated but not proved: `MetaMathlibExt.kingFlatPOPAboveGF_one_eq_rename` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popabove-gf-one-eq-rename).

## The king generating function avoiding $Q_3$

Let $A_{P_2}(x, p, q, u, v)$ be the
generating function of king permutations avoiding the flat pattern $P_2$ (label $2$ below labels
$1, 3, 4$), where $x, p, q, u, v$ mark length, ascents, descents, left-to-right maxima and
right-to-left maxima, and let $\bar A_{Q_3}(x, p, q, s, t)$ be the generating function of king
permutations avoiding the flat pattern $Q_3$ (label $3$ above labels $1, 2, 4$), where
$x, p, q, s, t$ mark length, ascents, descents, left-to-right minima and right-to-left minima.
Then $\bar A_{Q_3}(x, p, q, s, t) = A_{P_2}(x, p, q, t, s)$: the coefficient of each power of $x$
in $\bar A_{Q_3}$ is obtained from the corresponding coefficient of $A_{P_2}$ by exchanging the
last two variables.

## Sources

- Dan Li and Sergey Kitaev, *King Permutations and Partially Ordered Patterns*, INTEGERS 26 (2026), Article A59, Corollary 6.

Stated but not proved: `MetaMathlibExt.kingFlatPOPAboveGF_two_eq_rename` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/KingPermutationsWanted.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html#king-flat-popabove-gf-two-eq-rename).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: King permutations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/king-permutations)
