---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.ZerosOfSumZDivNPowNWanted.F, MathlibExt.Analysis.Complex.ZerosOfSumZDivNPowNWanted.exists_finset_zeros_sum_analyticOrderNatAt_le
statement: formalized
---

# Zeros of the entire function 1 + Σ (z/n)ⁿ

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-of-the-entire-function-1-z-n/index.html).

## The entire function $1+\sum_{n\ge 1}(z/n)^n$

This is the function
$F:\mathbb{C}\to\mathbb{C}$ given by

$$F(z)=1+\sum_{n=1}^{\infty}\left(\frac{z}{n}\right)^{n}.$$

Formalized by `MathlibExt.Analysis.Complex.ZerosOfSumZDivNPowNWanted.F`, a definition declared in [WantedExt/Analysis/Complex/ZerosOfSumZDivNPowNWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ZerosOfSumZDivNPowNWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-of-the-entire-function-1-z-n/index.html#f).

## Zeros of $1+\sum_{n\ge 1}(z/n)^n$ in a disc

Let $F$ be the entire function

$$F(z)=1+\sum_{n=1}^{\infty}\left(\frac{z}{n}\right)^{n}.$$

For every real $R>0$, $F$ has only finitely many zeros in the open disc
$\{z\in\mathbb{C} : |z|\lt R\}$, and the number of these zeros counted with multiplicity is at
most $4R$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Entire and meromorphic functions of one complex variable, and related topics), problem `ma_proofbench_l2_91`.

Stated but not proved: `MathlibExt.Analysis.Complex.ZerosOfSumZDivNPowNWanted.exists_finset_zeros_sum_analyticOrderNatAt_le` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ZerosOfSumZDivNPowNWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Complex/ZerosOfSumZDivNPowNWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-of-the-entire-function-1-z-n/index.html#exists-finset-zeros-sum-analytic-order-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zeros of the entire function 1 + Σ (z/n)ⁿ](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/zeros-of-the-entire-function-1-z-n/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/entire-functions/zeros-of-the-entire-function-1-z-n)
