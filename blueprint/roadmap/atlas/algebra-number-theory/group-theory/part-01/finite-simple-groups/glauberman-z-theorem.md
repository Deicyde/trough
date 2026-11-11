---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.GlaubermanZStarWanted.GroupTheory.glauberman_zStar, MathlibExt.GroupTheory.InvolutionOddProductCentralKourovka11Problem13Wanted.oddCore, MathlibExt.GroupTheory.InvolutionOddProductCentralKourovka11Problem13Wanted.periodicInvolutionCentralModOddCore, MathlibExt.GroupTheory.InvolutionOddProductCentralKourovka11Problem13Wanted.periodicInvolutionCentralModOddCore_refuted
statement: formalized
---

# Glauberman Z\*-theorem

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem/index.html).

## Glauberman's $Z^*$-theorem

**Glauberman's $Z^*$-theorem.** Let $G$ be a finite group and let $t \in G$ be an involution
($t \neq 1$ and $t^2 = 1$) such that every conjugate $g t g^{-1}$ of $t$ that commutes with $t$
equals $t$. Then there is a normal subgroup $N$ of $G$ of odd order such that
$g t g^{-1} t^{-1} \in N$ for every $g \in G$.

## Sources

- G. Glauberman, Central elements in core-free groups, J. Algebra 4 (1966). Problem `glauberman_zStar` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.GlaubermanZStarWanted.GroupTheory.glauberman_zStar` is written with `theorem_wanted` in [WantedExt/GroupTheory/GlaubermanZStarWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GlaubermanZStarWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem/index.html#glauberman-z-star).

## Odd core from normal subgroups of odd-order elements

For a group $G$, $O(G)$ is the join,
in the lattice of subgroups of $G$, of all normal subgroups $N$ of $G$ such that every element of
$N$ has finite odd order. In a periodic group this join is again a normal subgroup consisting of
elements of odd order, so it is the largest such subgroup.

Formalized by `MathlibExt.GroupTheory.InvolutionOddProductCentralKourovka11Problem13Wanted.oddCore`, a definition declared in [WantedExt/GroupTheory/InvolutionOddProductCentralKourovka11Problem13Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InvolutionOddProductCentralKourovka11Problem13Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem/index.html#odd-core).

## Borovik's question on involutions with odd-order products (Kourovka 11.13)

For a group
$G$, let $O(G)$ be the join of all normal subgroups of $G$ all of whose elements have odd order.
This is the statement that for every periodic group $G$ and every involution $i \in G$ such that
$g^{-1} i g i$ has odd order for every $g \in G$, the image of $i$ in $G / O(G)$ is central, that
is, $g i g^{-1} i^{-1} \in O(G)$ for every $g \in G$.

Formalized by `MathlibExt.GroupTheory.InvolutionOddProductCentralKourovka11Problem13Wanted.periodicInvolutionCentralModOddCore`, a definition declared in [WantedExt/GroupTheory/InvolutionOddProductCentralKourovka11Problem13Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InvolutionOddProductCentralKourovka11Problem13Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem/index.html#periodic-involution-central-mod-odd-core).

## A periodic counterexample to Borovik's question (Kourovka 11.13)

For a group $G$, let $O(G)$
be the join of all normal subgroups of $G$ all of whose elements have odd order. There exist a
periodic group $G$ and an involution $i \in G$ such that $g^{-1} i g i$ has odd order for every
$g \in G$, but the image of $i$ in $G / O(G)$ is not central: $g i g^{-1} i^{-1} \notin O(G)$ for
some $g \in G$. This answers Kourovka Problem 11.13 in the negative.

For finite groups the answer is yes, by Glauberman's $Z^*$-theorem.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.13 (A. V. Borovik); resolution: E. B. Durakov and A. I. Sozutov, Algebra and Logic 52, no. 5 (2013), 422-425, Kourovka Archive, Problem 11.13: "No, not always", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.InvolutionOddProductCentralKourovka11Problem13Wanted.periodicInvolutionCentralModOddCore_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/InvolutionOddProductCentralKourovka11Problem13Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/InvolutionOddProductCentralKourovka11Problem13Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem/index.html#periodic-involution-central-mod-odd-core-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Glauberman Z*-theorem](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-simple-groups/glauberman-z-theorem)
