---
declaration: section
origin: cited
lean: MetaMathlibExt.IsRamseyUltrafilter, MetaMathlibExt.IsDeltaSystem
statement: formalized
proof: formalized
---

# Infinitary combinatorics: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/index.html).

Combinatorics of infinite and uncountable sets: clubs and stationary sets, partition relations, Δ-systems, almost disjoint families, combinatorial principles such as diamond and square, set-theoretic trees, Ramsey ultrafilters and the structure of P(ω)/fin.

## Ramsey ultrafilter

An ultrafilter $U$ on $\mathbb{N}$ is *Ramsey* if for every sequence
$(A_n)_{n \in \mathbb{N}}$ of pairwise disjoint subsets of $\mathbb{N}$ whose union is
$\mathbb{N}$ and such that $A_n \notin U$ for all $n$, there is $X \in U$ such that
$X \cap A_n$ has at most one element for every $n$.

Formalized by `MetaMathlibExt.IsRamseyUltrafilter`, a definition declared in [MathlibExt/SetTheory/Ultrafilter/Ramsey.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Ultrafilter/Ramsey.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/index.html#is-ramsey-ultrafilter).

## Δ-system

A family $A$ of subsets of a type $\alpha$ is a Δ-system with root
$r \subseteq \alpha$ if $s \cap t = r$ for any two distinct members $s$ and $t$ of $A$.

Formalized by `MetaMathlibExt.IsDeltaSystem`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/DeltaSystem.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/InfinitaryCombinatorics/DeltaSystem.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/index.html#is-delta-system).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinitary combinatorics](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics)
