---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiPeriodicTwo, MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiBinaryFinite, MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiPeriodicTwo_refuted, MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiBinaryFinite_holds, MathlibExt.GroupTheory.BaerSuzukiWanted.GroupTheory.Defs.pCore, MathlibExt.GroupTheory.BaerSuzukiWanted.GroupTheory.baer_suzuki
statement: formalized
---

# Baer–Suzuki theorem

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html).

## Baer–Suzuki property for periodic groups at the prime 2

The proposition that for every
group $G$ in which every element has finite order and every element $a \in G$ such that any two
conjugates of $a$ generate a finite $2$-subgroup, there is a normal $2$-subgroup of $G$ containing
$a$. Here a $2$-subgroup is a subgroup in which every element has order a power of $2$.

This is the case $p = 2$ of Kourovka Problem 11.11(a) (A. V. Borovik).

Formalized by `MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiPeriodicTwo`, a definition declared in [WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html#baer-suzuki-periodic-two).

## Baer–Suzuki property for binary finite groups

The proposition that for every prime $p$,
every group $G$ in which any two elements generate a finite subgroup, and every element $a \in G$
such that any two conjugates of $a$ generate a $p$-subgroup, there is a normal $p$-subgroup of $G$
containing $a$. Here a $p$-subgroup is a subgroup in which every element has order a power of $p$.

This is the statement asked about in Kourovka Problem 11.11(b) (A. V. Borovik).

Formalized by `MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiBinaryFinite`, a definition declared in [WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html#baer-suzuki-binary-finite).

## Failure of the Baer–Suzuki theorem for periodic groups at the prime 2

There is a group $G$
in which every element has finite order, together with an element $a \in G$ such that any two
conjugates of $a$ generate a finite $2$-subgroup, but no normal $2$-subgroup of $G$ contains $a$.
Here a $2$-subgroup is a subgroup in which every element has order a power of $2$.

This answers Kourovka Problem 11.11(a) negatively for $p = 2$ (Mazurov, Olshanskii and
Sozutov, 2015).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.11 (A. V. Borovik); resolution: V. D. Mazurov, A. Yu. Olshanskii and A. I. Sozutov, Algebra and Logic 54, no. 2 (2015), 161-166 (a); A. I. Sozutov, Siberian Math. J. 41, no. 3 (2000), 561-562 (b), Kourovka Archive, Problem 11.11.

Stated but not proved: `MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiPeriodicTwo_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html#baer-suzuki-periodic-two-refuted).

## Baer–Suzuki theorem for binary finite groups

For every prime $p$, every group $G$ in
which any two elements generate a finite subgroup, and every element $a \in G$ such that any two
conjugates of $a$ generate a $p$-subgroup, there is a normal $p$-subgroup of $G$ containing $a$.
Here a $p$-subgroup is a subgroup in which every element has order a power of $p$.

This answers Kourovka Problem 11.11(b) affirmatively (Sozutov, 2000): by the Baer–Suzuki theorem
for finite groups, $\langle a_1, b \rangle$ is a finite $p$-group for every conjugate $a_1$ of $a$
and every element $b$ of $p$-power order, so by induction every product $a_1 \cdots a_n$ of
conjugates of $a$ has $p$-power order, and the normal closure of $a$ is a normal $p$-subgroup.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.11 (A. V. Borovik); resolution: V. D. Mazurov, A. Yu. Olshanskii and A. I. Sozutov, Algebra and Logic 54, no. 2 (2015), 161-166 (a); A. I. Sozutov, Siberian Math. J. 41, no. 3 (2000), 561-562 (b), Kourovka Archive, Problem 11.11.

Stated but not proved: `MathlibExt.GroupTheory.BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.baerSuzukiBinaryFinite_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BaerSuzukiPeriodicBinaryFiniteKourovka11Problem11Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html#baer-suzuki-binary-finite-holds).

## The $p$-core of a group

For a natural number $p$ and a group $G$, the $p$-core $O_p(G)$
is the supremum, in the lattice of subgroups of $G$, of all normal subgroups $N$ of $G$ that are
$p$-groups, that is, such that every $y \in N$ satisfies $y^{p^k} = 1$ for some $k \ge 0$.

When $p$ is prime, $O_p(G)$ is itself a normal $p$-subgroup of $G$, hence the largest one, and no
finiteness hypothesis is needed: the join of two normal $p$-subgroups is again a normal
$p$-subgroup, so the family is directed and every element of the supremum lies in one of them.

Formalized by `MathlibExt.GroupTheory.BaerSuzukiWanted.GroupTheory.Defs.pCore`, a definition declared in [WantedExt/GroupTheory/BaerSuzukiWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BaerSuzukiWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html#p-core).

## Baer–Suzuki theorem

Let $G$ be a finite group, $p$ a prime and $x \in G$. Then $x$ lies
in the $p$-core $O_p(G)$ of $G$ if and only if, for every $g \in G$, the subgroup of $G$ generated
by $x$ and $g x g^{-1}$ is a $p$-group, that is, every element of it has order a power of $p$.

## Sources

- R. Baer, Engelsche Elemente Noetherscher Gruppen, Math. Ann. 133 (1957), 256-270; M. Suzuki, Finite groups in which the centralizer of any element of order 2 is 2-closed, Ann. of Math. (2) 82 (1965), 191-212. Problem `baer_suzuki` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.BaerSuzukiWanted.GroupTheory.baer_suzuki` is written with `theorem_wanted` in [WantedExt/GroupTheory/BaerSuzukiWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BaerSuzukiWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html#baer-suzuki).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Baer–Suzuki theorem](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-simple-groups/baer-suzuki-theorem)
