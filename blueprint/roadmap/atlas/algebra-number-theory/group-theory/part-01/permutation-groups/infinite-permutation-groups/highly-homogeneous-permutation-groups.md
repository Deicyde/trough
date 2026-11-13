---
declaration: section
origin: cited
lean: MetaMathlibExt.isBetween, MetaMathlibExt.betweennessAutSubgroup, MetaMathlibExt.circularOrderAutSubgroup, MetaMathlibExt.IsHighlyHomogeneous, MetaMathlibExt.isHighlyHomogeneous_top, MetaMathlibExt.orderAutSubgroup, Equiv.Perm.pointwiseTopology, MetaMathlibExt.CameronBetweennessGroupWanted.betweennessAutSubgroup_isClosed_and_highlyHomogeneous
statement: formalized
proof: formalized
---

# Highly homogeneous permutation groups

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html).

## Strict betweenness

Let $\alpha$ be a type with a relation $<$ and let $a, b, c \in \alpha$.
Then $b$ lies strictly between $a$ and $c$ when either $a < b$ and $b < c$, or $c < b$ and
$b < a$.

Formalized by `MetaMathlibExt.isBetween`, a definition declared in [MathlibExt/GroupTheory/Permutation/Betweenness.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/Betweenness.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#is-between).

## The betweenness automorphism group of a linear order

Let $\alpha$ be a linearly ordered
set, and say that $b$ lies strictly between $a$ and $c$ when $a < b < c$ or $c < b < a$. The
betweenness automorphism group of $\alpha$ is the subgroup of the group of permutations of
$\alpha$ consisting of the permutations $\sigma$ such that, for all $a, b, c \in \alpha$, $b$ lies
strictly between $a$ and $c$ if and only if $\sigma(b)$ lies strictly between $\sigma(a)$ and
$\sigma(c)$.

Formalized by `MetaMathlibExt.betweennessAutSubgroup`, a definition declared in [MathlibExt/GroupTheory/Permutation/Betweenness.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/Betweenness.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#betweenness-aut-subgroup).

## The automorphism group of a circular order

Let $\alpha$ be a circularly ordered set with
non-strict circular betweenness relation $\operatorname{btw}$. The automorphism group of $\alpha$
is the subgroup of the group of permutations of $\alpha$ consisting of the permutations $\sigma$
such that, for all $a, b, c \in \alpha$, $\operatorname{btw}(a, b, c)$ holds if and only if
$\operatorname{btw}(\sigma(a), \sigma(b), \sigma(c))$ holds.

Formalized by `MetaMathlibExt.circularOrderAutSubgroup`, a definition declared in [MathlibExt/GroupTheory/Permutation/CircularOrder.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/CircularOrder.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#circular-order-aut-subgroup).

## Highly homogeneous permutation groups

Let $G$ be a group of permutations of a set
$\alpha$. Then $G$ is highly homogeneous when, for every natural number $k$, it acts transitively
on the $k$-element subsets of $\alpha$: for any two $k$-element subsets $X$ and $Y$ of $\alpha$
there is some $g \in G$ with $g(X) = Y$.

Formalized by `MetaMathlibExt.IsHighlyHomogeneous`, a definition declared in [MathlibExt/GroupTheory/Permutation/HighlyHomogeneous.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/HighlyHomogeneous.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#is-highly-homogeneous).

## The full symmetric group is highly homogeneous

For every set $\alpha$, the group of all
permutations of $\alpha$ is highly homogeneous: for every natural number $k$, any $k$-element
subset of $\alpha$ can be carried to any other $k$-element subset of $\alpha$ by some permutation
of $\alpha$.

Formalized by `MetaMathlibExt.isHighlyHomogeneous_top`, a theorem declared in [MathlibExt/GroupTheory/Permutation/HighlyHomogeneous.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/HighlyHomogeneous.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#is-highly-homogeneous-top).

## Order automorphism group

For a type $\alpha$ equipped with a relation $<$, the order
automorphism group of $\alpha$ is the subgroup of the group of permutations of $\alpha$
consisting of the permutations $\sigma$ such that for all $a, b \in \alpha$, $a < b$ holds if and
only if $\sigma(a) < \sigma(b)$ holds.

Formalized by `MetaMathlibExt.orderAutSubgroup`, a definition declared in [MathlibExt/GroupTheory/Permutation/Order.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/Order.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#order-aut-subgroup).

## Pointwise convergence topology on permutations

For a type $\alpha$, the pointwise
convergence topology on the group of permutations of $\alpha$ is the topology induced by the map
sending a permutation $\sigma$ to the underlying function $\sigma \colon \alpha \to \alpha$, where
$\alpha$ carries the discrete topology and the space of functions $\alpha \to \alpha$ carries the
product topology.

Formalized by `Equiv.Perm.pointwiseTopology`, an abbreviation declared in [MathlibExt/GroupTheory/Permutation/PointwiseTopology.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/PointwiseTopology.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#pointwise-topology).

## The betweenness group of the rationals is closed and highly homogeneous

Let $G$ be the
group of permutations $\sigma$ of $\mathbb{Q}$ preserving strict betweenness in both directions:
for all $a, b, c \in \mathbb{Q}$, $b$ lies strictly between $a$ and $c$ (that is, $a < b < c$ or
$c < b < a$) if and only if $\sigma(b)$ lies strictly between $\sigma(a)$ and $\sigma(c)$. Then
$G$ is closed in the topology of pointwise convergence on the permutations of $\mathbb{Q}$, where
$\mathbb{Q}$ carries the discrete topology, and $G$ is highly homogeneous: for every natural
number $k$ it has a single orbit on the $k$-element subsets of $\mathbb{Q}$.

## Sources

- Daniele A. Gewurz and Francesca Merola, "Sequences realized as Parker vectors of oligomorphic permutation groups," Journal of Integer Sequences 6, <https://cs.uwaterloo.ca/journals/JIS/VOL6/Gewurz/gewurz22.tex>, lines 331–359. The source identifies `B` (also `∂C*`) as the rational-order permutations preserving or reversing order and calls Cameron's five representatives closed and highly homogeneous, glossed as one orbit on `k`-sets for all `k`. The source cites Peter J. Cameron, "Transitivity of permutation groups on unordered sets," Math. Z. 148 (1976), 127–139. Interpretation boundary: only the `B` representative is asserted, not exhaustive classification, uniqueness, or conjugacy.

Formalized by `MetaMathlibExt.CameronBetweennessGroupWanted.betweennessAutSubgroup_isClosed_and_highlyHomogeneous`, a theorem declared in [MathlibExt/GroupTheory/Permutation/CameronBetweennessGroup.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/CameronBetweennessGroup.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#betweenness-aut-subgroup-is-closed-and-h).

## The automorphism group of a countably infinite dense circular order is closed and highly homogeneous

**The automorphism group of a countably infinite dense circular order is closed and highly
homogeneous.** Let $\alpha$ be a countably infinite set with a circular order, and write
$\operatorname{btw}(a, b, c)$ when $b$ lies between $a$ and $c$ going around from $a$ to $c$.
Suppose the circular order is dense: for all distinct $a, b \in \alpha$ there is some
$c \in \alpha$, different from $a$ and $b$, with $\operatorname{btw}(a, c, b)$. Then the group of
permutations $\sigma$ of $\alpha$ such that $\operatorname{btw}(a, b, c)$ holds if and only if
$\operatorname{btw}(\sigma(a), \sigma(b), \sigma(c))$ holds, for all $a, b, c \in \alpha$, is
closed in the topology of pointwise convergence on the permutations of $\alpha$, where $\alpha$
carries the discrete topology, and it is highly homogeneous: for every natural number $k$ it has
a single orbit on the $k$-element subsets of $\alpha$.

## Sources

- Daniele A. Gewurz and Francesca Merola, "Sequences realized as Parker vectors of oligomorphic permutation groups," JIS 6, https://cs.uwaterloo.ca/journals/JIS/VOL6/Gewurz/gewurz22.tex, lines 331–359. Interpretation boundary: only Cameron group C is asserted, with standard countable dense infinite circular-order hypotheses, not exhaustive classification, uniqueness, or conjugacy.

Formalized by `MetaMathlibExt.CameronCircularOrderGroupWanted.circularOrderAutSubgroup_isClosed_and_highlyHomogeneous`, a theorem declared in [MathlibExt/GroupTheory/Permutation/CameronCircularOrderGroup.lean, line 659](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/CameronCircularOrderGroup.lean#L659). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#circular-order-aut-subgroup-is-closed-an).

## The order-automorphism group of the rationals is closed and highly homogeneous

The group of
order automorphisms of $\mathbb{Q}$, that is, of the permutations $\sigma$ of $\mathbb{Q}$ such
that $a < b$ if and only if $\sigma(a) < \sigma(b)$ for all $a, b \in \mathbb{Q}$, is closed in
the topology of pointwise convergence on the permutations of $\mathbb{Q}$, where $\mathbb{Q}$
carries the discrete topology, and it is highly homogeneous: for every natural number $k$ it has
a single orbit on the $k$-element subsets of $\mathbb{Q}$.

## Sources

- Daniele A. Gewurz and Francesca Merola, "Sequences realized as Parker vectors of oligomorphic permutation groups," JIS 6, https://cs.uwaterloo.ca/journals/JIS/VOL6/Gewurz/gewurz22.tex, lines 331-359. Primary source, cited there: Peter J. Cameron, "Transitivity of permutation groups on unordered sets," *Mathematische Zeitschrift* 148(2) (1976), 127--139, DOI 10.1007/BF01214702.

Formalized by `MetaMathlibExt.CameronOrderGroupWanted.orderAutSubgroup_isClosed_and_highlyHomogeneous`, a theorem declared in [MathlibExt/GroupTheory/Permutation/CameronOrderGroup.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/CameronOrderGroup.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#order-aut-subgroup-is-closed-and-highly).

## The symmetric group of the rationals is closed and highly homogeneous

Let
$\operatorname{Sym}(\mathbb{Q})$ be the group of all permutations of the set $\mathbb{Q}$. Then
$\operatorname{Sym}(\mathbb{Q})$ is closed in the topology of pointwise convergence on the
permutations of $\mathbb{Q}$, and it is highly homogeneous: for every natural number $k$ it has a
single orbit on the $k$-element subsets of $\mathbb{Q}$.

Here $\mathbb{Q}$ serves only as a countably infinite set; its order, its field structure and its
usual topology play no role.

## Sources

- Daniele A. Gewurz and Francesca Merola, *Sequences realized as Parker vectors of oligomorphic permutation groups*, Journal of Integer Sequences 6, source lines 331--359 at https://cs.uwaterloo.ca/journals/JIS/VOL6/Gewurz/gewurz22.tex. Peter J. Cameron, "Transitivity of permutation groups on unordered sets," *Mathematische Zeitschrift* 148(2) (1976), 127--139, DOI 10.1007/BF01214702. Scope: this proves only Cameron's representative S, not Cameron's exhaustive classification, uniqueness, conjugacy, Parker-sequence claims, or the other four representatives.

Formalized by `MetaMathlibExt.cameron_symmetricGroup_closed_highlyHomogeneous`, a theorem declared in [MathlibExt/GroupTheory/Permutation/CameronSymmetricGroup.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/CameronSymmetricGroup.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#cameron-symmetric-group-closed-highly-ho).

## Separation of pairs in a circular order

Let $\alpha$ be a circular order, and write
$\operatorname{sbtw}(x, y, z)$ for its strict betweenness relation ($y$ lies strictly between
$x$ and $z$ going around the circle). For $a, b, c, d \in \alpha$, the pairs $a, b$ and $c, d$
separate each other when either $\operatorname{sbtw}(a, c, b)$ and $\operatorname{sbtw}(b, d, a)$
both hold, or $\operatorname{sbtw}(a, d, b)$ and $\operatorname{sbtw}(b, c, a)$ both hold.

Formalized by `MetaMathlibExt.circularSeparates`, a definition declared in [MathlibExt/GroupTheory/Permutation/Separation.lean, line 20](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/Separation.lean#L20). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#circular-separates).

## Separation-preserving permutation group

For a circular order $\alpha$, the
separation-preserving group of $\alpha$ is the subgroup of the group of permutations of $\alpha$
consisting of the permutations $\sigma$ such that for all $a, b, c, d \in \alpha$, the pairs
$a, b$ and $c, d$ separate each other if and only if the pairs $\sigma(a), \sigma(b)$ and
$\sigma(c), \sigma(d)$ separate each other.

Formalized by `MetaMathlibExt.separationAutSubgroup`, a definition declared in [MathlibExt/GroupTheory/Permutation/Separation.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/Separation.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#separation-aut-subgroup).

## The separation group of a countably infinite dense circular order is closed and highly homogeneous

**The separation group of a countably infinite dense circular order is closed and highly
homogeneous.** Let $\alpha$ be a countably infinite set with a circular order, and write
$\operatorname{btw}(a, b, c)$ when $b$ lies between $a$ and $c$ going around from $a$ to $c$.
Suppose the circular order is dense: for all distinct $a, b \in \alpha$ there is some
$c \in \alpha$, different from $a$ and $b$, with $\operatorname{btw}(a, c, b)$. Then the
separation automorphism group of $\alpha$ is closed in the topology of pointwise convergence on
the permutations of $\alpha$, where $\alpha$ carries the discrete topology, and it is highly
homogeneous: for every natural number $k$ it has a single orbit on the $k$-element subsets of
$\alpha$.

## Sources

- Daniele A. Gewurz and Francesca Merola, "Sequences realized as Parker vectors of oligomorphic permutation groups," Journal of Integer Sequences 6, <https://cs.uwaterloo.ca/journals/JIS/VOL6/Gewurz/gewurz22.tex>, lines 331–359. The source identifies `D` (also `C*`) as the cyclic-order permutations preserving or reversing the order and calls Cameron's five representatives closed and highly homogeneous, glossed as one orbit on `k`-sets for all `k`. The source cites Peter J. Cameron, "Transitivity of permutation groups on unordered sets," Math. Z. 148 (1976), 127–139. Interpretation boundary: only the `D` representative is asserted, not exhaustive classification, uniqueness, or conjugacy. The explicit countability, infinitude, and circular-density hypotheses select the intended countable dense circular order.

Formalized by `MetaMathlibExt.CameronSeparationGroupWanted.separationAutSubgroup_isClosed_and_highlyHomogeneous`, a theorem declared in [MathlibExt/GroupTheory/Permutation/CameronSeparationGroup.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/Permutation/CameronSeparationGroup.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html#separation-aut-subgroup-is-closed-and-hi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Highly homogeneous permutation groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/highly-homogeneous-permutation-groups)
