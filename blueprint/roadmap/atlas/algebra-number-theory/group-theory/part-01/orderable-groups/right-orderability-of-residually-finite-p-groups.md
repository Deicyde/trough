---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.IsRightOrderable, MathlibExt.GroupTheory.ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.residuallyTwoPrimesNotRightOrderable, MathlibExt.GroupTheory.ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.residuallyTwoPrimesNotRightOrderable_holds
statement: formalized
---

# Right-orderability of residually finite p-groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/right-orderability-of-residually-finite-p-groups/index.html).

## Right-orderable groups

A group $G$ is right-orderable when it admits a linear order $\le$
that is invariant under right multiplication: $a \le b$ implies $ac \le bc$ for all
$a, b, c \in G$.

Formalized by `MathlibExt.GroupTheory.ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.IsRightOrderable`, a definition declared in [WantedExt/GroupTheory/ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/right-orderability-of-residually-finite-p-groups/index.html#is-right-orderable).

## Medvedev's question on right-orderability (Kourovka 10.30)

The statement that there exist
a group $G$ and distinct primes $p$ and $q$ such that $G$ is residually a finite $p$-group and
residually a finite $q$-group, but $G$ is not right-orderable.

Formalized by `MathlibExt.GroupTheory.ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.residuallyTwoPrimesNotRightOrderable`, a definition declared in [WantedExt/GroupTheory/ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/right-orderability-of-residually-finite-p-groups/index.html#residually-two-primes-not-right-orderabl).

## A non-right-orderable group that is residually $p$ for two primes (Linnell)

There exist a
group $G$ and distinct primes $p$ and $q$ such that $G$ is residually a finite $p$-group and
residually a finite $q$-group but is not right-orderable.

By Rhemtulla, a group that is residually a finite $p$-group for infinitely many primes $p$ is
orderable.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.30 (N. Ya. Medvedev); resolution: P. A. Linnell, J. Algebra 248 (2002), 605-607, Kourovka Archive, Problem 10.30 ("Yes, there does").

Stated but not proved: `MathlibExt.GroupTheory.ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.residuallyTwoPrimesNotRightOrderable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ResiduallyTwoPrimesNotRightOrderableKourovka10Problem30Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/right-orderability-of-residually-finite-p-groups/index.html#residually-two-primes-not-right-orderabl-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Right-orderability of residually finite p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/orderable-groups/right-orderability-of-residually-finite-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/orderable-groups/right-orderability-of-residually-finite-p-groups)
