---
declaration: section
origin: cited
lean: MetaMathlibExt.HyperfactorialDigitsNormalized, MetaMathlibExt.HyperfactorialPartition
statement: formalized
proof: formalized
---

# Hyperfactorial partitions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/hyperfactorial-partitions/index.html).

## Normalized hyperfactorial digit vectors

A vector $(h_1, \dots, h_k)$ of natural numbers
is normalized when either $k = 0$ or its last entry $h_k$ is nonzero. In particular the empty
vector is normalized; it is the canonical representation of zero.

Formalized by `MetaMathlibExt.HyperfactorialDigitsNormalized`, a definition declared in [MathlibExt/NumberTheory/HyperfactorialPartition.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HyperfactorialPartition.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/hyperfactorial-partitions/index.html#hyperfactorial-digits-normalized).

## Hyperfactorial partition

A hyperfactorial partition of a natural number $n$ consists of
a length $k \in \mathbb{N}$ and natural numbers $h_1, \dots, h_k$ such that $h_i \le 2i$ for
every $1 \le i \le k$, the digit vector is normalized (either $k = 0$ or $h_k \neq 0$), and

$$n = \sum_{i=1}^{k} h_i \cdot i!.$$

Formalized by `MetaMathlibExt.HyperfactorialPartition`, a structure declared in [MathlibExt/NumberTheory/HyperfactorialPartition.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HyperfactorialPartition.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/hyperfactorial-partitions/index.html#hyperfactorial-partition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperfactorial partitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/hyperfactorial-partitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/hyperfactorial-partitions)
