---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.LatticeTerm, MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.LatticeTerm.eval, MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.IsBlock, MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.blockSup, MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.LatticeTerm.evalBlock, MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.blockLatticesGenerateAllLattices, MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.blockLatticesGenerateAllLattices_refuted
statement: formalized
---

# Block lattices of groups

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html).

## Lattice terms

Lattice terms in the variables $x_0, x_1, x_2, \dots$ are built
inductively: each variable $x_n$ is a term, and for terms $s$ and $t$ their join $s \vee t$ and
their meet $s \wedge t$ are terms.

Formalized by `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.LatticeTerm`, an inductive type declared in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#lattice-term).

## Evaluation of lattice terms

Let $L$ be a lattice and $v$ an assignment of an element
$v(n)$ of $L$ to each variable $x_n$. The value of a lattice term under $v$ is defined by
recursion on the term: the variable $x_n$ has value $v(n)$, and a join $s \vee t$ or meet
$s \wedge t$ has as value the join or meet in $L$ of the values of $s$ and $t$.

Formalized by `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.LatticeTerm.eval`, a definition declared in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#eval).

## Blocks of a group

A subset $X$ of a group $G$ is a block if it is empty or a coset $gN$
of a normal subgroup $N$ of $G$ (Kourovka Notebook, Archive 9.62). Ordered by inclusion, the
blocks of $G$ form the block lattice $C(G)$.

Formalized by `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.IsBlock`, a definition declared in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#is-block).

## Join in the block lattice

For subsets $X$ and $Y$ of a group $G$, their block join is the
intersection of all blocks of $G$ that contain $X \cup Y$. Since blocks are closed under
intersections and $G$ itself is a block, this is the smallest block containing $X \cup Y$; for
blocks $X$ and $Y$ it is their join in the block lattice of $G$.

Formalized by `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.blockSup`, a definition declared in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#block-sup).

## Evaluation of lattice terms in the block lattice

Let $G$ be a group and $v$ an assignment
of a subset $v(n)$ of $G$ to each variable $x_n$. The value of a lattice term under $v$ is defined
by recursion on the term: the variable $x_n$ has value $v(n)$, a meet $s \wedge t$ has as value
the intersection of the values of $s$ and $t$, and a join $s \vee t$ has as value the block join of
the values of $s$ and $t$, the intersection of all blocks of $G$ containing their union. When
every $v(n)$ is a block, this is the value of the term in the block lattice of $G$.

Formalized by `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.LatticeTerm.evalBlock`, a definition declared in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#eval-block).

## Kourovka Problem 11.93: do block lattices generate all lattices?

**Kourovka Problem 11.93: do block lattices generate all lattices?** The proposition, asked by
D. M. Smirnov, that the block lattices of finite groups generate the variety of all lattices. Here
the blocks of a group $G$ are the cosets of normal subgroups of $G$ and the empty set; ordered by
inclusion they form the block lattice of $G$, whose meet is intersection and whose join of two
blocks is the intersection of all blocks containing their union. Formally, the proposition states:
for all lattice terms $p$ and $q$, if $p$ and $q$ take the same value in the block lattice of every
finite group $G$ under every assignment of blocks of $G$ to the variables, then $p$ and $q$ take
the same value in every lattice $L$ under every assignment of elements of $L$ to the variables.

By Birkhoff's theorem this is equivalent to the variety generated by these block lattices being
the variety of all lattices.

Formalized by `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.blockLatticesGenerateAllLattices`, a definition declared in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#block-lattices-generate-all-lattices).

## Smirnov's negative answer to Kourovka Problem 11.93

The block lattices of finite groups do
not generate the variety of all lattices: there are lattice terms $p$ and $q$ such that $p$ and $q$
take the same value in the block lattice of every finite group $G$ under every assignment of blocks
of $G$ to the variables, but take different values in some lattice $L$ under some assignment of
elements of $L$ to the variables. Here the blocks of $G$ are the cosets of normal subgroups of $G$
and the empty set, and the block lattice of $G$ is the set of blocks ordered by inclusion.

Smirnov shows that the variety generated by the block lattices of groups does not contain all
finite lattices: for each element $g$ of a group $G$, the filter of blocks containing $g$ is a
modular, even arguesian, lattice.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.93 (D. M. Smirnov); resolution: D. M. Smirnov, Siberian Math. J. 33, no. 4 (1992), 663-668, Kourovka Archive, Problem 11.93: "No, it is not"; Archive 9.62: the variety generated by the block lattices of groups does not contain all finite lattices, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.BlockLatticeVarietyKourovka11Problem93Wanted.blockLatticesGenerateAllLattices_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BlockLatticeVarietyKourovka11Problem93Wanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html#block-lattices-generate-all-lattices-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Block lattices of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/subgroup-embedding/block-lattices-of-groups)
