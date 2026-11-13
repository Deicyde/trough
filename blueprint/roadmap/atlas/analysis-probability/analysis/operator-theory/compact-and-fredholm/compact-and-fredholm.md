---
declaration: section
origin: cited
lean: MathlibExt.Analysis.OperatorTheory.CompactOperatorKernelNonseparableWanted.not_separableSpace_ker_of_isCompactOperator_of_not_separableSpace
statement: formalized
---

# Compact and Fredholm operators: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/index.html).

Compact and finite-rank operators, Schauder's theorem, complete continuity, Hilbert–Schmidt operators, Riesz–Schauder theory, Fredholm alternative and index, closed-range theorems.

## The kernel of a compact operator on a nonseparable Hilbert space is nonseparable

Let
$H$ be a complex Hilbert space that is not separable and let $A : H \to H$ be a compact operator.
Then the kernel $\ker A$ is not separable.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Special classes of linear operators), problem `ma_proofbench_l2_42`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.CompactOperatorKernelNonseparableWanted.not_separableSpace_ker_of_isCompactOperator_of_not_separableSpace` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/CompactOperatorKernelNonseparableWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OperatorTheory/CompactOperatorKernelNonseparableWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/index.html#not-separable-space-ker-of-is-compact-op).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compact and Fredholm operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm)
