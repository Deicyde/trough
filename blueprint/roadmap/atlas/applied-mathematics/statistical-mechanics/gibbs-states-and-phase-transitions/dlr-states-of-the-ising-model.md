---
declaration: section
origin: cited
lean: StatMech.Ising.upMeasSystem, StatMech.Ising.gibbsMix, StatMech.Ising.boxFinset, StatMech.Ising.bondPairsTouch, StatMech.Ising.bondPairsInternal, StatMech.Ising.bondFinsetTouch, StatMech.Ising.bondFinsetInternal, StatMech.Ising.glue
statement: formalized
proof: formalized
---

# DLR states of the Ising model

42 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html).

## Measurable increasing events of the configuration space

The measurable increasing events of the configuration space.

Formalized by `StatMech.Ising.upMeasSystem`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsChoquet.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsChoquet.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#up-meas-system).

## Weighted mixture of two measures

The mixture `a μ⁻ + b μ⁺` of two measures.

Formalized by `StatMech.Ising.gibbsMix`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsChoquet.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsChoquet.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#gibbs-mix).

## Box $(-n, n)^d$ as a finite set of sites

The box `Λ_n = [-n, n]^d` as a finite set of sites.

Formalized by `StatMech.Ising.boxFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#box-finset).

## Ordered nearest-neighbour pairs touching the box

Ordered nearest-neighbour pairs with at least one endpoint in `Λ_n`.

Formalized by `StatMech.Ising.bondPairsTouch`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#bond-pairs-touch).

## Ordered nearest-neighbour pairs inside the box

Ordered nearest-neighbour pairs with both endpoints in `Λ_n`.

Formalized by `StatMech.Ising.bondPairsInternal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#bond-pairs-internal).

## Bonds touching the box

The bonds with at least one endpoint in `Λ_n` (used for plus and minus boundary conditions).

Formalized by `StatMech.Ising.bondFinsetTouch`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#bond-finset-touch).

## Bonds inside the box

The bonds with both endpoints in `Λ_n` (used for the free boundary condition).

Formalized by `StatMech.Ising.bondFinsetInternal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#bond-finset-internal).

## Configuration glued from inside spins and a boundary condition

The configuration equal to `τ` inside the box `Λ_n` and to the boundary condition `η`
outside.

Formalized by `StatMech.Ising.glue`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#glue).

## Box energy with a boundary condition

The box energy `-∑_{e ∈ B} σ_e - h ∑_{x ∈ Λ_n} σ_x` of the configuration `glue η τ`.

Formalized by `StatMech.Ising.fvEnergy`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fv-energy).

## Finite-volume Boltzmann weight with a boundary condition

The Boltzmann weight `exp (-β H)` of an inside configuration `τ` with boundary condition `η`.

Formalized by `StatMech.Ising.fvWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fv-weight).

## Finite-volume partition function with a boundary condition

The finite-volume partition function with boundary condition `η`.

Formalized by `StatMech.Ising.fvZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fv-z).

## Finite-volume Gibbs probability with a boundary condition

The finite-volume Gibbs probability of an inside configuration `τ` with boundary condition
`η`.

Formalized by `StatMech.Ising.fvProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fv-prob).

## Finite-volume Gibbs measure on configurations of $\mathbb{Z}^d$

The finite-volume Gibbs measure in `Λ_n` with boundary condition `η` and bond set `B`, as a
measure on configurations of `ℤ^d`.

Formalized by `StatMech.Ising.fvMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fv-measure).

## Finite-volume Gibbs measure as a probability measure

The finite-volume Gibbs measure as a `ProbabilityMeasure`.

Formalized by `StatMech.Ising.fvProbabilityMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fv-probability-measure).

## All-plus configuration

The all-plus configuration.

Formalized by `StatMech.Ising.plusField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#plus-field).

## All-minus configuration

The all-minus configuration.

Formalized by `StatMech.Ising.minusField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#minus-field).

## Plus-boundary Ising measure in a box

The Ising measure in `Λ_n` with plus boundary condition.

Formalized by `StatMech.Ising.plusMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#plus-measure).

## Minus-boundary Ising measure in a box

The Ising measure in `Λ_n` with minus boundary condition.

Formalized by `StatMech.Ising.minusMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#minus-measure).

## Free-boundary Ising measure in a box

The Ising measure in `Λ_n` with free boundary condition (internal bonds only).

