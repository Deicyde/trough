---
declaration: section
origin: cited
lean: StatMech.Ising.pst_plusShiftedFinite, StatMech.Ising.pst_minusShiftedFinite, StatMech.Ising.pst_PlusIntegralShiftDecay, StatMech.Ising.pst_MinusIntegralShiftDecay, StatMech.Ising.pstc_decayFun, StatMech.Ising.pstc_coordCM, StatMech.Ising.pstc_coordBcf, StatMech.Ising.pstc_cylinderAlg
statement: formalized
proof: formalized
---

# Translation invariance and ergodicity of the plus state

47 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html).

## Shifted plus-boundary box measure

The plus-boundary box measure on `Λ_n` pushed forward by the shift `g`.

Formalized by `StatMech.Ising.pst_plusShiftedFinite`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pst-plus-shifted-finite).

## Shifted minus-boundary box measure

The minus-boundary box measure on `Λ_n` pushed forward by the shift `g`.

Formalized by `StatMech.Ising.pst_minusShiftedFinite`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pst-minus-shifted-finite).

## Decay of shifted integrals for plus box measures

Along `φ`, integrals of bounded continuous functions against the plus box measures and their
shifts by `g` become equal.

Formalized by `StatMech.Ising.pst_PlusIntegralShiftDecay`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pst-plus-integral-shift-decay).

## Decay of shifted integrals for minus box measures

Along `φ`, integrals of bounded continuous functions against the minus box measures and their
shifts by `g` become equal.

Formalized by `StatMech.Ising.pst_MinusIntegralShiftDecay`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTI.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pst-minus-integral-shift-decay).

## Difference between an integral and its shifted version

The difference `∫ f dμ_n - ∫ f ∘ shift_g dμ_n`.

Formalized by `StatMech.Ising.pstc_decayFun`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-decay-fun).

## Plus-spin indicator at a site as a continuous function

The coordinate `ω ↦ 1_{ω_x = +}` as a continuous function.

Formalized by `StatMech.Ising.pstc_coordCM`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-coord-cm).

## Plus-spin indicator at a site as a bounded continuous function

The coordinate `ω ↦ 1_{ω_x = +}` as a bounded continuous function.

Formalized by `StatMech.Ising.pstc_coordBcf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-coord-bcf).

## Subalgebra of cylinder functions

The subalgebra generated by the spin coordinates (cylinder functions).

Formalized by `StatMech.Ising.pstc_cylinderAlg`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-cylinder-alg).

## Cylinder functions as bounded continuous functions

The cylinder functions as bounded continuous functions.

Formalized by `StatMech.Ising.pstc_cylinderBcfSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-cylinder-bcf-set).

## Decay of shifted cylinder integrals for plus box measures

Shifted integrals of cylinder functions against the plus box measures decay along `φ`.

Formalized by `StatMech.Ising.pstc_PlusCylinderDecay`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-plus-cylinder-decay).

## Decay of shifted cylinder integrals for minus box measures

Shifted integrals of cylinder functions against the minus box measures decay along `φ`.

Formalized by `StatMech.Ising.pstc_MinusCylinderDecay`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTICylinder.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#pstc-minus-cylinder-decay).

## Boundary bond fraction of a box

The number of bonds touching but not inside `Λ_n`, divided by the number of sites of `Λ_n`.

Formalized by `StatMech.Ising.ibs_boundaryFraction`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/IsingBoxSqueeze.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/IsingBoxSqueeze.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#ibs-boundary-fraction).

## Boundary influence bound for the plus box measures

Shift differences of cylinder-function integrals against the plus box measures are
`O(boundary fraction)`.

Formalized by `StatMech.Ising.ibs_PlusBoundaryInfluence`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/IsingBoxSqueeze.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/IsingBoxSqueeze.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#ibs-plus-boundary-influence).

## Boundary influence bound for the minus box measures

Shift differences of cylinder-function integrals against the minus box measures are
`O(boundary fraction)`.

Formalized by `StatMech.Ising.ibs_MinusBoundaryInfluence`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/IsingBoxSqueeze.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/IsingBoxSqueeze.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#ibs-minus-boundary-influence).

