---
declaration: section
origin: cited
lean: StatMech.Ising.negHam, StatMech.Ising.cov2, StatMech.Ising.onePt, StatMech.Ising.cov3sym, StatMech.Ising.ghsBoundSym, StatMech.Ising.bondEnergySusceptibility, StatMech.Ising.susceptibility, StatMech.Ising.GHSThreePointSym
statement: formalized
proof: formalized
---

# The Aizenman–Barsky–Fernández differential inequality, finite volume

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html).

## A. Derivatives of the partition function

## Negative Hamiltonian of the Ising model

The negative Hamiltonian `∑_{xy ∈ E} σ_xσ_y + h ∑_x σ_x`.

Formalized by `StatMech.Ising.negHam`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#neg-ham).

## Two-point spin covariance

The spin covariance `Cov(σ_x, σ_y) = ⟨σ_xσ_y⟩ - ⟨σ_x⟩⟨σ_y⟩`.

Formalized by `StatMech.Ising.cov2`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#cov2).

## Ising one-point function

The one-point function `⟨σ_x⟩`.

Formalized by `StatMech.Ising.onePt`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#one-pt).

## Covariance of a spin with a bond variable

The covariance `⟨σ_o σ_x σ_y⟩ - ⟨σ_o⟩⟨σ_x σ_y⟩` of `σ_o` with the bond variable of `e = {x,
y}`.

Formalized by `StatMech.Ising.cov3sym`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#cov3sym).

## GHS bound for a bond

The GHS bound `Cov(σ_o, σ_x)⟨σ_y⟩ + Cov(σ_o, σ_y)⟨σ_x⟩` for the bond `e = {x, y}`.

Formalized by `StatMech.Ising.ghsBoundSym`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#ghs-bound-sym).

## Bond-energy susceptibility

The bond-energy susceptibility `∑_{e ∈ E} Cov(σ_o, σ_e)`.

Formalized by `StatMech.Ising.bondEnergySusceptibility`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#bond-energy-susceptibility).

## Ising susceptibility at a site

The susceptibility `χ(o) = ∑_x Cov(σ_o, σ_x)`.

Formalized by `StatMech.Ising.susceptibility`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#susceptibility).

## GHS three-point inequality at a site for every edge

The GHS inequality at `o` for every edge: `cov3sym ≤ ghsBoundSym`, equivalently `u₃(o, x, y)
≤ 0` for every edge `{x, y}`.

Formalized by `StatMech.Ising.GHSThreePointSym`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#ghsthree-point-sym).

## Conditional finite-volume Aizenman–Barsky–Fernández inequality

A conditional finite-volume form of the Aizenman–Barsky–Fernández inequality: if the GHS
bound holds at `o` and the GHS bounds sum to `J ⟨σ_o⟩ χ(o)`, then the bond-energy
susceptibility is at most `J ⟨σ_o⟩ χ(o)`.

Formalized by `StatMech.Ising.aizenman_barsky_inequality`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/AizenmanBarsky.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html#aizenman-barsky-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Aizenman–Barsky–Fernández differential inequality, finite volume](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/the-aizenman-barsky-fern-ndez-differential-inequ)
