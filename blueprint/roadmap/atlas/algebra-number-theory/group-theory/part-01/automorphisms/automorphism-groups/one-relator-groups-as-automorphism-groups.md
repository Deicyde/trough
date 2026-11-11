---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OneRelatorAutomorphismGroupKourovka16Problem75Wanted.oneRelatorGroupIsAutomorphismGroup, MathlibExt.GroupTheory.OneRelatorAutomorphismGroupKourovka16Problem75Wanted.oneRelatorGroupIsAutomorphismGroup_holds
statement: formalized
---

# One-relator groups as automorphism groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/one-relator-groups-as-automorphism-groups/index.html).

## Kourovka Problem 16.75: one-relator automorphism groups

The proposition that there exist
a natural number $n$ and an element $r$ of the free group on generators $x_0, \dots, x_{n-1}$ such
that the one-relator group $\langle x_0, \dots, x_{n-1} \mid r \rangle$ is non-abelian and is
isomorphic to the automorphism group $\operatorname{Aut}(H)$ of some group $H$. The problem is due
to M. V. Neshchadim.

Formalized by `MathlibExt.GroupTheory.OneRelatorAutomorphismGroupKourovka16Problem75Wanted.oneRelatorGroupIsAutomorphismGroup`, a definition declared in [WantedExt/GroupTheory/OneRelatorAutomorphismGroupKourovka16Problem75Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OneRelatorAutomorphismGroupKourovka16Problem75Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/one-relator-groups-as-automorphism-groups/index.html#one-relator-group-is-automorphism-group).

## Some non-abelian one-relator group is an automorphism group

There exist a natural number $n$
and an element $r$ of the free group on generators $x_0, \dots, x_{n-1}$ such that the one-relator
group $\langle x_0, \dots, x_{n-1} \mid r \rangle$ is non-abelian and is isomorphic to the
automorphism group $\operatorname{Aut}(H)$ of some group $H$. This answers Kourovka Problem 16.75
in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.75 (M. V. Neshchadim); resolution: D. J. Collins, Proc. London Math. Soc. (3) 36 (1978), no. 3, 480-493; V. A. Churkin, letter of 5 April 2006, as recorded in the Kourovka Archive, Kourovka Archive, Problem 16.75 (Yes, it can: for integers r, s with gcd(r, s) = 1, |r| ≠ |s| and r - s even, G = ⟨a, b | a⁻¹ b^r a = b^s⟩ is isomorphic to Aut(Aut(G)), Collins).

Stated but not proved: `MathlibExt.GroupTheory.OneRelatorAutomorphismGroupKourovka16Problem75Wanted.oneRelatorGroupIsAutomorphismGroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OneRelatorAutomorphismGroupKourovka16Problem75Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OneRelatorAutomorphismGroupKourovka16Problem75Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/one-relator-groups-as-automorphism-groups/index.html#one-relator-group-is-automorphism-group-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: One-relator groups as automorphism groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/one-relator-groups-as-automorphism-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/one-relator-groups-as-automorphism-groups)
