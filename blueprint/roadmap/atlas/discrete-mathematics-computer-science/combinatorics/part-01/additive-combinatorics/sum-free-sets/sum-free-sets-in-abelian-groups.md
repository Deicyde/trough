---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSumFreeSet, MetaMathlibExt.IsDistinctSumFreeSet, MetaMathlibExt.IsSumFreeSet.isDistinctSumFreeSet, MetaMathlibExt.isSumFreeSet_empty, MetaMathlibExt.largestSumFreeCard, MetaMathlibExt.largestSumFreeCard_le, MetaMathlibExt.maxSumFreeCount, MetaMathlibExt.maxDistinctSumFreeCount
statement: formalized
---

# Sum-free sets in abelian groups

31 results, 16 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html).

## Sum-free set

Let $G$ be a set with an addition. A subset $S \subseteq G$ is sum-free if
$x + y \notin S$ for all $x, y \in S$, where $x = y$ is allowed; that is, $S$ contains no Schur
triple $x + y = z$ with $x, y, z \in S$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction.

Formalized by `MetaMathlibExt.IsSumFreeSet`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-sum-free-set).

## Distinct sum-free sets

Let $G$ be a set with an addition. A subset $S \subseteq G$ is
distinct sum-free if there are no pairwise distinct $x, y, z \in S$ with $x + y = z$, that is, if
$S$ contains no distinct Schur triple.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction.

Formalized by `MetaMathlibExt.IsDistinctSumFreeSet`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-distinct-sum-free-set).

## Sum-free sets are distinct sum-free

For every set $G$ with an addition, every sum-free
subset of $G$ is distinct sum-free.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction.

Formalized by `MetaMathlibExt.IsSumFreeSet.isDistinctSumFreeSet`, a theorem declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-distinct-sum-free-set-2).

## The empty set is sum-free

For every set $G$ with an addition, the empty subset of $G$ is
sum-free.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction.

Formalized by `MetaMathlibExt.isSumFreeSet_empty`, a theorem declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-sum-free-set-empty).

## Size of a largest sum-free subset

Let $G$ be a set with an addition and $S \subseteq G$.
Write $\mu(S)$ for the supremum in $\mathbb{N}$ of the sizes of the finite sum-free subsets of
$S$ (sets $T$ with $x + y \notin T$ for all $x, y \in T$), taken to be $0$ if these sizes are
unbounded. For finite $S$ this is the largest size of a sum-free subset of $S$, and $\mu(G)$ is
the value for $S = G$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction (`μ(G)`) and Theorem 2.

Formalized by `MetaMathlibExt.largestSumFreeCard`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#largest-sum-free-card).

## Trivial bound on sum-free subsets

Let $G$ be a set with an addition. For every finite
subset $S \subseteq G$, the largest size of a sum-free subset of $S$ is at most $|S|$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction.

Formalized by `MetaMathlibExt.largestSumFreeCard_le`, a theorem declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#largest-sum-free-card-le).

## Number of maximal sum-free sets

For a set $G$ with an addition, $f_{\max}(G)$ is the
number of maximal sum-free subsets of $G$, that is, of sets $S \subseteq G$ with $x + y \notin S$
for all $x, y \in S$ (including $x = y$) that are not properly contained in another such set;
it is $0$ if there are infinitely many.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction.

Formalized by `MetaMathlibExt.maxSumFreeCount`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-sum-free-count).

## Number of maximal distinct sum-free sets

Let $G$ be a set with an addition. The number
$f^*_{\max}(G)$ is the number of subsets of $G$ that are maximal, with respect to inclusion, among
the distinct sum-free subsets of $G$, and it is $0$ if there are infinitely many such subsets.
Here $S \subseteq G$ is distinct sum-free if $x + y \notin S$ for all $x, y \in S$ such that $x$,
$y$ and $x + y$ are pairwise distinct.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, section "Maximal distinct sum-free subsets".

Formalized by `MetaMathlibExt.maxDistinctSumFreeCount`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-distinct-sum-free-count).

## Number of distinct Schur triples

For a subset $F$ of a set $G$ with an addition, this is
the number of ordered pairs $(x, y)$ with $x, y \in F$ such that $x$, $y$ and $x + y$ are pairwise
distinct and $x + y \in F$, that is, the number of ordered distinct Schur triples $(x, y, x + y)$
in $F$. If there are infinitely many such pairs, the value is $0$ by convention.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, introduction and Lemma 1.

