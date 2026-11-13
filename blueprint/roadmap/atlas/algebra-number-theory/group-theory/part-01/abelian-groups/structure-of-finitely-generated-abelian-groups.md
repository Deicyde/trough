---
declaration: section
origin: cited
lean: elementary_divisors_unique, AddCommGroup.fg_torsion, AddCommGroup.finite_torsion_of_fg, AddCommGroup.torsion_equiv_directSum_zmod_of_fg, AddCommGroup.equiv_free_prod_directSum_invariant_factors, AddCommGroup.equiv_directSum_invariant_factors_of_finite, AddCommGroup.elementary_divisors_equiv_invariant_factors
statement: formalized
proof: formalized
---

# Structure of finitely generated abelian groups

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html).

## Uniqueness of elementary divisors

Let $p$ be a prime and let $A$ be an abelian group.
If $A \cong \bigoplus_{i=1}^{n} \mathbb{Z}/p^{e_i}\mathbb{Z}$ and
$A \cong \bigoplus_{j=1}^{m} \mathbb{Z}/p^{f_j}\mathbb{Z}$ for positive integers
$e_1, \dots, e_n$ and $f_1, \dots, f_m$, then $n = m$ and the multisets
$\{e_1, \dots, e_n\}$ and $\{f_1, \dots, f_m\}$ are equal.

Formalized by `elementary_divisors_unique`, a theorem declared in [MathlibExt/GroupTheory/ElementaryDivisorsUniqueness.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ElementaryDivisorsUniqueness.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#elementary-divisors-unique).

## Torsion subgroup of a finitely generated abelian group is finitely generated

If $A$ is a
finitely generated abelian group, then its torsion subgroup is finitely generated.

Formalized by `AddCommGroup.fg_torsion`, a theorem declared in [MathlibExt/GroupTheory/FiniteAbelian/Torsion.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteAbelian/Torsion.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#fg-torsion).

## Torsion subgroup of a finitely generated abelian group is finite

If $A$ is a finitely
generated abelian group, then its torsion subgroup is finite.

Formalized by `AddCommGroup.finite_torsion_of_fg`, a theorem declared in [MathlibExt/GroupTheory/FiniteAbelian/Torsion.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteAbelian/Torsion.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#finite-torsion-of-fg).

## Torsion subgroup of a finitely generated abelian group as a sum of cyclic groups

If $A$
is a finitely generated abelian group, then there exist a natural number $n$ and positive
integers $d_1, \dots, d_n$ such that the torsion subgroup of $A$ is isomorphic to the direct sum
$\mathbb{Z}/d_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/d_n\mathbb{Z}$ of finite cyclic groups.

Formalized by `AddCommGroup.torsion_equiv_directSum_zmod_of_fg`, a theorem declared in [MathlibExt/GroupTheory/FiniteAbelian/Torsion.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/FiniteAbelian/Torsion.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#torsion-equiv-direct-sum-zmod-of-fg).

## Fundamental theorem of finitely generated abelian groups, invariant factor form

Every
finitely generated abelian group $A$ is isomorphic to
$\mathbb{Z}^a \times \bigoplus_{i < k} \mathbb{Z}/d_i\mathbb{Z}$ for some $a, k \in \mathbb{N}$
and natural numbers $d_0, \dots, d_{k-1}$ with $d_i > 1$ for every $i$ and $d_i \mid d_j$
whenever $i \le j$.

Formalized by `AddCommGroup.equiv_free_prod_directSum_invariant_factors`, a theorem declared in [MathlibExt/GroupTheory/InvariantFactors.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/InvariantFactors.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#equiv-free-prod-direct-sum-invariant-fac).

## Invariant factor decomposition of finite abelian groups

Every finite abelian group $A$
is isomorphic to $\bigoplus_{i < k} \mathbb{Z}/d_i\mathbb{Z}$ for some $k \in \mathbb{N}$ and
natural numbers $d_0, \dots, d_{k-1}$ with $d_i > 1$ for every $i$ and $d_i \mid d_j$ whenever
$i \le j$.

Formalized by `AddCommGroup.equiv_directSum_invariant_factors_of_finite`, a theorem declared in [MathlibExt/GroupTheory/InvariantFactors.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/InvariantFactors.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#equiv-direct-sum-invariant-factors-of-fi).

## From elementary divisors to invariant factors

Let $I$ be a finite set, and for each
$i \in I$ let $p_i$ be a prime and $e_i$ a natural number. Then there are $k \in \mathbb{N}$ and
natural numbers $d_0, \dots, d_{k-1}$ with $d_j > 1$ for every $j$ and $d_j \mid d_l$ whenever
$j \le l$, such that $\bigoplus_{i \in I} \mathbb{Z}/p_i^{e_i}\mathbb{Z}$ is isomorphic to
$\bigoplus_{j < k} \mathbb{Z}/d_j\mathbb{Z}$.

Exponent zero is allowed, giving a trivial summand.

Formalized by `AddCommGroup.elementary_divisors_equiv_invariant_factors`, a theorem declared in [MathlibExt/GroupTheory/InvariantFactors.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/InvariantFactors.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html#elementary-divisors-equiv-invariant-fact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Structure of finitely generated abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/abelian-groups/structure-of-finitely-generated-abelian-groups)
