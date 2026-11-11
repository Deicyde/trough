---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.SetIntegralLogDensityBoundWanted.setIntegral_log_le_measure_mul_log_inv_measure, MathlibExt.MeasureTheory.SqrtOnePlusSqIntegralBoundsWanted.sqrt_one_add_sq_integral_le_and_le_one_add
statement: formalized
---

# Jensen's inequality for integrals

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/jensen-s-inequality-for-integrals/index.html).

## Upper bound for the integral of the logarithm of a probability density over a set

Let
$\mu$ be a measure on a measurable space $X$ and let $f : X \to \mathbb{R}$ be integrable with
respect to $\mu$, with $f(x) > 0$ for every $x \in X$ and $\int_X f\,d\mu = 1$. Then for every
measurable set $E \subseteq X$ with $0 < \mu(E) < \infty$ such that $\log f$ is integrable on $E$,

$$
\int_E \log f\,d\mu \le \mu(E)\log\frac{1}{\mu(E)}.
$$

The integrability of $\log f$ on $E$ is assumed so that the statement is real-valued: the
positive part of $\log f$ is integrable on $E$ (since $(\log f)^{+}\le f$), so if $\log f$
is not integrable on $E$ then $\int_E(\log f)\,d\mu=-\infty$ and the inequality holds in
$\mathbb{R}\cup\{-\infty\}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Measure and integration; Classical measure theory), problem `ma_proofbench_l1_82`.

Stated but not proved: `MathlibExt.MeasureTheory.SetIntegralLogDensityBoundWanted.setIntegral_log_le_measure_mul_log_inv_measure` is written with `theorem_wanted` in [WantedExt/MeasureTheory/SetIntegralLogDensityBoundWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/SetIntegralLogDensityBoundWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/jensen-s-inequality-for-integrals/index.html#set-integral-log-le-measure-mul-log-inv).

## Two-sided bound for the integral of the square root of one plus a square

Let $\mu$ be a
probability measure on a measurable space $\Omega$ and let $h : \Omega \to [0,\infty)$ be a
measurable function with $\int_\Omega h\,d\mu < \infty$. If $A = \int_\Omega h\,d\mu$, then

$$
\sqrt{1+A^2}\le \int_\Omega \sqrt{1+h^2}\,d\mu \le 1+A.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Measure and integration; Classical measure theory), problem `ma_proofbench_l1_66`.

Stated but not proved: `MathlibExt.MeasureTheory.SqrtOnePlusSqIntegralBoundsWanted.sqrt_one_add_sq_integral_le_and_le_one_add` is written with `theorem_wanted` in [WantedExt/MeasureTheory/SqrtOnePlusSqIntegralBoundsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/SqrtOnePlusSqIntegralBoundsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/jensen-s-inequality-for-integrals/index.html#sqrt-one-add-sq-integral-le-and-le-one-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jensen's inequality for integrals](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/jensen-s-inequality-for-integrals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/integration/jensen-s-inequality-for-integrals)
