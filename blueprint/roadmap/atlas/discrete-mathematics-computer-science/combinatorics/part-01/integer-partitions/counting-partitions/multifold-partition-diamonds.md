---
declaration: section
origin: cited
lean: MetaMathlibExt.permValueAt, MetaMathlibExt.permDescentSet, MetaMathlibExt.permDes, MetaMathlibExt.permMaj, MetaMathlibExt.eulerMahonian, MetaMathlibExt.eulerMahonian_one, MetaMathlibExt.eulerMahonian_three_two_three, MetaMathlibExt.card_perm_three_des_one_maj_one
statement: formalized
---

# Multifold partition diamonds

21 results, 17 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html).

## Value of a permutation at a natural position

For a permutation $\tau$ of
$\{0, 1, \dots, d - 1\}$ and a natural number $j$, this is the natural number $\tau(j)$ when
$j < d$, and $0$ when $j \ge d$. It is used to read off descents.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1 (descent statistics).

Formalized by `MetaMathlibExt.permValueAt`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#perm-value-at).

## Descent set of a permutation

For a permutation $\tau$ of $\{0, 1, \dots, d - 1\}$, the
descent set is $\mathrm{Des}(\tau) = \{p \in \{1, \dots, d - 1\} : \tau(p - 1) > \tau(p)\}$. If
$\tau$ is read as the permutation $p \mapsto \tau(p - 1) + 1$ of $\{1, \dots, d\}$, this is the
usual descent set: the positions $p$, numbered from $1$, where the value at $p$ exceeds the
value at $p + 1$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1.

Formalized by `MetaMathlibExt.permDescentSet`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#perm-descent-set).

## Number of descents from the descent set

For a permutation $\tau$ of
$\{0, 1, \dots, d - 1\}$, the number of descents $\mathrm{des}(\tau) = |\mathrm{Des}(\tau)|$ is the
number of elements of the descent set $\mathrm{Des}(\tau)$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1.

Formalized by `MetaMathlibExt.permDes`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#perm-des).

## Major index of a permutation

For a permutation $\tau$ of $\{0, 1, \dots, d - 1\}$, the
major index is $\mathrm{maj}(\tau) = \sum_{p \in \mathrm{Des}(\tau)} p$, the sum of the
positions, numbered from $1$, in the descent set $\mathrm{Des}(\tau)$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1.

Formalized by `MetaMathlibExt.permMaj`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#perm-maj).

## Euler–Mahonian polynomial

For a natural number $d$ and elements $x, y$ of a commutative
ring, the Euler–Mahonian polynomial evaluated at $(x, y)$ is
$E_d(x, y) = \sum_{\tau \in S_d} x^{\operatorname{des}(\tau)} y^{\operatorname{maj}(\tau)}$,
where $\operatorname{des}(\tau)$ is the number of descents and $\operatorname{maj}(\tau)$ the
major index of the permutation $\tau$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1.

Formalized by `MetaMathlibExt.eulerMahonian`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#euler-mahonian).

## The first Euler–Mahonian polynomial is $1$

For every commutative ring $R$ and all
$x, y \in R$, the Euler–Mahonian polynomial $E_1$ satisfies $E_1(x, y) = 1$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1 (`F_1 = 1` in recursion (1)).

Formalized by `MetaMathlibExt.eulerMahonian_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#euler-mahonian-one).

## Euler–Mahonian polynomial $E_3$ at $(2, 3)$

Over the integers, the Euler–Mahonian
polynomial $E_3$ takes the value $E_3(2, 3) = 157$.

This agrees with $E_3(x, y) = 1 + 2xy + 2xy^2 + x^2y^3$: the six permutations of $S_3$ have
$(\operatorname{des}, \operatorname{maj})$ equal to $(0, 0)$, $(1, 1)$, $(1, 1)$, $(1, 2)$,
$(1, 2)$ and $(2, 3)$. Only the value at $x = 2$, $y = 3$ is checked, not the polynomial
identity.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1.

Formalized by `MetaMathlibExt.eulerMahonian_three_two_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#euler-mahonian-three-two-three).

## Permutations of $S_3$ with descent set $\{1\}$

