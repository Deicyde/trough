---
declaration: section
origin: cited
lean: ProbabilityTheory.continuous_mapping, MeasureTheory.ProbabilityMeasure.tendsto_map_of_tendsto_of_ae_continuous
statement: formalized
proof: formalized
---

# Continuous mapping theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/continuous-mapping-theorem/index.html).

## Probability Theory

## Continuous mapping theorem, integral form

Let $\mu_n$ ($n \in \mathbb{N}$) and $\mu$ be
probability measures on $\mathbb{R}$, let $g : \mathbb{R} \to \mathbb{R}$ be a measurable function
whose set of discontinuity points has $\mu$-measure zero, and write $\nu \circ g^{-1}$ for the
pushforward of a measure $\nu$ on $\mathbb{R}$ under $g$. If $\int f \, d\mu_n \to \int f \, d\mu$
as $n \to \infty$ for every bounded continuous function $f : \mathbb{R} \to \mathbb{R}$, then
$\int f \, d(\mu_n \circ g^{-1}) \to \int f \, d(\mu \circ g^{-1})$ as $n \to \infty$ for every
bounded continuous function $f : \mathbb{R} \to \mathbb{R}$.

## Sources

- Lecture 12, continuous mapping theorem.

Formalized by `ProbabilityTheory.continuous_mapping`, a theorem declared in [MathlibExt/Probability/ContinuousMapping.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ContinuousMapping.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/continuous-mapping-theorem/index.html#continuous-mapping).

## Continuous mapping theorem for weak convergence of probability measures

Let $\mu_n$
($n \in \mathbb{N}$) and $\mu$ be probability measures on $\mathbb{R}$, and let
$g : \mathbb{R} \to \mathbb{R}$ be a measurable function whose set of discontinuity points has
$\mu$-measure zero. If $\mu_n$ converges weakly to $\mu$ as $n \to \infty$, then the pushforward
probability measures $\mu_n \circ g^{-1}$ converge weakly to $\mu \circ g^{-1}$.

This generalizes the case where $g$ is continuous everywhere, which is already in Mathlib.

## Sources

- Lecture 12, continuous mapping theorem.

Formalized by `MeasureTheory.ProbabilityMeasure.tendsto_map_of_tendsto_of_ae_continuous`, a theorem declared in [MathlibExt/Probability/ContinuousMapping.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ContinuousMapping.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/continuous-mapping-theorem/index.html#tendsto-map-of-tendsto-of-ae-continuous).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuous mapping theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/continuous-mapping-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/convergence-of-measures/continuous-mapping-theorem)