Formalized by `StatMech.Ising.freeMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#free-measure).

## Infinite-volume state of a sequence of measures

`μ` is an infinite-volume state of the sequence `ρ`: some subsequence of `ρ` converges weakly to
`μ`.

Formalized by `StatMech.Ising.InfiniteVolumeState`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#infinite-volume-state).

## Existence of infinite-volume states

Every sequence of probability measures on configurations has an infinite-volume state, by
Prokhorov compactness.

Formalized by `StatMech.Ising.exists_infiniteVolumeState`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#exists-infinite-volume-state).

## Chosen subsequential weak limit of a sequence of measures

A subsequential weak limit of `ρ`, chosen by `exists_infiniteVolumeState`.

Formalized by `StatMech.Ising.limitState`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#limit-state).

## Infinite-volume plus state as a subsequential weak limit

The plus state: a weak subsequential limit of the plus-boundary box measures.
Full-sequence convergence is not claimed here: the library only provides this state as a
chosen subsequential limit (see `plusState_isInfiniteVolumeState`).

Formalized by `StatMech.Ising.plusState`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#plus-state).

## Infinite-volume minus state as a subsequential weak limit

The minus state: a weak subsequential limit of the minus-boundary box measures.

Formalized by `StatMech.Ising.minusState`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#minus-state).

## Infinite-volume free state as a subsequential weak limit

The free state: a weak subsequential limit of the free-boundary box measures.

Formalized by `StatMech.Ising.freeState`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InfiniteVolume.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#free-state).

## DLR state of the Ising model on $\mathbb{Z}^d$

The DLR condition: for every `n`, the conditional distribution of `μ` given the spins outside
the box `Λ_n` equals, for `μ`-almost every `η`, the finite-volume Gibbs measure `fvMeasure η n
(bondFinsetTouch d n) β h` with boundary condition `η`.

Formalized by `StatMech.Ising.IsDLRState`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/DLR.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/DLR.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#is-dlrstate).

## Finite intersections of a family of sets

The finite intersections of sets from `S` (together with `univ`), a π-system generating the
same σ-algebra.

Formalized by `StatMech.Ising.finInterSystem`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplex.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplex.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fin-inter-system).

## Ising specification in a box

The Ising specification in `Λ_n`: the kernel `η ↦ fvMeasure η n B β h`, measurable with
respect to the spins outside `Λ_n`.

Formalized by `StatMech.Ising.isingSpec`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplex.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplex.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#ising-spec).

## Convexity of the set of DLR states

The DLR states form a convex set: `a μ₁ + b μ₂` with `a + b = 1` is a DLR state if `μ₁`, `μ₂`
are.

Formalized by `StatMech.Ising.convex_isDLRState`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplex.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplex.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#convex-is-dlrstate).

## Stochastic domination on increasing clopen events

`μ ≼c ν`: `μ(A) ≤ ν(A)` for every increasing clopen event `A`.

Formalized by `StatMech.Ising.StochasticallyDominatedClopen`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#stochastically-dominated-clopen).

## Stochastic domination implies clopen domination, upper measure finite

ENNReal stochastic domination gives real-mass clopen domination when the upper measure is
finite.

Formalized by `StatMech.Ising.StochasticallyDominated.toClopen`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#to-clopen).

## Increasing clopen events

The increasing clopen events, a π-system generating the Borel σ-algebra.

Formalized by `StatMech.Ising.clopenUpSystem`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#clopen-up-system).

## Uniqueness of the Gibbs state

For `β, h ≥ 0`, if the plus and minus states agree then
every DLR state that is a probability measure equals the plus state.

S. Friedli and Y. Velenik, *Statistical Mechanics of Lattice Systems*, Cambridge University
Press (2017), Chapter 3.

Formalized by `StatMech.Ising.gsi_gibbs_unique_of_phases_eq`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/GibbsSimplexInfinite.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#gsi-gibbs-unique-of-phases-eq).

## Specification applied to a function

The specification applied to `f`: `η ↦ ∫ f d(fvMeasure η n B β h)`.

Formalized by `StatMech.Ising.specApply`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#spec-apply).

## Specification applied to a bounded continuous function

The specification applied to a bounded continuous function, as a bounded continuous function.

Formalized by `StatMech.Ising.specApply_bcf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#spec-apply-bcf).

## Consistency of the plus measures under the specification

The plus measures in `Λ_m` are invariant under the specification in every `Λ_n ⊆ Λ_m`.

Formalized by `StatMech.Ising.FVConsistency`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#fvconsistency).

## Ising specification as a Markov kernel

The Ising specification in `Λ_n` as a Markov kernel on the full σ-algebra.

Formalized by `StatMech.Ising.isingSpecFull`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#ising-spec-full).

## $\sigma$-algebra of events determined outside a region

The σ-algebra of events determined by the spins outside `Λ`.

Formalized by `StatMech.Ising.outsideInvariantMS`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLR.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#outside-invariant-ms).

## Overwriting a configuration on an inner box

The configuration on `Λ_m` obtained from `σ` by overwriting its spins in `Λ_n` with `τ`.

Formalized by `StatMech.Ising.ovrBox`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#ovr-box).

## Restriction of a configuration to an inner box

The restriction of a configuration on `Λ_m` to `Λ_n`.

Formalized by `StatMech.Ising.resBox`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#res-box).

## Involution swapping inner-box parts of configuration pairs

The involution of pairs exchanging the `Λ_n` parts of a configuration on `Λ_m` and a
configuration on `Λ_n`.

Formalized by `StatMech.Ising.swapPair`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#swap-pair).

## The plus state is a Gibbs (DLR) state

For all `β, h`, the plus state of the Ising model
on `ℤ^d` satisfies the DLR condition.

H.-O. Georgii, *Gibbs Measures and Phase Transitions*, de Gruyter (1988), Chapter 4.

Formalized by `StatMech.Ising.plusState_isDLR`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateDLRConsistency.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html#plus-state-is-dlr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: DLR states of the Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/dlr-states-of-the-ising-model)
