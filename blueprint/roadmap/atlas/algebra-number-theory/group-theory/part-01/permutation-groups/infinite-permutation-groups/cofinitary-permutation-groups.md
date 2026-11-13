---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.IsCofinitary, MathlibExt.GroupTheory.ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.closedCofinitaryLocallyCompact, MathlibExt.GroupTheory.ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.closedCofinitaryLocallyCompact_refuted
statement: formalized
---

# Cofinitary permutation groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/cofinitary-permutation-groups/index.html).

## Cofinitary permutation groups

A subgroup $G$ of the group of permutations of a set
$\Omega$ is cofinitary when every non-identity element of $G$ fixes only finitely many points of
$\Omega$.

Formalized by `MathlibExt.GroupTheory.ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.IsCofinitary`, a definition declared in [WantedExt/GroupTheory/ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/cofinitary-permutation-groups/index.html#is-cofinitary).

## Claim of Kourovka Problem 13.28

For every infinite set $\Omega$, every cofinitary subgroup
$G$ of the group of permutations of $\Omega$ that is closed in the topology of pointwise
convergence is locally compact in the subspace topology.

Formalized by `MathlibExt.GroupTheory.ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.closedCofinitaryLocallyCompact`, a definition declared in [WantedExt/GroupTheory/ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/cofinitary-permutation-groups/index.html#closed-cofinitary-locally-compact).

## Closed cofinitary permutation groups need not be locally compact

The claim of Kourovka
Problem 13.28 is false: there are an infinite set $\Omega$ and a subgroup $G$ of the group of
permutations of $\Omega$ such that $G$ is cofinitary (every non-identity element of $G$ fixes only
finitely many points of $\Omega$) and closed in the topology of pointwise convergence, but $G$ is
not locally compact in the subspace topology.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.28 (D. M. Evans; P. J. Cameron); resolution: G. Hjorth, J. Algebra 200 (1998), no. 2, 439-448, Kourovka Archive, Problem 13.28: No, not always.

Stated but not proved: `MathlibExt.GroupTheory.ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.closedCofinitaryLocallyCompact_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedCofinitaryLocallyCompactKourovka13Problem28Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/cofinitary-permutation-groups/index.html#closed-cofinitary-locally-compact-refute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cofinitary permutation groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/cofinitary-permutation-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/cofinitary-permutation-groups)
