---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.freeActionEmbedsInSkewField, MathlibExt.GroupTheory.FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.freeActionEmbedsInSkewField_refuted
statement: formalized
---

# Groups acting freely on abelian groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/groups-acting-freely-on-abelian-groups/index.html).

## Kourovka Problem 16.54 (free actions and embeddings in skew-fields)

The statement, a
question of V. D. Mazurov, that every group $G$ with a free action by automorphisms on a
nontrivial abelian group $V$, meaning $g \cdot v \ne v$ for all $g \ne 1$ in $G$ and all $v \ne 0$
in $V$, has an injective homomorphism into the multiplicative group of some division ring.

Formalized by `MathlibExt.GroupTheory.FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.freeActionEmbedsInSkewField`, a definition declared in [WantedExt/GroupTheory/FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/groups-acting-freely-on-abelian-groups/index.html#free-action-embeds-in-skew-field).

## Groups acting freely on abelian groups need not embed in skew-fields (Kourovka 16.54)

There
is a group $G$ with an action by automorphisms on a nontrivial abelian group $V$ such that
$g \cdot v \ne v$ for all $g \ne 1$ in $G$ and all $v \ne 0$ in $V$, but with no injective
homomorphism into the multiplicative group of any division ring. This answers Kourovka
Problem 16.54 in the negative.

The Kourovka Archive answers "No, it is not" (Nedrenko): the group $2.A_5.2$ with a quaternion
Sylow $2$-subgroup acts freely on an elementary abelian group of order $7^4$, but by Theorem 7 of
Amitsur's classification of finite subgroups of division rings it does not embed in the
multiplicative group of any skew-field.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.54 (V. D. Mazurov); resolution: D. Nedrenko, letter of 20 January 2014, as recorded in the Kourovka Archive; S. A. Amitsur, Finite subgroups of division rings, Trans. Amer. Math. Soc. 80 (1955), 361-386, Kourovka Archive, Problem 16.54 (No: 2.A_5.2 with a quaternion Sylow 2-subgroup acts freely on an elementary abelian group of order 7^4 but does not embed in the multiplicative group of a skew-field, by Amitsur's Theorem 7).

Stated but not proved: `MathlibExt.GroupTheory.FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.freeActionEmbedsInSkewField_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeActionSkewFieldEmbeddingKourovka16Problem54Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/groups-acting-freely-on-abelian-groups/index.html#free-action-embeds-in-skew-field-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups acting freely on abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/groups-acting-freely-on-abelian-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/groups-acting-freely-on-abelian-groups)
