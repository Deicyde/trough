---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.biOrders, MathlibExt.GroupTheory.FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.finitelyPresentedOrderableInsolubleWordProblem, MathlibExt.GroupTheory.FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.finitelyPresentedOrderableInsolubleWordProblem_holds, MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.IsRecursivelyPresented, MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.rightOrders, MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.solubleRightOrderableInsolubleWordProblem, MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.solubleRightOrderableInsolubleWordProblem_holds
statement: formalized
---

# Word problem for orderable groups

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html).

## Bi-invariant linear orders on a group

For a group $G$, the bi-invariant orders of $G$ are
the linear orders $\le$ on $G$ (reflexive, antisymmetric, transitive and total relations) that are
invariant under left and right multiplication: for all $a, b, c \in G$, $a \le b$ implies
$ca \le cb$ and $ac \le bc$.

Formalized by `MathlibExt.GroupTheory.FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.biOrders`, a definition declared in [WantedExt/GroupTheory/FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#bi-orders).

## Kourovka Problem 17.29 (V. V. Bludov, A. M. W. Glass)

The statement that there is a
finitely presented group $G$ that admits a bi-invariant linear order and has a finite generating
family $g_1, \dots, g_k$ for which the word problem is insoluble: no algorithm decides, given a word
in the $g_i$ and their inverses, whether it equals $1$ in $G$.

Formalized by `MathlibExt.GroupTheory.FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.finitelyPresentedOrderableInsolubleWordProblem`, a definition declared in [WantedExt/GroupTheory/FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#finitely-presented-orderable-insoluble-w).

## Bludov–Glass: a finitely presented orderable group with insoluble word problem

There is a
finitely presented group $G$ that admits a bi-invariant linear order and has a finite generating
family $g_1, \dots, g_k$ for which the word problem is insoluble: no algorithm decides, given a word
in the $g_i$ and their inverses, whether it equals $1$ in $G$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.29 (V. V. Bludov, A. M. W. Glass); resolution: V. V. Bludov and A. M. W. Glass, Bull. London Math. Soc. 44 (2012), 85-98, Kourovka Archive, Problem 17.29 (Such a group is constructed).

Stated but not proved: `MathlibExt.GroupTheory.FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.finitelyPresentedOrderableInsolubleWordProblem_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FinitelyPresentedOrderableWordProblemKourovka17Problem29Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#finitely-presented-orderable-insoluble-w-2).

## Recursively presented group

Let $G$ be a group, $k$ a natural number and $\varphi$ a
homomorphism from the free group on $k$ generators to $G$. The group $G$ is recursively presented
with respect to $\varphi$ when the set of words $w$ (finite lists of letters $(i, \varepsilon)$
with $i < k$ and $\varepsilon$ true or false, the letter $(i, \mathrm{false})$ standing for the
inverse of the $i$-th generator) with $\varphi(w) = 1$ in $G$ is recursively enumerable.

When $\varphi$ is surjective, this is the same as a presentation of $G$ on the images of the
generators with a recursively enumerable set of relators; it is the enumerable counterpart of a
solvable word problem.

Formalized by `MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.IsRecursivelyPresented`, a definition declared in [WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#is-recursively-presented).

## Right orders of a group

The right orders of `G`: linear orders (as relations) invariant under right multiplication.

Formalized by `MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.rightOrders`, a definition declared in [WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#right-orders).

## The Bludov–Glass question (Kourovka 17.28)

The statement that there exist a soluble group
$G$ that admits a right order, a natural number $k$ and elements $g_0, \dots, g_{k-1}$ generating
$G$ such that, for the homomorphism $\varphi$ from the free group on $k$ generators to $G$ sending
the $i$-th generator to $g_i$, the group $G$ is recursively presented with respect to $\varphi$
and the word problem for $\varphi$ is not solvable. In words: there is a finitely generated,
recursively presented, soluble right-orderable group with insoluble word problem.

Formalized by `MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.solubleRightOrderableInsolubleWordProblem`, a definition declared in [WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#soluble-right-orderable-insoluble-word-p).

## A soluble right-orderable group with insoluble word problem (Kourovka 17.28)

There exist a
soluble group $G$ that admits a right order, a natural number $k$ and elements
$g_0, \dots, g_{k-1}$ generating $G$ such that, for the homomorphism $\varphi$ from the free group
on $k$ generators to $G$ sending the $i$-th generator to $g_i$, the group $G$ is recursively
presented with respect to $\varphi$ and the word problem for $\varphi$ is not solvable.

Resolved true: Darbinyan constructs a two-generated, recursively presented, bi-orderable (hence
right-orderable) soluble group of derived length 3 with undecidable word problem; the Kourovka
Archive answers 17.28 "Yes, there is".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.28 (V. V. Bludov, A. M. W. Glass); resolution: A. Darbinyan, Computability, orders, and solvable groups, J. Symbolic Logic 85 (2020), 1588-1598 (arXiv:1909.05720), abstract, result (2) (a bi-orderable, two-generated, recursively presented solvable group of derived length 3 with undecidable word problem, answering the question of Bludov and Glass); Kourovka Archive, Problem 17.28 (Yes, there is), https://arxiv.org/abs/1909.05720.

Stated but not proved: `MathlibExt.GroupTheory.SolubleRightOrderableWordProblemKourovka17Problem28Wanted.solubleRightOrderableInsolubleWordProblem_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SolubleRightOrderableWordProblemKourovka17Problem28Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html#soluble-right-orderable-insoluble-word-p-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Word problem for orderable groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/orderable-groups/word-problem-for-orderable-groups)
