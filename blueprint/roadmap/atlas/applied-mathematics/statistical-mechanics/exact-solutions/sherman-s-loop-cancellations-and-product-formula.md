---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_reversibleTurnMatrix, StatMech.Onsager.ons_stateWeightedReversibleTurnMatrix, StatMech.Onsager.ons_involutiveLoopRev, StatMech.Onsager.ons_maskedReversibleFactor, StatMech.Onsager.ons_factorMajorant, StatMech.Onsager.ons_ShermanRadius, StatMech.Onsager.ons_tupleProd_eq_listProd, StatMech.Onsager.ons_one_sub_ne_zero_of_norm_lt_one
statement: formalized
proof: formalized
---

# Sherman's loop cancellations and product formula

53 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html).

## Reversible turn matrix on a state space with directions

The matrix `q x y · turnW(dir y, dir x)` on an abstract state space with directions.

Formalized by `StatMech.Onsager.ons_reversibleTurnMatrix`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-reversible-turn-matrix).

## State-weighted reversible turn matrix

The reversible turn matrix with additional row and column weights on states.

Formalized by `StatMech.Onsager.ons_stateWeightedReversibleTurnMatrix`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-state-weighted-reversible-turn-matri).

## Reversal of a cyclic sequence of states

Reversal of a cyclic sequence of states: position `k` carries `rev` of the state at position
`-k`.

Formalized by `StatMech.Onsager.ons_involutiveLoopRev`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean, line 799](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean#L799). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-involutive-loop-rev).

## Masked reversible factor

The reversible factor with the rows and columns of `forbidden` set to zero.

Formalized by `StatMech.Onsager.ons_maskedReversibleFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean, line 925](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/AugmentedTurnCancellation.lean#L925). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-masked-reversible-factor).

## Majorant $q^{|s|-1}$ for the weight of a walk

The majorant `q^{|s| - 1}` for the weight of a walk `s` with at least two states, and `0` for
shorter lists.

Formalized by `StatMech.Onsager.ons_factorMajorant`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanConvergence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanConvergence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-factor-majorant).

## Sherman's convergence radius for the torus Kac-Ward matrix

The radius `1 / (2 (number of darts)²)` below which Sherman's first-return series for the torus
Kac-Ward matrix converges with total weight below `1`.

Formalized by `StatMech.Onsager.ons_ShermanRadius`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanConvergence.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanConvergence.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-sherman-radius).

## Product over a tuple equals the product over its list

The product over a tuple equals the product over the list `List.ofFn p`; see also
`List.prod_ofFn` and `List.map_ofFn`.

Formalized by `StatMech.Onsager.ons_tupleProd_eq_listProd`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFactor.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFactor.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-tuple-prod-eq-list-prod).

## $1 - z \neq 0$ for $|z| < 1$

`1 - z ≠ 0` when `‖z‖ < 1`.

Formalized by `StatMech.Onsager.ons_one_sub_ne_zero_of_norm_lt_one`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFirstReturn.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFirstReturn.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-one-sub-ne-zero-of-norm-lt-one).

## First-return loop at a directed edge

A cyclic sequence `v` is a first-return loop at `e` (avoiding `rev e`) if it starts at `e`, does
not visit `e` again, and never uses the reverse edge `rev e`.

Formalized by `StatMech.Onsager.ons_isFirstReturn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFirstReturn.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFirstReturn.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-is-first-return).

## Cyclic sequences rooted at an edge avoiding its reverse

The cyclic sequences of length `n` that start at `e` and never use `rev e`.

Formalized by `StatMech.Onsager.ons_rootedAvoiding`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFirstReturn.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanFirstReturn.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rooted-avoiding).

## Term of the list series: product of weights over length

The term `(∏_{a ∈ l} wt a) / |l|` of the list series, set to `0` on the empty list.

Formalized by `StatMech.Onsager.ons_listSeriesTerm`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanListSeries.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanListSeries.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-list-series-term).

## Weight of a cyclic sequence

The weight `∏ₖ Λ (v k) (v (k + 1))` of a cyclic sequence `v : Fin n → E`, indices taken modulo
`n`.

Formalized by `StatMech.Onsager.ons_loopWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLoop.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLoop.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-loop-weight).

## Rotation of a cyclic sequence by one step

Rotation of a cyclic sequence by one step: `(ons_cyclicShift v) k = v (k + 1)`.

Formalized by `StatMech.Onsager.ons_cyclicShift`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLoop.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLoop.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-cyclic-shift).

## Kac-Ward bucket: walks through a dart, not its reverse

The total Kac-Ward weight of closed walks of length `n + 1` that visit `e` but not its reverse.

Formalized by `StatMech.Onsager.ons_bucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanDetFactor.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanDetFactor.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-bucket-e).

## Kac-Ward bucket: walks avoiding a dart and its reverse

