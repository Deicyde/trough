---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SmallSubsetsSeparatedKourovka17Problem102Wanted.AreSeparated, MathlibExt.GroupTheory.SmallSubsetsSeparatedKourovka17Problem102Wanted.smallDisjointSubsetsSeparated, MathlibExt.GroupTheory.SmallSubsetsSeparatedKourovka17Problem102Wanted.smallDisjointSubsetsSeparated_refuted
statement: formalized
---

# Separated subsets of groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/separated-subsets-of-groups/index.html).

## Separated subsets of a group

Two subsets $A$ and $B$ of a group $G$ are separated, in the
sense of I. V. Protasov, when there is an infinite subset $X \subseteq G$ with $1 \in X$,
$X^{-1} = X$ and $XAX \cap B = \emptyset$, where $XAX = \{x a y : x, y \in X,\ a \in A\}$.

Formalized by `MathlibExt.GroupTheory.SmallSubsetsSeparatedKourovka17Problem102Wanted.AreSeparated`, a definition declared in [WantedExt/GroupTheory/SmallSubsetsSeparatedKourovka17Problem102Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SmallSubsetsSeparatedKourovka17Problem102Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/separated-subsets-of-groups/index.html#are-separated).

## Separation of small disjoint subsets of infinite groups (Kourovka 17.102)

The statement,
posed by I. V. Protasov, that for every infinite group $G$ and all disjoint subsets
$A, B \subseteq G$ with $|A| < |G|$ and $|B| < |G|$, the sets $A$ and $B$ are separated.

Formalized by `MathlibExt.GroupTheory.SmallSubsetsSeparatedKourovka17Problem102Wanted.smallDisjointSubsetsSeparated`, a definition declared in [WantedExt/GroupTheory/SmallSubsetsSeparatedKourovka17Problem102Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SmallSubsetsSeparatedKourovka17Problem102Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/separated-subsets-of-groups/index.html#small-disjoint-subsets-separated).

## Small disjoint subsets of an infinite group need not be separated

There exist an infinite
group $G$ and disjoint subsets $A, B \subseteq G$ with $|A| < |G|$ and $|B| < |G|$ such that $A$
and $B$ are not separated. That is, the statement of Kourovka Problem 17.102 is false.

Resolved false: Wan (Theorem 1.1) takes $G = \mathrm{Sym}(\mathbb{N})$ and splits the set of
transpositions into $A$ and $B$ using a graph on $\mathbb{N}$ with trivial automorphism group, so
that $|A| = |B| = \aleph_0 < 2^{\aleph_0}$. The Kourovka Notebook (21st issue) answers 17.102
"No, not always".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 17.102 (I. V. Protasov); resolution: S. Wan, Counterexamples to Problem 17.102 of The Kourovka Notebook, preprint, arXiv:2608.00504 (2026), Theorem 1.1 (an infinite group G with disjoint A, B, |A|, |B| < |G|, not separated; in the proof G = Sym(N) and A, B split the transpositions by a rigid graph on N); the Kourovka Notebook (21st issue) marks 17.102 solved (No, not always), https://arxiv.org/abs/2608.00504.

Stated but not proved: `MathlibExt.GroupTheory.SmallSubsetsSeparatedKourovka17Problem102Wanted.smallDisjointSubsetsSeparated_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SmallSubsetsSeparatedKourovka17Problem102Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SmallSubsetsSeparatedKourovka17Problem102Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/separated-subsets-of-groups/index.html#small-disjoint-subsets-separated-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Separated subsets of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/separated-subsets-of-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/combinatorics-in-groups/separated-subsets-of-groups)
