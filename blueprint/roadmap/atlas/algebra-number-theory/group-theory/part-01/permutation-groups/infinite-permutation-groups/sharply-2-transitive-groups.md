---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.IsSharplyTwoTransitive, MathlibExt.GroupTheory.SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.sharplyTwoTransitiveHasAbelianNormal, MathlibExt.GroupTheory.SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.sharplyTwoTransitiveHasAbelianNormal_refuted
statement: formalized
---

# Sharply 2-transitive groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/sharply-2-transitive-groups/index.html).

## Sharply doubly transitive action

An action of a group $G$ on a set $\Omega$ is sharply
doubly transitive when for all points $\alpha, \beta, \gamma, \delta \in \Omega$ with
$\alpha \ne \beta$ and $\gamma \ne \delta$ there is exactly one $g \in G$ with
$g \cdot \alpha = \gamma$ and $g \cdot \beta = \delta$.

Formalized by `MathlibExt.GroupTheory.SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.IsSharplyTwoTransitive`, a definition declared in [WantedExt/GroupTheory/SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/sharply-2-transitive-groups/index.html#is-sharply-two-transitive).

## Mazurov's question on sharply 2-transitive groups (Kourovka 11.52)

The statement that every
group $G$ acting sharply doubly transitively on a set $\Omega$ with at least two points has a
nontrivial abelian normal subgroup.

Formalized by `MathlibExt.GroupTheory.SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.sharplyTwoTransitiveHasAbelianNormal`, a definition declared in [WantedExt/GroupTheory/SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/sharply-2-transitive-groups/index.html#sharply-two-transitive-has-abelian-norma).

## A sharply 2-transitive group without nontrivial abelian normal subgroups

The statement of
Kourovka Problem 11.52 is false: there is a group $G$ acting sharply doubly transitively on a set
$\Omega$ with at least two points such that no nontrivial normal subgroup of $G$ is abelian.

Rips, Segev and Tent construct such a group; the Kourovka Archive answers 11.52 "No, not every".
For finite groups the answer is yes, by Frobenius's theorem.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.52 (V. D. Mazurov); resolution: E. Rips, Y. Segev and K. Tent, J. Eur. Math. Soc. 19, no. 10 (2017), 2895-2910, Kourovka Archive, Problem 11.52: "No, not every", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.sharplyTwoTransitiveHasAbelianNormal_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SharplyTwoTransitiveAbelianNormalKourovka11Problem52Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/sharply-2-transitive-groups/index.html#sharply-two-transitive-has-abelian-norma-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sharply 2-transitive groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/sharply-2-transitive-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/sharply-2-transitive-groups)
