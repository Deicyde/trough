---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_V, StatMech.Onsager.ons_dirStep, StatMech.Onsager.ons_Dart, StatMech.Onsager.ons_turnW, StatMech.Onsager.ons_KWmat, StatMech.Onsager.ons_shiftDart, StatMech.Onsager.trace_pow_endo, StatMech.Onsager.ons_detWalkRoot
statement: formalized
proof: formalized
---

# Kac–Ward matrices

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html).

## Sites of the square-lattice torus

The sites `ℤ_L × ℤ_L` of the `L × L` square-lattice torus.

Formalized by `StatMech.Onsager.ons_V`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-v).

## Neighbouring site in a given direction on the torus

The neighbor of a site in direction `μ`: `0` east, `1` north, `2` west, `3` south.

Formalized by `StatMech.Onsager.ons_dirStep`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-dir-step).

## Darts of the square-lattice torus

Darts (directed edges) of the torus: a starting site and a direction.

Formalized by `StatMech.Onsager.ons_Dart`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-dart).

## Turn weight between two lattice directions

The turn weight from direction `μ` to direction `ν`: `1` straight, `ω` for a left turn, `0` for
a U-turn, `ω⁻¹` for a right turn.

Formalized by `StatMech.Onsager.ons_turnW`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-turn-w).

## Kac–Ward matrix of the square-lattice torus

The Kac-Ward matrix: the entry from `d₁` to `d₂` is `x * ons_turnW ω d₁.2 d₂.2` when `d₂` starts
at the head of `d₁`, and `0` otherwise.

Formalized by `StatMech.Onsager.ons_KWmat`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwmat).

## Translation of a dart by a lattice vector

Translation of a dart by a lattice vector `t`.

Formalized by `StatMech.Onsager.ons_shiftDart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/KacWardMatrix.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-shift-dart).

## Trace of a power as a power sum of characteristic roots

The trace of `φ ^ k` is the sum of the `k`-th powers of the roots of the characteristic
polynomial of `φ`. See also `Matrix.trace_eq_sum_roots_charpoly`, the case `k = 1`.

Formalized by `StatMech.Onsager.trace_pow_endo`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DetLoopExpansion.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/DetLoopExpansion.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#trace-pow-endo).

## Walk-series square root of det(1 − Λ)

The walk-series square root of `det (1 - Λ)`: the exponential of minus one half of
`∑ₙ (∑ over closed walks of length n + 1 of their weight) / (n + 1)`.

Formalized by `StatMech.Onsager.ons_detWalkRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DetWalkExp.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/DetWalkExp.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-det-walk-root).

## Matrix with forbidden rows and columns set to zero

The matrix `Λ` with every row and column indexed by a state of `forbidden` set to zero.

Formalized by `StatMech.Onsager.ons_maskMatrix`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DetWalkExp.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/DetWalkExp.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-mask-matrix).

## Matrix with selected columns scaled

The matrix `Λ` with every column indexed by an element of `S` multiplied by `t`.

Formalized by `StatMech.Onsager.ons_scaleColumns`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/FirstReturnScale.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/FirstReturnScale.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-scale-columns).

## Turning phase $\omega = e^{i\pi/4}$

The turning phase `ω = e^{iπ/4}`, so a turn by `±π/2` contributes `ω^{±1}` and `ω² = i`.

Formalized by `StatMech.Onsager.ons_turnRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWDetLimit.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWDetLimit.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-turn-root).

## Primitive L-th root of unity $e^{2\pi i/L}$

The primitive `L`-th root of unity `e^{2πi/L}`.

Formalized by `StatMech.Onsager.ons_spaceRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWDetLimit.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWDetLimit.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-space-root).

## Sector determinant with boundary phases

The sector determinant: the product of `ons_symbolDispersion β` over the momenta
`(2π(i + a/2) / L, 2π(j + b/2) / L)`, `i, j < L`, for boundary phases `a, b ∈ {0, 1}`.

Formalized by `StatMech.Onsager.ons_spinDet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWDetLimit.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWDetLimit.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-spin-det).

## Edge weight function with one weight scaled by t

The edge weight function with the weight of `edge` multiplied by `t`.

Formalized by `StatMech.Onsager.ons_scaleEdgeWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWEdgeScale.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWEdgeScale.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-scale-edge-weight).

