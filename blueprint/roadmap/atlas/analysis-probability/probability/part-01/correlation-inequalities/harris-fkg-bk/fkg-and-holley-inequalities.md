---
declaration: section
origin: cited
lean: StatMech.fkg_inequality, StatMech.fkg_inequality_events, StatMech.holley_dominates, StatMech.FK.measOfMass, StatMech.FK.measOfMass_eq_toMeasure, StatMech.FK.holley_stochasticallyDominated, StatMech.FK.holley_exists_monotoneCoupling
statement: formalized
proof: formalized
---

# FKG and Holley inequalities

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html).

## FKG inequality

The **FKG inequality** (Fortuin, Kasteleyn, Ginibre 1971). Let `π` be a probability weight on
`ConfigSpace E` (`π ≥ 0`, `∑ π = 1`) satisfying the FKG lattice condition. Then any two monotone
functions `f g : ConfigSpace E → ℝ` are positively correlated:
`E_π[f] * E_π[g] ≤ E_π[f * g]`.

See also Mathlib's `fkg`, which assumes `f, g ≥ 0` and does not normalize `π`; this version
removes the sign condition by shifting `f` and `g` by their values at `⊥`.

Formalized by `StatMech.fkg_inequality`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/FKG.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/FKG.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#fkg-inequality).

## FKG inequality for increasing events

The **FKG inequality for events**: under a probability weight `π` satisfying the FKG lattice
condition, two increasing events are positively correlated, `π(A) * π(B) ≤ π(A ∩ B)`.

Formalized by `StatMech.fkg_inequality_events`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/FKG.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/FKG.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#fkg-inequality-events).

## Holley inequality for increasing events

The **Holley inequality** for increasing events (Holley 1974). If `μ₁, μ₂ ≥ 0` have equal
total mass and satisfy `μ₁ a * μ₂ b ≤ μ₁ (a ⊓ b) * μ₂ (a ⊔ b)`, then `μ₁(A) ≤ μ₂(A)` for every
increasing event `A`. This is Mathlib's `holley` applied to the indicator of `A`.

Formalized by `StatMech.holley_dominates`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/FKG.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/FKG.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#holley-dominates).

## Finite measure with prescribed point masses

The finite measure `∑_ω μ(ω) δ_ω` on `ConfigSpace E` with point masses `μ(ω)` (negative
masses are truncated to `0`). For a normalized nonnegative `μ` it is the measure of the `PMF`
`PMF.ofFintype μ`; see `measOfMass_eq_toMeasure`.

Formalized by `StatMech.FK.measOfMass`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#meas-of-mass).

## Normalized point masses give the probability mass function's measure

For a normalized nonnegative mass function, `measOfMass μ` is the measure of the `PMF`
`PMF.ofFintype (ENNReal.ofReal ∘ μ)`.

Formalized by `StatMech.FK.measOfMass_eq_toMeasure`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#meas-of-mass-eq-to-measure).

## Holley's inequality

If `μ₁, μ₂ ≥ 0` on `{0,1}^E` have equal total mass and satisfy
the Holley lattice condition `μ₁(a) μ₂(b) ≤ μ₁(a ∧ b) μ₂(a ∨ b)`, then `measOfMass μ₁` is
stochastically dominated by `measOfMass μ₂`. Strict positivity, assumed in Holley's paper, is not
needed. See R. Holley, *Remarks on the FKG inequalities*, Comm. Math. Phys. 36 (1974); the
real-valued form is `StatMech.holley_dominates`, from Mathlib's `holley`.

Formalized by `StatMech.FK.holley_stochasticallyDominated`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#holley-stochastically-dominated).

## Holley's coupling theorem

If `μ₁, μ₂` are strictly positive probability mass functions
on `{0,1}^E` satisfying the Holley lattice condition `μ₁(a) μ₂(b) ≤ μ₁(a ∧ b) μ₂(a ∨ b)`, there
is a finite measure on pairs with marginals `measOfMass μ₁` and `measOfMass μ₂`, concentrated on
`{(a, b) | a ≤ b}`. See R. Holley, *Remarks on the FKG inequalities*, Comm. Math. Phys. 36
(1974), and G. Grimmett, *The Random-Cluster Model* (2006), Chapter 2.

Formalized by `StatMech.FK.holley_exists_monotoneCoupling`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/HolleyCoupling.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html#holley-exists-monotone-coupling).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: FKG and Holley inequalities](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/harris-fkg-bk/fkg-and-holley-inequalities)
