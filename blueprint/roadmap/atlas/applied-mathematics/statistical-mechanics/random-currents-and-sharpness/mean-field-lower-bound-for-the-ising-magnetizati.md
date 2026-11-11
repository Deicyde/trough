---
declaration: section
origin: cited
lean: StatMech.Sharpness.sct_cInf, StatMech.Sharpness.sct_cInfDep, StatMech.Sharpness.sctBox, StatMech.Sharpness.sctBoxGraph, StatMech.Sharpness.sctBoxInLarger, StatMech.Sharpness.sctBoxInclusionEquiv, StatMech.Sharpness.sctBoxOrigin, StatMech.Sharpness.sctTranslatedBox
statement: formalized
proof: formalized
---

# Mean-field lower bound for the Ising magnetization

82 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html).

## Minimal magnetization ratio for sites indexed by $\mathbb{N}$

The minimal ratio `min_{y ∈ sites n} M(n)/m(n, y)` for sites indexed by `ℕ`.

Formalized by `StatMech.Sharpness.sct_cInf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatio.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatio.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-c-inf).

## Minimal magnetization ratio for $n$-dependent site types

The minimal ratio `min_{y ∈ sites n} M(n)/m(n, y)` for site types depending on `n`.

Formalized by `StatMech.Sharpness.sct_cInfDep`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatio.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatio.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-c-inf-dep).

## Box $\Lambda_n$ as a type

The box `Λ_n = [-n, n]^d ⊆ ℤ^d` as a type.

Formalized by `StatMech.Sharpness.sctBox`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box).

## Nearest-neighbour graph on a box

The nearest-neighbour graph induced on `Λ_n`.

Formalized by `StatMech.Sharpness.sctBoxGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-graph).

## Membership of a larger-box site in a smaller box

A site of `Λ_m` lies in `Λ_n`.

Formalized by `StatMech.Sharpness.sctBoxInLarger`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-in-larger).

## Smaller box as a subtype of a larger box

For `n ≤ m`, `Λ_n` is equivalent to the subtype of `Λ_m` of sites lying in `Λ_n`.

Formalized by `StatMech.Sharpness.sctBoxInclusionEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-inclusion-equiv).

## Origin as a site of a box

The origin as a site of `Λ_n`.

Formalized by `StatMech.Sharpness.sctBoxOrigin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-origin).

## Translated box $\Lambda_n - y$

The translate `Λ_n - y`.

Formalized by `StatMech.Sharpness.sctTranslatedBox`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-translated-box).

## Translation onto a translated box

Translation by `-y` as an equivalence `Λ_n ≃ Λ_n - y`.

Formalized by `StatMech.Sharpness.sctTranslateEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-translate-equiv).

## Nearest-neighbour graph on a translated box

The nearest-neighbour graph induced on `Λ_n - y`.

Formalized by `StatMech.Sharpness.sctTranslatedBoxGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-translated-box-graph).

## Membership of a doubled-box site in a translated box

A site of `Λ_{2n}` lies in `Λ_n - y`.

Formalized by `StatMech.Sharpness.sctTranslatedInDouble`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-translated-in-double).

## Translated box as a subtype of the doubled box

For `y ∈ Λ_n`, `Λ_n - y` is equivalent to the subtype of `Λ_{2n}` of sites lying in it.

Formalized by `StatMech.Sharpness.sctTranslatedInDoubleEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-translated-in-double-equiv).

## Free-boundary site magnetization in a box

The free-boundary magnetization `⟨σ_x⟩_{Λ_n, β, h}` at a site `x ∈ Λ_n`.

Formalized by `StatMech.Sharpness.sctBoxMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-mag).

## Origin magnetization in a box

The origin magnetization `⟨σ_0⟩_{Λ_n, β, h}`.

