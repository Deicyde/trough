---
declaration: section
origin: cited
lean: MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.IsingSite, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.spinValue, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.rightNeighbour, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.upNeighbour, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.isingEnergy, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.isingPartitionFunction, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.finiteIsingFreeEnergy, MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.finiteIsingFreeEnergySeq
statement: formalized
---

# Onsager's 2D Ising phase transition

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html).

## Sites of the periodic square lattice

For a positive integer $L$, the sites of the
periodic $L \times L$ square lattice are the pairs $(i, j)$ with
$i, j \in \mathbb{Z}/L\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.IsingSite`, an abbreviation declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#ising-site).

## Numerical value of a spin

A spin, recorded as a Boolean, has the real value $1$ if it is
true and $-1$ if it is false.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.spinValue`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#spin-value).

## Right neighbour

For a positive integer $L$, the right neighbour of a site $(i, j)$ of
the periodic $L \times L$ square lattice is $(i + 1, j)$, with addition in
$\mathbb{Z}/L\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.rightNeighbour`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#right-neighbour).

## Upward neighbour

For a positive integer $L$, the upward neighbour of a site $(i, j)$ of
the periodic $L \times L$ square lattice is $(i, j + 1)$, with addition in
$\mathbb{Z}/L\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.upNeighbour`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#up-neighbour).

## Energy of an Ising configuration

For a positive integer $L$, let $\sigma$ be a spin
configuration on the periodic $L \times L$ square lattice, assigning to each site $p$ a spin
$\sigma_p \in \{1, -1\}$. Its energy in the zero-field ferromagnetic Ising model with unit
coupling is

$$H_L(\sigma) = -\sum_p \left(\sigma_p \sigma_{p + e_1} + \sigma_p \sigma_{p + e_2}\right),$$

where $p$ runs over all sites, and $p + e_1$ and $p + e_2$ are obtained from $p$ by adding $1$
modulo $L$ to its first and to its second coordinate respectively.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.isingEnergy`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#ising-energy).

## Ising partition function

For a positive integer $L$ and real $\beta$, the partition
function of the Ising model on the periodic $L \times L$ square lattice at inverse temperature
$\beta$ is $Z_L(\beta) = \sum_\sigma e^{-\beta H_L(\sigma)}$, where $\sigma$ runs over all spin
configurations on the lattice and $H_L(\sigma)$ is the Ising energy of $\sigma$.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.isingPartitionFunction`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#ising-partition-function).

## Finite-volume Ising free energy density

For a positive integer $L$ and real $\beta$, the
free energy density of the Ising model on the periodic $L \times L$ square lattice is
$\log Z_L(\beta) / L^2$, where $Z_L(\beta)$ is the partition function at inverse temperature
$\beta$.

No factor $-1/\beta$ is included.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.finiteIsingFreeEnergy`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#finite-ising-free-energy).

## Ising free energy density along side lengths $n + 1$

For a natural number $n$ and real
$\beta$, this is the finite-volume free energy density of the Ising model on the periodic
$(n + 1) \times (n + 1)$ square lattice at inverse temperature $\beta$, namely
$\log Z_{n+1}(\beta) / (n + 1)^2$, where $Z_{n+1}(\beta)$ is the partition function of that
lattice at inverse temperature $\beta$.

Formalized by `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.finiteIsingFreeEnergySeq`, a definition declared in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#finite-ising-free-energy-seq).

## Onsager's phase transition for the two-dimensional Ising model

For a positive integer $L$
and real $\beta$, let $Z_L(\beta)$ be the partition function of the zero-field ferromagnetic Ising
model on the periodic $L \times L$ square lattice at inverse temperature $\beta$. There exist a
function $F : \mathbb{R} \to \mathbb{R}$ and a real number $\beta_c > 0$ such that, for every real
$\beta$, $\log Z_{n+1}(\beta) / (n+1)^2$ converges to $F(\beta)$ as $n \to \infty$, and $F$ is not
real analytic at $\beta_c$.

## Sources

- L. Onsager, *Crystal statistics I*, Phys. Rev. 65 (1944). Knill, §158. Problem `ising_2d_phase_transition` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.IsingPhaseTransitionWanted.Analysis.IsingPhaseTransition.ising_2d_phase_transition` is written with `theorem_wanted` in [WantedExt/Analysis/IsingPhaseTransitionWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/IsingPhaseTransitionWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html#ising-2d-phase-transition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Onsager's 2D Ising phase transition](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/onsager-s-2d-ising-phase-transition)
