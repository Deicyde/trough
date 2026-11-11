---
declaration: section
origin: cited
lean: ODE.exists_explicitEuler_localTruncationError_le, MathlibExt.Analysis.ODE.ExplicitEulerWanted.explicit_euler_first_order_convergence, MathlibExt.Analysis.ODE.ExplicitEulerWanted.explicit_euler_local_truncation_error
statement: formalized
proof: formalized
---

# Euler method

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/euler-method/index.html).

## Uniform quadratic bound on the explicit Euler local error

Let $E$ be a real normed
space, let $t_0 < T$ be real numbers, let $f : \mathbb{R} \times E \to E$ be $C^2$, and let
$x : \mathbb{R} \to E$ be differentiable at every $t \in [t_0, T]$ with $x'(t) = f(t, x(t))$.
Then there is a constant $C \ge 0$ such that
$\|x(t + h) - (x(t) + h f(t, x(t)))\| \le C h^2$ for every $h \in (0, T - t_0]$ and every
$t \in [t_0, T]$ with $t + h \le T$.

Formalized by `ODE.exists_explicitEuler_localTruncationError_le`, a theorem declared in [MathlibExt/Analysis/ODE/ExplicitEuler.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/ExplicitEuler.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/euler-method/index.html#exists-explicit-euler-local-truncation-e).

## First-order convergence of the explicit Euler method

Let $E$ be a real Banach space,
let $t_0 < T$, let $x_0 \in E$ and $L \ge 0$, and let $f : \mathbb{R} \times E \to E$ be $C^2$
with $f(t, \cdot)$ $L$-Lipschitz for every $t \in [t_0, T]$. Then there are a function
$x : \mathbb{R} \to E$ with $x(t_0) = x_0$ and $x'(t) = f(t, x(t))$ for every $t \in [t_0, T]$,
and a constant $C$, such that the following holds for every step size $h \in (0, T - t_0]$: if
$(X_n)_{n \in \mathbb{N}}$ is the explicit Euler sequence $X_0 = x_0$,
$X_{n+1} = X_n + h f(t_0 + n h, X_n)$, then $\|X_n - x(t_0 + n h)\| \le C h$ for every
$n \in \mathbb{N}$ with $n h \le T - t_0$.

Proof: clamp the time variable and use global existence for globally Lipschitz right-hand
sides. The local truncation bound and the discrete Grönwall inequality then give the
first-order global estimate.

## Sources

- E. Hairer, S. P. Nørsett and G. Wanner, Solving Ordinary Differential Equations I, 2nd ed., Theorem I.7.3; stable ref https://en.wikipedia.org/wiki/Euler_method.

Formalized by `MathlibExt.Analysis.ODE.ExplicitEulerWanted.explicit_euler_first_order_convergence`, a theorem declared in [MathlibExt/Analysis/ODE/ExplicitEuler.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/ExplicitEuler.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/euler-method/index.html#explicit-euler-first-order-convergence).

## Local truncation error of the explicit Euler method

Let $E$ be a real Banach space, let
$t_0 < T$, let $f : \mathbb{R} \times E \to E$ be $C^2$, let $x_0 \in E$, and let
$x : \mathbb{R} \to E$ satisfy $x(t_0) = x_0$ and $x'(t) = f(t, x(t))$ for every
$t \in [t_0, T]$. Then there is a constant $C$ such that
$\|x(t + h) - (x(t) + h f(t, x(t)))\| \le C h^2$ for every $h \in (0, T - t_0]$ and every
$t \in [t_0, T]$ with $t + h \le T$.

Proof: differentiate the velocity by the chain rule, bound that derivative on the compact time
interval, and apply the mean value inequality twice.

## Sources

- E. Hairer, S. P. Nørsett and G. Wanner, Solving Ordinary Differential Equations I, 2nd ed., Section I.7.

Formalized by `MathlibExt.Analysis.ODE.ExplicitEulerWanted.explicit_euler_local_truncation_error`, a theorem declared in [MathlibExt/Analysis/ODE/ExplicitEuler.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/ExplicitEuler.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/euler-method/index.html#explicit-euler-local-truncation-error).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler method](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/euler-method/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/numerical-analysis/euler-method)
