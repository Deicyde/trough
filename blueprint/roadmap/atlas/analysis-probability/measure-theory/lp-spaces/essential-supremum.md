---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Function.EssSupContinuousMap.eLpNormEssSup_eq_enorm_continuousMap, MathlibExt.MeasureTheory.Function.EssSupContinuousMap.eLpNorm_top_eq_enorm_continuousMap, MathlibExt.Analysis.FunctionalAnalysis.LpNormTendstoEssSupWanted.tendsto_eLpNorm_atTop_eLpNorm_top_of_isFiniteMeasure, MathlibExt.MeasureTheory.LinftyNormLeSupLpNormUnitIntervalWanted.eLpNorm_top_le_of_forall_one_le_eLpNorm_le
statement: formalized
---

# Essential supremum

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/essential-supremum/index.html).

## Essential supremum of a continuous map

Let $\alpha$ be a compact topological space with
its Borel $\sigma$-algebra, let $\mu$ be a measure on $\alpha$ that is positive on every nonempty
open set, let $E$ be a seminormed additive commutative group, and let $f : \alpha \to E$ be
continuous. Then the essential supremum of $\|f\|$ with respect to $\mu$ equals the supremum norm
$\sup_{x \in \alpha} \|f(x)\|$ of $f$, as an equality in $[0, \infty]$.

Formalized by `MathlibExt.MeasureTheory.Function.EssSupContinuousMap.eLpNormEssSup_eq_enorm_continuousMap`, a theorem declared in [MathlibExt/MeasureTheory/Function/EssSupContinuousMap.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/EssSupContinuousMap.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/essential-supremum/index.html#e-lp-norm-ess-sup-eq-enorm-continuous-ma).

## The $L^\infty$ norm of a continuous map is its supremum norm

Let $\alpha$ be a compact
topological space with its Borel $\sigma$-algebra, let $\mu$ be a measure on $\alpha$ that is
positive on every nonempty open set, let $E$ be a seminormed additive commutative group such that
$\alpha$ or $E$ is second-countable, and let $f : \alpha \to E$ be continuous. Then
$\|f\|_{L^\infty(\mu)} = \sup_{x \in \alpha} \|f(x)\|$, as an equality in $[0, \infty]$.

Formalized by `MathlibExt.MeasureTheory.Function.EssSupContinuousMap.eLpNorm_top_eq_enorm_continuousMap`, a theorem declared in [MathlibExt/MeasureTheory/Function/EssSupContinuousMap.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/EssSupContinuousMap.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/essential-supremum/index.html#e-lp-norm-top-eq-enorm-continuous-map).

## The $L^p$ norm tends to the $L^\infty$ norm

Let $\mu$ be a finite measure on a measurable
space $\alpha$ and let $f \colon \alpha \to \mathbb{R}$ be essentially bounded,
$f \in L^\infty(\mu)$. Then $\|f\|_{L^p(\mu)} \to \|f\|_{L^\infty(\mu)}$ as the real exponent
$p$ tends to $\infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l1_42`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.LpNormTendstoEssSupWanted.tendsto_eLpNorm_atTop_eLpNorm_top_of_isFiniteMeasure` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/LpNormTendstoEssSupWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/LpNormTendstoEssSupWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/essential-supremum/index.html#tendsto-e-lp-norm-at-top-e-lp-norm-top-o).

## Uniform $L^p$ bounds on $(0,1)$ give the same $L^\infty$ bound

Let $M$ be a real number,
write $M^+ = \max(M, 0)$, and let $f_0, f_1, f_2, \dots : \mathbb{R} \to \mathbb{R}$ be functions
that are almost everywhere strongly measurable with respect to Lebesgue measure restricted to
$[0,1]$. If $\|f_n\|_{L^p[0,1]} \le M^+$ for every $n$ and every real $p \ge 1$, then
$\|f_n\|_{L^\infty[0,1]} \le M^+$ for every $n$. All norms are taken with respect to Lebesgue
measure restricted to $[0,1]$ and may be infinite.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_52`.

Stated but not proved: `MathlibExt.MeasureTheory.LinftyNormLeSupLpNormUnitIntervalWanted.eLpNorm_top_le_of_forall_one_le_eLpNorm_le` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LinftyNormLeSupLpNormUnitIntervalWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LinftyNormLeSupLpNormUnitIntervalWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/essential-supremum/index.html#e-lp-norm-top-le-of-forall-one-le-e-lp-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Essential supremum](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/essential-supremum/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lp-spaces/essential-supremum)
