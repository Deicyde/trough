---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.homozygosityStep, MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.eqHomozygosity, MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.homozygosityStep_eqHomozygosity, MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.homozygosityStep_eq_self_iff, MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.tendsto_iterate_homozygosityStep, MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.tendsto_eqHomozygosity, MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.tendsto_one_sub_eqHomozygosity
statement: formalized
proof: formalized
---

# Infinite-alleles model and homozygosity

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html).

## Homozygosity recursion in the infinite-alleles model

One generation of drift and mutation in the infinite-alleles model with `M` gene copies and
mutation probability `u` per copy: `F' = (1 - u)² (1/M + (1 - 1/M) F)`. The model domain is
`2 ≤ M` (two distinct copies must exist) and `0 ≤ u ≤ 1`; the theorems below assume only
`1 ≤ M`, and `M = 1` is an algebraic extension with no biological meaning. For `M = 0` the
definition uses the junk value `1/0 = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.homozygosityStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#homozygosity-step).

## Equilibrium homozygosity in the infinite-alleles model

The equilibrium homozygosity `F* = (1 - u)² / (M - (M - 1)(1 - u)²)`. Biologically meaningful
for `2 ≤ M`; its denominator is positive for `1 ≤ M` and `0 < u ≤ 1`, the hypotheses of the
theorems below (`M = 1` being an algebraic extension).

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.eqHomozygosity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#eq-homozygosity).

## Equilibrium homozygosity is a fixed point of the recursion

`F*` is a fixed point of the homozygosity recursion.

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.homozygosityStep_eqHomozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#homozygosity-step-eq-homozygosity).

## Uniqueness of the equilibrium homozygosity

For `0 < u ≤ 1`, `F*` is the unique fixed point of the homozygosity recursion.

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.homozygosityStep_eq_self_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#homozygosity-step-eq-self-iff).

## Convergence of homozygosity to equilibrium

For `0 < u ≤ 1` the homozygosity converges to `F*` from every initial value `F₀`.

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.tendsto_iterate_homozygosityStep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#tendsto-iterate-homozygosity-step).

## Kimura–Crow limit

With `M = 2N` gene copies and mutation probability `u = θ/(4N)`
(so that `θ = 4Nu`), the equilibrium homozygosity tends to `1/(1 + θ)` as `N → ∞`.

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.tendsto_eqHomozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#tendsto-eq-homozygosity).

## Limit $\theta/(1+\theta)$ of the equilibrium heterozygosity

The equilibrium heterozygosity `H* = 1 - F*` tends to `θ/(1 + θ)` as `N → ∞` with
`M = 2N` and `u = θ/(4N)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.InfiniteAlleles.tendsto_one_sub_eqHomozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/InfiniteAlleles.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html#tendsto-one-sub-eq-homozygosity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinite-alleles model and homozygosity](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/infinite-alleles-model-and-homozygosity)