Formalized by `StatMech.Sharpness.sctOriginMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-origin-mag).

## All sites of a box

All sites of `Λ_n`.

Formalized by `StatMech.Sharpness.sctBoxSites`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-sites).

## Minimal origin-to-site magnetization ratio in a box

The minimal ratio `min_{x ∈ Λ_n} ⟨σ_0⟩_{Λ_n}/⟨σ_x⟩_{Λ_n}`.

Formalized by `StatMech.Sharpness.sctLatticeC`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoxMagnetizationRatioLattice.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-lattice-c).

## Origin–site covariance in a box

The covariance `⟨σ_0σ_x⟩_{Λ_n} - ⟨σ_0⟩_{Λ_n}⟨σ_x⟩_{Λ_n}` in the box at `(β, h)`.

Formalized by `StatMech.Sharpness.sctBoxCovariance`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-box-covariance).

## Exterior neighbours of a site

The lattice neighbours of `x` outside `Λ_n`.

Formalized by `StatMech.Sharpness.sctExteriorNeighbours`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-exterior-neighbours).

## Boundary covariance error

The boundary error `∑_{x ∈ Λ_n} #(exterior neighbours of x) · Cov(σ_0, σ_x)`.

Formalized by `StatMech.Sharpness.sctBoundaryCovarianceError`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-boundary-covariance-error).

## Covariance sum over the outer layer

The sum of `Cov(σ_0, σ_x)` over the outer layer `Λ_n \ Λ_{n-1}`.

Formalized by `StatMech.Sharpness.sctOuterCovarianceSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-outer-covariance-sum).

## Field switched off on the outer layer

The site field equal to `βh` on `Λ_{n-1}` and `0` on the outer layer.

Formalized by `StatMech.Sharpness.sctInnerField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-inner-field).

## Outer-layer indicator as a field direction

The indicator of the outer layer `Λ_n \ Λ_{n-1}`, used as a field direction.

Formalized by `StatMech.Sharpness.sctOuterDirection`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-outer-direction).

## Origin magnetization with the outer-layer field switched off

The origin magnetization in `Λ_n` with the field switched off on the outer layer.

Formalized by `StatMech.Sharpness.sctInnerFieldMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BoundaryErrorLattice.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-inner-field-mag).

## Coupling restricted to the edges inside a set

The coupling `J` restricted to the edges inside `S` (zero on all other edges).

Formalized by `StatMech.Sharpness.couplingIn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#coupling-in).

## Edge lying inside a set

An edge of `G` lies inside `S`.

Formalized by `StatMech.Sharpness.isIn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#is-in).

## Extension by zero of a current inside a set

Extension by zero of a current on the edges inside `S` to all edges of `G`.

Formalized by `StatMech.Sharpness.aFull`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#a-full).

## Extension by zero of a current outside a set

Extension by zero of a current on the edges not inside `S` to all edges of `G`.

Formalized by `StatMech.Sharpness.bFull`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#b-full).

## Reassembly of a current from its inside and outside parts

Reassembly of a current from its parts inside and outside `S`.

Formalized by `StatMech.Sharpness.reEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#re-edge).

## Outside summand of a gated double-current sum

The summand of the outside double-current sum: weights of the outside part and of the second
current, gated by `P` on their sum.

Formalized by `StatMech.Sharpness.contextSummand`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#context-summand).

## Inside weight with prescribed sources

The weight of the inside part of a current, restricted to source set `A`.

Formalized by `StatMech.Sharpness.factorSummand`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#factor-summand).

## Vertices not connected to a vertex by positive current

The set of vertices not connected to `g` by edges carrying positive current.

Formalized by `StatMech.Sharpness.notConnComp`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterFactorization.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#not-conn-comp).

## Outside part of a gated double-current summand

The outside part of a double-current summand: weights of the two outside currents with sources
`B` and `D`, gated by `P`.

Formalized by `StatMech.Sharpness.claim1Context`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#claim1-context).

## Regrouping a split pair of currents

Regrouping a pair of currents split along `S` into the pair of inside parts and the pair of
outside parts.

Formalized by `StatMech.Sharpness.pairCutEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#pair-cut-equiv).

## Gated double-current sum over edge-indexed currents

The gated double-current sum `∑_{∂n₁ = A, ∂n₂ = B} w(n₁) w(n₂) 1_{P(n₁ + n₂)}` over edge-indexed
currents.

Formalized by `StatMech.Sharpness.gatedSourcePairSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#gated-source-pair-sum).

