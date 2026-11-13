---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.FreeMetabelian, MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.SameDistribution, MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.sameDistributionIffAutomorphic, MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.sameDistributionIffAutomorphic_refuted
statement: formalized
---

# Equally distributed elements of free metabelian groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian/index.html).

## Free metabelian group of rank $n$ (Kourovka 19.94)

For a natural number $n$, let $F_n$
be the free group on $n$ generators. The free metabelian group of rank $n$ is the quotient
$M_n = F_n / F_n''$ of $F_n$ by its second derived subgroup $F_n'' = [[F_n, F_n], [F_n, F_n]]$.

Formalized by `MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.FreeMetabelian`, an abbreviation declared in [WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian/index.html#free-metabelian).

## Words with the same distribution

Let $n$ be a natural number and $F_n$ the free group on
generators $x_1, \dots, x_n$. Words $w_1, w_2 \in F_n$ have the same distribution when, for every
finite metabelian group $G$ (that is, $G'' = 1$) and every $g \in G$, the number of tuples
$(a_1, \dots, a_n) \in G^n$ with $w_1(a_1, \dots, a_n) = g$ equals the number of tuples with
$w_2(a_1, \dots, a_n) = g$. Here $w(a_1, \dots, a_n)$ is the image of $w$ under the homomorphism
$F_n \to G$ sending $x_i$ to $a_i$.

Since $G$ is metabelian, this depends only on the images of $w_1, w_2$ in the free metabelian group
$F_n / F_n''$.

Formalized by `MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.SameDistribution`, a definition declared in [WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian/index.html#same-distribution).

## Timoshenko's question on equally distributed elements (Kourovka 19.94)

The statement that
for every natural number $n$ and all words $w_1, w_2$ in the free group $F_n$ of rank $n$, the
words $w_1$ and $w_2$ have the same distribution if and only if some automorphism of the free
metabelian group $M_n = F_n / F_n''$ maps the image of $w_1$ in $M_n$ to the image of $w_2$.

Formalized by `MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.sameDistributionIffAutomorphic`, a definition declared in [WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian/index.html#same-distribution-iff-automorphic).

## Equally distributed elements need not be automorphic (Kourovka 19.94)

It is not the case
that for every natural number $n$ and all words $w_1, w_2$ in the free group $F_n$ of rank $n$,
the words $w_1$ and $w_2$ have the same distribution if and only if some automorphism of the free
metabelian group $M_n = F_n / F_n''$ maps the image of $w_1$ in $M_n$ to the image of $w_2$.

Ionin and Semidetnov (Answer 2.2) give two elements of the free metabelian group of rank $2$ with
the same distribution on every finite metabelian group that no automorphism maps one to the other
(the converse direction is automatic). The solution was found with the assistance of large
language models and checked by the authors; the 21st issue of the Kourovka Notebook marks 19.94
solved ("No, it is not true").

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.94 (E. I. Timoshenko); resolution: V. Ionin and A. Semidetnov, On Some More Problems from the Kourovka Notebook, preprint, arXiv:2608.29219 (2026), Section 2, Answer 2.2 with Proposition 2.3 and Lemmas 2.6-2.7: in M₂ = ⟨x, y⟩ with c = [x, y] and a^z = z⁻¹az, the elements g₁ = c^{x²y⁷}(c^x)⁻¹(c^{xy⁷})⁻¹c and g₂ = c^{x³y⁷}(c^x)⁻¹(c^{x²y⁷})⁻¹c have the same distribution on every finite metabelian group but lie in distinct Aut(M₂)-orbits; found with the assistance of large language models and checked by the authors; the Kourovka Notebook (21st issue) marks 19.94 solved: No, it is not true, https://arxiv.org/abs/2608.29219.

Stated but not proved: `MathlibExt.GroupTheory.FreeMetabelianSameDistributionKourovka19Problem94Wanted.sameDistributionIffAutomorphic_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FreeMetabelianSameDistributionKourovka19Problem94Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian/index.html#same-distribution-iff-automorphic-refute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equally distributed elements of free metabelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/equally-distributed-elements-of-free-metabelian)