## All-plus monomial as a continuous function

The monomial `ω ↦ ∏_{x ∈ T} 1_{ω_x = +}` as a continuous function.

Formalized by `StatMech.Ising.iti_monomialCM`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iti-monomial-cm).

## All-plus monomial as a bounded continuous function

The monomial `ω ↦ ∏_{x ∈ T} 1_{ω_x = +}` as a bounded continuous function.

Formalized by `StatMech.Ising.iti_monomialBcf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iti-monomial-bcf).

## Shift homogeneity of all-plus events in the plus state

The plus state gives the all-plus events on `T` and on `g⁻¹ T` the same probability, for
every finite `T`.

Formalized by `StatMech.Ising.iti_PlusMultiHomogeneous`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iti-plus-multi-homogeneous).

## Continuous functions with decaying shifted integrals

The continuous functions whose shifted integrals against the plus box measures decay along
`φ`.

Formalized by `StatMech.Ising.iti_decaySet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTIOfHomogeneous.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iti-decay-set).

## Asymptotic shift homogeneity of all-plus events in plus boxes

Along `φ`, the plus box measures give the all-plus events on `T` and on `g⁻¹ T`
asymptotically equal probabilities.

Formalized by `StatMech.Ising.itb_PlusMultiBoundaryDecay`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTranslatedBoxes.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTranslatedBoxes.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#itb-plus-multi-boundary-decay).

## Off-centre domination of all-plus events

For every finite `T` there is `c` such that plus measures on boxes of sizes `m + c` and `m`
compare the all-plus events on `T` and `g⁻¹ T` in both directions.

Formalized by `StatMech.Ising.itb_OffCentreDomination`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateTranslatedBoxes.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateTranslatedBoxes.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#itb-off-centre-domination).

## Shift vector $R e_{i_0}$

The vector `R e_{i₀}` of `ℤ^d`.

Formalized by `StatMech.Ising.icb_shiftVec`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateUpperDecay.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateUpperDecay.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#icb-shift-vec).

## Unit vector of $\mathbb{Z}^d$

The unit vector `e_i` of `ℤ^d`.

Formalized by `StatMech.Ising.gvUnit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-unit).

## Site with its nearest neighbours

The site `x` and its nearest neighbours.

Formalized by `StatMech.Ising.gvBall`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-ball).

## Set with its nearest neighbours

The sites of `S` together with their nearest neighbours.

Formalized by `StatMech.Ising.gvCand`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-cand).

## Bonds touching a set

The bonds with at least one endpoint in `S`.

Formalized by `StatMech.Ising.gvBondTouch`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-bond-touch).

## Configuration glued from a set and a boundary condition

The configuration equal to `τ` on `S` and to `η` off `S`.

Formalized by `StatMech.Ising.gvGlue`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-glue).

## Energy on a set with a boundary condition

The energy `-∑_{e touching S} σ_e - h ∑_{x ∈ S} σ_x` of `gvGlue η S τ`.

Formalized by `StatMech.Ising.gvEnergy`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-energy).

## Boltzmann weight on a set with a boundary condition

The Boltzmann weight of the configuration `τ` on `S` with boundary condition `η`.

Formalized by `StatMech.Ising.gvWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-weight).

## Partition function on a set with a boundary condition

The partition function on `S` with boundary condition `η`.

Formalized by `StatMech.Ising.gvZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-z).

## Gibbs probability on a set with a boundary condition

The Gibbs probability of `τ` on `S` with boundary condition `η`.

Formalized by `StatMech.Ising.gvProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-prob).

## Finite-volume Gibbs measure on a finite set

The finite-volume Gibbs measure on the finite set `S` with boundary condition `η`.

Formalized by `StatMech.Ising.gvMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-measure).

## Finite-volume Gibbs measure with plus boundary condition

The finite-volume Gibbs measure on `S` with plus boundary condition.

Formalized by `StatMech.Ising.gvPlusMeasure`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-plus-measure).

## Overwriting a configuration on an inner set

The configuration on `Sout` obtained by overwriting its spins in `Sin` with `τ`.

Formalized by `StatMech.Ising.gvOvr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-ovr).