Exactly two permutations $\tau \in S_3$
have exactly one descent and major index $1$, that is, $\operatorname{des}(\tau) = 1$ and
$\operatorname{maj}(\tau) = 1$; equivalently, their descent set is $\{1\}$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 1.

Formalized by `MetaMathlibExt.card_perm_three_des_one_maj_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#card-perm-three-des-one-maj-one).

## Position of the $k$th link of a multifold partition diamond

For natural numbers
$d_1, \dots, d_M$ (the numbers of folds of the $M$ diamonds) and a natural number $k$, the
position of the $k$th link, counting positions from $0$, is
$L_k = \sum_{m=1}^{\min(k, M)} (d_m + 1)$. In particular $L_0 = 0$, and
$L_k = d_1 + \dots + d_M + M$ for every $k \ge M$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Figure 3 and Section 3.

Formalized by `MetaMathlibExt.diamondLinkPos`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#diamond-link-pos).

## Number of parts of a multifold partition diamond

The multifold partition diamond whose
$M$ diamonds have $d_1, \dots, d_M$ folds has $c = d_1 + \dots + d_M + M + 1$ parts.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Figure 3 (`c = M(d + 1) + 1`).

Formalized by `MetaMathlibExt.diamondSize`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#diamond-size).

## The set of link positions of a multifold partition diamond

For natural numbers
$d_1, \dots, d_M$, the set of link positions is $\{L_0, L_1, \dots, L_M\}$, where
$L_k = \sum_{m=1}^{k} (d_m + 1)$ is the position of the $k$th link. These positions satisfy
$0 = L_0 < L_1 < \dots < L_M = c - 1$, where $c = d_1 + \dots + d_M + M + 1$ is the number of
parts.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Figure 3.

Formalized by `MetaMathlibExt.diamondLinks`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#diamond-links).

## Multifold partition diamonds with given fold and link sums

Let $d_1, \dots, d_M$ be
natural numbers, let $L_k = \sum_{m=1}^{k} (d_m + 1)$ for $0 \le k \le M$ be the link
positions, let $c = L_M + 1$, and let $i$ and $j$ be natural numbers. A function
$b : \mathbb{N} \to \mathbb{N}$ is a multifold partition diamond with fold sum $i$ and link sum
$j$ when the following hold: for every $k$ with $0 \le k < M$ and every $f$ with
$1 \le f \le d_{k+1}$, we have $b(L_k) \le b(L_k + f) \le b(L_{k+1})$; the sum of $b(p)$ over
the positions $p < c$ different from $L_0, \dots, L_M$ is $i$; and
$b(L_0) + \dots + b(L_M) = j$.

This models the paper's $P$-partitions (order-preserving maps to $\mathbb{Z}_{\ge 0}$) of the
poset in which, for each $k < M$, the folds at positions $L_k + 1, \dots, L_k + d_{k+1}$ lie
above the link at $L_k$ and below the link at $L_{k+1}$. In particular, when every
$d_k \ge 1$, $b(0)$ is the smallest of $b(0), \dots, b(c - 1)$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Sections 2-3.

Formalized by `MetaMathlibExt.IsMultifoldDiamond`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#is-multifold-diamond).

## Extending a part vector by zero

Let $c = d_1 + \dots + d_M + M + 1$ be the number of
parts of the multifold partition diamond whose diamonds have $d_1, \dots, d_M$ folds, and let
$n$ be a natural number. A vector $(a_0, \dots, a_{c-1})$ with entries in $\{0, \dots, n - 1\}$
is read as the function $\mathbb{N} \to \mathbb{N}$ that sends $p$ to $a_p$ for $p < c$ and to
$0$ for $p \ge c$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Section 2.

Formalized by `MetaMathlibExt.diamondPart`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#diamond-part).

## Number of multifold partition diamonds

Let $d_1, \dots, d_M$ be natural numbers. Put
$L_k = \sum_{m=1}^{k} (d_m + 1)$ for $0 \le k \le M$ and $c = L_M + 1$. A multifold partition
diamond of shape $(d_1, \dots, d_M)$ is a sequence $(b_0, \dots, b_{c-1})$ of nonnegative integers
such that $b_{L_{k-1}} \le b_{L_{k-1} + f} \le b_{L_k}$ for all $1 \le k \le M$ and
$1 \le f \le d_k$. The parts $b_{L_0}, \dots, b_{L_M}$ are its links and the other parts are its
folds; its link sum is $\sum_{k=0}^{M} b_{L_k}$ and its fold sum is the sum of its folds. This is
the number of multifold partition diamonds of shape $(d_1, \dots, d_M)$ with fold sum $i$ and
link sum $j$.

Every part of such a diamond is at most $i + j$, so this number is finite.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, equation (2) and Section 3.

Formalized by `MetaMathlibExt.multifoldDiamondCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#multifold-diamond-count).

