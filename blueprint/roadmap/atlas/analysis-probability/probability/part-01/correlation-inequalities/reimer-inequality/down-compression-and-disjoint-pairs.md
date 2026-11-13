---
declaration: section
origin: cited
lean: StatMech.cfgSupport, StatMech.supportCfg, StatMech.cfgEquivFinset, StatMech.downCompress, StatMech.reimer_wprob_one, StatMech.DependsOn, StatMech.disjointOccurrence_eq_inter_of_dependsOn, StatMech.wprob_inter_mul_of_split
statement: formalized
proof: formalized
---

# Down-compression and disjoint pairs

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html).

## Support of a configuration as a finset

The support `{i | ω i = true}` of a configuration, as a finset.

Formalized by `StatMech.cfgSupport`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#cfg-support).

## Configuration with a given support

The configuration whose open coordinates are exactly the elements of `s`.

Formalized by `StatMech.supportCfg`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#support-cfg).

## Configurations on a finite set as finsets

Configurations on a finite set are the same as finsets (their supports).

Formalized by `StatMech.cfgEquivFinset`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#cfg-equiv-finset).

## Down-compression of a family of configurations

Down-compression at `i` of a family of configurations, through `cfgEquivFinset`.

Formalized by `StatMech.downCompress`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#down-compress).

## Reimer's inequality on one coordinate

Reimer's inequality on one coordinate, for all events.

Formalized by `StatMech.reimer_wprob_one`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#reimer-wprob-one).

## Event depending only on a set of coordinates

`DependsOn A S`: whether a configuration lies in `A` depends only on its values on `S`.
This is Mathlib's `DependsOn` for the membership predicate of `A`.

Formalized by `StatMech.DependsOn`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#depends-on).

## Disjoint occurrence equals intersection for disjoint dependence sets

If `A` depends only on `S`, `B` only on `T`, and `S, T` are disjoint, then
`A □ B = A ∩ B`.

Formalized by `StatMech.disjointOccurrence_eq_inter_of_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#disjoint-occurrence-eq-inter-of-depends).

## Independence of events on complementary coordinate sets

Events depending on complementary coordinate sets are independent under a product
probability weight.

Formalized by `StatMech.wprob_inter_mul_of_split`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#wprob-inter-mul-of-split).

## Reimer's inequality for events on disjoint coordinate sets

Reimer's inequality, with equality, for events depending on disjoint coordinate sets.

Formalized by `StatMech.reimer_wprob_of_disjoint_support`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerCompression.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#reimer-wprob-of-disjoint-support).

## Number of disjoint pairs from two families

The number of disjoint pairs `(S, T) ∈ 𝒜 × ℬ`.

Formalized by `StatMech.dpairsCount`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointPairCount.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointPairCount.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#dpairs-count).

## Recursion for disjoint pairs by membership of a coordinate

Splitting disjoint pairs by membership of `i`: pairs where neither, only the first, or
only the second set contains `i`.

Formalized by `StatMech.dpairsCount_fiber_recursion`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointPairCount.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointPairCount.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#dpairs-count-fiber-recursion).

## One compression step on the doubled disjoint-pair family

Bookkeeping for one compression step at coordinate `i` on `boxDoubled 𝒜 ℬ`:
`doubleCompress i` preserves its size and makes it down-closed at `inl i` and up-closed at
`inr i`, and sizes split over `memberSubfamily i` and `nonMemberSubfamily i`.

Formalized by `StatMech.reimer_butterfly_compress_step`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDisjointPairCount.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDisjointPairCount.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#reimer-butterfly-compress-step).

## Down-compression does not decrease the disjoint-pair count

Down-compressing both families at `i` does not decrease the number of disjoint pairs.

Formalized by `StatMech.dpairsCount_downDown_mono`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#dpairs-count-down-down-mono).

## Weight kernel of disjoint pairs off a coordinate

`fwt' w i S * fwt' w i T` for disjoint `S, T`, and `0` otherwise.

Formalized by `StatMech.pairKernel'`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#pair-kernel).

## Down-compression does not decrease weighted disjoint pairs

Down-compressing both families at `i` does not decrease the weighted number of disjoint
pairs when `w i true ≤ w i false`.

Formalized by `StatMech.wdpairs_downDown_mono`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#wdpairs-down-down-mono).

## Weighted down-compression monotonicity fails for general weights

Without `w i true ≤ w i false`, `wdpairs_downDown_mono` can fail.

Formalized by `StatMech.wdpairs_downDown_not_mono_general`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerDownCompressionPairs.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#wdpairs-down-down-not-mono-general).

## Iterated down-compression along a list of coordinates

Down-compression at each coordinate of `cs` in turn (the head of `cs` is applied last).

Formalized by `StatMech.iterDownComp`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#iter-down-comp).

## Down-compression map on a single finset

The compression map: erase `i` from `s` when `s` contains `i` and `s.erase i ∉ 𝒜`.

Formalized by `StatMech.cmap`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#cmap).

## Total size of a family of finsets

The total size `∑ S ∈ 𝒜, #S` of a family.

Formalized by `StatMech.totalSize`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#total-size).

## Iterated down-compression reaches a lower set

Some iterated down-compression of `𝒜` is a lower set.

Formalized by `StatMech.exists_iterDownComp_isLowerSet`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerIteratedCompression.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#exists-iter-down-comp-is-lower-set).

## Members of a disjoint-union family avoiding a coordinate

The members of `𝒜 ○ ℬ` avoiding `i` are exactly the disjoint unions of members of `𝒜` and
`ℬ` avoiding `i`.

Formalized by `StatMech.boxFamily_filter_notMem_coord`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#box-family-filter-not-mem-coord).

## Family closed under erasing a coordinate

`IsDownAtCoord i 𝒜`: the family `𝒜` is closed under erasing `i`.

Formalized by `StatMech.IsDownAtCoord`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#is-down-at-coord).

## First family in the box-compression counterexample

The family `{∅, {1}}` on `Fin 2`, the first family of the counterexample
`StatMech.reimerStep_box_compression_false`.

Formalized by `StatMech.reimerStepCexA`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#reimer-step-cex-a).

## Second family in the box-compression counterexample

The family `{∅, {0, 1}}` on `Fin 2`, the second family of the counterexample
`StatMech.reimerStep_box_compression_false`.

Formalized by `StatMech.reimerStepCexB`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#reimer-step-cex-b).

## Down-compression can shrink the disjoint-union family

Down-compressing both families at the same coordinate can strictly decrease the size of
`𝒜 ○ ℬ`.

Formalized by `StatMech.reimerStep_box_compression_false`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/ReimerStep.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html#reimer-step-box-compression-false).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Down-compression and disjoint pairs](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/down-compression-and-disjoint-pairs)
