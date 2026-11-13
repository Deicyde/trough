---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.IsJustInfinite, MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.IsResiduallyFinite, MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.IsHereditarilyJustInfinite, MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteTorsionGroup, MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteIsLinear, MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteTorsionGroup_holds, MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteIsLinear_refuted, MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.TreeVertex
statement: formalized
---

# Just infinite groups

16 results, 13 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html).

## Just infinite groups

A group $G$ is just infinite if it is infinite and every nontrivial
normal subgroup of $G$ has finite index in $G$.

Formalized by `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.IsJustInfinite`, a definition declared in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#is-just-infinite).

## Residually finite groups

A group $G$ is residually finite if every element $g \ne 1$ of
$G$ lies outside some normal subgroup of finite index in $G$.

Formalized by `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.IsResiduallyFinite`, a definition declared in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#is-residually-finite).

## Hereditarily just infinite groups

A group $G$ is hereditarily just infinite (in the
sense of Kourovka 15.18) if it is infinite, residually finite, and every nontrivial normal
subgroup of $G$, viewed as a group in its own right, is just infinite.

Formalized by `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.IsHereditarilyJustInfinite`, a definition declared in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#is-hereditarily-just-infinite).

## Kourovka 15.18(a): hereditarily just infinite torsion groups

The proposition that there
exists a finitely generated hereditarily just infinite group $G$ that is a torsion group, i.e.
every element of $G$ has finite order.

Formalized by `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteTorsionGroup`, a definition declared in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#fg-hereditarily-just-infinite-torsion-gr).

## Kourovka 15.18(b): linearity of hereditarily just infinite groups

The proposition that
every finitely generated hereditarily just infinite group $G$ is linear, i.e. that there are a
field $K$, a natural number $n$ and an injective group homomorphism $G \to \mathrm{GL}_n(K)$.

Formalized by `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteIsLinear`, a definition declared in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#fg-hereditarily-just-infinite-is-linear).

## Finitely generated hereditarily just infinite torsion groups exist

There is a finitely
generated hereditarily just infinite group $G$ in which every element has finite order.

