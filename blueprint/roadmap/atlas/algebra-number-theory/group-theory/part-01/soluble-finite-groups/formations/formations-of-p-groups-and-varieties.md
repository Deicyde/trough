---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.GroupClass, MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.IsFormation, MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.SatisfiesLaws, MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.subformationOfPGroupsIsVarietal, MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.subformationOfPGroupsIsVarietal_refuted
statement: formalized
---

# Formations of p-groups and varieties

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html).

## Classes of groups

A class of groups is a predicate on groups: it assigns to every group
$G$ (in the lowest universe of types) a proposition, read as "$G$ belongs to the class". No
closure under isomorphism is required.

Formalized by `MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.GroupClass`, an abbreviation declared in [WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html#group-class).

## Formations of finite groups

A class $\mathfrak F$ of groups is a formation when every group
in $\mathfrak F$ is finite, $\mathfrak F$ contains at least one group, $\mathfrak F$ is closed under
isomorphism, $\mathfrak F$ is closed under quotients (if $G \in \mathfrak F$ and $N$ is a normal
subgroup of $G$, then $G/N \in \mathfrak F$), and $\mathfrak F$ is closed under subdirect products:
if $G$ is a finite group with normal subgroups $M$ and $N$ such that $G/M \in \mathfrak F$ and
$G/N \in \mathfrak F$, then $G/(M \cap N) \in \mathfrak F$.

Formalized by `MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.IsFormation`, a structure declared in [WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html#is-formation).

## Groups satisfying a set of laws

Let $W$ be a set of words in the free group on countably
many generators $x_0, x_1, x_2, \dots$. A group $G$ satisfies the laws in $W$ when every
homomorphism from this free group to $G$ sends every $w \in W$ to $1$. The groups satisfying $W$
form the variety defined by $W$, and every variety arises this way.

Formalized by `MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.SatisfiesLaws`, a definition declared in [WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html#satisfies-laws).

## Kourovka Problem 11.21 (Vasil'yev's question on formations of $p$-groups)

The proposition
that for every prime $p$ and every formation $\mathfrak F$ all of whose members are $p$-groups (a
subformation of the formation $\mathfrak N_p$ of all finite $p$-groups), there is a set $W$ of laws,
words in the free group on countably many generators, such that a finite $p$-group lies in
$\mathfrak F$ if and only if it satisfies every law in $W$. In other words, every such
$\mathfrak F$ equals $\mathfrak N_p \cap \mathfrak M$ for the variety $\mathfrak M$ defined by
$W$.

Formalized by `MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.subformationOfPGroupsIsVarietal`, a definition declared in [WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html#subformation-of-pgroups-is-varietal).

## Kourovka Problem 11.21 has a negative answer

There are a prime $p$ and a formation
$\mathfrak F$ all of whose members are $p$-groups such that for every set $W$ of laws, words in the
free group on countably many generators, some finite $p$-group lies in $\mathfrak F$ and fails a
law in $W$, or satisfies every law in $W$ and does not lie in $\mathfrak F$. Thus $\mathfrak F$ is
not of the form $\mathfrak N_p \cap \mathfrak M$ for any variety $\mathfrak M$, where
$\mathfrak N_p$ is the formation of all finite $p$-groups.

The Kourovka Archive answers 11.21 "No, it is not true" (A. N. Krasil'nikov): formations of finite
$p$-groups correspond bijectively to varieties of pro-$p$ groups, there are continuously many
varieties of nilpotent pro-$p$ groups of class at most $6$ (Zubkov), hence continuously many
formations of finite $p$-groups of class at most $6$, while such a formation of the form
$\mathfrak N_p \cap \mathfrak M$ equals $\mathfrak N_p \cap (\mathfrak M \cap \mathfrak N_6)$, where
$\mathfrak N_6$ is the variety of nilpotent groups of class at most $6$, and there are only
countably many varieties of nilpotent groups of class at most $6$ (all finitely based).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.21 (A. F. Vasil'yev); resolution: A. N. Krasil'nikov, letter of 17 July 1998, using A. N. Zubkov, Siberian Math. J. 29, no. 3 (1988), 491-494, Kourovka Archive, Problem 11.21: "No, it is not true"; formations of finite `p`-groups correspond to varieties of pro-`p` groups, there are continuously many varieties of nilpotent pro-`p` groups of class at most 6 (Zubkov) but only countably many varieties of nilpotent groups of class at most 6, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.FormationVarietyPGroupsKourovka11Problem21Wanted.subformationOfPGroupsIsVarietal_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FormationVarietyPGroupsKourovka11Problem21Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html#subformation-of-pgroups-is-varietal-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Formations of p-groups and varieties](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/formations-of-p-groups-and-varieties)
