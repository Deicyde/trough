---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.IsElementaryAmenable, MathlibExt.GroupTheory.ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.finitelyPresentedElementaryAmenableVirtuallySolvable, MathlibExt.GroupTheory.ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.finitelyPresentedElementaryAmenableVirtuallySolvable_refuted
statement: formalized
---

# Elementary amenable groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/elementary-amenable-groups/index.html).

## Elementary amenable groups

The class of elementary amenable groups is the smallest class
of groups that contains every finite group and every abelian group and is closed under
isomorphisms, subgroups, quotients, extensions and directed unions. Closure under extensions means
that a group $G$ with a normal subgroup $N$ is elementary amenable whenever $N$ and $G/N$ are;
closure under directed unions means that $G$ is elementary amenable whenever it is the union of a
family of elementary amenable subgroups that is directed under inclusion.

Formalized by `MathlibExt.GroupTheory.ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.IsElementaryAmenable`, an inductive type declared in [WantedExt/GroupTheory/ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/elementary-amenable-groups/index.html#is-elementary-amenable).

## Kourovka Problem 16.52 (Linnell–Schick)

The statement that every finitely presented
elementary amenable group $G$ is solvable-by-finite, that is, $G$ has a solvable subgroup of finite
index.

Formalized by `MathlibExt.GroupTheory.ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.finitelyPresentedElementaryAmenableVirtuallySolvable`, a definition declared in [WantedExt/GroupTheory/ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/elementary-amenable-groups/index.html#finitely-presented-elementary-amenable-v).

## Finitely presented elementary amenable groups need not be virtually solvable

There is a
finitely presented elementary amenable group $G$ that is not solvable-by-finite: no subgroup of
finite index in $G$ is solvable. This answers Kourovka Problem 16.52 (P. Linnell, T. Schick) in
the negative.

As Belegradek and Cornulier observed, Houghton's groups $H_n$, finitely presented for $n \ge 3$
by Brown, are elementary amenable (the locally finite group of finitary permutations extended by
$\mathbb{Z}^{n-1}$) but not virtually solvable.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.52 (P. Linnell, T. Schick); resolution: C. H. Houghton, Arch. Math. (Basel) 31 (1978/79), 254-258; K. S. Brown, J. Pure Appl. Algebra 44 (1987), 45-75; observation of I. Belegradek and Y. Cornulier, MathOverflow question 107996, Kourovka Archive, Problem 16.52 (No, not every: Houghton's groups are finitely presented (Brown) and elementary amenable, but not virtually solvable), https://mathoverflow.net/questions/107996.

Stated but not proved: `MathlibExt.GroupTheory.ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.finitelyPresentedElementaryAmenableVirtuallySolvable_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ElementaryAmenableVirtuallySolvableKourovka16Problem52Wanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/elementary-amenable-groups/index.html#finitely-presented-elementary-amenable-v-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elementary amenable groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/elementary-amenable-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/geometric-group-theory/elementary-amenable-groups)