## Edges of a graph inside a set

The edges of `G` inside `S`.

Formalized by `StatMech.Sharpness.edgesIn`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#edges-in).

## Cluster lower bound for double-current sums

The cluster lower bound: for `β, J ≥ 0`, `o, x ∉ S`, `y, g ∈ S`, `y ≠ g` and `⟨σ_yσ_g⟩ > 0`, the
double-current sum with sources `{y, g} ∆ {o, x}` and `∅` on the event that the vertices not
connected to `o` form `S` is at least `⟨σ_yσ_g⟩⁻¹` times the sum with sources `{o, x}` and `∅` on
the same event and `y ↔ g`. Reference: M. Aizenman, D. J. Barsky, R. Fernández, "The phase
transition in a general class of Ising-type models is sharp", J. Stat. Phys. 47 (1987) 343–374.

Formalized by `StatMech.Sharpness.claim1_ising_of_expectation_pos`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean, line 758](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ClusterLowerBound.lean#L758). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#claim1-ising-of-expectation-pos).

## Four-source double-current sum with a connection pattern

The double-current sum with sources `{o, g} ∆ {x, y}` and `∅` restricted to `o ↔ x`, `y ↔ g` and
`o ↮ g` in the summed current.

Formalized by `StatMech.Sharpness.isingDeltaPairSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#ising-delta-pair-sum).

## Lower mass of the four-source bound

The lower mass `∑_S ⟨σ_oσ_x⟩_{J|S} · Z(∂ = ∅, C(g)ᶜ = S)` over sets `S` containing `o, x` and
not `y, g`, where `C(g)ᶜ` is the set of vertices not connected to `g`.

Formalized by `StatMech.Sharpness.isingDeltaLowerMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#ising-delta-lower-mass).

## Lower mass in the degenerate case $x = o$

The lower mass in the degenerate case `x = o`: `∑_S Z(∂ = ∅, C(g)ᶜ = S)` over `S ∋ o` with `y, g
∉ S`.

Formalized by `StatMech.Sharpness.isingDeltaSelfLowerMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#ising-delta-self-lower-mass).

## Four-source lower bound for the pattern sum

The four-source lower bound: for `β ≥ 0`, `J ≥ 0`, distinct `o, x, y, g` and `⟨σ_yσ_g⟩ > 0`, the
pattern sum `Δ(o, x, y, g)` is at least `⟨σ_yσ_g⟩⁻¹` times the lower mass. Reference: M. Aizenman,
D. J. Barsky, R. Fernández, "The phase transition in a general class of Ising-type models is sharp",
J. Stat. Phys. 47 (1987) 343–374.

Formalized by `StatMech.Sharpness.ising_delta_bound`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaBound.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#ising-delta-bound).

## Bond energy of a configuration

The bond energy `∑_{e ∈ E(G)} σ_e` of a configuration, where `σ_{xy} = σ_x σ_y`.

Formalized by `StatMech.Sharpness.sdrBondEnergy`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaRewrite.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaRewrite.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sdr-bond-energy).

## Switching gap of a current

The switching gap of a current `m` with sources `A`: the number of sub-currents (subsets of edge
copies) with sources `A` minus the number with sources `A ∆ {u, v}`; zero if the sources of `m` are
not `A`.

Formalized by `StatMech.Sharpness.HcovAssembly.hca_gap`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-gap).

## Gap-weighted current sum restricted to a predicate

The current sum `∑_m 1_{P m} · gap(m) · w(m)` of the switching gap weighted by the current
weight, restricted to currents satisfying `P`.

Formalized by `StatMech.Sharpness.HcovAssembly.hca_pairSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-pair-sum).

## Ghost source set of a bond covariance

The ghost-graph source set `{ghost} ∪ ({o} ∆ {x, y})` attached to the bond covariance `Cov(σ_o,
σ_xσ_y)`.

Formalized by `StatMech.Sharpness.HcovAssembly.hcaBondSource`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-bond-source).

