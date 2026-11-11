---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.rightOrders, MathlibExt.GroupTheory.SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.existsSimpleFGRightOrderable, MathlibExt.GroupTheory.SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.existsSimpleFGRightOrderable_holds
statement: formalized
---

# Simple right-orderable groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/simple-right-orderable-groups/index.html).

## Right orders on a group (Kourovka Problem 16.50)

The right orders of a group $G$ are the
linear orders $\le$ on $G$, viewed as relations, that are invariant under right multiplication:
$a \le b$ implies $ac \le bc$ for all $a, b, c \in G$.

Formalized by `MathlibExt.GroupTheory.SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.rightOrders`, a definition declared in [WantedExt/GroupTheory/SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/simple-right-orderable-groups/index.html#right-orders).

## Kourovka Problem 16.50 (finitely generated simple right-orderable groups)

The statement
that there exists a finitely generated simple group $G$ admitting a right order, that is, a linear
order $\le$ on $G$ such that $a \le b$ implies $ac \le bc$ for all $a, b, c \in G$. The problem is
due to V. M. Kopytov and N. Ya. Medvedev.

Formalized by `MathlibExt.GroupTheory.SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.existsSimpleFGRightOrderable`, a definition declared in [WantedExt/GroupTheory/SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/simple-right-orderable-groups/index.html#exists-simple-fgright-orderable).

## Finitely generated simple right-orderable groups exist

There is a finitely generated simple
group $G$ that admits a right order, that is, a linear order $\le$ on $G$ such that $a \le b$
implies $ac \le bc$ for all $a, b, c \in G$. This answers Kourovka Problem 16.50 positively.

Hyde and Lodha (Theorem 1.3) construct finitely generated simple groups of orientation-preserving
homeomorphisms of the real line, which are finitely generated simple left (or right) orderable
groups (Corollary 1.5 and the abstract). The Kourovka Archive answers 16.50 "Yes, such groups do
exist".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.50 (V. M. Kopytov, N. Ya. Medvedev); resolution: J. Hyde and Y. Lodha, Finitely generated infinite simple groups of homeomorphisms of the real line, Invent. Math. 218 (2019), 83-112, arXiv:1807.06478, Theorem 1.3 (G_ρ is a finitely generated simple subgroup of Homeo+(ℝ)) and Corollary 1.5 (finitely generated simple left orderable groups exist; by the abstract, equivalently left or right orderable); Kourovka Archive, Problem 16.50 (Yes, such groups do exist), https://arxiv.org/abs/1807.06478.

Stated but not proved: `MathlibExt.GroupTheory.SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.existsSimpleFGRightOrderable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleFinitelyGeneratedRightOrderableKourovka16Problem50Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/simple-right-orderable-groups/index.html#exists-simple-fgright-orderable-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simple right-orderable groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/simple-right-orderable-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orderable-groups/simple-right-orderable-groups)
