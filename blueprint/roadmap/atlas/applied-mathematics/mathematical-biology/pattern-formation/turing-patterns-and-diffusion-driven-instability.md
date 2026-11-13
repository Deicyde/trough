---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.TuringPatterns.diffusionMatrix, MathlibExt.Biology.Dynamics.TuringPatterns.modeMatrix, MathlibExt.Biology.Dynamics.TuringPatterns.IsUnstableMode, MathlibExt.Biology.Dynamics.TuringPatterns.fourierMode, MathlibExt.Biology.Dynamics.TuringPatterns.IsLinearizedSolution, MathlibExt.Biology.Dynamics.TuringPatterns.dispersionDet, MathlibExt.Biology.Dynamics.TuringPatterns.criticalWavenumberSq, MathlibExt.Biology.Dynamics.TuringPatterns.bandDiscriminant
statement: formalized
proof: formalized
---

# Turing patterns and diffusion-driven instability

55 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html).

## Diffusion matrix of a two-species system

The diffusion matrix `D = diag(d_u, d_v)` of a two-species reaction-diffusion system.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.diffusionMatrix`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#diffusion-matrix).

## Mode matrix of a linearized reaction-diffusion system

The mode matrix `J - k² D` governing the Fourier mode of wavenumber `k` of the linearized
system `w_t = D w_xx + J w`, where `J` is the Jacobian of the kinetics at the steady state
(convention: `J i j` is the partial derivative of the `i`-th reaction term with respect to the
`j`-th species, so `J = [[f_u, f_v], [g_u, g_v]]`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.modeMatrix`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#mode-matrix).

## Linearly unstable Fourier mode

The Fourier mode of wavenumber `k` is *linearly unstable*: the mode matrix `J - k² D` has
a complex eigenvalue `μ` with `0 < Re μ`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.IsUnstableMode`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-unstable-mode).

## Complex Fourier mode

The complex Fourier mode `w(t, x) = e^{μ t} cos(k x) v` with growth rate `μ`, wavenumber `k`
and amplitude vector `v`. (The real part of a complex solution of the real linear system is a
real solution.)

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.fourierMode`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#fourier-mode).

## Classical solution of the linearized reaction-diffusion system

`w` is a classical solution of the linearized reaction-diffusion system
`w_t = D w_xx + J w` on `ℝ × ℝ`: `w(t, ·)` is twice differentiable with first and second
derivatives `wx`, `wxx`, and `w(·, x)` is differentiable with the prescribed time derivative.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.IsLinearizedSolution`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-linearized-solution).

## Dispersion polynomial

The dispersion polynomial `h(q) = d_u d_v q² - (d_v f_u + d_u g_v) q + det J`, so that
`det (J - k² D) = h(k²)` (`det_modeMatrix`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.dispersionDet`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#dispersion-det).

## Squared critical wavenumber

The squared critical wavenumber `k_c² = (d_v f_u + d_u g_v) / (2 d_u d_v)`, the minimizer
of the dispersion polynomial (meaningful for `d_u, d_v > 0`; division by zero gives `0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.criticalWavenumberSq`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#critical-wavenumber-sq).

## Discriminant of the dispersion polynomial

The discriminant `(d_v f_u + d_u g_v)² - 4 d_u d_v det J` of the dispersion polynomial.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.bandDiscriminant`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#band-discriminant).

## Lower end of the unstable wavenumber band

Lower end `q₋ = (S - √Δ) / (2 d_u d_v)` of the unstable band of squared wavenumbers, where
`S = d_v f_u + d_u g_v` and `Δ = bandDiscriminant` (meaningful when `0 < Δ`, `d_u, d_v > 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.bandLower`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#band-lower).

## Upper end of the unstable wavenumber band

Upper end `q₊ = (S + √Δ) / (2 d_u d_v)` of the unstable band of squared wavenumbers
(meaningful when `0 < Δ`, `d_u, d_v > 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.bandUpper`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#band-upper).

## Neumann wavenumber on an interval

The Neumann wavenumber `k_n = n π / L` of the mode `cos(n π x / L)` on `[0, L]`.
Meaningful only for `0 < L`; at `L = 0` the totalized division gives `0`, so every
labeled Neumann mode collapses to the homogeneous mode.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.neumannWavenumber`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#neumann-wavenumber).

## Trace of the mode matrix

`tr (J - k² D) = tr J - k² (d_u + d_v)`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.trace_modeMatrix`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#trace-mode-matrix).

## Determinant of the mode matrix is the dispersion polynomial

`det (J - k² D) = h(k²)`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.det_modeMatrix`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#det-mode-matrix).

## Routh–Hurwitz for `2 × 2` matrices

A real `2 × 2` matrix has a complex eigenvalue with
positive real part iff its trace is positive or its determinant is negative.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.exists_eigenvalue_re_pos_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#exists-eigenvalue-re-pos-iff).

## Instability criterion for a Fourier mode via trace and determinant

Mode `k` is unstable iff `0 < tr (J - k² D)` or `det (J - k² D) < 0`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.isUnstableMode_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-unstable-mode-iff).