The total Kac-Ward weight of closed walks of length `n + 1` that visit neither `e` nor its
reverse.

Formalized by `StatMech.Onsager.ons_bucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanDetFactor.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanDetFactor.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-bucket-n).

## Loop sum vanishes under a fixed-point-free sign-reversing involution

A fixed-point-free involution of `S` that reverses the sign of the loop weight forces the loop
weights over `S` to sum to zero. See also `Finset.sum_involution`.

Formalized by `StatMech.Onsager.ons_sum_zero_of_sign_involution`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-sum-zero-of-sign-involution).

## Cyclic sequences visiting two given states

The cyclic sequences of length `n` that visit both `a` and `b`.

Formalized by `StatMech.Onsager.ons_loopSetBoth`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-loop-set-both).

## Mirror position within a segment

The mirror image `l + m - k` of a position `k` in the segment `[l, m]` (truncated to `n - 1`).

Formalized by `StatMech.Onsager.ons_mir`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-mir).

## Reversal of a segment of a cyclic sequence

Reversal of the segment `[l, m]` of `v`: positions inside are mirrored and their entries
replaced by their reverses; positions outside are unchanged.

Formalized by `StatMech.Onsager.ons_revSeg`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rev-seg).

## Positions where a sequence meets an edge or its reverse

The positions where `v` meets `e` or `rev e`.

Formalized by `StatMech.Onsager.ons_hitSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-hit-set).

## First position meeting an edge or its reverse

The first position where `v` meets `e` or `rev e` (`0` if there is none).

Formalized by `StatMech.Onsager.ons_l`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-l).

## Positions meeting the reverse of the first hit

The positions where `v` meets the reverse of its entry at `ons_l e rev v`.

Formalized by `StatMech.Onsager.ons_mSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-m-set).

## Last position meeting the reverse of the first hit

The last position where `v` meets the reverse of its entry at `ons_l e rev v` (`0` if there is
none).

Formalized by `StatMech.Onsager.ons_m`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-m).

## Sherman's segment-reversal surgery

Sherman's surgery: reverse the segment between `ons_l` and `ons_m` when `v` visits both `e` and
`rev e`; otherwise leave `v` unchanged.

Formalized by `StatMech.Onsager.ons_surgery`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-surgery).

## Sherman's Lemma 5

If the surgery reverses the sign of loop weights, the loops that visit
both `e` and `rev e` have total weight zero (S. Sherman, *Combinatorial aspects of the Ising model
for ferromagnetism. I*, 1960).

Formalized by `StatMech.Onsager.ons_lemma5`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLemma5.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-lemma5).

## Reverse of a closed walk

The reverse of a closed walk: position `k` carries the reverse of the dart at position `-k`.

Formalized by `StatMech.Onsager.ons_loopRev`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLoopReversal.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanLoopReversal.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-loop-rev).

## Rotation-orbit equivalence on cyclic sequences

The rotation-orbit equivalence relation on cyclic sequences: `v ∼ w` when `w` is obtained from
`v` by an iterated rotation.

Formalized by `StatMech.Onsager.ons_orbitSetoid`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanOrbitSum.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanOrbitSum.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-orbit-setoid).

## Chosen representative of a rotation orbit

A chosen representative of the rotation orbit of `v`.

Formalized by `StatMech.Onsager.ons_rep`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanOrbitSum.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanOrbitSum.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rep).

## Number of sequences with a given orbit representative

The number of sequences whose chosen orbit representative is `r`; for a representative `r` this
is the size of its rotation orbit, and `0` otherwise.

Formalized by `StatMech.Onsager.ons_orbitCard`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanOrbitSum.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanOrbitSum.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-orbit-card).

## Rotation of a cyclic sequence by $k$ steps

Rotation of a cyclic sequence by `k` steps: `(ons_rotate k v) j = v (j + k)`.

Formalized by `StatMech.Onsager.ons_rotate`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanReroot.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanReroot.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rotate).

## Rotation by $k$ as an equivalence of sequences

Rotation by `k` as an equivalence of `Fin n → E`, with inverse the rotation by `-k`.

Formalized by `StatMech.Onsager.ons_rotateEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanReroot.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanReroot.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rotate-equiv).

## Number of visits of a sequence to a state

The number of positions `k` with `v k = e`.

Formalized by `StatMech.Onsager.ons_visitCount`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanReroot.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanReroot.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-visit-count).

## Edge weight of a walk

The edge weight `Λ e₀ e₁ * Λ e₁ e₂ * ⋯ * Λ eₖ₋₁ eₖ` of a walk `[e₀, …, eₖ]`; walks with at most
one entry have weight `1`.