Formalized by `MetaMathlibExt.distinctSchurTripleCount`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#distinct-schur-triple-count).

## Groups of type I(p)

Let $G$ be a finite set and $p$ a natural number. $G$ is of type
$\mathrm{I}(p)$ if $p$ is the smallest prime with $p \equiv 2 \pmod 3$ dividing $|G|$: that is,
$p$ is prime, $p \equiv 2 \pmod 3$, $p$ divides $|G|$, and $p \le q$ for every prime $q$ with
$q \equiv 2 \pmod 3$ that divides $|G|$.

Only the order of $G$ is used; in the paper $G$ is a finite abelian group.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Definition 1.

Formalized by `MetaMathlibExt.IsTypeOneGroup`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-type-one-group).

## Characterization of type I(p)

Let $G$ be a finite set and $p$ a natural number. Then $G$
is of type $\mathrm{I}(p)$ if and only if $p$ is prime, $p \equiv 2 \pmod 3$, $p$ divides $|G|$,
and $p \le q$ for every prime $q$ with $q \equiv 2 \pmod 3$ that divides $|G|$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Definition 1.

Formalized by `MetaMathlibExt.isTypeOneGroup_iff`, a theorem declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-type-one-group-iff).

## Diananda–Yap and Green–Ruzsa theorem

Let $G$ be a finite abelian group of order $n$, and
let $\mu(G)$ be the largest size of a sum-free subset of $G$. If $G$ is of type $\mathrm{I}(p)$
for a natural number $p$, then $\mu(G) = n\left(\frac{1}{3} + \frac{1}{3p}\right)$. If no prime
$q \equiv 2 \pmod 3$ divides $n$ and $3 \mid n$ (type $\mathrm{II}$), then $\mu(G) = n/3$. If no
prime $q \equiv 2 \pmod 3$ divides $n$ and $3 \nmid n$ (type $\mathrm{III}$), then
$\mu(G) = n\left(\frac{1}{3} - \frac{1}{3m}\right)$, where $m$ is the exponent of $G$.

The paper quotes this result from Diananda–Yap and Green–Ruzsa.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Theorem 1, with Definition 1.

