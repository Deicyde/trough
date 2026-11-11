---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Ewens.cycleTypeWeight, MathlibExt.Biology.PopulationGenetics.Ewens.numAllelesProb, MathlibExt.Biology.PopulationGenetics.Ewens.ewensCondProb, MathlibExt.Biology.PopulationGenetics.Ewens.condUpperPValue, MathlibExt.Biology.PopulationGenetics.Ewens.homozygosity, MathlibExt.Biology.PopulationGenetics.Ewens.cycleTypeWeight_pos, MathlibExt.Biology.PopulationGenetics.Ewens.ewensProb_eq_mul_cycleTypeWeight, MathlibExt.Biology.PopulationGenetics.Ewens.ewensCondProb_eq
statement: formalized
proof: formalized
---

# Ewens–Watterson test

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html).

## Number of permutations with a given cycle type

The number of permutations of `n` letters with cycle type `π`,
`w(π) = n! / ∏ j, j ^ (a j) * (a j)!` with `a j = π.parts.count j` (Cauchy's formula).

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.cycleTypeWeight`, a definition declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#cycle-type-weight).

## Probability of a given number of alleles under the Ewens formula

The probability `P_θ(K = k)` that a sample of `n` genes carries exactly `k` distinct
alleles under the Ewens sampling formula.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.numAllelesProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#num-alleles-prob).

## Ewens conditional probability given the number of alleles

The conditional probability of the allelic partition `π` given that the number of alleles
is `K = K(π) = π.parts.card`, under the Ewens sampling formula with parameter `θ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.ewensCondProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#ewens-cond-prob).

## Conditional upper-tail p-value of the Ewens–Watterson test

The **conditional upper-tail p-value** of a statistic `T` of the allelic partition: the
conditional probability, given the observed number of alleles `K(π)`, that `T` is at least
its observed value `T π`. It is written with the cycle-type weights and so does not involve
`θ` (by `ewensCondProb_eq` it is the conditional tail probability for every `θ > 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.condUpperPValue`, a definition declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#cond-upper-pvalue).

## Sample homozygosity of an allelic partition

The **sample homozygosity** `F(π) = ∑_i (n_i / n)²`, the sum over the alleles of the
squared sample frequencies (Watterson 1978); `n_i` ranges over the parts of `π`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.homozygosity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#homozygosity).

## Positivity of the cycle-type weight

The cycle-type weight is positive.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.cycleTypeWeight_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#cycle-type-weight-pos).

## Factorization of the Ewens sampling formula

**Factorization of the Ewens sampling formula** (Ewens 1972):
`P_θ(π) = θ ^ K(π) / θ^{(n)} * w(π)`, with `K(π) = π.parts.card` the number of alleles.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.ewensProb_eq_mul_cycleTypeWeight`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#ewens-prob-eq-mul-cycle-type-weight).

## `K` is sufficient for `θ`

**`K` is sufficient for `θ`** (Ewens 1972): for `θ > 0`, the conditional law of the
allelic partition given the number of alleles is `w(π) / ∑_{K(π') = K(π)} w(π')`, which does
not depend on `θ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.ewensCondProb_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#ewens-cond-prob-eq).

## Cauchy's count by number of cycles

The cycle-type weights of the partitions of `n`
into `k` parts sum to the unsigned Stirling number of the first kind `|s(n, k)|`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_cycleTypeWeight_eq_stirlingFirst`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#sum-cycle-type-weight-eq-stirling-first).

## Law of the number of alleles

**Law of the number of alleles** (Ewens 1972):
`P_θ(K = k) = |s(n, k)| θ ^ k / θ^{(n)}`. As an identity between the defining sums it holds
for every real `θ`; it is a probability for `θ > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.numAllelesProb_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#num-alleles-prob-eq).

## The Ewens–Watterson conditional law

**The Ewens–Watterson conditional law** (Ewens 1972; Watterson 1978): for `θ > 0`,
`P(π | K = K(π)) = w(π) / |s(n, K(π))| = n! / (|s(n, k)| ∏ j, j ^ (a j) (a j)!)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.ewensCondProb_eq_stirlingFirst`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#ewens-cond-prob-eq-stirling-first).

## Validity of a discrete upper-tail p-value

For nonnegative masses `q` on a finite set
`s` and a statistic `T`, the upper-tail p-value `p x = ∑_{y ∈ s, T x ≤ T y} q y` satisfies
`∑_{x ∈ s, p x ≤ t} q x ≤ t` for every `t ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_upperTail_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#sum-upper-tail-le).

## Conditional validity of the Ewens–Watterson test

For `θ > 0`, every number of alleles
`k` and every level `t ≥ 0`, the conditional probability given `K = k` that the conditional
upper-tail p-value of `T` is at most `t` is at most `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_condUpperPValue_le_cond`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#sum-cond-upper-pvalue-le-cond).

## Validity of the Ewens–Watterson test

**Validity of the Ewens–Watterson test** (Watterson 1978): for every `θ > 0` and every
level `t ≥ 0`, the Ewens probability that the conditional upper-tail p-value of `T` is at most
`t` is at most `t`. With `T = homozygosity` this is the test against excess homozygosity, with
`T = -homozygosity` the test against a deficit of homozygosity.

Formalized by `MathlibExt.Biology.PopulationGenetics.Ewens.sum_condUpperPValue_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/EwensWatterson.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html#sum-cond-upper-pvalue-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ewens–Watterson test](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/ewens-watterson-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/detecting-selection/ewens-watterson-test)