## Single-fold diamonds with fold sum 1 and link sum 1

There is exactly one multifold
partition diamond of shape $(1)$ with fold sum $1$ and link sum $1$. Equivalently, there is exactly
one triple of nonnegative integers $b_0 \le b_1 \le b_2$ with $b_1 = 1$ and $b_0 + b_2 = 1$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, equation (2).

Formalized by `MetaMathlibExt.multifoldDiamondCount_one_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#multifold-diamond-count-one-one-one).

## Two-fold diamonds with fold sum 1 and link sum 2

There are exactly two multifold
partition diamonds of shape $(2)$ with fold sum $1$ and link sum $2$. Equivalently, there are
exactly two quadruples $(b_0, b_1, b_2, b_3)$ of nonnegative integers with $b_0 \le b_f \le b_3$
for $f = 1, 2$, $b_1 + b_2 = 1$ and $b_0 + b_3 = 2$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, equation (2).

Formalized by `MetaMathlibExt.multifoldDiamondCount_two_one_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#multifold-diamond-count-two-one-two).

## The bivariate series of multifold partition diamonds

For natural numbers
$d_1, \dots, d_M$, $\sigma_{d_1, \dots, d_M}(a, b)$ is the formal power series in
$\mathbb{Z}[[a, b]]$ whose coefficient of $a^i b^j$ is the number of multifold partition diamonds
of shape $(d_1, \dots, d_M)$ with fold sum $i$ and link sum $j$. That is,
$\sigma_{d_1, \dots, d_M}(a, b) = \sum a^{\text{fold sum}} b^{\text{link sum}}$, summed over all
such diamonds. We write $\sigma_{d,M}$ for the case $d_1 = \dots = d_M = d$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, equation (2) and Section 3.

Formalized by `MetaMathlibExt.multifoldDiamondSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#multifold-diamond-series).

## Recursion for the Euler–Mahonian polynomials

For every commutative ring $R$, every
natural number $d \ge 1$ and all $x, y \in R$, the Euler–Mahonian polynomials $E_d$ and
$E_{d+1}$ satisfy

$$(1 - y) E_{d+1}(x, y) = (1 - x y^{d+1}) E_d(x, y) - y (1 - x) E_d(xy, y).$$

Together with $E_1 = 1$, this says that the Euler–Mahonian polynomials are the
Dockery–Jameson–Sellers–Wilson polynomials $F_d$, defined by $F_1 = 1$ and
$F_d(q_0, w) = \bigl((1 - q_0 w^d) F_{d-1}(q_0, w) - w (1 - q_0) F_{d-1}(q_0 w, w)\bigr)/(1 - w)$
for $d \ge 2$: since $1 - w$ is a nonzerodivisor in $\mathbb{Z}[q_0, w]$, the recursion is
stated multiplied by $1 - w$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Theorem 1 with recursion (1).

Stated but not proved: `MetaMathlibExt.eulerMahonian_succ_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#euler-mahonian-succ-recursion).

## Product formula for equal-fold partition diamonds

Let $d$ and $M$ be positive integers.
Let $\sigma_{d,M}(a, b)$ be the generating function of multifold partition diamonds of shape
$(d, \dots, d)$ ($M$ copies), where $a$ marks the fold sum and $b$ marks the link sum, and let
$E_d(x, y) = \sum_{\tau} x^{\mathrm{des}(\tau)} y^{\mathrm{maj}(\tau)}$ be the Euler–Mahonian
polynomial, summed over the permutations $\tau$ of $\{1, \dots, d\}$. Then the following
identity holds in $\mathbb{Z}[[a, b]]$:

