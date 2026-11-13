---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.sum_inv_choose_two, MathlibExt.Biology.PopulationGenetics.Coalescent.sum_mul_inv_choose_two, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.tmrca, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.totalLength, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.choose_two_pos, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integrable_T, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_T
statement: formalized
proof: formalized
---

# Kingman's coalescent and Watterson's estimator

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html).

## Elementary sums

## Sum of reciprocals of binomial coefficients $\binom{k}{2}$

`∑_{k=2}^n (k.choose 2)⁻¹ = 2 (1 - 1/n)` for `n ≥ 1` (telescoping `2/(k(k-1))`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_inv_choose_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#sum-inv-choose-two).

## Weighted sum of reciprocals of $\binom{k}{2}$ is twice a harmonic number

`∑_{k=2}^n k (k.choose 2)⁻¹ = 2 H_{n-1}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_mul_inv_choose_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#sum-mul-inv-choose-two).

## Holding times of Kingman's coalescent

Kingman's coalescent for a sample of size `n`, through its holding times: `T k` is the
time (in units of `2N` generations) during which the genealogy has exactly `k` lineages,
for `2 ≤ k ≤ n`. These are independent, and `T k` is exponential with rate `k.choose 2`.
The values of `T k` for `k ∉ [2, n]` are irrelevant.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes`, a structure declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#kingman-times).

## Time to the most recent common ancestor

Time to the most recent common ancestor of the sample.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.tmrca`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#tmrca).

## Total branch length of a coalescent genealogy

Total branch length of the sample genealogy: `k` branches during `T k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.totalLength`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#total-length).

## Positivity of the number of pairs

The number of pairs `k.choose 2` is positive for `k ∈ [2, n]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.choose_two_pos`, a lemma declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#choose-two-pos).

## Integrability of coalescent holding times

Each holding time is integrable.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integrable_T`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integrable-t).

## Expected coalescent holding time

`E[T k] = (k.choose 2)⁻¹`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_T`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integral-t).

## Expected time to the most recent common ancestor

The expected time to the most recent common ancestor is `2 (1 - 1/n)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_tmrca`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integral-tmrca).

## Integrability of the total branch length

The total branch length is integrable.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integrable_totalLength`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integrable-total-length).

## Expected total branch length of the coalescent

The expected total branch length is `2 H_{n-1}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_totalLength`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integral-total-length).

## Variance of the time to the most recent common ancestor

The variance of the time to the most recent common ancestor is
`∑_{k=2}^n ((k.choose 2)⁻¹)²` (this uses independence).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.variance_tmrca`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#variance-tmrca).

## Expected number of segregating sites

Infinite-sites mutation at rate `θ/2` per lineage per unit time: if the number of
segregating sites `S` is integrable and has conditional mean `(θ/2) L` given the genealogy
σ-algebra `m`, then `E S = θ H_{n-1}`. (Integrability matters: Mathlib's conditional
expectation of a non-integrable function is `0`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_segSites`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integral-seg-sites).

## Integrability of Watterson's estimator

Watterson's estimator `S / H_{n-1}` is integrable when `S` is.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integrable_watterson`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#integrable-watterson).

## Watterson's estimator is unbiased

`E[S / H_{n-1}] = θ` for a sample of size
`n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.watterson_unbiased`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#watterson-unbiased).

## Canonical probability space for Kingman holding times

The canonical probability space for the Kingman holding times of a sample of size `n`:
the product of the exponential laws `Exp (k.choose 2)`, `2 ≤ k ≤ n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.piMeasure`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#pi-measure).

## Kingman coalescent from coordinate projections

The coordinate projections of `piMeasure n` form a Kingman coalescent; in particular
`KingmanTimes` is inhabited for every sample size.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.ofPi`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#of-pi).

## Probability of no coalescence in one Wright–Fisher generation

In a Wright–Fisher population of `M` gene copies, the probability that `k` lineages,
choosing their parents independently and uniformly, have `k` distinct parents.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.noCoalProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#no-coal-prob).

## No-coalescence probability as a falling factorial ratio

`noCoalProb M k` is the falling factorial `M (M-1) ⋯ (M-k+1)` divided by `M ^ k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.noCoalProb_eq_descFactorial_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#no-coal-prob-eq-desc-factorial-div).

## No-coalescence probability tends to one

`noCoalProb M k → 1` as `M → ∞`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tendsto_noCoalProb_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#tendsto-no-coal-prob-one).

## Kingman's coalescence rate

For `M` gene copies (`M = 2N`), the per-generation
probability that some of `k` lineages coalesce is `(k.choose 2) / M + o(1/M)`; i.e. in time
units of `M` generations, coalescences occur at rate `k.choose 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tendsto_coalescence_rate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#tendsto-coalescence-rate).

## Wright–Fisher coalescence times converge to exponential laws

After `⌊t M⌋` Wright–Fisher generations (`t ≥ 0` coalescent time units), the probability
that `k` lineages have not coalesced tends to `exp (-(k.choose 2) t)`, the survival function
of the exponential law with rate `k.choose 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tendsto_noCoalProb_pow_floor`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/Kingman.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html#tendsto-no-coal-prob-pow-floor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kingman's coalescent and Watterson's estimator](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/coalescent-theory/kingman-s-coalescent-and-watterson-s-estimator)