## Bond term $\Delta_e$ of the magnetization derivative

The bond term `Δ_e`: the ghost-graph double-current sum with sources `hcaBondSource o e` and `∅`
in which `o` is not connected to the ghost.

Formalized by `StatMech.Sharpness.HcovAssembly.hcaBondDelta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-bond-delta).

## Ghost source set of a field covariance

The ghost-graph source set `{o} ∆ {z}` attached to the field covariance `Cov(σ_o, σ_z)`.

Formalized by `StatMech.Sharpness.HcovAssembly.hcaFieldSource`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-field-source).

## Field term $\Delta_z$ of the magnetization derivative

The field term `Δ_z`: the ghost-graph double-current sum with sources `hcaFieldSource o z` and
`∅` in which `o` is not connected to the ghost.

Formalized by `StatMech.Sharpness.HcovAssembly.hcaFieldDelta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-field-delta).

## Random-current form of the $\beta$-derivative of the magnetization

The `β`-derivative of the magnetization in random-current form: `∂_β ⟨σ_o⟩_{β,h} = Z⁻² (∑_{e ∈
E(G)} Δ_e + h ∑_z Δ_z)`, with `Z` the sourceless ghost-graph current sum. Reference: M. Aizenman, D.
J. Barsky, R. Fernández, "The phase transition in a general class of Ising-type models is sharp", J.
Stat. Phys. 47 (1987) 343–374.

Formalized by `StatMech.Sharpness.HcovAssembly.hca_deriv_magnetization_eq_currentDelta`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BetaDerivCurrent.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#hca-deriv-magnetization-eq-current-delta).

## Integrated mean-field lower bound from $m(\beta_0) = 0$

If `(m²)' ≥ (2/β)(1 - m²)` above `β₀ > 0`, `m(β₀) = 0` and `m ≥ 0`, then `m(β) ≥ √(1 - (β₀/β)²)`
for `β ≥ β₀`. See also `meanfield_lower_bound_of_initial_nonneg`, which drops the hypothesis `m(β₀)
= 0`.

Formalized by `StatMech.Sharpness.meanfield_lower_bound`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsing.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsing.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#meanfield-lower-bound).

## Random-current cut mass of a vertex set

The cut mass `Z⁻² Z(∂n₁ = ∂n₂ = ∅; {v : v ↮ g in n₁ + n₂} = S)`, with `Z` the sourceless current
sum.

Formalized by `StatMech.Sharpness.isingCutMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingMass.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingMass.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#ising-cut-mass).

## Vertex subsets as ghost-free subsets of the extended vertex set

Subsets of `V` correspond to subsets of `V ⊔ {ghost}` not containing the ghost.

Formalized by `StatMech.Sharpness.ghostFreeFinsetEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingMass.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingMass.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#ghost-free-finset-equiv).

## Subgraph of edges inside a vertex set

The subgraph of `G` with the edges inside `T`.

Formalized by `StatMech.Sharpness.localizedGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingMass.lean, line 705](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingMass.lean#L705). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#localized-graph).

## Integrated mean-field lower bound without an initial condition

If `(m²)' ≥ (2/β)(1 - m²)` above `β₀ > 0` and `m ≥ 0`, then `m(β) ≥ √(1 - (β₀/β)²)` for `β ≥
β₀`. This strengthens `meanfield_lower_bound` by dropping `m(β₀) = 0`.

Formalized by `StatMech.Sharpness.meanfield_lower_bound_of_initial_nonneg`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldLimit.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldLimit.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#meanfield-lower-bound-of-initial-nonneg).

## Infinite-volume magnetization in a field as a supremum over boxes

The infinite-volume magnetization in field `h`, the supremum over `n` of the origin
magnetizations in the boxes `Λ_n`.

Formalized by `StatMech.Sharpness.sctInfiniteFieldMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldLimit.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldLimit.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-infinite-field-mag).

## $\beta$-derivative of the origin magnetization in a box

