---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaD, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1_two, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2_two, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1_three, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2_three, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1_pos, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2_pos, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaVarEstimator_pos
statement: formalized
proof: formalized
---

# Tajima's D

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html).

## Tajima's `D`

**Tajima's `D`** (Tajima 1989) for a sample of `n` genes with mean number of pairwise
differences `π` and `S` segregating sites:
`D = (π - S / a₁) / √(e₁ S + e₂ S (S - 1))`. It is meaningful for `n ≥ 4` and `S ≥ 1`
(`tajimaVarEstimator_pos`); otherwise Lean's junk values for `x / 0` and `√` of a nonpositive
number apply.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaD`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-d).

## Tajima's $c_1$ vanishes for two genes

For two genes `c₁ = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-c1-two).

## Tajima's $c_2$ vanishes for two genes

For two genes `c₂ = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-c2-two).

## Tajima's $c_1$ vanishes for three genes

For three genes `c₁ = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1_three`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-c1-three).

## Tajima's $c_2$ vanishes for three genes

For three genes `c₂ = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2_three`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-c2-three).

## Positivity of Tajima's $c_1$ for at least four genes

`c₁ = (n + 1) / (3 (n - 1)) - 1 / a₁ > 0` for `n ≥ 4`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-c1-pos).

## Positivity of Tajima's $c_2$ for at least four genes

`c₂ = b₂ - (n + 2) / (a₁ n) + a₂ / a₁² > 0` for `n ≥ 4`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-c2-pos).

## Positivity of the denominator of Tajima's D

The denominator of Tajima's `D` is well defined: `e₁ S + e₂ S (S - 1) > 0` for `n ≥ 4` and
`S ≥ 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaVarEstimator_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-var-estimator-pos).

## Chebyshev test of neutrality

The rejection region of the **Chebyshev test of neutrality** at level `α` and hypothesized
`θ₀`: `|π - S / a₁| ≥ √((c₁ θ₀ + c₂ θ₀²) / α)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaChebyshevTest`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#tajima-chebyshev-test).

## Level of the Chebyshev test

If Tajima's numerator `π - S / a₁` is square integrable
with mean `0` and variance `c₁ θ₀ + c₂ θ₀² > 0` (as under the standard neutral model, by
`KingmanTimes.integral_tajimaNumerator` and `KingmanTimes.variance_tajimaNumerator`), then for
every `α > 0` the test rejects with probability at most `α`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.measure_tajimaChebyshevTest_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaD.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html#measure-tajima-chebyshev-test-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tajima's D](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/tajima-s-d/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/detecting-selection/tajima-s-d)