## Dispersion relation

The Fourier mode `e^{μ t} cos(k x) v` is a classical solution of
the linearized system `w_t = D w_xx + J w` iff `(J - k² D) v = μ v`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.fourierMode_isLinearizedSolution_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#fourier-mode-is-linearized-solution-iff).

## Amplitude of a Fourier mode

The amplitude of a Fourier mode: `‖w(t, 0)‖ = e^{Re μ · t} ‖v‖`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.norm_fourierMode_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#norm-fourier-mode-zero).

## Fourier mode is largest at the origin

`‖w(t, 0)‖` is the amplitude of the mode: `‖w(t, x)‖ ≤ ‖w(t, 0)‖` for every `x`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.norm_fourierMode_le`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#norm-fourier-mode-le).

## Fourier mode grows unboundedly iff its growth rate is positive

A nonzero Fourier mode grows without bound iff its growth rate has positive real part.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.tendsto_norm_fourierMode_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#tendsto-norm-fourier-mode-iff).

## A Fourier mode grows iff `J - k² D` has an eigenvalue with positive real part

**A Fourier mode grows iff `J - k² D` has an eigenvalue with positive real part.**

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.isUnstableMode_iff_exists_growing`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-unstable-mode-iff-exists-growing).

## Homogeneous mode is stable for stable kinetics

