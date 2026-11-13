---
declaration: section
origin: cited
lean: StatMech.FK.innerBdryFinEvent, StatMech.FK.condBcProb_add_sum_eq_smallerBox, StatMech.FK.condWiredSucc_le_smallerBox
statement: formalized
proof: formalized
---

# One-step comparison of wired boundary-connection probabilities

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/one-step-comparison-of-wired-boundary-connection/index.html).

## B. Boundary-connection events

## Origin-to-$\partial\Lambda_n$ event as an event on $\Lambda_{n+1}$

The event on `Λ_(n+1)` that the origin is connected to `∂Λ_n` by open edges of `Λ_n`.

Formalized by `StatMech.FK.innerBdryFinEvent`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredBoxLimit.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredBoxLimit.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/one-step-comparison-of-wired-boundary-connection/index.html#inner-bdry-fin-event).

## Closed annulus plus inner-boundary wiring gives wired $\Lambda_n$ law

With all annulus edges closed and a wiring made of the inner-boundary clique and an annulus
wiring `D`, the conditional measure on `Λ_(n+1)` equals the wired measure on `Λ_n`, on any event
pulled back by `crossExt`.

Formalized by `StatMech.FK.condBcProb_add_sum_eq_smallerBox`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredBoxLimit.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredBoxLimit.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/one-step-comparison-of-wired-boundary-connection/index.html#cond-bc-prob-add-sum-eq-smaller-box).

## Closed-annulus wired bound on origin-to-$\partial\Lambda_n$, $q = 2$

At `q = 2`, the wired measure on `Λ_(n+1)` conditioned on all annulus edges closed gives `{0 ↔
∂Λ_n}` at most `φ¹_n(0 ↔ ∂Λ_n)`.

Formalized by `StatMech.FK.condWiredSucc_le_smallerBox`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/WiredBoxLimit.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/WiredBoxLimit.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/one-step-comparison-of-wired-boundary-connection/index.html#cond-wired-succ-le-smaller-box).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: One-step comparison of wired boundary-connection probabilities](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/one-step-comparison-of-wired-boundary-connection/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/one-step-comparison-of-wired-boundary-connection)
