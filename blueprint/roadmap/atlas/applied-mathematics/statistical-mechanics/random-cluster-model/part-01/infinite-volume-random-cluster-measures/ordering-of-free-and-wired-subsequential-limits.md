---
declaration: section
origin: cited
lean: StatMech.FK.weakLimit_extremality_of_common_subseq, StatMech.FK.exists_common_subseq_weak_limits, StatMech.FK.exists_infiniteVolume_extremal
statement: formalized
proof: formalized
---

# Ordering of free and wired subsequential limits

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/ordering-of-free-and-wired-subsequential-limits/index.html).

## A. Domination passes to weak limits

## Free limit at most wired limit along a common subsequence, $q \ge 1$

If free and wired box measures converge weakly to `ν₀` and `ν₁` along a common subsequence and
`q ≥ 1`, then `ν₀(A) ≤ ν₁(A)` for every clopen increasing event `A`.

Formalized by `StatMech.FK.weakLimit_extremality_of_common_subseq`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitsInfinite.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitsInfinite.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/ordering-of-free-and-wired-subsequential-limits/index.html#weak-limit-extremality-of-common-subseq).

## Common subsequence with free and wired weak limits

Free and wired box measures have weak limits along a common strictly increasing subsequence.

Formalized by `StatMech.FK.exists_common_subseq_weak_limits`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitsInfinite.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitsInfinite.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/ordering-of-free-and-wired-subsequential-limits/index.html#exists-common-subseq-weak-limits).

## Ordered free and wired subsequential limits exist for $q \ge 1$

For `q ≥ 1` there are a subsequence and weak limits `φ0` (free) and `φ1` (wired) along it with
`φ0(A) ≤ φ1(A)` for all clopen increasing `A`.

Formalized by `StatMech.FK.exists_infiniteVolume_extremal`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/LimitsInfinite.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/LimitsInfinite.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/ordering-of-free-and-wired-subsequential-limits/index.html#exists-infinite-volume-extremal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ordering of free and wired subsequential limits](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/ordering-of-free-and-wired-subsequential-limits/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/ordering-of-free-and-wired-subsequential-limits)
