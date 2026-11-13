---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.commutatorIdentityPeriodicDerived, MathlibExt.GroupTheory.CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.commutatorIdentityPeriodicDerived_refuted
statement: formalized
---

# Commutator power identities

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-power-identities/index.html).

## Derived subgroups under a commutator power identity (Kourovka 13.34)

This is the
proposition that for every integer $n \ge 1$ and every group $G$ with $[x, y]^n = 1$ for all
$x, y \in G$, every element of the derived subgroup $[G, G]$ has finite order, that is, the derived
subgroup of $G$ is periodic.

This is Kourovka Notebook Problem 13.34 (I. D. Macdonald).

Formalized by `MathlibExt.GroupTheory.CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.commutatorIdentityPeriodicDerived`, a definition declared in [WantedExt/GroupTheory/CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-power-identities/index.html#commutator-identity-periodic-derived).

## A commutator power identity need not make the derived subgroup periodic

There exist an
integer $n \ge 1$ and a group $G$ such that $[x, y]^n = 1$ for all $x, y \in G$ but some element of
the derived subgroup $[G, G]$ has infinite order. This answers Kourovka Notebook Problem 13.34
(I. D. Macdonald; V. D. Mazurov) in the negative, by results of G. S. Deryabina and P. A.
Kozhevnikov from 1999 and of S. I. Adyan from 2000.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.34 (I. D. Macdonald; V. D. Mazurov); resolution: G. S. Deryabina and P. A. Kozhevnikov, Commun. Algebra 27 (1999), no. 9, 4525-4530; S. I. Adyan, Dokl. Math. 62 (2000), no. 2, 174-176, Kourovka Archive, Problem 13.34: No, not always.

Stated but not proved: `MathlibExt.GroupTheory.CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.commutatorIdentityPeriodicDerived_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CommutatorPowerPeriodicDerivedKourovka13Problem34Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-power-identities/index.html#commutator-identity-periodic-derived-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Commutator power identities](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-power-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/commutator-power-identities)
