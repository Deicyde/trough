---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidRelators, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.BraidGroup, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidNonInjectiveNoncyclicEndomorphism, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidCommutatorEndomorphismAutomorphism, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidTorsionFreeNonabelianProperQuotient, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidNonInjectiveNoncyclicEndomorphism_refuted, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidCommutatorEndomorphismAutomorphism_holds, MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidTorsionFreeNonabelianProperQuotient_holds
statement: formalized
---

# Endomorphisms of braid groups

8 results, 5 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html).

## Artin's braid relators

Artin's relators for the braid group on `n` strands, in the free group on the generators
`σ₀, …, σ_{n-2}` (indexed by `Fin (n - 1)`): `σᵢ σⱼ = σⱼ σᵢ` when `j ≥ i + 2`, and
`σᵢ σᵢ₊₁ σᵢ = σᵢ₊₁ σᵢ σᵢ₊₁`.

Formalized by `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidRelators`, a definition declared in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-relators).

## Braid group on n strands

The braid group `Bₙ` on `n` strands, by Artin's presentation.

Formalized by `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.BraidGroup`, an abbreviation declared in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-group).

## Kourovka Problem 14.102(a): non-injective braid endomorphisms with non-cyclic image

The
statement that for some $n > 4$ the braid group $B_n$ on $n$ strands has a non-injective
endomorphism whose image is not cyclic (in particular not trivial). Posed by V. Lin and
V. Shpilrain.

Formalized by `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidNonInjectiveNoncyclicEndomorphism`, a definition declared in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-non-injective-noncyclic-endomorphi).

## Kourovka Problem 14.102(b): endomorphisms of the braid commutator subgroup

The statement
that for every $n > 4$, every endomorphism of the commutator subgroup $[B_n, B_n]$ of the braid
group $B_n$ on $n$ strands other than the trivial endomorphism is bijective, that is, an
automorphism. Posed by V. Lin and V. Shpilrain.

Formalized by `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidCommutatorEndomorphismAutomorphism`, a definition declared in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-commutator-endomorphism-automorphi).

## Kourovka Problem 14.102(c): torsion-free quotients of braid groups

The statement that for
every $n > 4$, the braid group $B_n$ on $n$ strands has a nontrivial normal subgroup $N$ such that
the quotient $B_n / N$ is non-abelian and torsion-free (no element other than the identity has
finite order). Posed by V. Lin and V. Shpilrain.

Formalized by `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidTorsionFreeNonabelianProperQuotient`, a definition declared in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-torsion-free-nonabelian-proper-quo).

## Non-injective endomorphisms of braid groups on five or more strands have cyclic image

The
answer to Kourovka Problem 14.102(a) is negative: there is no $n > 4$ for which the braid group
$B_n$ on $n$ strands has a non-injective endomorphism whose image is not cyclic. Equivalently, for
every $n \ge 5$, every non-injective endomorphism of $B_n$ has cyclic image.

This was proved by Castel for $n \ge 6$ and by Chen, Kordek and Margalit for $n = 5$; the Kourovka
Notebook (21st issue) answers 14.102(a) "No".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.102 (V. Lin; V. Shpilrain); part (c) in the Archive of Solved Problems; resolution: (a) F. Castel, Geometric representations of the braid groups, Astérisque 378 (2016) (n ≥ 6), and L. Chen, K. Kordek and D. Margalit, Homomorphisms between braid groups, arXiv:1910.00712 (n = 5); (b) S. Orevkov, Ann. Fac. Sci. Toulouse Math. 33 (2024), no. 1, 105-121, extending K. Kordek and D. Margalit, Bull. London Math. Soc. 54 (2022), 95-111 (n ≥ 7); (c) P. Linnell and T. Schick, J. Amer. Math. Soc. 20 (2007), no. 4, 1003-1051, the Kourovka Notebook (21st issue) marks 14.102(a), (b) solved (for n ≥ 5 every non-injective endomorphism of B_n has cyclic image; every non-trivial endomorphism of [B_n, B_n] is an automorphism); Kourovka Archive, Problem 14.102(c) (Yes), https://arxiv.org/abs/1910.00712.