## 4 × 4 block of the Kac-Ward matrix between a site and the origin

The `4 × 4` block of the Kac-Ward matrix between the darts at site `g` and the darts at the
origin.

Formalized by `StatMech.Onsager.ons_KWblock`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWFourier.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWFourier.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwblock).

## Convergence radius of the twisted Kac-Ward walk expansion

The radius `1 / (number of darts) = 1 / (4L²)` below which the walk expansion of the twisted
Kac-Ward determinant converges.

Formalized by `StatMech.Onsager.ons_KWconvergenceRadius`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpectral.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpectral.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwconvergence-radius).

## Boundary phase of a step in a direction

The phase of a step in direction `μ`: `u, v, u⁻¹, v⁻¹` for east, north, west, south.

Formalized by `StatMech.Onsager.ons_dirPhase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-dir-phase).

## Horizontal displacement of a step in a direction

The horizontal displacement `1, 0, -1, 0` of a step in direction `μ`.

Formalized by `StatMech.Onsager.ons_dirExponentX`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-dir-exponent-x).

## Vertical displacement of a step in a direction

The vertical displacement `0, 1, 0, -1` of a step in direction `μ`.

Formalized by `StatMech.Onsager.ons_dirExponentY`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-dir-exponent-y).

## Twisted Kac-Ward matrix with direction phases

The Kac-Ward matrix with each step multiplied by its direction phase `ons_dirPhase u v`.

Formalized by `StatMech.Onsager.ons_KWmatPhase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwmat-phase).

## Block of the twisted Kac-Ward matrix between a site and the origin

The `4 × 4` block of the twisted Kac-Ward matrix between the darts at `g` and at the origin.

Formalized by `StatMech.Onsager.ons_KWblockPhase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwblock-phase).

## Boundary phase $e^{i\pi a/L}$

The boundary phase `e^{iπa/L}`, whose `L`-th power is `(-1)^a`.

Formalized by `StatMech.Onsager.ons_spinPhase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWSpinFourier.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-spin-phase).

## Edge-weighted Kac-Ward matrix

The edge-weighted Kac-Ward matrix: the entry from `d₁` to `d₂` is the weight of the torus edge
of `d₁` times the turn weight, when `d₂` starts at the head of `d₁`.

Formalized by `StatMech.Onsager.ons_KWmatWeighted`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeighted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeighted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwmat-weighted).

## Edge-weighted Kac-Ward matrix with direction phases

The edge-weighted Kac-Ward matrix with each step multiplied by its direction phase.

Formalized by `StatMech.Onsager.ons_KWmatWeightedPhase`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeighted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeighted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwmat-weighted-phase).

## Edge-weighted twisted bucket: walks through a dart, not its reverse

The total edge-weighted twisted Kac-Ward weight of closed walks of length `n + 1` visiting `e`
but not its reverse.

Formalized by `StatMech.Onsager.ons_weightedPhaseBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-weighted-phase-bucket-e).

## Edge-weighted twisted bucket: walks avoiding a dart and its reverse

The total edge-weighted twisted Kac-Ward weight of closed walks of length `n + 1` visiting
neither `e` nor its reverse.

Formalized by `StatMech.Onsager.ons_weightedPhaseBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-weighted-phase-bucket-n).

## Masked edge-weighted bucket: walks through a dart, not its reverse

As `ons_weightedPhaseBucketE`, with the darts of `forbidden` masked.

Formalized by `StatMech.Onsager.ons_maskWeightedPhaseBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-mask-weighted-phase-bucket-e).

## Masked edge-weighted bucket: walks avoiding a dart and its reverse

As `ons_weightedPhaseBucketN`, with the darts of `forbidden` masked.

Formalized by `StatMech.Onsager.ons_maskWeightedPhaseBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/KWWeightedBuckets.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-mask-weighted-phase-bucket-n).

## Fourier symbol of one minus the Kac-Ward matrix

The `4 × 4` Fourier symbol of `1 - ons_KWmat` at `zⱼ = e^{i kⱼ}`, rows and columns indexed by
the directions east, north, west, south.

Formalized by `StatMech.Onsager.ons_KWsymbolMat`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SymbolDet.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/SymbolDet.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html#ons-kwsymbol-mat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kac–Ward matrices](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/exact-solutions/kac-ward-matrices)