$$\left(1 - a^{Md} b^{M+1}\right) \prod_{n=1}^{M} \prod_{j=0}^{d} \left(1 - a^{nd-j} b^{n}\right)
\cdot \sigma_{d,M}(a, b) = \prod_{n=1}^{M} E_d\left(a^{(n-1)d} b^{n}, a\right).$$

Equivalently, $\sigma_{d,M}(a, b)$ is the product of the $E_d(a^{(n-1)d} b^n, a)$ divided by
$(1 - a^{Md} b^{M+1}) \prod_{n=1}^{M} \prod_{j=0}^{d} (1 - a^{nd-j} b^n)$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Theorem 2.

Stated but not proved: `MetaMathlibExt.partitionDiamond_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#partition-diamond-gen-fun).

## Product formula for multifold partition diamonds

Let $d_1, \dots, d_M$ be positive
integers with $M \ge 1$, and let $\omega_k = \sum_{m=k+1}^{M} d_m$ for $0 \le k \le M$. Let
$\sigma_{d_1, \dots, d_M}(a, b)$ be the generating function of multifold partition diamonds of
shape $(d_1, \dots, d_M)$, where $a$ marks the fold sum and $b$ marks the link sum, and let
$E_d(x, y) = \sum_{\tau} x^{\mathrm{des}(\tau)} y^{\mathrm{maj}(\tau)}$ be the Euler–Mahonian
polynomial, summed over the permutations $\tau$ of $\{1, \dots, d\}$. Then the following
identity holds in $\mathbb{Z}[[a, b]]$:

$$\left(1 - a^{\omega_0} b^{M+1}\right) \prod_{k=1}^{M} \prod_{j=0}^{d_k}
\left(1 - a^{\omega_k + d_k - j} b^{M-k+1}\right) \cdot \sigma_{d_1, \dots, d_M}(a, b) =
\prod_{k=1}^{M} E_{d_k}\left(a^{\omega_k} b^{M-k+1}, a\right).$$

The $k$th diamond (with $d_k$ folds) is the $k$th from the smallest part, as in the paper's poset
$\{1\} \oplus Q_{d_1} \oplus \dots \oplus Q_{d_M}$. If the parts are read in the opposite order,
the formula holds only for the reversed sequence: for $(d_1, d_2) = (1, 2)$ the coefficient of
$ab$ would be $1$, not $2$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Theorem 3.

Stated but not proved: `MetaMathlibExt.multifoldPartitionDiamond_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#multifold-partition-diamond-gen-fun).

## Generating function of Schmidt type $d$-fold partition diamonds

Let $d \ge 1$. A Schmidt
type $d$-fold partition diamond is a finitely supported sequence $(a_p)_{p \ge 0}$ of natural
numbers such that $a_{k(d+1)} \ge a_{k(d+1)+f} \ge a_{(k+1)(d+1)}$ for all $k \ge 0$ and all
$f$ with $1 \le f \le d$; its weight is the sum of its links $a_{k(d+1)}$, $k \ge 0$. Let
$s_d(w)$ be the number of such diamonds of weight $w$, and let
$S_d(q) = \sum_{w \ge 0} s_d(w) q^w \in \mathbb{Z}[[q]]$. Then for all natural numbers $n \le N$,
the coefficient of $q^n$ in $S_d(q) \prod_{m=1}^{N} (1 - q^m)^{d+1}$ equals the coefficient of
$q^n$ in $\prod_{m=1}^{N} E_d(q^m, 1)$, where $E_d$ is the Euler–Mahonian polynomial.

Since every factor $E_d(q^m, 1)/(1 - q^m)^{d+1}$ with $m > N$ is $1$ modulo $q^{N+1}$, the
statement for all $N$ is equivalent to $S_d(q) = \prod_{m \ge 1} E_d(q^m, 1)/(1 - q^m)^{d+1}$.

## Sources

- Matthias Beck and Kobe Wijesekera, *MacMahon's Double Vision: Partition Diamonds Revisited*, INTEGERS 26 (2026), Article A13, Corollary 1, quoting Dockery-Jameson-Sellers-Wilson.

Stated but not proved: `MetaMathlibExt.schmidtPartitionDiamond_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/PartitionDiamondsEulerMahonianWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html#schmidt-partition-diamond-gen-fun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multifold partition diamonds](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/multifold-partition-diamonds)
