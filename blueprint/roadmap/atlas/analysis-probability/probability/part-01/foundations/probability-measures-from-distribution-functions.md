---
declaration: section
origin: cited
lean: MathlibExt.Probability.StieltjesMeasureConstruction.stieltjes_measure_construction, MathlibExt.Probability.StieltjesMeasureConstruction.exists_unique_probabilityMeasure_of_stieltjes
statement: formalized
proof: formalized
---

# Probability measures from distribution functions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/probability-measures-from-distribution-functions/index.html).

## Construction of measures on ℝ

Let $f : \mathbb{R} \to \mathbb{R}$ be a Stieltjes
function, that is, non-decreasing and right-continuous, with $f(x) \to 0$ as $x \to -\infty$
and $f(x) \to 1$ as $x \to \infty$, and let $\mu_f$ be its Stieltjes measure on $\mathbb{R}$.
Then $\mu_f$ is a probability measure, $\mu_f((a, b]) = f(b) - f(a)$ for all real $a \le b$,
and every finite measure $\nu$ on $\mathbb{R}$ with $\nu((a, b]) = f(b) - f(a)$ for all real
$a \le b$ equals $\mu_f$.

Formalized by `MathlibExt.Probability.StieltjesMeasureConstruction.stieltjes_measure_construction`, a theorem declared in [MathlibExt/Probability/StieltjesMeasureConstruction.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StieltjesMeasureConstruction.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/probability-measures-from-distribution-functions/index.html#stieltjes-measure-construction).

## Construction of measures on ℝ, as unique existence

Let
$f : \mathbb{R} \to \mathbb{R}$ be a Stieltjes function, that is, non-decreasing and
right-continuous, with $f(x) \to 0$ as $x \to -\infty$ and $f(x) \to 1$ as $x \to \infty$.
Then there is exactly one measure $\mu$ on $\mathbb{R}$ that is a probability measure and
satisfies $\mu((a, b]) = f(b) - f(a)$ for all real $a \le b$.

Formalized by `MathlibExt.Probability.StieltjesMeasureConstruction.exists_unique_probabilityMeasure_of_stieltjes`, a theorem declared in [MathlibExt/Probability/StieltjesMeasureConstruction.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StieltjesMeasureConstruction.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/probability-measures-from-distribution-functions/index.html#exists-unique-probability-measure-of-sti).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Probability measures from distribution functions](https://deicyde.github.io/atlas-lean/roadmap/Probability/foundations/probability-measures-from-distribution-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/foundations/probability-measures-from-distribution-functions)
