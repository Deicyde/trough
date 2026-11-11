---
declaration: section
origin: cited
lean: StatMech.Ising.spinB, StatMech.Ising.monomial, StatMech.Ising.sum_monomial_nonneg, StatMech.Ising.IsSpinMonomial, StatMech.Ising.gks_kernel, StatMech.Ising.spinProd, StatMech.Ising.isingExpectation, StatMech.Ising.isingWeight_factor
statement: formalized
proof: formalized
---

# Griffiths inequalities

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html).

## Spin value of a Boolean

The spin value `±1` of a Boolean: `1` for `true`, `-1` for `false`. See also
`CondensedMatter.IsingModel.spin` and `StatMech.Ising.spinB_eq_isingModelSpin`.

Formalized by `StatMech.Ising.spinB`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#spin-b).

## Spin monomial with given exponents

The spin monomial `∏_x σ_x^{m_x}` with exponents `m : V → ℕ`.

Formalized by `StatMech.Ising.monomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#monomial).

## Configuration sum of a spin monomial is nonnegative

The sum of a spin monomial over all configurations is nonnegative.

Formalized by `StatMech.Ising.sum_monomial_nonneg`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#sum-monomial-nonneg).

## Being a spin monomial

`f` is a spin monomial `∏_x σ_x^{m_x}` for some exponents `m`.

Formalized by `StatMech.Ising.IsSpinMonomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#is-spin-monomial).

## Nonnegativity of the GKS positivity kernel

The positivity kernel of the GKS inequalities: for nonnegative `c_i, d_i` and spin monomials
`fac i`, `obs`, the configuration sum of `obs · ∏_i (c_i + d_i · fac_i)` is nonnegative.

Formalized by `StatMech.Ising.gks_kernel`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#gks-kernel).

## Spin product over a vertex set

The spin product `σ_A = ∏_{x ∈ A} σ_x`.

Formalized by `StatMech.Ising.spinProd`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#spin-prod).

## Finite-volume Ising expectation

The finite-volume Ising expectation `⟨f⟩ = ∑_s P(s) f(s)` of an observable `f`.

Formalized by `StatMech.Ising.isingExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#ising-expectation).

## Boltzmann weight as a product of cosh-plus-sinh factors

The Boltzmann weight factorizes as a product over edges and vertices of `cosh + sinh · σ`
terms.

Formalized by `StatMech.Ising.isingWeight_factor`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#ising-weight-factor).

## First Griffiths inequality (GKS I)

For the ferromagnetic Ising model on a finite graph with
`β ≥ 0` and `h ≥ 0`, every spin correlation is nonnegative: `0 ≤ ⟨σ_A⟩`.

R. B. Griffiths, *Correlations in Ising ferromagnets. I*, J. Math. Phys. 8 (1967); D. G. Kelly
and S. Sherman, *General Griffiths' inequalities on correlations in Ising ferromagnets*, J.
Math. Phys. 9 (1968).

Formalized by `StatMech.Ising.gks_first`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/GKS.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#gks-first).

## Pointwise product of two configurations

The pointwise product of two configurations: spin `σ_y σ'_y` at `y` (`true` when the spins
agree).

Formalized by `StatMech.Ising.xnor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS2.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS2.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#xnor).

## Duplicated-variable involution on configuration pairs

The involution `(σ, q) ↦ (σ, σ q)` of pairs of configurations.

Formalized by `StatMech.Ising.dblFun`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS2.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS2.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#dbl-fun).

## Ginibre's duplicated-variable change of variables

Ginibre's duplicated-variable change of variables `(σ, q) ↦ (σ, σ q)` as an equivalence.

Formalized by `StatMech.Ising.dblEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/GKS2.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS2.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#dbl-equiv).

## Unnormalized second Griffiths inequality

The unnormalized second Griffiths inequality: `Z² (⟨σ_{A ∆ B}⟩ - ⟨σ_A⟩⟨σ_B⟩) ≥ 0`.

Formalized by `StatMech.Ising.unnorm_gks2`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/GKS2.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS2.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#unnorm-gks2).

