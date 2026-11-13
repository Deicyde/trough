---
declaration: section
origin: cited
lean: StatMech.ConfigSpace.shift, StatMech.ConfigSpace.shift_eq_arrowAction_smul, StatMech.ConfigSpace.IsTranslationInvariant, StatMech.ConfigSpace.IsErgodic, StatMech.FK.bernoulli_iIndepFun, StatMech.FK.bernoulli_ergodic, StatMech.FK.bernoulli_isErgodic
statement: formalized
proof: formalized
---

# Translation invariance and ergodicity of random fields

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html).

## Shift of a configuration by a group element

The shift of a configuration by `g : G`: `(shift g ω) e = ω (g⁻¹ • e)`. This is the action
`arrowAction` of Mathlib on functions out of `E`.

Formalized by `StatMech.ConfigSpace.shift`, a definition declared in [MathlibExt/Probability/Configuration/Ergodicity.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Configuration/Ergodicity.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#shift).

## Configuration shift is the action on functions

`shift` is Mathlib's `arrowAction` of `G` on functions `E → Bool`.

Formalized by `StatMech.ConfigSpace.shift_eq_arrowAction_smul`, a lemma declared in [MathlibExt/Probability/Configuration/Ergodicity.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Configuration/Ergodicity.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#shift-eq-arrow-action-smul).

## Translation-invariant measure on configuration space

A measure on `ConfigSpace E` is translation invariant if every shift `shift g`, `g : G`,
preserves it.

Formalized by `StatMech.ConfigSpace.IsTranslationInvariant`, a definition declared in [MathlibExt/Probability/Configuration/Ergodicity.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Configuration/Ergodicity.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#is-translation-invariant).

## Ergodic measure on configuration space

A measure on `ConfigSpace E` is ergodic for the shift action of `G` if it is translation
invariant and every measurable set with `shift g ⁻¹' s = s` for all `g` has measure `0` or
`μ univ`. See also Mathlib's `ErgodicSMul`, which asks the same for a.e.-invariant sets.

Formalized by `StatMech.ConfigSpace.IsErgodic`, a definition declared in [MathlibExt/Probability/Configuration/Ergodicity.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Configuration/Ergodicity.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#is-ergodic).

## Independence of coordinates under the Bernoulli product measure

Coordinates are independent under the Bernoulli product measure. See also Mathlib's
`ProbabilityTheory.iIndepFun_infinitePi`, of which this is a special case.

Formalized by `StatMech.FK.bernoulli_iIndepFun`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Ergodicity.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Ergodicity.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#bernoulli-i-indep-fun).

## Bernoulli zero-one law for infinite groups acting finite-to-one

Invariant events of the Bernoulli product measure have probability `0` or `1`.

Formalized by `StatMech.FK.bernoulli_ergodic`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Ergodicity.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Ergodicity.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#bernoulli-ergodic).

## Ergodicity of Bernoulli measures under free infinite-group actions

The Bernoulli product measure is ergodic under every action of an infinite group with injective
orbit maps.

Formalized by `StatMech.FK.bernoulli_isErgodic`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Ergodicity.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Ergodicity.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html#bernoulli-is-ergodic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Translation invariance and ergodicity of random fields](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/random-fields/translation-invariance-and-ergodicity-of-random)
