---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SpecificLimits.SumSinSqDivSqWanted.tsum_sin_sq_mul_div_sq_mul, MathlibExt.Analysis.SpecialFunctions.TsumInvSqShiftEqPiSqDivSinSqWanted.tsum_one_div_add_int_sq_eq_pi_sq_div_sin_sq
statement: formalized
---

# Trigonometric and harmonic-number series: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/index.html).

Closed forms for series in powers of sin, cos or tan, central binomial series in trigonometric arguments, partial-fraction series of trigonometric functions, and identities with harmonic or odd harmonic numbers, as in Ramanujan's notebooks Chapter 9.

## A closed form for $\sum \sin^2(n\delta)/(n^2\delta)$

For every real $\delta$ with
$0 < \delta < \pi$,

$$\sum_{n=1}^{\infty} \frac{\sin^2(n\delta)}{n^2\delta} = \frac{\pi - \delta}{2}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Sequences, series, summability; Convergence and divergence of infinite limiting processes), problem `ma_proofbench_l1_03`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.SumSinSqDivSqWanted.tsum_sin_sq_mul_div_sq_mul` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/SumSinSqDivSqWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/SumSinSqDivSqWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/index.html#tsum-sin-sq-mul-div-sq-mul).

## Partial fraction expansion of $\pi^2/\sin^2(\pi u)$

For every real number $u$ that is
not an integer,

$$\sum_{n \in \mathbb{Z}} \frac{1}{(u+n)^2} = \frac{\pi^2}{\sin^2(\pi u)}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Sequences, series, summability; Convergence and divergence of infinite limiting processes), problem `ma_proofbench_l2_09`.

Stated but not proved: `MathlibExt.Analysis.SpecialFunctions.TsumInvSqShiftEqPiSqDivSinSqWanted.tsum_one_div_add_int_sq_eq_pi_sq_div_sin_sq` is written with `theorem_wanted` in [WantedExt/Analysis/SpecialFunctions/TsumInvSqShiftEqPiSqDivSinSqWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecialFunctions/TsumInvSqShiftEqPiSqDivSinSqWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/index.html#tsum-one-div-add-int-sq-eq-pi-sq-div-sin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trigonometric and harmonic-number series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series)