Stated but not proved: `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidNonInjectiveNoncyclicEndomorphism_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-non-injective-noncyclic-endomorphi-2).

## Nontrivial endomorphisms of the braid commutator subgroup on five or more strands are automorphisms

**Nontrivial endomorphisms of the braid commutator subgroup on five or more strands are
automorphisms.** For every $n > 4$, every endomorphism of the commutator subgroup $[B_n, B_n]$ of
the braid group $B_n$ on $n$ strands other than the trivial endomorphism is bijective, that is, an
automorphism.

This was proved by Kordek and Margalit for $n \ge 7$ and extended by Orevkov to all $n \ge 5$; the
Kourovka Notebook (21st issue) answers 14.102(b) "Yes".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.102 (V. Lin; V. Shpilrain); part (c) in the Archive of Solved Problems; resolution: (a) F. Castel, Geometric representations of the braid groups, Astérisque 378 (2016) (n ≥ 6), and L. Chen, K. Kordek and D. Margalit, Homomorphisms between braid groups, arXiv:1910.00712 (n = 5); (b) S. Orevkov, Ann. Fac. Sci. Toulouse Math. 33 (2024), no. 1, 105-121, extending K. Kordek and D. Margalit, Bull. London Math. Soc. 54 (2022), 95-111 (n ≥ 7); (c) P. Linnell and T. Schick, J. Amer. Math. Soc. 20 (2007), no. 4, 1003-1051, the Kourovka Notebook (21st issue) marks 14.102(a), (b) solved (for n ≥ 5 every non-injective endomorphism of B_n has cyclic image; every non-trivial endomorphism of [B_n, B_n] is an automorphism); Kourovka Archive, Problem 14.102(c) (Yes), https://arxiv.org/abs/1910.00712.

Stated but not proved: `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidCommutatorEndomorphismAutomorphism_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-commutator-endomorphism-automorphi-2).

## Braid groups on five or more strands have proper non-abelian torsion-free quotients

For
every $n > 4$, the braid group $B_n$ on $n$ strands has a nontrivial normal subgroup $N$ such that
the quotient $B_n / N$ is non-abelian and torsion-free (no element other than the identity has
finite order).

The Kourovka Archive answers 14.102(c) "Yes, it does", citing Linnell and Schick (every braid group
is residually torsion-free nilpotent-by-finite); Humphries had constructed such quotients for
$n < 7$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.102 (V. Lin; V. Shpilrain); part (c) in the Archive of Solved Problems; resolution: (a) F. Castel, Geometric representations of the braid groups, Astérisque 378 (2016) (n ≥ 6), and L. Chen, K. Kordek and D. Margalit, Homomorphisms between braid groups, arXiv:1910.00712 (n = 5); (b) S. Orevkov, Ann. Fac. Sci. Toulouse Math. 33 (2024), no. 1, 105-121, extending K. Kordek and D. Margalit, Bull. London Math. Soc. 54 (2022), 95-111 (n ≥ 7); (c) P. Linnell and T. Schick, J. Amer. Math. Soc. 20 (2007), no. 4, 1003-1051, the Kourovka Notebook (21st issue) marks 14.102(a), (b) solved (for n ≥ 5 every non-injective endomorphism of B_n has cyclic image; every non-trivial endomorphism of [B_n, B_n] is an automorphism); Kourovka Archive, Problem 14.102(c) (Yes), https://arxiv.org/abs/1910.00712.

Stated but not proved: `MathlibExt.GroupTheory.BraidGroupEndomorphismsKourovka14Problem102Wanted.braidTorsionFreeNonabelianProperQuotient_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/BraidGroupEndomorphismsKourovka14Problem102Wanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html#braid-torsion-free-nonabelian-proper-quo-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Endomorphisms of braid groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/endomorphisms-of-braid-groups)
