---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.LargeLevelSetReverseHolderWanted.μIcc01, MathlibExt.MeasureTheory.LargeLevelSetReverseHolderWanted.exists_tendsto_atTop_inf_measure_levelSet_pos
statement: formalized
---

# Reverse Hölder inequality

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/reverse-h-lder-inequality/index.html).

## Lebesgue measure on the unit interval

The measure on $\mathbb{R}$ that assigns to each
set $A \subseteq \mathbb{R}$ the Lebesgue measure of $A \cap [0,1]$.

Formalized by `MathlibExt.MeasureTheory.LargeLevelSetReverseHolderWanted.μIcc01`, an abbreviation declared in [WantedExt/MeasureTheory/LargeLevelSetReverseHolderWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/LargeLevelSetReverseHolderWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/reverse-h-lder-inequality/index.html#icc01).

## Uniformly large level sets under a reverse Hölder bound

Let $\mu$ be Lebesgue measure
on $[0,1]$, and let $f_0, f_1, f_2, \ldots : \mathbb{R} \to \mathbb{R}$ lie in $L^2(\mu)$ with
$\|f_n\|_{L^2(\mu)} \le 2024\,\|f_n\|_{L^1(\mu)}$ for every $n$ and
$\|f_n\|_{L^1(\mu)} \to \infty$ as $n \to \infty$. Then there is a sequence of real numbers
$y_n \to \infty$ such that

$$
\inf_n \mu(\{x : |f_n(x)| \ge y_n\}) > 0.
$$

The divergence hypothesis is the limit $\|f_n\|_{L^1(\mu)} \to \infty$ in $[0,\infty]$; the
formal source instead required $\|f_n\|_{L^1(\mu)} = \infty$ for all large $n$, which no function
in $L^2(\mu)$ satisfies, so its statement was vacuous.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_04`, with the change above.

Stated but not proved: `MathlibExt.MeasureTheory.LargeLevelSetReverseHolderWanted.exists_tendsto_atTop_inf_measure_levelSet_pos` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LargeLevelSetReverseHolderWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/LargeLevelSetReverseHolderWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/reverse-h-lder-inequality/index.html#exists-tendsto-at-top-inf-measure-level).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reverse Hölder inequality](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/reverse-h-lder-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/lp-spaces/reverse-h-lder-inequality)
