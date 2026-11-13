---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.localWordIdentityHoldsGlobally, MathlibExt.GroupTheory.LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.localWordIdentityHoldsGlobally_refuted
statement: formalized
---

# Local word identities

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/local-word-identities/index.html).

## Local word identities in connected groups (Kourovka 18.71)

The statement that for every
connected Hausdorff topological group $G$ and every word $W(x, y)$ in the free group on two
generators $x$, $y$, if $W(a, b) = 1$ for all $(a, b)$ in some nonempty open subset of $G \times G$,
then $W(a, b) = 1$ for all $a, b \in G$.

The problem is posed for connected topological groups; here they are also taken to be Hausdorff,
which weakens the statement.

Formalized by `MathlibExt.GroupTheory.LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.localWordIdentityHoldsGlobally`, a definition declared in [WantedExt/GroupTheory/LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/local-word-identities/index.html#local-word-identity-holds-globally).

## Local word identities need not hold globally in connected groups

There are a connected
Hausdorff topological group $G$, a word $W(x, y)$ in the free group on two generators $x$, $y$ and
a nonempty open subset $U$ of $G \times G$ such that $W(a, b) = 1$ for all $(a, b) \in U$ but
$W(a, b) \ne 1$ for some $a, b \in G$. This answers Kourovka Notebook Problem 18.71 in the
negative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.71 (J. Mycielski); resolution: I. N. Zyabrev and E. A. Reznichenko, On identities in connected topological groups, preprint, arXiv:2406.05203 (2024), abstract: a connected (indeed path-connected) Hausdorff topological group in which, for an odd n, the identity x^n = e holds in some neighbourhood of the identity but not in the whole group; the Kourovka Notebook (21st issue) marks 18.71 solved (odd n > 10^10), https://arxiv.org/abs/2406.05203.

Stated but not proved: `MathlibExt.GroupTheory.LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.localWordIdentityHoldsGlobally_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LocalWordIdentityConnectedGroupKourovka18Problem71Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/local-word-identities/index.html#local-word-identity-holds-globally-refut).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local word identities](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/local-word-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/local-word-identities)
