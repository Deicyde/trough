---
declaration: section
origin: cited
lean: Submodule.natCard_torsionBy_quotient_eq_pow_finrank, MathlibExt.GroupTheory.PureSubgroupShared.IsPureSubgroup
statement: formalized
proof: formalized
---

# Abelian groups: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/index.html).

Structure of abelian groups: finite and finitely generated abelian groups (invariant factors, elementary divisors, torsion, ranks, dual groups), torsion-free and infinite abelian groups (Baer–Specker group, pure subgroups, direct-sum cancellation, ultraproducts of abelian groups); colourings and partitions of abelian groups go to Combinatorics in groups.

## Cardinality of the $n$-torsion of a vector space modulo a lattice

The `n`-torsion of the quotient of a vector space by a free finite
lattice has cardinality `n ^ finrank L`.

This counts torsion points: for a lattice `L` of rank `r` in a vector
space, the `n`-torsion subgroup of `V ⧸ L` has `n ^ r` elements. It is
used for torsion in abelian varieties and elliptic curves, for class group
computations, and for lattice index arguments.

Formalized by `Submodule.natCard_torsionBy_quotient_eq_pow_finrank`, a theorem declared in [MathlibExt/Algebra/Module/TorsionQuotient.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/Module/TorsionQuotient.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/index.html#nat-card-torsion-by-quotient-eq-pow-finr).

## Pure subgroups of abelian groups

A subgroup $B$ of an abelian group $A$ is pure when
$nA \cap B = nB$ for every integer $n$: for every integer $n$ and every $a \in A$ with
$na \in B$ there is some $b \in B$ with $nb = na$.

Formalized by `MathlibExt.GroupTheory.PureSubgroupShared.IsPureSubgroup`, a definition declared in [WantedExt/GroupTheory/PureSubgroupShared.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureSubgroupShared.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/index.html#is-pure-subgroup).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/abelian-groups)
