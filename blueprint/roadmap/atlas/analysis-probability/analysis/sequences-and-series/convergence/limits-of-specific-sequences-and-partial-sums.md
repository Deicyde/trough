---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SpecificLimits.ReciprocalSumAddInvNullWanted.xSeq, MathlibExt.Analysis.SpecificLimits.ReciprocalSumAddInvNullWanted.tendsto_one_div_sum_add_inv_zero
statement: formalized
---

# Limits of specific sequences and partial sums

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/limits-of-specific-sequences-and-partial-sums/index.html).

## Partial sums of $a_k + 1/a_k$

For a real sequence $(a_k)_{k \in \mathbb{N}}$, the sequence
$(x_n)_{n \in \mathbb{N}}$ is given by $x_n = \sum_{k=0}^{n} (a_k + 1/a_k)$ for $n \in \mathbb{N}$,
with the convention $1/0 = 0$.

Formalized by `MathlibExt.Analysis.SpecificLimits.ReciprocalSumAddInvNullWanted.xSeq`, a definition declared in [WantedExt/Analysis/SpecificLimits/ReciprocalSumAddInvNullWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/ReciprocalSumAddInvNullWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/limits-of-specific-sequences-and-partial-sums/index.html#x-seq).

## The reciprocals of $\sum_{k=0}^{n} (a_k + 1/a_k)$ tend to zero

Let
$(a_n)_{n \in \mathbb{N}}$ be a sequence of positive real numbers, and for $n \in \mathbb{N}$ let
$x_n = \sum_{k=0}^{n} (a_k + 1/a_k)$. Then $1/x_n \to 0$ as $n \to \infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Sequences, series, summability; Convergence and divergence of infinite limiting processes), problem `ma_proofbench_l1_18`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.ReciprocalSumAddInvNullWanted.tendsto_one_div_sum_add_inv_zero` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/ReciprocalSumAddInvNullWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/ReciprocalSumAddInvNullWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/limits-of-specific-sequences-and-partial-sums/index.html#tendsto-one-div-sum-add-inv-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Limits of specific sequences and partial sums](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/limits-of-specific-sequences-and-partial-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/convergence/limits-of-specific-sequences-and-partial-sums)
