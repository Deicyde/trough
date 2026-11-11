---
declaration: section
origin: cited
lean: ProbabilityTheory.IsPoissonProcess, ProbabilityTheory.PoissonProcess.arrivalTime, ProbabilityTheory.PoissonProcess.count, ProbabilityTheory.PoissonProcess.hasLaw_arrivalTime, ProbabilityTheory.PoissonProcess.hasLaw_count, ProbabilityTheory.PoissonProcess.ae_count_zero, ProbabilityTheory.PoissonProcess.ae_count_monotone, ProbabilityTheory.IsPoissonProcess.add
statement: formalized
proof: formalized
---

# Poisson processes

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html).

## Probability Theory

## Poisson process

`N : ℝ≥0 → Ω → ℕ` is a **Poisson process of rate `r`** under `P` (Kingman 1993, ch. 4;
Karlin–Taylor 1975, ch. 4): `N 0 = 0` and the paths are nondecreasing almost surely, the
increments over consecutive intervals are independent, and for `s ≤ t` the increment `N t - N s`
has the Poisson law of mean `r (t - s)`.

Formalized by `ProbabilityTheory.IsPoissonProcess`, a structure declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#is-poisson-process).

## Arrival times from interarrival times

The `n`-th arrival time `S n = T 0 + ⋯ + T (n - 1)` of the interarrival times `T`.

Formalized by `ProbabilityTheory.PoissonProcess.arrivalTime`, a definition declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#arrival-time).

## Counting process of interarrival times

The counting process of the interarrival times `T`: `count T t ω` is the number of arrivals
`n ≥ 1` with `S n ≤ t`. When that set is infinite (a null event for exponential interarrivals of
positive rate) `Set.ncard` returns `0`.

Formalized by `ProbabilityTheory.PoissonProcess.count`, a definition declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#count).

## Arrival times of exponential interarrivals are Erlang

The `(n + 1)`-th arrival time of i.i.d. rate-`r` exponential interarrivals has the Gamma
(Erlang) law with shape `n + 1` and rate `r` (Karlin–Taylor 1975, §4.2).

Formalized by `ProbabilityTheory.PoissonProcess.hasLaw_arrivalTime`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#has-law-arrival-time).

## Arrival counts of exponential interarrivals are Poisson

The number of arrivals in `[0, t]` of i.i.d. rate-`r` exponential interarrivals has the
Poisson law of mean `r t` (Karlin–Taylor 1975, §4.2, Theorem 2.1).

Formalized by `ProbabilityTheory.PoissonProcess.hasLaw_count`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#has-law-count).

## Counting process starts at zero almost surely

The counting process of i.i.d. rate-`r` exponential interarrivals starts at `0` almost
surely (all interarrival times are positive almost surely).

Formalized by `ProbabilityTheory.PoissonProcess.ae_count_zero`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#ae-count-zero).

## Counting process has nondecreasing paths almost surely

The counting process of i.i.d. rate-`r` exponential interarrivals has nondecreasing paths
almost surely (the arrival times tend to infinity almost surely, so every arrival set in
`[0, t]` is finite).

Formalized by `ProbabilityTheory.PoissonProcess.ae_count_monotone`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#ae-count-monotone).

## Superposition

**Superposition** (Kingman 1993, §2.2): the sum of two independent Poisson processes of rates
`r₁` and `r₂` is a Poisson process of rate `r₁ + r₂`. Independence is of the two processes as
random paths.

Formalized by `ProbabilityTheory.IsPoissonProcess.add`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#add).

## Thinning of a Poisson process

The thinning of `N` by the marks `B`: the number of indices `i < N t` with `B i`, i.e. the
number of points of `N` in `[0, t]` that are kept when the `i`-th point (in time order, from
`0`) is kept iff `B i`.

Formalized by `ProbabilityTheory.PoissonProcess.thinning`, a definition declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#thinning).

## Thinning

**Thinning** (Kingman 1993, §5.1; Karlin–Taylor 1975, §4.1): keeping each point of a Poisson
process of rate `r` independently with probability `p`, independently of the process, gives a
Poisson process of rate `p r`. The marks `B i` are i.i.d. with `P(B i) = p` and independent of
`N` as a random path.

Formalized by `ProbabilityTheory.IsPoissonProcess.thinning`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 919](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#thinning-2).

## Independent Poisson increments of the counting process

The increments of the counting process of i.i.d. rate-`r` exponential interarrivals over
consecutive intervals `(t i, t (i + 1)]` are independent with the Poisson laws of means
`r (t (i + 1) - t i)`: the increment vector has the product law (Kingman 1993, ch. 4;
Karlin–Taylor 1975, ch. 4).

Formalized by `ProbabilityTheory.PoissonProcess.hasLaw_count_increments`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 1488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L1488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#has-law-count-increments).

## Exponential interarrivals give a Poisson process

**Exponential interarrivals give a Poisson process** (Kingman 1993, ch. 4; Karlin–Taylor
1975, ch. 4): the counting process of i.i.d. rate-`r` exponential interarrival times is a Poisson
process of rate `r`.

Formalized by `ProbabilityTheory.PoissonProcess.isPoissonProcess_count`, a theorem declared in [MathlibExt/Probability/Process/PoissonProcess.lean, line 1511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/PoissonProcess.lean#L1511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html#is-poisson-process-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson processes](https://deicyde.github.io/atlas-lean/roadmap/Probability/point-processes/poisson-processes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/point-processes/poisson-processes)