The homogeneous mode `k = 0` is stable when the kinetics are stable (`tr J < 0`,
`0 < det J`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.not_isUnstableMode_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#not-is-unstable-mode-zero).

## Mode instability iff the dispersion polynomial is negative

If `tr J < 0` and `d_u, d_v ≥ 0`, mode `k` is unstable iff `h(k²) < 0`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.isUnstableMode_iff_dispersionDet_neg`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-unstable-mode-iff-dispersion-det-neg).

## Diffusion-driven instability (Turing 1952)

If the steady state is stable without
diffusion (`tr J < 0`, `0 < det J`), `d_u, d_v ≥ 0`, and `det (J - k² D) < 0`, then the
homogeneous mode is stable while mode `k` is unstable.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.turing_instability`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#turing-instability).

## Minimum value of the dispersion polynomial

The value of the dispersion polynomial at its minimizer:
`h(k_c²) = det J - (d_v f_u + d_u g_v)² / (4 d_u d_v)`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.dispersionDet_criticalWavenumberSq`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#dispersion-det-critical-wavenumber-sq).

## Critical squared wavenumber minimizes the dispersion polynomial

The critical squared wavenumber minimizes the dispersion polynomial over all real `q`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.dispersionDet_criticalWavenumberSq_le`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#dispersion-det-critical-wavenumber-sq-le).

## Turing condition in squared form

The Turing condition in squared form: `2 √(d_u d_v det J) < S` iff `0 < S` and
`4 d_u d_v det J < S²`, where `S = d_v f_u + d_u g_v`. This holds for all real inputs: when
`d_u d_v det J < 0`, `Real.sqrt` returns `0` and both sides reduce to `0 < S`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.two_mul_sqrt_lt_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#two-mul-sqrt-lt-iff).

## Turing's criterion for diffusion-driven instability

For `d_u, d_v > 0` and `0 < det J`, the dispersion polynomial is negative at some
`q ≥ 0` iff `2 √(d_u d_v det J) < d_v f_u + d_u g_v`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.exists_dispersionDet_neg_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#exists-dispersion-det-neg-iff).

## Turing's criterion

If the steady state is stable without diffusion
(`tr J < 0`, `0 < det J`) and `d_u, d_v > 0`, some Fourier mode is unstable iff
`d_v f_u + d_u g_v > 2 √(d_u d_v det J)`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.exists_isUnstableMode_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#exists-is-unstable-mode-iff).

## Critical wavenumber is unstable under Turing's criterion

Under Turing's criterion the critical wavenumber `k_c = √(k_c²)` is itself unstable (and
`0 < k_c²`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.isUnstableMode_sqrt_criticalWavenumberSq`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-unstable-mode-sqrt-critical-wavenumbe).

## Critical wavenumber at the Turing bifurcation threshold

At the bifurcation threshold `d_v f_u + d_u g_v = 2 √(d_u d_v det J)` the critical
squared wavenumber is `k_c² = √(det J / (d_u d_v))` and `h(k_c²) = 0`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.criticalWavenumberSq_of_threshold`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#critical-wavenumber-sq-of-threshold).

## `f_u` and `g_v` have opposite signs

If the steady state is stable without diffusion
and `d_u, d_v ≥ 0`, diffusion-driven instability forces `f_u g_v < 0`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.mul_neg_of_exists_isUnstableMode`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#mul-neg-of-exists-is-unstable-mode).

## The inhibitor diffuses faster

In the activator-inhibitor sign pattern (`u` is the
activator, `0 < f_u`; then `g_v < 0` follows from `tr J < 0`), diffusion-driven instability of a
kinetically stable state forces `d_u < d_v`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.lt_of_exists_isUnstableMode`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#lt-of-exists-is-unstable-mode).

## Dispersion polynomial is negative exactly on the unstable band

For `d_u, d_v > 0`, the dispersion polynomial is negative exactly on the open band
`(q₋, q₊)`, which is nonempty iff the discriminant is positive.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.dispersionDet_neg_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#dispersion-det-neg-iff).

## Neumann modes have zero flux at the boundary

The Neumann mode `cos(k_n x)` has zero flux at both ends of `[0, L]`: the `x`-derivative of
the Fourier mode with wavenumber `k_n = n π / L` vanishes at `x = 0` and `x = L`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.hasDerivAt_fourierMode_neumannWavenumber`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#has-deriv-at-fourier-mode-neumann-wavenu).

## Finite domain

On `[0, L]` with Neumann boundary conditions, if `tr J < 0` and
`d_u, d_v > 0`, mode `n` is unstable iff `k_n² = (n π / L)²` lies in the unstable band
`(q₋, q₊)` (which requires a positive discriminant).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.isUnstableMode_neumannWavenumber_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#is-unstable-mode-neumann-wavenumber-iff).

## Only finitely many Neumann modes are unstable

Only finitely many Neumann modes are unstable on `[0, L]` (for `d_u, d_v, L > 0`, any `J`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.finite_setOf_isUnstableMode_neumannWavenumber`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#finite-set-of-is-unstable-mode-neumann-w).

## Small domains admit no pattern

If the first nonhomogeneous mode already lies beyond the
band, `q₊ ≤ (π / L)²`, then no Neumann mode is unstable on `[0, L]`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.not_isUnstableMode_neumannWavenumber_of_le`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#not-is-unstable-mode-neumann-wavenumber).

## Long intervals have a squared Neumann wavenumber in any given band

Every long enough interval has a squared Neumann wavenumber inside a given nonempty open band
`(qlo, qhi)` with `0 < qhi`: there is `L₀ > 0` such that for all `L ≥ L₀` some `(n π / L)²` lies
in `(qlo, qhi)`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.exists_neumann_mem_band`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#exists-neumann-mem-band).

## Large domains pattern

Under Turing's criterion, every long enough interval `[0, L]` has
an unstable Neumann mode.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.exists_isUnstableMode_neumannWavenumber`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#exists-is-unstable-mode-neumann-wavenumb).

## Schnakenberg reaction kinetics

Schnakenberg's reaction terms `(f, g) = (a - u + u² v, b - u² v)` as a map on
`x = (u, v) : Fin 2 → ℝ`, with source rates `a, b` (biologically `a, b > 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.schnakenberg`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 781](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L781). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#schnakenberg).

## Steady state of the Schnakenberg kinetics

The homogeneous steady state `(u₀, v₀) = (a + b, b / (a + b)²)` of the Schnakenberg
kinetics (meaningful for `a + b ≠ 0`; at `a + b = 0` the division gives the junk `v₀ = 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.schnakenbergSteadyState`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 786](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L786). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#schnakenberg-steady-state).

## Jacobian of the Schnakenberg kinetics at its steady state

The Jacobian of the Schnakenberg kinetics at its steady state,
`[[(b - a) / (a + b), (a + b)²], [-2 b / (a + b), -(a + b)²]]`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.schnakenbergJacobian`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 791](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L791). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#schnakenberg-jacobian).

## Schnakenberg steady state is an equilibrium