Stated but not proved: `MetaMathlibExt.largestSumFreeCard_univ_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#largest-sum-free-card-univ-eq).

## Number of maximal independent sets

For a graph $\Gamma$, $\mathrm{mis}(\Gamma)$ is the
number of maximal independent sets of $\Gamma$, that is, of sets of pairwise non-adjacent
vertices that are not properly contained in another such set; it is $0$ if there are
infinitely many.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, subsection "Maximal independent sets in graphs".

Formalized by `MetaMathlibExt.maxIndepSetCount`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-indep-set-count).

## Edges of the distinct link graph

Let $G$ be a set with an addition and $S \subseteq G$.
Two elements $x, y \in G$ are adjacent in the distinct link graph of $S$ if $x \ne y$ and there
is some $s \in S$, different from both $x$ and $y$, with $x + y = s$, $x + s = y$ or $y + s = x$.
In an abelian group this says exactly that $\{x, y, s\}$ is a distinct Schur triple for some
$s \in S$. In the paper's graph $L^*_S[B]$ with vertex set $B$, these are the edges between
distinct vertices; the relation itself does not depend on $B$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Definition 2 (i).

Formalized by `MetaMathlibExt.DistinctLinkAdj`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#distinct-link-adj).

## Loops of the distinct link graph

Let $G$ be a set with an addition and $S \subseteq G$.
An element $x \in G$ carries a loop in the distinct link graph of $S$ if there are distinct
$s, s' \in S$, both different from $x$, with $s + s' = x$, $x + s = s'$ or $x + s' = s$. In an
abelian group this says exactly that $\{x, s, s'\}$ is a distinct Schur triple for some distinct
$s, s' \in S$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Definition 2 (ii).

Formalized by `MetaMathlibExt.DistinctLinkLoop`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#distinct-link-loop).

## Independent sets of the distinct link graph

Let $G$ be a set with an addition and let
$S, B, I \subseteq G$. The set $I$ is an independent set of the distinct link graph $L^*_S[B]$
(the graph on vertex set $B$ given by the edges and loops of the distinct link graph of $S$) if
$I \subseteq B$, no element of $I$ carries a loop, and no two elements of $I$ are adjacent.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Definition 2.

Formalized by `MetaMathlibExt.IsDistinctLinkIndep`, a definition declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-distinct-link-indep).

## The empty set is independent in the distinct link graph

For every set $G$ with an
addition and all $S, B \subseteq G$, the empty set is an independent set of the distinct link
graph $L^*_S[B]$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Definition 2.

Formalized by `MetaMathlibExt.isDistinctLinkIndep_empty`, a theorem declared in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#is-distinct-link-indep-empty).

## Container lemma

For every real $\delta > 0$ there is a natural number $n_0$ such that
every finite abelian group $G$ of order $n \ge n_0$ has a family $\mathcal{F}$ of subsets of $G$
with the following properties: (i) each $F \in \mathcal{F}$ contains at most $\delta n^2$ ordered
distinct Schur triples $(x, y, x + y)$; (ii) every distinct sum-free subset of $G$ is contained
in some $F \in \mathcal{F}$; (iii) $|\mathcal{F}| \le 2^{\delta n}$; (iv) every
$F \in \mathcal{F}$ is of the form $A \cup B$ with $A$ sum-free and $|B| \le \delta n$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 1.

Stated but not proved: `MetaMathlibExt.exists_distinct_sumFree_containers` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#exists-distinct-sum-free-containers).

## Green–Ruzsa structure lemma

Let $G$ be a finite abelian group of type $\mathrm{I}(p)$ and
let $k$ be a natural number with $p = 3k + 2$. If $A \subseteq G$ is sum-free and
$|A| > \left(\frac{1}{3} + \frac{1}{3(p + 1)}\right)|G|$, then there is a group homomorphism
$\psi : G \to \mathbb{Z}_p$ with $\psi(a) \in \{k + 1, \dots, 2k + 1\}$ for every $a \in A$,
where $\mathbb{Z}_p$ is identified with $\{0, 1, \dots, p - 1\}$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_addMonoidHom_zmod_of_large_sumFree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#exists-add-monoid-hom-zmod-of-large-sum).

## Counting subgroups by order and by index

In a finite abelian group $G$, for every
natural number $k$ the number of subgroups of order $k$ equals the number of subgroups of
index $k$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 3.

Stated but not proved: `MetaMathlibExt.ncard_addSubgroup_card_eq_ncard_index_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#ncard-add-subgroup-card-eq-ncard-index-e).

## Ranks of the index-two subgroups of a finite abelian 2-group

Let $r_1, r_2$ be natural
numbers with $r = r_1 + r_2 \ge 1$, let $\alpha_1, \dots, \alpha_{r_1} \ge 2$, and let
$G = \mathbb{Z}_{2^{\alpha_1}} \oplus \dots \oplus \mathbb{Z}_{2^{\alpha_{r_1}}} \oplus
\mathbb{Z}_2^{r_2}$. Then exactly $2^{r_1} - 1$ subgroups of $G$ of index $2$ have rank $r$,
and exactly $2^r - 2^{r_1}$ subgroups of $G$ of index $2$ have rank $r - 1$, where the rank
of a group is the minimal number of its generators.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 4.

Stated but not proved: `MetaMathlibExt.ncard_index_two_addSubgroup_rank` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#ncard-index-two-add-subgroup-rank).

## Balogh–Liu–Sharifzadeh–Treglown bound

Let $k \ge 1$ be a real number and let $\Gamma$
be a finite graph with $n$ vertices, minimum degree $\delta(\Gamma)$ and maximum degree
$\Delta(\Gamma) \le k\,\delta(\Gamma)$, and put $b = \sqrt{\delta(\Gamma)}$. Then the number
$\mathrm{mis}(\Gamma)$ of maximal independent sets of $\Gamma$ satisfies
$\mathrm{mis}(\Gamma) \le \bigl(\sum_{0 \le i \le n/b} \binom{n}{i}\bigr) \cdot
3^{\frac{k}{k+1} \cdot \frac{n}{3} + \frac{2n}{3b}}$, where $n/b$ and $2n/(3b)$ are read as $0$
when $\delta(\Gamma) = 0$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 5.

