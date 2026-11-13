---
declaration: section
origin: cited
lean: MathlibExt.Probability.FokkerPlanck.freeEnergy, MathlibExt.Probability.FokkerPlanck.negFlux, MathlibExt.Probability.FokkerPlanck.IsNoFluxSolutionOn, MathlibExt.Probability.FokkerPlanck.hasDerivAt_freeEnergy, MathlibExt.Probability.FokkerPlanck.antitoneOn_freeEnergy, MathlibExt.Probability.FokkerPlanck.hasDerivAt_mass, MathlibExt.Probability.FokkerPlanck.pderiv, MathlibExt.Probability.FokkerPlanck.grad
statement: formalized
proof: formalized
---

# Fokker–Planck equation

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html).

## Free energy of a Fokker–Planck density

The **free energy** `F(t) = ∫ₐᵇ (Ψ p + D p log p) dx` of the density `p(t, ·)` on
`[a, b]` (potential `Ψ`, diffusion coefficient `D`).

Formalized by `MathlibExt.Probability.FokkerPlanck.freeEnergy`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#free-energy).

## Negative probability flux of the Fokker–Planck equation

The (negative) probability flux `p Ψ' + D ∂ₓ p` of the gradient-drift Fokker–Planck
equation at `(t, x)`; the flux itself is `-(p Ψ' + D ∂ₓ p)`.

Formalized by `MathlibExt.Probability.FokkerPlanck.negFlux`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#neg-flux).

## No-flux solution of the gradient-drift Fokker–Planck equation

`p` solves the **gradient-drift Fokker–Planck equation** `∂ₜ p = ∂ₓ (p Ψ' + D ∂ₓ p)` on
`[a, b]` with **zero flux** at both ends, for times `t ∈ I`.