The `β`-derivative of the origin magnetization in `Λ_n`, as the covariance of `σ_0` with `-H`.

Formalized by `StatMech.Sharpness.sctOriginMagBetaDeriv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-origin-mag-beta-deriv).

## $\beta$-derivative of the squared origin magnetization in a box

The `β`-derivative of the squared origin magnetization.

Formalized by `StatMech.Sharpness.sctOriginMagSqBetaDeriv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-origin-mag-sq-beta-deriv).

## Box mean-field function $\beta^2(1 - \langle\sigma_0\rangle^2)$

`g_n(β) = β²(1 - ⟨σ_0⟩²_{Λ_n,β,h})`.

Formalized by `StatMech.Sharpness.sctMeanfieldG`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-meanfield-g).

## $\beta$-derivative of the box mean-field function

The `β`-derivative of `g_n`.

Formalized by `StatMech.Sharpness.sctMeanfieldGDeriv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-meanfield-gderiv).

## Error term bounding the derivative of the box mean-field function

The error `2β(1 - c_n)(1 - ⟨σ_0⟩²) + 2β² c_n ε_n` bounding `g_n'` from above.

Formalized by `StatMech.Sharpness.sctMeanfieldIntegratedError`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-meanfield-integrated-error).

## Infinite-volume mean-field function $\beta^2(1 - m(\beta,h)^2)$

`β²(1 - m(β, h)²)` for the infinite-volume magnetization in field `h`.

Formalized by `StatMech.Sharpness.sctInfiniteMeanfieldG`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingIntegrated.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-infinite-meanfield-g).

## Field sequence $h_k = 1/(k + 1)$

The field sequence `h_k = 1/(k + 1)`.

Formalized by `StatMech.Sharpness.sctFieldToZero`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingState.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingState.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-field-to-zero).

## Zero-field limit of the positive-field magnetization

The zero-field limit `m⁺(β) = inf_k m(β, h_k)` of the infinite-volume magnetization in positive
field.

Formalized by `StatMech.Sharpness.sctZeroPlusMag`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingState.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingState.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-zero-plus-mag).

## Energy with general couplings and a uniform field

The energy `∑_e J_e σ_e + h ∑_x σ_x`.

Formalized by `StatMech.Sharpness.WeightedFieldGhost.weightedEnergy`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#weighted-energy).

## Boltzmann weight with general couplings and a uniform field

The Boltzmann weight `exp(β (∑_e J_e σ_e + h ∑_x σ_x))`.

Formalized by `StatMech.Sharpness.WeightedFieldGhost.weightedWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#weighted-weight).

## Partition function with general couplings and a uniform field

The partition function with couplings `J` and field `h`.

Formalized by `StatMech.Sharpness.WeightedFieldGhost.weightedZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#weighted-z).

## Gibbs expectation with general couplings and a uniform field

The Gibbs expectation with couplings `J` and field `h`.

Formalized by `StatMech.Sharpness.WeightedFieldGhost.weightedExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#weighted-expectation).

## Bond term: ghost-graph disconnection sum for a bond covariance

The bond term: the ghost-graph disconnection sum for `Cov(σ_o, σ_e)` with couplings `J`.

Formalized by `StatMech.Sharpness.WeightedFieldGhost.weightedBondDelta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#weighted-bond-delta).

## Field term: ghost-graph disconnection sum for a site covariance

The field term: the ghost-graph disconnection sum for `Cov(σ_o, σ_z)` with couplings `J`.

Formalized by `StatMech.Sharpness.WeightedFieldGhost.weightedFieldDelta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/WeightedFieldGhost.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#weighted-field-delta).

## Lattice sites underlying a set of box sites

The sites of `ℤ^d` underlying a set `T` of sites of `Λ_n`.

Formalized by `StatMech.Sharpness.sctCutSites`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-cut-sites).

## Identification of a box cut set with its lattice sites

The identification of `T` with `sctCutSites T`.

Formalized by `StatMech.Sharpness.sctCutVertexEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-cut-vertex-equiv).

## Cut mass of a box set rooted at the field ghost

