---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.AbsContLusinNPropertyWanted.volume_image_eq_zero_of_absolutelyContinuous, MathlibExt.MeasureTheory.LipschitzIffAbsContBoundedDerivWanted.lipschitzWith_iff_absolutelyContinuous_and_ae_norm_deriv_le, MathlibExt.MeasureTheory.LipschitzOneAbsContDerivLinftyWanted.absolutelyContinuousOnInterval_and_eLpNorm_deriv_lt_top_of_lipschitzOnWith
statement: formalized
---

# Absolutely continuous functions

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/absolutely-continuous-functions/index.html).

## Absolutely continuous functions have the Lusin N property

Let $f : \mathbb{R} \to
\mathbb{R}$ be absolutely continuous on every closed bounded interval $[a, b]$. Then $f$ maps
Lebesgue null sets to null sets: for every set $s \subseteq \mathbb{R}$ of Lebesgue outer measure
zero, the image $f(s)$ has Lebesgue outer measure zero.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_75`.

Stated but not proved: `MathlibExt.MeasureTheory.AbsContLusinNPropertyWanted.volume_image_eq_zero_of_absolutelyContinuous` is written with `theorem_wanted` in [WantedExt/MeasureTheory/AbsContLusinNPropertyWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/AbsContLusinNPropertyWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/absolutely-continuous-functions/index.html#volume-image-eq-zero-of-absolutely-conti).

## Lipschitz functions are the absolutely continuous functions with bounded derivative

Let
$f : \mathbb{R} \to \mathbb{R}$ and let $M \ge 0$ be a real number. Then
$|f(x) - f(y)| \le M|x - y|$ for all $x, y \in \mathbb{R}$ if and only if $f$ is absolutely
continuous on every closed bounded interval and $|f'(x)| \le M$ for almost every $x \in \mathbb{R}$
(with respect to Lebesgue measure), where $f'(x)$ is taken to be $0$ at points where $f$ is not
differentiable.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_62`.

Stated but not proved: `MathlibExt.MeasureTheory.LipschitzIffAbsContBoundedDerivWanted.lipschitzWith_iff_absolutelyContinuous_and_ae_norm_deriv_le` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LipschitzIffAbsContBoundedDerivWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/LipschitzIffAbsContBoundedDerivWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/absolutely-continuous-functions/index.html#lipschitz-with-iff-absolutely-continuous).

## A $1$-Lipschitz function on $(a,b)$ is absolutely continuous with essentially bounded derivative

**A $1$-Lipschitz function on $[a,b]$ is absolutely continuous with essentially bounded
derivative.** Let $a \le b$ be real numbers and let $f : \mathbb{R} \to \mathbb{R}$ satisfy
$|f(x) - f(y)| \le |x - y|$ for all $x, y \in [a, b]$. Then $f$ is absolutely continuous on
$[a, b]$, and its derivative $f'$, taken to be $0$ at points where $f$ is not differentiable, has
finite norm $\|f'\|_{L^\infty[a,b]}$, the essential supremum with respect to Lebesgue measure on
$[a, b]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_34`.

Stated but not proved: `MathlibExt.MeasureTheory.LipschitzOneAbsContDerivLinftyWanted.absolutelyContinuousOnInterval_and_eLpNorm_deriv_lt_top_of_lipschitzOnWith` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LipschitzOneAbsContDerivLinftyWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/LipschitzOneAbsContDerivLinftyWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/absolutely-continuous-functions/index.html#absolutely-continuous-on-interval-and-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Absolutely continuous functions](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/absolutely-continuous-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/real-functions/absolutely-continuous-functions)