Formalized by `MathlibExt.Probability.FokkerPlanck.IsNoFluxSolutionOn`, a structure declared in [MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#is-no-flux-solution-on).

## Dissipation identity

Let `p` be `C²` in `(t, x)`, positive for times in an open set
`I`, and solve the no-flux gradient-drift Fokker–Planck equation on `[a, b]` for `t ∈ I`, with
`C²` potential `Ψ` (any real `D`). Then for `t ∈ I`,
`F'(t) = -∫ₐᵇ p (Ψ' + D ∂ₓ log p)² dx`. Only the values of `p` on `[a, b]` enter `F`;
positivity is asked of the whole `C²` function `p t` so that `log (p t)` is `C²`.

Formalized by `MathlibExt.Probability.FokkerPlanck.hasDerivAt_freeEnergy`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#has-deriv-at-free-energy).

## Free-energy decay

Under the hypotheses of `hasDerivAt_freeEnergy`, on a convex open
time set `I` the free energy is nonincreasing.

Formalized by `MathlibExt.Probability.FokkerPlanck.antitoneOn_freeEnergy`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#antitone-on-free-energy).

## Mass conservation

If `p` is `C²` and solves the no-flux equation on `[a, b]` for times
in `I` (positivity is not needed), the total mass `∫ₐᵇ p(t, x) dx` has zero time derivative at
every `t ∈ I`.

Formalized by `MathlibExt.Probability.FokkerPlanck.hasDerivAt_mass`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckFreeEnergy.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#has-deriv-at-mass).

## Partial derivative on Euclidean coordinate space

The partial derivative `∂ᵢ f (x) = Df(x) eᵢ` on `Fin n → ℝ`.

Formalized by `MathlibExt.Probability.FokkerPlanck.pderiv`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#pderiv).

## Gradient of a function on Euclidean coordinate space

The gradient `∇f(x) = (∂ᵢ f(x))ᵢ`.

Formalized by `MathlibExt.Probability.FokkerPlanck.grad`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#grad).

## Divergence of a vector field

The divergence `div F (x) = ∑ᵢ ∂ᵢ Fᵢ (x)` of a vector field.

Formalized by `MathlibExt.Probability.FokkerPlanck.divergence`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#divergence).

## Probability flux of a diffusion

The **probability flux** `J = b p - D ∇p` of the diffusion `dX = b dt + √(2D) dW` with
density `p`.

Formalized by `MathlibExt.Probability.FokkerPlanck.flux`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#flux).

## Fokker–Planck operator

The **Fokker–Planck operator** `-div J`: the density evolves by `∂ₜ p = fokkerPlanckOp D b p`,
and `p` is stationary iff this vanishes.

Formalized by `MathlibExt.Probability.FokkerPlanck.fokkerPlanckOp`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#fokker-planck-op).

## Gibbs density

The (unnormalized) **Gibbs density** `e^{-Ψ(x) / D}`.

Formalized by `MathlibExt.Probability.FokkerPlanck.gibbs`, a definition declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#gibbs).

## The Gibbs density has zero flux

**The Gibbs density has zero flux** under the gradient drift `-∇Ψ`: for differentiable `Ψ`,
`D ≠ 0` and any constant `c`, `J = -∇Ψ · c e^{-Ψ/D} - D ∇(c e^{-Ψ/D}) = 0`.

Formalized by `MathlibExt.Probability.FokkerPlanck.flux_gibbs_eq_zero`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#flux-gibbs-eq-zero).

## The Gibbs density is stationary

**The Gibbs density is stationary** for the gradient drift: `-div J = 0`.

Formalized by `MathlibExt.Probability.FokkerPlanck.fokkerPlanckOp_gibbs_eq_zero`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#fokker-planck-op-gibbs-eq-zero).

## A zero-flux density determines the drift

If `p > 0` is differentiable and the
gradient drift `-∇Ψ` has zero flux for `p`, then `∂ᵢ Ψ = -D ∂ᵢ log p`.

Formalized by `MathlibExt.Probability.FokkerPlanck.pderiv_eq_of_flux_eq_zero`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#pderiv-eq-of-flux-eq-zero).

## Identifiability of the potential

Two differentiable potentials whose gradient drifts
both have zero flux for the same positive differentiable density differ by a constant.

Formalized by `MathlibExt.Probability.FokkerPlanck.exists_const_of_flux_eq_zero`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#exists-const-of-flux-eq-zero).

## Flux of the Gibbs density under a rotational gradient drift

The flux of the Gibbs density under the drift `-(∇Ψ + A ∇Ψ)` is the rotational part
`-(A ∇Ψ) e^{-Ψ / D}` (for differentiable `Ψ`, `D ≠ 0`, any matrix `A`).

Formalized by `MathlibExt.Probability.FokkerPlanck.flux_rotational_gibbs`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#flux-rotational-gibbs).

## Rotational drifts share the Gibbs stationary density

**Rotational drifts share the Gibbs stationary density** (non-identifiability): for a
`C²` potential `Ψ`, `D ≠ 0` and an antisymmetric matrix `A` (`Aᵀ = -A`), the drift
`-(∇Ψ + A ∇Ψ)` satisfies `div J = 0` for `p = e^{-Ψ / D}`.

Formalized by `MathlibExt.Probability.FokkerPlanck.divergence_flux_rotational_gibbs`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#divergence-flux-rotational-gibbs).

## An explicit rotational drift with nonzero flux

**An explicit rotational drift with nonzero flux** (our derivation): on `ℝ²` with
`Ψ(x) = (x₀² + x₁²) / 2`, `D = 1` and the rotation generator `A = [[0, 1], [-1, 0]]`, the
drift `-(∇Ψ + A ∇Ψ)` has the Gibbs (standard Gaussian, up to normalization) density as a
stationary density, yet its flux at `(1, 0)` is nonzero, so it is not the gradient drift.

Formalized by `MathlibExt.Probability.FokkerPlanck.exists_rotational_flux_ne_zero`, a theorem declared in [MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Diffusion/FokkerPlanckGradient.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html#exists-rotational-flux-ne-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fokker–Planck equation](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/fokker-planck-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/stochastic-calculus/fokker-planck-equation)
