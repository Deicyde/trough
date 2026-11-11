---
declaration: section
origin: cited
lean: MathlibExt.Probability.PoissonPointProcess.countingMeasure, MathlibExt.Probability.PoissonPointProcess.poissonPointProcess, MathlibExt.Probability.PoissonPointProcess.countingMeasure_apply, MathlibExt.Probability.PoissonPointProcess.measurable_countingMeasure, MathlibExt.Probability.PoissonPointProcess.lintegral_countingMeasure, MathlibExt.Probability.PoissonPointProcess.tsum_coeff_mul_pow, MathlibExt.Probability.PoissonPointProcess.lintegral_pi_eval, MathlibExt.Probability.PoissonPointProcess.countingMeasure_comp
statement: formalized
---

# Poisson point processes

15 results, 14 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html).

## Counting measure of a finite tuple of points

The counting measure `∑_{i < n} δ_{x_i}` of a finite tuple of points.

Formalized by `MathlibExt.Probability.PoissonPointProcess.countingMeasure`, a definition declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#counting-measure).

## Poisson point process with finite intensity

The law of the Poisson point process with finite intensity `μ` on `E`:
`∑_n e^{-μ(E)} / n! • (μ^{⊗n}).map countingMeasure`, a probability measure on `Measure E`
(Last–Penrose Prop. 3.5, mixed binomial construction).

Formalized by `MathlibExt.Probability.PoissonPointProcess.poissonPointProcess`, a definition declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#poisson-point-process).

## Counting measure of a set as a sum of indicators

`(∑ δ_{x_i})(s) = #{i | x_i ∈ s}`, as a sum of indicators.

Formalized by `MathlibExt.Probability.PoissonPointProcess.countingMeasure_apply`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#counting-measure-apply).

## Measurability of the counting measure in the points

The counting measure of a tuple depends measurably on the tuple.

Formalized by `MathlibExt.Probability.PoissonPointProcess.measurable_countingMeasure`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#measurable-counting-measure).

## Integral against a counting measure

`∫ f d(∑ δ_{x_i}) = ∑ f(x_i)`.

Formalized by `MathlibExt.Probability.PoissonPointProcess.lintegral_countingMeasure`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#lintegral-counting-measure).

## Poisson weights sum to one

The Poisson weights sum to one: `∑_n e^{-μ(E)} μ(E)^n / n! = 1`.

Formalized by `MathlibExt.Probability.PoissonPointProcess.tsum_coeff_mul_pow`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#tsum-coeff-mul-pow).

## Integral of a coordinate function under a product measure

`∫ f(x_i) dμ^{⊗n}(x) = μ(E)^{n-1} ∫ f dμ`.

Formalized by `MathlibExt.Probability.PoissonPointProcess.lintegral_pi_eval`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#lintegral-pi-eval).

## Image of a counting measure under a map

The image of `∑ δ_{x_i}` under `T` is `∑ δ_{T(x_i)}`.

Formalized by `MathlibExt.Probability.PoissonPointProcess.countingMeasure_comp`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#counting-measure-comp).

## Point counts of a Poisson point process are Poisson

The number of points `η(B)` in a measurable set `B` has the Poisson law of mean `μ(B)`.

Formalized by `MathlibExt.Probability.PoissonPointProcess.map_apply_eq_poissonMeasure`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#map-apply-eq-poisson-measure).

## Mixed binomial process is a Poisson process

The counts `η(A i)` of pairwise disjoint measurable sets are independent, and `η(A i)`
has the Poisson law of mean `μ(A i)`: the mixed binomial process is a Poisson process with
intensity `μ` in the sense of Last–Penrose Def. 3.1 (Last–Penrose Prop. 3.5).

Formalized by `MathlibExt.Probability.PoissonPointProcess.map_apply_pi`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#map-apply-pi).

## Campbell's formula

`E ∫ f dη = ∫ f dμ` for measurable `f : E → [0, ∞]`
(Last–Penrose Prop. 2.7).

Formalized by `MathlibExt.Probability.PoissonPointProcess.lintegral_lintegral`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#lintegral-lintegral).

## Laplace functional

For measurable `f : E → [0, ∞)`,
`E exp(-∫ f dη) = exp(-∫ (1 - e^{-f}) dμ)` (Last–Penrose Thm. 3.9). The integral `∫ f dη` is a
finite sum `∑ f(x_i)` for every configuration charged by the process.

Formalized by `MathlibExt.Probability.PoissonPointProcess.integral_exp_neg`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#integral-exp-neg).

## Mecke equation

For measurable `h : E × Measure E → [0, ∞]`,
`E ∫ h(x, η) η(dx) = ∫ E h(x, η + δ_x) μ(dx)` (Mecke 1967; Last–Penrose Thm. 4.1).

Formalized by `MathlibExt.Probability.PoissonPointProcess.lintegral_lintegral_mecke`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#lintegral-lintegral-mecke).

## Mapping theorem

The image `η ∘ T⁻¹` of a Poisson point process under a measurable map
`T : E → F` is the Poisson point process with intensity `μ ∘ T⁻¹` (Last–Penrose Thm. 5.1).

Formalized by `MathlibExt.Probability.PoissonPointProcess.map_map`, a theorem declared in [MathlibExt/Probability/Process/PoissonPointProcess.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonPointProcess.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#map-map).

## Restriction theorem

The restrictions `η|_{A i}` of a Poisson point process with finite
intensity `μ` to pairwise disjoint measurable sets `A i` are independent Poisson point processes
with intensities `μ|_{A i}` (Last–Penrose Thm. 5.2).

Stated but not proved: `MathlibExt.Probability.PoissonPointProcess.map_restrict_pi` is written with `theorem_wanted` in [WantedExt/Probability/Process/PoissonPointProcessWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/Process/PoissonPointProcessWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html#map-restrict-pi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson point processes](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-point-processes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/point-processes/poisson-point-processes)