Stated but not proved: `MetaMathlibExt.maxIndepSetCount_le_of_maxDegree_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-indep-set-count-le-of-max-degree-le).

## Almost triangle-free bound

Let $\Gamma$ be a finite graph, let $T$ be a set of vertices
of $\Gamma$, let $n \ge 1$ and $D \ge 1$ be integers, and let $k$ be a real number. Suppose
that the graph $\Gamma'$ obtained from $\Gamma$ by deleting $T$ is triangle-free, has $n$
vertices and has at least $n/2 + k$ edges, and that $\Gamma$ has maximum degree
$\Delta(\Gamma) \le D$. Then the number $\mathrm{mis}(\Gamma)$ of maximal independent sets of
$\Gamma$ satisfies $\mathrm{mis}(\Gamma) \le 2^{n/2 - k/(100D^2) + 2|T|}$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 6.

Stated but not proved: `MetaMathlibExt.maxIndepSetCount_le_of_almost_triangleFree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-indep-set-count-le-of-almost-triangl).

## Liu–Sharifzadeh stability bound

Let $\Gamma$ be a graph with $n$ vertices, $n + k$
edges for an integer $k$, and maximum degree $\Delta \ge 1$. Then the number
$\mathrm{mis}(\Gamma)$ of maximal independent sets of $\Gamma$ satisfies
$\mathrm{mis}(\Gamma) \le 3^{\Delta/13} \cdot 3^{n/3 - k/(13\Delta)}$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 7.

Stated but not proved: `MetaMathlibExt.maxIndepSetCount_le_of_edge_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-indep-set-count-le-of-edge-count).

## Link-graph extension lemma

Let $G$ be an abelian group and let $B, S \subseteq G$ be
disjoint distinct sum-free sets. If $I \subseteq B$ and $S \cup I$ is a maximal distinct
sum-free subset of $G$, then $I$ is a maximal independent set of the distinct link graph
$L^*_S[B]$: a subset of $B$ with no looped vertex and no two adjacent vertices that is not
properly contained in another such set.

Disjointness of $B$ and $S$ is needed: for $G = \mathbb{Z}_2$, $S = G$, $B = \{0\}$ and
$I = \emptyset$ the conclusion fails.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Lemma 8.

Stated but not proved: `MetaMathlibExt.maximal_isDistinctLinkIndep_of_maximal` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#maximal-is-distinct-link-indep-of-maxima).

## Maximal distinct sum-free sets in groups of type $I(p)$

Let $G$ be a finite abelian
group and let $p \ge 5$ be such that $G$ is of type $I(p)$, that is, $p$ is the smallest prime
with $p \equiv 2 \pmod 3$ that divides $|G|$. Call $S \subseteq G$ sum-free if $x + y \notin S$
for all $x, y \in S$, and distinct sum-free if $x + y \notin S$ for all $x, y \in S$ such that
$x$, $y$ and $x + y$ are pairwise distinct. Let $\mu(G)$ be the size of a largest sum-free subset
of $G$, and let $f^*_{\max}(G)$ be the number of maximal distinct sum-free subsets of $G$. Then
$f^*_{\max}(G) \ge 2^{\mu(G)/2}$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Proposition 1.

Stated but not proved: `MetaMathlibExt.two_rpow_le_maxDistinctSumFreeCount_of_typeOne` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#two-rpow-le-max-distinct-sum-free-count).

## Random sum-free sets

For a finite abelian group $G$ let $\mu(G)$ be the size of a
largest sum-free subset of $G$. Let $(G_n)_{n \ge 0}$ be finite abelian groups with
$|G_i| < |G_j|$ and $\mu(G_i)/|G_i| = \mu(G_j)/|G_j|$ whenever $i < j$. Then for every
$\varepsilon > 0$ there is $C > 0$ such that for every real sequence $(p_n)$ with
$C |G_n|^{-1/2} \le p_n \le 1$ for all $n$, the probability that the largest sum-free subset
of the binomial random subset $G_{n,p_n}$ has size within $\varepsilon \mu(G_n) p_n$ of
$\mu(G_n) p_n$ tends to $1$ as $n \to \infty$. Here $G_{n,p}$ contains each element of $G_n$
independently with probability $p$, so this probability is
$\sum_S p_n^{|S|} (1-p_n)^{|G_n|-|S|}$ over the subsets $S \subseteq G_n$ with that property.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Theorem 2.

Stated but not proved: `MetaMathlibExt.tendsto_prob_largestSumFreeCard_random` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#tendsto-prob-largest-sum-free-card-rando).

## Counting maximal sum-free sets in elementary abelian 2- and 3-groups

Let $f_{\max}(G)$
be the number of maximal sum-free subsets of $G$. As $k \to \infty$, with $n = 2^k$,
$f_{\max}(\mathbb{Z}_2^k) = \bigl(\binom{n-1}{2} + o(1)\bigr) 2^{n/4}$, and with $n = 3^k$,
$f_{\max}(\mathbb{Z}_3^k) = \bigl((n-3)(n-1)/3 + o(1)\bigr) 3^{n/9}$; that is,
$f_{\max}(\mathbb{Z}_2^k)/2^{n/4} - \binom{n-1}{2} \to 0$ and
$f_{\max}(\mathbb{Z}_3^k)/3^{n/9} - (n-3)(n-1)/3 \to 0$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Theorem 3.

Stated but not proved: `MetaMathlibExt.maxSumFreeCount_elementary_two_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-sum-free-count-elementary-two-three).