## Restriction of a configuration to an inner set

The restriction of a configuration on `Sout` to `Sin`.

Formalized by `StatMech.Ising.gvRes`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-res).

## Involution swapping inner-set parts of configuration pairs

The involution exchanging the `Sin` parts of a configuration on `Sout` and a configuration on
`Sin`.

Formalized by `StatMech.Ising.gvSwapPair`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#gv-swap-pair).

## Box sites as a set and as a finite set

The sites of the box `Λ_n` as a set and as a finset.

Formalized by `StatMech.Ising.iptp_boxEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iptp-box-equiv).

## Translation as an equivalence onto a translate

Translation by `g` as an equivalence between `S` and its translate.

Formalized by `StatMech.Ising.iptp_transInteriorEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 737](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L737). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iptp-trans-interior-equiv).

## Translation invariance of the plus state

For `β, h ≥ 0`, the plus state of the Ising
model on `ℤ^d` is invariant under all lattice translations.

S. Friedli and Y. Velenik, *Statistical Mechanics of Lattice Systems*, Cambridge University
Press (2017), Chapter 3.

Formalized by `StatMech.Ising.iptp_plusState_isTranslationInvariant`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 967](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L967). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iptp-plus-state-is-translation-invariant).

## Extremality of the plus state

For `d ≥ 1` and `β, h ≥ 0`, the plus state is an extreme
point of the translation-invariant probability measures.

H.-O. Georgii, *Gibbs Measures and Phase Transitions*, de Gruyter (1988), Chapter 14.

Formalized by `StatMech.Ising.ising_plus_extreme`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 977](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L977). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#ising-plus-extreme).

## Ergodicity of the plus state

For `d ≥ 1` and `β, h ≥ 0`, the plus state is ergodic under
lattice translations.

H.-O. Georgii, *Gibbs Measures and Phase Transitions*, de Gruyter (1988), Chapter 14.

Formalized by `StatMech.Ising.iptp_plusState_isErgodic`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean, line 986](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateErgodic.lean#L986). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#iptp-plus-state-is-ergodic).

## Extreme point of the DLR states

`μ` is an extreme point of the DLR states: a proper convex decomposition into DLR probability
measures is trivial.

Formalized by `StatMech.Ising.IsDLRExtremePoint`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateZeroOne.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateZeroOne.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#is-dlrextreme-point).

## All-plus Dirac mass gives the all-plus event probability one

A nonvacuity check: the Dirac mass at the all-plus configuration gives the all-plus event
probability one.

Formalized by `StatMech.Ising.atip2_ergodic_zeroOne_nonvacuous`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PlusStateZeroOne.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PlusStateZeroOne.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#atip2-ergodic-zero-one-nonvacuous).

## Tail event for lattice spin configurations

A tail event: measurable with respect to the spins outside `Λ_n`, for every `n`.

Formalized by `StatMech.Ising.IsTailEvent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TailEventsErgodic.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TailEventsErgodic.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#is-tail-event).

## σ-algebra generated by the spins in a finite set

The σ-algebra generated by the spins in the finite set `F`.

Formalized by `StatMech.Ising.aetc_finSig`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#aetc-fin-sig).

## Cylinder events of the Ising configuration space

The cylinder events: events depending on the spins in some box.

Formalized by `StatMech.Ising.aetc_Cring`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#aetc-cring).

## Approximation in measure by events measurable outside every box

For every box `Λ_k` and `ε > 0`, `s` is `ε`-approximated in `μ`-measure by an event
measurable outside `Λ_k`.

Formalized by `StatMech.Ising.AeApproxFarOut`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#ae-approx-far-out).

## Nonvacuity of the a.s.-tail theorem via the all-plus Dirac mass

The hypotheses of `aetc_haeTail` are satisfiable: the Dirac mass at the all-plus
configuration.

Formalized by `StatMech.Ising.aetc_haeTail_nonvacuous`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/InvariantEventsTail.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html#aetc-hae-tail-nonvacuous).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Translation invariance and ergodicity of the plus state](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/translation-invariance-and-ergodicity-of-the-plu)
