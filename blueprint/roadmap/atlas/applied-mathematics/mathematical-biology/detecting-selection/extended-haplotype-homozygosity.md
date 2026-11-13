---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.SelectionScan.window, MathlibExt.Biology.PopulationGenetics.SelectionScan.window_eq_iff, MathlibExt.Biology.PopulationGenetics.SelectionScan.concordantPairs, MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh, MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_eq_zero_of_card_le_one, MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_zero_window, MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_antitone, MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_eq_sum_counts
statement: formalized
proof: formalized
---

# Extended haplotype homozygosity

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html).

## Sample

## Haplotype window around the core

The window of radius `d` of haplotype `i`: its alleles at the `d` sites closest to the
core, in the direction indexed by `ℕ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.window`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#window).

## Equality of haplotype windows

Two haplotypes have the same window of radius `d` exactly when they agree at every site
`k < d`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.window_eq_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#window-eq-iff).

## Concordant haplotype pairs at a given radius

The number of ordered pairs of distinct haplotypes of `C` whose windows of radius `d`
agree.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.concordantPairs`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#concordant-pairs).

## Extended haplotype homozygosity (EHH)

Extended haplotype homozygosity at radius `d` of the haplotype set `C`: the probability
that two distinct haplotypes drawn from `C` without replacement agree at all `d` sites nearest
the core (Sabeti et al. 2002). For `#C ≤ 1` the denominator vanishes and the junk value `0` is
returned; every statement below that needs the probabilistic reading assumes `2 ≤ #C`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#ehh).

## EHH is zero for a set of at most one haplotype

Outside the domain `2 ≤ #C` the definition returns the junk value `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_eq_zero_of_card_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#ehh-eq-zero-of-card-le-one).

## EHH at radius zero equals one

At radius `0` every pair of haplotypes agrees, so `EHH(0) = 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_zero_window`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#ehh-zero-window).

## EHH is nonincreasing in the radius

EHH is nonincreasing in the radius: widening the window can only break ties.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_antitone`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#ehh-antitone).

## EHH as homozygosity of window-type counts

EHH as the sampling-without-replacement homozygosity of the partition of `C` into window
types: `EHH(d) = ∑_t c_t (c_t - 1) / (#C (#C - 1))`, where `c_t` is the number of haplotypes of
`C` with window `t`. This is the form in which EHH is usually defined.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ehh_eq_sum_counts`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#ehh-eq-sum-counts).

## Concordant haplotype pairs sharing a core allele

The number of ordered pairs of distinct haplotypes of `C` whose core alleles (under
`core`) agree and whose windows of radius `d` agree. The extended haplotype includes the
core, so pairs carrying different core alleles are never concordant, even when their
outward windows match.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.concordantPairsCore`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#concordant-pairs-core).

## Extended haplotype homozygosity with core-allele labels

Extended haplotype homozygosity with core-allele labels: the probability that two
distinct haplotypes drawn from `C` without replacement share both their core allele and
their window of radius `d`. For a set `C` of carriers of a single core allele this is the
same count as `ehh`; for a pooled set `D` carrying several core alleles it excludes the
cross-core pairs that plain `ehh` would wrongly count as concordant.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ehhCore`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#ehh-core).

## Relative extended haplotype homozygosity (REHH)

Relative extended haplotype homozygosity: the core-labelled EHH of the core-allele
carriers `C` divided by the core-labelled EHH of the pooled set `D` of haplotypes carrying
the other core alleles. The denominator counts only pairs sharing a core allele, so
cross-core pairs never inflate it. This is the statistic of the long-range haplotype test
(Sabeti et al. 2002). It is a junk value `0` when the denominator vanishes;
`one_lt_rehh_iff` assumes a positive denominator.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.rehh`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#rehh).

## Criterion for relative EHH to exceed one

With a positive reference EHH, the relative EHH exceeds `1` exactly when the core allele's
haplotypes are the more homozygous ones.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.one_lt_rehh_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#one-lt-rehh-iff).

## Probability of no recombination on a pair's genealogy

The probability that no recombination falls on the genealogy of a pair of lineages within
genetic distance `d` of the core, given that the pair coalesces at time `t` (time in units of
`2N` generations, `ρ = 4Nr` the scaled recombination rate per site): the two lineages carry
recombination events at total rate `ρ * d` until they coalesce.

In a mutation-free model this is a lower bound for the probability that the two haplotypes
are identical over the window — no recombination then implies identical windows, while a
recombined lineage may still carry the same alleles — so it is a lower bound for the
expected EHH, not its value. Without the mutation-free assumption the bound is not
established: mutations on either descendant branch can make the haplotypes differ even
with no recombination.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.pairNoRecomb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#pair-no-recomb).

## No-recombination probability decays with distance

The no-recombination probability decays in the distance from the core.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.pairNoRecomb_antitone`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#pair-no-recomb-antitone).

## Mean no-recombination probability under the neutral coalescent

Averaging over the pair coalescence time `T₂`, which is exponential of rate `1` in units of
`2N` generations under the neutral coalescent, the probability that no recombination falls on
the pair's genealogy within distance `d` is `1 / (1 + ρ d)`. In a mutation-free model, since
a recombined lineage can still carry an identical haplotype, this is a lower bound for
`E[EHH(d)]`; without that assumption the bound is not established.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.integral_pairNoRecomb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/ExtendedHaplotypeHomozygosity.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html#integral-pair-no-recomb).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extended haplotype homozygosity](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/detecting-selection/extended-haplotype-homozygosity)
