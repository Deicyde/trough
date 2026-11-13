---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FieldAutomorphismGroupRingKourovka11Problem79Wanted.subfieldContainsInfinitelyManyInvariants, MathlibExt.GroupTheory.FieldAutomorphismGroupRingKourovka11Problem79Wanted.subfieldContainsInfinitelyManyInvariants_holds
statement: formalized
---

# Group-ring powers in fields

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/group-ring-powers-in-fields/index.html).

## Group-ring powers and invariant elements (Kourovka 11.79)

The proposition that the
following holds for every prime $p$, every infinite field $F$ of characteristic $p$, every finite
group $G$ of ring automorphisms of $F$, and every element $\xi = \sum_{g \in G} \xi_g \, g$ of the
group ring $\mathbb{Z}G$ with $\xi \notin p\mathbb{Z}G$, that is, with some integer coefficient
$\xi_g$ not divisible by $p$. For nonzero $x \in F$ put $x^\xi = \prod_{g \in G} g(x)^{\xi_g}$.
If a subfield $K$ of $F$ contains $x^\xi$ for every nonzero $x \in F$, then $K$ contains
infinitely many elements $y$ with $g(y) = y$ for all $g \in G$.

Formalized by `MathlibExt.GroupTheory.FieldAutomorphismGroupRingKourovka11Problem79Wanted.subfieldContainsInfinitelyManyInvariants`, a definition declared in [WantedExt/GroupTheory/FieldAutomorphismGroupRingKourovka11Problem79Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FieldAutomorphismGroupRingKourovka11Problem79Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/group-ring-powers-in-fields/index.html#subfield-contains-infinitely-many-invari).

## Subfields containing all group-ring powers have infinitely many invariants

Let $p$ be a
prime, $F$ an infinite field of characteristic $p$, $G$ a finite group of ring automorphisms of
$F$, and $\xi = \sum_{g \in G} \xi_g \, g$ an element of the group ring $\mathbb{Z}G$ with
$\xi \notin p\mathbb{Z}G$, that is, with some integer coefficient $\xi_g$ not divisible by $p$.
For nonzero $x \in F$ put $x^\xi = \prod_{g \in G} g(x)^{\xi_g}$. If a subfield $K$ of $F$
contains $x^\xi$ for every nonzero $x \in F$, then $K$ contains infinitely many elements $y$ with
$g(y) = y$ for all $g \in G$. This is the positive answer to Kourovka Notebook Problem 11.79,
given by K. N. Ponomarëv (1992).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.79 (K. N. Ponomarëv); resolution: K. N. Ponomarëv, Siberian Math. J. 33 (1992), 1094-1099, Kourovka Archive, Problem 11.79: "Yes", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.FieldAutomorphismGroupRingKourovka11Problem79Wanted.subfieldContainsInfinitelyManyInvariants_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FieldAutomorphismGroupRingKourovka11Problem79Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FieldAutomorphismGroupRingKourovka11Problem79Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/group-ring-powers-in-fields/index.html#subfield-contains-infinitely-many-invari-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Group-ring powers in fields](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/group-ring-powers-in-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/group-rings/group-ring-powers-in-fields)
