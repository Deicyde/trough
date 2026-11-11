---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Haldane.pgf_poissonMeasure, MathlibExt.Biology.PopulationGenetics.Haldane.mean_poissonMeasure, MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb, MathlibExt.Biology.PopulationGenetics.Haldane.one_sub_survivalProb, MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb_pos, MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb_lt_one, MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb_nonneg, MathlibExt.Biology.PopulationGenetics.Haldane.tendsto_survivalProb_div
statement: formalized
proof: formalized
---

# Haldane's survival probability of a beneficial mutation

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html).

## Generating function of the Poisson distribution

The Poisson(`r`) generating function: `∑ e^{-r} r^k / k! x^k = exp (r (x - 1))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.pgf_poissonMeasure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#pgf-poisson-measure).

## Mean of the Poisson distribution

The Poisson(`r`) law has mean `r`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.mean_poissonMeasure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#mean-poisson-measure).

## Haldane's survival probability of a mutant

Haldane's survival probability `π(s) = 1 - q(s)` of a mutant with selective advantage `s`
per generation, whose number of copies in the next generation is Poisson with mean `1 + s`.
The model needs `s ≥ -1`; for `s < -1` the mean is truncated to `0` (`Real.toNNReal`), the
mutant leaves no copies, and `π(s) = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#survival-prob).

## Haldane's equation for the survival probability

`π(s)` solves Haldane's equation `1 - π = exp (-(1 + s) π)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.one_sub_survivalProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#one-sub-survival-prob).

## Beneficial mutant survives with positive probability

A beneficial mutant survives with positive probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#survival-prob-pos).

## Survival probability is less than one

The survival probability is less than `1`: the mutant leaves no copies with positive
probability `exp (-(1 + s))`. (For `s < -1`, outside the model, `π(s) = 0`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb_lt_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#survival-prob-lt-one).

## Nonnegativity of the survival probability

The survival probability is non-negative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.survivalProb_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#survival-prob-nonneg).

## Haldane's approximation $\pi(s) \approx 2s$

Haldane's approximation (Haldane 1927): `π(s) / s → 2` as `s → 0⁺`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Haldane.tendsto_survivalProb_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Haldane.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Haldane.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html#tendsto-survival-prob-div).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Haldane's survival probability of a beneficial mutation](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/haldane-s-survival-probability-of-a-beneficial-m)