`(a + b, b / (a + b)²)` is a steady state of the Schnakenberg kinetics when `a + b ≠ 0`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.schnakenberg_steadyState`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 795](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L795). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#schnakenberg-steady-state-2).

## Computation of the Schnakenberg Jacobian at the steady state

The Jacobian matrix of the Schnakenberg kinetics at the steady state is
`schnakenbergJacobian a b`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.jacobianMatrix_schnakenberg`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 802](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L802). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#jacobian-matrix-schnakenberg).

## Determinant of the Schnakenberg Jacobian

`det J = (a + b)²` for the Schnakenberg Jacobian (`a + b ≠ 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.det_schnakenbergJacobian`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 827](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L827). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#det-schnakenberg-jacobian).

## Stability of the Schnakenberg steady state without diffusion

The Schnakenberg steady state is stable without diffusion iff `b - a < (a + b)³`
(for `0 < a + b`; then `0 < det J` automatically).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.trace_schnakenbergJacobian_neg_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 835](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L835). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#trace-schnakenberg-jacobian-neg-iff).

## Turing instability of the Schnakenberg kinetics

**Turing instability of the Schnakenberg kinetics** (Murray 2003, ch. 2). With
`d_u = 1`, `d_v = d > 0`, `0 < a + b` and `b - a < (a + b)³` (stable without diffusion), some
Fourier mode is unstable iff `2 √d (a + b)² < d (b - a) - (a + b)³`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.schnakenberg_turing_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 845](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L845). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#schnakenberg-turing-iff).

## Gierer–Meinhardt activator-inhibitor kinetics

Gierer–Meinhardt activator-inhibitor kinetics in Murray's nondimensional form
`(f, g) = (a - b u + u² / v, u² - v)` on `x = (u, v)` (biologically `a, b > 0` and `u, v > 0`;
at `v = 0` the division gives the junk `u² / 0 = 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.giererMeinhardt`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 868](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L868). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#gierer-meinhardt).

## Steady state of the Gierer–Meinhardt kinetics

The homogeneous steady state `(u₀, v₀) = ((a + 1) / b, ((a + 1) / b)²)` of the
Gierer–Meinhardt kinetics (meaningful for `b ≠ 0`, `a + 1 ≠ 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.giererMeinhardtSteadyState`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 873](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L873). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#gierer-meinhardt-steady-state).

## Jacobian of the Gierer–Meinhardt kinetics at its steady state

The Jacobian of the Gierer–Meinhardt kinetics at its steady state,
`[[b (1 - a) / (1 + a), -(b / (a + 1))²], [2 (a + 1) / b, -1]]`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.giererMeinhardtJacobian`, a definition declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 878](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L878). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#gierer-meinhardt-jacobian).

## Gierer–Meinhardt steady state is an equilibrium

`((a + 1) / b, ((a + 1) / b)²)` is a steady state of the Gierer–Meinhardt kinetics when
`a + 1 ≠ 0` and `b ≠ 0`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.giererMeinhardt_steadyState`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 883](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L883). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#gierer-meinhardt-steady-state-2).

## Computation of the Gierer–Meinhardt Jacobian at the steady state

The Jacobian matrix of the Gierer–Meinhardt kinetics at the steady state is
`giererMeinhardtJacobian a b`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.jacobianMatrix_giererMeinhardt`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#jacobian-matrix-gierer-meinhardt).

## Determinant of the Gierer–Meinhardt Jacobian

`det J = b` for the Gierer–Meinhardt Jacobian (`a + 1 ≠ 0`, `b ≠ 0`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.det_giererMeinhardtJacobian`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 924](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L924). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#det-gierer-meinhardt-jacobian).

## Stability of the Gierer–Meinhardt steady state without diffusion

The Gierer–Meinhardt steady state is stable without diffusion iff `b (1 - a) < 1 + a`
(for `0 < a + 1`; then `0 < det J = b` for `0 < b`).

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.trace_giererMeinhardtJacobian_neg_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 933](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L933). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#trace-gierer-meinhardt-jacobian-neg-iff).

## Turing instability of the Gierer–Meinhardt kinetics

With `d_u = 1`, `d_v = d > 0`,
`0 < a + 1`, `0 < b` and `b (1 - a) < 1 + a` (stable without diffusion), some Fourier mode is
unstable iff `2 √(d b) < d b (1 - a) / (1 + a) - 1`.

Formalized by `MathlibExt.Biology.Dynamics.TuringPatterns.giererMeinhardt_turing_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/TuringPatterns.lean, line 944](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/TuringPatterns.lean#L944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html#gierer-meinhardt-turing-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turing patterns and diffusion-driven instability](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/pattern-formation/turing-patterns-and-diffusion-driven-instability)