## Second Griffiths inequality (GKS II)

For the ferromagnetic Ising model on a finite graph
with `β ≥ 0` and `h ≥ 0`, spin correlations are positively correlated: `⟨σ_A⟩ ⟨σ_B⟩ ≤ ⟨σ_A σ_B⟩
= ⟨σ_{A ∆ B}⟩`.

R. B. Griffiths, *Correlations in Ising ferromagnets. I*, J. Math. Phys. 8 (1967); D. G. Kelly
and S. Sherman, *General Griffiths' inequalities on correlations in Ising ferromagnets*, J.
Math. Phys. 9 (1968).

Formalized by `StatMech.Ising.gks_second`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/GKS2.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/GKS2.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#gks-second).

## Energy observable of the Ising model

The energy observable `∑_{e ∈ E(G)} σ_x σ_y + h ∑_x σ_x`, the `β`-derivative of the
log-weight.

Formalized by `StatMech.IsingFK.energyObs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/CorrelationMonotone.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/CorrelationMonotone.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#energy-obs).

## Monotonicity of correlations

**Monotonicity of correlations** (a consequence of the second Griffiths inequality): for `h ≥
0`, every spin correlation `⟨σ_A⟩_{β,h}` is nondecreasing in `β ≥ 0` (Griffiths, J. Math. Phys.
8 (1967)).

Formalized by `StatMech.IsingFK.corr_monotone`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/CorrelationMonotone.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/CorrelationMonotone.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#corr-monotone).

## Boltzmann weight with inhomogeneous couplings and site fields

The Boltzmann weight `exp(∑_{e ∈ E} J_e σ_e + ∑_x h_x σ_x)`.

Formalized by `StatMech.Sharpness.wJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#w-j).

## Partition function with inhomogeneous couplings and site fields

The partition function `∑_σ wJ E J h σ`.

Formalized by `StatMech.Sharpness.ZJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#zj).

## Gibbs expectation with inhomogeneous couplings and site fields

The Gibbs expectation `⟨f⟩_{E,J,h} = ∑_σ f(σ) w(σ) / Z`.

Formalized by `StatMech.Sharpness.expJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#exp-j).

## Griffiths' second inequality for inhomogeneous couplings

Griffiths' second inequality for nonnegative couplings and fields: `⟨σ_A⟩⟨σ_B⟩ ≤ ⟨σ_{A ∆ B}⟩`.
Reference: R. B. Griffiths, "Correlations in Ising ferromagnets I", J. Math. Phys. 8 (1967) 478–483;
J. Ginibre, "General formulation of Griffiths' inequalities", Comm. Math. Phys. 16 (1970) 310–328.
See also `gks_second` (GKS2) for uniform couplings.

Formalized by `StatMech.Sharpness.gks_second_J`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#gks-second-j).

## Griffiths monotonicity of correlations in the edge set

Griffiths monotonicity: adding edges with nonnegative couplings increases every correlation
`⟨σ_A⟩`. Reference: R. B. Griffiths, "Correlations in Ising ferromagnets I", J. Math. Phys. 8 (1967)
478–483.

Formalized by `StatMech.Sharpness.griffiths_mono`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Simon.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#griffiths-mono).

## Edge-removal ratio of partition functions

The edge-removal ratio `ζ(S) = (Z_{E∖S} / Z_E) ∏_{e ∈ S} cosh J_e`.

Formalized by `StatMech.Walls.ghy_zeta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/EdgeRemovalSupermult.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/EdgeRemovalSupermult.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#ghy-zeta).

## Edge-removal weight with hyperbolic sine factors

The weight `ρ(S) = ζ(S) ∏_{e ∈ S} tanh J_e = (Z_{E∖S} / Z_E) ∏_{e ∈ S} sinh J_e`.

Formalized by `StatMech.Walls.ghy_rho`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/EdgeRemovalSupermult.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/EdgeRemovalSupermult.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html#ghy-rho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Griffiths inequalities](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/correlation-inequalities/griffiths-inequalities)
