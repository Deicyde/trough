---
declaration: section
origin: cited
lean: Matrix.IsHurwitz.exists_norm_exp_smul_mulVec_le, MathlibExt.Analysis.ODE.LinearizedStability.globalSolution_decay_of_hasFDerivAt, MathlibExt.Analysis.LinearStabilityWanted.Analysis.ODE.linear_ode_asymptotic_stability, MathlibExt.Analysis.ODE.LinearizedInstabilityWanted.exists_unstable_of_hasFDerivAt
statement: formalized
---

# Lyapunov's indirect method

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method/index.html).

## Exponential decay of a Hurwitz semigroup

If `A` is Hurwitz, there are `M, α > 0`
with `‖exp(t A) v‖ ≤ M e^{-α t} ‖v‖` for all `t ≥ 0` and all vectors `v`.

Formalized by `Matrix.IsHurwitz.exists_norm_exp_smul_mulVec_le`, a theorem declared in [MathlibExt/Analysis/ODE/LinearizedStability.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/LinearizedStability.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method/index.html#exists-norm-exp-smul-mul-vec-le).

## Lyapunov's indirect method (linearized stability), conditional decay form

Let
`f (x⋆) = 0` and let `f` be differentiable at `x⋆` with Jacobian matrix `A`. If `A` is Hurwitz,
then for some `δ, C, α > 0`, every solution of `x' = f(x)` on `[0, ∞)` with
`‖x(0) - x⋆‖ < δ` satisfies `‖x(t) - x⋆‖ ≤ C e^{-α t} ‖x(0) - x⋆‖` for all `t ≥ 0`.
This is conditional on the solution being defined on all of `[0, ∞)`; it does not assert
solution existence, so it is not by itself local exponential stability (Khalil 2002,
Theorem 4.7, which assumes `f` is `C¹` and concludes asymptotic stability).

Formalized by `MathlibExt.Analysis.ODE.LinearizedStability.globalSolution_decay_of_hasFDerivAt`, a theorem declared in [MathlibExt/Analysis/ODE/LinearizedStability.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/LinearizedStability.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method/index.html#global-solution-decay-of-has-fderiv-at).

## Asymptotic stability of linear ODEs with eigenvalues in the open left half-plane

Let
$n \ge 0$ and let $A$ be a real $n \times n$ matrix such that every complex eigenvalue $\mu$ of $A$
(an eigenvalue of $A$ viewed as a complex matrix acting on $\mathbb{C}^n$) satisfies
$\operatorname{Re} \mu < 0$. Let $x : \mathbb{R} \to \mathbb{R}^n$ be a function that, at every
$t > 0$, is differentiable with derivative $x'(t) = A\,x(t)$. Then $\|x(t)\| \to 0$ as
$t \to \infty$, where $\|\cdot\|$ is the sup norm on $\mathbb{R}^n$.

## Sources

- Classical linear stability theory; Hirsch-Smale-Devaney. Problem `linear_ode_asymptotic_stability` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.LinearStabilityWanted.Analysis.ODE.linear_ode_asymptotic_stability` is written with `theorem_wanted` in [WantedExt/Analysis/LinearStabilityWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/LinearStabilityWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method/index.html#linear-ode-asymptotic-stability).

## Lyapunov's indirect method, instability

**Lyapunov's indirect method, instability** (Khalil 2002, Theorem 4.7). If `f` is `C¹`,
`f x⋆ = 0`, and the Jacobian matrix `A` of `f` at `x⋆` has an eigenvalue with positive real
part, then `x⋆` is unstable: for some `ε > 0`, every neighbourhood of `x⋆` contains an initial
point `x₀` from which a solution segment of `x' = f(x)` on some finite interval `[0, T]`
reaches distance `≥ ε` from `x⋆`. Quantifying over finite segments (rather than only over
solutions on all of `[0, ∞)`) keeps the statement non-vacuous when solutions blow up in
finite time.

Stated but not proved: `MathlibExt.Analysis.ODE.LinearizedInstabilityWanted.exists_unstable_of_hasFDerivAt` is written with `theorem_wanted` in [WantedExt/Analysis/ODE/LinearizedInstabilityWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ODE/LinearizedInstabilityWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method/index.html#exists-unstable-of-has-fderiv-at).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lyapunov's indirect method](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/ordinary-differential-equations/lyapunov-s-indirect-method)
