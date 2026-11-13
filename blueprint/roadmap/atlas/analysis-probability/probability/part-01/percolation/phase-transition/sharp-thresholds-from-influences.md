---
declaration: section
origin: cited
lean: StatMech.BeffaraDC.openEdge, StatMech.BeffaraDC.russoFormula, StatMech.BeffaraDC.influence, StatMech.TwoDim.sth_sharpThreshold, StatMech.TwoDim.ktr_sharpThreshold_via_kkl
statement: formalized
proof: formalized
---

# Sharp thresholds from influences

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html).

## Event that an edge is open

The event `{ω_e = 1}` that the edge `e` is open.

Formalized by `StatMech.BeffaraDC.openEdge`, a definition declared in [MathlibExt/Probability/Percolation/RussoInfluence.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/RussoInfluence.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html#open-edge).

## Russo's formula

**Russo's formula**, covariance form: for increasing `A` and `p ∉ {0, 1}`,
`d/dp ℙ_p(A) = (p(1 - p))⁻¹ ∑_e (ℙ_p(A ∩ {ω_e = 1}) - ℙ_p(ω_e = 1) ℙ_p(A))`.

Formalized by `StatMech.BeffaraDC.russoFormula`, a theorem declared in [MathlibExt/Probability/Percolation/RussoInfluence.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/RussoInfluence.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html#russo-formula).

## Influence of an edge on an event

The influence `I_e^p(A) = ℙ_p(e is pivotal for A)` of the coordinate `e` on the event `A`
under the `p`-biased product measure.

See also `MathlibExt.Analysis.Fourier.BooleanCubeInfluence.boolInfluence`, the influence of a
real function on the uniform Boolean cube (the case `p = 1/2`, in Fourier normalization).

Formalized by `StatMech.BeffaraDC.influence`, a definition declared in [MathlibExt/Probability/Percolation/RussoInfluence.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/RussoInfluence.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html#influence).

## Sharp threshold from influences

If `A` is increasing, `ℙ_{1/2}(A) = 1/2`, and the total
influence `∑_e I_e^p(A)` is at least `M` for all `p ∈ (1/2, q)`, then
`ℙ_q(A) ≥ 1/2 + M (q - 1/2)`.

Formalized by `StatMech.TwoDim.sth_sharpThreshold`, a theorem declared in [MathlibExt/Probability/Percolation/SharpThreshold.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/SharpThreshold.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html#sth-sharp-threshold).

## Sharp threshold from a KKL-type influence inequality

Sharp threshold from a KKL-type inequality: if `ℙ_{1/2}(A) = 1/2` and for all `p ∈ (1/2, q)`
`∑_e I_e^p(A) ≥ C · ℙ_p(A)(1 - ℙ_p(A)) · L'(p)`, `ℙ_p(A)(1 - ℙ_p(A)) ≥ v₀` and `L'(p) ≥ L`, then
`ℙ_q(A) ≥ 1/2 + C v₀ L (q - 1/2)`. The KKL-type inequality is a hypothesis.

Formalized by `StatMech.TwoDim.ktr_sharpThreshold_via_kkl`, a theorem declared in [MathlibExt/Probability/Percolation/SharpThresholdKKL.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/SharpThresholdKKL.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html#ktr-sharp-threshold-via-kkl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sharp thresholds from influences](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/phase-transition/sharp-thresholds-from-influences)