This answers Kourovka 15.18(a) positively, as recorded in the Kourovka Archive ("Yes, such groups
exist"; Ershov and Jaikin-Zapirain).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.18 (L. Bartholdi, R. I. Grigorchuk, Z. Šunić); resolution: M. Ershov and A. Jaikin-Zapirain, Groups of positive weighted deficiency and their applications, J. Reine Angew. Math. 677 (2013), 71-134, arXiv:1007.1489, Kourovka Archive, Problem 15.18 ((a) Yes, such groups exist; (b) No, not every); the abstract constructs finitely generated residually finite p-torsion groups and shows that every group of positive weighted deficiency has a hereditarily just infinite quotient, https://arxiv.org/abs/1007.1489.

Stated but not proved: `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteTorsionGroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#fg-hereditarily-just-infinite-torsion-gr-2).

## Not every finitely generated hereditarily just infinite group is linear

There is a finitely
generated hereditarily just infinite group $G$ such that for no field $K$ and no natural number
$n$ is there an injective group homomorphism $G \to \mathrm{GL}_n(K)$.

This answers Kourovka 15.18(b) negatively, as recorded in the Kourovka Archive ("No, not every";
Ershov and Jaikin-Zapirain). As the problem notes, a positive answer to (b) would contradict (a):
a finitely generated linear torsion group is finite, while a just infinite group is infinite.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.18 (L. Bartholdi, R. I. Grigorchuk, Z. Šunić); resolution: M. Ershov and A. Jaikin-Zapirain, Groups of positive weighted deficiency and their applications, J. Reine Angew. Math. 677 (2013), 71-134, arXiv:1007.1489, Kourovka Archive, Problem 15.18 ((a) Yes, such groups exist; (b) No, not every); the abstract constructs finitely generated residually finite p-torsion groups and shows that every group of positive weighted deficiency has a hereditarily just infinite quotient, https://arxiv.org/abs/1007.1489.

Stated but not proved: `MathlibExt.GroupTheory.HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.fgHereditarilyJustInfiniteIsLinear_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HereditarilyJustInfiniteGroupsKourovka15Problem18Wanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#fg-hereditarily-just-infinite-is-linear-2).

## Vertices of a spherically homogeneous rooted tree

For a sequence $m : \mathbb{N} \to
\mathbb{N}$ of branching indices, the vertices of the spherically homogeneous rooted tree with
branching sequence $m$ are the finite words $x_0 x_1 \cdots x_{\ell-1}$ of natural numbers with
$x_i < m(i)$ for every $i < \ell$. The length of a word is its level and its prefixes are its
ancestors.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.TreeVertex`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#tree-vertex).

## Rigid vertex stabilizer

Let $\rho$ be a homomorphism from a group $G$ to the group of
permutations of the vertices of the rooted tree with branching sequence $m$, and let $v$ be a
vertex. The rigid vertex stabilizer of $v$ is the set of elements $g \in G$ such that $\rho(g)$
fixes every vertex that does not have $v$ as a prefix, that is, the elements whose support (the set
of vertices they move) lies in the subtree rooted at $v$.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.rigidVertexStabilizer`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#rigid-vertex-stabilizer).

## Rigid level stabilizer

Let $\rho$ be a homomorphism from a group $G$ to the group of
permutations of the vertices of the rooted tree with branching sequence $m$. For a natural number
$n$, the $n$-th rigid level stabilizer is the subgroup of $G$ generated by the union of the rigid
vertex stabilizers of all vertices at level $n$, that is, of all words of length $n$.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.rigidLevelStabilizer`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#rigid-level-stabilizer).

## Branch groups

A group $G$ is a branch group (Kourovka 15.12) if there are a sequence
$m : \mathbb{N} \to \mathbb{N}$ with $m(i) \ge 2$ for all $i$ and a homomorphism $\rho$ from $G$ to
the group of permutations of the vertices of the rooted tree with branching sequence $m$ such that
$\rho$ is injective; every $\rho(g)$ is a tree automorphism, that is, for all vertices $v$ and $w$,
$v$ is a prefix of $w$ if and only if $\rho(g)(v)$ is a prefix of $\rho(g)(w)$; the action is
level-transitive, that is, for any two vertices $v$ and $w$ of the same level there is $g \in G$
with $\rho(g)(v) = w$; and for every $n$ the $n$-th rigid level stabilizer has finite index in
$G$.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.IsBranchGroup`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#is-branch-group).

## Growth rate of a finite generating family

Let $P$ be a generating family of a group $G$
indexed by $\{0, \dots, k-1\}$, and let $\beta_P(n)$ be the number of elements of $G$ whose word
length with respect to $P$ is at most $n$, that is, which are products of at most $n$ members of
$P$ and their inverses. The growth rate of $P$ is the real number
$\omega(G, P) = \limsup_{n \to \infty} \beta_P(n)^{1/n}$.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.growthRate`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#growth-rate).

## Just infinite groups

A group $G$ is just infinite if it is infinite and every nontrivial
normal subgroup of $G$ has finite index, that is, all proper quotients of $G$ are finite.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.IsJustInfinite`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#is-just-infinite-2).

## Groups of intermediate growth

A group $G$ has intermediate growth if it is finitely
generated and, for every natural number $k$ and every generating family $P$ of $G$ indexed by
$\{0, \dots, k-1\}$, the growth rate of $P$ is at most $1$ (subexponential growth) and $P$ does
not have polynomial growth.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.HasIntermediateGrowth`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#has-intermediate-growth).

## The branch question for just infinite groups of intermediate growth

Kourovka
Problem 15.17 (L. Bartholdi, R. I. Grigorchuk, Z. Šunić) is the assertion that every finitely
generated just infinite group of intermediate growth is a branch group.

Formalized by `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.justInfiniteIntermediateGrowthIsBranch`, a definition declared in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#just-infinite-intermediate-growth-is-bra).

## Just infinite groups of intermediate growth need not be branch groups

It is not the case
that every finitely generated just infinite group of intermediate growth is a branch group: the
Kourovka Archive answers Problem 15.17 "No, not every".

Nekrashevych constructed infinite finitely generated simple groups of intermediate growth. Such a
group is just infinite, and it is not a branch group: its rigid level stabilizers, nontrivial normal
subgroups of finite index, would be the whole group, which they split as a direct product of at
least two nontrivial factors.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.17 (L. Bartholdi, R. I. Grigorchuk, Z. Šunić); resolution: V. Nekrashevych, Palindromic subshifts and simple periodic groups of intermediate growth, Ann. of Math. (2) 187 (2018), no. 3, 667-719, abstract (infinite finitely generated periodic groups of intermediate growth, among them the first simple groups of intermediate growth); Kourovka Archive, Problem 15.17 (answer: No, not every; there exist simple finitely generated groups of intermediate growth; the Archive prints the volume as 87), https://arxiv.org/abs/1601.01033.

Stated but not proved: `MathlibExt.GroupTheory.JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.justInfiniteIntermediateGrowthIsBranch_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustInfiniteIntermediateGrowthBranchKourovka15Problem17Wanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html#just-infinite-intermediate-growth-is-bra-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Just infinite groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/geometric-group-theory/branch-and-thompson-groups/just-infinite-groups)