The cut mass of `T` in `Λ_n` with the field ghost as root.

Formalized by `StatMech.Sharpness.sctCurrentCutMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-current-cut-mass).

## Oriented cut mass over cuts $T \ni 0, x$ with $y \notin T$

The sum over cut sets `T ∋ 0, x` with `y ∉ T` of `⟨σ_0σ_x⟩_T` times the cut mass of `T`.

Formalized by `StatMech.Sharpness.sctOrientedCutMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-oriented-cut-mass).

## Symmetrized cut mass of an edge

The symmetrized cut mass `sctOrientedCutMass x y + sctOrientedCutMass y x` of an edge.

Formalized by `StatMech.Sharpness.sctEdgeCutMass`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-edge-cut-mass).

## Boundary correlation of an edge crossing a cut

For an edge crossing the cut `T`, the correlation `⟨σ_0σ_x⟩_T` at its endpoint `x ∈ T`; zero
otherwise.

Formalized by `StatMech.Sharpness.sctEdgeBoundaryCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-edge-boundary-corr).

## Internal boundary correlation of a cut in the box

The sum of `sctEdgeBoundaryCorr` over the edges of `Λ_n`.

Formalized by `StatMech.Sharpness.sctInternalBoundaryCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-internal-boundary-corr).

## Lattice site as a box site, defaulting to the origin

A site of `ℤ^d` as a site of `Λ_n` (the origin if it lies outside).

Formalized by `StatMech.Sharpness.sctBoxize`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-boxize).

## Edge with exactly one endpoint in a cut set

An edge has exactly one endpoint in `T`.

Formalized by `StatMech.Sharpness.sctCrossesCut`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-crosses-cut).

## External boundary correlation of a cut, over edges leaving the box

The sum of `⟨σ_0σ_x⟩_T` over boundary edges `(x, y)` of `T` with `y ∉ Λ_n`.

Formalized by `StatMech.Sharpness.sctExternalBoundaryCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-external-boundary-corr).

## Boundary error of the finite-volume mean-field inequality

The boundary error `∑_{T ∋ 0}` (external boundary correlation of `T`) × (cut mass of `T`).

Formalized by `StatMech.Sharpness.sctCurrentBoundaryError`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 763](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-current-boundary-error).

## Finite-volume mean-field inequality for the Ising model

The finite-volume mean-field inequality: for `β, h > 0` and `inf_S φ_β(S) ≥ φ₀`, `∂_β
⟨σ_0⟩²_{Λ_n} ≥ 2 c_n ((φ₀/β)(1 - ⟨σ_0⟩²) - ε_n)`. Reference: H. Duminil-Copin, V. Tassion, "A new
proof of the sharpness of the phase transition for Bernoulli percolation and the Ising model", Comm.
Math. Phys. 343 (2016) 725–745.

Formalized by `StatMech.Sharpness.sct_finite_meanfield_inequality`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 859](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L859). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-finite-meanfield-inequality).

## Pairs of a box site and an outside lattice neighbour

Pairs `(x, y)` with `x ∈ Λ_n` and `y` a lattice neighbour of `x` outside `Λ_n`.

Formalized by `StatMech.Sharpness.sctExternalBoxPairs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean, line 935](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingFinite.lean#L935). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-external-box-pairs).

## Mean-field lower bound for the spontaneous magnetization

The mean-field lower bound for the spontaneous magnetization: if `β̃_c > 0` and its defining set
is bounded, then `m*(β) ≥ √(1 - (β̃_c/β)²)` for `β ≥ β̃_c`. Reference: H. Duminil-Copin, V. Tassion,
"A new proof of the sharpness of the phase transition for Bernoulli percolation and the Ising
model", Comm. Math. Phys. 343 (2016) 725–745.

Formalized by `StatMech.Sharpness.sct_magnetization_meanfield_lower_bound_integrated`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingPlusBridge.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldIsingPlusBridge.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html#sct-magnetization-meanfield-lower-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mean-field lower bound for the Ising magnetization](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/mean-field-lower-bound-for-the-ising-magnetizati)
