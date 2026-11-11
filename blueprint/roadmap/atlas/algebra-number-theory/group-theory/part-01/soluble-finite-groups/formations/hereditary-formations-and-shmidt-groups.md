---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.GroupClass, MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsHereditarySolubleFormation, MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsSaturated, MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsMinimalNon, MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsShmidtGroup, MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.hereditaryFormationLocalOfShmidt, MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.hereditaryFormationLocalOfShmidt_holds
statement: formalized
---

# Hereditary formations and Shmidt groups

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html).

## Classes of groups

A class of groups is a property of groups: for each group $G$ it gives
a proposition, read as "$G$ belongs to the class". No closure under isomorphism is required.

Formalized by `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.GroupClass`, an abbreviation declared in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#group-class).

## Hereditary formations of finite soluble groups

A class $\mathfrak F$ of groups is a
hereditary formation of finite soluble groups if every group in $\mathfrak F$ is finite and
soluble; $\mathfrak F$ is closed under isomorphisms, under taking subgroups and under taking
quotients by normal subgroups; and for every finite group $G$ with normal subgroups $M$ and $N$
such that $G/M$ and $G/N$ lie in $\mathfrak F$, also $G/(M \cap N)$ lies in $\mathfrak F$.

Formalized by `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsHereditarySolubleFormation`, a structure declared in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#is-hereditary-soluble-formation).

## Saturated classes of groups

A class $\mathfrak F$ of groups is saturated if every finite
soluble group $G$ such that $G/\Phi(G)$ lies in $\mathfrak F$, where $\Phi(G)$ is the Frattini
subgroup of $G$, itself lies in $\mathfrak F$.

By the Gaschütz–Lubeseder theorem, a nonempty formation of finite soluble groups is saturated if
and only if it is local.

Formalized by `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsSaturated`, a definition declared in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#is-saturated).

## Minimal non-members of a class of groups

Let $\mathfrak F$ be a class of groups. A group
$G$ is a minimal non-$\mathfrak F$-group if $G$ does not lie in $\mathfrak F$ but every proper
subgroup of $G$ lies in $\mathfrak F$.

Formalized by `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsMinimalNon`, a definition declared in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#is-minimal-non).

## Shmidt groups

A group $G$ is a Shmidt group if it is finite and not nilpotent, but every
proper subgroup of $G$ is nilpotent.

Formalized by `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.IsShmidtGroup`, a definition declared in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#is-shmidt-group).

## Kourovka Problem 11.91 (statement)

The statement that every hereditary formation
$\mathfrak F$ of finite soluble groups such that every finite soluble non-simple minimal
non-$\mathfrak F$-group (a group outside $\mathfrak F$ all of whose proper subgroups lie in
$\mathfrak F$) is a Shmidt group is saturated, that is, every finite soluble group $G$ whose
quotient $G/\Phi(G)$ by its Frattini subgroup $\Phi(G)$ lies in $\mathfrak F$ itself lies in
$\mathfrak F$.

Under this hypothesis $\mathfrak F$ contains the trivial group, so by the Gaschütz–Lubeseder
theorem saturated is the same as local, the property the problem (V. N. Semenchuk) asks for.

Formalized by `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.hereditaryFormationLocalOfShmidt`, a definition declared in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#hereditary-formation-local-of-shmidt).

## Skiba's theorem (Kourovka Problem 11.91)

Let $\mathfrak F$ be a hereditary formation of
finite soluble groups: every group in $\mathfrak F$ is finite and soluble, $\mathfrak F$ is closed
under isomorphisms, subgroups and quotients, and whenever $M$ and $N$ are normal subgroups of a
finite group $G$ with $G/M$ and $G/N$ in $\mathfrak F$, also $G/(M \cap N)$ lies in $\mathfrak F$.
Suppose that every finite soluble group that is not simple and is a minimal non-$\mathfrak F$-group
(it does not lie in $\mathfrak F$, but all of its proper subgroups do) is a Shmidt group, that is,
a finite non-nilpotent group all of whose proper subgroups are nilpotent. Then $\mathfrak F$ is
saturated: every finite soluble group $G$ such that $G/\Phi(G)$ lies in $\mathfrak F$, where
$\Phi(G)$ is the Frattini subgroup of $G$, itself lies in $\mathfrak F$.

The hypothesis forces the trivial group into $\mathfrak F$, and by the Gaschütz–Lubeseder theorem a
nonempty saturated formation of finite soluble groups is local, so $\mathfrak F$ is local.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.91 (V. N. Semenchuk); resolution: A. N. Skiba, Dokl. Akad. Nauk Belorus. SSR 34, no. 11 (1990), 982-985 (Russian), Kourovka Archive, Problem 11.91: "This is proved", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.HereditaryFormationShmidtLocalKourovka11Problem91Wanted.hereditaryFormationLocalOfShmidt_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/HereditaryFormationShmidtLocalKourovka11Problem91Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html#hereditary-formation-local-of-shmidt-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hereditary formations and Shmidt groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/hereditary-formations-and-shmidt-groups)
