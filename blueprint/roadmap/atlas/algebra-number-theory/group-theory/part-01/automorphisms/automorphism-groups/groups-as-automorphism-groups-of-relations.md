---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ScottishBook142Wanted.IsAutomorphismGroupOf, MathlibExt.GroupTheory.ScottishBook142Wanted.everyGroupIsAutomorphismGroupOfBinaryRelation
statement: formalized
---

# Groups as automorphism groups of relations

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-automorphism-groups-of-relations/index.html).

## Full automorphism group of a binary relation

Let $G$ be a group, $Z$ a set and
$X \subseteq Z \times Z$ a binary relation on $Z$. Then $G$ is the full automorphism group of
$X$ when there is an injective group homomorphism $\varphi$ from $G$ to the group of
permutations of $Z$ whose image is exactly the set of permutations $f$ of $Z$ with
$(x, y) \in X \iff (f(x), f(y)) \in X$ for all $x, y \in Z$.

Formalized by `MathlibExt.GroupTheory.ScottishBook142Wanted.IsAutomorphismGroupOf`, a definition declared in [WantedExt/GroupTheory/ScottishBook142Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook142Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-automorphism-groups-of-relations/index.html#is-automorphism-group-of).

## Birkhoff's theorem: every group is the automorphism group of a binary relation

For every
group $G$ there are a set $Z$ and a binary relation $X \subseteq Z \times Z$ such that $G$ is
the full automorphism group of $X$: there is an injective group homomorphism $\varphi$ from $G$
to the group of permutations of $Z$ whose image is exactly the set of permutations $f$ of $Z$
with $(x, y) \in X \iff (f(x), f(y)) \in X$ for all $x, y \in Z$.

The set $Z$ lies in the same universe as $G$.

## Sources

- S. Ulam, Problem 142 of the Scottish Book, headed "Problem (Ulam) - Theorem (Garrett Birkhoff)"; the representation is Birkhoff's theorem.

Stated but not proved: `MathlibExt.GroupTheory.ScottishBook142Wanted.everyGroupIsAutomorphismGroupOfBinaryRelation` is written with `theorem_wanted` in [WantedExt/GroupTheory/ScottishBook142Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook142Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-automorphism-groups-of-relations/index.html#every-group-is-automorphism-group-of-bin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups as automorphism groups of relations](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-automorphism-groups-of-relations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-automorphism-groups-of-relations)
