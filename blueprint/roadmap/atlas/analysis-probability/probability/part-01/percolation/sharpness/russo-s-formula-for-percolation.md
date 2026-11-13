---
declaration: section
origin: cited
lean: StatMech.Percolation.measureProb, StatMech.Percolation.russo_derivative, StatMech.Percolation.russo_formula, StatMech.Percolation.russo_derivative_measure, StatMech.Sharpness.openInd, StatMech.Sharpness.hasDerivAt_prob_eq_pivotalFactor
statement: formalized
proof: formalized
---

# Russo's formula for percolation

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html).

## Probability of an event under Bernoulli product measure

The probability `ℙ_p(A)` of `A` under the Bernoulli(`p`) product measure on `{0, 1}^E` for
`p ∈ [0, 1]`; outside `[0, 1]` it is the polynomial `StatMech.prob p A`, so that the function is
defined on all of `ℝ`.

Formalized by `StatMech.Percolation.measureProb`, a definition declared in [MathlibExt/Probability/Percolation/CylinderDerivative.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/CylinderDerivative.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html#measure-prob).

## Russo's formula

**Russo's formula** (Margulis–Russo): for an increasing event `A` on a finite edge set and
`0 < p < 1`, `p ↦ ℙ_p(A)` has derivative `∑_e ℙ_p(e is pivotal for A)` at `p`.
See also `StatMech.hasDerivAt_prob_eq_sum_pivotalProb` (the polynomial form, for all `p`) and
`StatMech.hasDerivAt_realProb_cylinder_pivotal` (cylinder events on an infinite edge set).

Formalized by `StatMech.Percolation.russo_derivative`, a theorem declared in [MathlibExt/Probability/Percolation/CylinderDerivative.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/CylinderDerivative.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html#russo-derivative).

## Russo's formula

**Russo's formula**, `deriv` form: `d/dp ℙ_p(A) = ∑_e ℙ_p(e is pivotal for A)` for an
increasing event `A` and `0 < p < 1`.

Formalized by `StatMech.Percolation.russo_formula`, a theorem declared in [MathlibExt/Probability/Percolation/CylinderDerivative.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/CylinderDerivative.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html#russo-formula).

## Russo's formula for the Bernoulli product measure

Russo's formula for `p : ℝ≥0`, packaged with the identification of `measureProb A p` with
`(bernoulliProductMeasure p hp).real A`.

Formalized by `StatMech.Percolation.russo_derivative_measure`, a theorem declared in [MathlibExt/Probability/Percolation/CylinderDerivative.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/CylinderDerivative.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html#russo-derivative-measure).

## Real-valued indicator that an edge is open

The indicator `ω_e ∈ {0, 1}` (as a real number) that the edge `e` is open in `ω`.

Formalized by `StatMech.Sharpness.openInd`, a definition declared in [MathlibExt/Probability/Percolation/PivotalFactor.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PivotalFactor.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html#open-ind).

## Russo's formula

**Russo's formula** in pivotal-factor form: for increasing `A` and `0 < p < 1`,
`d/dp ℙ_p(A) = (p(1 - p))⁻¹ ∑_e 𝔼_p[1_A (ω_e - p)]`.

Formalized by `StatMech.Sharpness.hasDerivAt_prob_eq_pivotalFactor`, a theorem declared in [MathlibExt/Probability/Percolation/PivotalFactor.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/PivotalFactor.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html#has-deriv-at-prob-eq-pivotal-factor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Russo's formula for percolation](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/sharpness/russo-s-formula-for-percolation)
