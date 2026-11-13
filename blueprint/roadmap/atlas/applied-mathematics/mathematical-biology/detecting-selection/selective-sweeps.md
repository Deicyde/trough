---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepTraj, MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepTraj_mem_Ioo, MathlibExt.Biology.PopulationGenetics.SelectionScan.hasDerivAt_sweepTraj, MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepDuration, MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepTraj_sweepDuration, MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepDuration_pos, MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepDuration_full, MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepEhh
statement: formalized
proof: formalized
---

# Selective sweeps

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html).

## The deterministic logistic sweep

## Logistic trajectory of a selective sweep

The logistic trajectory of a favourable allele with genic selection coefficient `s`,
starting from frequency `x₀`: the solution of `x' = s x (1 - x)` with `x 0 = x₀`
(Maynard Smith and Haigh 1974).

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepTraj`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-traj).

## Sweep trajectory stays strictly between 0 and 1

The trajectory stays strictly between `0` and `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepTraj_mem_Ioo`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-traj-mem-ioo).

## Sweep trajectory solves the logistic equation

The logistic equation: `x'(t) = s x(t) (1 - x(t))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.hasDerivAt_sweepTraj`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#has-deriv-at-sweep-traj).

## Duration of a logistic sweep between two frequencies

The time the logistic trajectory with selection coefficient `s` takes to go from frequency
`a` to frequency `b`: `(1/s) log (b (1 - a) / (a (1 - b)))`, the difference of the logits
divided by `s`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepDuration`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-duration).

## Sweep trajectory reaches its target at the sweep duration

`sweepDuration s a b` is the exact time at which the trajectory started at `a` reaches
`b`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepTraj_sweepDuration`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-traj-sweep-duration).

## Positivity of the sweep duration

The time to reach a higher frequency is positive.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepDuration_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-duration-pos).

## Duration of a complete deterministic sweep

A complete sweep in a population of `N` diploids, from a single copy `1 / (2N)` to
`1 - 1 / (2N)`, takes exactly `(2 / s) log (2N - 1)` generations in the deterministic logistic
model. (The familiar `(2 / s) log (2Ns)` is the conditional expected duration of the
corresponding stochastic sweep, a different quantity.)

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepDuration_full`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-duration-full).

## EHH in the star-genealogy sweep model

The probability that two carriers of a swept allele are identical over a window of genetic
length `d`, in the star-genealogy model of Voight et al. (2006): all carriers coalesce at the
start of the sweep, a time `T` ago, and the pair is identical exactly when neither of its two
lineages recombined, each at rate `r * d` per unit time.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepEhh`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-ehh).

## Star-genealogy EHH as a squared Poisson zero probability

The star-genealogy EHH is the square of the probability that a Poisson number of
recombination events with mean `r d T` on one lineage is zero.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepEhh_eq_poisson_sq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-ehh-eq-poisson-sq).

## Star-genealogy EHH decays with window length

Haplotype homozygosity decays with the window length.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepEhh_antitone`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-ehh-antitone).

## One-sided integrated haplotype homozygosity

The one-sided integrated haplotype homozygosity: the area under the EHH decay curve
in one direction from the focal site. Voight et al.'s iHH integrates in both directions;
see `ihh_twoSided`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihh`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihh).

## Two-sided integrated haplotype homozygosity

The two-sided integrated haplotype homozygosity of Voight et al.: the sum of the
one-sided integrals in the two chromosome directions.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihh_twoSided`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihh-two-sided).

## One-sided iHH in the star-genealogy model

In the star-genealogy model the one-sided integrated haplotype homozygosity is
`1 / (2 r T)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihh_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihh-eq).

## Two-sided iHH in the star-genealogy model

In the star-genealogy model the two-sided integrated haplotype homozygosity is
`1 / (r T)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihh_twoSided_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihh-two-sided-eq).

## Integrated haplotype score (iHS)

The integrated haplotype score of Voight et al. (2006): the log ratio of the integrated
haplotype homozygosities of the ancestral and the derived allele, whose star genealogies have
ages `T_A` and `T_D`. The factor of two between the one-sided and two-sided integrals
cancels in this ratio.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihs`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihs).

## iHS as the log ratio of genealogy ages

In the star-genealogy model the integrated haplotype score is the log ratio of the two
ages, so the recombination rate cancels.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihs_eq_log_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihs-eq-log-div).

## iHS is negative exactly when the derived allele is younger

The integrated haplotype score is negative exactly when the derived allele's star
genealogy is the younger one, i.e. when the derived allele swept faster.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.ihs_neg_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#ihs-neg-iff).

## Power-law EHH after a complete sweep

Combining the exact sweep duration with the star-genealogy decay: after a complete sweep
of a favourable allele with selection coefficient `s` in a population of `N` diploids, the
extended haplotype homozygosity at genetic distance `d` is the power law
`(2N - 1) ^ (-(4 r d / s))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweepEhh_sweepDuration_full`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/SelectionScan/SelectiveSweep.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html#sweep-ehh-sweep-duration-full).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Selective sweeps](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/selective-sweeps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/detecting-selection/selective-sweeps)
