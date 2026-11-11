---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.STCONNLComplete.stconDec, MetaMathlibExt.Complexity.KeyTheorems.STCONNLComplete.stcon_nl_complete
statement: formalized
---

# Directed s-t connectivity

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/directed-s-t-connectivity/index.html).

## Directed $s$-$t$ connectivity

The decision problem of directed $s$-$t$ connectivity
accepts a bitstring $x$ exactly when decoding $x$ with the canonical bitstring encoding of
tuples $(n, E, s, t)$, where $n$, $s$ and $t$ are natural numbers and $E$ is a list of pairs of
natural numbers, succeeds and gives a tuple such that $s < n$, $t < n$, and there are pairwise
distinct natural numbers $v_0, \dots, v_k$, all less than $n$, with $v_0 = s$, $v_k = t$ and
$(v_j, v_{j+1}) \in E$ for every $j < k$. Bitstrings that do not decode are rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.STCONNLComplete.stconDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/STCONNLCompleteWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/STCONNLCompleteWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/directed-s-t-connectivity/index.html#stcon-dec).

## ST-connectivity is NL-complete

Directed $s$-$t$ connectivity is in NL, and every
decision problem in NL is log-space many-one reducible to directed $s$-$t$ connectivity.

## Sources

- S. A. Cook, "A hierarchy for nondeterministic time complexity" (1973) and the standard NL-completeness of directed reachability; see S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Chapter 4, and C. H. Papadimitriou, Computational Complexity, 1994, Theorem 7.3.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.STCONNLComplete.stcon_nl_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/STCONNLCompleteWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/STCONNLCompleteWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/directed-s-t-connectivity/index.html#stcon-nl-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Directed s-t connectivity](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/completeness-other-classes/directed-s-t-connectivity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/completeness-other-classes/directed-s-t-connectivity)
