---
declaration: section
origin: cited
lean: ProbabilityTheory.tendsto_taylor_sum_sub, ProbabilityTheory.tendsto_sum_riemann_uniform, ProbabilityTheory.leftPointProcess, ProbabilityTheory.tendsto_lintegral_leftPointProcess_sub_sq, ProbabilityTheory.ElementaryIntegrand.leftPoint, ProbabilityTheory.ElementaryIntegrand.itoIntegral_leftPoint, ProbabilityTheory.ElementaryIntegrand.toProcess_leftPoint, ProbabilityTheory.ito_formula
statement: formalized
proof: formalized
---

# Itô's formula

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html).

## Pathwise Taylor sums and Riemann sums

## Second-order Taylor sums along a continuous path

For `f` of class `C²`, a continuous
path `w`, `t ≥ 0`, and a sequence of mesh counts `ns j → ∞` along which the quadratic sums
`∑_{k < ns j} (w (t (k + 1) / ns j) - w (t k / ns j))²` stay bounded, the telescoped increment
`f (w t) - f (w 0)` minus the second-order Taylor sums
`∑_k (f'(w_k) Δw_k + (1/2) f''(w_k) Δw_k²)` tends to `0`.

Formalized by `ProbabilityTheory.tendsto_taylor_sum_sub`, a theorem declared in [MathlibExt/Probability/ItoFormula.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#tendsto-taylor-sum-sub).

## Left-point Riemann sums of a continuous function

**Left-point Riemann sums of a continuous function** on the uniform partition of `[0, t]`
converge to the integral: `∑_{k < n} g (t k / n) (t / n) → ∫_0^t g` (`t ≥ 0`).

Formalized by `ProbabilityTheory.tendsto_sum_riemann_uniform`, a theorem declared in [MathlibExt/Probability/ItoFormula.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#tendsto-sum-riemann-uniform).

## Left-point step process along a Brownian path

The left-point step process `∑_{k < n} g(B (t k / n)) 1_{(t k / n, t (k + 1) / n]}` of
`u ↦ g (B u)` on the uniform partition of `[0, t]` into `n` cells.

Formalized by `ProbabilityTheory.leftPointProcess`, a definition declared in [MathlibExt/Probability/ItoFormula.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#left-point-process).

## Left-point approximation of a Lipschitz function of Brownian motion

For a pre-Brownian
motion `B` that is jointly measurable in `(u, ω)` and an `L`-Lipschitz `g`, the left-point step
processes of `u ↦ g (B u)` converge to it in `L²(P ⊗ du)` on `(0, t] × Ω`:
`E ∫_0^t |leftPointProcess g B t n u - g (B u)|² du → 0`.

Formalized by `ProbabilityTheory.tendsto_lintegral_leftPointProcess_sub_sq`, a theorem declared in [MathlibExt/Probability/ItoFormula.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#tendsto-lintegral-left-point-process-sub).

## Left-point elementary integrand along a Brownian path

The left-point elementary integrand `∑_{k < n} g(B (t k / n)) 1_{(t k / n, t (k + 1) / n]}`
of `u ↦ g (B u)` on the uniform partition of `[0, t]`, for a measurable `g` bounded by `C` and
an adapted `B`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.leftPoint`, a definition declared in [MathlibExt/Probability/ItoFormula.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#left-point).

## Itô integral of the left-point integrand is the left-point sum

The elementary Itô integral of `leftPoint` at time `t` is the left-point Itô sum
`∑_{k < n} g(B (t k / n)) (B (t (k + 1) / n) - B (t k / n))`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.itoIntegral_leftPoint`, a theorem declared in [MathlibExt/Probability/ItoFormula.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#ito-integral-left-point).

## Process of the left-point integrand is the left-point step process

The process of `leftPoint` is `leftPointProcess`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.toProcess_leftPoint`, a theorem declared in [MathlibExt/Probability/ItoFormula.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#to-process-left-point).

## Itô's formula

**Itô's formula** for Brownian motion: for a Brownian motion `B` adapted to `F` with
increments independent of the past and jointly measurable in `(t, ω)`, and `f` of class `C²`
with `|f'| ≤ C` and `|f''| ≤ C`,
`f(B t) = f(B 0) + ∫_0^t f'(B u) dB u + (1/2) ∫_0^t f''(B u) du` almost surely, for every
`t ≥ 0` (Karatzas–Shreve 1991, Theorem 3.3.3). The last integral is a pathwise Riemann integral;
it is the integral of a continuous function on almost every path.

Formalized by `ProbabilityTheory.ito_formula`, a theorem declared in [MathlibExt/Probability/ItoFormula.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoFormula.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html#ito-formula).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Itô's formula](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-s-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/stochastic-calculus/it-s-formula)
