---
declaration: section
origin: cited
lean: StatMech.Sharpness.bondParam, StatMech.Sharpness.phiBeta, StatMech.Sharpness.tildeBetaCPercoSet, StatMech.Sharpness.tildeBetaCPerco, StatMech.Sharpness.graphS, StatMech.Sharpness.freeCorr, StatMech.Sharpness.corrOriginInner, StatMech.Sharpness.phiIsing
statement: formalized
proof: formalized
---

# The Duminil-Copin–Tassion point for the Ising model

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html).

## A. The percolation version

## Bond parameter $1 - e^{-\beta}$

The bond parameter `1 - exp(-β)` as an element of `ℝ≥0`.

Formalized by `StatMech.Sharpness.bondParam`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#bond-param).

## Percolation quantity $\varphi_p(S)$ at $p = 1 - e^{-\beta}$

The percolation quantity `φ_p(S)` at `p = 1 - exp(-β)`.

Formalized by `StatMech.Sharpness.phiBeta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#phi-beta).

## Inverse temperatures with a percolation witness $\varphi(S) < 1$

Inverse temperatures `β ≥ 0` with a finite `S ∋ 0` such that `φ_{1-e^{-β}}(S) < 1`.

Formalized by `StatMech.Sharpness.tildeBetaCPercoSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#tilde-beta-cperco-set).

## Percolation auxiliary critical point on the $\beta$ scale

The percolation auxiliary critical point on the `β` scale, the supremum of `tildeBetaCPercoSet`.

Formalized by `StatMech.Sharpness.tildeBetaCPerco`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#tilde-beta-cperco).

## Induced subgraph of $\mathbb{Z}^d$ on a finite set

The subgraph of `ℤ^d` induced by a finite set `S`, on the vertex type `S`.

Formalized by `StatMech.Sharpness.graphS`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#graph-s).

## Free-boundary zero-field two-point function in a finite set

The free-boundary zero-field two-point function `⟨σ_aσ_b⟩_S` in the induced graph on `S` (equal
to `1` when `a = b`).

Formalized by `StatMech.Sharpness.freeCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#free-corr).

## Free origin correlation in a set, extended by zero

The function `x ↦ ⟨σ_0σ_x⟩_S`, extended by `0` outside `S` (and identically `0` if `0 ∉ S`).

Formalized by `StatMech.Sharpness.corrOriginInner`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#corr-origin-inner).

## Duminil-Copin–Tassion quantity $\varphi_\beta(S)$ for the Ising model

The Duminil-Copin–Tassion quantity `φ_β(S) = tanh β ∑_{(x,y) ∈ ∂S} ⟨σ_0σ_x⟩_S`.

Formalized by `StatMech.Sharpness.phiIsing`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#phi-ising).

## Inverse temperatures with an Ising witness $\varphi_\beta(S) < 1$

Inverse temperatures `β ≥ 0` with a finite `S ∋ 0` such that `φ_β(S) < 1`.

Formalized by `StatMech.Sharpness.tildeBetaCIsingSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#tilde-beta-cising-set).

## Auxiliary critical point $\tilde\beta_c$ of the Ising model

The auxiliary critical point `β̃_c(d) = sup {β ≥ 0 | ∃ S ∋ 0, φ_β(S) < 1}`.

Formalized by `StatMech.Sharpness.tildeBetaCIsing`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TildeBc.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html#tilde-beta-cising).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Duminil-Copin–Tassion point for the Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-duminil-copin-tassion-point-for-the-ising-mo)