## Maximal distinct sum-free sets in groups of even order

Write $f^*_{\max}(G)$ for the
number of maximal distinct sum-free subsets of an abelian group $G$. There is a natural number
$C$ such that for every real $\varepsilon > 0$ there is $n_0$ with the following property. Let
$r \ge 1$, let $\alpha_1, \dots, \alpha_r \ge 1$, let $K$ be a finite abelian group of odd order,
and let $G = \mathbb{Z}_{2^{\alpha_1}} \oplus \dots \oplus \mathbb{Z}_{2^{\alpha_r}} \oplus K$
have order $n$. If $n \ge n_0$ and $n / 2^r \ge C$, then
$2^{(1/4 - \varepsilon) n} \le f^*_{\max}(G) \le 2^{(1/4 + \varepsilon) n}$.

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Theorem 4.

Stated but not proved: `MetaMathlibExt.maxDistinctSumFreeCount_even_order` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-distinct-sum-free-count-even-order).

## Sharp upper bound on maximal distinct sum-free sets

Write $f^*_{\max}(G)$ for the number
of maximal distinct sum-free subsets of an abelian group $G$. There is a natural number $C$ such
that for every real $\eta > 0$ there is $n_0$ with the following property. Let $r_1, r_2 \ge 0$
with $r = r_1 + r_2 \ge 1$, let $\alpha_1, \dots, \alpha_{r_1} \ge 2$, let $K$ be a finite
abelian group of odd order, and let
$G = \mathbb{Z}_{2^{\alpha_1}} \oplus \dots \oplus \mathbb{Z}_{2^{\alpha_{r_1}}} \oplus
\mathbb{Z}_2^{r_2} \oplus K$ have order $n$. If $n \ge n_0$ and $n / 2^r \ge C$, then

$$f^*_{\max}(G) \le (2^{2r-1} + 2^{r+r_1-1} - 2^{r+1} + 2^{r_1})\, 2^{n/4} +
(2^r - 2^{r_1} + \eta)\, 2^{n/4 - 2^{r-2}}.$$

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Theorem 5.

Stated but not proved: `MetaMathlibExt.maxDistinctSumFreeCount_le_sharp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#max-distinct-sum-free-count-le-sharp).

## Sharp lower bound on maximal distinct sum-free sets

Write $f^*_{\max}(G)$ for the number
of maximal distinct sum-free subsets of an abelian group $G$. There is a natural number $C$ such
that for every real $\eta > 0$ there is $n_0$ with the following property. Let $r_1, r_2 \ge 0$
with $r = r_1 + r_2 \ge 1$, let $\alpha_1, \dots, \alpha_{r_1} \ge 2$, let $K$ be a finite
abelian group of odd order, and let
$G = \mathbb{Z}_{2^{\alpha_1}} \oplus \dots \oplus \mathbb{Z}_{2^{\alpha_{r_1}}} \oplus
\mathbb{Z}_2^{r_2} \oplus K$ have order $n$. If $n \ge n_0$ and $n / 2^r \ge C$, then

$$(2^{2r-1} + 2^{r+r_1-1} - 2^{r+1} + 2^{r_1})\, 2^{n/4} +
(2^r - 2^{r_1} - \eta)\, 2^{n/4 - 2^{r-2}} \le f^*_{\max}(G).$$

## Sources

- Nathanaël Hassler and Andrew Treglown, *Notes on Sum-Free Sets in Abelian Groups*, INTEGERS 26 (2026), Article A97, Theorem 6.

Stated but not proved: `MetaMathlibExt.le_maxDistinctSumFreeCount_sharp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/SumFreeAbelianGroupsWanted.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html#le-max-distinct-sum-free-count-sharp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sum-free sets in abelian groups](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/sum-free-sets-in-abelian-groups)
