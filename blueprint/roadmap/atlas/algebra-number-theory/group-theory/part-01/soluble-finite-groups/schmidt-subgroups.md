---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.IsMinimalNonNilpotent, MathlibExt.GroupTheory.MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.permutesMinimalNonNilpotentCoreQuotientNilpotent, MathlibExt.GroupTheory.MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.permutesMinimalNonNilpotentCoreQuotientNilpotent_refuted, MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.IsSchmidtSubgroup, MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.IsPSubnormal, MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.schmidtSubgroupsPSubnormalImpliesSoluble, MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.schmidtSubgroupsPSubnormalImpliesSoluble_holds, MathlibExt.GroupTheory.SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.schmidtSigmaSubnormalCyclicQuotient
statement: formalized
---

# Schmidt subgroups

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html).

## Minimal non-nilpotent subgroup

A subgroup $M$ of a group $G$ is minimal non-nilpotent if
$M$ is not nilpotent but every proper subgroup of $M$ is nilpotent.

Formalized by `MathlibExt.GroupTheory.MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.IsMinimalNonNilpotent`, a definition declared in [WantedExt/GroupTheory/MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#is-minimal-non-nilpotent).

## Subgroups permuting with all minimal non-nilpotent subgroups (Kourovka 17.56)

The
statement that if $H$ is a subgroup of a finite group $G$ with $HM = MH$ (as sets of products) for
every minimal non-nilpotent subgroup $M$ of $G$, then the quotient $H/H_G$ is nilpotent, where the
normal core $H_G$ is the largest normal subgroup of $G$ contained in $H$.

The question is due to V. N. Knyagina and V. S. Monakhov.

Formalized by `MathlibExt.GroupTheory.MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.permutesMinimalNonNilpotentCoreQuotientNilpotent`, a definition declared in [WantedExt/GroupTheory/MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#permutes-minimal-non-nilpotent-core-quot).

## Permutability with minimal non-nilpotent subgroups does not force a nilpotent core quotient

There exist a finite group $G$ and a subgroup $H$ of $G$ with $HM = MH$ (as sets of products) for
every minimal non-nilpotent subgroup $M$ of $G$ such that the quotient $H/H_G$ is not nilpotent,
where the normal core $H_G$ is the largest normal subgroup of $G$ contained in $H$.

This answers Kourovka Problem 17.56 in the negative (Ballester-Bolinches, Esteban-Romero,
Kamornikov and Pérez-Calabuig, 2022).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 17.56 (V. N. Knyagina, V. S. Monakhov); resolution: A. Ballester-Bolinches, R. Esteban-Romero, S. F. Kamornikov and V. Pérez-Calabuig, J. Algebra 608 (2022), 382-387, the Kourovka Notebook (21st issue) marks 17.56 solved (No, not always).

Stated but not proved: `MathlibExt.GroupTheory.MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.permutesMinimalNonNilpotentCoreQuotientNilpotent_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MinimalNonNilpotentPermutableCoreKourovka17Problem56Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#permutes-minimal-non-nilpotent-core-quot-2).

## Schmidt subgroup

A subgroup $H$ of a group $G$ is a Schmidt subgroup when $H$ is not
nilpotent but every proper subgroup of $H$ is nilpotent.

Finiteness of $H$ is not part of this definition.

Formalized by `MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.IsSchmidtSubgroup`, a definition declared in [WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#is-schmidt-subgroup).

## $\mathbb{P}$-subnormal subgroup

A subgroup $H$ of a group $G$ is $\mathbb{P}$-subnormal in
$G$ when $H = G$ or there is a chain of subgroups $H = H_0 < H_1 < \cdots < H_n = G$ in which every
index $|H_i : H_{i-1}|$ is a prime number.

Formalized by `MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.IsPSubnormal`, a definition declared in [WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#is-psubnormal).

## Claim of Kourovka Problem 18.30

The statement that every finite group in which every
Schmidt subgroup is $\mathbb{P}$-subnormal is soluble. The problem is due to A. F. Vasil'ev,
T. I. Vasil'eva and V. N. Tyutyanov.

Formalized by `MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.schmidtSubgroupsPSubnormalImpliesSoluble`, a definition declared in [WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#schmidt-subgroups-psubnormal-implies-sol).

## Finite groups with $\mathbb{P}$-subnormal Schmidt subgroups are soluble

Every finite group in
which every Schmidt subgroup is $\mathbb{P}$-subnormal is soluble. This answers Kourovka Notebook
Problem 18.30 in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.30 (A. F. Vasil'ev, T. I. Vasil'eva, V. N. Tyutyanov); resolution: V. N. Tyutyanov, Probl. Fiz. Mat. Tekhn. 2015, no. 1 (22), 88-91 (Russian), Kourovka Archive, Problem 18.30: Yes, it must, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.schmidtSubgroupsPSubnormalImpliesSoluble_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SchmidtSubgroupsPrimeSubnormalKourovka18Problem30Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#schmidt-subgroups-psubnormal-implies-sol-2).

## Claim of Kourovka Problem 19.85

The statement that for every partition $\sigma$ of the set
of all primes into nonempty pairwise disjoint blocks and every finite group $G$ in which every
Schmidt subgroup is $\sigma$-subnormal, $G$ has a normal $\sigma$-nilpotent subgroup $N$ such that
$G / N$ is cyclic: there is $g \in G$ such that every $x \in G$ satisfies $x g^{-k} \in N$ for some
integer $k$. The problem is due to A. N. Skiba.

Formalized by `MathlibExt.GroupTheory.SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.schmidtSigmaSubnormalCyclicQuotient`, a definition declared in [WantedExt/GroupTheory/SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#schmidt-sigma-subnormal-cyclic-quotient).

## Finite groups with $\sigma$-subnormal Schmidt subgroups are $\sigma$-nilpotent-by-cyclic

Let
$\sigma$ be a partition of the set of all primes into nonempty pairwise disjoint blocks, and let $G$
be a finite group in which every Schmidt subgroup is $\sigma$-subnormal. Then $G$ has a normal
$\sigma$-nilpotent subgroup $N$ such that $G / N$ is cyclic: there is $g \in G$ such that every
$x \in G$ satisfies $x g^{-k} \in N$ for some integer $k$. This answers Kourovka Notebook
Problem 19.85 in the affirmative.

Yi and Kamornikov prove that $G / F_\sigma(G)$ is cyclic, where $F_\sigma(G)$ is the largest normal
$\sigma$-nilpotent subgroup of $G$; for nilpotent $G$ one takes $N = G$. The case of the partition
of the primes into single primes was known before.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 19.85 (A. N. Skiba); resolution: X. Yi and S. F. Kamornikov, Finite groups with σ-subnormal Schmidt subgroups, J. Algebra 560 (2020), 181-191, main result, quoted as Lemma 8 (reference [11]) in A. Ballester-Bolinches, S. F. Kamornikov and X. Yi, Finite groups with σ-subnormal Schmidt subgroups, Bull. Malays. Math. Sci. Soc. (2022): if every Schmidt subgroup of a non-nilpotent group G is σ-subnormal, then G / F_σ(G) is cyclic, F_σ(G) the largest normal σ-nilpotent subgroup; Kourovka Archive, Problem 19.85: Yes, it is true, https://doi.org/10.1007/s40840-022-01369-y.

Stated but not proved: `MathlibExt.GroupTheory.SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.schmidtSigmaSubnormalCyclicQuotient_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SchmidtSubgroupsSigmaSubnormalKourovka19Problem85Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html#schmidt-sigma-subnormal-cyclic-quotient-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schmidt subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/soluble-finite-groups/schmidt-subgroups)