Formalized by `StatMech.Onsager.ons_edgeWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-edge-weight).

## Gluing of walk segments at a root

Concatenation of walk segments sharing their end points at `e`: each segment except the last
loses its final entry, and the result ends in `e`.

Formalized by `StatMech.Onsager.ons_glue`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-glue).

## Splitting a list at the occurrences of a root

Splitting of a list at the occurrences of `e`: each piece runs from one occurrence of `e` to the
next.

Formalized by `StatMech.Onsager.ons_firstReturnSplit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-first-return-split).

## First-return segment at a state

A first-return segment at `e`: a list `e :: interior ++ [e]` whose interior avoids `e`.

Formalized by `StatMech.Onsager.ons_isFirstReturnSegment`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-is-first-return-segment).

## First-return segments of a closed walk

The first-return segments of a closed walk at `e`, without the trailing one-element piece `[e]`.

Formalized by `StatMech.Onsager.ons_firstReturnFactors`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanSplit.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-first-return-factors).

## Rooted closed walk at a state avoiding another

A rooted closed walk at `e` avoiding `r`: a list starting and ending at `e` that never contains
`r`.

Formalized by `StatMech.Onsager.ons_validRootedList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-valid-rooted-list).

## List of first-return segments avoiding a state

A list of first-return segments at `e`, none of which contains `r`.

Formalized by `StatMech.Onsager.ons_validFactorList`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-valid-factor-list).

## Rooted closed walks as lists of first-return segments

Rooted closed walks at `e` avoiding `r` are equivalent to lists of first-return segments
avoiding `r`, by splitting and gluing.

Formalized by `StatMech.Onsager.ons_rootedFactorEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rooted-factor-equiv).

## Weight of a first-return segment avoiding a state

The edge weight of `s` if `s` is a first-return segment at `e` avoiding `r`, and `0` otherwise.

Formalized by `StatMech.Onsager.ons_firstReturnWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-first-return-weight).

## Rooted term: walk weight over its number of first-return factors

The rooted term of a walk: its edge weight divided by its number of first-return factors at `e`.

Formalized by `StatMech.Onsager.ons_rootedListTerm`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanGenericCancellation.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-rooted-list-term).

## Twisted bucket: walks through a dart, not its reverse

The total twisted Kac-Ward weight of closed walks of length `n + 1` visiting `e` but not its
reverse.

Formalized by `StatMech.Onsager.ons_phaseBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-phase-bucket-e).

## Twisted bucket: walks avoiding a dart and its reverse

The total twisted Kac-Ward weight of closed walks of length `n + 1` visiting neither `e` nor its
reverse.

Formalized by `StatMech.Onsager.ons_phaseBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-phase-bucket-n).

## Masked twisted bucket: walks through a dart, not its reverse

As `ons_phaseBucketE`, for the twisted matrix with the darts of `forbidden` masked.

Formalized by `StatMech.Onsager.ons_maskPhaseBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-mask-phase-bucket-e).

## Masked twisted bucket: walks avoiding a dart and its reverse

As `ons_phaseBucketN`, for the twisted matrix with the darts of `forbidden` masked.

Formalized by `StatMech.Onsager.ons_maskPhaseBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-mask-phase-bucket-n).

## Walk-series square root of the twisted Kac-Ward determinant

The walk-series square root of the twisted Kac-Ward determinant with boundary phases `a, b` at
activity `x`.

Formalized by `StatMech.Onsager.ons_spinWalkRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-spin-walk-root).

## Exponential of minus half the series avoiding a dart and its reverse

The exponential of minus one half of the series of closed walks avoiding `e` and its reverse.

Formalized by `StatMech.Onsager.ons_phaseAvoidRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-phase-avoid-root).

## Adding a dart and its reverse to the masked set

Add a dart and its reverse to a set of masked darts.

Formalized by `StatMech.Onsager.ons_addDartPair`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-add-dart-pair).

## Masked darts after pairwise elimination along a list

The set of masked darts after eliminating the darts of a list, pair by pair.

Formalized by `StatMech.Onsager.ons_maskAfter`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-mask-after).

## Product of first-return factors along a dart elimination

The product of the factors `1 - λ_e` along a list of darts, each first-return weight `λ_e`
computed with the previously eliminated darts masked.

Formalized by `StatMech.Onsager.ons_maskEliminationProduct`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/ShermanProductFormula.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-mask-elimination-product).

## Matrix bucket: walks through one state avoiding another

The total weight of closed walks of length `n + 1` of `M` that visit `e` but not `r`.

Formalized by `StatMech.Onsager.ons_matrixBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/StateWeightedDeletion.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/StateWeightedDeletion.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-matrix-bucket-e).

## Matrix bucket: walks avoiding two given states

The total weight of closed walks of length `n + 1` of `M` that visit neither `e` nor `r`.

Formalized by `StatMech.Onsager.ons_matrixBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/StateWeightedDeletion.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/StateWeightedDeletion.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html#ons-matrix-bucket-n).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sherman's loop cancellations and product formula](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/exact-solutions/sherman-s-loop-cancellations-and-product-formula)
