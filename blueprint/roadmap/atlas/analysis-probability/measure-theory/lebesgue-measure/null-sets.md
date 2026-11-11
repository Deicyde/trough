---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.measure_image_null_of_locally_null, MvPolynomial.measure_setOf_eval_eq_zero_of_ne_zero, MathlibExt.MeasureTheory.GraphMeasurableNullWanted.measurableSet_and_volume_eq_zero_graph
statement: formalized
---

# Null sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/null-sets/index.html).

## Sets with locally null image have null image

Let $X$ be a second-countable topological
space, $Y$ a measurable space with a measure $\mu$, $f : X \to Y$ a function and $s \subseteq X$.
If every point $x \in s$ has a neighbourhood $V$ with $\mu(f(V \cap s)) = 0$, then
$\mu(f(s)) = 0$.

Here $\mu$ is evaluated as an outer measure, so the images need not be measurable.

Formalized by `MathlibExt.MeasureTheory.measure_image_null_of_locally_null`, a theorem declared in [MathlibExt/MeasureTheory/Measure/ImageNull.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/ImageNull.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/null-sets/index.html#measure-image-null-of-locally-null).

## Nonzero polynomials over nondiscrete fields have Haar-null zero sets

A nonzero multivariate polynomial over a nondiscrete locally compact
second-countable Hausdorff topological field has an additive Haar-null zero set.
This includes the empty variable type.

Formalized by `MvPolynomial.measure_setOf_eval_eq_zero_of_ne_zero`, a theorem declared in [MathlibExt/MeasureTheory/Polynomial.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Polynomial.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/null-sets/index.html#measure-set-of-eval-eq-zero-of-ne-zero).

## The graph of a measurable function is a null set

Let $d \ge 0$ be an integer and let
$f : \mathbb{R}^d \to \mathbb{R}$ be Borel measurable. Identify $\mathbb{R}^d \times \mathbb{R}$
with $\mathbb{R}^{d+1}$ by taking the last coordinate as $y$. Then the graph
$\Gamma = \{(x, y) \in \mathbb{R}^d \times \mathbb{R} : y = f(x)\}$ is a Borel measurable subset
of $\mathbb{R}^{d+1}$ and has Lebesgue measure $0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Measure and integration; Classical measure theory), problem `ma_proofbench_l1_38`.

Stated but not proved: `MathlibExt.MeasureTheory.GraphMeasurableNullWanted.measurableSet_and_volume_eq_zero_graph` is written with `theorem_wanted` in [WantedExt/MeasureTheory/GraphMeasurableNullWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/GraphMeasurableNullWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/null-sets/index.html#measurable-set-and-volume-eq-zero-graph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Null sets](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/null-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lebesgue-measure/null-sets)
